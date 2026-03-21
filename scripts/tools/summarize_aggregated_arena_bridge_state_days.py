#!/usr/bin/env python3
"""Roll up measured bridge rows from outcome-level to state-day units.

This keeps row-level diagnostics intact while adding the performance lens that
collapses Midday/Evening into one state-day result per source family.
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
    _write_csv,
)


SAME_DAY_PROFILES = {
    "direct_same_outcome",
    "same_day_precursor_plus_same_day",
    "same_day_carryforward",
}


def _state_day_profile(profiles: Sequence[str]) -> str:
    values = {str(p or "") for p in profiles if str(p or "").strip()}
    if values & SAME_DAY_PROFILES:
        return "same_day_state"
    if "future_day_decay" in values:
        return "future_day_state"
    return "miss"


def _outcome_span(outcomes: Sequence[str]) -> str:
    ordered = []
    seen = set()
    for outcome in outcomes:
        text = str(outcome or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        ordered.append(text)
    if len(ordered) == 2:
        return "Midday+Evening"
    if len(ordered) == 1:
        return ordered[0]
    return "Unknown"


def _collapse_state_days(rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    grouped: Dict[tuple[str, str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = (
            str(row.get("source_mix") or ""),
            str(row.get("date") or ""),
            str(row.get("state_key") or ""),
        )
        grouped[key].append(row)

    out: List[Dict[str, str]] = []
    for (source_mix, date, state_key), picked in sorted(grouped.items(), key=lambda item: item[0]):
        profiles = [str(row.get("box_resolution_profile") or "") for row in picked]
        state_profile = _state_day_profile(profiles)
        first_event = next((str(row.get("first_box_event") or "").strip() for row in picked if str(row.get("first_box_event") or "").strip()), "")
        out.append(
            {
                "source_mix": source_mix,
                "date": date,
                "state_key": state_key,
                "window_count": str(len({str(row.get('window') or '') for row in picked})),
                "row_count": str(len(picked)),
                "outcome_span": _outcome_span([str(row.get("outcome") or "") for row in picked]),
                "state_day_profile": state_profile,
                "same_day_state": "1" if state_profile == "same_day_state" else "0",
                "future_day_state": "1" if state_profile == "future_day_state" else "0",
                "miss_state": "1" if state_profile == "miss" else "0",
                "first_box_event": first_event,
            }
        )
    return out


def _group_state_days(rows: Sequence[Dict[str, str]], *, key: str) -> List[Dict[str, str]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "")].append(row)

    out: List[Dict[str, str]] = []
    for group_key, picked in sorted(grouped.items(), key=lambda item: item[0]):
        total = len(picked)
        out.append(
            {
                key: group_key,
                "state_days": str(total),
                "same_day_state": _fmt_ratio(sum(r["same_day_state"] == "1" for r in picked), total),
                "future_day_state": _fmt_ratio(sum(r["future_day_state"] == "1" for r in picked), total),
                "miss_state": _fmt_ratio(sum(r["miss_state"] == "1" for r in picked), total),
            }
        )
    return out


def _render_md(
    *,
    raw_rows: Sequence[Dict[str, str]],
    state_day_rows: Sequence[Dict[str, str]],
    by_family: Sequence[Dict[str, str]],
    by_family_span: Sequence[Dict[str, str]],
    out_csv: Path,
    rule_name: str,
) -> str:
    lines: List[str] = [
        "# Aggregated Arena Bridge State-Day Scoreboard",
        "",
        "- Purpose: collapse measured bridge rows from outcome-level into one state-day result per source family, so same-state same-day crossover is visible as one performance unit.",
        f"- Rule analyzed: `{rule_name}`",
        f"- summary_csv: `{out_csv}`",
        f"- outcome rows: `{len(raw_rows)}`",
        f"- state-day rows: `{len(state_day_rows)}`",
        "",
        "## By Family",
        "",
    ]
    lines.extend(_md_table(by_family, ["source_mix", "state_days", "same_day_state", "future_day_state", "miss_state"]))
    lines.extend(
        [
            "",
            "## By Family And Outcome Span",
            "",
        ]
    )
    lines.extend(
        _md_table(
            by_family_span,
            ["source_mix", "outcome_span", "state_days", "same_day_state", "future_day_state", "miss_state"],
        )
    )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `same_day_state` means at least one row for that state-day-family resolved on the same day, including Midday/Evening carry-forward.",
            "- `future_day_state` means no same-day resolution occurred, but a later-day decay hit did.",
            "- `miss_state` means neither same-day nor later-day resolution occurred for that state-day-family.",
            "- `outcome_span` shows whether the family was measured on Midday only, Evening only, or both outcomes for the same state-day.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Summarize measured bridge rows at the state-day level.")
    ap.add_argument("--bridge-rows-csv", nargs="*", default=[str(path) for path in DEFAULT_ROWS])
    ap.add_argument("--rule-name", default="top4_perm")
    ap.add_argument(
        "--out-summary-csv",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-21__AGGREGATED_ARENA__BRIDGE_STATE_DAY_SCOREBOARD.csv",
    )
    ap.add_argument(
        "--out-md",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-21__AGGREGATED_ARENA__BRIDGE_STATE_DAY_SCOREBOARD.md",
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    raw_rows = _normalize_rows([Path(raw) for raw in args.bridge_rows_csv], rule_name=str(args.rule_name))
    state_day_rows = _collapse_state_days(raw_rows)
    by_family = _group_state_days(state_day_rows, key="source_mix")

    grouped: Dict[tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in state_day_rows:
        grouped[(str(row.get("source_mix") or ""), str(row.get("outcome_span") or ""))].append(row)
    by_family_span: List[Dict[str, str]] = []
    for (source_mix, outcome_span), picked in sorted(grouped.items(), key=lambda item: item[0]):
        total = len(picked)
        by_family_span.append(
            {
                "source_mix": source_mix,
                "outcome_span": outcome_span,
                "state_days": str(total),
                "same_day_state": _fmt_ratio(sum(r["same_day_state"] == "1" for r in picked), total),
                "future_day_state": _fmt_ratio(sum(r["future_day_state"] == "1" for r in picked), total),
                "miss_state": _fmt_ratio(sum(r["miss_state"] == "1" for r in picked), total),
            }
        )

    out_csv = Path(args.out_summary_csv)
    out_md = Path(args.out_md)
    combined_rows: List[Dict[str, str]] = []
    for row in by_family:
        merged = dict(row)
        merged["group"] = "family"
        combined_rows.append(merged)
    for row in by_family_span:
        merged = dict(row)
        merged["group"] = "family_span"
        combined_rows.append(merged)

    _write_csv(out_csv, combined_rows)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(
        _render_md(
            raw_rows=raw_rows,
            state_day_rows=state_day_rows,
            by_family=by_family,
            by_family_span=by_family_span,
            out_csv=out_csv,
            rule_name=str(args.rule_name),
        ),
        encoding="utf-8",
    )
    print(f"summary_csv={out_csv}")
    print(f"report_md={out_md}")
    print(f"state_days={len(state_day_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
