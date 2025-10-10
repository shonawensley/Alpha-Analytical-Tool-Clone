import pytest
from pathlib import Path

from core.aux_config import POS_SHORTLIST_CONFIG, POSITIONAL_WINDOW
from modules.module_d_auxiliary_tools.refactored import positional_tool
from alpha_analytical.control_center import aux_validation as av

pytestmark = [pytest.mark.acceptance, pytest.mark.smoke]

FIXTURE_DIR = Path(__file__).resolve().parent.parent / "fixtures" / "acceptance" / "positional"


def _load_variant_draws(state: str, variant: str) -> list[str]:
    path = FIXTURE_DIR / f"{state}_{variant}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Missing fixture for {state} {variant}: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def test_positional_shortlist_delaware_repeat_endcap():
    state = "Delaware4"
    draws_by_variant = {}
    for variant in ("combined", "midday", "evening"):
        draws = _load_variant_draws(state, variant)
        if draws:
            draws_by_variant[variant] = draws

    report = positional_tool.analyze_state_variants(
        draws_by_variant,
        window=POSITIONAL_WINDOW,
        topk=int(POS_SHORTLIST_CONFIG.get("topk_per_pos", 3)),
        due_doubles_active=False,
        shortlist_cfg=POS_SHORTLIST_CONFIG,
        vtrac_hot_indices=set(),
        vtrac_hot_families={},
    )

    top_combos = [cand.combo for cand in report.candidates[:5]]
    assert top_combos == ["845", "145", "545", "844", "144"]

    repeat_candidates = [cand for cand in report.candidates if cand.source == "repeat_endcap"]
    assert any(cand.combo == "545" for cand in repeat_candidates)
    assert all("Repeat-Endcap" in cand.tags for cand in repeat_candidates)

    tagged_candidates = [cand for cand in report.candidates if cand.tags]
    assert tagged_candidates, "Expected shortlist candidates to carry tag metadata"

    assert all(cand.score >= 0 for cand in report.candidates[:10]), "Scores should be non-negative"



def test_positional_shortlist_report_aligns_with_helper(monkeypatch):
    state = "Delaware4"
    draws_cache = {variant: _load_variant_draws(state, variant) for variant in ("combined", "midday", "evening")}

    def fake_loader(state_label, variant="combined", base=None, max_n=1000):
        return draws_cache[variant], f"fixture/{state_label}_{variant}"

    monkeypatch.setattr(av, "load_state_draws", fake_loader)

    shortlist = av.positional_shortlist_report(
        state,
        window=POSITIONAL_WINDOW,
        topk=int(POS_SHORTLIST_CONFIG.get("topk_per_pos", 3)),
    )

    combos = [entry["combo"] for entry in shortlist["candidates"][:5]]
    assert combos == ["845", "145", "545", "844", "144"]

    consensus_notes = shortlist.get("consensus_notes", [])
    assert any("XVAR-Cons" in note for note in consensus_notes)

    double_pressure_notes = shortlist.get("double_pressure_notes", [])
    assert any("Double-Pressure" in note for note in double_pressure_notes)

    variant_top_digits = shortlist["variant_top_digits"]
    combined_top = variant_top_digits["combined"][0]
    assert combined_top["position"] == 0
    assert combined_top["digit"] == 8

    midday_digits = {entry["digit"] for entry in variant_top_digits["midday"]}
    assert 0 in midday_digits
