#!/usr/bin/env python3
"""Create the direct-evidence Structural Convergence Anchor Slate."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.compact_candidate_slates import (  # noqa: E402
    build_anchor_slate,
    default_anchor_output_path,
    discover_related_artifacts,
    read_json,
    write_slate_files,
)


def _resolve_path(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Create a winner-free experimental slate of directly supported boxed "
            "canonicals from Candidate Universe, Aggregated Arena, and Translation Sandbox."
        )
    )
    parser.add_argument("--candidate-universe", required=True)
    parser.add_argument("--aggregated-arena", default="")
    parser.add_argument("--translation-sandbox", default="")
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
    parser.add_argument(
        "--freeze-receipt",
        default="",
        help="Optional external frozen-receipt identifier. Absence is reported, not inferred.",
    )
    args = parser.parse_args(argv)

    candidate_path = _resolve_path(args.candidate_universe)
    if not candidate_path.exists():
        raise SystemExit(f"Missing Candidate Universe: {candidate_path}")

    discovered_arena, discovered_sandbox = discover_related_artifacts(candidate_path)
    arena_path = _resolve_path(args.aggregated_arena) if args.aggregated_arena else discovered_arena
    sandbox_path = (
        _resolve_path(args.translation_sandbox)
        if args.translation_sandbox
        else discovered_sandbox
    )
    if arena_path is not None and not arena_path.exists():
        raise SystemExit(f"Missing Aggregated Arena: {arena_path}")
    if sandbox_path is not None and not sandbox_path.exists():
        raise SystemExit(f"Missing Translation Sandbox: {sandbox_path}")

    candidate_payload = read_json(candidate_path)
    arena_payload = read_json(arena_path) if arena_path is not None else None
    sandbox_payload = read_json(sandbox_path) if sandbox_path is not None else None

    try:
        payload = build_anchor_slate(
            candidate_universe=candidate_payload,
            aggregated_arena=arena_payload,
            translation_sandbox=sandbox_payload,
            candidate_path=candidate_path,
            arena_path=arena_path,
            sandbox_path=sandbox_path,
            repo_root=REPO_ROOT,
            target_period=args.target_period,
            run_mode=args.run_mode,
            freeze_receipt=args.freeze_receipt,
        )
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    output_path = _resolve_path(args.output) if args.output else default_anchor_output_path(candidate_path)
    if output_path.suffix.lower() != ".json":
        raise SystemExit("error: --output must end in .json")
    json_path, markdown_path = write_slate_files(output_path, payload)
    print(f"[ok] anchor slate JSON -> {json_path}")
    print(f"[ok] anchor slate Markdown -> {markdown_path}")
    print(
        "[info] "
        f"CORE3={payload['tiers']['CORE3']['boxed_count']} "
        f"EXTENDED6={payload['tiers']['EXTENDED6']['boxed_count']} "
        f"timing={payload['evidence_safety']['timing_status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
