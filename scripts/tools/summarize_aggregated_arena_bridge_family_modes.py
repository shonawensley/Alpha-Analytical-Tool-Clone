#!/usr/bin/env python3
"""Summarize measured bridge families by source-family and reviewed outcome.

This keeps bridge research in measurement mode. It makes family/mode evidence
explicit and tags each slice with a simple sample-size band so we can separate
repeatable findings from thin anecdotes.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import sys
from typing import Dict, List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.summarize_aggregated_arena_bridge_families import (
    DEFAULT_ROWS,
    _fmt_ratio,
    _md_table,
    _normalize_rows,
    _profile_count,
    _write_csv,
)


def _sample_band(total: int, *, thin_threshold: int, measured_threshold: int) -> str:
    if total < thin_threshold:
        return "thin"
    if total < measured_threshold:
        return "provisional"
    return "measured"


def _mode_hint(direct: int, precursor: int, carry: int, future: int, miss: int) -> str:
    same_day = direct + precursor + carry
    if same_day == 0 and future == 0:
        return "all_miss"
    if miss == 0 and future == 0:
        return "same_day_only"
    if miss == 0 and same_day == 0:
        return "future_day_only"
    if future > 0 and same_day > 0 and miss == 0:
        return "resolved_mixed"
    if same_day > 0 and future == 0 and miss > 0:
        return "same_day_mixed"
    if future > 0 and same_day == 0 and miss > 0:
        return "future_day_mixed"
    if same_day > 0 and future > 0 and miss > 0:
        return "mixed_all_modes"
    return "unclear"


def _family_mode_summary(
    rows: Sequence[Dict[str, str]], *, thin_threshold: int, measured_threshold: int
) -> List[Dict[str, str]]:
    grouped: Dict[tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("source_mix") or ""), str(row.get("outcome") or ""))].append(row)

    out: List[Dict[str, str]] = []
    for (source_mix, outcome), picked in sorted(grouped.items(), key=lambda item: item[0]):
        total = len(picked)
        direct = _profile_count(picked, "direct_same_outcome")
        precursor = _profile_count(picked, "same_day_precursor_plus_same_day")
        carry = _profile_count(picked, "same_day_carryforward")
        future = _profile_count(picked, "future_day_decay")
        miss = _profile_count(picked, "miss")
        same_day_any = direct + precursor + carry
        resolved_any = total - miss
        out.append(
            {
                "source_mix": source_mix,
                "outcome": outcome,
                "rows": str(total),
                "sample_band": _sample_band(
                    total, thin_threshold=thin_threshold, measured_threshold=measured_threshold
                ),
                "mode_hint": _mode_hint(direct, precursor, carry, future, miss),
                "same_day_any": _fmt_ratio(same_day_any, total),
                "resolved_any": _fmt_ratio(resolved_any, total),
                "direct_same_outcome": _fmt_ratio(direct, total),
                "same_day_precursor_plus_same_day": _fmt_ratio(precursor, total),
                "same_day_carryforward": _fmt_ratio(carry, total),
                "future_day_decay": _fmt_ratio(future, total),
                "miss": _fmt_ratio(miss, total),
            }
        )
    return out


def _render_md(
    *,
    rows: Sequence[Dict[str, str]],
    summary_rows: Sequence[Dict[str, str]],
    rule_name: str,
    out_summary_csv: Path,
    thin_threshold: int,
    measured_threshold: int,
) -> str:
    lines: List[str] = [
        "# Aggregated Arena Bridge Family Mode Scoreboard",
        "",
        "- Purpose: summarize bridge evidence by source family plus reviewed outcome, with simple sample-size bands so thin slices are not over-read.",
        f"- Rule analyzed: `{rule_name}`",
        f"- summary_csv: `{out_summary_csv}`",
        f"- total bridge rows: `{len(rows)}`",
        f"- sample bands: `thin < {thin_threshold}`, `provisional < {measured_threshold}`, `measured >= {measured_threshold}`",
        "",
    ]

    lines.append("## Family + Mode")
    lines.append("")
    lines.extend(
        _md_table(
            summary_rows,
            [
                "source_mix",
                "outcome",
                "rows",
                "sample_band",
                "mode_hint",
                "same_day_any",
                "resolved_any",
                "direct_same_outcome",
                "same_day_precursor_plus_same_day",
                "same_day_carryforward",
                "future_day_decay",
                "miss",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Guidance",
            "",
            "- `thin` means the slice is interesting but too small for a strong judgment.",
            "- `provisional` means the slice is worth studying, but not promoting.",
            "- `measured` means the slice has enough rows to guide the next bounded study mode more confidently.",
            "- `same_day_any` counts direct, same-day precursor+same-day, and same-day carry-forward together.",
            "- `resolved_any` counts any non-miss resolution, including future-day decay.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Summarize measured bridge families by source-family and reviewed outcome.")
    ap.add_argument("--bridge-rows-csv", nargs="*", default=[str(path) for path in DEFAULT_ROWS])
    ap.add_argument("--rule-name", default="top4_perm")
    ap.add_argument("--thin-threshold", type=int, default=3)
    ap.add_argument("--measured-threshold", type=int, default=5)
    ap.add_argument(
        "--out-summary-csv",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_FAMILY_MODE_SCOREBOARD.csv",
    )
    ap.add_argument(
        "--out-md",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_FAMILY_MODE_SCOREBOARD.md",
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    rows = _normalize_rows([Path(raw) for raw in args.bridge_rows_csv], rule_name=str(args.rule_name))
    summary_rows = _family_mode_summary(
        rows,
        thin_threshold=int(args.thin_threshold),
        measured_threshold=int(args.measured_threshold),
    )

    out_summary_csv = Path(args.out_summary_csv)
    out_md = Path(args.out_md)
    _write_csv(out_summary_csv, summary_rows)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(
        _render_md(
            rows=rows,
            summary_rows=summary_rows,
            rule_name=str(args.rule_name),
            out_summary_csv=out_summary_csv,
            thin_threshold=int(args.thin_threshold),
            measured_threshold=int(args.measured_threshold),
        ),
        encoding="utf-8",
    )
    print(f"summary_csv={out_summary_csv}")
    print(f"report_md={out_md}")
    print(f"rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
