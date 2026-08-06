from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from scripts.tools.aux_core import (
    BASE_SOURCE_FAMILIES,
    _json_list,
    build_aux_core,
    canonical,
    grade_winner,
    normalize_pick3,
    normalize_playable_pick3,
    render_external_markdown,
    stable_sha256,
)


ROOT = Path(__file__).resolve().parents[1]
DAY_DIR = ROOT / "sharepacks" / "_replay_rpattern_current" / "2026-03-09"
HOLDOUT_DAY_DIR = ROOT / "sharepacks" / "2026-01-20"


@pytest.fixture(scope="module")
def connecticut_payload() -> dict[str, Any]:
    if not DAY_DIR.exists():
        pytest.skip("local March replay fixture is not present")
    return build_aux_core(
        state_key="Connecticut4",
        results_date="2026-03-09",
        day_dir=DAY_DIR,
    )


def test_pick3_identity_helpers_preserve_zeroes() -> None:
    assert normalize_pick3("91") == "091"
    assert canonical("091") == "019"
    assert canonical("900") == "009"


def test_candidate_arrays_reject_vtrac_metadata_labels() -> None:
    assert normalize_playable_pick3("091") == "091"
    assert normalize_playable_pick3("v125") == ""
    assert _json_list('["091", "v125", "019"]') == ["091", "019"]


def test_pre_result_object_is_complete_and_result_free(
    connecticut_payload: dict[str, Any],
) -> None:
    assert connecticut_payload["schema_version"] == "aux_core_v1"
    assert connecticut_payload["metadata"]["source_is_frozen_pre_result"] is True
    assert connecticut_payload["metadata"]["winner_fields_present"] is False
    assert connecticut_payload["validation"]["forbidden_result_key_paths"] == []
    assert [
        block["block_id"]
        for block in connecticut_payload["blocks"].values()
    ] == list(range(1, 11))


def test_frozen_hash_is_reproducible(
    connecticut_payload: dict[str, Any],
) -> None:
    rebuilt = build_aux_core(
        state_key="Connecticut4",
        results_date="2026-03-09",
        day_dir=DAY_DIR,
    )
    assert rebuilt["frozen_object_sha256"] == connecticut_payload[
        "frozen_object_sha256"
    ]
    without_hash = dict(connecticut_payload)
    without_hash.pop("frozen_object_sha256")
    assert stable_sha256(without_hash) == connecticut_payload[
        "frozen_object_sha256"
    ]


def test_frozen_hash_is_reproducible_across_process_hash_seeds(
    connecticut_payload: dict[str, Any],
) -> None:
    code = """
from pathlib import Path
from scripts.tools.aux_core import build_aux_core
payload = build_aux_core(
    state_key="Connecticut4",
    results_date="2026-03-09",
    day_dir=Path("sharepacks/_replay_rpattern_current/2026-03-09"),
)
print(payload["frozen_object_sha256"])
"""
    hashes = []
    for seed in ("1", "2"):
        env = dict(os.environ)
        env["PYTHONHASHSEED"] = seed
        hashes.append(
            subprocess.check_output(
                [sys.executable, "-c", code],
                cwd=ROOT,
                env=env,
                text=True,
            ).strip()
        )
    assert hashes == [
        connecticut_payload["frozen_object_sha256"],
        connecticut_payload["frozen_object_sha256"],
    ]


def test_classic_due_doubles_table_2_reuses_validated_authority(
    connecticut_payload: dict[str, Any],
) -> None:
    table = connecticut_payload["blocks"]["block_2_boxed_combinations"][
        "classic_due_doubles_table_2"
    ]
    assert [
        (row["pair"], row["draws_since"], row["band"])
        for row in table["pair_slots"]
    ] == [
        ("11", 45, "PURPLE"),
        ("33", 43, "PURPLE"),
        ("77", 41, "PURPLE"),
        ("88", 35, "PURPLE"),
    ]
    assert list(table["pair_slots"][0]["red_boxes"]) == [
        {
            "variant": "midday",
            "badge": "M",
            "combo": "116",
            "draws_since": 1000,
            "unseen": True,
        }
    ]
    assert list(table["closure"]) == [
        "113",
        "117",
        "118",
        "133",
        "177",
        "188",
        "337",
        "338",
        "377",
        "388",
        "778",
        "788",
    ]
    assert table["derived"] is True
    assert table["source_lineages"] == [
        "PAIR_TRACKER",
        "BOXED_COMBO_TRACKER",
    ]
    assert "cannot create an additional source vote" in table[
        "credit_boundary"
    ]


def test_full_external_report_is_complete_and_deterministic(
    connecticut_payload: dict[str, Any],
) -> None:
    report = render_external_markdown(connecticut_payload)
    assert report == render_external_markdown(connecticut_payload)
    assert "## Complete legend" in report
    for block_id in range(1, 11):
        assert f"## Block {block_id}:" in report
    assert "### Doubles Table 2:" in report
    assert "Winner fields present: `False`" in report
    assert "Post-Result Winner Join" not in report


def test_badge_concentration_matches_accepted_connecticut_mock(
    connecticut_payload: dict[str, Any],
) -> None:
    block = connecticut_payload["blocks"][
        "block_7_badge_concentration"
    ]
    expected = {
        "midday": [
            (17, 6, 9, 10),
            (21, 6, 7, 13),
            (22, 5, 10, 11),
            (18, 5, 8, 13),
            (8, 5, 5, 9),
            (14, 5, 5, 7),
            (19, 4, 6, 8),
            (20, 4, 6, 8),
        ],
        "evening": [
            (24, 7, 12, 16),
            (9, 7, 12, 15),
            (21, 6, 13, 17),
            (15, 6, 10, 11),
            (18, 6, 9, 14),
            (14, 6, 8, 12),
            (12, 6, 7, 12),
            (8, 6, 6, 14),
        ],
        "combined": [
            (8, 6, 11, 13),
            (21, 6, 10, 17),
            (23, 6, 9, 13),
            (29, 6, 8, 10),
            (13, 5, 8, 7),
            (24, 5, 7, 14),
            (11, 5, 7, 9),
            (18, 5, 6, 11),
        ],
    }
    actual = {
        variant: [
            (
                row["vtrac_index"],
                row["core_badged_member_count"],
                row["core_badge_event_count"],
                row["pressure_raw"],
            )
            for row in block["by_variant"][variant]
        ]
        for variant in ("midday", "evening", "combined")
    }
    assert actual == expected
    assert connecticut_payload["validation"]["block_7"][
        "qualification_failures"
    ] == []


def test_shortlist_convergence_preserves_source_semantics(
    connecticut_payload: dict[str, Any],
) -> None:
    block = connecticut_payload["blocks"][
        "block_8_shortlist_convergence"
    ]
    ordered = block["within_block_convergence"]["ordered_support"]
    assert [
        (row["literal"], row["source_families"])
        for row in ordered
    ] == [("667", ["POSITIONAL", "PROFIT_ALERTS"])]

    canonicals = block["within_block_convergence"]["canonical_support"]
    assert [row["canonical"] for row in canonicals] == [
        "016",
        "146",
        "167",
        "168",
        "667",
        "689",
    ]
    row_016 = next(row for row in canonicals if row["canonical"] == "016")
    assert row_016["source_families"] == ["BLACKAPPLE", "POSITIONAL"]


def test_optional_compound_source_missing_is_not_a_negative_event() -> None:
    if not HOLDOUT_DAY_DIR.exists():
        pytest.skip("local January holdout fixture is not present")
    payload = build_aux_core(
        state_key="Connecticut4",
        results_date="2026-01-20",
        day_dir=HOLDOUT_DAY_DIR,
    )
    provenance = payload["source_provenance"]["control_center"][
        "profit_compound_events.csv"
    ]
    assert provenance["required"] is False
    assert provenance["present"] is False
    assert payload["blocks"]["block_8_shortlist_convergence"][
        "availability"
    ]["profit_compound_events"] == "SOURCE_MISSING"


def test_box_alert_does_not_create_false_order_credit(
    connecticut_payload: dict[str, Any],
) -> None:
    rows = connecticut_payload["blocks"][
        "block_10_cross_block_convergence"
    ]["by_identity_level"]["exact_literal"]
    row_168 = next(row for row in rows if row["identity"] == "168")
    assert row_168["order_aware_source_lineages"] == ["POSITIONAL"]
    assert "PROFIT_ALERTS" not in row_168["identity_source_lineages"]

    row_667 = next(row for row in rows if row["identity"] == "667")
    assert row_667["order_aware_source_lineages"] == [
        "POSITIONAL",
        "PROFIT_ALERTS",
    ]
    assert "ORDERED_MULTI_SOURCE" in row_667["role_labels"]


def test_derived_blocks_never_become_independent_source_votes(
    connecticut_payload: dict[str, Any],
) -> None:
    rows = connecticut_payload["blocks"][
        "block_10_cross_block_convergence"
    ]["rows"]
    allowed = set(BASE_SOURCE_FAMILIES)
    assert rows
    for row in rows:
        assert set(row["base_source_lineages"]).issubset(allowed)
        assert "BLOCK_7_BADGE_CONCENTRATION" not in row[
            "base_source_lineages"
        ]
        assert "BLOCK_8_SHORTLIST_CONVERGENCE" not in row[
            "base_source_lineages"
        ]


def test_block_10_views_separate_narrowed_and_untranslated_rows(
    connecticut_payload: dict[str, Any],
) -> None:
    block = connecticut_payload["blocks"][
        "block_10_cross_block_convergence"
    ]
    views = block["review_views"]
    refs = [
        (row["identity_level"], row["identity"], row["review_tier"])
        for view in views.values()
        for row in view
    ]
    rows = [
        (row["identity_level"], row["identity"], row["review_tier"])
        for row in block["rows"]
    ]
    assert sorted(refs) == sorted(rows)
    assert len(refs) == len(set(refs))
    assert block["inventory"]["narrowed_rows"] == (
        len(views["independent_identity_convergence"])
        + len(views["narrowed_source_plus_structure"])
    )
    assert block["inventory"]["untranslated_structure_rows"] == len(
        views["untranslated_structure"]
    )


def test_091_join_reports_canonical_and_vtrac_without_false_exact(
    connecticut_payload: dict[str, Any],
) -> None:
    grading = grade_winner(
        connecticut_payload,
        period="Evening",
        winner="091",
    )
    assert grading["winner"] == "091"
    assert grading["winner_canonical"] == "019"
    assert grading["winner_vtrac_index"] == 9
    assert grading["winner_ordered_vcode"] == "v152"
    conversion = grading["conversion_read"]
    assert conversion["exact_literal_expressed"] is False
    assert conversion["ordered_lane_expressed"] is False
    assert conversion["canonical_box_expressed"] is True
    assert conversion["vtrac_territory_expressed"] is True
    assert conversion["highest_specificity_reached"] == "canonical_box"
    assert conversion["highest_specificity_tier"] == (
        "TIER_C_UNTRANSLATED_STRUCTURE"
    )
    assert conversion["translation_gap"] == "CANONICAL_TO_ORDER"
    assert conversion["highest_narrowed_specificity"] == "vtrac_index"
    assert conversion["narrowed_translation_gap"] == "VTRAC_TO_CANONICAL"
    assert conversion["canonical_box_narrowed"] is False
    assert conversion["vtrac_territory_narrowed"] is True
    assert conversion["canonical_untranslated_structure"] is True
    block10 = grading["block_alignment"][
        "block_10_cross_block_convergence"
    ]
    assert block10["exact_literal"] is None
    assert block10["ordered_lane"] is None
    assert block10["canonical_box"]["identity"] == "019"
    assert block10["canonical_box"]["review_tier"] == (
        "TIER_C_UNTRANSLATED_STRUCTURE"
    )
    assert int(block10["vtrac_index"]["identity"]) == 9


def test_result_join_does_not_mutate_frozen_payload(
    connecticut_payload: dict[str, Any],
) -> None:
    before = stable_sha256(connecticut_payload)
    grade_winner(connecticut_payload, period="Midday", winner="917")
    after = stable_sha256(connecticut_payload)
    assert before == after
