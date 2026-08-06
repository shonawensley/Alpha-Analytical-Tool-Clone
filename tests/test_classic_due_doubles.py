from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
for candidate in (ROOT, SRC_DIR):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from core.classic_due_doubles import (
    build_classic_due_doubles_review,
    build_due_pair_boxed_closure,
    canonical_box,
    double_boxes_for_pair,
    group_red_box_entries,
    rank_due_repeating_pairs,
)


def test_canonical_box_and_pair_members_collapse_permutations():
    assert canonical_box("441") == "144"
    assert canonical_box("414") == "144"
    assert canonical_box("144") == "144"
    assert canonical_box("44") == ""
    assert double_boxes_for_pair("44") == (
        "044",
        "144",
        "244",
        "344",
        "445",
        "446",
        "447",
        "448",
        "449",
    )


def test_top_four_pairs_are_ranked_from_combined_history():
    draws = ["123"] * 360
    pair_gaps = {
        "00": 2,
        "11": 4,
        "22": 6,
        "33": 8,
        "44": 10,
        "55": 12,
        "66": 14,
        "77": 16,
        "88": 18,
        "99": 20,
    }
    for pair, gap in pair_gaps.items():
        singleton = "0" if pair != "00" else "1"
        draws[gap] = pair + singleton

    assert rank_due_repeating_pairs(draws, limit=4) == (
        ("99", 20),
        ("88", 18),
        ("77", 16),
        ("66", 14),
    )
    assert rank_due_repeating_pairs([], limit=4) == ()


def test_top_four_closure_has_twelve_unique_boxed_candidates():
    closure = build_due_pair_boxed_closure(("11", "44", "55", "66"))
    assert closure == (
        "114",
        "115",
        "116",
        "144",
        "155",
        "166",
        "445",
        "446",
        "455",
        "466",
        "556",
        "566",
    )
    assert "441" not in closure


def test_red_boxes_require_full_history_and_keep_variant_provenance():
    combined = ["411", "222", "333", "555", "666"]
    midday = ["222", "333", "555", "666", "777"]
    evening = ["114", "222", "333", "555", "666"]
    review = build_classic_due_doubles_review(
        "Example",
        {
            "combined": combined,
            "midday": midday,
            "evening": evening,
        },
        pair_window=5,
        pair_limit=10,
        combination_window=5,
        red_threshold=5,
    )

    slot_11 = next(slot for slot in review.pair_slots if slot.pair == "11")
    tokens = {(entry.combo, entry.badge) for entry in slot_11.red_boxes}
    assert ("114", "C") not in tokens
    assert ("114", "E") not in tokens
    assert ("114", "M") in tokens
    assert all(entry.unseen for entry in slot_11.red_boxes)
    grouped = dict(group_red_box_entries(slot_11.red_boxes))
    assert grouped["114"] == ("M",)
    assert grouped["115"] == ("C", "M", "E")
    assert {coverage.badge for coverage in review.coverage if coverage.red_eligible} == {
        "C",
        "M",
        "E",
    }


def test_seen_at_oldest_draw_is_not_red_but_absent_box_is_red():
    review = build_classic_due_doubles_review(
        "Boundary",
        {
            "combined": ["222", "333", "555", "666", "411"],
        },
        pair_window=5,
        pair_limit=10,
        combination_window=5,
        red_threshold=5,
    )

    slot_11 = next(slot for slot in review.pair_slots if slot.pair == "11")
    tokens = {(entry.combo, entry.badge) for entry in slot_11.red_boxes}
    assert ("114", "C") not in tokens
    assert ("115", "C") in tokens


def test_incomplete_variant_history_never_receives_red_credit():
    review = build_classic_due_doubles_review(
        "Incomplete",
        {
            "combined": ["222", "333", "555", "666"],
        },
        pair_window=4,
        pair_limit=4,
        combination_window=5,
        red_threshold=5,
    )

    assert all(not slot.red_boxes for slot in review.pair_slots)
    assert review.coverage[0].draws_used == 4
    assert review.coverage[0].red_eligible is False
