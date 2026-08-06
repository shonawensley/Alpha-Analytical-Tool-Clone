#!/usr/bin/env python3
"""Create BOXED12 and STRAIGHT12 from merit-qualified VTRAC clusters."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.compact_candidate_slates import read_json  # noqa: E402
from scripts.tools.merit_allocated_vtrac_cluster_slates import (  # noqa: E402
    build_merit_allocated_slate,
    default_merit_output_path,
    discover_merit_inputs,
    write_merit_slate_files,
)


def _resolve_path(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def _optional_override(value: str, discovered: Optional[Path]) -> Optional[Path]:
    return _resolve_path(value) if value else discovered


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Create a winner-blind multi-cluster VTRAC shadow artifact with "
            "separate BOXED12 and STRAIGHT12 surfaces."
        )
    )
    parser.add_argument("--candidate-universe", required=True)
    parser.add_argument("--tables-json", default="")
    parser.add_argument("--aggregated-arena", default="")
    parser.add_argument("--translation-sandbox", default="")
    parser.add_argument("--aux-summary", default="")
    parser.add_argument("--output", default="")
    parser.add_argument(
        "--target-period",
        choices=("Day", "Midday", "Evening", "Combined"),
        default="Day",
    )
    parser.add_argument(
        "--run-mode",
        choices=("shadow", "development_replay"),
        default="shadow",
    )
    parser.add_argument("--freeze-receipt", default="")
    parser.add_argument("--maximum-clusters", type=int, choices=(1, 2, 3, 4), default=4)
    parser.add_argument("--width-cap", type=int, choices=range(1, 13), default=12)
    args = parser.parse_args(argv)

    candidate_path = _resolve_path(args.candidate_universe)
    if not candidate_path.exists():
        raise SystemExit(f"Missing Candidate Universe: {candidate_path}")

    discovered_tables, discovered_arena, discovered_sandbox, discovered_aux = (
        discover_merit_inputs(candidate_path)
    )
    tables_path = _optional_override(args.tables_json, discovered_tables)
    arena_path = _optional_override(args.aggregated_arena, discovered_arena)
    sandbox_path = _optional_override(args.translation_sandbox, discovered_sandbox)
    aux_path = _optional_override(args.aux_summary, discovered_aux)

    if tables_path is None or not tables_path.exists():
        raise SystemExit(
            "Missing predictive pattern tables. Supply --tables-json explicitly."
        )
    for label, path in (
        ("Aggregated Arena", arena_path),
        ("Translation Sandbox", sandbox_path),
        ("Aux summary", aux_path),
    ):
        if path is not None and not path.exists():
            raise SystemExit(f"Missing {label}: {path}")

    candidate_payload = read_json(candidate_path)
    tables_payload = read_json(tables_path)
    arena_payload = read_json(arena_path) if arena_path is not None else None
    sandbox_payload = read_json(sandbox_path) if sandbox_path is not None else None
    aux_payload = read_json(aux_path) if aux_path is not None else None
    try:
        payload = build_merit_allocated_slate(
            pattern_tables=tables_payload,
            candidate_universe=candidate_payload,
            aggregated_arena=arena_payload,
            translation_sandbox=sandbox_payload,
            aux_summary=aux_payload,
            tables_path=tables_path,
            candidate_path=candidate_path,
            arena_path=arena_path,
            sandbox_path=sandbox_path,
            aux_path=aux_path,
            repo_root=REPO_ROOT,
            target_period=args.target_period,
            run_mode=args.run_mode,
            freeze_receipt=args.freeze_receipt,
            maximum_clusters=args.maximum_clusters,
            width_cap=args.width_cap,
        )
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc

    output_path = (
        _resolve_path(args.output)
        if args.output
        else default_merit_output_path(candidate_path)
    )
    if output_path.suffix.lower() != ".json":
        raise SystemExit("error: --output must end in .json")
    json_path, markdown_path = write_merit_slate_files(output_path, payload)
    boxed = payload["surfaces"]["BOXED12"]
    straight = payload["surfaces"]["STRAIGHT12"]
    selected = payload["pattern_scan_receipt"]["selected_vtrac_indices"]
    print(f"[ok] merit slate JSON -> {json_path}")
    print(f"[ok] merit slate Markdown -> {markdown_path}")
    print(
        "[info] "
        f"clusters={','.join(str(value) for value in selected) or '-'} "
        f"BOXED12={boxed['candidate_count']} "
        f"STRAIGHT12={straight['candidate_count']} "
        f"timing={payload['evidence_safety']['timing_status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
