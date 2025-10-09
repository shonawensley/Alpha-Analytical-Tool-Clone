#!/usr/bin/env python
"""CLI helper to validate Aux double stats against raw draw CSVs."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / 'src'
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from alpha_analytical.control_center.aux_validation import (
    collect_variant_stats,
    multi_variant_alerts,
)


def _print_variant_stats(state: str, variants: List[str], base: Path | None = None, max_n: int = 1000) -> None:
    stats = collect_variant_stats(state, base=base, max_n=max_n)
    for variant in variants:
        variant_stats = stats.get(variant)
        if not variant_stats:
            print(f"[{state}] {variant.title()}: no data")
            continue
        top = sorted(variant_stats.items(), key=lambda kv: kv[1]["draws_since"], reverse=True)[:10]
        print(f"[{state}] {variant.title()} top doubles (draws since >= thresholds):")
        for combo, payload in top:
            print(f"  {combo}: {payload['draws_since']} ({payload['severity']})")
        print()


def run(states: List[str], base: Path | None = None, max_n: int = 1000) -> None:
    variants = ["combined", "midday", "evening"]
    for state in states:
        _print_variant_stats(state, variants, base=base, max_n=max_n)
        alerts = multi_variant_alerts(state, base=base, max_n=max_n)
        if alerts:
            print(f"[{state}] combos flagged in multiple variants:")
            for combo, by_variant in alerts.items():
                parts = [f"{variant}:{payload['draws_since']}" for variant, payload in sorted(by_variant.items())]
                print(f"  {combo} -> {'; '.join(parts)}")
        else:
            print(f"[{state}] no combos flagged in more than one variant.")
        print("-" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Aux double metrics against draws CSVs.")
    parser.add_argument("states", nargs="+", help="State labels, e.g., Connecticut4 NewYork4")
    parser.add_argument("--draws-root", type=Path, default=None, help="Optional alternate draws directory")
    parser.add_argument("--max-n", type=int, default=1000, help="Maximum draws to inspect (default 1000)")
    args = parser.parse_args()
    run(args.states, base=args.draws_root, max_n=args.max_n)


if __name__ == "__main__":
    main()

