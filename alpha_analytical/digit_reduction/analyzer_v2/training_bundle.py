from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence


DEFAULT_ANALYSIS_ROOT = Path("data/outputs/analysis")
VARIANT_NAMES: Sequence[str] = ("Combined", "Midday", "Evening")
PACKAGED_VARIANTS_DEFAULT: Sequence[str] = ("Midday", "Evening")
_MAP_STAMP_RE = re.compile(r"^(?P<stamp>\d{8})_(?P<variant>Combined|Midday|Evening)_winner_map\.json$")
_ARTIFACT_RE = re.compile(
    r"^(?P<stamp>\d{8})_(?P<variant>Combined|Midday|Evening)_(?P<artifact>winner_(map|flags|stamp|hits|overlay)\.(json|csv|html))$"
)


class TrainingBundleError(RuntimeError):
    """Raised when a bundle cannot be prepared."""


def _analysis_root(path: Optional[Path | str]) -> Path:
    if path is None:
        return DEFAULT_ANALYSIS_ROOT
    resolved = Path(path)
    return resolved


def _state_root(state: str, analysis_root: Path) -> Path:
    return analysis_root / "digit_reduction" / state


def _training_steps_path(state: str, analysis_root: Path) -> Optional[Path]:
    training_dir = _state_root(state, analysis_root) / "training"
    if not training_dir.exists():
        return None
    target = training_dir / f"{state}_digit_reduction_steps.csv"
    return target if target.exists() else None


def _training_logs_path(state: str, analysis_root: Path) -> Optional[Path]:
    training_dir = _state_root(state, analysis_root) / "training"
    if not training_dir.exists():
        return None
    candidates = (
        training_dir / f"{state}_digit_reduction_logs.json",
        training_dir / f"{state}_digit_reduction_log.json",
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _collect_available_stamps(winners_dir: Path) -> Dict[str, List[str]]:
    stamp_variants: Dict[str, List[str]] = {}
    if not winners_dir.exists():
        return stamp_variants
    for path in winners_dir.glob("*_winner_map.json"):
        match = _MAP_STAMP_RE.match(path.name)
        if not match:
            continue
        stamp = match.group("stamp")
        variant = match.group("variant")
        stamp_variants.setdefault(stamp, []).append(variant)
    for variants in stamp_variants.values():
        variants.sort()
    return stamp_variants


def find_latest_stamp(state: str, analysis_root: Optional[Path | str] = None) -> Optional[str]:
    root = _analysis_root(analysis_root)
    winners_dir = _state_root(state, root) / "analyzer_v2" / "winners"
    stamp_variants = _collect_available_stamps(winners_dir)
    if not stamp_variants:
        return None
    return max(stamp_variants.keys())


def _copy_file(src: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / src.name
    shutil.copy2(src, dest_path)
    return dest_path


def package_training_bundle(
    state: str,
    *,
    stamp: Optional[str] = None,
    analysis_root: Optional[Path | str] = None,
    include_overlay: bool = False,
    include_hits: bool = True,
    include_combined: bool = False,
    make_zip: bool = False,
) -> Dict[str, Optional[str]]:
    root = _analysis_root(analysis_root)
    state_root = _state_root(state, root)
    analyzer_dir = state_root / "analyzer_v2"
    winners_dir = analyzer_dir / "winners"

    stamp_variants = _collect_available_stamps(winners_dir)
    if not stamp_variants:
        raise TrainingBundleError(
            f"No winner overlays found for state {state}. Run the overlay batch first."
        )
    if stamp is None:
        stamp = max(stamp_variants.keys())
    if stamp not in stamp_variants:
        raise TrainingBundleError(
            f"Stamp {stamp} not found for state {state}. Available: {sorted(stamp_variants)}"
        )
    variants = stamp_variants[stamp]
    packaged_variants = list(PACKAGED_VARIANTS_DEFAULT if not include_combined else VARIANT_NAMES)
    packaged_variants = [variant for variant in variants if variant in packaged_variants]

    bundle_root = state_root / "training_sets" / stamp
    if bundle_root.exists():
        shutil.rmtree(bundle_root)
    bundle_root.mkdir(parents=True, exist_ok=True)

    copied: List[Path] = []

    training_steps = _training_steps_path(state, root)
    if training_steps is not None:
        copied.append(_copy_file(training_steps, bundle_root))
    training_logs = _training_logs_path(state, root)
    if training_logs is not None:
        copied.append(_copy_file(training_logs, bundle_root))

    per_item = analyzer_dir / f"{state}_analyzer_v2_per_item.csv"
    top_candidates = analyzer_dir / f"{state}_analyzer_v2_top_candidates.csv"
    meta = analyzer_dir / f"{state}_analyzer_v2_meta.json"
    essentials = [per_item, top_candidates, meta]
    missing = [path.name for path in essentials if not path.exists()]
    if missing:
        raise TrainingBundleError(
            "Missing analyzer outputs: " + ", ".join(missing)
        )
    for essential in essentials:
        copied.append(_copy_file(essential, bundle_root))

    packaged_variants = list(packaged_variants)
    winners_dir_target = bundle_root / "winners"
    winners_dir_target.mkdir(parents=True, exist_ok=True)

    for variant in packaged_variants:
        stem = f"{stamp}_{variant}"
        for artifact in ("winner_map.json", "winner_flags.csv", "winner_stamp.json"):
            path_obj = winners_dir / f"{stem}_{artifact}"
            if not path_obj.exists():
                raise TrainingBundleError(f"Missing winner artifact: {path_obj.name}")
            copied.append(_copy_file(path_obj, winners_dir_target))
        if include_hits:
            path_obj = winners_dir / f"{stem}_winner_hits.csv"
            if not path_obj.exists():
                raise TrainingBundleError(f"Missing winner artifact: {path_obj.name}")
            copied.append(_copy_file(path_obj, winners_dir_target))
        if include_overlay:
            path_obj = winners_dir / f"{stem}_winner_overlay.html"
            if not path_obj.exists():
                raise TrainingBundleError(f"Missing winner artifact: {path_obj.name}")
            copied.append(_copy_file(path_obj, winners_dir_target))

    manifest = {
        "state": state,
        "stamp": stamp,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "analysis_root": str(root.resolve()),
        "include_overlay": include_overlay,
        "include_hits": include_hits,
        "include_combined": include_combined,
        "make_zip": make_zip,
        "packaged_variants": packaged_variants,
        "files": [
            {
                "name": path.name,
                "relative_path": str(path.relative_to(bundle_root)),
            }
            for path in sorted(copied)
        ],
    }
    manifest_path = bundle_root / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    zip_path: Optional[Path] = None
    if make_zip:
        archive_base = bundle_root.parent / f"{stamp}"
        zip_path = Path(shutil.make_archive(str(archive_base), "zip", bundle_root))

    return {
        "bundle_dir": str(bundle_root),
        "zip_path": str(zip_path) if zip_path else None,
        "stamp": stamp,
        "variants": ",".join(variants),
    }


def list_training_bundles(state: str, *, analysis_root: Optional[Path | str] = None) -> List[Path]:
    root = _analysis_root(analysis_root)
    bundles_dir = _state_root(state, root) / "training_sets"
    if not bundles_dir.exists():
        return []
    return sorted(
        [p for p in bundles_dir.iterdir() if p.is_dir()],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )


def cleanup_training_bundles(
    state: str,
    *,
    analysis_root: Optional[Path | str] = None,
    stamp: Optional[str] = None,
) -> List[Path]:
    root = _analysis_root(analysis_root)
    bundles_dir = _state_root(state, root) / "training_sets"
    if not bundles_dir.exists():
        return []
    removed: List[Path] = []
    if stamp:
        target = bundles_dir / stamp
        if target.exists():
            shutil.rmtree(target)
            removed.append(target)
        archive = bundles_dir / f"{stamp}.zip"
        if archive.exists():
            archive.unlink()
    else:
        for entry in bundles_dir.glob("*"):
            if entry.is_dir():
                shutil.rmtree(entry)
                removed.append(entry)
            elif entry.suffix.lower() == ".zip":
                entry.unlink()
                removed.append(entry)
    return removed
