import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
src_path = ROOT / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from core.vtrac_families import VTRAC_DOUBLE_FAMILIES, INDEX_TO_FAMILY


def test_family_count_and_membership():
    labels = {fam.label for fam in VTRAC_DOUBLE_FAMILIES}
    assert "0/5-4/9" in labels
    fam = next(f for f in VTRAC_DOUBLE_FAMILIES if f.label == "0/5-4/9")
    expected = {"004", "009", "044", "099", "445", "455", "559", "599"}
    assert set(fam.combos) == expected
    assert set(fam.indices) == {5, 15}


def test_index_family_lookup():
    fam = INDEX_TO_FAMILY[5]
    assert fam.label == "0/5-4/9"
    assert 15 in fam.indices


def test_family_combo_sizes():
    for fam in VTRAC_DOUBLE_FAMILIES:
        combo_set = set(fam.combos)
        # same-class families carry two doubles, cross-class families carry eight
        if len(fam.key) == 2 and fam.key[0] == fam.key[1]:
            assert len(combo_set) == 2
        else:
            assert len(combo_set) == 8

def test_rank_double_families_badges_and_unseen():
    from core.vtrac_family_ranker import rank_double_families

    variant_draws = {
        "combined": ["004", "009", "044", "099", "445", "559", "599"],
        "midday": ["004", "009", "120", "455", "044"],
        "evening": ["455", "004", "009"],
    }
    rankings = rank_double_families(variant_draws, red_threshold=4, blue_threshold=2, limit=20)
    members = []
    for entry in rankings:
        for member in entry["members"]:
            if member["combo"] == "455":
                members.append(member)
    assert {m["variant"] for m in members} == {"combined", "midday"}
    combined_entry = next(m for m in members if m["variant"] == "combined")
    assert combined_entry["severity"] == "R"
    assert combined_entry["unseen"] is True
    midday_entry = next(m for m in members if m["variant"] == "midday")
    assert midday_entry["severity"] == "B"
    assert midday_entry["unseen"] is False


