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
    "funnel_precol1",
    "vt_only_lane",
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
    df["_draw_idx"] = (
        df.get("Draw", "").astype(str).str.extract(r"(\d+)").fillna(-1).astype(int)
    )

    compound_rows = []
    grouped = df.groupby(["section", "Canonical"], sort=False)
    for (section, canonical), group in grouped:
        base_max = float(group["score"].max())
        sets = group["Set"].dropna().unique().tolist()
        set_chain = len(sets)
        set1_group = group[group["Set"].astype(str) == "Set1"]
        draw_chain = int(set1_group["Draw"].nunique()) if not set1_group.empty else 0
        col1_mask = group["Column"].astype(str) == "1"
        col1_hits = int(col1_mask.sum())
        funnel_precol1 = 0
        if col1_hits > 0 and not set1_group.empty:
            col2_hot2 = set1_group[
                (set1_group["Column"].astype(str) == "2") & set1_group["hot_level"].eq(2)
            ]
            col1_rows = set1_group[set1_group["Column"].astype(str) == "1"]
            if not col2_hot2.empty and not col1_rows.empty:
                if col2_hot2["_draw_idx"].max() < col1_rows["_draw_idx"].min():
                    funnel_precol1 = 1
        hot1 = int(group["is_hot1"].sum())
        hot2 = int(group["is_hot2"].sum())
        consensus_hits = int(group["is_consensus"].sum())
        hidden_hits = int(group["is_hidden3v"].sum())
        vtrac_hits = int(group["is_vtrac_straight"].sum())
        double_hits = int(group["is_double_mirror"].sum())

        hot2_cap = cfg.get("compound.hot2_cap")
        double_cap = cfg.get("compound.double_mirror_cap")
        hot2_effective = min(hot2, int(hot2_cap)) if hot2_cap is not None else hot2
        double_effective = min(double_hits, int(double_cap)) if double_cap is not None else double_hits
        vt_only_threshold = cfg.get("compound.vt_only_threshold", 2)
        vt_only = vtrac_hits >= int(vt_only_threshold or 0) and hot2 == 0 and col1_hits == 0

        bonus = (
            cfg.get("compound.set_chain_bonus", 2.0) * max(0, set_chain - 1)
            + cfg.get("compound.draw_chain_bonus", 0.5) * draw_chain
            + cfg.get("compound.col1_bonus", 1.0) * col1_hits
            + cfg.get("compound.hot1_bonus", 1.0) * hot1
            + cfg.get("compound.hot2_bonus", 2.0) * hot2_effective
            + cfg.get("compound.consensus_bonus", 1.0) * consensus_hits
            + cfg.get("compound.hidden_core_bonus", 1.0) * hidden_hits
            + cfg.get("compound.vtrac_straight_bonus", 0.5) * vtrac_hits
            + cfg.get("compound.double_mirror_bonus", 0.5) * double_effective
            + cfg.get("compound.col2_funnel_bonus", 1.0) * funnel_precol1
        )
        if vt_only:
            bonus += cfg.get("compound.vt_only_bonus", 1.0)
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
                "funnel_precol1": int(funnel_precol1),
                "vt_only_lane": bool(vt_only),
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
