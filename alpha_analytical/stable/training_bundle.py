from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd

DEFAULT_ANALYSIS_ROOT = Path("data/outputs/analysis/patterns")


def _resolve_root(root: Optional[str | Path]) -> Path:
    return Path(root) if root is not None else DEFAULT_ANALYSIS_ROOT


def _state_dir(state: str, analysis_root: Path) -> Path:
    return analysis_root / state


def _copy(src: Optional[str | Path], dest_root: Path, subdir: Optional[str] = None) -> Optional[Path]:
    if not src:
        return None
    src_path = Path(src)
    if not src_path.exists():
        return None
    target_dir = dest_root / subdir if subdir else dest_root
    target_dir.mkdir(parents=True, exist_ok=True)
    dest = target_dir / src_path.name
    shutil.copy2(src_path, dest)
    return dest


def _load_optional_csv(path: Optional[str | Path]) -> Optional[pd.DataFrame]:
    if not path:
        return None
    csv_path = Path(path)
    if not csv_path.exists():
        return None
    try:
        return pd.read_csv(csv_path)
    except Exception:
        return None


def write_training_bundle(
    *,
    state: str,
    stamp: str,
    analysis_root: Optional[str | Path] = None,
    scores_path: str | Path,
    html_path: Optional[str | Path] = None,
    families_path: Optional[str | Path] = None,
    spotlight_raw_path: Optional[str | Path] = None,
    spotlight_family_path: Optional[str | Path] = None,
    winners: Optional[Iterable[str]] = None,
) -> dict:
    if not stamp:
        raise ValueError("stamp must be provided")

    analysis_root_path = _resolve_root(analysis_root)
    state_dir = _state_dir(state, analysis_root_path)
    bundle_dir = state_dir / "training_sets" / stamp

    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True, exist_ok=True)

    copied_scores = _copy(scores_path, bundle_dir, "artifacts")
    copied_html = _copy(html_path, bundle_dir, "artifacts") if html_path else None
    copied_families = _copy(families_path, bundle_dir, "artifacts") if families_path else None
    copied_spotlight_raw = _copy(spotlight_raw_path, bundle_dir, "artifacts") if spotlight_raw_path else None
    copied_spotlight_family = _copy(spotlight_family_path, bundle_dir, "artifacts") if spotlight_family_path else None

    df_scores = _load_optional_csv(scores_path)
    df_spotlight = _load_optional_csv(spotlight_raw_path)
    df_spotlight_families = _load_optional_csv(spotlight_family_path)

    stats = {
        "total_patterns": int(df_scores.shape[0]) if df_scores is not None else 0,
        "section_counts": df_scores["section"].value_counts().to_dict() if df_scores is not None and "section" in df_scores.columns else {},
        "family_ids": sorted(df_spotlight["family_id"].dropna().unique().tolist()) if df_spotlight is not None and "family_id" in df_spotlight.columns else [],
        "spotlight_rows": int(df_spotlight.shape[0]) if df_spotlight is not None else 0,
        "spotlight_family_rows": int(df_spotlight_families.shape[0]) if df_spotlight_families is not None else 0,
    }

    winners_list = [str(w).strip() for w in (winners or []) if str(w).strip()]

    manifest = {
        "state": state,
        "stamp": stamp,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "analysis_root": str(analysis_root_path.resolve()),
        "winners": winners_list,
        "files": {
            "scores_csv": str(copied_scores.relative_to(bundle_dir)) if copied_scores else None,
            "report_html": str(copied_html.relative_to(bundle_dir)) if copied_html else None,
            "families_csv": str(copied_families.relative_to(bundle_dir)) if copied_families else None,
            "spotlight_raw_csv": str(copied_spotlight_raw.relative_to(bundle_dir)) if copied_spotlight_raw else None,
            "spotlight_families_csv": str(copied_spotlight_family.relative_to(bundle_dir)) if copied_spotlight_family else None,
        },
        "stats": stats,
    }

    manifest_path = bundle_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    return {
        "bundle_dir": str(bundle_dir),
        "manifest": str(manifest_path),
    }
