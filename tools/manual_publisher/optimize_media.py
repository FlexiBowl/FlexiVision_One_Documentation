from __future__ import annotations

import argparse
import hashlib
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


def recompress_shared_videos(shared_root: Path, ffmpeg_path: str, crf: int, preset: str) -> tuple[int, int]:
    rewritten = 0
    bytes_saved = 0

    for video_path in sorted((shared_root / "videos").rglob("*.mp4")) if (shared_root / "videos").exists() else []:
        temp_path = video_path.with_name(video_path.stem + "__optimized.mp4")
        original_size = video_path.stat().st_size

        command = [
            ffmpeg_path,
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
            str(temp_path),
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0 or not temp_path.exists():
            if temp_path.exists():
                temp_path.unlink()
            print(f"Skipping video compression for {video_path.name}: ffmpeg failed.")
            continue

        optimized_size = temp_path.stat().st_size
        if optimized_size < original_size:
            temp_path.replace(video_path)
            rewritten += 1
            bytes_saved += original_size - optimized_size
        else:
            temp_path.unlink()

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
