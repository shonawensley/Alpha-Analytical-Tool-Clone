from alpha_analytical.hot_zones.scanner import (
    _generate_guard_triads,
    mine_evidence,
    BoxData,
    BoxRef,
    HotScanConfig,
    TopCandidateRow,
)
from alpha_analytical.hot_zones.writer import write_winner_map

def make_box(
    section: str,
    column: int,
    col_value: str,
    hot_count: int,
    *,
    set_name: str = "Set1",
    draw_name: str = "Draw1",
) -> BoxData:
    ref = BoxRef(
        section=section,
        set_name=set_name,
        draw_name=draw_name,
        row_name="R2",
        column_index=column,
        is_starred=True,
        star_count=hot_count,
        is_set1=True,
    )
    return BoxData(
        ref=ref,
        draw_data=[col_value],
        col_value=col_value,
        s_raw=col_value,
        vt_code="",
        s_mirror="",
        is_superhot_slot=True,
        hot_zone_count=hot_count,
    )

def test_guard_triads_include_canonical_and_mirror_for_ct_494():
    row_boxes = [make_box("Combined", 1, "494", 20)]
    triads = _generate_guard_triads(row_boxes)
    assert triads == {"449", "499"}

def test_guard_triads_include_canonical_and_mirror_for_fl_733():
    row_boxes = [make_box("Combined", 1, "733", 20)]
    triads = _generate_guard_triads(row_boxes)
    assert triads == {"288", "337"}

def test_guard_triads_are_gated_by_section_set_draw_column_and_hot_count():
    assert _generate_guard_triads([make_box("Midday", 1, "494", 20)]) == set()
    assert _generate_guard_triads([make_box("Combined", 1, "494", 20, set_name="Set2")]) == set()
    assert _generate_guard_triads([make_box("Combined", 1, "494", 20, draw_name="Draw2")]) == set()
    assert _generate_guard_triads([make_box("Combined", 3, "494", 20)]) == set()
    assert _generate_guard_triads([make_box("Combined", 1, "494", 19)]) == set()

def test_guard_triads_require_exactly_three_digits_in_column_value():
    assert _generate_guard_triads([make_box("Combined", 1, "49", 20)]) == set()
    assert _generate_guard_triads([make_box("Combined", 1, "4949", 20)]) == set()
    assert _generate_guard_triads([make_box("Combined", 1, "49X", 20)]) == set()

def test_mine_evidence_clears_guard_injected_when_no_vt_support():
    boxes = [make_box("Combined", 1, "494", 20)]
    triad_to_evs = mine_evidence(boxes, HotScanConfig(use_metadata_hot_flags=False))

    assert "449" in triad_to_evs
    assert "499" in triad_to_evs  # mirror triad from guard injection

    assert any(e.guard_injected for e in triad_to_evs["449"])
    assert all(not e.guard_injected for e in triad_to_evs["499"])

def test_winner_map_includes_guard_rows(tmp_path):
    non_guard = TopCandidateRow(
        triad="123",
        vt_triad="123",
        support_count=1,
        hot_hits=1,
        superhot_hits=0,
        vertical_hits=1,
        set1_hits=1,
        col1_hits=0,
        precol1_hits=0,
        vt_straight_hits=0,
        vt_only_lane_hits=0,
        guard_hits=0,
        literal_hits=0,
        variant_span=1,
        set_span=1,
        column_span=1,
        score_mean=10.0,
        score_max=10.0,
        evidence_tags="",
    )
    guard_row = TopCandidateRow(
        triad="449",
        vt_triad="55",
        support_count=1,
        hot_hits=1,
        superhot_hits=1,
        vertical_hits=1,
        set1_hits=1,
        col1_hits=1,
        precol1_hits=1,
        vt_straight_hits=1,
        vt_only_lane_hits=0,
        guard_hits=2,
        literal_hits=1,
        variant_span=1,
        set_span=1,
        column_span=1,
        score_mean=5.0,
        score_max=5.0,
        evidence_tags="guard_set1",
    )
    winner_path = write_winner_map(
        state="Test",
        date_stamp="2025-06-24",
        out_dir=str(tmp_path),
        tops=[non_guard, guard_row],
        limit=1,
    )
    data = winner_path.read_text()
    assert '"triad": "449"' in data
