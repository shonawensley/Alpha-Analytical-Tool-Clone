#!/usr/bin/env python
"""CLI helper to validate Aux double and pair stats against raw draw CSVs."""
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

from core.aux_config import PAIRS_WINDOW
from alpha_analytical.control_center.aux_validation import (
    collect_variant_stats,
    collect_pair_stats_for_state,
    multi_variant_alerts,
    pair_multi_variant_alerts,
)


VARIANTS: List[str] = ["combined", "midday", "evening"]


def _print_variant_double_stats(state: str, *, base: Path | None, max_n: int, limit: int) -> None:
    stats = collect_variant_stats(state, base=base, max_n=max_n)
    for variant in VARIANTS:
        variant_stats = stats.get(variant)
        header = f"[{state}] {variant.title()} top doubles"
        if not variant_stats:
            print(f"{header}: no data")
            continue
        top = sorted(variant_stats.items(), key=lambda kv: kv[1]["draws_since"], reverse=True)[:limit]
        print(f"{header} (draws since >= thresholds):")
        for combo, payload in top:
            print(f"  {combo}: {payload['draws_since']} ({payload['severity']})")
        print()


def _print_variant_pair_stats(
    state: str,
    *,
    base: Path | None,
    max_n: int,
    limit: int,
    window: int | None,
) -> None:
    effective_window = window if window is not None else PAIRS_WINDOW
    stats_by_variant = collect_pair_stats_for_state(
        state,
        base=base,
        max_n=max_n,
        window=effective_window,
    )
    for variant in VARIANTS:
        payload = stats_by_variant.get(variant)
        header = f"[{state}] {variant.title()} pairs"
        if not payload:
            print(f"{header}: no data")
            continue
        repeating = sorted(payload["repeating"].items(), key=lambda kv: kv[1], reverse=True)[:limit]
        non_repeating = sorted(payload["non_repeating"].items(), key=lambda kv: kv[1], reverse=True)[:limit]
        print(f"{header} — repeating (top {limit}):")
        for pair, overdue in repeating:
            severity = payload["status"].get(pair, "")
            sev_suffix = f" {severity}" if severity else ""
            print(f"  {pair}: {overdue}{sev_suffix}")
        print(f"{header} — non-repeating (top {limit}):")
        for pair, overdue in non_repeating:
            severity = payload["status"].get(pair, "")
            sev_suffix = f" {severity}" if severity else ""
            print(f"  {pair}: {overdue}{sev_suffix}")
        print()


def run(
    states: List[str],
    *,
    base: Path | None,
    max_n: int,
    limit: int,
    show_doubles: bool,
    show_pairs: bool,
    pairs_window: int | None,
) -> None:
    effective_window = pairs_window if pairs_window is not None else PAIRS_WINDOW
    for state in states:
        if show_doubles:
            _print_variant_double_stats(state, base=base, max_n=max_n, limit=limit)
            alerts = multi_variant_alerts(state, base=base, max_n=max_n)
            if alerts:
                print(f"[{state}] double combos flagged in multiple variants:")
                for combo, by_variant in alerts.items():
                    parts = [
                        f"{variant}:{payload['draws_since']}({payload['severity']})"
                        for variant, payload in sorted(by_variant.items())
                    ]
                    print(f"  {combo} -> {'; '.join(parts)}")
            else:
                print(f"[{state}] no double combos flagged in more than one variant.")
            print("-" * 60)

        if show_pairs:
            _print_variant_pair_stats(
                state,
                base=base,
                max_n=max_n,
                limit=limit,
                window=effective_window,
            )
            pair_alerts = pair_multi_variant_alerts(
                state,
                base=base,
                max_n=max_n,
                window=effective_window,
            )
            if pair_alerts:
                print(f"[{state}] pairs flagged in multiple variants:")
                for pair, by_variant in pair_alerts.items():
                    parts = [
                        f"{variant}:{payload['draws_since']}({payload['severity']})"
                        for variant, payload in sorted(by_variant.items())
                    ]
                    print(f"  {pair} -> {'; '.join(parts)}")
            else:
                print(f"[{state}] no pairs flagged in more than one variant.")
            print("=" * 60)



def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Aux double/pair metrics against draws CSVs.",
    )
    parser.add_argument("states", nargs="+", help="State labels, e.g., Connecticut4 NewYork4")
    parser.add_argument("--draws-root", type=Path, default=None, help="Optional alternate draws directory")
    parser.add_argument("--max-n", type=int, default=1000, help="Maximum draws to inspect (default 1000)")
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="How many top items to display per variant (default 10)",
    )
    parser.add_argument(
        "--no-doubles",
        action="store_true",
        help="Suppress double validation output",
    )
    parser.add_argument(
        "--no-pairs",
        action="store_true",
        help="Suppress pair validation output",
    )
    parser.add_argument(
        "--pairs-window",
        type=int,
        default=None,
        help="Override the pair analysis window (default: project PAIRS_WINDOW)",
    )
    args = parser.parse_args()

    run(
        args.states,
        base=args.draws_root,
        max_n=args.max_n,
        limit=args.limit,
        show_doubles=not args.no_doubles,
        show_pairs=not args.no_pairs,
        pairs_window=args.pairs_window,
    )


if __name__ == "__main__":
    main()
