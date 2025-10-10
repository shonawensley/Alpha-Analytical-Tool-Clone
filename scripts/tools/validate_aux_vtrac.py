
#!/usr/bin/env python
"""CLI helper to validate Aux V-TRAC overlays, heatboard stats, and sums analytics."""
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
    sums_stats_by_variant,
    vtrac_heatboard_by_variant,
    vtrac_overlay_by_variant,
)

VARIANTS: List[str] = ["combined", "midday", "evening"]


def _render_overlay(state: str, overlay_by_variant: dict[str, dict[int, int]], limit: int) -> None:
    for variant in VARIANTS:
        overlay = overlay_by_variant.get(variant)
        if not overlay:
            print(f"[{state}] {variant.title()} V-TRAC overlay: no data")
            continue
        top = sorted(overlay.items(), key=lambda item: item[1], reverse=True)[:limit]
        formatted = ", ".join(f"{idx}:{gap}" for idx, gap in top)
        print(f"[{state}] {variant.title()} V-TRAC overlay top {limit}: {formatted}")
    print("-" * 60)


def _render_heatboard(state: str, heatboard_by_variant: dict[str, dict[int, dict]], limit: int) -> None:
    for variant in VARIANTS:
        payload = heatboard_by_variant.get(variant)
        if not payload:
            print(f"[{state}] {variant.title()} heatboard: no data")
            continue
        top = sorted(payload.items(), key=lambda item: item[1]["ds"], reverse=True)[:limit]
        lines = []
        for idx, stats in top:
            ds = stats.get("ds")
            freq_short = stats.get("freq_short")
            freq_long = stats.get("freq_long")
            lines.append(f"{idx}:ds={ds} fs={freq_short} fl={freq_long}")
        print(f"[{state}] {variant.title()} heatboard top {limit}: {', '.join(lines)}")
    print("=" * 60)


def _render_sums(state: str, sums_by_variant: dict[str, dict]) -> None:
    for variant in VARIANTS:
        payload = sums_by_variant.get(variant)
        if not payload:
            print(f"[{state}] {variant.title()} sums: no data")
            continue
        window = payload.get("window", 0)
        by_sum = payload.get("by_sum", {})
        top = sorted(by_sum.items(), key=lambda item: item[1]["draws_since"], reverse=True)[:5]
        lines = []
        for label, stats in top:
            ds = stats.get("draws_since")
            flags = stats.get("flags", {})
            active = [name for name, flag in flags.items() if flag]
            lines.append(f"S{label}:ds={ds} flags={'+'.join(active) if active else '-'}")
        print(f"[{state}] {variant.title()} sums (window={window}): {', '.join(lines)}")
    print("~" * 60)


def run(
    states: List[str],
    *,
    draws_root: Path | None,
    max_n: int,
    window: int,
    overlay_limit: int,
) -> None:
    for state in states:
        overlay = vtrac_overlay_by_variant(state, base=draws_root, max_n=max_n)
        _render_overlay(state, overlay, overlay_limit)
        heatboard = vtrac_heatboard_by_variant(state, base=draws_root, max_n=max_n, window=window)
        _render_heatboard(state, heatboard, overlay_limit)
        sums_data = sums_stats_by_variant(state, base=draws_root, max_n=max_n, window=window)
        _render_sums(state, sums_data)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Aux V-TRAC overlays/heatboard and sums analytics against draw CSVs.",
    )
    parser.add_argument("states", nargs="+", help="State labels, e.g., Connecticut4 NewYork4")
    parser.add_argument("--draws-root", type=Path, default=None, help="Optional alternate draws directory")
    parser.add_argument("--max-n", type=int, default=1000, help="Maximum draws to inspect (default 1000)")
    parser.add_argument(
        "--window",
        type=int,
        default=150,
        help="Window for sums / heatboard calculations (default 150)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="How many rows to display for overlay / heatboard summaries (default 10)",
    )
    args = parser.parse_args()

    run(
        args.states,
        draws_root=args.draws_root,
        max_n=args.max_n,
        window=args.window,
        overlay_limit=args.limit,
    )


if __name__ == "__main__":
    main()
