#!/usr/bin/env python3
"""Summarize measured bridge families across one or more bridge-study CSVs.

This stays in research mode. It turns row-level bridge-study outputs into a
compact family scoreboard so we can compare direct same-outcome closure,
same-day carry-forward, future-day decay, and misses by source family.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

DEFAULT_ROWS = (
    RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_GATED_ROWS.csv",
    RUNS_DIR / "2026-01-05_to_2026-01-09__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_GATED_ROWS.csv",
    RUNS_DIR / "2025-06-21_to_2025-06-24__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_GATED_ROWS.csv",
    RUNS_DIR / "2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS.csv",
)


def _read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _infer_window(path: Path) -> str:
    name = path.stem
    marker = "__AGGREGATED_ANALYSIS_ARENA__"
    return name.split(marker)[0] if marker in name else name


def _fmt_ratio(num: int, den: int) -> str:
    return f"{num}/{den}" if den else "0/0"


def _profile_count(rows: Sequence[Dict[str, str]], profile: str) -> int:
    return sum(str(row.get("box_resolution_profile") or "") == profile for row in rows)


def _normalize_rows(paths: Sequence[Path], *, rule_name: str) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for path in paths:
        if not path.exists():
            continue
        window = _infer_window(path)
        for row in _read_csv(path):
            if str(row.get("rule_name") or "") != rule_name:
                continue
            merged = dict(row)
            merged["window"] = window
            out.append(merged)
    return out


def _group_summary(rows: Sequence[Dict[str, str]], *, key: str) -> List[Dict[str, str]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "")].append(row)

    out: List[Dict[str, str]] = []
    for group_key, picked in sorted(grouped.items(), key=lambda item: item[0]):
        total = len(picked)
        out.append(
            {
                key: group_key,
                "rows": str(total),
                "direct_same_outcome": _fmt_ratio(_profile_count(picked, "direct_same_outcome"), total),
                "same_day_precursor_plus_same_day": _fmt_ratio(
                    _profile_count(picked, "same_day_precursor_plus_same_day"), total
                ),
                "same_day_carryforward": _fmt_ratio(_profile_count(picked, "same_day_carryforward"), total),
                "future_day_decay": _fmt_ratio(_profile_count(picked, "future_day_decay"), total),
                "miss": _fmt_ratio(_profile_count(picked, "miss"), total),
            }
        )
    return out


def _write_csv(path: Path, rows: Sequence[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: List[str] = []
    seen = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _md_table(rows: Sequence[Dict[str, str]], columns: Sequence[str]) -> List[str]:
    if not rows:
        return ["_None._"]
    lines = [
        "| " + " | ".join(columns) + " |",
        "|---" * len(columns) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return lines


def _render_md(
    *,
    rows: Sequence[Dict[str, str]],
    by_family: Sequence[Dict[str, str]],
    by_outcome: Sequence[Dict[str, str]],
    by_family_outcome: Sequence[Dict[str, str]],
    rule_name: str,
    summary_csv: Path,
) -> str:
    columns = [
        "rows",
        "direct_same_outcome",
        "same_day_precursor_plus_same_day",
        "same_day_carryforward",
        "future_day_decay",
        "miss",
    ]
    lines: List[str] = [
        "# Aggregated Arena Bridge Family Scoreboard",
        "",
        "- Purpose: summarize measured bridge families by direct closure, same-day carry-forward, future-day decay, and miss across the current frozen-window corpus.",
        f"- Rule analyzed: `{rule_name}`",
        f"- summary_csv: `{summary_csv}`",
        f"- total rows: `{len(rows)}`",
        "",
        "## By Family",
        "",
    ]
    lines.extend(_md_table(by_family, ["source_mix", *columns]))
    lines.extend([
        "",
        "## By Reviewed Outcome",
        "",
    ])
    lines.extend(_md_table(by_outcome, ["outcome", *columns]))
    lines.extend([
        "",
        "## By Family And Outcome",
        "",
    ])
    lines.extend(_md_table(by_family_outcome, ["source_mix", "outcome", *columns]))
    lines.extend([
        "",
        "## Notes",
        "",
        "- `direct_same_outcome` means the bridge hit the reviewed row itself.",
        "- `same_day_precursor_plus_same_day` means the bridge already hit another same-day outcome while still hitting the reviewed row.",
        "- `same_day_carryforward` means the bridge missed the reviewed row but converted on the other draw from the same day.",
        "- `future_day_decay` means the bridge resolved only on a later day inside the measured horizon.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Summarize measured bridge families across one or more bridge-study CSVs.")
    ap.add_argument("--bridge-rows-csv", nargs="*", default=[str(path) for path in DEFAULT_ROWS])
    ap.add_argument("--rule-name", default="top4_perm")
    ap.add_argument(
        "--out-summary-csv",
        default=str(RUNS_DIR / "2026-03-20__AGGREGATED_ARENA__BRIDGE_FAMILY_SCOREBOARD.csv"),
    )
    ap.add_argument(
        "--out-md",
        default=str(RUNS_DIR / "2026-03-20__AGGREGATED_ARENA__BRIDGE_FAMILY_SCOREBOARD.md"),
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    rows = _normalize_rows([Path(raw) for raw in args.bridge_rows_csv], rule_name=str(args.rule_name))
    by_family = _group_summary(rows, key="source_mix")
    by_outcome = _group_summary(rows, key="outcome")

    family_outcome_rows: List[Dict[str, str]] = []
    grouped: Dict[tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("source_mix") or ""), str(row.get("outcome") or ""))].append(row)
    for (source_mix, outcome), picked in sorted(grouped.items(), key=lambda item: item[0]):
        total = len(picked)
        family_outcome_rows.append(
            {
                "source_mix": source_mix,
                "outcome": outcome,
                "rows": str(total),
                "direct_same_outcome": _fmt_ratio(_profile_count(picked, "direct_same_outcome"), total),
                "same_day_precursor_plus_same_day": _fmt_ratio(
                    _profile_count(picked, "same_day_precursor_plus_same_day"), total
                ),
                "same_day_carryforward": _fmt_ratio(_profile_count(picked, "same_day_carryforward"), total),
                "future_day_decay": _fmt_ratio(_profile_count(picked, "future_day_decay"), total),
                "miss": _fmt_ratio(_profile_count(picked, "miss"), total),
            }
        )

    out_summary_csv = Path(args.out_summary_csv)
    out_md = Path(args.out_md)
    combined_rows: List[Dict[str, str]] = []
    for row in by_family:
        merged = dict(row)
        merged["group"] = "family"
        combined_rows.append(merged)
    for row in by_outcome:
        merged = dict(row)
        merged["group"] = "outcome"
        combined_rows.append(merged)
    for row in family_outcome_rows:
        merged = dict(row)
        merged["group"] = "family_outcome"
        combined_rows.append(merged)

    _write_csv(out_summary_csv, combined_rows)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(
        _render_md(
            rows=rows,
            by_family=by_family,
            by_outcome=by_outcome,
            by_family_outcome=family_outcome_rows,
            rule_name=str(args.rule_name),
            summary_csv=out_summary_csv,
        ),
        encoding="utf-8",
    )
    print(f"summary_csv={out_summary_csv}")
    print(f"report_md={out_md}")
    print(f"rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
