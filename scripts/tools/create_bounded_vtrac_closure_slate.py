#!/usr/bin/env python3
"""Create the bounded VTRAC/double/mirror translation slate."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.compact_candidate_slates import (  # noqa: E402
    build_closure_slate,
    default_closure_output_path,
    read_json,
    write_slate_files,
)


def _resolve_path(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Translate a Structural Convergence Anchor Slate through bounded "
            "same-index double/mirror and pair-key closures."
        )
    )
    parser.add_argument("--anchor-slate", required=True)
    parser.add_argument("--output", default="")
    args = parser.parse_args(argv)

    anchor_path = _resolve_path(args.anchor_slate)
    if not anchor_path.exists():
        raise SystemExit(f"Missing Anchor Slate: {anchor_path}")
    anchor_payload = read_json(anchor_path)
    try:
        payload = build_closure_slate(
            anchor_slate=anchor_payload,
            anchor_path=anchor_path,
            repo_root=REPO_ROOT,
        )
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc

    output_path = _resolve_path(args.output) if args.output else default_closure_output_path(anchor_path)
    if output_path.suffix.lower() != ".json":
        raise SystemExit("error: --output must end in .json")
    json_path, markdown_path = write_slate_files(output_path, payload)
    print(f"[ok] closure slate JSON -> {json_path}")
    print(f"[ok] closure slate Markdown -> {markdown_path}")
    print(
        "[info] "
        f"CORE3={payload['tiers']['CORE3']['boxed_count']} "
        f"EXTENDED6={payload['tiers']['EXTENDED6']['boxed_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
