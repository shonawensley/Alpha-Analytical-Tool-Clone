#!/usr/bin/env python3
"""Shared Brain 2 rank-integrity contract and governance receipts.

The current board priority formula is dominated by caller-supplied state
order.  Phase 2 keeps that legacy receipt readable while making the absence
of a validated analytical state rank explicit and machine-enforceable.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple


RANK_CONTRACT_SCHEMA = "brain2_rank_contract_v1"
RANK_INTEGRITY_INVALID_STATIC_ORDER = "INVALID_STATIC_ORDER"
RANK_EVALUATION_NOT_EVALUABLE = "NOT_EVALUABLE"
LEGACY_BOARD_RANK_SOURCE = "state_order_dominated_legacy_formula"
RANK_EXCLUSION_INVALID_STATIC_ORDER = "INVALID_STATIC_ORDER"
DISPLAY_ORDER_SOURCE_INPUT_ROSTER = "INPUT_ROSTER_NON_ANALYTICAL"
DISPLAY_ORDER_SOURCE_ALPHABETICAL = "ALPHABETICAL_NON_ANALYTICAL"
DISPLAY_ORDER_SOURCE_UNAVAILABLE = "UNAVAILABLE_NON_ANALYTICAL"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _optional_int(value: object) -> Optional[int]:
    try:
        if value is None or str(value).strip() == "":
            return None
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return None


def _optional_float(value: object) -> Optional[float]:
    try:
        if value is None or str(value).strip() == "":
            return None
        return float(str(value).strip())
    except (TypeError, ValueError):
        return None


def unavailable_rank_contract() -> Dict[str, Any]:
    """Return the canonical contract for the quarantined legacy board rank."""

    return {
        "schema_version": RANK_CONTRACT_SCHEMA,
        "analytical_rank": None,
        "analytical_score": None,
        "analytical_rank_source": None,
        "rank_integrity_status": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        "rank_signal_available": False,
        "rank_signal_valid": False,
        "rank_contribution": 0.0,
        "rank_contribution_mode": "neutral_ignored",
        "rank_exclusion_reason": RANK_EXCLUSION_INVALID_STATIC_ORDER,
    }


def rank_contract_from_row(row: Mapping[str, Any] | None) -> Dict[str, Any]:
    """Read a valid analytical rank or return the unavailable contract.

    Missing fields never fall back to ``score_rank``, ``input_rank``,
    ``priority_score``, or their legacy aliases.
    """

    source = row if isinstance(row, Mapping) else {}
    rank = _optional_int(source.get("analytical_rank"))
    score = _optional_float(source.get("analytical_score"))
    rank_source = str(source.get("analytical_rank_source") or "").strip() or None
    explicitly_valid = source.get("rank_signal_valid") is True
    explicitly_available = source.get("rank_signal_available") is True
    integrity = str(source.get("rank_integrity_status") or "").strip()
    if explicitly_valid and explicitly_available and rank is not None and rank_source:
        return {
            "schema_version": RANK_CONTRACT_SCHEMA,
            "analytical_rank": rank,
            "analytical_score": score,
            "analytical_rank_source": rank_source,
            "rank_integrity_status": integrity or "VALID",
            "rank_signal_available": True,
            "rank_signal_valid": True,
            "rank_contribution": _optional_float(source.get("rank_contribution")) or 0.0,
            "rank_contribution_mode": str(source.get("rank_contribution_mode") or "active"),
            "rank_exclusion_reason": None,
        }
    return unavailable_rank_contract()


def analytical_rank(row: Mapping[str, Any] | None) -> Optional[int]:
    return _optional_int(rank_contract_from_row(row).get("analytical_rank"))


def analytical_score(row: Mapping[str, Any] | None) -> Optional[float]:
    return _optional_float(rank_contract_from_row(row).get("analytical_score"))


def rank_signal_is_valid(row: Mapping[str, Any] | None) -> bool:
    return bool(rank_contract_from_row(row).get("rank_signal_valid"))


def display_order_fields(
    display_order: int,
    *,
    source: str = DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
) -> Dict[str, Any]:
    """Describe deterministic navigation order without implying rank."""

    return {
        "display_order": int(display_order),
        "display_order_source": str(source),
        "display_order_is_analytical": False,
    }


def display_order_contract_from_row(row: Mapping[str, Any] | None) -> Dict[str, Any]:
    """Read or derive navigation order without treating it as rank."""

    source = row if isinstance(row, Mapping) else {}
    order = _optional_int(source.get("display_order"))
    if order is None:
        order = _optional_int(source.get("input_order"))
    if order is None:
        order = _optional_int(source.get("input_rank"))
    if order is None:
        return {
            "display_order": None,
            "display_order_source": DISPLAY_ORDER_SOURCE_UNAVAILABLE,
            "display_order_is_analytical": False,
        }
    order_source = str(source.get("display_order_source") or "").strip()
    return display_order_fields(
        order,
        source=order_source or DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
    )


def legacy_rank_fields(
    *,
    input_order: int,
    legacy_static_rank: int,
    legacy_priority_score: int,
) -> Dict[str, Any]:
    """Build explicit legacy fields plus deprecated compatibility aliases."""

    fields: Dict[str, Any] = {
        "input_order": int(input_order),
        "legacy_static_rank": int(legacy_static_rank),
        "legacy_priority_score": int(legacy_priority_score),
        "legacy_rank_source": LEGACY_BOARD_RANK_SOURCE,
        # Compatibility aliases. Consumers must use the explicit contract.
        "input_rank": int(input_order),
        "score_rank": int(legacy_static_rank),
        "priority_score": int(legacy_priority_score),
        "legacy_fields_deprecated": True,
        "legacy_fields_treatment": "diagnostic_only",
    }
    fields.update(display_order_fields(input_order))
    fields.update(unavailable_rank_contract())
    return fields


def rank_evaluation_status(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    valid = [row for row in rows if rank_signal_is_valid(row)]
    if not valid:
        return {
            "status": RANK_EVALUATION_NOT_EVALUABLE,
            "evaluable": False,
            "valid_ranked_state_count": 0,
            "reason": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        }
    return {
        "status": "EVALUABLE",
        "evaluable": True,
        "valid_ranked_state_count": len(valid),
        "reason": None,
    }


def input_order_key(row: Mapping[str, Any]) -> Tuple[int, str]:
    order = _optional_int(row.get("input_order"))
    if order is None:
        order = _optional_int(row.get("input_rank"))
    return (order if order is not None else 999999, str(row.get("state_key") or ""))


def quarantine_decision(
    decision: Mapping[str, Any] | None,
    scoreboard_row: Mapping[str, Any] | None,
) -> Dict[str, Any]:
    """Prevent a stale rank-derived decision from crossing the sandbox edge."""

    out = dict(decision) if isinstance(decision, Mapping) else {}
    contract = rank_contract_from_row(scoreboard_row)
    out["rank_contract"] = contract
    if contract["rank_signal_valid"]:
        return out

    blockers = [str(value) for value in (out.get("blockers") or []) if str(value)]
    if "RANK_SIGNAL_UNAVAILABLE" not in blockers:
        blockers.append("RANK_SIGNAL_UNAVAILABLE")
    reasons = [str(value) for value in (out.get("reason_codes") or []) if str(value)]
    reasons = [value for value in reasons if value not in {"PLAY_STATE", "WATCH_STATE", "SKIP_STATE"}]
    if "RANK_SIGNAL_UNAVAILABLE" not in reasons:
        reasons.append("RANK_SIGNAL_UNAVAILABLE")
    if "UNRESOLVED_STATE" not in reasons:
        reasons.append("UNRESOLVED_STATE")
    out.update(
        {
            "posture": "UNRESOLVED",
            "cap_class": "unavailable",
            "translator_route": "none",
            "carryover_action": "unresolved",
            "blockers": blockers,
            "reason_codes": reasons,
        }
    )
    return out


def build_rank_source_registry_payload() -> Dict[str, Any]:
    sources = [
        {
            "source_id": "brain2_legacy_board_priority",
            "producer": "scripts/tools/build_board_spillover_overlay.py::_build_board_summary",
            "fields": ["legacy_static_rank", "legacy_priority_score", "score_rank", "priority_score"],
            "formula": "input-order points + spent adjustment + direct-cross adjustment - overlap adjustment",
            "input_provenance": "Arena state summaries, relationship receipts, caller state order, optional Midday outcomes",
            "timing_class": "PRE_MIDDAY_OR_POST_MIDDAY_PRE_EVENING_BY_INVOCATION",
            "scope": "cross_state_board",
            "validity_class": RANK_INTEGRITY_INVALID_STATIC_ORDER,
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["ordering", "top-target labels", "Shadow DPL posture", "caps", "rank reports"],
            "phase2_treatment": "preserve relationship/spent evidence; quarantine rank and score as diagnostic-only",
        },
        {
            "source_id": "predictive_portfolio_arena_first",
            "producer": "scripts/tools/create_predictive_portfolio_report.py::main",
            "fields": ["arena_rank"],
            "formula": "inherits board score_rank, then candidate-union and alert tie-breaks",
            "input_provenance": "Brain 2 scoreboard plus predictive Candidate Universe and Profit Alerts",
            "timing_class": "PRE_RESULT",
            "scope": "cross_state_portfolio",
            "validity_class": "INHERITS_INVALID_STATIC_ORDER",
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["portfolio ordering"],
            "phase2_treatment": "superseded for analytical rank evaluation",
        },
        {
            "source_id": "predictive_portfolio_tool_first",
            "producer": "scripts/tools/create_predictive_portfolio_report.py::main",
            "fields": ["candidate_top_support", "candidate_union", "due_doubles_count", "candidate_packs"],
            "formula": "top support desc, union burden asc, due doubles desc, packs desc, state key",
            "input_provenance": "predictive Candidate Universe, Play Card, and due-double receipts",
            "timing_class": "PRE_RESULT",
            "scope": "cross_state_control_arm",
            "validity_class": "UNVALIDATED_HEURISTIC",
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["portfolio ordering", "portfolio-vs-results evaluation"],
            "phase2_treatment": "retain as named legacy control-arm heuristic; do not promote to Brain 2 analytical rank",
        },
        {
            "source_id": "predictive_portfolio_profit_alerts",
            "producer": "scripts/tools/create_predictive_portfolio_report.py::main",
            "fields": ["alerts_count", "alerts_strength_sum_top", "candidate_union"],
            "formula": "alert count desc, top-alert strength desc, candidate union asc, state key",
            "input_provenance": "predictive Control Center Profit Alerts and Candidate Universe",
            "timing_class": "PRE_RESULT",
            "scope": "cross_state_control_arm",
            "validity_class": "UNVALIDATED_HEURISTIC",
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["portfolio ordering"],
            "phase2_treatment": "retain as named diagnostic heuristic; do not promote to Brain 2 analytical rank",
        },
        {
            "source_id": "portfolio_vs_results_tool_first",
            "producer": "scripts/tools/create_portfolio_vs_results_report.py::_rank_key",
            "fields": ["rank"],
            "formula": "same pre-result tool_first ordering, graded after outcomes are available",
            "input_provenance": "frozen predictive Candidate Universe and Play Card, then winner truth for grading",
            "timing_class": "PRE_RESULT_RANK_POST_RESULT_EVALUATION",
            "scope": "cross_state_evaluation",
            "validity_class": "UNVALIDATED_HEURISTIC_EVALUATION",
            "available_or_displayed": True,
            "historically_influential": False,
            "historical_influence_paths": [],
            "phase2_treatment": "retain as historical control-arm evaluation only",
        },
        {
            "source_id": "superbrain_experimental_rankers",
            "producer": "scripts/tools/superbrain_config_harness.py::_rank_key",
            "fields": ["baseline_tool_first", "pressure_tiebreak"],
            "formula": "Candidate Universe heuristic with optional Aux pressure tie-break",
            "input_provenance": "frozen predictive Candidate Universe, Aux pressure, and Play Card",
            "timing_class": "PRE_RESULT_RANK_POST_RESULT_HARNESS",
            "scope": "cross_state_experiment",
            "validity_class": "EXPERIMENTAL_UNVALIDATED",
            "available_or_displayed": True,
            "historically_influential": False,
            "historical_influence_paths": [],
            "phase2_treatment": "retain as experiment; not a current Brain 2 rank source",
        },
        {
            "source_id": "post_midday_competition_priority",
            "producer": "scripts/tools/build_board_spillover_overlay.py::_build_board_summary",
            "fields": ["legacy_static_rank", "legacy_priority_score"],
            "formula": "legacy board formula after Midday spent-status enrichment",
            "input_provenance": "frozen predictive evidence plus known Midday outcomes",
            "timing_class": "POST_MIDDAY_PRE_EVENING",
            "scope": "period_specific_board",
            "validity_class": "DECISION_TIME_SPECIFIC_LEGACY_PRIORITY",
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["competition rerank", "Evening shadow decision"],
            "phase2_treatment": "keep distinct from pre-Midday rank; quarantine strongest-state claims",
        },
        {
            "source_id": "tool_local_candidate_ranks",
            "producer": "Stable/Digit Reduction/VTRAC/Hot Zones/Arena/Candidate Universe/Play Card producers",
            "fields": ["candidate rank", "canonical rank", "VTRAC rank", "signal rank"],
            "formula": "tool-specific",
            "input_provenance": "within-state predictive tool evidence",
            "timing_class": "PRE_RESULT",
            "scope": "within_state_candidate_or_lane",
            "validity_class": "OUT_OF_SCOPE_NOT_A_STATE_RANK",
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["within-state candidate preservation and control-arm combination forming"],
            "phase2_treatment": "preserve unchanged; never reinterpret as cross-state analytical rank",
        },
        {
            "source_id": "due_doubles_state_order",
            "producer": "scripts/tools/export_control_center_sharepack.py and due-doubles audits",
            "fields": ["draws_since_double rank"],
            "formula": "draws since double desc within period/board",
            "input_provenance": "historical draw cadence",
            "timing_class": "PRE_RESULT",
            "scope": "mechanism_specific_state_context",
            "validity_class": "VALID_MECHANISM_CONTEXT_NOT_GLOBAL_STATE_RANK",
            "available_or_displayed": True,
            "historically_influential": True,
            "historical_influence_paths": ["due-double context and audits"],
            "phase2_treatment": "preserve as mechanism-specific context only",
        },
        {
            "source_id": "post_result_deep_review_priority",
            "producer": "Deep Review templates and truth-aware review reports",
            "fields": ["review priority", "hit rank", "gap priority"],
            "formula": "truth-aware diagnostic ordering",
            "input_provenance": "predictive artifacts plus known outcomes",
            "timing_class": "POST_RESULT",
            "scope": "review_only",
            "validity_class": "VALID_REVIEW_PRIORITY_NOT_PREDICTIVE_RANK",
            "available_or_displayed": True,
            "historically_influential": False,
            "historical_influence_paths": [],
            "phase2_treatment": "preserve but label truth-aware; never use for predictive Capture@K",
        },
    ]
    return {
        "schema_version": "brain2_rank_source_registry_v1",
        "generated_at": _now_iso(),
        "analytical_rank_status": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        "replacement_ranker_introduced": False,
        "sources": sources,
    }


def build_supersession_registry_payload() -> Dict[str, Any]:
    affected = [
        ("board_overlay_strongest_state_order", "board overlay legacy rank/priority ordering"),
        ("compact_scoreboard_top_targets", "top/secondary/best-host labels derived from legacy order"),
        ("shadow_dpl_rank_decisions", "PLAY/WATCH/SKIP, tier, and cap decisions requiring legacy rank"),
        ("translation_sandbox_rank_receipts", "rank-derived posture/order receipts; candidate seeds remain valid"),
        ("brain2_master_rank_claims", "top-ranked-state and Capture@K conclusions"),
        ("window_rank_diagnostics", "top-N board cohorts, rank medians, and rank-performance conclusions"),
        ("predictive_portfolio_arena_first", "portfolio ordering inherited from board score_rank"),
        ("daily_report_board_order", "daily report ordering and top-state language inherited from score_rank"),
    ]
    return {
        "schema_version": "brain2_rank_supersession_registry_v1",
        "generated_at": _now_iso(),
        "supersession_status": "SUPERSEDED",
        "validity_status": "INVALID_FOR_ANALYTICAL_RANK_EVALUATION",
        "legacy_class": "LEGACY_STATIC_ORDER",
        "affected_claim_families": [
            {"claim_id": claim_id, "description": description, "status": "SUPERSEDED"}
            for claim_id, description in affected
        ],
        "preserved_finding_families": [
            "tool hit classification",
            "Arena evidence preservation",
            "candidate burden",
            "origin-ladder evidence",
            "exact/box/VTRAC containment",
            "conversion gaps",
            "spent status",
            "cross-state topology and transfer relationships",
            "tracker hints",
            "rank-independent translation seeds",
        ],
        "bulk_historical_rewrite_performed": False,
    }


def _registry_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Brain 2 Rank Source Registry",
        "",
        f"- Analytical rank status: `{payload.get('analytical_rank_status')}`",
        f"- Replacement ranker introduced: `{payload.get('replacement_ranker_introduced')}`",
        "",
        "| Source | Timing | Scope | Validity | Displayed | Influential | Phase 2 treatment |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in payload.get("sources") or []:
        lines.append(
            f"| `{row.get('source_id')}` | {row.get('timing_class')} | {row.get('scope')} | "
            f"{row.get('validity_class')} | {row.get('available_or_displayed')} | "
            f"{row.get('historically_influential')} | {row.get('phase2_treatment')} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def _supersession_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Brain 2 Rank Supersession Registry",
        "",
        f"- Status: `{payload.get('supersession_status')}`",
        f"- Validity: `{payload.get('validity_status')}`",
        f"- Legacy class: `{payload.get('legacy_class')}`",
        "- Historical files are not bulk rewritten.",
        "",
        "## Superseded Rank Claims",
        "",
    ]
    for row in payload.get("affected_claim_families") or []:
        lines.append(f"- `{row.get('claim_id')}`: {row.get('description')} (`{row.get('status')}`)")
    lines.extend(["", "## Preserved Findings", ""])
    for value in payload.get("preserved_finding_families") or []:
        lines.append(f"- {value}")
    return "\n".join(lines).rstrip() + "\n"


def write_rank_governance_files(out_dir: Path) -> Dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    source_payload = build_rank_source_registry_payload()
    supersession_payload = build_supersession_registry_payload()
    outputs = {
        "source_json": out_dir / "BRAIN2_RANK_SOURCE_REGISTRY.json",
        "source_md": out_dir / "BRAIN2_RANK_SOURCE_REGISTRY.md",
        "supersession_json": out_dir / "BRAIN2_RANK_SUPERSESSION_REGISTRY.json",
        "supersession_md": out_dir / "BRAIN2_RANK_SUPERSESSION_REGISTRY.md",
    }
    outputs["source_json"].write_text(json.dumps(source_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    outputs["source_md"].write_text(_registry_markdown(source_payload), encoding="utf-8")
    outputs["supersession_json"].write_text(
        json.dumps(supersession_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    outputs["supersession_md"].write_text(_supersession_markdown(supersession_payload), encoding="utf-8")
    return {key: str(path) for key, path in outputs.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Write Brain 2 rank source and supersession registries.")
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    outputs = write_rank_governance_files(Path(args.out_dir))
    for label, path in outputs.items():
        print(f"[ok] {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
