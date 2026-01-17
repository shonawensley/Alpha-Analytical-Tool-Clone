from __future__ import annotations

from pathlib import Path

from alpha_analytical.hot_zones import (
    load_table_env_from_json,
    HotZoneScanner,
    HotZoneWeights,
)
from alpha_analytical.hot_zones.scanner import Evidence, aggregate

FIXTURE = Path("tests/fixtures/hot_zones/Sample_tables.json")

def test_hot_zones_scanner_basic(tmp_path):
    env = load_table_env_from_json(FIXTURE)
    scanner = HotZoneScanner(env, weights=HotZoneWeights())
    per_items, tops = scanner.scan()
    assert per_items, "Should emit per-item rows"
    assert tops, "Should emit top candidates"
    assert any(row.col1_arrival or row.precol1_funnel for row in per_items)
    assert any(top.hot_hits >= 1 for top in tops)


def test_hot_zones_top_sort_tiebreaks_are_deterministic():
    weights = HotZoneWeights()
    for name in weights.__dataclass_fields__:  # type: ignore[attr-defined]
        setattr(weights, name, 0.0)
    weights.w_set1_bias = 1.0

    def ev(
        triad: str,
        *,
        is_set1: bool = True,
        is_literal_draw: bool = False,
        guard_injected: bool = False,
    ) -> Evidence:
        return Evidence(
            triad=triad,
            vt_triad="",
            section="Combined",
            set_name="Set1",
            draw_name="Draw1",
            column_index=1,
            row_hits={},
            has_straight=False,
            has_vt_straight=False,
            vt_only_lane=False,
            col1_arrival=False,
            precol1_funnel=False,
            ls_col_42=False,
            ls2_lane=False,
            is_starred=False,
            star_count=0,
            is_superhot_slot=False,
            is_set1=is_set1,
            is_literal_draw=is_literal_draw,
            guard_injected=guard_injected,
        )

    triad_to_evs = {
        # All candidates share score_max=1.0; ordering must be decided by tie-breaks.
        "111": [ev("111", guard_injected=True), ev("111", guard_injected=True)],
        "222": [ev("222", guard_injected=True), ev("222", is_literal_draw=True), ev("222", is_literal_draw=True)],
        "333": [ev("333", guard_injected=True), ev("333")],
        "444": [ev("444")],
        "555": [ev("555"), ev("555", is_set1=False)],
    }

    _, tops = aggregate(triad_to_evs, weights)
    assert [t.triad for t in tops[:5]] == ["111", "222", "333", "444", "555"]
