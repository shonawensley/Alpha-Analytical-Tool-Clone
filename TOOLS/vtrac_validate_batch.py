#!/usr/bin/env python3
"""
Batch helper to run the V-TRAC validator across multiple states and compute quick metrics.

Example:
    python tools/vtrac_validate_batch.py --states Delaware4 Florida4

To compare an alternate analyzer bundle per state:
    python tools/vtrac_validate_batch.py \
        --analysis-json-b-pattern "data/outputs/analysis/vtrac_legacy/{state}.json" \
        --label-b legacy
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

DEFAULT_WINNERS_ROOT = Path("data/outputs/analysis/winners")
VALIDATION_OUTPUT_ROOT = Path("data/outputs/analysis/vtrac_validation")


def _discover_states(root: Path) -> list[str]:
    if not root.exists():
        return []
    return sorted({p.name for p in root.iterdir() if p.is_dir()})


def _precision_at_k(candidates: Sequence[str], hits: set[str], k: int) -> tuple[float, list[str], list[str]]:
    top = [c for c in candidates[:k] if isinstance(c, str)]
    if not top:
        return 0.0, [], []
    matches = [c for c in top if c in hits]
    precision = len(matches) / len(top)
    return precision, matches, top


def _run_validator(
    state: str,
    winners_root: Path | None,
    analysis_pattern: str | None,
    analysis_b_pattern: str | None,
    label_b: str,
) -> Path:
    cmd: list[str] = [
        "python",
        "tools/vtrac_validate.py",
        "--state",
        state,
    ]
    if winners_root:
        winners_dir = winners_root / state
        cmd.extend(["--winners-dir", str(winners_dir)])
    if analysis_pattern:
        analysis_json = Path(analysis_pattern.format(state=state))
        if analysis_json.exists():
            cmd.extend(["--analysis-json", str(analysis_json)])
        else:
            raise FileNotFoundError(f"Primary analyzer JSON not found for {state}: {analysis_json}")
    if analysis_b_pattern:
        analysis_json_b = Path(analysis_b_pattern.format(state=state))
        if analysis_json_b.exists():
            cmd.extend(["--analysis-json-b", str(analysis_json_b), "--label-b", label_b])
        else:
            raise FileNotFoundError(f"Alternate analyzer JSON not found for {state}: {analysis_json_b}")
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return VALIDATION_OUTPUT_ROOT / state / "validation_report.json"


def _summarise_report(report_path: Path, labels: Iterable[str], k: int) -> dict:
    data = json.loads(report_path.read_text(encoding="utf-8"))
    html_hits = {
        pattern for pattern, count in (data.get("straight_occurrences") or {}).items() if count
    }
    global_top = data.get("analyzer_global_top_straights") or {}

    precision = {}
    for label in labels:
        candidates = global_top.get(label, [])
        precision[label] = _precision_at_k(candidates, html_hits, k)

    combined = data.get("sections", {}).get("Combined", {})
    winners_signatures = set(combined.get("signals", {}).get("top_vtrac_box_signatures", []))
    analyzer_signatures = {}
    for label in labels:
        sigs = combined.get("analyzer_signatures", {}).get(label, [])
        analyzer_signatures[label] = set(sigs)

    return {
        "precision": precision,
        "html_hits": html_hits,
        "combined_signatures": winners_signatures,
        "analyzer_signatures": analyzer_signatures,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch V-TRAC validator helper")
    parser.add_argument("--states", nargs="*", help="States to validate (defaults to all under winners root)")
    parser.add_argument("--winners-root", type=Path, default=DEFAULT_WINNERS_ROOT, help="Root directory for winners HTML")
    parser.add_argument("--analysis-json-pattern", help="Pattern for analyzer JSON (use {state} placeholder)")
    parser.add_argument("--analysis-json-b-pattern", help="Pattern for alternate analyzer JSON (use {state} placeholder)")
    parser.add_argument("--label-b", default="comparison", help="Label to assign to alternate analyzer JSON (default: comparison)")
    parser.add_argument("--precision-k", type=int, default=5, help="Compute precision@k (default: 5)")
    args = parser.parse_args()

    states = args.states or _discover_states(args.winners_root)
    if not states:
        raise SystemExit("No states found to validate.")

    # Track labels present for precision reporting
    labels = ["primary"]
    if args.analysis_json_b_pattern:
        labels.append(args.label_b)

    print(f"# V-TRAC Validator Batch (precision@{args.precision_k})")
    header = ["State", "HTML Straights>0", "P@K(primary)"]
    if args.analysis_json_b_pattern:
        header.append(f"P@K({args.label_b})")
    print(" | ".join(header))
    print("-" * 80)

    for state in states:
        try:
            report_path = _run_validator(
                state=state,
                winners_root=args.winners_root,
                analysis_pattern=args.analysis_json_pattern,
                analysis_b_pattern=args.analysis_json_b_pattern,
                label_b=args.label_b,
            )
        except FileNotFoundError as exc:
            print(f"{state} | ERROR: {exc}")
            continue

        summary = _summarise_report(report_path, labels, args.precision_k)
        html_hits = summary["html_hits"]
        row = [state, str(len(html_hits))]

        for label in labels:
            precision, matches, top = summary["precision"][label]
            if not top:
                row.append("n/a")
            else:
                pct = f"{precision*100:.1f}%"
                detail = f"{pct} ({len(matches)}/{len(top)})"
                row.append(detail)

        print(" | ".join(row))


if __name__ == "__main__":
    main()
