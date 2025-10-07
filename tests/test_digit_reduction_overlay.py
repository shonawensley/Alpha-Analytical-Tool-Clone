import csv
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
src_path = ROOT / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from alpha_analytical.digit_reduction.analyzer_v2.pipeline import _load_winner_flags
from alpha_analytical.digit_reduction.analyzer_v2.score import score_row
from alpha_analytical.digit_reduction.analyzer_v2.winners_overlay import WinnerSpec, _highlight_text_segment, _render_banner, _collect_recent_draws
import alpha_analytical.digit_reduction.analyzer_v2.winners_overlay as overlay


def test_highlight_marks_embedded_exact_sequences():
    spec = WinnerSpec(combo="590")
    highlighted = _highlight_text_segment("45590*", spec)
    assert '<span class="dr-winner-exact">590</span>' in highlighted


def test_highlight_marks_vtrac_family_sequences():
    spec = WinnerSpec(combo="123")
    highlighted = _highlight_text_segment("Box678*", spec)
    assert 'dr-winner-vtrac' in highlighted


def test_load_winner_flags_reads_latest_csv(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    winners_dir = tmp_path / "digit_reduction" / "TestState" / "analyzer_v2" / "winners"
    winners_dir.mkdir(parents=True)
    csv_path = winners_dir / "20250101_Combined_winner_flags.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "area",
            "section",
            "set",
            "draw",
            "col",
            "method",
            "mode",
            "dr_win_exact",
            "dr_win_vtrac",
            "dr_win_step_exact",
            "dr_win_step_vtrac",
            "dr_win_final_value",
            "dr_win_vtrac_local_index",
        ])
        writer.writerow([
            "LS1",
            "Combined",
            "Set1",
            "20240905",
            7,
            "MethodA",
            "combined",
            1,
            0,
            3,
            -1,
            "590",
            12,
        ])

    def fake_analyzer_out_dir(state: str, analysis_root):
        base = Path(analysis_root) / "digit_reduction" / state / "analyzer_v2"
        base.mkdir(parents=True, exist_ok=True)
        return base

    monkeypatch.setattr(
        "alpha_analytical.digit_reduction.analyzer_v2.pipeline.analyzer_out_dir",
        fake_analyzer_out_dir,
    )

    flags_map = _load_winner_flags("TestState", tmp_path)
    key = (
        "TestState",
        "LS1",
        "Combined",
        "Set1",
        "20240905",
        7,
        "MethodA",
        "combined",
    )
    assert key in flags_map
    entry = flags_map[key]
    assert entry["dr.win_exact"] == 1
    assert entry["dr.win_vtrac"] == 0
    assert entry["dr.win_step_exact"] == 3
    assert entry["dr.win_final_value"] == "590"


def test_score_row_includes_winner_signals():
    row = {
        "dr.win_exact": 1,
        "dr.win_vtrac": 0,
        "dr.win_step_exact": 2,
        "dr.win_step_vtrac": 4,
    }
    weights = {
        "dr.win_exact": 3.0,
        "dr.win_vtrac": 1.5,
        "dr.win_early_exact": 1.0,
        "dr.win_early_vtrac": 0.5,
    }
    penalties = {}
    caps = {"score_min": 0.0, "score_max": 100.0}
    thresholds = {"dr_max_step": 10}
    score = score_row(row, weights, penalties, caps, thresholds)
    assert score == pytest.approx(41.3636, rel=1e-3)



def test_collect_recent_draws_uses_loader(monkeypatch: pytest.MonkeyPatch):
    calls = []

    def fake_loader(state_label: str, variant: str, *, max_n: int, base=None):
        calls.append((state_label, variant, max_n))
        return [f"{variant}-a", f"{variant}-b", f"{variant}-c"], f"{variant}.csv"

    monkeypatch.setattr(overlay, "load_state_draws", fake_loader)
    summary = _collect_recent_draws("Connecticut4", depth=2)

    assert calls == [
        ("Connecticut4", "combined", 2),
        ("Connecticut4", "midday", 2),
        ("Connecticut4", "evening", 2),
    ]
    combined = summary["Combined"]
    assert combined["draws"] == ["combined-a", "combined-b"]
    assert combined["source"] == "combined.csv"
    assert combined["sets"]["Set1"] == "combined-a"
    assert combined["sets"]["Set2"] == "combined-b"
    assert "Set3" not in combined["sets"]
    assert combined["labels"]["current"] == "combined-a"
    assert combined["labels"]["previous"] == "combined-b"
    assert "two_prior" not in combined["labels"]


def test_render_banner_includes_recent_draws():
    summary = {
        "counts": {},
        "earliest": {},
        "recent_draws": {
            "Combined": {
                "draws": ["059", "022"],
                "source": "combined.csv",
                "sets": {"Set1": "059", "Set2": "022"},
                "labels": {"current": "059", "previous": "022"},
            },
            "Midday": {
                "draws": ["159"],
                "source": "midday.csv",
                "sets": {"Set1": "159"},
                "labels": {"current": "159"},
            },
            "Evening": {
                "draws": [],
                "source": "evening.csv",
                "sets": {},
                "labels": {},
            },
        },
        "recent_draw_depth": 2,
    }
    html = _render_banner("Connecticut4", "Combined", WinnerSpec(combo="059"), summary)
    assert "Draw timeline (Set1 current, Set2 previous, Set3 two prior)" in html
    assert "Combined: Set1=059, Set2=022, Set3=n/a" in html
    assert "Midday: Set1=159, Set2=n/a, Set3=n/a" in html
    assert "Evening: Set1=n/a, Set2=n/a, Set3=n/a" in html
