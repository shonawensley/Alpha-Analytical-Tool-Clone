#!/usr/bin/env python3
"""
Shared pure functions for the compact candidate slate shadow tools.

The two slate types deliberately separate:

1. direct structural extraction from existing predictive evidence; and
2. bounded translation of those anchors through VTRAC mirror closures.

The module does not read results, mutate runtime artifacts, or modify any
existing Candidate Universe or Play Card output.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Set, Tuple

from modules.vtrac_reference import get_index_set, get_vtrac_index


SCHEMA_VERSION = "compact_candidate_slates_v1"
ANCHOR_ARTIFACT_TYPE = "structural_convergence_anchor_slate"
CLOSURE_ARTIFACT_TYPE = "bounded_vtrac_closure_slate"
EXPERIMENTAL_STATUS = "EXPERIMENTAL_SHADOW"

MIRROR_DIGIT_MAP: Dict[str, str] = {
    "0": "5",
    "1": "6",
    "2": "7",
    "3": "8",
    "4": "9",
    "5": "0",
    "6": "1",
    "7": "2",
    "8": "3",
    "9": "4",
}

# Raw evidence families. These weights are intentionally bounded and do not
# reuse raw tool scores, whose scales differ substantially by tool.
SOURCE_FAMILY_WEIGHT: Dict[str, float] = {
    "stable": 2.0,
    "digit_reduction": 1.6,
    "vtrac": 1.5,
    "hot_zones": 1.3,
    "aux_positional": 1.5,
    "due_doubles": 1.6,
    "profit_alerts": 1.5,
    "consensus": 1.7,
    "blackapple": 0.6,
    "combo_pack": 0.8,
    "other": 0.7,
}

ROLE_WEIGHT: Dict[str, float] = {
    "arena_dominant": 3.5,
    "arena_context_reinforced": 2.5,
    "arena_consensus": 2.0,
    "frontier_observation": 2.8,
    "sandbox_dominant": 3.0,
    "sandbox_context_reinforced": 2.2,
    "sandbox_secondary": 1.0,
    "survivor_frontier": 3.2,
    "survivor_last_remaining": 4.0,
    "r_consensus": 3.0,
    "candidate_universe": 1.0,
    "positional": 1.8,
    "due_double": 2.0,
    "profit_alert": 1.7,
    "blackapple": 0.5,
}

SYNTHETIC_SOURCE_FAMILIES = {"arena_synthesis", "translation_sandbox"}
CONTEXT_SOURCE_FAMILIES = {
    "aux_positional",
    "due_doubles",
    "profit_alerts",
    "consensus",
    "blackapple",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_pick3(value: Any) -> str:
    raw = str(value if value is not None else "").strip()
    if not raw:
        return ""
    if not re.fullmatch(r"\d{1,3}", raw):
        return ""
    return raw.zfill(3)


def canonicalize(value: Any) -> str:
    literal = normalize_pick3(value)
    return "".join(sorted(literal)) if literal else ""


def mirror_digit(value: str) -> str:
    return MIRROR_DIGIT_MAP.get(str(value), "")


def straight_equivalent_cost(canonical: str) -> int:
    canonical = canonicalize(canonical)
    if not canonical:
        return 0
    counts = Counter(canonical)
    denominator = 1
    for count in counts.values():
        denominator *= math.factorial(count)
    return math.factorial(3) // denominator


def boxed_members_for_index(index: Any) -> List[str]:
    try:
        numeric_index = int(index)
    except (TypeError, ValueError):
        return []
    return sorted({canonicalize(value) for value in get_index_set(numeric_index) if canonicalize(value)})


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return payload


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def safe_path(path: Optional[Path], repo_root: Optional[Path] = None) -> str:
    if path is None:
        return ""
    if repo_root is not None:
        try:
            return str(path.resolve().relative_to(repo_root.resolve()))
        except ValueError:
            pass
    return str(path)


def input_receipt(path: Optional[Path], role: str, repo_root: Optional[Path] = None) -> Dict[str, Any]:
    if path is None:
        return {"role": role, "available": False, "path": ""}
    return {
        "role": role,
        "available": path.exists(),
        "path": safe_path(path, repo_root),
        "sha256": sha256_path(path) if path.exists() else "",
    }


def assess_input_safety(
    *,
    candidate_universe: Mapping[str, Any],
    aggregated_arena: Optional[Mapping[str, Any]],
    translation_sandbox: Optional[Mapping[str, Any]],
    candidate_path: Optional[Path],
    run_mode: str,
    freeze_receipt: str = "",
    additional_paths: Sequence[Optional[Path]] = (),
) -> Dict[str, Any]:
    declared_winner_artifacts = bool(candidate_universe.get("contains_winners_artifacts"))
    leakage_issues = [str(value) for value in (candidate_universe.get("leakage_issues") or []) if str(value)]

    for payload in (aggregated_arena, translation_sandbox):
        metadata = (
            payload.get("metadata")
            if isinstance(payload, Mapping) and isinstance(payload.get("metadata"), Mapping)
            else {}
        )
        if bool(metadata.get("contains_winners_artifacts")):
            declared_winner_artifacts = True
        if isinstance(payload, Mapping) and bool(payload.get("result_dependent")):
            declared_winner_artifacts = True

    supplied_paths = [
        path
        for path in (candidate_path, *additional_paths)
        if path is not None
    ]
    winner_side_paths = [
        str(path)
        for path in supplied_paths
        if any("winner" in part.lower() for part in path.resolve().parts)
    ]
    non_predictive_paths = [
        str(path)
        for path in supplied_paths
        if "_predictive" not in {part.lower() for part in path.resolve().parts}
    ]
    source_root_predictive = bool(
        candidate_path is not None
        and "_predictive" in {part.lower() for part in candidate_path.resolve().parts}
    )
    run_mode = str(run_mode or "shadow").strip().lower()
    if run_mode not in {"shadow", "development_replay"}:
        raise ValueError("run_mode must be 'shadow' or 'development_replay'")

    if run_mode == "shadow" and (declared_winner_artifacts or leakage_issues):
        details = "; ".join(leakage_issues[:3]) or "winner artifacts declared"
        raise ValueError(
            "Shadow generation rejected winner-dependent input. "
            "Use a clean _predictive Candidate Universe or explicitly use development_replay. "
            f"Details: {details}"
        )
    if run_mode == "shadow" and winner_side_paths:
        raise ValueError(
            "Shadow generation rejected winner-side input path: "
            f"{winner_side_paths[0]}"
        )
    if (
        run_mode == "shadow"
        and supplied_paths
        and non_predictive_paths
        and not str(freeze_receipt or "").strip()
    ):
        raise ValueError(
            "Shadow generation requires supplied inputs under a _predictive root "
            "or an explicit freeze receipt. Use development_replay for historical "
            f"reconstruction. First non-predictive path: {non_predictive_paths[0]}"
        )

    results_date = str(candidate_universe.get("results_date") or "")
    generated_at = str(candidate_universe.get("generated_at") or "")
    timing_status = "UNVERIFIED_FREEZE"
    if freeze_receipt:
        timing_status = "EXPLICIT_FREEZE_RECEIPT"
    elif generated_at and results_date and generated_at[:10] > results_date:
        timing_status = "RETROSPECTIVE_WINNER_FREE_REPLAY"
    elif source_root_predictive:
        timing_status = "PREDICTIVE_ROOT_NO_FREEZE_RECEIPT"

    return {
        "run_mode": run_mode,
        "winner_artifacts_declared": declared_winner_artifacts,
        "leakage_issues": leakage_issues,
        "source_root_predictive": source_root_predictive,
        "winner_side_input_paths": winner_side_paths,
        "non_predictive_input_paths": non_predictive_paths,
        "winner_free_input": not declared_winner_artifacts and not leakage_issues,
        "freeze_receipt": str(freeze_receipt or ""),
        "timing_status": timing_status,
        "claim_boundary": (
            "Experimental candidate surface only. It is not selected, funded, "
            "or realized without a separate frozen receipt."
        ),
    }


def validate_artifact_alignment(
    *,
    candidate_universe: Mapping[str, Any],
    aggregated_arena: Optional[Mapping[str, Any]],
    translation_sandbox: Optional[Mapping[str, Any]],
) -> Dict[str, Any]:
    if not isinstance(candidate_universe.get("packs"), list):
        raise ValueError("Candidate Universe must contain a packs list")
    expected = {
        "state_key": str(candidate_universe.get("state_key") or ""),
        "results_date": str(candidate_universe.get("results_date") or ""),
        "history_date": str(candidate_universe.get("history_date") or ""),
        "profile": str(candidate_universe.get("profile") or ""),
    }
    if not expected["state_key"] or not expected["results_date"]:
        raise ValueError("Candidate Universe must declare state_key and results_date")

    checked: List[Dict[str, Any]] = []
    for role, payload in (
        ("aggregated_arena", aggregated_arena),
        ("translation_sandbox", translation_sandbox),
    ):
        if not isinstance(payload, Mapping):
            checked.append({"role": role, "available": False, "aligned": True})
            continue
        metadata = payload.get("metadata") if isinstance(payload.get("metadata"), Mapping) else {}
        mismatches: List[str] = []
        for field in ("state_key", "results_date", "history_date", "profile"):
            expected_value = expected.get(field) or ""
            actual_value = str(metadata.get(field) or "")
            if expected_value and actual_value and expected_value != actual_value:
                mismatches.append(
                    f"{field}: candidate={expected_value!r}, {role}={actual_value!r}"
                )
        if mismatches:
            raise ValueError(
                f"Artifact alignment failed for {role}: " + "; ".join(mismatches)
            )
        checked.append(
            {
                "role": role,
                "available": True,
                "aligned": True,
                "state_key": str(metadata.get("state_key") or ""),
                "results_date": str(metadata.get("results_date") or ""),
                "history_date": str(metadata.get("history_date") or ""),
                "profile": str(metadata.get("profile") or ""),
            }
        )
    return {"expected": expected, "checked": checked, "aligned": True}


def _source_family(source_id: str) -> str:
    source = str(source_id or "").strip().lower()
    if source.startswith("stable") or "stable_" in source:
        return "stable"
    if source.startswith("dr:") or "digit_reduction" in source:
        return "digit_reduction"
    if source.startswith("vtrac") or "vtrac_" in source:
        return "vtrac"
    if source.startswith("hot:") or "hot_zone" in source:
        return "hot_zones"
    if "aux_positional" in source or source.startswith("aux:positional") or "badge_combo" in source:
        return "aux_positional"
    if "due_double" in source or "doubles_mirror" in source or "mirror_pair_closure" in source:
        return "due_doubles"
    if "profit_alert" in source:
        return "profit_alerts"
    if "consensus" in source:
        return "consensus"
    if "blackapple" in source:
        return "blackapple"
    if source.startswith("pack") or "combo_pack" in source:
        return "combo_pack"
    return "other"


def _variant_from_source(source_id: str, fallback: str = "Unknown") -> str:
    source = str(source_id or "")
    for value in ("Combined", "Evening", "Midday"):
        if value.lower() in source.lower():
            return value
    return str(fallback or "Unknown")


def _empty_evidence_row(canonical: str) -> Dict[str, Any]:
    return {
        "canonical": canonical,
        "vtrac_index": get_vtrac_index(canonical),
        "straight_equivalent_cost": straight_equivalent_cost(canonical),
        "lineages": {},
        "roles": set(),
        "variants": set(),
        "tags": set(),
        "ordered_hints": set(),
    }


def _add_evidence(
    evidence: MutableMapping[str, Dict[str, Any]],
    *,
    value: Any,
    source_family: str,
    source_id: str,
    variant: str,
    role: str,
    weight: float,
    artifact_role: str,
    tags: Iterable[str] = (),
    ordered_hint: Any = "",
) -> None:
    canonical = canonicalize(value)
    if not canonical:
        return
    row = evidence.setdefault(canonical, _empty_evidence_row(canonical))
    family = str(source_family or "other")
    variant = str(variant or "Unknown")
    role = str(role or "candidate_universe")
    lineage_id = f"{family}|{variant}|{role}"
    lineage = row["lineages"].setdefault(
        lineage_id,
        {
            "lineage_id": lineage_id,
            "source_family": family,
            "variant": variant,
            "role": role,
            "weight": 0.0,
            "source_ids": set(),
            "artifact_roles": set(),
            "tags": set(),
        },
    )
    lineage["weight"] = max(float(lineage.get("weight") or 0.0), float(weight or 0.0))
    lineage["source_ids"].add(str(source_id or "?"))
    lineage["artifact_roles"].add(str(artifact_role or "?"))
    lineage["tags"].update(str(tag) for tag in tags if str(tag))
    row["roles"].add(role)
    row["variants"].add(variant)
    row["tags"].update(str(tag) for tag in tags if str(tag))
    hint = normalize_pick3(ordered_hint)
    if hint and canonicalize(hint) == canonical:
        row["ordered_hints"].add(hint)


def _add_ranked_values(
    evidence: MutableMapping[str, Dict[str, Any]],
    values: Sequence[Any],
    *,
    role: str,
    source_family: str,
    artifact_role: str,
    base_weight: float,
    variant: str = "Unknown",
    tags: Iterable[str] = (),
) -> None:
    for rank, value in enumerate(values, start=1):
        rank_weight = max(0.5, float(base_weight) - ((rank - 1) * 0.12))
        _add_evidence(
            evidence,
            value=value,
            source_family=source_family,
            source_id=f"{artifact_role}:{role}:rank={rank}",
            variant=variant,
            role=role,
            weight=rank_weight,
            artifact_role=artifact_role,
            tags=[*tags, f"rank:{rank}"],
        )


def _parse_arena_row_sources(
    evidence: MutableMapping[str, Dict[str, Any]],
    *,
    row: Mapping[str, Any],
    role: str,
    artifact_role: str,
    rank: int,
) -> None:
    value = row.get("value")
    _add_evidence(
        evidence,
        value=value,
        source_family="arena_synthesis",
        source_id=f"{artifact_role}:{role}:rank={rank}",
        variant="Unknown",
        role=role,
        weight=max(0.8, ROLE_WEIGHT.get(role, 1.0) - ((rank - 1) * 0.1)),
        artifact_role=artifact_role,
        tags=[
            f"rank:{rank}",
            f"support_count:{int(row.get('support_count') or 0)}",
            f"string_source_count:{int(row.get('string_source_count') or 0)}",
            f"context_source_count:{int(row.get('context_source_count') or 0)}",
        ],
    )
    for source in row.get("sources") or []:
        if not isinstance(source, Mapping):
            continue
        source_id = str(source.get("source") or "?")
        family = _source_family(source_id)
        _add_evidence(
            evidence,
            value=value,
            source_family=family,
            source_id=source_id,
            variant=_variant_from_source(source_id),
            role=role,
            weight=SOURCE_FAMILY_WEIGHT.get(family, SOURCE_FAMILY_WEIGHT["other"]),
            artifact_role=artifact_role,
            tags=[f"arena_raw_score:{source.get('score')}"],
        )
    for literal in row.get("example_literals") or []:
        _add_evidence(
            evidence,
            value=value,
            source_family="arena_synthesis",
            source_id=f"{artifact_role}:{role}:literal",
            variant="Unknown",
            role=role,
            weight=0.0,
            artifact_role=artifact_role,
            ordered_hint=literal,
        )


def _collect_arena_evidence(
    evidence: MutableMapping[str, Dict[str, Any]],
    arena: Optional[Mapping[str, Any]],
    context: MutableMapping[str, Any],
) -> None:
    if not isinstance(arena, Mapping):
        return
    synthesis = arena.get("arena_synthesis") if isinstance(arena.get("arena_synthesis"), Mapping) else {}
    relations = arena.get("cross_tool_relations") if isinstance(arena.get("cross_tool_relations"), Mapping) else {}

    for role, key in (
        ("arena_dominant", "dominant_canonicals"),
        ("arena_context_reinforced", "context_reinforced_canonicals"),
    ):
        rows = synthesis.get(key) or []
        for rank, row in enumerate(rows, start=1):
            if isinstance(row, Mapping):
                _parse_arena_row_sources(
                    evidence,
                    row=row,
                    role=role,
                    artifact_role="aggregated_arena",
                    rank=rank,
                )

    consensus_rows = relations.get("canonical_consensus_top") or []
    for rank, row in enumerate(consensus_rows, start=1):
        if not isinstance(row, Mapping):
            continue
        _add_evidence(
            evidence,
            value=row.get("value"),
            source_family="arena_synthesis",
            source_id=f"aggregated_arena:canonical_consensus:rank={rank}",
            variant="Unknown",
            role="arena_consensus",
            weight=max(0.5, 2.0 - ((rank - 1) * 0.08)),
            artifact_role="aggregated_arena",
            tags=[f"rank:{rank}"],
        )

    survivor = synthesis.get("stable_survivor_context")
    if isinstance(survivor, Mapping):
        for entry_index, entry in enumerate(survivor.get("frontier_examples") or [], start=1):
            if not isinstance(entry, Mapping):
                continue
            variant = str(entry.get("section") or "Unknown")
            source_id = (
                f"frontier:{variant}:{entry.get('set')}:{entry.get('draw')}:"
                f"col={entry.get('frontier_column')}:row={entry_index}"
            )
            tags = [
                "frontier",
                f"set:{entry.get('set')}",
                f"draw:{entry.get('draw')}",
                f"frontier_column:{entry.get('frontier_column')}",
                f"progression_columns:{entry.get('progression_column_count')}",
            ]
            for value in entry.get("exact3digit_patterns") or []:
                _add_evidence(
                    evidence,
                    value=value,
                    source_family="stable",
                    source_id=source_id,
                    variant=variant,
                    role="frontier_observation",
                    weight=SOURCE_FAMILY_WEIGHT["stable"],
                    artifact_role="aggregated_arena",
                    tags=tags,
                    ordered_hint=value,
                )

    watchlist = synthesis.get("vtrac_literal_watchlist") or []
    for rank, row in enumerate(watchlist, start=1):
        if not isinstance(row, Mapping):
            continue
        try:
            index = int(row.get("vtrac_index"))
        except (TypeError, ValueError):
            continue
        context["vtrac_rank"].setdefault(index, rank)
        context["vtrac_tags"][index].update(
            {
                f"arena_vtrac_rank:{rank}",
                f"arena_vtrac_support:{int(row.get('support_count') or 0)}",
            }
        )
        for value in row.get("candidate_canonicals") or []:
            _add_evidence(
                evidence,
                value=value,
                source_family="vtrac",
                source_id=f"aggregated_arena:vtrac_watchlist:{index}",
                variant="Unknown",
                role="arena_consensus",
                weight=max(0.5, 1.8 - ((rank - 1) * 0.12)),
                artifact_role="aggregated_arena",
                tags=[f"vtrac_rank:{rank}", f"vtrac_index:{index}"],
            )


def _collect_sandbox_evidence(
    evidence: MutableMapping[str, Dict[str, Any]],
    sandbox: Optional[Mapping[str, Any]],
    context: MutableMapping[str, Any],
) -> None:
    if not isinstance(sandbox, Mapping):
        return
    brain1 = sandbox.get("brain1_core") if isinstance(sandbox.get("brain1_core"), Mapping) else {}
    brain2 = sandbox.get("brain2_context") if isinstance(sandbox.get("brain2_context"), Mapping) else {}

    for key, role, weight in (
        ("dominant_canonicals", "sandbox_dominant", 3.0),
        ("context_reinforced_canonicals", "sandbox_context_reinforced", 2.2),
        ("secondary_canonicals", "sandbox_secondary", 1.0),
        ("survivor_frontier_canonicals", "survivor_frontier", 3.2),
        ("survivor_last_remaining_canonicals", "survivor_last_remaining", 4.0),
    ):
        _add_ranked_values(
            evidence,
            list(brain1.get(key) or []),
            role=role,
            source_family="translation_sandbox",
            artifact_role="translation_sandbox",
            base_weight=weight,
        )

    r_consensus = brain1.get("r_consensus_context")
    if isinstance(r_consensus, Mapping):
        _add_ranked_values(
            evidence,
            list(r_consensus.get("top_support_canonicals") or []),
            role="r_consensus",
            source_family="consensus",
            artifact_role="translation_sandbox",
            base_weight=3.0,
            tags=[
                f"signal_strength:{r_consensus.get('signal_strength_class')}",
                f"event_count:{r_consensus.get('event_count')}",
            ],
        )

    for rank, value in enumerate(brain1.get("dominant_vtrac_indices") or [], start=1):
        try:
            index = int(value)
        except (TypeError, ValueError):
            continue
        context["vtrac_rank"].setdefault(index, rank)
        context["vtrac_tags"][index].add(f"sandbox_dominant_vtrac_rank:{rank}")
    for value in brain1.get("watchlist_indices") or []:
        try:
            index = int(value)
        except (TypeError, ValueError):
            continue
        context["watchlist_indices"].add(index)

    _add_ranked_values(
        evidence,
        list(brain2.get("profit_alert_implied_canonicals") or []),
        role="profit_alert",
        source_family="profit_alerts",
        artifact_role="translation_sandbox",
        base_weight=1.7,
    )
    _add_ranked_values(
        evidence,
        list(brain2.get("blackapple_recommended_canonicals") or []),
        role="blackapple",
        source_family="blackapple",
        artifact_role="translation_sandbox",
        base_weight=0.5,
    )
    _add_ranked_values(
        evidence,
        list(brain2.get("due_double_example_canonicals") or []),
        role="due_double",
        source_family="due_doubles",
        artifact_role="translation_sandbox",
        base_weight=2.0,
        tags=["due_double"],
    )

    for rank, row in enumerate(brain2.get("positional_shortlist_top") or [], start=1):
        if not isinstance(row, Mapping):
            continue
        tags = [str(tag) for tag in (row.get("tags") or []) if str(tag)]
        canonical = canonicalize(row.get("canonical") or row.get("combo"))
        _add_evidence(
            evidence,
            value=canonical,
            source_family="aux_positional",
            source_id=f"translation_sandbox:positional:rank={rank}",
            variant="Unknown",
            role="positional",
            weight=max(0.5, 1.8 - ((rank - 1) * 0.1)),
            artifact_role="translation_sandbox",
            tags=[*tags, f"rank:{rank}"],
            ordered_hint=row.get("combo"),
        )
        if canonical:
            if any(tag.startswith("Mirror-Echo") for tag in tags):
                context["mirror_echo_canonicals"].add(canonical)
            if "Double-Pressure" in tags:
                context["double_pressure_canonicals"].add(canonical)
            for digit in canonical:
                lineage = f"positional|rank={rank}|digit={digit}"
                context["digit_support"][digit]["lineages"].add(lineage)
                context["digit_support"][digit]["score"] += max(0.2, 1.0 - ((rank - 1) * 0.06))

    for value in brain2.get("due_double_example_canonicals") or []:
        canonical = canonicalize(value)
        if not canonical:
            continue
        context["due_double_canonicals"].add(canonical)
        index = get_vtrac_index(canonical)
        if index is not None:
            context["due_double_indices"].add(index)
        for digit in canonical:
            context["digit_support"][digit]["lineages"].add(f"due_double|{canonical}|{digit}")
            context["digit_support"][digit]["score"] += 0.35

    for row in brain2.get("top_profit_alerts") or []:
        if not isinstance(row, Mapping):
            continue
        canonical = canonicalize(row.get("canonical"))
        if not canonical:
            continue
        strength = float(row.get("strength") or 0.0)
        for digit in canonical:
            context["digit_support"][digit]["lineages"].add(
                f"profit_alert|{row.get('alert_id')}|{canonical}|{digit}"
            )
            context["digit_support"][digit]["score"] += min(0.8, strength * 0.15)

    context["positional_signal_notes"].extend(
        str(value) for value in (brain2.get("positional_signal_notes") or []) if str(value)
    )


def _collect_candidate_universe_evidence(
    evidence: MutableMapping[str, Dict[str, Any]],
    candidate_universe: Mapping[str, Any],
    context: MutableMapping[str, Any],
) -> None:
    for pack in candidate_universe.get("packs") or []:
        if not isinstance(pack, Mapping):
            continue
        method_id = str(pack.get("method_id") or "other")
        family = _source_family(method_id)
        variant = str(pack.get("variant") or "Unknown")
        pack_id = str(pack.get("pack_id") or "?")
        tags = [str(tag) for tag in (pack.get("why_tags") or []) if str(tag)]
        weight = SOURCE_FAMILY_WEIGHT.get(family, SOURCE_FAMILY_WEIGHT["other"])
        canonical_values = {
            canonicalize(value)
            for value in [
                *(pack.get("canonicals") or []),
                *(pack.get("combos") or []),
            ]
            if canonicalize(value)
        }
        ordered_by_canonical: Dict[str, List[str]] = defaultdict(list)
        for value in pack.get("combos") or []:
            literal = normalize_pick3(value)
            if literal:
                ordered_by_canonical[canonicalize(literal)].append(literal)
        for canonical in sorted(canonical_values):
            _add_evidence(
                evidence,
                value=canonical,
                source_family=family,
                source_id=f"candidate_universe:{method_id}:{pack_id}",
                variant=variant,
                role="candidate_universe",
                weight=weight,
                artifact_role="candidate_universe",
                tags=[*tags, f"method:{method_id}", f"pack:{pack_id}"],
                ordered_hint=(ordered_by_canonical.get(canonical) or [""])[0],
            )
            if any(tag.startswith("Mirror-Echo") for tag in tags):
                context["mirror_echo_canonicals"].add(canonical)
            if "Double-Pressure" in tags:
                context["double_pressure_canonicals"].add(canonical)
            if family == "due_doubles":
                context["due_double_canonicals"].add(canonical)
                index = get_vtrac_index(canonical)
                if index is not None:
                    context["due_double_indices"].add(index)

    for envelope_rank, envelope in enumerate(candidate_universe.get("digit_envelopes") or [], start=1):
        if not isinstance(envelope, Mapping):
            continue
        for digit in envelope.get("digits") or []:
            digit = str(digit)
            if digit not in MIRROR_DIGIT_MAP:
                continue
            context["digit_support"][digit]["lineages"].add(
                f"digit_envelope|rank={envelope_rank}|digit={digit}"
            )
            context["digit_support"][digit]["score"] += max(0.15, 0.5 - ((envelope_rank - 1) * 0.05))


def build_evidence_index(
    *,
    candidate_universe: Mapping[str, Any],
    aggregated_arena: Optional[Mapping[str, Any]] = None,
    translation_sandbox: Optional[Mapping[str, Any]] = None,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    evidence: Dict[str, Dict[str, Any]] = {}
    context: Dict[str, Any] = {
        "vtrac_rank": {},
        "vtrac_tags": defaultdict(set),
        "watchlist_indices": set(),
        "due_double_canonicals": set(),
        "due_double_indices": set(),
        "mirror_echo_canonicals": set(),
        "double_pressure_canonicals": set(),
        "digit_support": defaultdict(lambda: {"score": 0.0, "lineages": set()}),
        "positional_signal_notes": [],
    }
    _collect_candidate_universe_evidence(evidence, candidate_universe, context)
    _collect_arena_evidence(evidence, aggregated_arena, context)
    _collect_sandbox_evidence(evidence, translation_sandbox, context)
    return evidence, context


def _source_occurrence_count(row: Mapping[str, Any], role: str) -> int:
    count = 0
    for lineage in (row.get("lineages") or {}).values():
        if not isinstance(lineage, Mapping) or str(lineage.get("role")) != role:
            continue
        count += len(lineage.get("source_ids") or [])
    return count


def score_anchor_candidate(
    row: Mapping[str, Any],
    *,
    context: Mapping[str, Any],
    target_period: str = "Day",
) -> Tuple[float, Dict[str, float]]:
    lineages = list((row.get("lineages") or {}).values())
    roles = set(row.get("roles") or [])
    variants = {str(value) for value in (row.get("variants") or []) if str(value) != "Unknown"}
    raw_families = {
        str(lineage.get("source_family"))
        for lineage in lineages
        if isinstance(lineage, Mapping)
        and str(lineage.get("source_family")) not in SYNTHETIC_SOURCE_FAMILIES
    }
    context_families = raw_families & CONTEXT_SOURCE_FAMILIES

    role_score = min(12.0, sum(ROLE_WEIGHT.get(role, 0.0) for role in roles))
    source_score = min(9.0, sum(SOURCE_FAMILY_WEIGHT.get(family, 0.7) for family in raw_families))
    variant_score = min(2.4, len(variants) * 0.8)
    context_score = min(1.8, len(context_families) * 0.45)
    target_period = str(target_period or "Day")
    target_alignment = 0.0
    if target_period in {"Midday", "Evening", "Combined"}:
        if target_period in variants:
            target_alignment += 0.8
        if target_period != "Combined" and "Combined" in variants:
            target_alignment += 0.4

    frontier_occurrences = _source_occurrence_count(row, "frontier_observation")
    frontier_recurrence = min(2.0, max(0, frontier_occurrences - 1) * 0.35)

    index = row.get("vtrac_index")
    vtrac_rank = (context.get("vtrac_rank") or {}).get(index)
    vtrac_score = 0.0
    if isinstance(vtrac_rank, int):
        vtrac_score = max(0.4, 2.0 - ((vtrac_rank - 1) * 0.25))
    elif index in (context.get("watchlist_indices") or set()):
        vtrac_score = 0.5

    canonical = str(row.get("canonical") or "")
    due_double_score = 0.0
    if canonical in (context.get("due_double_canonicals") or set()):
        due_double_score += 1.0
    if canonical in (context.get("mirror_echo_canonicals") or set()):
        due_double_score += 0.6
    if canonical in (context.get("double_pressure_canonicals") or set()):
        due_double_score += 0.5

    cost = int(row.get("straight_equivalent_cost") or 0)
    cost_efficiency = 0.45 if cost == 3 else (0.75 if cost == 1 else 0.0)

    noise_penalty = 0.0
    if len(raw_families) == 1 and not roles.intersection(
        {
            "arena_dominant",
            "survivor_frontier",
            "survivor_last_remaining",
            "r_consensus",
        }
    ):
        noise_penalty += 1.5
    if raw_families and raw_families <= {"blackapple"}:
        noise_penalty += 2.0

    components = {
        "role_strength": round(role_score, 4),
        "independent_source_strength": round(source_score, 4),
        "cross_variant_support": round(variant_score, 4),
        "target_period_alignment": round(target_alignment, 4),
        "context_confirmation": round(context_score, 4),
        "frontier_recurrence": round(frontier_recurrence, 4),
        "vtrac_corridor_support": round(vtrac_score, 4),
        "double_mirror_support": round(due_double_score, 4),
        "cost_efficiency": round(cost_efficiency, 4),
        "noise_penalty": round(-noise_penalty, 4),
    }
    total = round(sum(components.values()), 4)
    return total, components


def _serialize_lineage(lineage: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "lineage_id": str(lineage.get("lineage_id") or ""),
        "source_family": str(lineage.get("source_family") or ""),
        "variant": str(lineage.get("variant") or "Unknown"),
        "role": str(lineage.get("role") or ""),
        "weight": round(float(lineage.get("weight") or 0.0), 4),
        "source_ids": sorted(str(value) for value in (lineage.get("source_ids") or [])),
        "artifact_roles": sorted(str(value) for value in (lineage.get("artifact_roles") or [])),
        "tags": sorted(str(value) for value in (lineage.get("tags") or [])),
    }


def serialize_anchor_candidate(
    row: Mapping[str, Any],
    *,
    score: float,
    components: Mapping[str, float],
) -> Dict[str, Any]:
    lineages = sorted(
        (_serialize_lineage(value) for value in (row.get("lineages") or {}).values()),
        key=lambda value: (
            value["source_family"],
            value["variant"],
            value["role"],
            value["lineage_id"],
        ),
    )
    raw_families = sorted(
        {
            value["source_family"]
            for value in lineages
            if value["source_family"] not in SYNTHETIC_SOURCE_FAMILIES
        }
    )
    return {
        "canonical": str(row.get("canonical") or ""),
        "vtrac_index": row.get("vtrac_index"),
        "score": round(score, 4),
        "score_components": dict(components),
        "straight_equivalent_cost": int(row.get("straight_equivalent_cost") or 0),
        "roles": sorted(str(value) for value in (row.get("roles") or [])),
        "source_families": raw_families,
        "variants": sorted(str(value) for value in (row.get("variants") or [])),
        "tags": sorted(str(value) for value in (row.get("tags") or [])),
        "ordered_hints": sorted(str(value) for value in (row.get("ordered_hints") or [])),
        "lineages": lineages,
    }


def select_nested_tiers(
    ranked_candidates: Sequence[Mapping[str, Any]],
    *,
    core_width: int = 3,
    extended_width: int = 6,
    minimum_score: float = 2.0,
    core_index_cap: int = 2,
    extended_index_cap: int = 3,
    require_derived_in_core: bool = False,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    eligible = [
        dict(row)
        for row in ranked_candidates
        if canonicalize(row.get("canonical")) and float(row.get("score") or 0.0) >= minimum_score
    ]

    def add_with_cap(
        selected: List[Dict[str, Any]],
        index_counts: Counter,
        row: Mapping[str, Any],
        cap: int,
    ) -> bool:
        canonical = canonicalize(row.get("canonical"))
        if any(canonicalize(value.get("canonical")) == canonical for value in selected):
            return False
        index = row.get("vtrac_index")
        if index is not None and index_counts[index] >= cap:
            return False
        selected.append(dict(row))
        if index is not None:
            index_counts[index] += 1
        return True

    core: List[Dict[str, Any]] = []
    core_counts: Counter = Counter()
    if require_derived_in_core:
        best_derived = next((row for row in eligible if bool(row.get("is_derived"))), None)
        if best_derived is not None:
            add_with_cap(core, core_counts, best_derived, core_index_cap)
    for row in eligible:
        if len(core) >= core_width:
            break
        add_with_cap(core, core_counts, row, core_index_cap)

    core.sort(key=lambda row: (-float(row.get("score") or 0.0), str(row.get("canonical") or "")))
    extended = [dict(row) for row in core]
    extended_counts: Counter = Counter(row.get("vtrac_index") for row in extended if row.get("vtrac_index") is not None)
    for row in eligible:
        if len(extended) >= extended_width:
            break
        add_with_cap(extended, extended_counts, row, extended_index_cap)
    return core, extended


def tier_receipt(candidates: Sequence[Mapping[str, Any]], width_cap: int) -> Dict[str, Any]:
    canonicals = [canonicalize(row.get("canonical")) for row in candidates if canonicalize(row.get("canonical"))]
    return {
        "width_cap": int(width_cap),
        "unused_slots": max(0, int(width_cap) - len(canonicals)),
        "boxed_canonicals": canonicals,
        "boxed_count": len(canonicals),
        "straight_equivalent_lines": sum(straight_equivalent_cost(value) for value in canonicals),
        "candidates": [dict(row) for row in candidates],
    }


def _serialize_context(context: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "vtrac_rank": {
            str(key): int(value)
            for key, value in sorted((context.get("vtrac_rank") or {}).items(), key=lambda item: int(item[0]))
        },
        "vtrac_tags": {
            str(key): sorted(str(value) for value in values)
            for key, values in sorted((context.get("vtrac_tags") or {}).items(), key=lambda item: int(item[0]))
        },
        "watchlist_indices": sorted(int(value) for value in (context.get("watchlist_indices") or set())),
        "due_double_canonicals": sorted(context.get("due_double_canonicals") or set()),
        "due_double_indices": sorted(int(value) for value in (context.get("due_double_indices") or set())),
        "mirror_echo_canonicals": sorted(context.get("mirror_echo_canonicals") or set()),
        "double_pressure_canonicals": sorted(context.get("double_pressure_canonicals") or set()),
        "digit_support": {
            digit: {
                "score": round(float(values.get("score") or 0.0), 4),
                "lineages": sorted(str(value) for value in (values.get("lineages") or set())),
            }
            for digit, values in sorted((context.get("digit_support") or {}).items())
        },
        "positional_signal_notes": list(dict.fromkeys(context.get("positional_signal_notes") or [])),
    }


def build_anchor_slate(
    *,
    candidate_universe: Mapping[str, Any],
    aggregated_arena: Optional[Mapping[str, Any]] = None,
    translation_sandbox: Optional[Mapping[str, Any]] = None,
    candidate_path: Optional[Path] = None,
    arena_path: Optional[Path] = None,
    sandbox_path: Optional[Path] = None,
    repo_root: Optional[Path] = None,
    target_period: str = "Day",
    run_mode: str = "shadow",
    freeze_receipt: str = "",
) -> Dict[str, Any]:
    alignment = validate_artifact_alignment(
        candidate_universe=candidate_universe,
        aggregated_arena=aggregated_arena,
        translation_sandbox=translation_sandbox,
    )
    safety = assess_input_safety(
        candidate_universe=candidate_universe,
        aggregated_arena=aggregated_arena,
        translation_sandbox=translation_sandbox,
        candidate_path=candidate_path,
        run_mode=run_mode,
        freeze_receipt=freeze_receipt,
        additional_paths=(arena_path, sandbox_path),
    )
    evidence, context = build_evidence_index(
        candidate_universe=candidate_universe,
        aggregated_arena=aggregated_arena,
        translation_sandbox=translation_sandbox,
    )

    ranked: List[Dict[str, Any]] = []
    for row in evidence.values():
        score, components = score_anchor_candidate(
            row,
            context=context,
            target_period=target_period,
        )
        ranked.append(serialize_anchor_candidate(row, score=score, components=components))
    ranked.sort(key=lambda row: (-float(row.get("score") or 0.0), str(row.get("canonical") or "")))
    for rank, row in enumerate(ranked, start=1):
        row["rank"] = rank

    core, extended = select_nested_tiers(
        ranked,
        core_width=3,
        extended_width=6,
        minimum_score=2.0,
        core_index_cap=2,
        extended_index_cap=3,
    )
    metadata = {
        "generated_at": now_iso(),
        "state_key": str(candidate_universe.get("state_key") or ""),
        "results_date": str(candidate_universe.get("results_date") or ""),
        "history_date": str(candidate_universe.get("history_date") or ""),
        "profile": str(candidate_universe.get("profile") or ""),
        "target_period": str(target_period or "Day"),
        "run_mode": run_mode,
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "artifact_type": ANCHOR_ARTIFACT_TYPE,
        "status": EXPERIMENTAL_STATUS,
        "metadata": metadata,
        "evidence_safety": safety,
        "input_alignment": alignment,
        "source_artifacts": [
            input_receipt(candidate_path, "candidate_universe", repo_root),
            input_receipt(arena_path, "aggregated_arena", repo_root),
            input_receipt(sandbox_path, "translation_sandbox", repo_root),
        ],
        "scoring_contract": {
            "raw_tool_scores_reused": False,
            "independent_lineage_rule": "One scored lineage per source_family + variant + role.",
            "source_family_weights": dict(SOURCE_FAMILY_WEIGHT),
            "role_weights": dict(ROLE_WEIGHT),
            "core_width": 3,
            "extended_width": 6,
            "core_vtrac_index_cap": 2,
            "extended_vtrac_index_cap": 3,
            "minimum_score": 2.0,
            "static_scoreboard_rank_used": False,
        },
        "translation_context": _serialize_context(context),
        "ranked_candidates": ranked,
        "tiers": {
            "CORE3": tier_receipt(core, 3),
            "EXTENDED6": tier_receipt(extended, 6),
        },
    }


def _deserialize_anchor_context(payload: Mapping[str, Any]) -> Dict[str, Any]:
    raw = payload.get("translation_context") if isinstance(payload.get("translation_context"), Mapping) else {}
    return {
        "vtrac_rank": {
            int(key): int(value)
            for key, value in (raw.get("vtrac_rank") or {}).items()
            if str(key).isdigit()
        },
        "vtrac_tags": {
            int(key): set(str(value) for value in values)
            for key, values in (raw.get("vtrac_tags") or {}).items()
            if str(key).isdigit()
        },
        "watchlist_indices": set(int(value) for value in (raw.get("watchlist_indices") or [])),
        "due_double_canonicals": set(raw.get("due_double_canonicals") or []),
        "due_double_indices": set(int(value) for value in (raw.get("due_double_indices") or [])),
        "mirror_echo_canonicals": set(raw.get("mirror_echo_canonicals") or []),
        "double_pressure_canonicals": set(raw.get("double_pressure_canonicals") or []),
        "digit_support": {
            str(digit): {
                "score": float(values.get("score") or 0.0),
                "lineages": set(values.get("lineages") or []),
            }
            for digit, values in (raw.get("digit_support") or {}).items()
            if isinstance(values, Mapping)
        },
        "positional_signal_notes": list(raw.get("positional_signal_notes") or []),
    }


def _double_parts(canonical: str) -> Optional[Tuple[str, str]]:
    canonical = canonicalize(canonical)
    if not canonical:
        return None
    counts = Counter(canonical)
    repeated = [digit for digit, count in counts.items() if count == 2]
    if len(repeated) != 1:
        return None
    repeated_digit = repeated[0]
    key_digit = next(digit for digit, count in counts.items() if count == 1)
    return repeated_digit, key_digit


def _add_closure_candidate(
    pool: MutableMapping[str, Dict[str, Any]],
    *,
    canonical: str,
    parent: Mapping[str, Any],
    transform_type: str,
    transform_prior: float,
    gate_lineages: Iterable[str],
    tags: Iterable[str],
    context: Mapping[str, Any],
    anchor_lookup: Mapping[str, Mapping[str, Any]],
    key_digit: str = "",
    transform_distance: int = 0,
) -> None:
    canonical = canonicalize(canonical)
    if not canonical:
        return
    parent_canonical = canonicalize(parent.get("canonical"))
    parent_index = parent.get("vtrac_index")
    index = get_vtrac_index(canonical)
    same_index = parent_index is not None and index == parent_index
    direct = anchor_lookup.get(canonical)
    direct_score = float(direct.get("score") or 0.0) if isinstance(direct, Mapping) else 0.0
    parent_score = float(parent.get("score") or 0.0)
    gate_set = {str(value) for value in gate_lineages if str(value)}
    due_support = (
        canonical in (context.get("due_double_canonicals") or set())
        or index in (context.get("due_double_indices") or set())
    )
    mirror_support = (
        canonical in (context.get("mirror_echo_canonicals") or set())
        or canonical in (context.get("double_pressure_canonicals") or set())
    )
    digit_row = (context.get("digit_support") or {}).get(key_digit, {}) if key_digit else {}
    key_support = float(digit_row.get("score") or 0.0) if isinstance(digit_row, Mapping) else 0.0
    key_lineages = set(digit_row.get("lineages") or []) if isinstance(digit_row, Mapping) else set()
    gate_set.update(str(value) for value in key_lineages)

    vtrac_rank = (context.get("vtrac_rank") or {}).get(index)
    vtrac_score = 0.0
    if isinstance(vtrac_rank, int):
        vtrac_score = max(0.3, 1.5 - ((vtrac_rank - 1) * 0.2))
    elif index in (context.get("watchlist_indices") or set()):
        vtrac_score = 0.4

    complexity_penalty = max(0.0, (transform_distance - 1) * 0.55)
    unsupported_penalty = 0.0
    if transform_type != "identity_anchor" and direct_score <= 0.0 and len(gate_set) < 2:
        unsupported_penalty = 1.2

    components = {
        "parent_anchor_strength": round(min(5.0, parent_score / 4.0), 4),
        "direct_candidate_support": round(min(4.0, direct_score / 4.0), 4),
        "transform_prior": round(transform_prior, 4),
        "same_index_preservation": 1.8 if same_index else 0.0,
        "due_double_support": 1.2 if due_support else 0.0,
        "mirror_positional_support": 1.0 if mirror_support else 0.0,
        "key_digit_support": round(min(1.8, key_support * 0.45), 4),
        "vtrac_corridor_support": round(vtrac_score, 4),
        "lineage_diversity": round(min(1.2, len(gate_set) * 0.25), 4),
        "complexity_penalty": round(-complexity_penalty, 4),
        "unsupported_transform_penalty": round(-unsupported_penalty, 4),
    }
    score = round(sum(components.values()), 4)

    row = pool.setdefault(
        canonical,
        {
            "canonical": canonical,
            "vtrac_index": index,
            "score": score,
            "score_components": components,
            "straight_equivalent_cost": straight_equivalent_cost(canonical),
            "parent_anchors": set(),
            "transform_types": set(),
            "translation_lineages": set(),
            "tags": set(),
            "ordered_hints": set(),
            "is_derived": transform_type != "identity_anchor",
        },
    )
    if score > float(row.get("score") or 0.0):
        row["score"] = score
        row["score_components"] = components
    row["parent_anchors"].add(parent_canonical)
    row["transform_types"].add(transform_type)
    row["translation_lineages"].update(gate_set)
    row["tags"].update(str(value) for value in tags if str(value))
    row["is_derived"] = bool(row.get("is_derived")) or transform_type != "identity_anchor"
    if isinstance(direct, Mapping):
        row["ordered_hints"].update(str(value) for value in (direct.get("ordered_hints") or []))


def _transform_gate_lineages(
    *,
    parent: Mapping[str, Any],
    candidate: str,
    context: Mapping[str, Any],
) -> Set[str]:
    parent_canonical = canonicalize(parent.get("canonical"))
    candidate = canonicalize(candidate)
    index = get_vtrac_index(candidate)
    gates: Set[str] = set()
    if index in (context.get("due_double_indices") or set()):
        gates.add(f"due_double_index:{index}")
    if parent_canonical in (context.get("due_double_canonicals") or set()):
        gates.add(f"due_double_parent:{parent_canonical}")
    if candidate in (context.get("due_double_canonicals") or set()):
        gates.add(f"due_double_candidate:{candidate}")
    if parent_canonical in (context.get("mirror_echo_canonicals") or set()):
        gates.add(f"mirror_echo_parent:{parent_canonical}")
    if candidate in (context.get("mirror_echo_canonicals") or set()):
        gates.add(f"mirror_echo_candidate:{candidate}")
    if parent_canonical in (context.get("double_pressure_canonicals") or set()):
        gates.add(f"double_pressure_parent:{parent_canonical}")
    if candidate in (context.get("double_pressure_canonicals") or set()):
        gates.add(f"double_pressure_candidate:{candidate}")
    return gates


def _candidate_is_directly_supported(
    canonical: str,
    anchor_lookup: Mapping[str, Mapping[str, Any]],
) -> bool:
    row = anchor_lookup.get(canonicalize(canonical))
    return isinstance(row, Mapping) and float(row.get("score") or 0.0) >= 2.0


def _build_double_closures(
    pool: MutableMapping[str, Dict[str, Any]],
    *,
    parent: Mapping[str, Any],
    context: Mapping[str, Any],
    anchor_lookup: Mapping[str, Mapping[str, Any]],
) -> None:
    parent_canonical = canonicalize(parent.get("canonical"))
    parts = _double_parts(parent_canonical)
    if parts is None:
        return
    repeated, key = parts
    repeated_mirror = mirror_digit(repeated)
    key_mirror = mirror_digit(key)
    index = parent.get("vtrac_index")

    transforms = [
        (
            canonicalize(f"{repeated}{repeated_mirror}{key}"),
            "double_anchor_one_mirror",
            2.2,
            1,
            key,
        ),
        (
            canonicalize(f"{repeated_mirror}{repeated_mirror}{key}"),
            "double_anchor_full_pair_mirror",
            0.9,
            2,
            key,
        ),
        (
            canonicalize(f"{repeated}{repeated}{key_mirror}"),
            "double_anchor_key_mirror",
            1.2,
            1,
            key_mirror,
        ),
        (
            canonicalize(f"{repeated}{repeated_mirror}{key_mirror}"),
            "double_anchor_one_mirror_plus_key_mirror",
            0.9,
            2,
            key_mirror,
        ),
        (
            canonicalize(f"{repeated_mirror}{repeated_mirror}{key_mirror}"),
            "double_anchor_full_mirror",
            0.6,
            3,
            key_mirror,
        ),
    ]
    for candidate, transform_type, prior, distance, candidate_key in transforms:
        if not candidate or get_vtrac_index(candidate) != index:
            continue
        gates = _transform_gate_lineages(parent=parent, candidate=candidate, context=context)
        if transform_type == "double_anchor_one_mirror":
            allowed = bool(gates) or _candidate_is_directly_supported(candidate, anchor_lookup)
        elif transform_type in {"double_anchor_key_mirror", "double_anchor_full_pair_mirror"}:
            allowed = len(gates) >= 2 or _candidate_is_directly_supported(candidate, anchor_lookup)
        else:
            allowed = len(gates) >= 2 and (
                _candidate_is_directly_supported(candidate, anchor_lookup)
                or candidate in (context.get("due_double_canonicals") or set())
            )
        if not allowed:
            continue
        _add_closure_candidate(
            pool,
            canonical=candidate,
            parent=parent,
            transform_type=transform_type,
            transform_prior=prior,
            gate_lineages=gates,
            tags=[
                f"parent:{parent_canonical}",
                f"mirror_pair:{'/'.join(sorted({repeated, repeated_mirror}))}",
                f"key_digit:{candidate_key}",
                "same_vtrac_index",
            ],
            context=context,
            anchor_lookup=anchor_lookup,
            key_digit=candidate_key,
            transform_distance=distance,
        )


def _build_unique_anchor_closures(
    pool: MutableMapping[str, Dict[str, Any]],
    *,
    parent: Mapping[str, Any],
    context: Mapping[str, Any],
    anchor_lookup: Mapping[str, Mapping[str, Any]],
) -> None:
    parent_canonical = canonicalize(parent.get("canonical"))
    if len(set(parent_canonical)) != 3:
        return
    parent_index = parent.get("vtrac_index")
    for digit in sorted(set(parent_canonical)):
        transformed_digits = list(parent_canonical)
        transformed_digits[transformed_digits.index(digit)] = mirror_digit(digit)
        candidate = canonicalize("".join(transformed_digits))
        if not candidate or get_vtrac_index(candidate) != parent_index:
            continue
        gates = _transform_gate_lineages(parent=parent, candidate=candidate, context=context)
        digit_row = (context.get("digit_support") or {}).get(mirror_digit(digit), {})
        if isinstance(digit_row, Mapping):
            gates.update(str(value) for value in (digit_row.get("lineages") or set()))
        if len(gates) < 2 and not _candidate_is_directly_supported(candidate, anchor_lookup):
            continue
        _add_closure_candidate(
            pool,
            canonical=candidate,
            parent=parent,
            transform_type="single_key_mirror",
            transform_prior=0.8,
            gate_lineages=gates,
            tags=[
                f"parent:{parent_canonical}",
                f"mirrored_digit:{digit}->{mirror_digit(digit)}",
                "same_vtrac_index",
            ],
            context=context,
            anchor_lookup=anchor_lookup,
            key_digit=mirror_digit(digit),
            transform_distance=1,
        )


def _build_pair_key_recombinations(
    pool: MutableMapping[str, Dict[str, Any]],
    *,
    parents: Sequence[Mapping[str, Any]],
    context: Mapping[str, Any],
    anchor_lookup: Mapping[str, Mapping[str, Any]],
) -> None:
    pair_parents: Dict[str, Mapping[str, Any]] = {}
    for parent in parents:
        parts = _double_parts(canonicalize(parent.get("canonical")))
        if parts is None:
            continue
        repeated, _key = parts
        pair = "/".join(sorted({repeated, mirror_digit(repeated)}))
        existing = pair_parents.get(pair)
        if existing is None or float(parent.get("score") or 0.0) > float(existing.get("score") or 0.0):
            pair_parents[pair] = parent

    digit_support = context.get("digit_support") or {}
    ranked_digits = sorted(
        (
            (
                str(digit),
                float(values.get("score") or 0.0),
                set(values.get("lineages") or set()),
            )
            for digit, values in digit_support.items()
            if isinstance(values, Mapping) and str(digit) in MIRROR_DIGIT_MAP
        ),
        key=lambda row: (-row[1], row[0]),
    )
    active_pairs = sorted(
        pair_parents.items(),
        key=lambda item: (-float(item[1].get("score") or 0.0), item[0]),
    )[:2]
    for pair, parent in active_pairs:
        left, right = pair.split("/")
        emitted = 0
        parent_parts = _double_parts(canonicalize(parent.get("canonical")))
        parent_key = parent_parts[1] if parent_parts else ""
        for digit, digit_score, lineages in ranked_digits:
            if emitted >= 2:
                break
            if digit in {left, right, parent_key, mirror_digit(parent_key)}:
                continue
            if digit_score < 0.8 or len(lineages) < 2:
                continue
            candidate = canonicalize(f"{left}{right}{digit}")
            index = get_vtrac_index(candidate)
            if index is None:
                continue
            if (
                index not in (context.get("watchlist_indices") or set())
                and index not in (context.get("vtrac_rank") or {})
                and not _candidate_is_directly_supported(candidate, anchor_lookup)
            ):
                continue
            gates = set(str(value) for value in lineages)
            gates.add(f"pair_family:{pair}")
            _add_closure_candidate(
                pool,
                canonical=candidate,
                parent=parent,
                transform_type="pair_key_recombination",
                transform_prior=1.1,
                gate_lineages=gates,
                tags=[
                    f"parent:{canonicalize(parent.get('canonical'))}",
                    f"mirror_pair:{pair}",
                    f"lingering_key_digit:{digit}",
                ],
                context=context,
                anchor_lookup=anchor_lookup,
                key_digit=digit,
                transform_distance=2,
            )
            emitted += 1


def _serialize_closure_candidate(row: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "canonical": canonicalize(row.get("canonical")),
        "vtrac_index": row.get("vtrac_index"),
        "score": round(float(row.get("score") or 0.0), 4),
        "score_components": dict(row.get("score_components") or {}),
        "straight_equivalent_cost": int(row.get("straight_equivalent_cost") or 0),
        "parent_anchors": sorted(str(value) for value in (row.get("parent_anchors") or [])),
        "transform_types": sorted(str(value) for value in (row.get("transform_types") or [])),
        "translation_lineages": sorted(str(value) for value in (row.get("translation_lineages") or [])),
        "tags": sorted(str(value) for value in (row.get("tags") or [])),
        "ordered_hints": sorted(str(value) for value in (row.get("ordered_hints") or [])),
        "is_derived": bool(row.get("is_derived")),
    }


def build_closure_slate(
    *,
    anchor_slate: Mapping[str, Any],
    anchor_path: Optional[Path] = None,
    repo_root: Optional[Path] = None,
) -> Dict[str, Any]:
    if str(anchor_slate.get("artifact_type") or "") != ANCHOR_ARTIFACT_TYPE:
        raise ValueError("Closure slate requires a structural_convergence_anchor_slate input")
    ranked_anchors = [
        dict(row)
        for row in (anchor_slate.get("ranked_candidates") or [])
        if isinstance(row, Mapping) and canonicalize(row.get("canonical"))
    ]
    anchor_lookup = {canonicalize(row.get("canonical")): row for row in ranked_anchors}
    context = _deserialize_anchor_context(anchor_slate)
    parent_anchors = [
        dict(row)
        for row in (
            ((anchor_slate.get("tiers") or {}).get("EXTENDED6") or {}).get("candidates") or []
        )
        if isinstance(row, Mapping)
    ]
    parent_anchors = parent_anchors[:6]
    if not parent_anchors:
        parent_anchors = ranked_anchors[:6]

    pool: Dict[str, Dict[str, Any]] = {}
    for parent in parent_anchors:
        parent_canonical = canonicalize(parent.get("canonical"))
        _add_closure_candidate(
            pool,
            canonical=parent_canonical,
            parent=parent,
            transform_type="identity_anchor",
            transform_prior=2.4,
            gate_lineages=[f"anchor:{parent_canonical}"],
            tags=[f"parent:{parent_canonical}", "direct_anchor_preserved"],
            context=context,
            anchor_lookup=anchor_lookup,
            transform_distance=0,
        )
        _build_double_closures(
            pool,
            parent=parent,
            context=context,
            anchor_lookup=anchor_lookup,
        )
        _build_unique_anchor_closures(
            pool,
            parent=parent,
            context=context,
            anchor_lookup=anchor_lookup,
        )
    _build_pair_key_recombinations(
        pool,
        parents=parent_anchors,
        context=context,
        anchor_lookup=anchor_lookup,
    )

    ranked = [_serialize_closure_candidate(row) for row in pool.values()]
    ranked.sort(key=lambda row: (-float(row.get("score") or 0.0), str(row.get("canonical") or "")))
    for rank, row in enumerate(ranked, start=1):
        row["rank"] = rank

    core, extended = select_nested_tiers(
        ranked,
        core_width=3,
        extended_width=6,
        minimum_score=2.0,
        core_index_cap=3,
        extended_index_cap=4,
        require_derived_in_core=True,
    )
    anchor_metadata = anchor_slate.get("metadata") if isinstance(anchor_slate.get("metadata"), Mapping) else {}
    return {
        "schema_version": SCHEMA_VERSION,
        "artifact_type": CLOSURE_ARTIFACT_TYPE,
        "status": EXPERIMENTAL_STATUS,
        "metadata": {
            **dict(anchor_metadata),
            "generated_at": now_iso(),
            "source_anchor_artifact_type": ANCHOR_ARTIFACT_TYPE,
        },
        "evidence_safety": dict(anchor_slate.get("evidence_safety") or {}),
        "source_artifacts": [
            input_receipt(anchor_path, "structural_convergence_anchor_slate", repo_root),
        ],
        "translation_contract": {
            "parent_anchor_limit": 6,
            "active_pair_family_limit": 2,
            "pair_key_additions_per_family": 2,
            "core_width": 3,
            "extended_width": 6,
            "core_vtrac_index_cap": 3,
            "extended_vtrac_index_cap": 4,
            "minimum_score": 2.0,
            "full_mirror_requires_independent_support": True,
            "free_form_digit_recombination": False,
            "static_scoreboard_rank_used": False,
            "ordered_permutations_funded": False,
        },
        "parent_anchors": [
            {
                "canonical": canonicalize(row.get("canonical")),
                "score": float(row.get("score") or 0.0),
                "vtrac_index": row.get("vtrac_index"),
            }
            for row in parent_anchors
        ],
        "ranked_candidates": ranked,
        "tiers": {
            "CORE3": tier_receipt(core, 3),
            "EXTENDED6": tier_receipt(extended, 6),
        },
    }


def render_slate_markdown(payload: Mapping[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), Mapping) else {}
    safety = payload.get("evidence_safety") if isinstance(payload.get("evidence_safety"), Mapping) else {}
    artifact_type = str(payload.get("artifact_type") or "compact_candidate_slate")
    title = (
        "Structural Convergence Anchor Slate"
        if artifact_type == ANCHOR_ARTIFACT_TYPE
        else "Bounded VTRAC Closure Slate"
    )
    lines: List[str] = [
        f"# {title}",
        "",
        f"- Status: `{payload.get('status')}`",
        f"- State: `{metadata.get('state_key') or '-'}`",
        f"- Results date: `{metadata.get('results_date') or '-'}`",
        f"- Target period: `{metadata.get('target_period') or '-'}`",
        f"- Timing status: `{safety.get('timing_status') or '-'}`",
        f"- Winner-free input: `{safety.get('winner_free_input')}`",
        "",
        "> Experimental shadow surface. It is not a selected, funded, or realized prediction without a separate frozen receipt.",
        "",
        "## Compact Tiers",
        "",
    ]
    tiers = payload.get("tiers") if isinstance(payload.get("tiers"), Mapping) else {}
    for tier_name in ("CORE3", "EXTENDED6"):
        tier = tiers.get(tier_name) if isinstance(tiers.get(tier_name), Mapping) else {}
        lines.extend(
            [
                f"### {tier_name}",
                "",
                f"- Boxed count: `{tier.get('boxed_count') or 0}`",
                f"- Unused slots: `{tier.get('unused_slots') or 0}`",
                f"- Straight-equivalent lines: `{tier.get('straight_equivalent_lines') or 0}`",
                f"- Canonicals: `{', '.join(tier.get('boxed_canonicals') or []) or '-'}`",
                "",
                "| Rank | Canonical | Score | VTRAC | Cost | Origin |",
                "|---:|---|---:|---:|---:|---|",
            ]
        )
        for row in tier.get("candidates") or []:
            if not isinstance(row, Mapping):
                continue
            origin = ",".join(row.get("transform_types") or row.get("roles") or []) or "-"
            lines.append(
                f"| {row.get('rank') or '-'} | `{row.get('canonical')}` | "
                f"{float(row.get('score') or 0.0):.4f} | "
                f"{row.get('vtrac_index') if row.get('vtrac_index') is not None else '-'} | "
                f"{row.get('straight_equivalent_cost') or 0} | {origin} |"
            )
        lines.append("")

    lines.extend(["## Ranked Candidate Detail", ""])
    for row in (payload.get("ranked_candidates") or [])[:12]:
        if not isinstance(row, Mapping):
            continue
        lines.append(
            f"### {row.get('rank')}. `{row.get('canonical')}` "
            f"(score={float(row.get('score') or 0.0):.4f}, VTRAC={row.get('vtrac_index')})"
        )
        if row.get("transform_types"):
            lines.append(f"- Transforms: `{', '.join(row.get('transform_types') or [])}`")
            lines.append(f"- Parents: `{', '.join(row.get('parent_anchors') or []) or '-'}`")
        else:
            lines.append(f"- Roles: `{', '.join(row.get('roles') or []) or '-'}`")
            lines.append(f"- Source families: `{', '.join(row.get('source_families') or []) or '-'}`")
        lines.append(f"- Variants: `{', '.join(row.get('variants') or []) or '-'}`")
        lines.append(f"- Ordered hints: `{', '.join(row.get('ordered_hints') or []) or '-'}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_slate_files(json_path: Path, payload: Mapping[str, Any]) -> Tuple[Path, Path]:
    write_json(json_path, payload)
    markdown_path = json_path.with_suffix(".md")
    markdown_path.write_text(render_slate_markdown(payload), encoding="utf-8")
    return json_path, markdown_path


def discover_related_artifacts(candidate_path: Path) -> Tuple[Optional[Path], Optional[Path]]:
    state_dir = candidate_path.parent
    suffix = candidate_path.name.removeprefix("candidate_universe").removesuffix(".json")
    arena = state_dir / "analysis" / f"aggregated_analysis_arena{suffix}.json"
    sandbox = state_dir / "analysis" / f"translation_sandbox_seed{suffix}.json"
    return (arena if arena.exists() else None, sandbox if sandbox.exists() else None)


def default_anchor_output_path(candidate_path: Path) -> Path:
    suffix = candidate_path.name.removeprefix("candidate_universe").removesuffix(".json")
    return candidate_path.parent / "analysis" / f"structural_convergence_anchor_slate{suffix}.json"


def default_closure_output_path(anchor_path: Path) -> Path:
    suffix = anchor_path.name.removeprefix("structural_convergence_anchor_slate").removesuffix(".json")
    return anchor_path.parent / f"bounded_vtrac_closure_slate{suffix}.json"


__all__ = [
    "ANCHOR_ARTIFACT_TYPE",
    "CLOSURE_ARTIFACT_TYPE",
    "EXPERIMENTAL_STATUS",
    "MIRROR_DIGIT_MAP",
    "SCHEMA_VERSION",
    "assess_input_safety",
    "boxed_members_for_index",
    "build_anchor_slate",
    "build_closure_slate",
    "canonicalize",
    "default_anchor_output_path",
    "default_closure_output_path",
    "discover_related_artifacts",
    "mirror_digit",
    "normalize_pick3",
    "read_json",
    "render_slate_markdown",
    "select_nested_tiers",
    "straight_equivalent_cost",
    "tier_receipt",
    "validate_artifact_alignment",
    "write_json",
    "write_slate_files",
]
