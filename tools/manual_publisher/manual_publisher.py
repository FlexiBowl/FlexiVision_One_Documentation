from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import time
import zipfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import escape
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote

FULL_MANUAL_PDF_NAME = "manual_full.pdf"
PRINT_FULL_MANUAL_HTML_NAME = "print_full_manual.html"
OFFLINE_MANUAL_ZIP_NAME = "Offline manual.zip"
LEGACY_OFFLINE_MANUAL_ZIP_NAME = "client_site_bundle.zip"
SHARED_BUILD_MEDIA_ROOT = Path("_shared") / "media"
VIDEO_FILE_EXTENSIONS = {".mp4", ".mov", ".webm", ".m4v", ".ogv"}
HTML_BUILD_WORKERS_ENV = "FV_HTML_WORKERS"
COPY_WORKERS_ENV = "FV_COPY_WORKERS"
HTML_BUILD_WORKER_CAP = 4
COPY_WORKER_CAP = 4
HTML_COPY_IGNORE = shutil.ignore_patterns(".doctrees")
MEDIA_REFERENCE_PATTERN = re.compile(
    r'(?P<prefix>\b(?:src|href|poster)=["\'])'
    r'(?P<url>(?:\.\./)*_images/[^"\'?#]+)'
    r'(?P<suffix>(?:[?#][^"\']*)?)'
    r'(?P<quote>["\'])'
)
STATIC_REFERENCE_PATTERN = re.compile(
    r'(?P<prefix>\b(?:src|href)=["\'])'
    r'(?P<url>(?:\.\./)*(?:_static|_sphinx_design_static)/[^"\'?#]+)'
    r'(?P<suffix>(?:[?#][^"\']*)?)'
    r'(?P<quote>["\'])'
)
RELEASE_ARTIFACT_NAMES = {
    FULL_MANUAL_PDF_NAME,
    PRINT_FULL_MANUAL_HTML_NAME,
    OFFLINE_MANUAL_ZIP_NAME,
    LEGACY_OFFLINE_MANUAL_ZIP_NAME,
}


def format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.2f}s"

    minutes, remaining_seconds = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}m {remaining_seconds:04.1f}s"

    hours, remaining_minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(remaining_minutes)}m {remaining_seconds:04.1f}s"


def log_timing(message: str) -> None:
    print(f"[timing] {message}")


@contextlib.contextmanager
def timed_step(label: str, timings: list[tuple[str, float]] | None = None, *, record: bool = True):
    log_timing(f"Starting {label}")
    started_at = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - started_at
        if timings is not None and record:
            timings.append((label, elapsed))
        log_timing(f"Finished {label} in {format_duration(elapsed)}")


def print_timing_summary(timings: list[tuple[str, float]], overall_duration: float) -> None:
    print("")
    print("Build timing summary (slowest recorded steps first):")
    if not timings:
        print(f"  total wall time: {format_duration(overall_duration)}")
        return

    label_width = max(len(label) for label, _ in timings)
    for label, elapsed in sorted(timings, key=lambda item: item[1], reverse=True):
        print(f"  {label.ljust(label_width)}  {format_duration(elapsed)}")
    print(f"  {'TOTAL WALL TIME'.ljust(label_width)}  {format_duration(overall_duration)}")


def resolve_worker_count(env_var: str, worker_cap: int, task_count: int) -> int:
    if task_count <= 1:
        return 1

    configured_value = os.environ.get(env_var, "").strip()
    if configured_value:
        try:
            requested_workers = max(1, int(configured_value))
        except ValueError:
            requested_workers = 1
    else:
        requested_workers = max(1, min(worker_cap, os.cpu_count() or 1))

    return max(1, min(task_count, requested_workers))


def run_parallel_tasks(
    stage_label: str,
    task_specs: list[dict[str, object]],
    worker_fn,
    timings: list[tuple[str, float]] | None,
    *,
    env_var: str,
    worker_cap: int,
) -> None:
    if not task_specs:
        return

    worker_count = resolve_worker_count(env_var, worker_cap, len(task_specs))
    log_timing(f"Using {worker_count} worker(s) for {stage_label} across {len(task_specs)} task(s).")

    errors: list[str] = []

    def handle_result(result: tuple[str, float, str]) -> None:
        label, elapsed, detail = result
        if timings is not None:
            timings.append((label, elapsed))
        suffix = f" [{detail}]" if detail else ""
        log_timing(f"Finished {label} in {format_duration(elapsed)}{suffix}")

    if worker_count == 1:
        for task_spec in task_specs:
            try:
                handle_result(worker_fn(task_spec))
            except Exception as exc:
                errors.append(f"{task_spec['label']}: {exc}")
    else:
        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            future_map = {executor.submit(worker_fn, task_spec): task_spec for task_spec in task_specs}
            for future in as_completed(future_map):
                task_spec = future_map[future]
                try:
                    handle_result(future.result())
                except Exception as exc:
                    errors.append(f"{task_spec['label']}: {exc}")

    if errors:
        raise RuntimeError("\n\n".join(errors))


def handle_remove_readonly(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clear_directory(path: Path) -> bool:
    if path.exists():
        try:
            shutil.rmtree(path, onexc=handle_remove_readonly)
        except PermissionError:
            return False
    path.mkdir(parents=True, exist_ok=True)
    return True


def remove_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path, onexc=handle_remove_readonly)


def sync_directory(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for root, _, files in os.walk(source):
        source_dir = Path(root)
        relative_dir = source_dir.relative_to(source)
        destination_dir = destination / relative_dir
        destination_dir.mkdir(parents=True, exist_ok=True)
        for file_name in files:
            source_file = source_dir / file_name
            destination_file = destination_dir / file_name
            try:
                shutil.copy2(source_file, destination_file)
            except PermissionError:
                print(f"Skipping locked file during sync: {destination_file}")


def merge_directory(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(source):
        source_dir = Path(root)
        relative_dir = source_dir.relative_to(source)
        destination_dir = destination / relative_dir
        destination_dir.mkdir(parents=True, exist_ok=True)
        for directory_name in dirs:
            (destination_dir / directory_name).mkdir(parents=True, exist_ok=True)
        for file_name in files:
            source_file = source_dir / file_name
            destination_file = destination_dir / file_name
            shutil.copy2(source_file, destination_file)


def mirror_directory(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)

    source_dirs = {Path(".")}
    source_files: set[Path] = set()

    for root, dirs, files in os.walk(source):
        source_dir = Path(root)
        relative_dir = source_dir.relative_to(source)
        source_dirs.add(relative_dir)
        destination_dir = destination / relative_dir
        destination_dir.mkdir(parents=True, exist_ok=True)

        for directory_name in dirs:
            directory_relative = relative_dir / directory_name if relative_dir != Path(".") else Path(directory_name)
            source_dirs.add(directory_relative)
            (destination / directory_relative).mkdir(parents=True, exist_ok=True)

        for file_name in files:
            relative_file = relative_dir / file_name if relative_dir != Path(".") else Path(file_name)
            source_files.add(relative_file)
            destination_file = destination / relative_file
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_dir / file_name, destination_file)

    if not destination.exists():
        return

    existing_items = sorted(
        destination.rglob("*"),
        key=lambda path: len(path.relative_to(destination).parts),
        reverse=True,
    )

    for item in existing_items:
        relative_item = item.relative_to(destination)
        if item.is_file():
            if relative_item not in source_files:
                item.unlink()
            continue

        if relative_item not in source_dirs:
            remove_directory(item)


def remove_named_files(root: Path, names: set[str]) -> None:
    if not root.exists():
        return

    for item in root.rglob("*"):
        if not item.is_file() or item.name not in names:
            continue
        try:
            item.unlink()
        except PermissionError:
            print(f"Skipping locked generated artifact during cleanup: {item}")


def create_site_zip(source_root: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for item in source_root.rglob("*"):
            if not item.is_file():
                continue
            if item.resolve() == zip_path.resolve():
                continue
            archive.write(item, item.relative_to(source_root))


def list_version_paths(source_root: Path) -> list[Path]:
    return sorted(path for path in source_root.iterdir() if path.is_dir() and not path.name.startswith("_"))


def list_language_paths(version_path: Path) -> list[Path]:
    return sorted(path for path in version_path.iterdir() if path.is_dir() and not path.name.startswith("_"))


def build_source_catalog(source_root: Path) -> list[tuple[str, list[str]]]:
    catalog = []
    versions = sorted(list_version_paths(source_root), key=lambda path: version_sort_key(path.name), reverse=True)
    for version_path in versions:
        languages = sorted([path.name for path in list_language_paths(version_path)], key=language_sort_key)
        catalog.append((version_path.name, languages))
    return catalog


def build_version_manifest(catalog: list[tuple[str, list[str]]]) -> str:
    payload = {
        "versions": [version for version, _ in catalog],
        "languagesByVersion": {version: languages for version, languages in catalog},
        "defaultLanguageByVersion": {
            version: choose_preferred_language(languages)
            for version, languages in catalog
            if languages
        },
    }
    return "window.FV_VERSIONING = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"


def write_site_version_manifest(site_root: Path, catalog: list[tuple[str, list[str]]] | None = None) -> None:
    if not site_root.exists():
        return

    manifest = build_version_manifest(catalog or build_catalog(site_root))
    static_dirs: set[Path] = set()

    shared_static_dir = site_root / "_shared" / "static"
    if shared_static_dir.exists():
        static_dirs.add(shared_static_dir)

    for version_path in list_version_paths(site_root):
        for language_path in list_language_paths(version_path):
            static_dir = language_path / "_static"
            if static_dir.exists():
                static_dirs.add(static_dir)

    for static_dir in static_dirs:
        static_dir.mkdir(parents=True, exist_ok=True)
        (static_dir / "versioning-data.js").write_text(manifest, encoding="utf-8")


def ensure_nojekyll(site_root: Path) -> None:
    if not site_root.exists():
        return

    (site_root / ".nojekyll").write_text("", encoding="utf-8")


def remove_target_scope(output_root: Path, target_version: str | None, target_language: str | None) -> None:
    if not output_root.exists():
        return

    if target_version and target_language:
        remove_directory(output_root / target_version / target_language)
        version_dir = output_root / target_version
        if version_dir.exists() and not any(version_dir.iterdir()):
            version_dir.rmdir()
        return

    if target_version:
        remove_directory(output_root / target_version)
        return

    if target_language:
        for version_path in list_version_paths(output_root):
            remove_directory(version_path / target_language.upper())


def configure_footer_features(
    temp_root: Path,
    *,
    enable_offline_zip: bool,
) -> None:
    footer_path = temp_root / "data" / "footer.html"
    if not footer_path.exists():
        return

    footer = footer_path.read_text(encoding="utf-8")
    footer = footer.replace("{offline_zip_enabled}", "true" if enable_offline_zip else "false")
    footer_path.write_text(footer, encoding="utf-8")


def configure_release_download_flags(site_root: Path) -> None:
    zip_available = (site_root / OFFLINE_MANUAL_ZIP_NAME).exists()

    for version_path in list_version_paths(site_root):
        for language_path in list_language_paths(version_path):
            for html_file in language_path.rglob("*.html"):
                content = html_file.read_text(encoding="utf-8")
                updated = re.sub(
                    r"const offlineZipEnabled = (true|false);",
                    f"const offlineZipEnabled = {'true' if zip_available else 'false'};",
                    content,
                    count=1,
                )
                if updated != content:
                    html_file.write_text(updated, encoding="utf-8")


def hash_file(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_href_from_path(path: Path) -> str:
    return "/".join(quote(part) for part in path.parts)


def hash_directory(directory: Path) -> tuple[str, tuple[str, ...]]:
    signature_entries = []
    for file_path in sorted(path for path in directory.rglob("*") if path.is_file()):
        relative_path = file_path.relative_to(directory).as_posix()
        signature_entries.append(f"{relative_path}|{hash_file(file_path)}")

    signature_payload = "\n".join(signature_entries).encode("utf-8")
    signature_digest = hashlib.sha256(signature_payload).hexdigest()
    return signature_digest, tuple(signature_entries)


def pick_shared_media_target(shared_root: Path, sample_path: Path, digest: str) -> Path:
    media_bucket = "videos" if sample_path.suffix.lower() in VIDEO_FILE_EXTENSIONS else "images"
    target_dir = shared_root / media_bucket
    target_dir.mkdir(parents=True, exist_ok=True)

    candidate = target_dir / sample_path.name
    if candidate.exists():
        if hash_file(candidate) == digest:
            return candidate
        candidate = target_dir / f"{sample_path.stem}-{digest[:12]}{sample_path.suffix}"

    counter = 2
    while candidate.exists():
        if hash_file(candidate) == digest:
            return candidate
        candidate = target_dir / f"{sample_path.stem}-{digest[:12]}-{counter}{sample_path.suffix}"
        counter += 1

    return candidate


def rewrite_shared_media_references(html_file: Path, shared_targets_by_source: dict[Path, Path]) -> bool:
    original_content = html_file.read_text(encoding="utf-8")

    def replace_reference(match: re.Match[str]) -> str:
        encoded_url = match.group("url")
        suffix = match.group("suffix") or ""
        url_path = PurePosixPath(unquote(encoded_url))
        source_path = (html_file.parent / Path(*url_path.parts)).resolve()
        shared_target = shared_targets_by_source.get(source_path)
        if shared_target is None:
            return match.group(0)

        relative_target = Path(os.path.relpath(shared_target, html_file.parent))
        relative_href = build_href_from_path(relative_target)
        return f"{match.group('prefix')}{relative_href}{suffix}{match.group('quote')}"

    updated_content = MEDIA_REFERENCE_PATTERN.sub(replace_reference, original_content)
    if updated_content == original_content:
        return False

    html_file.write_text(updated_content, encoding="utf-8")
    return True


def rewrite_shared_static_references(html_file: Path, shared_targets_by_source: dict[Path, Path]) -> bool:
    original_content = html_file.read_text(encoding="utf-8")

    def replace_reference(match: re.Match[str]) -> str:
        encoded_url = match.group("url")
        suffix = match.group("suffix") or ""
        url_path = PurePosixPath(unquote(encoded_url))
        source_path = (html_file.parent / Path(*url_path.parts)).resolve()
        shared_target = shared_targets_by_source.get(source_path)
        if shared_target is None:
            return match.group(0)

        relative_target = Path(os.path.relpath(shared_target, html_file.parent))
        relative_href = build_href_from_path(relative_target)
        return f"{match.group('prefix')}{relative_href}{suffix}{match.group('quote')}"

    updated_content = STATIC_REFERENCE_PATTERN.sub(replace_reference, original_content)
    if updated_content == original_content:
        return False

    html_file.write_text(updated_content, encoding="utf-8")
    return True


def optimize_shared_media(build_root: Path) -> None:
    duplicate_groups: dict[str, list[Path]] = defaultdict(list)

    for version_path in list_version_paths(build_root):
        for language_path in list_language_paths(version_path):
            images_root = language_path / "_images"
            if not images_root.exists():
                continue
            for asset_path in images_root.rglob("*"):
                if asset_path.is_file():
                    duplicate_groups[hash_file(asset_path)].append(asset_path)

    shared_targets_by_source: dict[Path, Path] = {}
    duplicate_group_count = 0
    removable_bytes = 0
    shared_root = build_root / SHARED_BUILD_MEDIA_ROOT

    for digest, file_paths in duplicate_groups.items():
        if len(file_paths) < 2:
            continue

        target_path = pick_shared_media_target(shared_root, file_paths[0], digest)
        if not target_path.exists():
            shutil.copy2(file_paths[0], target_path)

        duplicate_group_count += 1
        file_size = file_paths[0].stat().st_size
        removable_bytes += file_size * (len(file_paths) - 1)

        resolved_target_path = target_path.resolve()
        for file_path in file_paths:
            shared_targets_by_source[file_path.resolve()] = resolved_target_path

    if not shared_targets_by_source:
        return

    updated_html_files = 0
    for version_path in list_version_paths(build_root):
        for language_path in list_language_paths(version_path):
            for html_file in language_path.rglob("*.html"):
                if rewrite_shared_media_references(html_file, shared_targets_by_source):
                    updated_html_files += 1

    removed_files = 0
    for source_path in shared_targets_by_source:
        try:
            Path(source_path).unlink()
            removed_files += 1
        except PermissionError:
            print(f"Skipping locked duplicate media during optimization: {source_path}")

    for version_path in list_version_paths(build_root):
        for language_path in list_language_paths(version_path):
            images_root = language_path / "_images"
            if images_root.exists() and not any(images_root.iterdir()):
                images_root.rmdir()

    print(
        "Optimized shared media: consolidated "
        f"{duplicate_group_count} duplicate asset groups into '{SHARED_BUILD_MEDIA_ROOT.as_posix()}', "
        f"updated {updated_html_files} HTML files, and removed {removed_files} duplicate files "
        f"(about {removable_bytes / (1024 * 1024):.1f} MiB saved)."
    )


def optimize_shared_static_directories(build_root: Path) -> None:
    shared_directory_roots = {
        "_static": Path("_shared") / "static",
        "_sphinx_design_static": Path("_shared") / "sphinx_design_static",
    }
    shared_targets_by_source: dict[Path, Path] = {}
    source_directories_to_remove: set[Path] = set()
    consolidated_group_count = 0
    removed_directory_count = 0
    removable_bytes = 0
    shared_target_dirs: set[Path] = set()

    for directory_name, shared_relative_root in shared_directory_roots.items():
        candidate_directories: list[Path] = []
        for version_path in list_version_paths(build_root):
            for language_path in list_language_paths(version_path):
                static_dir = language_path / directory_name
                if static_dir.exists():
                    candidate_directories.append(static_dir)

        signature_groups: dict[tuple[str, tuple[str, ...]], list[Path]] = defaultdict(list)
        for directory in candidate_directories:
            signature_groups[hash_directory(directory)].append(directory)

        for (signature_digest, signature_entries), directories in signature_groups.items():
            if len(directories) < 2:
                continue

            target_dir = build_root / shared_relative_root
            if target_dir.exists():
                existing_signature = hash_directory(target_dir)
                if existing_signature != (signature_digest, signature_entries):
                    target_dir = build_root / "_shared" / f"{shared_relative_root.name}-{signature_digest[:12]}"

            if not target_dir.exists():
                shutil.copytree(directories[0], target_dir)
            shared_target_dirs.add(target_dir)

            consolidated_group_count += 1
            for directory in directories:
                source_directories_to_remove.add(directory.resolve())
                for file_path in directory.rglob("*"):
                    if not file_path.is_file():
                        continue
                    relative_path = file_path.relative_to(directory)
                    shared_targets_by_source[file_path.resolve()] = (target_dir / relative_path).resolve()
                    removable_bytes += file_path.stat().st_size

    if not shared_targets_by_source:
        return

    updated_html_files = 0
    for version_path in list_version_paths(build_root):
        for language_path in list_language_paths(version_path):
            for html_file in language_path.rglob("*.html"):
                if rewrite_shared_static_references(html_file, shared_targets_by_source):
                    updated_html_files += 1

    for directory_name in shared_directory_roots:
        for version_path in list_version_paths(build_root):
            for language_path in list_language_paths(version_path):
                source_dir = language_path / directory_name
                if not source_dir.exists() or source_dir.resolve() not in source_directories_to_remove:
                    continue
                remove_directory(source_dir)
                removed_directory_count += 1

    redundant_sphinx_design_root = build_root / "_shared" / "sphinx_design_static"
    shared_static_root = build_root / "_shared" / "static"
    if redundant_sphinx_design_root.exists():
        can_remove = True
        for file_path in redundant_sphinx_design_root.rglob("*"):
            if not file_path.is_file():
                continue
            equivalent_path = shared_static_root / file_path.relative_to(redundant_sphinx_design_root)
            if not equivalent_path.exists() or hash_file(equivalent_path) != hash_file(file_path):
                can_remove = False
                break
        if can_remove:
            remove_directory(redundant_sphinx_design_root)
            shared_target_dirs.discard(redundant_sphinx_design_root)

    removable_bytes -= sum(
        file_path.stat().st_size
        for shared_dir in shared_target_dirs
        for file_path in shared_dir.rglob("*")
        if file_path.is_file()
    )

    print(
        "Optimized shared static assets: consolidated "
        f"{consolidated_group_count} duplicate directory groups, "
        f"updated {updated_html_files} HTML files, and removed {removed_directory_count} "
        f"duplicate static directories (about {max(removable_bytes, 0) / (1024 * 1024):.1f} MiB saved)."
    )


def choose_preferred_language(languages: list[str]) -> str:
    if not languages:
        return "EN"
    preferred_languages = ["IT", "EN", "FR"]
    return next((language for language in preferred_languages if language in languages), sorted(languages)[0])


def version_sort_key(label: str) -> tuple[tuple[int, ...], str]:
    numbers = tuple(int(part) for part in re.findall(r"\d+", label))
    return numbers, label.lower()


def language_sort_key(code: str) -> tuple[int, str]:
    preferred_order = {"EN": 0, "IT": 1, "FR": 2, "DE": 3, "ES": 4}
    normalized = code.upper()
    return preferred_order.get(normalized, 99), normalized


def language_display_name(code: str) -> str:
    labels = {
        "DE": "German",
        "EN": "English",
        "ES": "Spanish",
        "FR": "French",
        "IT": "Italian",
    }
    normalized = code.upper()
    return labels.get(normalized, normalized)


def build_catalog(build_root: Path) -> list[tuple[str, list[str]]]:
    versions = sorted(
        [path.name for path in build_root.iterdir() if path.is_dir() and not path.name.startswith("_")],
        key=version_sort_key,
        reverse=True,
    )
    catalog = []
    for version in versions:
        languages = sorted(
            [path.name for path in (build_root / version).iterdir() if path.is_dir() and not path.name.startswith("_")],
            key=language_sort_key,
        )
        catalog.append((version, languages))
    return catalog


def pick_brand_asset(source_root: Path, version: str, language: str, file_name: str) -> Path | None:
    candidates = [
        source_root / "_shared" / "media" / "images" / file_name,
        source_root / version / language / "img" / file_name,
        source_root / version / "EN" / "img" / file_name,
        source_root / version / "IT" / "img" / file_name,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate

    for candidate in source_root.rglob(file_name):
        if candidate.is_file():
            return candidate

    return None


def create_root_landing_page(build_root: Path, source_root: Path) -> None:
    catalog = build_catalog(build_root)
    if not catalog:
        return

    latest_version, latest_languages = catalog[0]
    default_language = "EN" if "EN" in latest_languages else latest_languages[0]
    latest_href = f"./{quote(latest_version)}/{quote(default_language)}/index.html"

    asset_dir = build_root / "_assets" / "landing"
    asset_dir.mkdir(parents=True, exist_ok=True)

    logo_source = pick_brand_asset(source_root, latest_version, default_language, "logo.png")
    product_source = pick_brand_asset(source_root, latest_version, default_language, "Icon_FlexiVision.png")

    logo_relative = None
    product_relative = None

    if logo_source:
        logo_target = asset_dir / "ars-logo.png"
        shutil.copy2(logo_source, logo_target)
        logo_relative = "./_assets/landing/ars-logo.png"

    if product_source:
        product_target = asset_dir / "flexivision-icon.png"
        shutil.copy2(product_source, product_target)
        product_relative = "./_assets/landing/flexivision-icon.png"

    total_versions = len(catalog)
    total_language_variants = sum(len(languages) for _, languages in catalog)

    hero_logo = (
        f'<img src="{logo_relative}" alt="ARS Automation logo" class="brand-logo">'
        if logo_relative
        else '<div class="brand-fallback">ARS Automation</div>'
    )

    product_figure = (
        f'<img src="{product_relative}" alt="FlexiVision One system illustration" class="product-figure">'
        if product_relative
        else ""
    )

    cards = []
    for index, (version, languages) in enumerate(catalog):
        is_latest = index == 0
        badge = '<span class="version-badge">Latest release</span>' if is_latest else ""
        language_links = []
        for language in languages:
            href = f"./{quote(version)}/{quote(language)}/index.html"
            label = language_display_name(language)
            language_links.append(
                "\n".join(
                    [
                        f'<a class="language-button" href="{href}">',
                        f'  <span class="language-name">{escape(label)}</span>',
                        f'  <span class="language-code">{escape(language.upper())}</span>',
                        "</a>",
                    ]
                )
            )

        cards.append(
            "\n".join(
                [
                    f'<section class="version-card{" latest" if is_latest else ""}">',
                    '  <div class="version-top">',
                    '    <div>',
                    f'      <p class="version-kicker">Documentation release</p>',
                    f'      <h2>{escape(version)}</h2>',
                    '    </div>',
                    f'    {badge}' if badge else "",
                    '  </div>',
                    f'  <p class="version-copy">{len(languages)} language{"s" if len(languages) != 1 else ""} available for this release.</p>',
                    '  <div class="language-grid">',
                    *language_links,
                    '  </div>',
                    '</section>',
                ]
            ).replace("\n\n", "\n")
        )

    html = "\n".join(
        [
            "<!doctype html>",
            '<html lang="en">',
            "<head>",
            '  <meta charset="utf-8">',
            '  <meta name="viewport" content="width=device-width, initial-scale=1">',
            "  <title>ARS Automation Documentation Portal</title>",
            "  <style>",
            "    :root {",
            "      --ars-ink: #110d44;",
            "      --ars-blue: #3936d4;",
            "      --ars-red: #eb4b50;",
            "      --ars-steel: #1a3e72;",
            "      --ars-sky: #dce7ff;",
            "      --ars-white: #ffffff;",
            "      --ars-muted: #5a6482;",
            "      --ars-line: rgba(17, 13, 68, 0.12);",
            "      --ars-shadow: 0 24px 60px rgba(17, 13, 68, 0.12);",
            "    }",
            "    * { box-sizing: border-box; }",
            "    html { scroll-behavior: smooth; }",
            "    body {",
            '      margin: 0;',
            '      font-family: Aptos, "Segoe UI", "Helvetica Neue", Arial, sans-serif;',
            "      color: var(--ars-ink);",
            "      background:",
            "        radial-gradient(circle at top left, rgba(57, 54, 212, 0.18), transparent 28%),",
            "        radial-gradient(circle at 82% 16%, rgba(235, 75, 80, 0.12), transparent 20%),",
            "        linear-gradient(180deg, #f6f8ff 0%, #eef3ff 46%, #fdfdff 100%);",
            "    }",
            "    body::before {",
            '      content: "";',
            "      position: fixed;",
            "      inset: 0;",
            "      pointer-events: none;",
            "      opacity: 0.42;",
            "      background-image:",
            "        linear-gradient(rgba(26, 62, 114, 0.05) 1px, transparent 1px),",
            "        linear-gradient(90deg, rgba(26, 62, 114, 0.05) 1px, transparent 1px);",
            "      background-size: 32px 32px;",
            "      mask-image: linear-gradient(180deg, rgba(0,0,0,0.7), transparent 88%);",
            "    }",
            "    main {",
            "      position: relative;",
            "      max-width: 1220px;",
            "      margin: 0 auto;",
            "      padding: 32px 24px 72px;",
            "    }",
            "    .hero {",
            "      display: grid;",
            "      grid-template-columns: minmax(0, 1.15fr) minmax(300px, 0.85fr);",
            "      gap: 32px;",
            "      align-items: stretch;",
            "    }",
            "    .hero-copy, .hero-visual {",
            "      border-radius: 30px;",
            "      border: 1px solid var(--ars-line);",
            "      box-shadow: var(--ars-shadow);",
            "    }",
            "    .hero-copy {",
            "      padding: 34px;",
            "      background: rgba(255, 255, 255, 0.84);",
            "      backdrop-filter: blur(12px);",
            "    }",
            "    .hero-visual {",
            "      position: relative;",
            "      overflow: hidden;",
            "      min-height: 440px;",
            "      background:",
            "        radial-gradient(circle at top left, rgba(57, 54, 212, 0.22), transparent 34%),",
            "        linear-gradient(165deg, rgba(17, 13, 68, 0.98), rgba(26, 62, 114, 0.96));",
            "    }",
            "    .hero-visual::before {",
            '      content: "";',
            "      position: absolute;",
            "      inset: auto -80px -120px auto;",
            "      width: 340px;",
            "      height: 340px;",
            "      border-radius: 50%;",
            "      background: radial-gradient(circle, rgba(255,255,255,0.22), rgba(255,255,255,0));",
            "    }",
            "    .brand-row {",
            "      display: flex;",
            "      align-items: center;",
            "      gap: 16px;",
            "      margin-bottom: 28px;",
            "    }",
            "    .brand-logo {",
            "      width: min(100%, 240px);",
            "      height: auto;",
            "      display: block;",
            "    }",
            "    .brand-fallback {",
            "      font-size: 1.4rem;",
            "      font-weight: 800;",
            "      letter-spacing: -0.03em;",
            "    }",
            "    .eyebrow {",
            "      margin: 0 0 10px;",
            "      font-size: 0.82rem;",
            "      font-weight: 700;",
            "      letter-spacing: 0.22em;",
            "      text-transform: uppercase;",
            "      color: var(--ars-steel);",
            "    }",
            "    h1 {",
            "      margin: 0;",
            "      font-size: clamp(2.7rem, 5.5vw, 5rem);",
            "      line-height: 0.94;",
            "      letter-spacing: -0.05em;",
            "      max-width: 10ch;",
            "    }",
            "    .hero-copy p {",
            "      margin: 20px 0 0;",
            "      max-width: 62ch;",
            "      font-size: 1.05rem;",
            "      line-height: 1.7;",
            "      color: var(--ars-muted);",
            "    }",
            "    .hero-actions {",
            "      display: flex;",
            "      flex-wrap: wrap;",
            "      gap: 12px;",
            "      margin-top: 26px;",
            "    }",
            "    .primary-cta, .secondary-cta {",
            "      display: inline-flex;",
            "      align-items: center;",
            "      justify-content: center;",
            "      min-height: 48px;",
            "      padding: 0 18px;",
            "      border-radius: 999px;",
            "      text-decoration: none;",
            "      font-weight: 700;",
            "      transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;",
            "    }",
            "    .primary-cta {",
            "      background: linear-gradient(135deg, var(--ars-blue), #5e6cff);",
            "      color: var(--ars-white);",
            "      box-shadow: 0 18px 34px rgba(57, 54, 212, 0.22);",
            "    }",
            "    .secondary-cta {",
            "      color: var(--ars-ink);",
            "      border: 1px solid rgba(26, 62, 114, 0.18);",
            "      background: rgba(255, 255, 255, 0.72);",
            "    }",
            "    .primary-cta:hover, .secondary-cta:hover {",
            "      transform: translateY(-2px);",
            "    }",
            "    .stat-ribbon {",
            "      display: flex;",
            "      flex-wrap: wrap;",
            "      gap: 10px;",
            "      margin-top: 24px;",
            "    }",
            "    .stat-pill {",
            "      display: inline-flex;",
            "      align-items: baseline;",
            "      gap: 8px;",
            "      padding: 10px 14px;",
            "      border-radius: 999px;",
            "      border: 1px solid rgba(26, 62, 114, 0.12);",
            "      background: rgba(255, 255, 255, 0.78);",
            "    }",
            "    .stat-pill strong {",
            "      font-size: 1rem;",
            "    }",
            "    .stat-pill span {",
            "      color: var(--ars-muted);",
            "      font-size: 0.92rem;",
            "    }",
            "    .visual-copy {",
            "      position: absolute;",
            "      inset: 28px auto auto 28px;",
            "      width: min(260px, calc(100% - 56px));",
            "      padding: 18px 18px 16px;",
            "      border-radius: 22px;",
            "      background: rgba(255, 255, 255, 0.09);",
            "      border: 1px solid rgba(255, 255, 255, 0.14);",
            "      color: rgba(255, 255, 255, 0.95);",
            "      backdrop-filter: blur(10px);",
            "    }",
            "    .visual-copy p {",
            "      margin: 0;",
            "      line-height: 1.6;",
            "      color: rgba(255, 255, 255, 0.78);",
            "    }",
            "    .visual-copy strong {",
            "      display: block;",
            "      margin-bottom: 8px;",
            "      font-size: 0.85rem;",
            "      letter-spacing: 0.18em;",
            "      text-transform: uppercase;",
            "    }",
            "    .product-figure {",
            "      position: absolute;",
            "      right: 26px;",
            "      bottom: -4px;",
            "      width: min(86%, 440px);",
            "      height: auto;",
            "      filter: drop-shadow(0 28px 34px rgba(0, 0, 0, 0.22));",
            "    }",
            "    .section-header {",
            "      display: flex;",
            "      justify-content: space-between;",
            "      align-items: end;",
            "      gap: 18px;",
            "      margin: 48px 0 18px;",
            "    }",
            "    .section-header h2 {",
            "      margin: 0;",
            "      font-size: clamp(1.8rem, 3vw, 2.5rem);",
            "      letter-spacing: -0.04em;",
            "    }",
            "    .section-header p {",
            "      margin: 8px 0 0;",
            "      color: var(--ars-muted);",
            "      max-width: 56ch;",
            "    }",
            "    .version-grid {",
            "      display: grid;",
            "      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));",
            "      gap: 20px;",
            "    }",
            "    .version-card {",
            "      display: flex;",
            "      flex-direction: column;",
            "      gap: 18px;",
            "      padding: 24px;",
            "      border-radius: 26px;",
            "      border: 1px solid var(--ars-line);",
            "      background: rgba(255, 255, 255, 0.88);",
            "      box-shadow: var(--ars-shadow);",
            "    }",
            "    .version-card.latest {",
            "      background: linear-gradient(165deg, rgba(17, 13, 68, 0.98), rgba(26, 62, 114, 0.96));",
            "      color: var(--ars-white);",
            "    }",
            "    .version-top {",
            "      display: flex;",
            "      justify-content: space-between;",
            "      gap: 12px;",
            "      align-items: flex-start;",
            "    }",
            "    .version-kicker {",
            "      margin: 0 0 6px;",
            "      font-size: 0.8rem;",
            "      letter-spacing: 0.16em;",
            "      text-transform: uppercase;",
            "      color: inherit;",
            "      opacity: 0.72;",
            "    }",
            "    .version-card h2 {",
            "      margin: 0;",
            "      font-size: 2rem;",
            "      letter-spacing: -0.04em;",
            "    }",
            "    .version-badge {",
            "      padding: 8px 12px;",
            "      border-radius: 999px;",
            "      background: rgba(255, 255, 255, 0.14);",
            "      border: 1px solid rgba(255, 255, 255, 0.18);",
            "      font-size: 0.78rem;",
            "      font-weight: 700;",
            "      text-transform: uppercase;",
            "      letter-spacing: 0.08em;",
            "      white-space: nowrap;",
            "    }",
            "    .version-copy {",
            "      margin: 0;",
            "      line-height: 1.6;",
            "      color: inherit;",
            "      opacity: 0.82;",
            "    }",
            "    .language-grid {",
            "      display: flex;",
            "      flex-wrap: wrap;",
            "      gap: 12px;",
            "    }",
            "    .language-button {",
            "      display: inline-flex;",
            "      align-items: center;",
            "      justify-content: space-between;",
            "      gap: 12px;",
            "      min-width: 156px;",
            "      padding: 12px 14px;",
            "      border-radius: 18px;",
            "      border: 1px solid rgba(17, 13, 68, 0.12);",
            "      background: rgba(255, 255, 255, 0.92);",
            "      text-decoration: none;",
            "      color: var(--ars-ink);",
            "      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;",
            "    }",
            "    .language-button:hover {",
            "      transform: translateY(-2px);",
            "      border-color: rgba(57, 54, 212, 0.3);",
            "      background: rgba(220, 231, 255, 0.92);",
            "      box-shadow: 0 16px 32px rgba(57, 54, 212, 0.12);",
            "    }",
            "    .version-card.latest .language-button {",
            "      border-color: rgba(255, 255, 255, 0.14);",
            "      background: rgba(255, 255, 255, 0.08);",
            "      color: var(--ars-white);",
            "    }",
            "    .version-card.latest .language-button:hover {",
            "      border-color: rgba(255, 255, 255, 0.28);",
            "      background: rgba(255, 255, 255, 0.14);",
            "      box-shadow: 0 18px 34px rgba(0, 0, 0, 0.18);",
            "    }",
            "    .language-name {",
            "      font-weight: 700;",
            "    }",
            "    .language-code {",
            "      display: inline-flex;",
            "      align-items: center;",
            "      justify-content: center;",
            "      min-width: 40px;",
            "      padding: 6px 8px;",
            "      border-radius: 999px;",
            "      background: rgba(17, 13, 68, 0.08);",
            "      font-size: 0.78rem;",
            "      font-weight: 800;",
            "      letter-spacing: 0.08em;",
            "      text-transform: uppercase;",
            "    }",
            "    .version-card.latest .language-code {",
            "      background: rgba(255, 255, 255, 0.14);",
            "    }",
            "    .landing-note {",
            "      margin-top: 22px;",
            "      color: var(--ars-muted);",
            "      font-size: 0.95rem;",
            "    }",
            "    @media (max-width: 920px) {",
            "      .hero { grid-template-columns: 1fr; }",
            "      .hero-visual { min-height: 360px; }",
            "      .product-figure { width: min(82%, 340px); }",
            "    }",
            "    @media (max-width: 640px) {",
            "      main { padding: 18px 16px 42px; }",
            "      .hero-copy, .hero-visual, .version-card { padding: 20px; }",
            "      .brand-logo { width: min(100%, 180px); }",
            "      .language-button { width: 100%; }",
            "      .visual-copy { position: static; width: auto; margin: 20px; }",
            "      .product-figure { right: 18px; width: min(82%, 280px); }",
            "    }",
            "  </style>",
            "</head>",
            "<body>",
            "  <main>",
            '    <section class="hero">',
            '      <div class="hero-copy">',
            f"        <div class=\"brand-row\">{hero_logo}</div>",
            '        <p class="eyebrow">Documentation portal</p>',
            "        <h1>Choose your version and language.</h1>",
            "        <p>Browse the FlexiVision One documentation by release and language from a single landing page. The newest versions are always listed first, and every destination opens directly to the manual home page.</p>",
            '        <div class="hero-actions">',
            f'          <a class="primary-cta" href="{latest_href}">Open latest release</a>',
            '          <a class="secondary-cta" href="#versions">Browse all versions</a>',
            "        </div>",
            '        <div class="stat-ribbon">',
            f'          <div class="stat-pill"><strong>{total_versions}</strong><span>release{"s" if total_versions != 1 else ""}</span></div>',
            f'          <div class="stat-pill"><strong>{total_language_variants}</strong><span>language option{"s" if total_language_variants != 1 else ""}</span></div>',
            f'          <div class="stat-pill"><strong>{escape(latest_version)}</strong><span>latest available version</span></div>',
            "        </div>",
            "      </div>",
            '      <div class="hero-visual" aria-hidden="true">',
            '        <div class="visual-copy">',
            '          <strong>ARS Automation</strong>',
            '          <p>Offline-friendly, web-ready documentation access for every published manual release.</p>',
            "        </div>",
            f"        {product_figure}",
            "      </div>",
            "    </section>",
            '    <section id="versions">',
            '      <div class="section-header">',
            "        <div>",
            "          <h2>Available releases</h2>",
            "          <p>Select a documentation release, then choose the language you want to open. Newer versions are shown first.</p>",
            "        </div>",
            "      </div>",
            '      <div class="version-grid">',
            *cards,
            "      </div>",
            '      <p class="landing-note">This portal is designed to work both when opened locally and when hosted online.</p>',
            "    </section>",
            "  </main>",
            "</body>",
            "</html>",
        ]
    )

    (build_root / "index.html").write_text(html, encoding="utf-8")


def select_default_language(source_root: Path, target_version: str | None, target_language: str | None) -> str:
    if target_language:
        return target_language.upper()

    version_paths = list_version_paths(source_root)
    if not version_paths:
        return "EN"

    if target_version:
        languages = [path.name for path in list_language_paths(source_root / target_version)]
        return choose_preferred_language(languages)

    common_languages = None
    for version_path in version_paths:
        version_languages = {path.name for path in list_language_paths(version_path)}
        common_languages = version_languages if common_languages is None else common_languages & version_languages

    if common_languages:
        return choose_preferred_language(sorted(common_languages))

    latest_languages = [path.name for path in list_language_paths(version_paths[-1])]
    return choose_preferred_language(latest_languages)


def validate_targets(source_root: Path, target_version: str | None, target_language: str | None) -> tuple[str | None, str | None]:
    normalized_version = target_version.strip() if target_version else None
    normalized_language = target_language.strip().upper() if target_language else None

    version_paths = {path.name: path for path in list_version_paths(source_root)}
    if normalized_version and normalized_version not in version_paths:
        available_versions = ", ".join(sorted(version_paths))
        raise ValueError(f"Unknown version '{normalized_version}'. Available versions: {available_versions}.")

    if normalized_language:
        if normalized_version:
            languages = {path.name.upper() for path in list_language_paths(version_paths[normalized_version])}
            if normalized_language not in languages:
                available_languages = ", ".join(sorted(languages))
                raise ValueError(
                    f"Language '{normalized_language}' is not available for version '{normalized_version}'. "
                    f"Available languages: {available_languages}."
                )
        else:
            available_anywhere = False
            for version_path in version_paths.values():
                languages = {path.name.upper() for path in list_language_paths(version_path)}
                if normalized_language in languages:
                    available_anywhere = True
                    break
            if not available_anywhere:
                raise ValueError(f"Unknown language '{normalized_language}'.")

    return normalized_version, normalized_language


def filter_temp_sources(temp_source_root: Path, target_version: str | None, target_language: str | None) -> None:
    for version_path in list_version_paths(temp_source_root):
        if target_version and version_path.name != target_version:
            shutil.rmtree(version_path, onexc=handle_remove_readonly)
            continue

        if not target_language:
            continue

        matching_language_found = False
        for language_path in list_language_paths(version_path):
            if language_path.name.upper() == target_language:
                matching_language_found = True
                continue
            shutil.rmtree(language_path, onexc=handle_remove_readonly)

        if not matching_language_found:
            shutil.rmtree(version_path, onexc=handle_remove_readonly)


def prepare_filtered_source_input(
    source_root: Path,
    staged_source_root: Path,
    target_version: str | None,
    target_language: str | None,
) -> None:
    clear_directory(staged_source_root)

    shared_root = source_root / "_shared"
    if shared_root.exists():
        shutil.copytree(shared_root, staged_source_root / "_shared", dirs_exist_ok=True)

    for version_path in list_version_paths(source_root):
        if target_version and version_path.name != target_version:
            continue

        destination_version_root = staged_source_root / version_path.name
        destination_version_root.mkdir(parents=True, exist_ok=True)

        for language_path in list_language_paths(version_path):
            if target_language and language_path.name.upper() != target_language.upper():
                continue
            shutil.copytree(language_path, destination_version_root / language_path.name, dirs_exist_ok=True)


def _build_html_task(task_spec: dict[str, object]) -> tuple[str, float, str]:
    label = str(task_spec["label"])
    source_dir = Path(task_spec["source_dir"])
    build_dir = Path(task_spec["build_dir"])
    started_at = time.perf_counter()

    clear_directory(build_dir)
    result = subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "html", ".", "_build/html"],
        capture_output=True,
        text=True,
        cwd=source_dir,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Sphinx HTML build failed without stderr output.")

    if not (build_dir / "index.html").exists():
        raise FileNotFoundError(f"Missing HTML build output: {build_dir / 'index.html'}")

    return label, time.perf_counter() - started_at, "rebuilt"


def build_project_parallel(
    version_languages: list[tuple[str, list[str]]],
    temp_src_root: Path,
    timings: list[tuple[str, float]] | None,
) -> None:
    task_specs: list[dict[str, object]] = []
    for version, languages in version_languages:
        for language in languages:
            source_dir = temp_src_root / version / language
            task_specs.append(
                {
                    "label": f"html {version} / {language}",
                    "source_dir": source_dir,
                    "build_dir": source_dir / "_build" / "html",
                }
            )

    with timed_step("build HTML via Sphinx", record=False):
        run_parallel_tasks(
            "HTML build",
            task_specs,
            _build_html_task,
            timings,
            env_var=HTML_BUILD_WORKERS_ENV,
            worker_cap=HTML_BUILD_WORKER_CAP,
        )


def _copy_html_output_task(task_spec: dict[str, object]) -> tuple[str, float, str]:
    label = str(task_spec["label"])
    source_html = Path(task_spec["source_html"])
    destination_dir = Path(task_spec["destination_dir"])
    clean_output = bool(task_spec["clean_output"])
    started_at = time.perf_counter()

    if not source_html.exists():
        raise FileNotFoundError(f"Missing built HTML directory: {source_html}")

    clear_directory(destination_dir)
    shutil.copytree(source_html, destination_dir, dirs_exist_ok=True, ignore=HTML_COPY_IGNORE)

    if clean_output:
        sources_dir = destination_dir / "_sources"
        if sources_dir.exists():
            remove_directory(sources_dir)

    return label, time.perf_counter() - started_at, "copied"


def setup_build_folder_parallel(
    version_languages: list[tuple[str, list[str]]],
    build_parent: Path,
    temp_src_root: Path,
    *,
    clean_output: bool,
    timings: list[tuple[str, float]] | None,
) -> None:
    build_root = build_parent / "build"
    task_specs: list[dict[str, object]] = []

    for version, languages in version_languages:
        for language in languages:
            task_specs.append(
                {
                    "label": f"copy html {version} / {language}",
                    "source_html": temp_src_root / version / language / "_build" / "html",
                    "destination_dir": build_root / version / language,
                    "clean_output": clean_output,
                }
            )

    with timed_step("organize HTML output folders", record=False):
        run_parallel_tasks(
            "HTML output copy",
            task_specs,
            _copy_html_output_task,
            timings,
            env_var=COPY_WORKERS_ENV,
            worker_cap=COPY_WORKER_CAP,
        )


def run_html_build(
    ev,
    build_parent: Path,
    temp_root: Path,
    source_root: Path,
    default_language: str,
    *,
    enable_offline_zip: bool,
    target_version: str | None = None,
    target_language: str | None = None,
    timings: list[tuple[str, float]] | None = None,
) -> Path:
    original_src_path = ev.SRC_PATH
    original_footer_path = ev.FOOTER_PATH
    staged_source_root = None

    ev.SRC_PATH = str(source_root)
    ev.FOOTER_PATH = str(source_root / "_data")

    if target_version or target_language:
        staged_source_root = temp_root.parent / f"{temp_root.name}_source"
        prepare_filtered_source_input(source_root, staged_source_root, target_version, target_language)
        ev.SRC_PATH = str(staged_source_root)

    ev.BUILD_PATH = str(build_parent)
    ev.TEMP_PATH = str(temp_root)
    ev.default_language = default_language
    ev.start_quick_server = lambda *args, **kwargs: None

    ev.info("Starting build configuration.")
    ev.info("Initial checks")
    if not os.path.exists(ev.SRC_PATH):
        raise FileNotFoundError("No source folder found. Exiting.")

    ev.info("Initial set-up:")
    with timed_step("initial setup", timings):
        ev.initial_setup()
    with timed_step("configure footer features", timings):
        configure_footer_features(
            temp_root,
            enable_offline_zip=enable_offline_zip,
        )

    try:
        with timed_step("filter temporary sources", timings):
            filter_temp_sources(Path(ev.TEMP_PATH) / "src", target_version, target_language)

        ev.info("Getting all the versions:")
        with timed_step("discover versions", timings):
            versions = ev.get_versions()
        if not versions:
            raise RuntimeError("No documentation versions found for this build.")
        ev.success("Retrieved all documentation versions.")

        with timed_step("validate default language coverage", timings):
            status = ev.check_default_language(versions)
        if status == -1:
            ev.warning("The default language is not present in every version of the documentation! This may cause problems")

        ev.info("Setting up the versions data:")
        with timed_step("prepare version metadata", timings):
            ev.project_data_setup(versions)
        ev.success("Setup ended.")

        ev.info("Adding versioning to all the Markdown files:")
        with timed_step("inject footer/versioning into markdown", timings):
            version_languages = ev.add_versioning(versions)
        ev.success("Versioning added to all Markdown files.")

        ev.info("Starting to build the project:")
        build_project_parallel(
            version_languages,
            Path(ev.TEMP_PATH) / "src",
            timings,
        )
        ev.success("Project built successfully.")

        ev.info("Organizing the folders to have a ready to use website")
        setup_build_folder_parallel(
            version_languages,
            build_parent,
            Path(ev.TEMP_PATH) / "src",
            clean_output=getattr(ev, "clean_website", True),
            timings=timings,
        )
        ev.success("All build files organized in the selected build directory.")
    finally:
        ev.info("Final cleaning process:")
        with timed_step("final cleanup", timings):
            ev.final_cleaning()
        ev.SRC_PATH = original_src_path
        ev.FOOTER_PATH = original_footer_path
        if staged_source_root is not None:
            remove_directory(staged_source_root)

    return Path(ev.BUILD_PATH) / "build"


def build_release_assets(
    build_root: Path,
    timings: list[tuple[str, float]] | None = None,
) -> None:
    with timed_step("remove temporary release artifacts", timings):
        remove_named_files(build_root, {PRINT_FULL_MANUAL_HTML_NAME, LEGACY_OFFLINE_MANUAL_ZIP_NAME})
    with timed_step("optimize shared media", timings):
        optimize_shared_media(build_root)
    with timed_step("optimize shared static assets", timings):
        optimize_shared_static_directories(build_root)
    with timed_step("create offline zip", timings):
        create_site_zip(build_root, build_root / OFFLINE_MANUAL_ZIP_NAME)
    with timed_step("configure release download flags", timings):
        configure_release_download_flags(build_root)


def sync_site_output(build_root: Path, output_root: Path, locked_message: str) -> None:
    mirror_directory(build_root, output_root)


def build_site(
    ev,
    repo_root: Path,
    source_root: Path,
    mode: str,
    target_version: str | None,
    target_language: str | None,
) -> int:
    timings: list[tuple[str, float]] = []
    build_started_at = time.perf_counter()
    default_language = select_default_language(source_root, target_version, target_language)
    source_catalog = build_source_catalog(source_root)
    run_token = str(os.getpid())
    work_root = repo_root / f".tmp_manual_build_{run_token}"
    stage_root = work_root / "stage"
    temp_root = work_root / "temp"
    output_root = repo_root / "build"
    work_root.mkdir(parents=True, exist_ok=True)

    try:
        build_root = run_html_build(
            ev,
            stage_root,
            temp_root,
            source_root,
            default_language,
            enable_offline_zip=mode == "full",
            target_version=target_version,
            target_language=target_language,
            timings=timings,
        )
        with timed_step("write build version manifest", timings):
            write_site_version_manifest(build_root, catalog=source_catalog)
        with timed_step("write build .nojekyll", timings):
            ensure_nojekyll(build_root)
        with timed_step("create build landing page", timings):
            create_root_landing_page(build_root, source_root)

        if mode == "full":
            build_release_assets(
                build_root,
                timings=timings,
            )
        else:
            with timed_step("remove release artifacts from quick build", timings):
                remove_named_files(build_root, RELEASE_ARTIFACT_NAMES)
            with timed_step("optimize shared media", timings):
                optimize_shared_media(build_root)
            with timed_step("optimize shared static assets", timings):
                optimize_shared_static_directories(build_root)

        preserve_existing = target_version is not None or target_language is not None
        if preserve_existing and output_root.exists():
            with timed_step("remove previous targeted output", timings):
                remove_target_scope(output_root, target_version, target_language)
            with timed_step("merge staged build into final build", timings):
                merge_directory(build_root, output_root)
            with timed_step("re-optimize shared media in final build", timings):
                optimize_shared_media(output_root)
            with timed_step("re-optimize shared static assets in final build", timings):
                optimize_shared_static_directories(output_root)
            if mode == "full":
                with timed_step("refresh offline zip after targeted merge", timings):
                    create_site_zip(output_root, output_root / OFFLINE_MANUAL_ZIP_NAME)
        else:
            with timed_step("sync staged build to final build folder", timings):
                sync_site_output(
                    build_root,
                    output_root,
                    "build is in use. Updating files in place where possible.",
                )

        if preserve_existing:
            if mode == "quick":
                with timed_step("remove release artifacts from final quick build", timings):
                    remove_named_files(output_root, RELEASE_ARTIFACT_NAMES)
            else:
                with timed_step("remove legacy zip artifact", timings):
                    remove_named_files(output_root, {LEGACY_OFFLINE_MANUAL_ZIP_NAME})

            with timed_step("write final build version manifest", timings):
                write_site_version_manifest(output_root)
            with timed_step("write final .nojekyll", timings):
                ensure_nojekyll(output_root)
            with timed_step("create final landing page", timings):
                create_root_landing_page(output_root, source_root)
            with timed_step("configure final release download flags", timings):
                configure_release_download_flags(output_root)
        else:
            log_timing("Skipping redundant final metadata pass because the synced build already contains the latest files.")
    finally:
        remove_directory(work_root)
        print_timing_summary(timings, time.perf_counter() - build_started_at)

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the FlexiVision One manual into the local build folder.")
    parser.add_argument(
        "--mode",
        choices=["quick", "full"],
        default="quick",
        help="Select `quick` for HTML only or `full` for HTML + offline ZIP.",
    )
    parser.add_argument("--version", help="Limit the selected build mode to a single version.")
    parser.add_argument("--language", help="Limit the selected build mode to a single language or to one language across versions.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    vendor_root = Path(__file__).resolve().parent / "vendor"
    source_root = repo_root / "sources"

    target_version, target_language = validate_targets(source_root, args.version, args.language)

    os.chdir(repo_root)
    sys.path.insert(0, str(vendor_root))

    from easy_versioning import main as ev  # Imported after chdir so the package reads the right root.

    return build_site(ev, repo_root, source_root, args.mode, target_version, target_language)


if __name__ == "__main__":
    raise SystemExit(main())
