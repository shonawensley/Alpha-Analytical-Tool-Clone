from __future__ import annotations

from typing import Dict

import pandas as pd

COMPOUND_COLUMNS = [
    "section",
    "Canonical",
    "family_id",
    "compound_score",
    "base_max_score",
    "set_chain_depth",
    "draw_chain_depth",
    "hot1_count",
    "hot2_count",
    "col1_hits",
    "consensus_hits",
    "hidden3v_hits",
    "vtrac_straight_hits",
    "double_mirror_hits",
    "rows_covered",
    "examples",
    "compound_why",
]


def compute_compound_scores(rows: pd.DataFrame, feature_cfg: Dict[str, float] | None) -> pd.DataFrame:
    """
    Aggregate per-row evidence into one record per (section, Canonical).

    Parameters
    ----------
    rows : pd.DataFrame
        Stable per-row scores as produced by the extractor. Expected columns include:
        section, Set, Draw, Column, Canonical, score, family_id, hot, score_cons,
        hidden3v, score_vtrac_straight, score_double_mirror, why, etc.
    feature_cfg : Dict[str, float] | None
        Feature configuration (compound weight entries). If None, defaults are used.

    Returns
    -------
    pd.DataFrame
        One row per (section, Canonical) with compound scores, sorted by section then score desc.
    """
    if rows is None or rows.empty:
        return pd.DataFrame(columns=COMPOUND_COLUMNS)

    cfg = feature_cfg or {}
    df = rows.copy()

    # Normalize helper flags
    df["hot_level"] = df.get("hot", 0).fillna(0).astype(int)
    df["is_hot1"] = df["hot_level"].eq(1)
    df["is_hot2"] = df["hot_level"].eq(2)
    df["is_consensus"] = (
        df.get("score_cons", 0).fillna(0).astype(float).gt(0)
        | df.get("cons_full", "").astype(str).str.upper().eq("Y")
        | df.get("cons_3v", "").astype(str).str.upper().eq("Y")
    )
    df["is_hidden3v"] = df.get("hidden3v", "").astype(str).str.upper().eq("Y")
    df["is_vtrac_straight"] = df.get("score_vtrac_straight", 0).fillna(0).astype(float).gt(0)
    df["is_double_mirror"] = (
        df.get("score_double_mirror", 0).fillna(0).astype(float).gt(0)
        | df.get("double_mirror", "").astype(str).str.upper().eq("Y")
    )

    compound_rows = []
    grouped = df.groupby(["section", "Canonical"], sort=False)
    for (section, canonical), group in grouped:
        base_max = float(group["score"].max())
        sets = group["Set"].dropna().unique().tolist()
        set_chain = len(sets)
        draw_chain = int(group.loc[group["Set"].eq("Set1"), "Draw"].nunique())
        col1_hits = int((group["Column"].astype(str) == "1").sum())
        hot1 = int(group["is_hot1"].sum())
        hot2 = int(group["is_hot2"].sum())
        consensus_hits = int(group["is_consensus"].sum())
        hidden_hits = int(group["is_hidden3v"].sum())
        vtrac_hits = int(group["is_vtrac_straight"].sum())
        double_hits = int(group["is_double_mirror"].sum())

        bonus = (
            cfg.get("compound.set_chain_bonus", 2.0) * max(0, set_chain - 1)
            + cfg.get("compound.draw_chain_bonus", 0.5) * draw_chain
            + cfg.get("compound.col1_bonus", 1.0) * col1_hits
            + cfg.get("compound.hot1_bonus", 1.0) * hot1
            + cfg.get("compound.hot2_bonus", 2.0) * hot2
            + cfg.get("compound.consensus_bonus", 1.0) * consensus_hits
            + cfg.get("compound.hidden_core_bonus", 1.0) * hidden_hits
            + cfg.get("compound.vtrac_straight_bonus", 0.5) * vtrac_hits
            + cfg.get("compound.double_mirror_bonus", 0.5) * double_hits
        )
        compound_score = round(base_max + bonus, 3)

        why_bits = []
        if set_chain > 1:
            why_bits.append(f"set_chain{set_chain}")
        if draw_chain > 0:
            why_bits.append(f"draw_chain{draw_chain}")
        if col1_hits:
            why_bits.append(f"col1x{col1_hits}")
        if hot1:
            why_bits.append(f"hot1x{hot1}")
        if hot2:
            why_bits.append(f"hot2x{hot2}")
        if consensus_hits:
            why_bits.append(f"consensusx{consensus_hits}")
        if hidden_hits:
            why_bits.append(f"hidden3vx{hidden_hits}")
        if vtrac_hits:
            why_bits.append(f"vstrx{vtrac_hits}")
        if double_hits:
            why_bits.append(f"dblmirrorx{double_hits}")

        fam_ids = group["family_id"].dropna().astype(int)
        family_id = int(fam_ids.mode().iat[0]) if not fam_ids.empty else None

        compound_rows.append(
            {
                "section": section,
                "Canonical": str(canonical),
                "family_id": family_id,
                "compound_score": compound_score,
                "base_max_score": base_max,
                "set_chain_depth": int(set_chain),
                "draw_chain_depth": int(draw_chain),
                "hot1_count": hot1,
                "hot2_count": hot2,
                "col1_hits": col1_hits,
                "consensus_hits": consensus_hits,
                "hidden3v_hits": hidden_hits,
                "vtrac_straight_hits": vtrac_hits,
                "double_mirror_hits": double_hits,
                "rows_covered": int(len(group)),
                "examples": ";".join(
                    group.sort_values("score", ascending=False)["why"].astype(str).head(2).tolist()
                ),
                "compound_why": "|".join(why_bits),
            }
        )

    return (
        pd.DataFrame(compound_rows)
        .sort_values(["section", "compound_score", "base_max_score"], ascending=[True, False, False])
        .reset_index(drop=True)
    )


__all__ = ["compute_compound_scores", "COMPOUND_COLUMNS"]
