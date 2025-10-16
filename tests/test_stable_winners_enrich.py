import pandas as pd

from alpha_analytical import stable as stable_module
from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index
from alpha_analytical.stable.winners_enrich import attach_stable_evidence


def test_attach_stable_evidence_uses_stable_canon():
    winners = pd.DataFrame([{"Winner": " 0277 "}])
    canonical = stable_module.canon(stable_module.digits_only(winners.iloc[0]["Winner"]))
    expected_family_id = derive_vtrac_index_for_canonical(canonical, get_vtrac_index)

    families_df = pd.DataFrame(
            {
                "family_id": [expected_family_id],
            "family_score": [10.0],
            "section_count": [3],
            "progression_flag": [True],
            "last_remaining_3v": [False],
            "any_doubles_support": [True],
        }
    )

    scores_df = pd.DataFrame(
        {
            "Canonical": ["227"],
            "score": [12.5],
            "type": ["straight"],
            "rows": ["R2"],
            "why": ["unit-test"],
            "cons_full": [True],
            "mirror": [False],
            "straight2": [True],
            "straight3": [False],
            "single_left": [False],
            "cons_3v": [False],
            "dom_last": [False],
            "dom_pair": [False],
            "hidden3v": [False],
        }
    )

    enriched = attach_stable_evidence(
        winners,
        families_df=families_df,
        scores_df=scores_df,
    )

    assert enriched["stable_canonical"].iat[0] == canonical
    assert (enriched["family_id"] == expected_family_id).all()
    assert enriched["family_score"].iloc[0] == 10.0

    bool_columns = [
        "progression_flag",
        "last_remaining_3v",
        "any_doubles_support",
        "mirror",
        "straight2",
        "straight3",
        "single_left",
        "cons_full",
        "cons_3v",
        "dom_last",
        "dom_pair",
        "hidden3v",
    ]
    for column in bool_columns:
        if column in enriched.columns:
            assert str(enriched[column].dtype) == "boolean"


def test_attach_stable_evidence_handles_extended_substrings():
    winner_value = "758"
    winner_canonical = stable_module.canon(stable_module.digits_only(winner_value))
    family_id = derive_vtrac_index_for_canonical(winner_canonical, get_vtrac_index)

    winners = pd.DataFrame([{"Winner": winner_value}])
    families_df = pd.DataFrame(
        {
            "family_id": [family_id],
            "family_score": [21.5],
            "section_count": [2],
            "progression_flag": [False],
            "last_remaining_3v": [False],
            "any_doubles_support": [True],
        }
    )
    scores_df = pd.DataFrame(
        {
            "Canonical": ["007788"],
            "family_id": [family_id],
            "section": ["Combined"],
            "score": [15.0],
            "type": ["straight"],
            "rows": ["R6"],
            "why": ["extended cluster"],
        }
    )

    enriched = attach_stable_evidence(
        winners,
        families_df=families_df,
        scores_df=scores_df,
    )

    assert enriched.loc[0, "family_id"] == family_id
    assert enriched.loc[0, "row_canonical"] == "007788"
    assert enriched.loc[0, "row_score"] == 15.0
    assert enriched.loc[0, "row_type"] == "straight"
    assert enriched.loc[0, "evidence_status"] == "ok"
