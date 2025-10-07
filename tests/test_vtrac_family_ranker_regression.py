from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
for candidate in (ROOT, SRC_DIR):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
from core.vtrac_family_ranker import rank_double_families

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "acceptance" / "doubles"
EXPECTED_PATH = FIXTURE_DIR / "expected.json"
VARIANTS = ("combined", "midday", "evening")

EXPECTED_TOKENS = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))


def _load_variant_draws(state: str, variant: str) -> list[str]:
    path = FIXTURE_DIR / f"{state}_{variant}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Missing doubles fixture for {state} {variant}: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def _tokens_by_label(rankings: list[dict]) -> dict[str, list[str]]:
    mapped: dict[str, list[str]] = {}
    for entry in rankings:
        label = entry.get("label")
        if not label:
            continue
        members = entry.get("members", [])
        tokens: list[str] = []
        for member in members:
            severity = member.get("severity")
            variant = member.get("variant", "")
            canonical = member.get("canonical") or member.get("combo")
            if severity not in ("R", "B") or not canonical or not variant:
                continue
            token = f"{severity}{canonical}{variant[0].upper()}"
            tokens.append(token)
        mapped[label] = tokens
    return mapped


def test_rank_double_families_regression():
    for state, expectations in EXPECTED_TOKENS.items():
        variant_draws = {
            variant: _load_variant_draws(state, variant)
            for variant in VARIANTS
        }
        rankings = rank_double_families(
            variant_draws,
            red_threshold=COMBO_DOUBLE_VERY_LATE,
            blue_threshold=COMBO_DOUBLE_LATE,
            limit=5,
        )
        actual = _tokens_by_label(rankings)
        assert actual == expectations

        for tokens in actual.values():
            for token in tokens:
                assert len(token) == 5, f"Unexpected token format: {token}"
                assert token[:1] in {"R", "B"}
                assert token[-1] in {"C", "M", "E"}

        for entry in rankings:
            for member in entry.get("members", []):
                unseen = bool(member.get("unseen"))
                if unseen:
                    assert int(member.get("draws_since", 0)) >= COMBO_DOUBLE_VERY_LATE, (
                        f"Unseen combo {member.get('combo')} should only trigger at or beyond red threshold"
                    )
