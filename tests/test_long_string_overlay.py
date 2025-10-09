import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(1, str(SRC))

import src.core.module_c_vtrac as vtrac


def test_is_long_string_cell_matches_known_windows():
    assert vtrac._is_long_string_cell('midday', 'Set1', 'Draw4', 'R2', 3)
    assert vtrac._is_long_string_cell('evening', 'Set3', 'Draw1', 'R2', 7)
    assert not vtrac._is_long_string_cell('midday', 'Set2', 'Draw2', 'R4', 5)
