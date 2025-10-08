from modules.vtrac_matchers import build_winner_targets, digits_only, analyze_cell, collect_spans


def test_digits_only_strips_non_digits():
    assert digits_only("9-0-3-4") == "9034"
    assert digits_only("abc") == ""


def test_analyze_cell_returns_winner_and_family_hits():
    targets = build_winner_targets("934", ["934", "394", "493"])
    straights_strict, straights_gap, family_strict, family_gap = analyze_cell("....5934....", targets)
    assert "934" in straights_strict
    assert "934" in family_strict
    _, straights_gap2, _, _ = analyze_cell("9034", targets)
    assert "934" in straights_gap2


def test_collect_spans_includes_gap_highlights():
    targets = build_winner_targets("934", ["934", "943"])
    spans = collect_spans("9034", targets)
    assert spans["winner_gap"] == [(0, 4)]
    spans_purple = collect_spans("--943--", targets)
    assert spans_purple["family_strict"] == [(2, 5)]



def test_collect_spans_marks_vt_straight_strict():
    targets = build_winner_targets("894", ["894", "349", "344"])
    spans = collect_spans("--3344--", targets)
    assert (2, 6) in spans["vt_straight_strict"]
    assert spans["vt_straight_gap"] == []



def test_collect_spans_marks_vt_straight_gap():
    targets = build_winner_targets("894", ["894", "349", "344"])
    spans = collect_spans("--336644--", targets)
    assert (2, 8) in spans["vt_straight_gap"]
    assert spans["vt_straight_strict"] == []
