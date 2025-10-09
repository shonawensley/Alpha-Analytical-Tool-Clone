import types

import pytest

from alpha_analytical.control_center import aux_validation as av


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
