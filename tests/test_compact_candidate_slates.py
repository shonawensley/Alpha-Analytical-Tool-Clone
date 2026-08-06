import pytest

from modules.vtrac_reference import get_vtrac_index
from scripts.tools.compact_candidate_slates import (
    ANCHOR_ARTIFACT_TYPE,
    CLOSURE_ARTIFACT_TYPE,
    assess_input_safety,
    build_anchor_slate,
    build_closure_slate,
    canonicalize,
    straight_equivalent_cost,
)
from scripts.tools.grade_compact_candidate_slates import grade_slates


def _candidate_universe():
    return {
        "schema_version": "1.0",
        "state_key": "Demo4",
        "results_date": "2026-07-25",
        "history_date": "2026-07-24",
        "profile": "tool_only",
        "contains_winners_artifacts": False,
        "leakage_issues": [],
        "packs": [
            {
                "method_id": "stable_top",
                "pack_id": "stable:Combined:one",
                "variant": "Combined",
                "play_mode": "STRAIGHT",
                "combos": ["664", "115", "226"],
                "canonicals": ["466", "115", "226"],
                "why_tags": ["frontier"],
            },
            {
                "method_id": "stable_top",
                "pack_id": "stable:Combined:duplicate-rendering",
                "variant": "Combined",
                "play_mode": "STRAIGHT",
                "combos": ["664"],
                "canonicals": ["466"],
                "why_tags": ["same-underlying-family"],
            },
            {
                "method_id": "aux_positional",
                "pack_id": "aux:Evening",
                "variant": "Evening",
                "play_mode": "STRAIGHT",
                "combos": ["614", "165", "276"],
                "canonicals": ["146", "156", "267"],
                "why_tags": ["Mirror-Echo", "Double-Pressure"],
            },
            {
                "method_id": "due_doubles",
                "pack_id": "due:Combined",
                "variant": "Combined",
                "play_mode": "BOX",
                "combos": ["664", "115", "226"],
                "canonicals": ["466", "115", "226"],
                "why_tags": ["due_double"],
            },
        ],
        "digit_envelopes": [
            {
                "digits": ["1", "2", "4", "6", "7"],
                "derived_triads": ["124", "146", "267"],
            }
        ],
    }


def _arena():
    return {
        "metadata": {
            "state_key": "Demo4",
            "results_date": "2026-07-25",
            "contains_winners_artifacts": False,
        },
        "arena_synthesis": {
            "dominant_canonicals": [
                {
                    "value": "466",
                    "support_count": 4,
                    "string_source_count": 3,
                    "context_source_count": 1,
                    "example_literals": ["664"],
                    "sources": [
                        {"source": "stable:Combined:compound", "score": 100},
                        {"source": "dr:Evening:candidate", "score": 20},
                        {"source": "aux:positional", "score": 10},
                    ],
                },
                {
                    "value": "115",
                    "support_count": 3,
                    "string_source_count": 2,
                    "context_source_count": 1,
                    "example_literals": ["115"],
                    "sources": [
                        {"source": "stable:Midday:compound", "score": 80},
                        {"source": "vtrac:straight", "score": 15},
                    ],
                },
                {
                    "value": "226",
                    "support_count": 3,
                    "string_source_count": 2,
                    "context_source_count": 1,
                    "example_literals": ["226"],
                    "sources": [
                        {"source": "stable:Evening:compound", "score": 70},
                        {"source": "hot:top_lane", "score": 12},
                    ],
                },
            ],
            "context_reinforced_canonicals": [],
            "stable_survivor_context": {
                "frontier_examples": [
                    {
                        "section": "Combined",
                        "set": "Set1",
                        "draw": "Draw1",
                        "frontier_column": 1,
                        "progression_column_count": 7,
                        "exact3digit_patterns": ["664", "115"],
                    },
                    {
                        "section": "Evening",
                        "set": "Set1",
                        "draw": "Draw1",
                        "frontier_column": 2,
                        "progression_column_count": 6,
                        "exact3digit_patterns": ["664", "226"],
                    },
                ]
            },
            "vtrac_literal_watchlist": [
                {
                    "vtrac_index": "19",
                    "rank": 1,
                    "support_count": 5,
                    "candidate_canonicals": ["466", "146"],
                },
                {
                    "vtrac_index": "6",
                    "rank": 2,
                    "support_count": 4,
                    "candidate_canonicals": ["115", "156"],
                },
                {
                    "vtrac_index": "20",
                    "rank": 3,
                    "support_count": 4,
                    "candidate_canonicals": ["226", "267"],
                },
            ],
        },
        "cross_tool_relations": {"canonical_consensus_top": []},
    }


def _sandbox():
    return {
        "schema_version": "translation_sandbox_seed_v1",
        "metadata": {
            "state_key": "Demo4",
            "results_date": "2026-07-25",
        },
        "brain1_core": {
            "dominant_canonicals": ["466", "115", "226"],
            "secondary_canonicals": ["146", "156", "267"],
            "context_reinforced_canonicals": [],
            "survivor_frontier_canonicals": ["466", "115", "226"],
            "survivor_last_remaining_canonicals": [],
            "dominant_vtrac_indices": ["19", "6", "20"],
            "watchlist_indices": ["19", "6", "20"],
            "r_consensus_context": {},
        },
        "brain2_context": {
            "due_double_example_canonicals": [
                "466",
                "114",
                "115",
                "665",
                "226",
                "776",
            ],
            "profit_alert_implied_canonicals": [],
            "blackapple_recommended_canonicals": [],
            "top_profit_alerts": [],
            "positional_shortlist_top": [
                {
                    "canonical": "146",
                    "combo": "614",
                    "score": 40,
                    "tags": ["Mirror-Echo", "Double-Pressure"],
                },
                {
                    "canonical": "156",
                    "combo": "165",
                    "score": 35,
                    "tags": ["Mirror-Echo"],
                },
                {
                    "canonical": "267",
                    "combo": "276",
                    "score": 30,
                    "tags": ["Mirror-Echo"],
                },
            ],
            "positional_signal_notes": ["Fixture mirror support"],
        },
    }


def test_pick3_and_cost_semantics():
    assert canonicalize("091") == "019"
    assert straight_equivalent_cost("019") == 6
    assert straight_equivalent_cost("115") == 3
    assert straight_equivalent_cost("777") == 1


def test_shadow_mode_rejects_winner_dependent_candidate_universe(tmp_path):
    payload = _candidate_universe()
    payload["contains_winners_artifacts"] = True
    with pytest.raises(ValueError, match="rejected winner-dependent input"):
        assess_input_safety(
            candidate_universe=payload,
            aggregated_arena=None,
            translation_sandbox=None,
            candidate_path=tmp_path / "candidate_universe.json",
            run_mode="shadow",
        )


def test_shadow_mode_requires_predictive_root_or_freeze_receipt(tmp_path):
    candidate_path = tmp_path / "replay" / "candidate_universe.json"
    with pytest.raises(ValueError, match="requires supplied inputs under a _predictive root"):
        assess_input_safety(
            candidate_universe=_candidate_universe(),
            aggregated_arena=None,
            translation_sandbox=None,
            candidate_path=candidate_path,
            run_mode="shadow",
        )

    receipt = assess_input_safety(
        candidate_universe=_candidate_universe(),
        aggregated_arena=None,
        translation_sandbox=None,
        candidate_path=candidate_path,
        run_mode="shadow",
        freeze_receipt="freeze-demo-001",
    )
    assert receipt["timing_status"] == "EXPLICIT_FREEZE_RECEIPT"
    assert receipt["non_predictive_input_paths"] == [str(candidate_path)]


def test_shadow_mode_rejects_winner_side_path_even_with_freeze_receipt(tmp_path):
    with pytest.raises(ValueError, match="rejected winner-side input path"):
        assess_input_safety(
            candidate_universe=_candidate_universe(),
            aggregated_arena=None,
            translation_sandbox=None,
            candidate_path=tmp_path / "winners" / "candidate_universe.json",
            run_mode="shadow",
            freeze_receipt="freeze-demo-001",
        )


def test_anchor_slate_rejects_cross_state_artifact_mix():
    arena = _arena()
    arena["metadata"]["state_key"] = "WrongState4"
    with pytest.raises(ValueError, match="Artifact alignment failed"):
        build_anchor_slate(
            candidate_universe=_candidate_universe(),
            aggregated_arena=arena,
            translation_sandbox=_sandbox(),
        )


def test_anchor_slate_is_nested_and_deduplicates_pack_lineages():
    slate = build_anchor_slate(
        candidate_universe=_candidate_universe(),
        aggregated_arena=_arena(),
        translation_sandbox=_sandbox(),
        target_period="Evening",
    )

    assert slate["artifact_type"] == ANCHOR_ARTIFACT_TYPE
    core = slate["tiers"]["CORE3"]["boxed_canonicals"]
    extended = slate["tiers"]["EXTENDED6"]["boxed_canonicals"]
    assert set(core).issubset(extended)
    assert len(core) <= 3
    assert len(extended) <= 6
    assert slate["scoring_contract"]["static_scoreboard_rank_used"] is False

    candidate = next(row for row in slate["ranked_candidates"] if row["canonical"] == "466")
    stable_cu_lineages = [
        row
        for row in candidate["lineages"]
        if row["source_family"] == "stable"
        and row["variant"] == "Combined"
        and row["role"] == "candidate_universe"
    ]
    assert len(stable_cu_lineages) == 1
    assert len(stable_cu_lineages[0]["source_ids"]) == 2


def test_candidate_ranking_is_deterministic_across_repeated_builds():
    kwargs = {
        "candidate_universe": _candidate_universe(),
        "aggregated_arena": _arena(),
        "translation_sandbox": _sandbox(),
        "target_period": "Evening",
    }
    first_anchor = build_anchor_slate(**kwargs)
    second_anchor = build_anchor_slate(**kwargs)
    assert first_anchor["ranked_candidates"] == second_anchor["ranked_candidates"]
    assert first_anchor["tiers"] == second_anchor["tiers"]

    first_closure = build_closure_slate(anchor_slate=first_anchor)
    second_closure = build_closure_slate(anchor_slate=second_anchor)
    assert first_closure["ranked_candidates"] == second_closure["ranked_candidates"]
    assert first_closure["tiers"] == second_closure["tiers"]


def test_closure_slate_builds_verified_same_index_mirror_transforms():
    anchor = build_anchor_slate(
        candidate_universe=_candidate_universe(),
        aggregated_arena=_arena(),
        translation_sandbox=_sandbox(),
    )
    closure = build_closure_slate(anchor_slate=anchor)
    by_canonical = {row["canonical"]: row for row in closure["ranked_candidates"]}

    assert closure["artifact_type"] == CLOSURE_ARTIFACT_TYPE
    assert "146" in by_canonical
    assert "156" in by_canonical
    assert "267" in by_canonical
    assert "double_anchor_one_mirror" in by_canonical["146"]["transform_types"]
    assert "double_anchor_one_mirror" in by_canonical["156"]["transform_types"]
    assert "double_anchor_one_mirror" in by_canonical["267"]["transform_types"]
    assert get_vtrac_index("664") == get_vtrac_index("614") == 19
    assert get_vtrac_index("115") == get_vtrac_index("165") == 6
    assert get_vtrac_index("226") == get_vtrac_index("276") == 20

    # 624 was discussed as a possible mirror example, but it is a different index.
    assert get_vtrac_index("624") == 22
    assert get_vtrac_index("624") != get_vtrac_index("664")

    core = closure["tiers"]["CORE3"]["boxed_canonicals"]
    extended = closure["tiers"]["EXTENDED6"]["boxed_canonicals"]
    assert set(core).issubset(extended)
    assert any(row["is_derived"] for row in closure["tiers"]["CORE3"]["candidates"])
    pair_key_rows = [
        row
        for row in closure["ranked_candidates"]
        if "pair_key_recombination" in row["transform_types"]
    ]
    pair_families = {
        tag
        for row in pair_key_rows
        for tag in row["tags"]
        if tag.startswith("mirror_pair:")
    }
    assert len(pair_families) <= 2


def test_grader_separates_canonical_hit_from_vtrac_only_and_ordered_hint():
    anchor = {
        "artifact_type": ANCHOR_ARTIFACT_TYPE,
        "status": "EXPERIMENTAL_SHADOW",
        "metadata": {"state_key": "Demo4", "results_date": "2026-07-25"},
        "tiers": {
            "CORE3": {
                "width_cap": 3,
                "boxed_count": 1,
                "straight_equivalent_lines": 6,
                "candidates": [
                    {
                        "canonical": "014",
                        "vtrac_index": 9,
                        "ordered_hints": ["041"],
                        "is_derived": False,
                    }
                ],
            },
            "EXTENDED6": {
                "width_cap": 6,
                "boxed_count": 1,
                "straight_equivalent_lines": 6,
                "candidates": [
                    {
                        "canonical": "014",
                        "vtrac_index": 9,
                        "ordered_hints": ["041"],
                        "is_derived": False,
                    }
                ],
            },
        },
    }
    closure = {
        "artifact_type": CLOSURE_ARTIFACT_TYPE,
        "status": "EXPERIMENTAL_SHADOW",
        "metadata": {"state_key": "Demo4", "results_date": "2026-07-25"},
        "tiers": {
            "CORE3": {
                "width_cap": 3,
                "boxed_count": 1,
                "straight_equivalent_lines": 6,
                "candidates": [
                    {
                        "canonical": "019",
                        "vtrac_index": 9,
                        "ordered_hints": ["091"],
                        "is_derived": True,
                        "transform_types": ["pair_key_recombination"],
                    }
                ],
            },
            "EXTENDED6": {
                "width_cap": 6,
                "boxed_count": 1,
                "straight_equivalent_lines": 6,
                "candidates": [
                    {
                        "canonical": "019",
                        "vtrac_index": 9,
                        "ordered_hints": ["091"],
                        "is_derived": True,
                        "transform_types": ["pair_key_recombination"],
                    }
                ],
            },
        },
    }

    grade = grade_slates(slates=[anchor, closure], winner="091", period="Evening")
    anchor_grade = grade["slate_grades"][0]["tier_grades"]["CORE3"]
    closure_grade = grade["slate_grades"][1]["tier_grades"]["CORE3"]

    assert anchor_grade["match_class"] == "VTRAC_ONLY"
    assert anchor_grade["canonical_hit"] is False
    assert closure_grade["match_class"] == "CANONICAL_BOX"
    assert closure_grade["ordered_hint_match"] is True
    assert closure_grade["derived_canonical_match"] is True
    assert grade["joint_diagnosis"]["CORE3"] == "CLOSURE_ONLY_CANONICAL"
