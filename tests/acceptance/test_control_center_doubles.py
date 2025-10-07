from __future__ import annotations

import json
from pathlib import Path

import pytest

import src.app as streamlit_app

pytestmark = [pytest.mark.acceptance, pytest.mark.smoke]

FIXTURE_DIR = Path(__file__).resolve().parent.parent / "fixtures" / "acceptance" / "doubles"
EXPECTED_PATH = FIXTURE_DIR / "expected.json"
VARIANTS = ("combined", "midday", "evening")

EXPECTED_TOKENS = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))


def _load_variant_draws(state: str, variant: str) -> list[str]:
    path = FIXTURE_DIR / f"{state}_{variant}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Missing doubles fixture for {state} {variant}: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def _extract_tokens(entry: dict) -> list[str]:
    tokens: list[str] = []
    for member in entry.get("members", []):
        severity = member.get("severity")
        variant = member.get("variant", "")
        canonical = member.get("canonical") or member.get("combo")
        if severity not in ("R", "B") or not canonical or not variant:
            continue
        tokens.append(f"{severity}{canonical}{variant[0].upper()}")
    return tokens


@pytest.mark.parametrize("state", sorted(EXPECTED_TOKENS.keys()))
def test_control_center_family_render(state: str) -> None:
    variant_draws = {
        variant: _load_variant_draws(state, variant)
        for variant in VARIANTS
    }
    rankings = streamlit_app._rank_double_families(
        variant_draws,
        limit=5,
    )

    expectations = EXPECTED_TOKENS[state]
    actual = {entry["label"]: _extract_tokens(entry) for entry in rankings}
    assert actual == expectations

    for entry in rankings:
        display = entry.get("display", "")
        assert "CEM" not in display
        assert display.count("<span") == len(_extract_tokens(entry))
        for token in _extract_tokens(entry):
            badge = token[-1]
            assert f"<sup>{badge}</sup>" in display
