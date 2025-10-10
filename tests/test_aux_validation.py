import types

import pytest
from pathlib import Path

from alpha_analytical.control_center import aux_validation as av

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "acceptance" / "doubles"

POS_FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "acceptance" / "positional"

@pytest.fixture
def thresholds(monkeypatch):
    monkeypatch.setattr(av, "COMBO_DOUBLE_LATE", 2)
    monkeypatch.setattr(av, "COMBO_DOUBLE_VERY_LATE", 3)


def test_compute_double_stats_respects_thresholds(thresholds):
    draws = ["123", "234", "345", "001", "456", "789"]
    stats = av.compute_double_stats(draws)
    assert stats["001"]["severity"] == "R"
    assert stats["001"]["draws_since"] == 3
    assert "123" not in stats


def test_multi_variant_alerts_highlights_overlap(thresholds, monkeypatch):
    def fake_loader(state, variant="combined", base=None, max_n=1000):
        data = {
            "combined": ["123", "234", "345", "112", "456"],
            "midday": ["456", "567", "678", "112", "789"],
            "evening": ["678", "789", "890", "112", "901"],
        }
        return data[variant], f"fake/{state}_{variant}"

    monkeypatch.setattr(av, "load_state_draws", fake_loader)

    alerts = av.multi_variant_alerts("TestState4")
    assert "112" in alerts
    assert set(alerts["112"].keys()) == {"combined", "midday", "evening"}


def test_family_badge_matrix_sources_variant_data(thresholds, monkeypatch):
    def fake_loader(state, variant="combined", base=None, max_n=1000):
        data = {
            "combined": ["005", "505", "550", "551", "115"],
            "midday": ["116", "661", "551", "115", "116"],
            "evening": ["772", "227", "551", "772", "227"],
        }
        return data[variant], f"fake/{state}_{variant}"

    monkeypatch.setattr(av, "load_state_draws", fake_loader)

    matrix = av.family_badge_matrix("TestState4")
    assert matrix  # at least one family flagged
    first_family = next(iter(matrix.values()))
    assert any(key.endswith(":combined") for key in first_family.keys())


@pytest.fixture
def pair_thresholds(monkeypatch):
    monkeypatch.setattr(av, "PAIRS_WINDOW", 5)
    monkeypatch.setattr(av, "REPEATING_LATE", 2)
    monkeypatch.setattr(av, "REPEATING_VERY_LATE", 3)
    monkeypatch.setattr(av, "NONREPEATING_LATE", 2)
    monkeypatch.setattr(av, "NONREPEATING_VERY_LATE", 3)
    monkeypatch.setattr(av, "PAIR_PENDING", 1)


def test_compute_pair_stats_flags_severity(pair_thresholds):
    draws = ["019", "234", "789", "456", "555"]
    stats = av.compute_pair_stats(draws, window=5)

    assert stats["repeating"]["55"] == 4
    assert stats["status"]["55"] == "red"
    assert stats["times_seen"]["55"] == 3
    assert stats["status"]["07"] == "red"


def test_pair_multi_variant_alerts_detects_overlap(pair_thresholds, monkeypatch):
    def fake_loader(state, variant="combined", base=None, max_n=1000):
        data = {
            "combined": ["234", "567", "890"],
            "midday": ["345", "678", "912"],
            "evening": ["012", "345", "678"],
        }
        return data[variant], f"fake/{state}_{variant}"

    monkeypatch.setattr(av, "load_state_draws", fake_loader)

    alerts = av.pair_multi_variant_alerts("TestState4")
    assert "01" in alerts
    assert set(alerts["01"].keys()) == {"combined", "midday"}
    for payload in alerts["01"].values():
        assert payload["severity"] == "red"
        assert payload["draws_since"] >= 3


@pytest.mark.parametrize("variant", ["combined", "midday", "evening"])
def test_summarize_repeat_watch_matches_fixture(variant):
    draws = (FIXTURE_DIR / f"Connecticut_{variant}.txt").read_text(encoding="utf-8").splitlines()
    summary = av.summarize_repeat_watch(draws)
    expected = {
        "combined": {"current_index": 21, "current_streak": 1, "last_repeat_gap": 3, "last_repeat_index": 7, "max_streak": 2, "window": 1000},
        "midday": {"current_index": 24, "current_streak": 1, "last_repeat_gap": 31, "last_repeat_index": 14, "max_streak": 3, "window": 1000},
        "evening": {"current_index": 21, "current_streak": 1, "last_repeat_gap": 23, "last_repeat_index": 31, "max_streak": 3, "window": 1000},
    }[variant]
    assert summary == expected


@pytest.mark.parametrize("variant, expected", [
    ("combined", [{"position": 0, "digit": 3, "draws_since": 59}]),
    ("midday", [{"position": 1, "digit": 1, "draws_since": 51}]),
    ("evening", [{"position": 0, "digit": 3, "draws_since": 51}]),
])
def test_positional_hard_due_flags_expected_digits(variant, expected):
    draws = (FIXTURE_DIR / f"Florida_{variant}.txt").read_text(encoding="utf-8").splitlines()
    flagged = av.positional_hard_due(draws, variant)
    assert flagged == expected


@pytest.mark.parametrize("variant", ["combined", "midday", "evening"])
def test_vtrac_overlay_matches_app_helper(variant):
    from modules import vtrac_reference as vr
    import src.app as streamlit_app

    draws = (FIXTURE_DIR / f"Connecticut_{variant}.txt").read_text(encoding="utf-8").splitlines()
    expected = streamlit_app._build_vtrac_overlay(draws, vr.get_vtrac_index)["draws_since"]
    actual = av.vtrac_overlay(draws)
    assert actual == expected


def test_vtrac_heatboard_matches_app_helper():
    from modules import vtrac_reference as vr
    import src.app as streamlit_app

    draws = (FIXTURE_DIR / "Connecticut_combined.txt").read_text(encoding="utf-8").splitlines()
    overlay = streamlit_app._build_vtrac_overlay(draws, vr.get_vtrac_index)
    expected = streamlit_app._build_vtrac_heatboard(draws, vr.get_vtrac_index, overlay)
    actual = av.vtrac_heatboard(draws, overlay=overlay["draws_since"], window=overlay["window"])
    # Compare a few key metrics to avoid float noise
    for idx in (21, overlay["top_overdue"][0]):
        assert actual[idx]["ds"] == expected[idx]["ds"]
        assert actual[idx]["freq_short"] == expected[idx]["freq_short"]
        assert actual[idx]["freq_long"] == expected[idx]["freq_long"]
        assert actual[idx]["sample_size"] == expected[idx]["sample_size"]
        if actual[idx]["avg_gap"] is not None:
            assert actual[idx]["avg_gap"] == pytest.approx(expected[idx]["avg_gap"])
        if actual[idx]["hazard"] is not None:
            assert actual[idx]["hazard"] == pytest.approx(expected[idx]["hazard"])


def test_sums_stats_align_with_module():
    draws = ["012", "345", "678", "012"]
    expected = av.sums_stats(draws, window=4)
    assert expected["window"] == 4
    assert expected["by_sum"][3]["count"] == 2
    assert expected["by_sum"][12]["draws_since"] == 1
    assert expected["by_sum"][21]["flags"]["blue"] is True
    assert expected["by_root_sum"][3]["count"] == 4


POS_STATE = "Delaware4"


def _load_positional_fixture(state: str, variant: str) -> list[str]:
    path = POS_FIXTURE_DIR / f"{state}_{variant}.txt"
    if path.exists():
        return path.read_text(encoding="utf-8").splitlines()
    return []


@pytest.mark.parametrize("variant", ["combined", "midday", "evening"])
def test_positional_shortlist_top_digits_align(monkeypatch, variant):
    def fake_loader(state, variant=variant, base=None, max_n=1000):
        draws = _load_positional_fixture(state, variant)
        return draws, f"fixture/{state}_{variant}"

    monkeypatch.setattr(av, "load_state_draws", fake_loader)

    report = av.positional_shortlist_report(POS_STATE, window=150)
    top_digits = report["variant_top_digits"].get(variant, [])
    assert top_digits, "Expected top digits for variant"
    digits = [entry["digit"] for entry in top_digits]
    if variant == "combined":
        assert digits[0] == 8
    if variant == "midday":
        assert 0 in digits


def test_positional_shortlist_candidates_and_consensus(monkeypatch):
    def fake_loader(state, variant="combined", base=None, max_n=1000):
        draws = _load_positional_fixture(state, variant)
        return draws, f"fixture/{state}_{variant}"

    monkeypatch.setattr(av, "load_state_draws", fake_loader)

    report = av.positional_shortlist_report(POS_STATE, window=150)
    combos = [entry["combo"] for entry in report["candidates"][:5]]
    assert combos == ["845", "145", "545", "844", "144"]
    assert any("XVAR-Cons" in note for note in report["consensus_notes"])
    assert report["double_pressure_notes"]
