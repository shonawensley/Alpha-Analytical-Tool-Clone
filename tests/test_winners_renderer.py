import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(1, str(SRC))

from modules import winner_report_full as wrf


def test_winner_report_contains_highlights(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(wrf.ph, "get_analysis_dir", lambda kind, state: str(tmp_path))
    out_path = Path(wrf.write_winner_full_report("Connecticut4", "934"))
    assert out_path.exists()
    html = out_path.read_text(encoding="utf-8")
    for token in ["legend", "hit-winner", "hit-winner-gap", "hit-vt-straight", "hit-vt-straight-gap", "hit-family"]:
        assert token in html
