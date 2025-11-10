from __future__ import annotations

import pandas as pd

from alpha_analytical.stable.compound import compute_compound_scores


def test_compound_bonus_and_sorting():
    rows = pd.DataFrame(
        [
            dict(
                section="Combined",
                Set="Set1",
                Draw="Draw5",
                Column=1,
                Canonical="244",
                family_id=355,
                score=30.0,
                hot=2,
                score_cons=1.0,
                hidden3v="Y",
                score_vtrac_straight=0.5,
                score_double_mirror=0.0,
                why="example A",
            ),
            dict(
                section="Combined",
                Set="Set1",
                Draw="Draw3",
                Column=2,
                Canonical="244",
                family_id=355,
                score=27.5,
                hot=1,
                score_cons=1.0,
                hidden3v="",
                score_vtrac_straight=0.0,
                score_double_mirror=0.5,
                why="example B",
            ),
            dict(
                section="Combined",
                Set="Set2",
                Draw="Draw1",
                Column=1,
                Canonical="244",
                family_id=553,
                score=25.0,
                hot=1,
                score_cons=0.0,
                hidden3v="Y",
                score_vtrac_straight=0.5,
                score_double_mirror=0.0,
                why="example C",
            ),
        ]
    )
    cfg = {
        "compound.set_chain_bonus": 2.0,
        "compound.draw_chain_bonus": 0.5,
        "compound.col1_bonus": 1.0,
        "compound.hot1_bonus": 1.0,
        "compound.hot2_bonus": 2.0,
        "compound.consensus_bonus": 1.0,
        "compound.hidden_core_bonus": 1.0,
        "compound.vtrac_straight_bonus": 0.5,
        "compound.double_mirror_bonus": 0.5,
    }
    compound_df = compute_compound_scores(rows, cfg)
    assert not compound_df.empty
    record = compound_df.iloc[0]
    assert record["Canonical"] == "244"
    assert record["set_chain_depth"] == 2
    assert record["draw_chain_depth"] >= 1
    assert record["hot1_count"] == 2
    assert record["hot2_count"] == 1
    assert "set_chain" in record["compound_why"]
    assert record["compound_score"] > record["base_max_score"]
