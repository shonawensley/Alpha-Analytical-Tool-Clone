
#!/usr/bin/env python
"""CLI helper to validate Aux repeat-watch and positional hard-due metrics."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from alpha_analytical.control_center.aux_validation import (
    positional_hard_due_by_variant,
    positional_shortlist_report,
    repeat_summary_by_variant,
)

VARIANTS: List[str] = ["combined", "midday", "evening"]


def _render_repeat_summary(state: str, summary: dict[str, dict[str, int | None]]) -> None:
    for variant in VARIANTS:
        payload = summary.get(variant)
        if not payload:
            print(f"[{state}] {variant.title()} repeat-watch: no data")
            continue
        current = payload.get("current_index")
        streak = payload.get("current_streak")
        last_gap = payload.get("last_repeat_gap")
        last_idx = payload.get("last_repeat_index")
        max_streak = payload.get("max_streak")
        print(
            f"[{state}] {variant.title()} repeat-watch: current={current}"
            f" streak={streak} max={max_streak} last_repeat_gap={last_gap}"
            f" last_index={last_idx}"
        )
    print("-" * 60)


def _render_positional(state: str, flagged: dict[str, list[dict[str, int]]]) -> None:
    for variant in VARIANTS:
        entries = flagged.get(variant)
        if not entries:
            print(f"[{state}] {variant.title()} positional hard-due: none")
            continue
        parts = [
            f"P{entry['position'] + 1}:{entry['digit']} ({entry['draws_since']})"
            for entry in entries
        ]
        print(f"[{state}] {variant.title()} positional hard-due -> {', '.join(parts)}")
    print("=" * 60)


def _render_shortlist(state: str, report: dict[str, object], limit: int) -> None:
    if not report:
        print(f"[{state}] positional shortlist: unavailable")
        return
    candidates = report.get("candidates", [])[:limit]
    if candidates:
        print(f"[{state}] positional shortlist top {limit}:")
        for entry in candidates:
            tags = entry.get("tags", [])
            tag_display = ",".join(tags[:3]) if tags else "-"
            print(f"  {entry.get('combo')}: score={entry.get('score'):.2f} tags={tag_display}")
    else:
        print(f"[{state}] positional shortlist: no candidates")
    consensus = report.get("consensus_notes", []) or []
    if consensus:
        print(f"[{state}] consensus notes:")
        for note in consensus:
            print(f"  - {note}")
    double_notes = report.get("double_pressure_notes", []) or []
    if double_notes:
        print(f"[{state}] double-pressure notes:")
        for note in double_notes:
            print(f"  - {note}")
    print("^" * 60)


def run(
    states: List[str],
    *,
    draws_root: Path | None,
    max_n: int,
    window: int,
    skip_repeat: bool,
    skip_positional: bool,
    skip_shortlist: bool,
    shortlist_limit: int,
) -> None:
    for state in states:
        if not skip_repeat:
            summary = repeat_summary_by_variant(state, base=draws_root, max_n=max_n)
            _render_repeat_summary(state, summary)
        if not skip_positional:
            flagged = positional_hard_due_by_variant(
                state,
                base=draws_root,
                max_n=max_n,
                window=window,
            )
            _render_positional(state, flagged)
        if not skip_shortlist:
            shortlist = positional_shortlist_report(
                state,
                base=draws_root,
                max_n=max_n,
                window=window,
            )
            _render_shortlist(state, shortlist, shortlist_limit)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Aux repeat-watch and positional hard-due metrics against draw CSVs.",
    )
    parser.add_argument("states", nargs="+", help="State labels, e.g., Connecticut4 NewYork4")
    parser.add_argument("--draws-root", type=Path, default=None, help="Optional alternate draws directory")
    parser.add_argument("--max-n", type=int, default=1000, help="Maximum draws to inspect (default 1000)")
    parser.add_argument(
        "--window",
        type=int,
        default=150,
        help="Positional analysis window (default 150)",
    )
    parser.add_argument(
        "--no-repeat",
        action="store_true",
        help="Suppress repeat-watch output",
    )
    parser.add_argument(
        "--no-positional",
        action="store_true",
        help="Suppress positional hard-due output",
    )
    parser.add_argument(
        "--no-shortlist",
        action="store_true",
        help="Suppress positional shortlist output",
    )
    parser.add_argument(
        "--shortlist-limit",
        type=int,
        default=5,
        help="How many shortlist candidates to display (default 5)",
    )
    args = parser.parse_args()

    run(
        args.states,
        draws_root=args.draws_root,
        max_n=args.max_n,
        window=args.window,
        skip_repeat=args.no_repeat,
        skip_positional=args.no_positional,
        skip_shortlist=args.no_shortlist,
        shortlist_limit=args.shortlist_limit,
    )


if __name__ == "__main__":
    main()
