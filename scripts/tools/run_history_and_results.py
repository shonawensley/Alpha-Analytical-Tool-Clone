#!/usr/bin/env python3
"""
Run the full pipeline for a given history workbook date and its day-ahead results,
then perform basic validation:
  - winners HTML exists for CT/FL triads from the results file
  - the Set1/Draw1 sequence from the Combined table appears inside at least one
    winners HTML per state (guards against stale tables).

Usage examples:
  PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-date 2025-06-22
  PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-file Pick3StatsC4_2025-06-22.xlsm
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
TABLES_DIR = ROOT / "data" / "outputs" / "tables"
WINNERS_ROOT = ROOT / "reports" / "stable" / "winners_by_date"
RESULTS_DIR = ROOT / "data" / "results"
VALIDATION_LOG_DIR = ROOT / "reports" / "stable" / "validation_logs"
GEN_AUX_DRAWS = ROOT / "scripts" / "auxiliary" / "generate_draws_csv.py"
VALIDATE_TABLES_AUX = ROOT / "scripts" / "tools" / "validate_tables_aux_alignment.py"


@dataclass
class StateCheck:
    state: str
    triads: List[str]
    winners_found: Dict[str, bool]
    sequence_in_html: bool
    sequence_source_csv: str
    sequence_html_file: Optional[str]


@dataclass
class RunSummary:
    history_file: str
    history_date: str
    results_file: str
    results_date: str
    winners_out_dir: str
    state_checks: List[StateCheck]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run pipeline + winners for a history workbook and validate outputs.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--history-date", help="History date (YYYY-MM-DD) to infer Pick3StatsC4_*.xlsm")
    g.add_argument("--history-file", help="Explicit history workbook filename under data/history/")
    p.add_argument(
        "--regen-aux-draws",
        action="store_true",
        help="Regenerate Aux draw CSVs for the sentinel states (CT/FL) from the activated workbook before validation.",
    )
    p.add_argument(
        "--skip-aux-alignment",
        action="store_true",
        help="Skip tables↔aux alignment validation (not recommended).",
    )
    return p.parse_args()


def history_filename_from_date(date_str: str) -> str:
    return f"Pick3StatsC4_{date_str}.xlsm"


def compute_results_date(history_date: str) -> str:
    dt = datetime.strptime(history_date, "%Y-%m-%d")
    return (dt + timedelta(days=1)).strftime("%Y-%m-%d")


def run_subprocess(cmd: List[str]) -> None:
    subprocess.run(cmd, check=True)


def parse_results(results_path: Path) -> Dict[str, List[str]]:
    winners: Dict[str, List[str]] = {}
    pat = re.compile(r"\d{3}")
    for raw in results_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.lower().startswith(("pick", "midday")):
            continue
        nums = pat.findall(line)
        if not nums:
            continue
        # crude state name extraction (first token stripped of digits)
        state_part = re.sub(r"\d", " ", line)
        state_part = re.sub(r"\s+", " ", state_part).strip(" -")
        state_key = state_part.replace(" ", "").title()
        winners[state_key] = nums[:2]
    return winners


def load_set1_sequence(state: str) -> List[str]:
    import pandas as pd

    path = TABLES_DIR / state / "Combined_Combined.csv"
    df = pd.read_csv(path)
    row = df[(df["Set"] == "Set1") & (df["Draw"] == "Draw1") & (df["RowType"] == "draw_data")].iloc[0]

    def norm(val: object) -> str:
        try:
            v = int(float(val))
            return f"{v:03d}"
        except Exception:
            s = str(val)
            return s.zfill(3) if s.isdigit() else s

    return [norm(row[str(i)]) for i in range(7, 0, -1)]


def winners_presence_and_sequence(state: str, triads: List[str], seq: List[str], winners_dir: Path) -> Tuple[Dict[str, bool], bool, Optional[str]]:
    found = {t: False for t in triads}
    seq_found = False
    seq_file: Optional[str] = None
    pat = re.compile(r"winner_(\d{3})_")
    for html in winners_dir.glob("*.html"):
        m = pat.search(html.name)
        if m and m.group(1) in found:
            found[m.group(1)] = True
        text = html.read_text(errors="ignore")
        if all(s in text for s in seq):
            seq_found = True
            seq_file = str(html)
    return found, seq_found, seq_file


def main() -> None:
    args = parse_args()
    if args.history_date:
        history_date = args.history_date
        history_file = history_filename_from_date(history_date)
    else:
        history_file = args.history_file
        history_date = history_file.replace("Pick3StatsC4_", "").replace(".xlsm", "").replace("_", "-")

    results_date = compute_results_date(history_date)
    history_path = ROOT / "data" / "history" / history_file
    results_path = RESULTS_DIR / f"{results_date}.txt"

    if not history_path.exists():
        raise SystemExit(f"History workbook not found: {history_path}")
    if not results_path.exists():
        raise SystemExit(f"Results file not found: {results_path}")

    winners_out = WINNERS_ROOT / results_date
    winners_out.mkdir(parents=True, exist_ok=True)

    # 1) Activate history workbook + regenerate tables
    run_subprocess([sys.executable, str(ROOT / "scripts" / "tools" / "run_tables_with_guard.py"), "--history-file", history_file])

    # 1b) Optional: regenerate Aux draw CSVs (CT/FL) from the activated workbook so Aux signals
    # match the same "world snapshot" as the tables.
    if args.regen_aux_draws:
        run_subprocess(
            [
                sys.executable,
                str(GEN_AUX_DRAWS),
                "--states",
                "Connecticut",
                "Florida",
                "--max-draws",
                "1000",
            ]
        )

    # 1c) Validate tables↔aux alignment for sentinel states (guards against stale/mismatched draws).
    if not args.skip_aux_alignment:
        try:
            for state in ("Connecticut4", "Florida4"):
                run_subprocess([sys.executable, str(VALIDATE_TABLES_AUX), "--state", state])
        except subprocess.CalledProcessError:
            raise SystemExit(
                "Tables↔Aux alignment failed. "
                "If you just swapped workbooks, re-run with --regen-aux-draws "
                "or regenerate the Aux draw CSVs from the active workbook."
            )

    # 2) Generate winners for the day-ahead results
    run_subprocess(
        [
            sys.executable,
            str(ROOT / "scripts" / "tools" / "generate_winners_from_results.py"),
            "--results-file",
            str(results_path),
            "--out-dir",
            str(winners_out),
        ]
    )

    # 3) Validate CT/FL presence + sequence
    winners_map = parse_results(results_path)
    summaries: List[StateCheck] = []
    for state in ("Connecticut4", "Florida4"):
        triads = winners_map.get(state.replace("4", ""), []) or winners_map.get(state, [])
        # Fall back to title-case key if needed
        if not triads:
            triads = winners_map.get(state, [])
        if len(triads) < 2:
            triads = triads or ["N/A"]
        seq = load_set1_sequence(state)
        found, seq_found, seq_file = winners_presence_and_sequence(state, triads, seq, winners_out / state)
        summaries.append(
            StateCheck(
                state=state,
                triads=triads,
                winners_found=found,
                sequence_in_html=seq_found,
                sequence_source_csv=str(TABLES_DIR / state / "Combined_Combined.csv"),
                sequence_html_file=seq_file,
            )
        )

    summary = RunSummary(
        history_file=str(history_path),
        history_date=history_date,
        results_file=str(results_path),
        results_date=results_date,
        winners_out_dir=str(winners_out),
        state_checks=summaries,
    )

    VALIDATION_LOG_DIR.mkdir(parents=True, exist_ok=True)
    out_path = VALIDATION_LOG_DIR / f"validation_{results_date}.json"
    out_path.write_text(json.dumps(asdict(summary), indent=2))
    print(f"Validation summary written to {out_path}")
    for check in summaries:
        print(
            f"{check.state}: triads={check.triads} winners_found={check.winners_found} "
            f"sequence_in_html={check.sequence_in_html} seq_html={check.sequence_html_file}"
        )


if __name__ == "__main__":
    main()
