"""
Lightweight harness for Digit Reduction Analyzer V2.

Usage:
    python3 scripts/checks/dr_analyzer_v2_harness.py \
        --state Connecticut4 \
        --training-json archive/fresh_run_20250930_013906/outputs_analysis/digit_reduction/Connecticut4/training/Connecticut4_digit_reduction_logs.json

If --training-json is omitted, the harness uses pipeline.load_training_json
which expects the latest reducer artifact under data/outputs/analysis.
"""

from __future__ import annotations

import argparse
import statistics
from pathlib import Path
from typing import Dict, Iterable
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alpha_analytical.digit_reduction.analyzer_v2.features import build_features
from alpha_analytical.digit_reduction.analyzer_v2.io import load_training_json
from alpha_analytical.digit_reduction.analyzer_v2.pipeline import (
    _aggregate_metrics,
    _load_config,
)
from alpha_analytical.digit_reduction.analyzer_v2.score import score_row


def _summary(feature_rows: Iterable[Dict[str, float]]) -> Dict[str, float]:
    rows = list(feature_rows)
    if not rows:
        return {}
    scores = [row["score"] for row in rows]
    density = [row["box_family_density"] for row in rows]
    dup_bonus = [row["dup_bonus"] for row in rows]
    return {
        "rows": len(rows),
        "score_min": min(scores),
        "score_max": max(scores),
        "score_mean": statistics.fmean(scores),
        "density_mean": statistics.fmean(density),
        "dup_bonus_max": max(dup_bonus),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Digit Reduction Analyzer V2 harness")
    parser.add_argument("--state", required=True, help="State key, e.g. Connecticut4")
    parser.add_argument(
        "--training-json",
        type=Path,
        help="Optional explicit path to digit_reduction_log.json",
    )
    args = parser.parse_args()

    state = args.state
    cfg = _load_config()

    if args.training_json:
        data = args.training_json.read_text(encoding="utf-8")
        import json
        payload = json.loads(data)
        items = []
        from alpha_analytical.digit_reduction.analyzer_v2.types import Item, Step, Key

        for entry in payload.get("items", []):
            key = Key(
                state=entry["state"],
                area=entry["area"],
                section=entry["section"],
                set=entry["set"],
                draw=entry["draw"],
                col=int(entry.get("col", 0)),
                method=entry["method"],
                mode=entry["mode"],
            )
            steps = [Step(**step) for step in entry.get("steps", [])]
            items.append(
                Item(
                    key=key,
                    grid_position=entry.get("grid_position", {}),
                    sequence_meta=entry.get("sequence_meta", {}),
                    steps=steps,
                    final=entry.get("final", {}),
                )
            )
    else:
        items, _ = load_training_json(state)

    features = build_features(items, cfg)
    _aggregate_metrics(features, cfg)

    rows = []
    for entry in features:
        score_payload = score_row(entry.row, cfg)
        row = dict(entry.row)
        row.update(score_payload)
        rows.append(row)

    summary = _summary(rows)

    print(f"[Analyzer V2 harness] state={state}")
    for key, value in summary.items():
        print(f"  {key}: {value}")

    interesting = [
        row
        for row in rows
        if row.get("score", 0.0) >= cfg["gates"]["early_lock"] or row.get("lock_decision") == "lock"
    ]
    if not interesting:
        print("  No locked candidates in this sample.")
    else:
        print("  Locked candidates:")
        for row in interesting[:5]:
            print(
                f"    {row['section']} {row['set']} col={row['col']} method={row['method']} "
                f"pattern={row.get('pattern','')} score={row['score']:.3f} "
                f"density={row['box_family_density']:.2f} dup_bonus={row['dup_bonus']}"
            )


if __name__ == "__main__":
    main()
