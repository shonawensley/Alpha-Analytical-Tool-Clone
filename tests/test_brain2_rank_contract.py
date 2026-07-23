from __future__ import annotations

import json
from pathlib import Path

from scripts.tools.brain2_rank_contract import (
    RANK_INTEGRITY_INVALID_STATIC_ORDER,
    analytical_rank,
    build_rank_source_registry_payload,
    build_supersession_registry_payload,
    legacy_rank_fields,
    quarantine_decision,
    rank_contract_from_row,
    rank_evaluation_status,
    write_rank_governance_files,
)


def test_legacy_aliases_never_become_analytical_rank() -> None:
    row = legacy_rank_fields(input_order=1, legacy_static_rank=1, legacy_priority_score=146)

    assert row["score_rank"] == 1
    assert row["priority_score"] == 146
    assert row["display_order"] == 1
    assert row["display_order_source"] == "INPUT_ROSTER_NON_ANALYTICAL"
    assert row["display_order_is_analytical"] is False
    assert analytical_rank(row) is None
    assert row["analytical_rank"] is None
    assert row["rank_integrity_status"] == RANK_INTEGRITY_INVALID_STATIC_ORDER
    assert row["rank_contribution"] == 0.0
    assert row["rank_contribution_mode"] == "neutral_ignored"
    assert rank_evaluation_status([row])["status"] == "NOT_EVALUABLE"


def test_missing_contract_does_not_fall_back_to_legacy_fields() -> None:
    contract = rank_contract_from_row({"score_rank": 1, "priority_score": 999, "input_rank": 1})
    assert contract["analytical_rank"] is None
    assert contract["rank_signal_valid"] is False


def test_stale_play_decision_is_quarantined_without_removing_evidence() -> None:
    decision = quarantine_decision(
        {"posture": "PLAY", "mode": "boxed", "reason_codes": ["PLAY_STATE", "LAST_REMAINING"]},
        {"score_rank": 1, "priority_score": 999},
    )
    assert decision["posture"] == "UNRESOLVED"
    assert decision["mode"] == "boxed"
    assert decision["cap_class"] == "unavailable"
    assert decision["translator_route"] == "none"
    assert "LAST_REMAINING" in decision["reason_codes"]
    assert "RANK_SIGNAL_UNAVAILABLE" in decision["blockers"]


def test_registry_separates_rank_timings_and_scopes(tmp_path: Path) -> None:
    payload = build_rank_source_registry_payload()
    by_id = {row["source_id"]: row for row in payload["sources"]}

    assert by_id["brain2_legacy_board_priority"]["validity_class"] == RANK_INTEGRITY_INVALID_STATIC_ORDER
    assert by_id["predictive_portfolio_tool_first"]["timing_class"] == "PRE_RESULT"
    assert by_id["post_midday_competition_priority"]["timing_class"] == "POST_MIDDAY_PRE_EVENING"
    assert by_id["tool_local_candidate_ranks"]["scope"] == "within_state_candidate_or_lane"
    assert payload["replacement_ranker_introduced"] is False

    supersession = build_supersession_registry_payload()
    assert supersession["bulk_historical_rewrite_performed"] is False
    assert "exact/box/VTRAC containment" in supersession["preserved_finding_families"]

    outputs = write_rank_governance_files(tmp_path)
    source_payload = json.loads(Path(outputs["source_json"]).read_text(encoding="utf-8"))
    assert source_payload["analytical_rank_status"] == RANK_INTEGRITY_INVALID_STATIC_ORDER
