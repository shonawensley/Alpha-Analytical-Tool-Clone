import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

WORKING_ROOT = PROJECT_ROOT / "scripts" / "auxiliary" / "working"
if str(WORKING_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKING_ROOT))

from modules.analyze_pairs import extract_pairs


@pytest.mark.parametrize(
    "draw, expected_non, expected_rep",
    [
        ("123", {"12", "13", "23"}, set()),
        ("111", set(), {"11"}),
        ("122", {"12"}, {"22"}),
    ],
)
def test_extract_pairs_semantics(draw, expected_non, expected_rep):
    nonrepeating, repeating = extract_pairs(draw)
    assert set(nonrepeating) == expected_non
    assert set(repeating) == expected_rep


def test_extract_pairs_rejects_bad_input():
    with pytest.raises(ValueError):
        extract_pairs("12")
