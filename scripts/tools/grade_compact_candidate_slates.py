#!/usr/bin/env python3
"""Grade compact candidate slates without mutating predictive artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_vtrac_index  # noqa: E402
from scripts.tools.compact_candidate_slates import (  # noqa: E402
    ANCHOR_ARTIFACT_TYPE,
    CLOSURE_ARTIFACT_TYPE,
    canonicalize,
    normalize_pick3,
    read_json,
    write_json,
)


GRADE_SCHEMA_VERSION = "compact_candidate_slate_grade_v1"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _resolve_path(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def _candidate_rows(tier: Mapping[str, Any]) -> List[Dict[str, Any]]:
    return [dict(row) for row in (tier.get("candidates") or []) if isinstance(row, Mapping)]


def grade_tier(tier_name: str, tier: Mapping[str, Any], winner: str) -> Dict[str, Any]:
    winner_literal = normalize_pick3(winner)
    if not winner_literal:
        raise ValueError(f"Invalid Pick-3 winner: {winner!r}")
    winner_canonical = canonicalize(winner_literal)
    winner_index = get_vtrac_index(winner_literal)
    candidates = _candidate_rows(tier)

    canonical_matches = [
        row for row in candidates if canonicalize(row.get("canonical")) == winner_canonical
    ]
    index_matches = [
        row
        for row in candidates
        if winner_index is not None and row.get("vtrac_index") == winner_index
    ]
    ordered_hint_matches = [
        {
            "canonical": canonicalize(row.get("canonical")),
            "ordered_hint": hint,
        }
        for row in candidates
        for hint in (row.get("ordered_hints") or [])
        if normalize_pick3(hint) == winner_literal
    ]

    if canonical_matches:
        match_class = "CANONICAL_BOX"
    elif index_matches:
        match_class = "VTRAC_ONLY"
    else:
        match_class = "NO_MATCH"

    direct_matches = [
        row
        for row in canonical_matches
        if "identity_anchor" in set(row.get("transform_types") or [])
        or not bool(row.get("is_derived"))
    ]
    derived_matches = [
        row for row in canonical_matches if bool(row.get("is_derived"))
    ]
    return {
        "tier": tier_name,
        "width_cap": int(tier.get("width_cap") or 0),
        "boxed_count": int(tier.get("boxed_count") or 0),
        "straight_equivalent_lines": int(tier.get("straight_equivalent_lines") or 0),
        "winner": winner_literal,
        "winner_canonical": winner_canonical,
        "winner_vtrac_index": winner_index,
        "match_class": match_class,
        "canonical_hit": bool(canonical_matches),
        "vtrac_index_hit": bool(index_matches),
        "ordered_hint_match": bool(ordered_hint_matches),
        "ordered_hint_credit_boundary": (
            "Diagnostic only. Ordered hints are not funded straight selections."
        ),
        "canonical_matches": canonical_matches,
        "vtrac_index_matches": index_matches,
        "ordered_hint_matches": ordered_hint_matches,
        "direct_canonical_match": bool(direct_matches),
        "derived_canonical_match": bool(derived_matches),
    }


def grade_slate(slate: Mapping[str, Any], winner: str) -> Dict[str, Any]:
    artifact_type = str(slate.get("artifact_type") or "")
    metadata = slate.get("metadata") if isinstance(slate.get("metadata"), Mapping) else {}
    tiers = slate.get("tiers") if isinstance(slate.get("tiers"), Mapping) else {}
    tier_grades: Dict[str, Dict[str, Any]] = {}
    for tier_name in ("CORE3", "EXTENDED6"):
        tier = tiers.get(tier_name)
        if isinstance(tier, Mapping):
            tier_grades[tier_name] = grade_tier(tier_name, tier, winner)

    core = tier_grades.get("CORE3") or {}
    extended = tier_grades.get("EXTENDED6") or {}
    incremental_lift = "NONE"
    if not core.get("canonical_hit") and extended.get("canonical_hit"):
        incremental_lift = "CANONICAL_GAIN"
    elif not core.get("vtrac_index_hit") and extended.get("vtrac_index_hit"):
        incremental_lift = "VTRAC_GAIN"

    return {
        "artifact_type": artifact_type,
        "status": str(slate.get("status") or ""),
        "state_key": str(metadata.get("state_key") or ""),
        "results_date": str(metadata.get("results_date") or ""),
        "target_period": str(metadata.get("target_period") or ""),
        "tier_grades": tier_grades,
        "extended6_incremental_lift_over_core3": incremental_lift,
        "claim_boundary": (
            "This is a post-result grade of an experimental surface, not proof "
            "of a frozen, selected, or funded ticket."
        ),
    }


def _joint_diagnosis(slate_grades: Sequence[Mapping[str, Any]], tier_name: str) -> str:
    by_type = {
        str(row.get("artifact_type") or ""): (
            ((row.get("tier_grades") or {}).get(tier_name) or {})
        )
        for row in slate_grades
    }
    anchor = by_type.get(ANCHOR_ARTIFACT_TYPE) or {}
    closure = by_type.get(CLOSURE_ARTIFACT_TYPE) or {}
    anchor_box = bool(anchor.get("canonical_hit"))
    closure_box = bool(closure.get("canonical_hit"))
    anchor_vtrac = bool(anchor.get("vtrac_index_hit"))
    closure_vtrac = bool(closure.get("vtrac_index_hit"))

    if anchor_box and closure_box:
        return "BOTH_CANONICAL"
    if anchor_box:
        return "ANCHOR_ONLY_CANONICAL"
    if closure_box:
        return "CLOSURE_ONLY_CANONICAL"
    if anchor_vtrac or closure_vtrac:
        return "VTRAC_TERRITORY_ONLY"
    return "MISS"


def grade_slates(
    *,
    slates: Sequence[Mapping[str, Any]],
    winner: str,
    period: str = "",
    source_paths: Sequence[str] = (),
) -> Dict[str, Any]:
    winner_literal = normalize_pick3(winner)
    if not winner_literal:
        raise ValueError(f"Invalid Pick-3 winner: {winner!r}")
    grades = [grade_slate(slate, winner_literal) for slate in slates]
    states = sorted({str(row.get("state_key") or "") for row in grades if row.get("state_key")})
    dates = sorted({str(row.get("results_date") or "") for row in grades if row.get("results_date")})
    return {
        "schema_version": GRADE_SCHEMA_VERSION,
        "artifact_type": "compact_candidate_slate_grade",
        "status": "POST_RESULT_DIAGNOSTIC",
        "result_dependent": True,
        "generated_at": _now_iso(),
        "state_key": states[0] if len(states) == 1 else "",
        "results_date": dates[0] if len(dates) == 1 else "",
        "period": str(period or ""),
        "winner": winner_literal,
        "winner_canonical": canonicalize(winner_literal),
        "winner_vtrac_index": get_vtrac_index(winner_literal),
        "source_slates": list(source_paths),
        "slate_grades": grades,
        "joint_diagnosis": {
            "CORE3": _joint_diagnosis(grades, "CORE3"),
            "EXTENDED6": _joint_diagnosis(grades, "EXTENDED6"),
        },
    }


def render_grade_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Compact Candidate Slate Grade",
        "",
        f"- Status: `{payload.get('status')}`",
        f"- State: `{payload.get('state_key') or '-'}`",
        f"- Results date: `{payload.get('results_date') or '-'}`",
        f"- Period: `{payload.get('period') or '-'}`",
        f"- Winner: `{payload.get('winner')}`",
        f"- Winner canonical: `{payload.get('winner_canonical')}`",
        f"- Winner VTRAC index: `{payload.get('winner_vtrac_index')}`",
        "",
        "> Post-result diagnostic only. It does not retroactively create a frozen or funded prediction.",
        "",
        "## Joint Diagnosis",
        "",
        f"- CORE3: `{(payload.get('joint_diagnosis') or {}).get('CORE3')}`",
        f"- EXTENDED6: `{(payload.get('joint_diagnosis') or {}).get('EXTENDED6')}`",
        "",
        "## Slate Grades",
        "",
    ]
    for slate in payload.get("slate_grades") or []:
        if not isinstance(slate, Mapping):
            continue
        lines.extend(
            [
                f"### {slate.get('artifact_type')}",
                "",
                f"- Extended lift: `{slate.get('extended6_incremental_lift_over_core3')}`",
                "",
                "| Tier | Match | Box | VTRAC | Ordered hint | Boxes | Straight-equivalent lines |",
                "|---|---|---:|---:|---:|---:|---:|",
            ]
        )
        for tier_name in ("CORE3", "EXTENDED6"):
            grade = (slate.get("tier_grades") or {}).get(tier_name) or {}
            lines.append(
                f"| {tier_name} | {grade.get('match_class') or '-'} | "
                f"{int(bool(grade.get('canonical_hit')))} | "
                f"{int(bool(grade.get('vtrac_index_hit')))} | "
                f"{int(bool(grade.get('ordered_hint_match')))} | "
                f"{grade.get('boxed_count') or 0} | "
                f"{grade.get('straight_equivalent_lines') or 0} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Grade one or more compact candidate slate JSON files."
    )
    parser.add_argument("--slate", action="append", required=True)
    parser.add_argument("--winner", required=True)
    parser.add_argument("--period", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    slate_paths = [_resolve_path(value) for value in args.slate]
    missing = [path for path in slate_paths if not path.exists()]
    if missing:
        raise SystemExit(f"Missing slate: {missing[0]}")
    slates = [read_json(path) for path in slate_paths]
    try:
        payload = grade_slates(
            slates=slates,
            winner=args.winner,
            period=args.period,
            source_paths=[str(path) for path in slate_paths],
        )
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc

    output_path = _resolve_path(args.output)
    if output_path.suffix.lower() != ".json":
        raise SystemExit("error: --output must end in .json")
    write_json(output_path, payload)
    markdown_path = output_path.with_suffix(".md")
    markdown_path.write_text(render_grade_markdown(payload), encoding="utf-8")
    print(f"[ok] slate grade JSON -> {output_path}")
    print(f"[ok] slate grade Markdown -> {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
