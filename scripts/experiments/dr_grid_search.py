#!/usr/bin/env python3
"""
Small helper to sweep Digit-Reduction scoring weights.

Creates temporary config variants, runs digit_reduction_validate.py for each,
and prints the best-performing combination based on mean Hit@3 + 0.5*MRR.
"""

from __future__ import annotations

import argparse
import itertools
import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import yaml

GRID_OPTIONS: Dict[str, List[float]] = {
    "scoring_v2.weights.extended_cluster_bonus": [0.15, 0.25, 0.35],
    "scoring_v2.guards.min_drop_run_len": [4, 5, 6],
}


def apply_override(cfg: Dict[str, any], dotted_key: str, value: float) -> None:
    parts = dotted_key.split(".")
    target = cfg
    for part in parts[:-1]:
        target = target.setdefault(part, {})
    target[parts[-1]] = value


def main() -> None:
    parser = argparse.ArgumentParser(description="Digit-Reduction scoring grid search.")
    parser.add_argument("stamp", help="Base stamp (e.g., 20250617)")
    parser.add_argument("winners_csv", help="Path to winners CSV")
    parser.add_argument("--analysis-root", default="data/outputs/analysis/digit_reduction")
    parser.add_argument("--config", default="alpha_analytical/digit_reduction/analyzer_v2/config.yml")
    args = parser.parse_args()

    base_cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    report_root = Path("reports/DR") / args.stamp
    report_root.mkdir(parents=True, exist_ok=True)
    cfg_dir = report_root / "grid_configs"
    cfg_dir.mkdir(exist_ok=True)

    keys = list(GRID_OPTIONS.keys())
    combos = list(itertools.product(*[GRID_OPTIONS[k] for k in keys]))
    results: List[Tuple[float, Dict[str, float], Path]] = []

    for idx, values in enumerate(combos, 1):
        cfg = deepcopy(base_cfg)
        overrides = {}
        for key, value in zip(keys, values):
            apply_override(cfg, key, value)
            overrides[key] = value
        # keep lockscore guard aligned with scoring guard
        try:
            min_drop = cfg["scoring_v2"]["guards"].get("min_drop_run_len", 5)
            cfg.setdefault("lockscore", {}).setdefault("guards", {})["min_drop_run_len"] = min_drop
        except Exception:
            pass
        cfg_path = cfg_dir / f"override_{idx:02d}.yml"
        cfg_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")
        stamp_variant = f"{args.stamp}_S{idx:02d}"
        cmd = [
            "python3",
            "scripts/experiments/digit_reduction_validate.py",
            stamp_variant,
            args.winners_csv,
            "--analysis-root",
            args.analysis_root,
            "--config",
            str(cfg_path),
        ]
        subprocess.run(cmd, check=True)
        metrics_path = Path("reports/DR") / stamp_variant / "digit_reduction_metrics.csv"
        df = pd.read_csv(metrics_path)
        score = (df["hit_at_3"].mean() if not df.empty else 0.0) + 0.5 * (df["mrr"].mean() if not df.empty else 0.0)
        results.append((score, overrides, metrics_path))
        print(json.dumps({"combo": overrides, "score": score, "stamp": stamp_variant}, indent=2))

    if results:
        best = max(results, key=lambda item: item[0])
        print("Best combo:", json.dumps(best[1], indent=2))
        print("Metrics:", best[2])


if __name__ == "__main__":
    main()
