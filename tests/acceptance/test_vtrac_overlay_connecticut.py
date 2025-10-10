
from pathlib import Path

import pytest

from alpha_analytical.control_center import aux_validation as av

pytestmark = [pytest.mark.acceptance]

FIXTURE_DIR = Path(__file__).resolve().parent.parent / 'fixtures' / 'acceptance' / 'doubles'
STATE = 'Connecticut'
VARIANTS = ('combined', 'midday', 'evening')
WINDOW = 150


def _load_draws(variant: str) -> list[str]:
    path = FIXTURE_DIR / f"{STATE}_{variant}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Missing V-TRAC fixture for {variant}: {path}")
    return path.read_text(encoding='utf-8').splitlines()


EXPECTED_OVERLAY = {
    'combined': [(13, 150), (2, 131), (4, 81), (23, 72), (8, 66)],
    'midday': [(26, 142), (13, 123), (19, 104), (23, 90), (17, 72)],
    'evening': [(2, 150), (20, 150), (15, 144), (32, 130), (16, 117)],
}

EXPECTED_HEAT = {
    'combined': [(13, 150, 0, 0), (2, 131, 0, 0), (4, 81, 1, 0)],
    'midday': [(26, 142, 0, 0), (13, 123, 0, 0), (19, 104, 0, 0)],
    'evening': [(2, 150, 0, 0), (20, 150, 0, 0), (15, 144, 0, 0)],
}

EXPECTED_SUMS = {
    'combined': [(0, 150), (1, 150), (26, 150), (27, 150), (24, 140)],
    'midday': [(0, 150), (1, 150), (2, 150), (3, 150), (25, 150)],
    'evening': [(0, 150), (1, 150), (26, 150), (27, 150), (21, 93)],
}


@pytest.mark.parametrize('variant', VARIANTS)
def test_vtrac_overlay_snapshot(variant: str) -> None:
    draws = _load_draws(variant)
    overlay = av.vtrac_overlay(draws, window=WINDOW)
    top = sorted(overlay.items(), key=lambda item: item[1], reverse=True)[:5]
    assert top == EXPECTED_OVERLAY[variant]


@pytest.mark.parametrize('variant', VARIANTS)
def test_vtrac_heatboard_snapshot(variant: str) -> None:
    draws = _load_draws(variant)
    overlay = av.vtrac_overlay(draws, window=WINDOW)
    heatboard = av.vtrac_heatboard(draws, overlay=overlay, window=WINDOW)
    top = sorted(heatboard.items(), key=lambda item: item[1]['ds'], reverse=True)[:3]
    expected = EXPECTED_HEAT[variant]
    result = [
        (idx, stats['ds'], stats['freq_short'], stats['freq_long'])
        for idx, stats in top
    ]
    assert result == expected


@pytest.mark.parametrize('variant', VARIANTS)
def test_sums_snapshot(variant: str) -> None:
    draws = _load_draws(variant)
    stats = av.sums_stats(draws, window=WINDOW)
    top = sorted(
        stats['by_sum'].items(), key=lambda item: item[1]['draws_since'], reverse=True
    )[:5]
    result = [(label, payload['draws_since']) for label, payload in top]
    assert result == EXPECTED_SUMS[variant]
