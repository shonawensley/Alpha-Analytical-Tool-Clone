

from core.aux_config import POS_SHORTLIST_CONFIG
from modules.module_d_auxiliary_tools.refactored import positional_tool as pt

AggregatedDigit = pt.AggregatedDigit
CandidateSeed = pt.CandidateSeed


def _make_agg(position: int, digit: int, score: float = 5.0, occurrences=None, tags=None) -> AggregatedDigit:
    occ = occurrences if occurrences is not None else [("combined", 1)]
    tg = tags if tags is not None else []
    return AggregatedDigit(digit=digit, position=position, score=score, occurrences=occ, tags=tg)


def _base_shortlist_cfg(overrides=None):
    overrides = overrides or {}
    return pt._load_shortlist_config(overrides)


def test_shortlist_config_override_merges_defaults():
    cfg = _base_shortlist_cfg(
        {
            "topk_per_pos": 5,
            "caps": {"cartesian": 12},
            "features": {"enable_vtrac_boosts": False},
        }
    )

    assert cfg.topk_per_pos == 5
    assert cfg.caps.cartesian == 12
    assert cfg.caps.repeat_endcap == POS_SHORTLIST_CONFIG["caps"]["repeat_endcap"]
    assert cfg.features.enable_vtrac_boosts is False
    assert cfg.features.enable_repeat_endcap is True


def test_score_seed_adds_vtrac_boost_and_family_tags():
    cfg = _base_shortlist_cfg()
    agg_map = {
        0: {1: _make_agg(0, 1, score=4.0)},
        1: {2: _make_agg(1, 2, score=3.5)},
        2: {3: _make_agg(2, 3, score=3.0)},
    }
    digit_variants = {
        0: {1: {"combined"}},
        1: {2: {"combined"}},
        2: {3: {"combined"}},
    }
    seed = CandidateSeed(digits=(1, 2, 3), source="cartesian")
    hot_indices = {17}
    hot_families = {"123": "Family 17"}

    original_resolver = pt.get_vtrac_index
    pt.get_vtrac_index = lambda combo: 17 if combo == "123" else None
    try:
        rec = pt._score_candidate_seed(seed, agg_map, digit_variants, cfg, hot_indices, hot_families)
    finally:
        pt.get_vtrac_index = original_resolver

    assert rec is not None
    assert rec.vtrac_index == 17
    assert "VTRAC-Hot" in rec.tags
    assert "Family-Family 17" in rec.tags
    assert any("V-TRAC idx 17 hot" in note for note in rec.evidence)
    assert any("Family Family 17 hot" in note for note in rec.evidence)


def test_score_seed_repeat_endcap_has_lane_metadata():
    cfg = _base_shortlist_cfg()
    agg_map = {
        0: {4: _make_agg(0, 4, score=4.5)},
        1: {5: _make_agg(1, 5, score=3.5)},
        2: {4: _make_agg(2, 4, score=4.0)},
    }
    digit_variants = {
        0: {4: {"combined"}},
        1: {5: {"combined"}},
        2: {4: {"combined"}},
    }
    seed = CandidateSeed(digits=(4, 5, 4), source="repeat_endcap", metadata={"lanes": ["C", "E"]})

    rec = pt._score_candidate_seed(seed, agg_map, digit_variants, cfg, set(), {})

    assert rec is not None
    assert "Repeat-Endcap" in rec.tags
    assert any("Repeat endcap lanes: C/E" in note for note in rec.evidence)


def test_score_seed_lane_concordance_marks_evidence():
    cfg = _base_shortlist_cfg()
    agg_map = {
        0: {7: _make_agg(0, 7, score=4.2)},
        1: {8: _make_agg(1, 8, score=4.0)},
        2: {9: _make_agg(2, 9, score=3.8)},
    }
    digit_variants = {
        0: {7: {"combined", "midday"}},
        1: {8: {"combined"}},
        2: {9: {"combined"}},
    }
    seed = CandidateSeed(digits=(7, 8, 9), source="lane", metadata={"lane": "Mirror lane"})

    rec = pt._score_candidate_seed(seed, agg_map, digit_variants, cfg, set(), {})

    assert rec is not None
    assert any(tag.startswith("Lane-") for tag in rec.tags)
    assert any("Lane concordance: Mirror lane" in note for note in rec.evidence)



def test_repeat_endcap_shortlist_includes_bridge():
    cfg = _base_shortlist_cfg()
    aggregated_map = {
        0: {9: _make_agg(0, 9, score=5.2, occurrences=[("combined", 1), ("evening", 1)], tags=["Mirror-Echo"])},
        1: {8: _make_agg(1, 8, score=4.8, occurrences=[("combined", 1)])},
        2: {9: _make_agg(2, 9, score=5.0, occurrences=[("combined", 1), ("evening", 2)])},
    }
    aggregated_sorted = {pos: list(dmap.values()) for pos, dmap in aggregated_map.items()}
    digit_variants = {
        0: {9: {"combined", "evening"}},
        1: {8: {"combined", "evening"}},
        2: {9: {"combined", "evening"}},
    }
    lane_hits = {
        "combined": {0: [9], 1: [8], 2: [9]},
        "evening": {0: [9], 1: [8], 2: [9]},
    }

    candidates = pt._build_shortlist_candidates(
        aggregated_sorted,
        aggregated_map,
        digit_variants,
        lane_hits,
        cfg,
        set(),
        {},
    )

    combos = {cand.combo for cand in candidates}
    assert "989" in combos


def test_lane_concordance_candidate_present():
    cfg = _base_shortlist_cfg()
    aggregated_map = {
        0: {1: _make_agg(0, 1, score=4.4, occurrences=[("midday", 1)])},
        1: {2: _make_agg(1, 2, score=4.1, occurrences=[("midday", 1)])},
        2: {3: _make_agg(2, 3, score=4.0, occurrences=[("midday", 1)])},
    }
    aggregated_sorted = {pos: list(dmap.values()) for pos, dmap in aggregated_map.items()}
    digit_variants = {
        0: {1: {"midday"}},
        1: {2: {"midday"}},
        2: {3: {"midday"}},
    }
    lane_hits = {"midday": {0: [1], 1: [2], 2: [3]}}

    candidates = pt._build_shortlist_candidates(
        aggregated_sorted, aggregated_map, digit_variants, lane_hits, cfg, set(), {}
    )

    lane_sources = {cand.source for cand in candidates}
    assert "lane" in lane_sources
    assert any(cand.combo == "123" for cand in candidates if cand.source == "lane")


def test_union_pool_respects_multi_variant_digits():
    cfg = _base_shortlist_cfg()
    aggregated_sorted = {
        0: [
            _make_agg(0, 4, score=5.5, occurrences=[("combined", 1)]),
            _make_agg(0, 7, score=5.0, occurrences=[("midday", 1)]),
        ],
        1: [
            _make_agg(1, 8, score=5.2, occurrences=[("combined", 1)]),
        ],
        2: [
            _make_agg(2, 9, score=5.3, occurrences=[("combined", 1)]),
        ],
    }
    pool = pt._build_union_pool(aggregated_sorted, cfg)

    digits_p1 = {agg.digit for agg in pool[0]}
    assert {4, 7}.issubset(digits_p1)
