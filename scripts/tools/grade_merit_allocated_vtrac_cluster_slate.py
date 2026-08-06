#!/usr/bin/env python3
"""Post-result grader for the merit-allocated VTRAC cluster slate."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_vtrac_index  # noqa: E402
from scripts.tools.compact_candidate_slates import (  # noqa: E402
    canonicalize,
    normalize_pick3,
    read_json,
    write_json,
)
from scripts.tools.merit_allocated_vtrac_cluster_slates import (  # noqa: E402
    ARTIFACT_TYPE,
)


GRADE_SCHEMA_VERSION = "merit_allocated_vtrac_cluster_slate_grade_v1"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _resolve_path(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def _rows(surface: Mapping[str, Any]) -> List[Dict[str, Any]]:
    return [
        dict(row)
        for row in (surface.get("candidates") or [])
        if isinstance(row, Mapping)
    ]


def grade_merit_slate(
    slate: Mapping[str, Any],
    *,
    winner: str,
    period: str = "",
    source_path: str = "",
) -> Dict[str, Any]:
    if str(slate.get("artifact_type") or "") != ARTIFACT_TYPE:
        raise ValueError(f"Expected artifact_type={ARTIFACT_TYPE}")
    winner_literal = normalize_pick3(winner)
    if not winner_literal:
        raise ValueError(f"Invalid Pick-3 winner: {winner!r}")
    winner_canonical = canonicalize(winner_literal)
    winner_index = get_vtrac_index(winner_literal)
    surfaces = slate.get("surfaces") if isinstance(slate.get("surfaces"), Mapping) else {}
    boxed_surface = (
        surfaces.get("BOXED12")
        if isinstance(surfaces.get("BOXED12"), Mapping)
        else {}
    )
    straight_surface = (
        surfaces.get("STRAIGHT12")
        if isinstance(surfaces.get("STRAIGHT12"), Mapping)
        else {}
    )
    boxed_rows = _rows(boxed_surface)
    straight_rows = _rows(straight_surface)

    boxed_matches = [
        row
        for row in boxed_rows
        if canonicalize(row.get("canonical")) == winner_canonical
    ]
    boxed_index_matches = [
        row
        for row in boxed_rows
        if winner_index is not None and row.get("vtrac_index") == winner_index
    ]
    straight_matches = [
        row
        for row in straight_rows
        if normalize_pick3(row.get("literal")) == winner_literal
    ]
    straight_box_matches = [
        row
        for row in straight_rows
        if canonicalize(row.get("literal")) == winner_canonical
    ]
    straight_index_matches = [
        row
        for row in straight_rows
        if winner_index is not None and row.get("vtrac_index") == winner_index
    ]

    if boxed_matches:
        boxed_class = "CANONICAL_BOX"
    elif boxed_index_matches:
        boxed_class = "VTRAC_ONLY"
    else:
        boxed_class = "NO_MATCH"

    if straight_matches:
        straight_class = "STRAIGHT"
    elif straight_box_matches:
        straight_class = "CANONICAL_ORDER_MISS"
    elif straight_index_matches:
        straight_class = "VTRAC_ONLY"
    else:
        straight_class = "NO_MATCH"

    selected_indices = [
        int(value)
        for value in (
            ((slate.get("pattern_scan_receipt") or {}).get("selected_vtrac_indices"))
            or []
        )
    ]
    return {
        "schema_version": GRADE_SCHEMA_VERSION,
        "artifact_type": "merit_allocated_vtrac_cluster_slate_grade",
        "status": "POST_RESULT_DIAGNOSTIC",
        "result_dependent": True,
        "generated_at": _now_iso(),
        "source_slate": str(source_path or ""),
        "state_key": str(((slate.get("metadata") or {}).get("state_key")) or ""),
        "results_date": str(
            ((slate.get("metadata") or {}).get("results_date")) or ""
        ),
        "period": str(period or ""),
        "winner": winner_literal,
        "winner_canonical": winner_canonical,
        "winner_vtrac_index": winner_index,
        "selected_vtrac_indices": selected_indices,
        "winner_cluster_selected": winner_index in selected_indices,
        "surface_grades": {
            "BOXED12": {
                "match_class": boxed_class,
                "canonical_hit": bool(boxed_matches),
                "vtrac_index_hit": bool(boxed_index_matches),
                "candidate_count": int(boxed_surface.get("candidate_count") or 0),
                "straight_equivalent_lines": int(
                    boxed_surface.get("straight_equivalent_lines") or 0
                ),
                "canonical_matches": boxed_matches,
                "vtrac_index_matches": boxed_index_matches,
            },
            "STRAIGHT12": {
                "match_class": straight_class,
                "straight_hit": bool(straight_matches),
                "canonical_present": bool(straight_box_matches),
                "vtrac_index_hit": bool(straight_index_matches),
                "candidate_count": int(
                    straight_surface.get("candidate_count") or 0
                ),
                "straight_matches": straight_matches,
                "canonical_matches": straight_box_matches,
                "vtrac_index_matches": straight_index_matches,
            },
        },
        "claim_boundary": (
            "Post-result diagnostic only. This does not retroactively create "
            "a frozen, selected, funded, or realized ticket."
        ),
    }


def render_grade_markdown(payload: Mapping[str, Any]) -> str:
    boxed = ((payload.get("surface_grades") or {}).get("BOXED12") or {})
    straight = ((payload.get("surface_grades") or {}).get("STRAIGHT12") or {})
    selected_text = ", ".join(
        str(value) for value in (payload.get("selected_vtrac_indices") or [])
    )
    lines = [
        "# Merit-Allocated VTRAC Cluster Slate Grade",
        "",
        f"- Status: `{payload.get('status')}`",
        f"- State: `{payload.get('state_key') or '-'}`",
        f"- Results date: `{payload.get('results_date') or '-'}`",
        f"- Period: `{payload.get('period') or '-'}`",
        f"- Winner: `{payload.get('winner')}`",
        f"- Winner canonical: `{payload.get('winner_canonical')}`",
        f"- Winner VTRAC index: `{payload.get('winner_vtrac_index')}`",
        f"- Selected VTRAC indices: `{selected_text or '-'}`",
        f"- Winner cluster selected: `{payload.get('winner_cluster_selected')}`",
        "",
        "> Post-result diagnostic only. It does not retroactively create a funded prediction.",
        "",
        "## Surface Grades",
        "",
        "| Surface | Match | Candidates | Box hit | Straight hit | VTRAC hit | Equivalent lines |",
        "|---|---|---:|---:|---:|---:|---:|",
        (
            f"| BOXED12 | {boxed.get('match_class')} | "
            f"{boxed.get('candidate_count') or 0} | "
            f"{int(bool(boxed.get('canonical_hit')))} | 0 | "
            f"{int(bool(boxed.get('vtrac_index_hit')))} | "
            f"{boxed.get('straight_equivalent_lines') or 0} |"
        ),
        (
            f"| STRAIGHT12 | {straight.get('match_class')} | "
            f"{straight.get('candidate_count') or 0} | "
            f"{int(bool(straight.get('canonical_present')))} | "
            f"{int(bool(straight.get('straight_hit')))} | "
            f"{int(bool(straight.get('vtrac_index_hit')))} | "
            f"{straight.get('candidate_count') or 0} |"
        ),
        "",
    ]
    return "\n".join(lines)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Grade a merit-allocated VTRAC cluster slate."
    )
    parser.add_argument("--slate", required=True)
    parser.add_argument("--winner", required=True)
    parser.add_argument("--period", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    slate_path = _resolve_path(args.slate)
    if not slate_path.exists():
        raise SystemExit(f"Missing slate: {slate_path}")
    try:
        payload = grade_merit_slate(
            read_json(slate_path),
            winner=args.winner,
            period=args.period,
            source_path=str(slate_path),
        )
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc

    output_path = _resolve_path(args.output)
    if output_path.suffix.lower() != ".json":
        raise SystemExit("error: --output must end in .json")
    write_json(output_path, payload)
    markdown_path = output_path.with_suffix(".md")
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_grade_markdown(payload), encoding="utf-8")
    print(f"[ok] merit slate grade JSON -> {output_path}")
    print(f"[ok] merit slate grade Markdown -> {markdown_path}")
    print(
        "[info] "
        f"BOXED12={payload['surface_grades']['BOXED12']['match_class']} "
        f"STRAIGHT12={payload['surface_grades']['STRAIGHT12']['match_class']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
