from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


MEDIA_PATTERN = re.compile(
    r"(?P<path>(?:\.\.?[\\/])?[^\"'\s<>()]+?\.(?:mp4|png|jpe?g|gif))",
    re.IGNORECASE,
)
VIDEO_EXTENSIONS = {".mp4"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
VIDEO_COMPRESSION_MANIFEST_NAME = ".video-compression-manifest.json"
VIDEO_COMPRESSION_CACHE_MANIFEST_NAME = "manifest.json"
VIDEO_COMPRESSION_CACHE_FILES_DIR = "files"
VIDEO_PROGRESS_STEP_PERCENT = 5
DURATION_PATTERN = re.compile(
    r"Duration:\s*(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+(?:\.\d+)?)",
    re.IGNORECASE,
)
PROGRESS_TIME_PATTERN = re.compile(
    r"(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+(?:\.\d+)?)"
)


def compute_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_markdown_files(source_root: Path) -> list[Path]:
    return sorted(
        path
        for path in source_root.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".rst"} and "_build" not in path.parts
    )


def extract_referenced_assets(source_root: Path) -> dict[Path, set[Path]]:
    references: dict[Path, set[Path]] = {}

    for markdown_path in iter_markdown_files(source_root):
        text = markdown_path.read_text(encoding="utf-8")
        for match in MEDIA_PATTERN.finditer(text):
            raw_reference = match.group("path")
            if "://" in raw_reference or raw_reference.startswith("/"):
                continue

            normalized_reference = raw_reference.replace("\\", "/")
            candidate = (markdown_path.parent / normalized_reference).resolve()
            if not candidate.exists() or not candidate.is_file():
                continue
            if source_root not in candidate.parents:
                continue
            if "_shared" in candidate.parts:
                continue

            references.setdefault(candidate, set()).add(markdown_path)

    return references


def shared_subfolder_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in VIDEO_EXTENSIONS:
        return "videos"
    return "images"


def choose_shared_target(shared_root: Path, source_file: Path, file_hash: str) -> Path:
    folder = shared_root / shared_subfolder_for(source_file)
    folder.mkdir(parents=True, exist_ok=True)

    candidate = folder / source_file.name
    if not candidate.exists():
        return candidate

    if compute_hash(candidate) == file_hash:
        return candidate

    return folder / f"{source_file.stem}__{file_hash[:10]}{source_file.suffix.lower()}"


def build_duplicate_mapping(source_root: Path, shared_root: Path) -> tuple[dict[Path, Path], list[tuple[list[Path], Path]]]:
    references = extract_referenced_assets(source_root)
    grouped_by_hash: dict[str, list[Path]] = {}

    for asset_path in references:
        file_hash = compute_hash(asset_path)
        grouped_by_hash.setdefault(file_hash, []).append(asset_path)

    mapping: dict[Path, Path] = {}
    groups: list[tuple[list[Path], Path]] = []

    for file_hash, asset_paths in grouped_by_hash.items():
        unique_paths = sorted(set(asset_paths))
        if len(unique_paths) < 2:
            continue

        preferred_source = next((path for path in unique_paths if "_shared" in path.parts), unique_paths[0])
        shared_target = choose_shared_target(shared_root, preferred_source, file_hash)
        if not shared_target.exists():
            shutil.copy2(preferred_source, shared_target)

        for path in unique_paths:
            mapping[path] = shared_target
        groups.append((unique_paths, shared_target))

    return mapping, groups


def rewrite_markdown_references(source_root: Path, path_mapping: dict[Path, Path]) -> int:
    updated_files = 0

    for markdown_path in iter_markdown_files(source_root):
        text = markdown_path.read_text(encoding="utf-8")
        changed = False

        def replace_reference(match: re.Match[str]) -> str:
            nonlocal changed

            raw_reference = match.group("path")
            if "://" in raw_reference or raw_reference.startswith("/"):
                return raw_reference

            normalized_reference = raw_reference.replace("\\", "/")
            source_path = (markdown_path.parent / normalized_reference).resolve()
            target_path = path_mapping.get(source_path)
            if target_path is None:
                return raw_reference

            relative_path = os.path.relpath(target_path, markdown_path.parent).replace("\\", "/")
            if relative_path != raw_reference:
                changed = True
            return relative_path

        updated_text = MEDIA_PATTERN.sub(replace_reference, text)
        if changed:
            markdown_path.write_text(updated_text, encoding="utf-8")
            updated_files += 1

    return updated_files


def collect_current_asset_references(source_root: Path) -> set[Path]:
    return set(extract_referenced_assets(source_root).keys())


def remove_unreferenced_duplicates(source_root: Path, path_mapping: dict[Path, Path]) -> int:
    referenced_assets = collect_current_asset_references(source_root)
    removed_count = 0

    for original_path, shared_target in path_mapping.items():
        if original_path == shared_target:
            continue
        if original_path in referenced_assets:
            continue
        if not original_path.exists():
            continue

        original_path.unlink()
        removed_count += 1

    return removed_count


def prune_empty_directories(root: Path) -> None:
    for directory in sorted((path for path in root.rglob("*") if path.is_dir()), reverse=True):
        try:
            next(directory.iterdir())
        except StopIteration:
            try:
                directory.rmdir()
            except PermissionError:
                continue


def find_ffmpeg(explicit_path: str | None) -> str | None:
    if explicit_path:
        return explicit_path

    for candidate in ("ffmpeg",):
        resolved = shutil.which(candidate)
        if resolved:
            return resolved

    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def read_json_file(path: Path, default: dict) -> dict:
    if not path.exists():
        return default

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def write_json_file(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_name(path.name + ".tmp")
    temp_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    temp_path.replace(path)


def video_compression_settings(crf: int, preset: str) -> dict[str, object]:
    return {
        "audio_bitrate": "96k",
        "audio_codec": "aac",
        "crf": crf,
        "pixel_format": "yuv420p",
        "preset": preset,
        "video_codec": "libx264",
    }


def settings_match(entry: dict | None, crf: int, preset: str) -> bool:
    if not isinstance(entry, dict):
        return False
    return entry.get("settings") == video_compression_settings(crf, preset)


def processed_current_file(entry: dict | None, current_hash: str, crf: int, preset: str) -> bool:
    if not settings_match(entry, crf, preset):
        return False

    status = entry.get("status")
    if status == "compressed":
        return entry.get("output_sha256") == current_hash
    if status == "kept":
        return entry.get("source_sha256") == current_hash
    return False


def manifest_contains_processed_hash(manifest: dict, current_hash: str, crf: int, preset: str) -> bool:
    for entry in manifest.get("videos", {}).values():
        if processed_current_file(entry, current_hash, crf, preset):
            return True
    return False


def make_cache_key(source_hash: str, crf: int, preset: str) -> str:
    payload = {
        "settings": video_compression_settings(crf, preset),
        "source_sha256": source_hash,
    }
    encoded_payload = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded_payload).hexdigest()


def cache_file_for(cache_root: Path, cache_key: str) -> Path:
    return cache_root / VIDEO_COMPRESSION_CACHE_FILES_DIR / cache_key[:2] / f"{cache_key}.mp4"


def parse_hhmmss(value: str) -> float | None:
    match = PROGRESS_TIME_PATTERN.search(value)
    if match is None:
        return None

    hours = int(match.group("hours"))
    minutes = int(match.group("minutes"))
    seconds = float(match.group("seconds"))
    return hours * 3600 + minutes * 60 + seconds


def probe_video_duration(ffmpeg_path: str, video_path: Path) -> float | None:
    result = subprocess.run(
        [ffmpeg_path, "-hide_banner", "-i", str(video_path)],
        capture_output=True,
        text=True,
    )
    match = DURATION_PATTERN.search(result.stderr or result.stdout or "")
    if match is None:
        return None

    return (
        int(match.group("hours")) * 3600
        + int(match.group("minutes")) * 60
        + float(match.group("seconds"))
    )


def parse_progress_seconds(key: str, value: str, duration_seconds: float) -> float | None:
    if key in {"out_time_ms", "out_time_us"}:
        try:
            raw_time = int(value)
        except ValueError:
            return None

        if raw_time > duration_seconds * 1000:
            return raw_time / 1_000_000
        return raw_time / 1_000

    if key == "out_time":
        return parse_hhmmss(value)

    return None


def print_video_progress(
    video_name: str,
    index: int,
    total: int,
    completed_bytes: int,
    current_file_bytes: int,
    total_bytes: int,
    file_fraction: float,
) -> None:
    weighted_bytes = completed_bytes + int(current_file_bytes * file_fraction)
    overall_fraction = weighted_bytes / total_bytes if total_bytes else 1
    print(
        "Video recompression "
        f"{overall_fraction * 100:5.1f}% "
        f"({index}/{total}) - {video_name}: {file_fraction * 100:3.0f}%"
    )


def run_ffmpeg_reencode_with_progress(
    command: list[str],
    ffmpeg_path: str,
    video_path: Path,
    index: int,
    total: int,
    completed_bytes: int,
    total_bytes: int,
) -> tuple[int, list[str]]:
    duration_seconds = probe_video_duration(ffmpeg_path, video_path)
    current_file_bytes = video_path.stat().st_size
    last_milestone = -1
    output_tail: list[str] = []

    if duration_seconds is None or duration_seconds <= 0:
        print(f"Video recompression ({index}/{total}) - {video_path.name}: started")
    else:
        print_video_progress(video_path.name, index, total, completed_bytes, current_file_bytes, total_bytes, 0)
        last_milestone = 0

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    assert process.stdout is not None
    for raw_line in process.stdout:
        line = raw_line.strip()
        if line:
            output_tail.append(line)
            output_tail = output_tail[-20:]

        if duration_seconds is None or "=" not in line:
            continue

        key, value = line.split("=", 1)
        elapsed_seconds = parse_progress_seconds(key, value, duration_seconds)
        if elapsed_seconds is None:
            continue

        file_fraction = min(max(elapsed_seconds / duration_seconds, 0), 1)
        milestone = int(file_fraction * 100 // VIDEO_PROGRESS_STEP_PERCENT) * VIDEO_PROGRESS_STEP_PERCENT
        if milestone <= last_milestone and file_fraction < 1:
            continue

        last_milestone = milestone
        print_video_progress(
            video_path.name,
            index,
            total,
            completed_bytes,
            current_file_bytes,
            total_bytes,
            file_fraction,
        )

    return_code = process.wait()
    if return_code == 0 and duration_seconds is not None and last_milestone < 100:
        print_video_progress(
            video_path.name,
            index,
            total,
            completed_bytes,
            current_file_bytes,
            total_bytes,
            1,
        )

    return return_code, output_tail


def build_manifest_entry(
    *,
    source_hash: str,
    output_hash: str,
    source_size: int,
    output_size: int,
    crf: int,
    preset: str,
    status: str,
) -> dict[str, object]:
    return {
        "output_sha256": output_hash,
        "output_size": output_size,
        "settings": video_compression_settings(crf, preset),
        "source_sha256": source_hash,
        "source_size": source_size,
        "status": status,
    }


def mark_video_kept(
    manifest: dict,
    cache_manifest: dict | None,
    cache_key: str | None,
    relative_path: str,
    source_hash: str,
    source_size: int,
    crf: int,
    preset: str,
) -> None:
    entry = build_manifest_entry(
        source_hash=source_hash,
        output_hash=source_hash,
        source_size=source_size,
        output_size=source_size,
        crf=crf,
        preset=preset,
        status="kept",
    )
    manifest.setdefault("videos", {})[relative_path] = entry
    if cache_manifest is not None and cache_key is not None:
        cache_manifest.setdefault("entries", {})[cache_key] = entry


def recompress_shared_videos(
    shared_root: Path,
    ffmpeg_path: str,
    crf: int,
    preset: str,
    *,
    cache_root: Path | None = None,
) -> tuple[int, int]:
    rewritten = 0
    bytes_saved = 0
    skipped = 0
    reused_from_cache = 0
    videos_root = shared_root / "videos"
    video_paths = sorted(videos_root.rglob("*.mp4")) if videos_root.exists() else []
    total_videos = len(video_paths)
    total_bytes = sum(path.stat().st_size for path in video_paths)
    completed_bytes = 0

    if not video_paths:
        return rewritten, bytes_saved

    print(
        "Video recompression queued: "
        f"{total_videos} MP4 file(s), about {total_bytes / (1024 * 1024):.1f} MiB."
    )

    manifest_path = videos_root / VIDEO_COMPRESSION_MANIFEST_NAME
    manifest = read_json_file(manifest_path, {"version": 1, "videos": {}})

    cache_manifest_path = None
    cache_manifest = None
    if cache_root is not None:
        cache_root.mkdir(parents=True, exist_ok=True)
        cache_manifest_path = cache_root / VIDEO_COMPRESSION_CACHE_MANIFEST_NAME
        cache_manifest = read_json_file(cache_manifest_path, {"version": 1, "entries": {}})

    for index, video_path in enumerate(video_paths, start=1):
        temp_path = video_path.with_name(video_path.stem + "__optimized.mp4")
        original_size = video_path.stat().st_size
        source_hash = compute_hash(video_path)
        relative_path = video_path.relative_to(shared_root).as_posix()
        cache_key = make_cache_key(source_hash, crf, preset) if cache_root is not None else None

        if processed_current_file(manifest.get("videos", {}).get(relative_path), source_hash, crf, preset) or manifest_contains_processed_hash(
            manifest,
            source_hash,
            crf,
            preset,
        ):
            skipped += 1
            completed_bytes += original_size
            print(
                "Video recompression "
                f"{completed_bytes / total_bytes * 100:5.1f}% "
                f"({index}/{total_videos}) - {video_path.name}: already processed, skipped"
            )
            continue

        cache_entry = None
        if cache_manifest is not None and cache_key is not None:
            cache_entry = cache_manifest.get("entries", {}).get(cache_key)

        if isinstance(cache_entry, dict) and settings_match(cache_entry, crf, preset):
            if cache_entry.get("status") == "compressed" and cache_root is not None:
                cached_relative_path = cache_entry.get("cache_file")
                cached_file = cache_root / cached_relative_path if isinstance(cached_relative_path, str) else cache_file_for(cache_root, cache_key)
                if cached_file.exists():
                    shutil.copy2(cached_file, video_path)
                    output_size = video_path.stat().st_size
                    output_hash = compute_hash(video_path)
                    manifest.setdefault("videos", {})[relative_path] = build_manifest_entry(
                        source_hash=source_hash,
                        output_hash=output_hash,
                        source_size=original_size,
                        output_size=output_size,
                        crf=crf,
                        preset=preset,
                        status="compressed",
                    )
                    rewritten += 1
                    reused_from_cache += 1
                    bytes_saved += max(original_size - output_size, 0)
                    completed_bytes += original_size
                    print(
                        "Video recompression "
                        f"{completed_bytes / total_bytes * 100:5.1f}% "
                        f"({index}/{total_videos}) - {video_path.name}: reused cached optimized file"
                    )
                    write_json_file(manifest_path, manifest)
                    continue
            elif cache_entry.get("status") == "kept":
                mark_video_kept(
                    manifest,
                    None,
                    None,
                    relative_path,
                    source_hash,
                    original_size,
                    crf,
                    preset,
                )
                skipped += 1
                completed_bytes += original_size
                print(
                    "Video recompression "
                    f"{completed_bytes / total_bytes * 100:5.1f}% "
                    f"({index}/{total_videos}) - {video_path.name}: already checked, kept original"
                )
                write_json_file(manifest_path, manifest)
                continue

        if temp_path.exists():
            temp_path.unlink()

        command = [
            ffmpeg_path,
            "-hide_banner",
            "-y",
            "-i",
            str(video_path),
            "-map",
            "0:v:0",
            "-map",
            "0:a?",
            "-c:v",
            "libx264",
            "-preset",
            preset,
            "-crf",
            str(crf),
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            "-c:a",
            "aac",
            "-b:a",
            "96k",
            "-progress",
            "pipe:1",
            "-nostats",
            str(temp_path),
        ]
        return_code, output_tail = run_ffmpeg_reencode_with_progress(
            command,
            ffmpeg_path,
            video_path,
            index,
            total_videos,
            completed_bytes,
            total_bytes,
        )
        if return_code != 0 or not temp_path.exists():
            if temp_path.exists():
                temp_path.unlink()
            print(f"Skipping video compression for {video_path.name}: ffmpeg failed.")
            if output_tail:
                print("Last ffmpeg output:")
                for line in output_tail[-5:]:
                    print(f"  {line}")
            completed_bytes += original_size
            continue

        optimized_size = temp_path.stat().st_size
        if optimized_size < original_size:
            output_hash = compute_hash(temp_path)
            if cache_root is not None and cache_manifest is not None and cache_key is not None:
                cached_file = cache_file_for(cache_root, cache_key)
                cached_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(temp_path, cached_file)
                cache_entry = build_manifest_entry(
                    source_hash=source_hash,
                    output_hash=output_hash,
                    source_size=original_size,
                    output_size=optimized_size,
                    crf=crf,
                    preset=preset,
                    status="compressed",
                )
                cache_entry["cache_file"] = cached_file.relative_to(cache_root).as_posix()
                cache_manifest.setdefault("entries", {})[cache_key] = cache_entry

            temp_path.replace(video_path)
            manifest.setdefault("videos", {})[relative_path] = build_manifest_entry(
                source_hash=source_hash,
                output_hash=output_hash,
                source_size=original_size,
                output_size=optimized_size,
                crf=crf,
                preset=preset,
                status="compressed",
            )
            rewritten += 1
            bytes_saved += original_size - optimized_size
        else:
            temp_path.unlink()
            mark_video_kept(
                manifest,
                cache_manifest,
                cache_key,
                relative_path,
                source_hash,
                original_size,
                crf,
                preset,
            )

        completed_bytes += original_size
        write_json_file(manifest_path, manifest)
        if cache_manifest_path is not None and cache_manifest is not None:
            write_json_file(cache_manifest_path, cache_manifest)

    if cache_manifest_path is not None and cache_manifest is not None:
        write_json_file(cache_manifest_path, cache_manifest)

    print(
        "Video recompression finished: "
        f"{rewritten} optimized, {reused_from_cache} reused from cache, {skipped} skipped."
    )

    return rewritten, bytes_saved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deduplicate and optimize shared media assets for the FlexiVision One manual.")
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "sources",
        help="Documentation source root. Defaults to <repo>/sources.",
    )
    parser.add_argument(
        "--shared-root",
        type=Path,
        default=None,
        help="Shared media root. Defaults to <source-root>/_shared/media.",
    )
    parser.add_argument(
        "--compress-videos",
        action="store_true",
        help="Re-encode shared MP4 files if ffmpeg is available.",
    )
    parser.add_argument(
        "--ffmpeg",
        help="Explicit ffmpeg executable path.",
    )
    parser.add_argument(
        "--cache-root",
        type=Path,
        default=None,
        help="Optional persistent cache for already optimized video outputs.",
    )
    parser.add_argument("--crf", type=int, default=30, help="CRF value used for video recompression.")
    parser.add_argument("--preset", default="slow", help="ffmpeg preset used for video recompression.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    shared_root = (args.shared_root or (source_root / "_shared" / "media")).resolve()
    shared_root.mkdir(parents=True, exist_ok=True)

    path_mapping, duplicate_groups = build_duplicate_mapping(source_root, shared_root)
    updated_markdown_files = rewrite_markdown_references(source_root, path_mapping)
    removed_files = remove_unreferenced_duplicates(source_root, path_mapping)
    prune_empty_directories(source_root)

    saved_bytes_from_dedup = sum(
        path.stat().st_size
        for original_path, path in path_mapping.items()
        if original_path != path and not original_path.exists()
    )

    recompressed_videos = 0
    saved_bytes_from_reencode = 0
    if args.compress_videos:
        ffmpeg_path = find_ffmpeg(args.ffmpeg)
        if ffmpeg_path is None:
            print("ffmpeg not found. Skipping video recompression.")
        else:
            recompressed_videos, saved_bytes_from_reencode = recompress_shared_videos(
                shared_root,
                ffmpeg_path,
                args.crf,
                args.preset,
                cache_root=args.cache_root,
            )

    print(
        "\n".join(
            [
                f"Duplicate groups centralized: {len(duplicate_groups)}",
                f"Markdown files updated: {updated_markdown_files}",
                f"Original duplicate files removed: {removed_files}",
                f"Estimated bytes saved by deduplication: {saved_bytes_from_dedup}",
                f"Shared videos recompressed: {recompressed_videos}",
                f"Estimated bytes saved by recompression: {saved_bytes_from_reencode}",
                f"Shared media root: {shared_root}",
            ]
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
