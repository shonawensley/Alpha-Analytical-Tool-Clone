#!/usr/bin/env python3
"""
Build a "predictive" (no-results) day snapshot from a history workbook.

This is a workflow helper for "live-style" runs where results D do not exist yet.
It:
  1) Activates a Pick3StatsC4 history workbook (H) into data/original/.
  2) Regenerates tables + JSON mirrors (world snapshot for tools).
  3) Runs Brain-1 analyzers WITHOUT winners:
       - Stable patterns
       - Digit Reduction + Analyzer V2
       - Hot Zones
       - Enhanced VTRAC analyzer bundle
  4) Freezes Brain-1 artifacts into an isolated sharepack root (default: sharepacks/_predictive/<D>/).
  5) Generates Aux draw snapshots + Part 3 summaries into the sharepack (from the same workbook H).
  6) Exports Brain-2 Control Center artifacts into the sharepack using an empty placeholder results file.

It intentionally does NOT:
  - Generate winners HTML (requires results).
  - Run Profit Alerts evaluation (requires results).

Example (H=2026-01-06 -> D=2026-01-07):
  PYTHONPATH=.:src python3 scripts/tools/run_predictive_day.py --history-date 2026-01-06
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from utils import path_handler as ph  # noqa: E402
from core import stable_pattern_extractor  # noqa: E402
from core.module_b_digit_reduction import run_digit_reduction  # noqa: E402
from alpha_analytical.digit_reduction.analyzer_v2 import run as run_dr_analyzer_v2  # noqa: E402
from alpha_analytical.hot_zones import (  # noqa: E402
    load_table_env_from_json,
    HotScanConfig,
    HotZoneScanner,
    HotZoneWeights,
    write_hotzones_artifacts,
    write_winner_map,
)
from modules import vtrac_enhanced as ve  # noqa: E402


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


def _history_filename_candidates_from_date(date_str: str) -> List[str]:
    return [
        f"Pick3StatsC4_{date_str}.xlsm",
        f"Pick3StatsC4_{date_str.replace('-', '_')}.xlsm",
    ]


def _compute_results_date(history_date: str) -> str:
    dt = datetime.strptime(history_date, "%Y-%m-%d")
    return (dt + timedelta(days=1)).strftime("%Y-%m-%d")


def _resolve_history_workbook(args: argparse.Namespace) -> tuple[str, str, Path]:
    if args.history_date:
        history_date = args.history_date.strip()
        candidates = _history_filename_candidates_from_date(history_date)
        hits = [REPO_ROOT / "data" / "history" / name for name in candidates]
        hit = next((p for p in hits if p.exists()), None)
        if not hit:
            raise SystemExit(f"History workbook not found for {history_date}. Expected one of: {', '.join(candidates)}")
        history_file = hit.name
        history_path = hit
        return history_file, history_date, history_path

    history_file = args.history_file.strip()
    history_path = REPO_ROOT / "data" / "history" / history_file
    if not history_path.exists():
        raise SystemExit(f"History workbook not found: {history_path}")

    history_date = history_file.replace("Pick3StatsC4_", "").replace(".xlsm", "").replace("_", "-")
    return history_file, history_date, history_path


def _activate_workbook(history_path: Path) -> str:
    dest = Path(ph.get_excel_path())
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(history_path, dest)
    return str(dest)


def _run_tables_guard(excel_path: str) -> None:
    from core.pipeline_runner import run_tables_with_guard

    summary = run_tables_with_guard(excel_path)
    if summary.get("skipped"):
        print("[OK] Tables already up to date for active workbook.")
    else:
        print("[OK] Tables regenerated for active workbook.")


def _run_hot_zones(state: str, *, date_label: str) -> None:
    json_dir = Path(ph.get_json_tables_dir())
    json_path = json_dir / f"{state}_tables.json"
    if not json_path.exists():
        raise SystemExit(f"Missing JSON tables for Hot Zones: {json_path}")

    out_dir = Path(ph.get_analysis_dir("hot_zones", state))
    env = load_table_env_from_json(json_path)
    scanner = HotZoneScanner(env, HotScanConfig(), HotZoneWeights())
    per_items, tops = scanner.scan()
    meta = {
        "state": state,
        "date": date_label,
        "json_source": str(json_path),
        "per_item_rows": len(per_items),
        "top_rows": len(tops),
        "guard_triads_total": sum(1 for row in tops if row.guard_hits > 0),
        "guard_triads_top20": sum(1 for row in tops[:20] if row.guard_hits > 0),
    }
    write_hotzones_artifacts(state, str(out_dir), per_items, tops, meta)
    write_winner_map(state, date_label, str(out_dir), tops)


def _run_vtrac_enhanced(state: str) -> None:
    engine_input = ve.build_engine_input_from_tables(state)
    weights = ve.DEFAULT_WEIGHTS.clone()
    mask_default = set("".join(sorted(ve.suggested_mask_digits(engine_input.recent_draws))))
    output = ve.run_analysis(engine_input, weights=weights, digits_to_mask=mask_default)
    ve.write_prediction_bundle(state, output, engine_input=engine_input)


def _write_placeholder_results(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("State\tMidday\tEvening\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build a predictive (no-results) sharepack day from a history workbook.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--history-date", help="History date H (YYYY-MM-DD) to infer Pick3StatsC4_*.xlsm")
    g.add_argument("--history-file", help="Explicit history workbook filename under data/history/")
    p.add_argument("--results-date", default=None, help="Override results date D (default: H+1)")
    p.add_argument("--states", nargs="*", help="Optional subset of states (default: tracked list)")
    p.add_argument(
        "--sharepacks-root",
        default=str(REPO_ROOT / "sharepacks" / "_predictive"),
        help="Sharepacks root directory (default: sharepacks/_predictive/)",
    )
    p.add_argument(
        "--skip-freeze",
        action="store_true",
        help="Skip freezing to sharepacks (runs tools only).",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="If the sharepack day exists and is non-empty, rebuild it safely (moves existing to _rebuild_backup/).",
    )
    p.add_argument(
        "--skip-aux",
        action="store_true",
        help="Skip Aux draw snapshot + summary generation into the sharepack.",
    )
    p.add_argument(
        "--skip-control-center",
        action="store_true",
        help="Skip Control Center export into the sharepack.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    history_file, history_date, history_path = _resolve_history_workbook(args)
    results_date = args.results_date.strip() if args.results_date else _compute_results_date(history_date)

    states = list(args.states) if args.states else list(DEFAULT_STATES)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    print(f"[INFO] H={history_date} ({history_file}) -> D={results_date}")
    print(f"[INFO] sharepacks_root={sharepacks_root}")

    # 1) Activate workbook + regenerate tables/json
    active_excel = _activate_workbook(history_path)
    _run_tables_guard(active_excel)

    # 2) Run Brain-1 analyzers (no winners)
    for state in states:
        tables_dir = Path(ph.get_state_tables_dir(state))
        stable_out = Path(ph.get_analysis_dir("patterns", state))
        dr_out = Path(ph.get_analysis_dir("digit_reduction", state))

        stable_pattern_extractor.run_stable_pattern_extraction(
            state=state,
            tables_path=tables_dir,
            out_path=stable_out,
            winners=None,
        )
        run_digit_reduction(state=state, tables_path=tables_dir, out_path=dr_out)
        run_dr_analyzer_v2(state, analysis_root=Path(ph.get_analysis_output_dir()) / "digit_reduction")
        _run_hot_zones(state, date_label=results_date)
        _run_vtrac_enhanced(state)

    if args.skip_freeze:
        print("[OK] Tool runs complete (freeze skipped).")
        return

    # 3) Freeze Brain-1 into sharepack root (skip global VTRAC validation bundle: results do not exist)
    freeze_cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "tools" / "freeze_sharepack_day.py"),
        "--date",
        results_date,
        "--sharepacks-root",
        str(sharepacks_root),
        "--skip-global-vtrac",
        "--skip-winners",
    ]
    if bool(args.force):
        freeze_cmd.append("--force")
    if states and states != DEFAULT_STATES:
        freeze_cmd.extend(["--states", *states])
    subprocess.run(freeze_cmd, check=True)

    # 4) Aux summaries (optional)
    if not args.skip_aux:
        for state in states:
            subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "tools" / "aux_sharepack_summary.py"),
                    "--date",
                    results_date,
                    "--state",
                    state,
                    "--excel",
                    str(history_path),
                    "--sharepacks-root",
                    str(sharepacks_root),
                ],
                check=True,
            )

    # 5) Control Center export (optional)
    if not args.skip_control_center:
        placeholder = sharepacks_root / results_date / "results_placeholder.txt"
        _write_placeholder_results(placeholder)
        subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "tools" / "export_control_center_sharepack.py"),
                "--date",
                results_date,
                "--sharepacks-root",
                str(sharepacks_root),
                "--results-file",
                str(placeholder),
            ],
            check=True,
        )

    print(f"[OK] Predictive pack built under {sharepacks_root / results_date}")


if __name__ == "__main__":
    main()
