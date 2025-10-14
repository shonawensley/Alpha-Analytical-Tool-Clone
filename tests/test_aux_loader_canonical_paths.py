from __future__ import annotations

import os
from pathlib import Path

import pytest

from modules.aux_loaders import load_state_draws

REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_DIR = REPO_ROOT / "data" / "cleaned" / "draws"


@pytest.mark.parametrize(
    "state,variant",
    [
        ("Connecticut4", "combined"),
        ("Connecticut4", "midday"),
        ("Connecticut4", "evening"),
    ],
)
def test_load_state_draws_resolves_canonical_directory(state: str, variant: str) -> None:
    """Ensure canonical loader points at data/cleaned/draws for live data."""
    if not CANONICAL_DIR.exists():
        pytest.skip("canonical draws directory missing")

    draws, resolved = load_state_draws(state, variant=variant)
    assert draws, f"expected draws for {state} ({variant})"
    assert resolved, f"expected path for {state} ({variant})"

    resolved_path = Path(resolved).resolve()
    try:
        resolved_path.relative_to(CANONICAL_DIR.resolve())
    except ValueError as exc:  # pragma: no cover - defensive guard
        raise AssertionError(
            f"resolved path {resolved_path} must live under {CANONICAL_DIR}"
        ) from exc

    assert resolved_path.name.startswith("Connecticut"), resolved_path
