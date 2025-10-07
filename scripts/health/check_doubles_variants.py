#!/usr/bin/env python
"""Quick health helper to audit doubles-family badges across variants."""

from __future__ import annotations

import argparse
import collections
import sys
from pathlib import Path
from typing import Dict, Iterable, List
from importlib.util import module_from_spec, spec_from_file_location

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

for candidate in (PROJECT_ROOT, SRC_DIR):
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)

from core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
from core.vtrac_family_ranker import rank_double_families


def _import_project_module(module_name: str, relative: str):
    target = PROJECT_ROOT / relative
    spec = spec_from_file_location(module_name, target)
    if not spec or not spec.loader:
        raise ImportError("Unable to load " + relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


_aux_loaders = _import_project_module("project_aux_loaders", "modules/aux_loaders.py")
load_state_draws = _aux_loaders.load_state_draws

VARIANTS = ("combined", "midday", "evening")
DRAWS_ROOT = PROJECT_ROOT / "data" / "cleaned" / "draws"


def _discover_states() -> List[str]:
    if not DRAWS_ROOT.exists():
        return []
    states: set[str] = set()
    for path in DRAWS_ROOT.glob("*_draws.csv"):
        stem = path.stem
        if stem.endswith("_Midday") or stem.endswith("_Evening"):
            continue
        states.add(stem[:-6] if stem.endswith("_draws") else stem)
    return sorted(states)


def _variant_tokens(rankings: List[dict]) -> Dict[str, List[str]]:
    grouped: Dict[str, List[str]] = {}
    for entry in rankings:
        label = entry.get("label") or "?"
        tokens: List[str] = []
        for member in entry.get("members", []):
            severity = member.get("severity")
            variant = member.get("variant", "")
            canonical = member.get("canonical") or member.get("combo")
            if severity not in ("R", "B") or not canonical or not variant:
                continue
            badge = variant[0].upper()
            token = f"{severity}{canonical}{badge}"
            tokens.append(token)
        if tokens:
            grouped[label] = tokens
    return grouped


def audit_state(state: str) -> dict:
    variant_draws: Dict[str, List[str]] = {}
    missing: List[str] = []
    unseen_flags: List[str] = []
    counts = collections.Counter()

    for variant in VARIANTS:
        draws, _ = load_state_draws(
            state,
            variant=variant,
            max_n=1000,
        )
        if not draws:
            missing.append(variant)
        variant_draws[variant] = draws

    rankings = rank_double_families(
        variant_draws,
        red_threshold=COMBO_DOUBLE_VERY_LATE,
        blue_threshold=COMBO_DOUBLE_LATE,
        limit=5,
    )

    tokens = _variant_tokens(rankings)
    for entry in rankings:
        for member in entry.get("members", []):
            if member.get("severity") in ("R", "B"):
                badge = member.get("variant", "?")
                counts[f"{member['severity']}_{badge}"] += 1
                if member.get("unseen"):
                    canon = member.get("canonical") or member.get("combo") or "?"
                    unseen_flags.append(f"{canon}:{badge}")

    merged_tokens = [token for token_list in tokens.values() for token in token_list if token.endswith("CEM")]

    return {
        "state": state,
        "missing_variants": missing,
        "tokens": tokens,
        "counts": counts,
        "unseen_badges": unseen_flags,
        "merged_tokens": merged_tokens,
    }


def render_report(results: Iterable[dict]) -> None:
    for item in results:
        state = item["state"]
        print(f"State: {state}")
        if item["missing_variants"]:
            print(f"  Missing variants: {', '.join(item['missing_variants'])}")
        for label, tokens in item["tokens"].items():
            print(f"  {label}: {' '.join(tokens)}")
        if item["unseen_badges"]:
            print(f"  Warning: unseen combos flagged as overdue -> {', '.join(item['unseen_badges'])}")
        if item["merged_tokens"]:
            print(f"  Warning: merged tokens detected -> {', '.join(item['merged_tokens'])}")
        counts = item["counts"]
        if counts:
            summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
            print(f"  Totals: {summary}")
        print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit doubles-family badge rendering across variants")
    parser.add_argument("--state", action="append", help="Specific state label(s) to audit")
    args = parser.parse_args(argv)

    states = args.state or _discover_states()
    if not states:
        print("No states discovered under data/cleaned/draws", file=sys.stderr)
        return 1

    results = [audit_state(state) for state in states]
    render_report(results)
    issues = [item for item in results if item["missing_variants"] or item["merged_tokens"]]
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())


