#!/usr/bin/env python3
"""
Freeze Brain-1 artifacts into a day sharepack folder (multi-day safe).

Why:
  Live output folders (especially Digit Reduction overlays and Hot Zones winner maps)
  can accumulate multiple runs/dates. A naive `cp -a .../.` risks contaminating a
  day sharepack with stale files from other runs.

This script copies only the lean, day-relevant artifacts into:
  sharepacks/<D>/<STATE>/...
  sharepacks/<D>/vtrac_compact_report.*
  sharepacks/<D>/summary.*
  sharepacks/<D>/*.zip (VTRAC payloads, if present)

It does NOT generate Aux or Control Center exports. Run separately:
  - python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE> --excel data/history/Pick3StatsC4_<H>.xlsm
  - python3 scripts/tools/export_control_center_sharepack.py --date <D>

Usage:
  python3 scripts/tools/freeze_sharepack_day.py --date 2025-06-22
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Iterable, List


ROOT = Path(__file__).resolve().parents[2]

DEFAULT_STATES: List[str] = [
    "Connecticut4",
    "Delaware4",
    "Florida4",
    "Indiana4",
    "Michigan4",
    "NewJersey4",
    "NewYork4",
    "NorthCarolina4",
    "Ohio4",
    "OntarioCanada4",
    "Pennsylvania4",
    "PuertoRico4",
    "SouthCarolina4",
    "Virginia4",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Freeze Brain-1 artifacts into sharepacks/<D>/ (multi-day safe).")
    p.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD), e.g. 2025-06-22")
    p.add_argument("--states", nargs="*", help="Optional subset of states (default: tracked list)")
    return p.parse_args()


def _abort_if_nonempty(path: Path) -> None:
    if path.exists() and any(path.iterdir()):
        raise SystemExit(f"[ABORT] {path} exists and is non-empty; refusing to overwrite")


def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _copy_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)


def _copy_many(files: Iterable[Path], dst_dir: Path) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        if f.is_file():
            shutil.copy2(f, dst_dir / f.name)


def _copy_latest_winner_files(src_dir: Path, dst_dir: Path) -> None:
    """
    Copy only the newest HTML/JSON winner artifacts per (base, ext).

    Live winners folders can accumulate many timestamped runs for the same winner/index.
    This keeps sharepacks deterministic without deleting anything from live outputs.
    """
    dst_dir.mkdir(parents=True, exist_ok=True)
    newest: dict[tuple[str, str], tuple[float, Path]] = {}

    for path in src_dir.iterdir():
        if not path.is_file():
            continue
        if path.suffix not in {".html", ".json"}:
            continue

        stem_parts = path.stem.split("_")
        base = path.stem
        if (
            len(stem_parts) >= 6
            and len(stem_parts[-2]) == 8
            and stem_parts[-2].isdigit()
            and len(stem_parts[-1]) == 6
            and stem_parts[-1].isdigit()
        ):
            base = "_".join(stem_parts[:-2])

        mtime = path.stat().st_mtime
        key = (base, path.suffix)
        prev = newest.get(key)
        if prev is None or mtime > prev[0]:
            newest[key] = (mtime, path)

    for _, src in sorted(newest.values(), key=lambda t: t[0]):
        shutil.copy2(src, dst_dir / src.name)


def main() -> None:
    args = parse_args()
    date = args.date.strip()
    states = list(args.states) if args.states else list(DEFAULT_STATES)

    share_day = ROOT / "sharepacks" / date
    _abort_if_nonempty(share_day)
    share_day.mkdir(parents=True, exist_ok=True)

    tables_dir = ROOT / "data" / "outputs" / "tables"
    json_dir = ROOT / "data" / "outputs" / "json_tables"
    winners_dir = ROOT / "reports" / "stable" / "winners_by_date" / date

    patterns_dir = ROOT / "data" / "outputs" / "analysis" / "patterns"
    dr_dir = ROOT / "data" / "outputs" / "analysis" / "digit_reduction"
    vtrac_dir = ROOT / "data" / "outputs" / "analysis" / "vtrac"
    vtrac_val_dir = ROOT / "data" / "outputs" / "analysis" / "vtrac_validation"
    hz_dir = ROOT / "data" / "outputs" / "analysis" / "hot_zones"

    for state in states:
        dest_state = share_day / state
        (dest_state / "tables").mkdir(parents=True, exist_ok=True)
        (dest_state / "json").mkdir(parents=True, exist_ok=True)

        # Tables
        for name in ("Combined_Combined.csv", "Midday_Combined.csv", "Evening_Combined.csv"):
            src = tables_dir / state / name
            if not src.exists():
                raise SystemExit(f"Missing tables file for {state}: {src}")
            _copy_file(src, dest_state / "tables" / name)

        # JSON tables
        json_src = json_dir / f"{state}_tables.json"
        if not json_src.exists():
            raise SystemExit(f"Missing JSON tables for {state}: {json_src}")
        _copy_file(json_src, dest_state / "json" / f"{state}_tables.json")

        # Winners lens (date-scoped)
        winners_src = winners_dir / state
        if winners_src.exists():
            _copy_latest_winner_files(winners_src, dest_state / "winners" / state)

        # Stable (lean artifacts; avoid dragging older bundles)
        stable_src = patterns_dir / state
        stable_dest = dest_state / "stable" / state
        stable_dest.mkdir(parents=True, exist_ok=True)

        stable_required = [
            f"{state}_stable_patterns_scores.csv",
            f"{state}_stable_patterns_families.csv",
            f"{state}_stable_patterns_compound.csv",
            f"{state}_metrics.json",
            f"{state}_stable_patterns_report.html",
        ]
        for fname in stable_required:
            src = stable_src / fname
            if src.exists():
                _copy_file(src, stable_dest / fname)

        # Spotlights + newest training bundle only when winners exist for the day.
        if winners_src.exists():
            for fname in (f"{state}_winner_family_spotlight_raw.csv", f"{state}_winner_family_spotlight_families.csv"):
                src = stable_src / fname
                if src.exists():
                    _copy_file(src, stable_dest / fname)
            ts_root = stable_src / "training_sets"
            if ts_root.exists():
                bundles = [p for p in ts_root.iterdir() if p.is_dir()]
                if bundles:
                    latest = max(bundles, key=lambda p: p.stat().st_mtime)
                    _copy_tree(latest, stable_dest / "training_sets" / latest.name)

        # Digit Reduction (lean artifacts; only newest overlay stamp when winners exist)
        dr_src = dr_dir / state
        dr_dest = dest_state / "digit_reduction" / state
        dr_dest.mkdir(parents=True, exist_ok=True)
        if dr_src.exists():
            _copy_many([p for p in dr_src.iterdir() if p.is_file()], dr_dest)
            _copy_tree(dr_src / "training", dr_dest / "training")
            analyzer_src = dr_src / "analyzer_v2"
            analyzer_dest = dr_dest / "analyzer_v2"
            analyzer_dest.mkdir(parents=True, exist_ok=True)
            if analyzer_src.exists():
                _copy_many([p for p in analyzer_src.iterdir() if p.is_file()], analyzer_dest)
                if winners_src.exists():
                    wsrc = analyzer_src / "winners"
                    if wsrc.exists():
                        stamp_files = [p for p in wsrc.glob("*_winner_stamp.json") if p.is_file()]
                        if stamp_files:
                            latest_stamp = max(stamp_files, key=lambda p: p.stat().st_mtime)
                            stamp = latest_stamp.name.split("_", 1)[0]
                            (analyzer_dest / "winners").mkdir(parents=True, exist_ok=True)
                            for f in sorted(wsrc.glob(f"{stamp}_*")):
                                if f.is_file():
                                    _copy_file(f, analyzer_dest / "winners" / f.name)

        # VTRAC (newest enhanced JSON + validation report)
        vtrac_src = vtrac_dir / state
        vtrac_dest = dest_state / "vtrac" / state
        vtrac_dest.mkdir(parents=True, exist_ok=True)
        enhanced = sorted(vtrac_src.glob(f"{state}_vtrac_enhanced_*.json"), key=lambda p: p.stat().st_mtime)
        if enhanced:
            _copy_file(enhanced[-1], vtrac_dest / enhanced[-1].name)
        val_src_dir = vtrac_val_dir / state
        for fname in ("validation_report.json", "validation_report.md"):
            src = val_src_dir / fname
            if src.exists():
                _copy_file(src, vtrac_dest / fname)

        # Hot Zones (current day winner maps only)
        hz_src = hz_dir / state
        hz_dest = dest_state / "hot_zones" / state
        hz_dest.mkdir(parents=True, exist_ok=True)
        for fname in (
            f"{state}_hot_zones_per_lane.csv",
            f"{state}_hot_zones_top_lanes.csv",
            f"{state}_hot_zones_meta.json",
            f"{date}_hot_zones_winner_map.csv",
            f"{date}_hot_zones_winner_map.json",
        ):
            src = hz_src / fname
            if src.exists():
                _copy_file(src, hz_dest / fname)

    # Day-level VTRAC artifacts (copy once)
    for fname in (
        "summary.md",
        "summary.csv",
        "vtrac_compact_report.json",
        "vtrac_compact_report.csv",
        "vtrac_pro_payload.zip",
        "vtrac_validation_full_payload.zip",
    ):
        src = vtrac_val_dir / fname
        if src.exists():
            _copy_file(src, share_day / fname)

    print(f"[OK] Frozen Brain-1 into {share_day}")


if __name__ == "__main__":
    main()
