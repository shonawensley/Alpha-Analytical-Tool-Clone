import csv
import json
import re

from modules.vtrac_reference import get_vtrac_index
from modules.vtrac_straight_map import (
    VSTRAIGHTS,
    assert_pick3_literals_only,
    boxed_index_for_vcode,
    ordered_vcode_for_combo,
    vstraight_lane_for_combo,
    vstraight_lanes_for_index,
)
from scripts.tools import create_candidate_universe as candidate_universe
from scripts.tools import export_control_center_sharepack as cc_export


def test_ordered_vstraight_fixture_lanes():
    expected_v152 = ["041", "046", "091", "096", "541", "546", "591", "596"]
    expected_v125 = ["014", "019", "064", "069", "514", "519", "564", "569"]
    expected_v512 = ["401", "406", "451", "456", "901", "906", "951", "956"]

    assert ordered_vcode_for_combo("091") == "v152"
    assert vstraight_lane_for_combo("091") == expected_v152
    assert ordered_vcode_for_combo("591") == "v152"
    assert vstraight_lane_for_combo("591") == expected_v152

    assert ordered_vcode_for_combo("019") == "v125"
    assert vstraight_lane_for_combo("019") == expected_v125

    assert ordered_vcode_for_combo("901") == "v512"
    assert vstraight_lane_for_combo("901") == expected_v512
    assert ordered_vcode_for_combo("906") == "v512"
    assert vstraight_lane_for_combo("906") == expected_v512

    assert ordered_vcode_for_combo("168") == "v224"
    assert vstraight_lane_for_combo("168") == ["113", "118", "163", "168", "613", "618", "663", "668"]


def test_boxed_index_remains_family_semantic():
    for combo in ["091", "019", "591", "906", "901", "096"]:
        assert get_vtrac_index(combo) == 9


def test_vstraight_table_invariants():
    for vcode, lane in VSTRAIGHTS.items():
        assert re.fullmatch(r"v[1-5]{3}", vcode)
        assert len(lane) == 8
        assert boxed_index_for_vcode(vcode) is not None
        for combo in lane:
            assert re.fullmatch(r"\d{3}", combo)
            assert ordered_vcode_for_combo(combo) == vcode


def test_index_lanes_are_not_one_representative_lane():
    lanes = vstraight_lanes_for_index(9)
    assert set(lanes) == {"v125", "v152", "v215", "v251", "v512", "v521"}
    corridor = cc_export._vtrac_index_corridor(9)
    assert len(corridor) == 48
    for combo in ["091", "019", "591", "906", "901", "096"]:
        assert combo in corridor


def test_export_vstraights_for_combo_uses_ordered_lane():
    assert cc_export._vstraights_for_combo("091") == VSTRAIGHTS["v152"]
    assert cc_export._vstraights_for_combo("019") == VSTRAIGHTS["v125"]
    assert cc_export._vstraights_for_combo("906") == VSTRAIGHTS["v512"]
    assert cc_export._vstraights_for_combo("v125") == []


def test_vcode_labels_are_not_playable_literals():
    assert ordered_vcode_for_combo("v125") is None
    try:
        assert_pick3_literals_only(["091", "v125"], context="test")
    except ValueError as exc:
        assert "v125" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("vcode label was accepted as a playable literal")


def test_candidate_universe_profit_alerts_quarantines_vcode_labels(tmp_path):
    cc_dir = tmp_path / "control_center"
    cc_dir.mkdir(parents=True)
    path = cc_dir / "profit_alerts.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "State",
                "StateKey",
                "Variant",
                "AlertId",
                "Strength",
                "Suggested",
                "CapLines",
                "DecayDraws",
                "Badges",
                "Canonical",
                "ImpliedSet",
                "Evidence",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "State": "Connecticut",
                "StateKey": "Connecticut4",
                "Variant": "Evening",
                "AlertId": "A05",
                "Strength": "4",
                "Suggested": "STR8_8",
                "CapLines": "8",
                "DecayDraws": "2",
                "Badges": "PERM",
                "Canonical": "091",
                "ImpliedSet": json.dumps(["091", "v125", "019"]),
                "Evidence": "{}",
            }
        )

    packs, _inputs = candidate_universe._parse_profit_alerts(day_dir=tmp_path, state_key="Connecticut4")

    assert len(packs) == 1
    assert packs[0]["combos"] == ["019", "091"]
    assert packs[0]["rejected_implied_values"] == ["v125"]
    assert "implied_guard_rejected:1" in packs[0]["why_tags"]
