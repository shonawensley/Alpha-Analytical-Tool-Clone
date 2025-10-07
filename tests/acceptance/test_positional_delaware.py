import pytest
from pathlib import Path

from core.aux_config import POS_SHORTLIST_CONFIG, POSITIONAL_WINDOW
from modules.module_d_auxiliary_tools.refactored import positional_tool

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
