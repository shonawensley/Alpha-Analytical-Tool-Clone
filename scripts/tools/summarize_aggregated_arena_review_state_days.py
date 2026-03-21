#!/usr/bin/env python3
"""Summarize aggregated arena review scoreboards at the state-day level.

The review harness is intentionally row-based (`date x state x outcome`) because
that is the best diagnostic unit. This tool adds the companion performance lens:
one `date x state` rollup that counts same-state Midday/Evening behavior together.
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

from scripts.tools.summarize_aggregated_arena_bridge_families import _fmt_ratio, _md_table, _read_csv, _write_csv

RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

DEFAULT_REVIEW_CSVS = (
    RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv",
    RUNS_DIR / "2026-01-05_to_2026-01-09__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv",
    RUNS_DIR / "2025-06-21_to_2025-06-24__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv",
    RUNS_DIR / "2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv",
    RUNS_DIR / "2026-01-18_to_2026-01-20__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv",
    RUNS_DIR / "2026-01-21_to_2026-01-22__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv",
)

GAP_PRIORITY = {
    "downstream_present": 3,
    "arena_present_but_underweighted": 2,
    "conversion_gap": 1,
    "arena_missing": 0,
}


def _to_bool(value: object) -> bool:
    return str(value or "").strip() == "1"


def _window_from_path(path: Path) -> str:
    marker = "__AGGREGATED_ANALYSIS_ARENA__"
    stem = path.stem
    return stem.split(marker, 1)[0] if marker in stem else stem


def _load_rows(paths: Sequence[Path]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for path in paths:
        if not path.exists():
            continue
        window = _window_from_path(path)
        for row in _read_csv(path):
            merged = dict(row)
            merged["window"] = window
            rows.append(merged)
    return rows


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
    grouped: Dict[tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("date") or ""), str(row.get("state_key") or ""))].append(row)

    out: List[Dict[str, str]] = []
    for (date, state_key), picked in sorted(grouped.items(), key=lambda item: item[0]):
        best = max(picked, key=lambda row: GAP_PRIORITY.get(str(row.get("gap_class") or ""), -1))
        outcome_span = _outcome_span([str(row.get("outcome") or "") for row in picked])
        out.append(
            {
                "date": date,
                "state_key": state_key,
                "window_count": str(len({str(row.get('window') or '') for row in picked})),
                "outcome_rows": str(len(picked)),
                "outcome_span": outcome_span,
                "state_day_gap_class": str(best.get("gap_class") or ""),
                "state_day_gap_detail": str(best.get("gap_detail") or ""),
                "arena_canonical_state_present": "1"
                if any(_to_bool(row.get("arena_canonical_any_present")) for row in picked)
                else "0",
                "arena_vtrac_state_present": "1"
                if any(_to_bool(row.get("arena_vtrac_any_present")) for row in picked)
                else "0",
                "arena_family_state_present": "1"
                if any(_to_bool(row.get("arena_family_any_present")) for row in picked)
                else "0",
                "context_reinforced_state": "1"
                if any(
                    _to_bool(row.get("winner_canonical_context_reinforced"))
                    or _to_bool(row.get("winner_vtrac_context_reinforced"))
                    or _to_bool(row.get("winner_family_context_reinforced"))
                    for row in picked
                )
                else "0",
                "profit_alert_state": "1"
                if any(
                    _to_bool(row.get("winner_canonical_profit_alert_present"))
                    or _to_bool(row.get("winner_vtrac_profit_alert_present"))
                    for row in picked
                )
                else "0",
                "due_doubles_state": "1"
                if any(
                    _to_bool(row.get("winner_canonical_due_doubles_present"))
                    or _to_bool(row.get("winner_vtrac_due_doubles_present"))
                    for row in picked
                )
                else "0",
                "blackapple_state": "1"
                if any(
                    _to_bool(row.get("winner_canonical_blackapple_present"))
                    or _to_bool(row.get("winner_vtrac_blackapple_present"))
                    for row in picked
                )
                else "0",
                "aux_badge_state": "1"
                if any(
                    _to_bool(row.get("winner_canonical_aux_badge_present"))
                    or _to_bool(row.get("winner_vtrac_aux_badge_present"))
                    for row in picked
                )
                else "0",
                "aux_overdue_state": "1"
                if any(_to_bool(row.get("winner_vtrac_aux_overdue_present")) for row in picked)
                else "0",
                "repeat_watch_state": "1"
                if any(_to_bool(row.get("winner_vtrac_repeat_watch_present")) for row in picked)
                else "0",
                "candidate_universe_literal_state": "1"
                if any(
                    _to_bool(row.get("candidate_universe_straight_present"))
                    or _to_bool(row.get("candidate_universe_box_present"))
                    for row in picked
                )
                else "0",
                "play_card_literal_state": "1"
                if any(
                    _to_bool(row.get("play_card_straight_present"))
                    or _to_bool(row.get("play_card_box_present"))
                    for row in picked
                )
                else "0",
                "downstream_literal_state": "1"
                if any(
                    _to_bool(row.get("candidate_universe_straight_present"))
                    or _to_bool(row.get("candidate_universe_box_present"))
                    or _to_bool(row.get("play_card_straight_present"))
                    or _to_bool(row.get("play_card_box_present"))
                    for row in picked
                )
                else "0",
            }
        )
    return out


def _group_counts(rows: Sequence[Dict[str, str]], *, key: str) -> List[Dict[str, str]]:
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
                "arena_canonical_state_present": _fmt_ratio(
                    sum(row["arena_canonical_state_present"] == "1" for row in picked), total
                ),
                "arena_vtrac_state_present": _fmt_ratio(
                    sum(row["arena_vtrac_state_present"] == "1" for row in picked), total
                ),
                "arena_family_state_present": _fmt_ratio(
                    sum(row["arena_family_state_present"] == "1" for row in picked), total
                ),
                "context_reinforced_state": _fmt_ratio(
                    sum(row["context_reinforced_state"] == "1" for row in picked), total
                ),
                "downstream_literal_state": _fmt_ratio(
                    sum(row["downstream_literal_state"] == "1" for row in picked), total
                ),
            }
        )
    return out


def _group_gap_class(rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("state_day_gap_class") or "")].append(row)

    out: List[Dict[str, str]] = []
    for gap_class, picked in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])):
        total = len(picked)
        out.append(
            {
                "state_day_gap_class": gap_class,
                "state_days": str(total),
                "share": _fmt_ratio(total, len(rows)),
            }
        )
    return out


def _render_md(
    *,
    raw_rows: Sequence[Dict[str, str]],
    state_day_rows: Sequence[Dict[str, str]],
    by_gap_class: Sequence[Dict[str, str]],
    by_outcome_span: Sequence[Dict[str, str]],
    out_csv: Path,
) -> str:
    lines: List[str] = [
        "# Aggregated Arena Review State-Day Scoreboard",
        "",
        "- Purpose: collapse aggregated arena review rows from `date x state x outcome` into one `date x state` performance unit while preserving row-level review as the diagnostic layer.",
        f"- summary_csv: `{out_csv}`",
        f"- outcome rows: `{len(raw_rows)}`",
        f"- state-days: `{len(state_day_rows)}`",
        "",
        "## State-Day Gap Class",
        "",
    ]
    lines.extend(_md_table(by_gap_class, ["state_day_gap_class", "state_days", "share"]))
    lines.extend(
        [
            "",
            "## By Outcome Span",
            "",
        ]
    )
    lines.extend(
        _md_table(
            by_outcome_span,
            [
                "outcome_span",
                "state_days",
                "arena_canonical_state_present",
                "arena_vtrac_state_present",
                "arena_family_state_present",
                "context_reinforced_state",
                "downstream_literal_state",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `state_day_gap_class` is the best available gap class for that date/state, using the priority: `downstream_present > arena_present_but_underweighted > conversion_gap > arena_missing`.",
            "- `context_reinforced_state` means at least one outcome row for that state-day had canonical/VTRAC/family context reinforcement.",
            "- `downstream_literal_state` means Candidate Universe or Play Card had a same-day literal closure on at least one outcome row for that state-day.",
            "- This is the performance/accounting lens; keep the original outcome-row review for diagnostics.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Summarize aggregated arena review scoreboards at the state-day level.")
    ap.add_argument("--review-csv", nargs="*", default=[str(path) for path in DEFAULT_REVIEW_CSVS])
    ap.add_argument(
        "--out-summary-csv",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-21__AGGREGATED_ARENA__REVIEW_STATE_DAY_SCOREBOARD.csv",
    )
    ap.add_argument(
        "--out-md",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-21__AGGREGATED_ARENA__REVIEW_STATE_DAY_SCOREBOARD.md",
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    raw_rows = _load_rows([Path(raw) for raw in args.review_csv])
    state_day_rows = _collapse_state_days(raw_rows)
    by_gap_class = _group_gap_class(state_day_rows)
    by_outcome_span = _group_counts(state_day_rows, key="outcome_span")

    out_csv = Path(args.out_summary_csv)
    out_md = Path(args.out_md)
    combined_rows: List[Dict[str, str]] = []
    for row in by_gap_class:
        merged = dict(row)
        merged["group"] = "gap_class"
        combined_rows.append(merged)
    for row in by_outcome_span:
        merged = dict(row)
        merged["group"] = "outcome_span"
        combined_rows.append(merged)

    _write_csv(out_csv, combined_rows)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(
        _render_md(
            raw_rows=raw_rows,
            state_day_rows=state_day_rows,
            by_gap_class=by_gap_class,
            by_outcome_span=by_outcome_span,
            out_csv=out_csv,
        ),
        encoding="utf-8",
    )
    print(f"summary_csv={out_csv}")
    print(f"report_md={out_md}")
    print(f"state_days={len(state_day_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
