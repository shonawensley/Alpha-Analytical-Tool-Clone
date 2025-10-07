#!/usr/bin/env python
"""Lightweight stress harness for the positional tracker analyzer."""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
AUX = ROOT / "scripts" / "auxiliary" / "working"

for candidate in (str(ROOT), str(SRC)):
    if candidate not in sys.path:
        sys.path.insert(0, candidate)
if str(AUX) not in sys.path:
    sys.path.append(str(AUX))

existing = os.environ.get("PYTHONPATH")
path_entries = [str(ROOT), str(SRC), str(AUX)]
if existing:
    path_entries.append(existing)
os.environ["PYTHONPATH"] = os.pathsep.join(path_entries)

from core.aux_config import POS_SHORTLIST_CONFIG, POSITIONAL_WINDOW  # noqa: E402
from modules.module_d_auxiliary_tools.refactored import positional_tool  # noqa: E402

DEFAULT_STATES = ["Delaware4"]
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "acceptance" / "positional"


def _load_draws_from_fixtures(state: str) -> dict[str, list[str]]:
    draws_by_variant: dict[str, list[str]] = {}
    for variant in ("combined", "midday", "evening"):
        path = FIXTURE_ROOT / f"{state}_{variant}.txt"
        if path.exists():
            draws_by_variant[variant] = path.read_text(encoding="utf-8").splitlines()
    return draws_by_variant


def _load_draws_from_live(state: str) -> dict[str, list[str]]:
    try:
        from modules.aux_loaders import load_state_draws  # noqa: import inside for optional dependency
    except ModuleNotFoundError:
        return {}

    draws_by_variant: dict[str, list[str]] = {}
    for variant in ("combined", "midday", "evening"):
        draws, _ = load_state_draws(state, variant=variant)
        if draws:
            draws_by_variant[variant] = list(draws)
    return draws_by_variant


def _load_draws(state: str, use_live_data: bool) -> dict[str, list[str]]:
    if use_live_data:
        live = _load_draws_from_live(state)
        if live:
            return live
        print(f"[warn] Live data unavailable for {state}, falling back to fixtures.")
    return _load_draws_from_fixtures(state)


def run_iteration(state: str, due_doubles: bool, use_live_data: bool) -> tuple[int, float]:
    draws = _load_draws(state, use_live_data)
    if not draws:
        return 0, 0.0
    started = time.perf_counter()
    report = positional_tool.analyze_state_variants(
        draws,
        window=POSITIONAL_WINDOW,
        topk=int(POS_SHORTLIST_CONFIG.get("topk_per_pos", 3)),
        due_doubles_active=due_doubles,
        shortlist_cfg=POS_SHORTLIST_CONFIG,
        vtrac_hot_indices=set(),
        vtrac_hot_families={},
    )
    duration = time.perf_counter() - started
    return len(report.candidates), duration


def main() -> None:
    parser = argparse.ArgumentParser(description="Stress the positional analyzer by running repeated iterations.")
    parser.add_argument("--state", action="append", help="State key to process (defaults to Delaware4)")
    parser.add_argument("--iterations", type=int, default=5, help="Number of iterations per state")
    parser.add_argument("--due-doubles", action="store_true", help="Force the due-doubles flag for each iteration")
    parser.add_argument("--use-live-data", action="store_true", help="Attempt to load draws via modules.aux_loaders before fixtures")
    args = parser.parse_args()

    states = args.state or DEFAULT_STATES
    print(
        f"Positional stress harness starting (states={states}, iterations={args.iterations}, live={args.use_live_data})"
    )
    for state in states:
        for iteration in range(1, args.iterations + 1):
            count, duration = run_iteration(state, args.due_doubles, args.use_live_data)
            print(f"[{state}] iteration {iteration:02d}: {count} candidates in {duration:.3f}s")
        print("---")


if __name__ == "__main__":
    main()
