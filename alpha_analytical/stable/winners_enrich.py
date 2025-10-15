from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional

import pandas as pd

from alpha_analytical import stable as stable_module
from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index


_WINNER_KEYS = ("Canonical", "Winner", "winner", "Combo", "combo")


def _load_csv(path: Optional[str | Path]) -> pd.DataFrame:
    if not path:
        return pd.DataFrame()
    csv_path = Path(path)
    if not csv_path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(csv_path)
    except Exception:
        return pd.DataFrame()


def _winner_value(row: pd.Series) -> str:
    for key in _WINNER_KEYS:
        if key in row:
            value = row[key]
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def attach_stable_evidence(
    winners: pd.DataFrame,
    *,
    families_path: Optional[str | Path] = None,
    families_df: Optional[pd.DataFrame] = None,
    scores_path: Optional[str | Path] = None,
    scores_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """
    Enrich a winners DataFrame with Stable Pattern evidence.

    The returned DataFrame includes family-level attributes such as `family_score`,
    `family_rank`, `any_doubles_support`, and row-level evidence like `row_score`
    and `row_why`. Missing families or scores gracefully yield NaNs for the
    associated evidence columns.
    """

    winners_df = winners.copy()

    if winners_df.empty:
        return winners_df

    families = families_df.copy() if isinstance(families_df, pd.DataFrame) else _load_csv(families_path)
    scores = scores_df.copy() if isinstance(scores_df, pd.DataFrame) else _load_csv(scores_path)

    if not isinstance(families, pd.DataFrame):
        families = pd.DataFrame()
    if not isinstance(scores, pd.DataFrame):
        scores = pd.DataFrame()

    winners_df["stable_winner"] = winners_df.apply(_winner_value, axis=1)

    def _stable_canon(value: str | int | float | None) -> str:
        if value is None:
            return ""
        digits = stable_module.digits_only(str(value))
        return stable_module.canon(digits) if digits else ""

    winners_df["stable_canonical"] = winners_df["stable_winner"].map(_stable_canon)

    def _family_for(canon: str) -> Optional[int]:
        if not canon:
            return None
        return derive_vtrac_index_for_canonical(canon, get_vtrac_index)

    winners_df["family_id"] = winners_df["stable_canonical"].map(_family_for)

    family_evidence = pd.DataFrame()
    if not families.empty and "family_score" in families.columns:
        fam = families.copy()
        fam = fam.dropna(subset=["family_id", "family_score"])
        fam["family_id"] = fam["family_id"].astype("Int64")
        fam.sort_values("family_score", ascending=False, inplace=True, ignore_index=True)
        fam["family_rank"] = fam["family_score"].rank(method="dense", ascending=False).astype(int)
        family_columns: Iterable[str] = [
            "family_id",
            "family_score",
            "family_rank",
            "section_count",
            "progression_flag",
            "last_remaining_3v",
            "any_doubles_support",
            "hot_density",
            "fam_cov",
            "fam_hpr",
            "fam_perm",
            "fam_repeat",
            "fam_cons",
            "fam_hot",
            "fam_straight2",
            "fam_straight3",
            "fam_doubles",
            "fam_section_bonus",
            "fam_progression_bonus",
            "fam_last_remaining_bonus",
        ]
        available_cols = [col for col in family_columns if col in fam.columns]
        family_evidence = (
            fam.loc[:, available_cols]
            .sort_values(["family_score"], ascending=False, ignore_index=True)
            .drop_duplicates(subset=["family_id"], keep="first")
        )

    row_evidence = pd.DataFrame()
    if not scores.empty and "score" in scores.columns:
        sc = scores.copy()
        sc["stable_canonical"] = sc["Canonical"].map(_stable_canon)
        sc.sort_values("score", ascending=False, inplace=True, ignore_index=True)
        row_columns: Iterable[str] = [
            "stable_canonical",
            "score",
            "type",
            "rows",
            "why",
            "score_cov",
            "score_hpr",
            "score_perm",
            "score_repeat",
            "score_straight",
            "score_single",
            "score_cons",
            "score_hot",
            "score_mirror",
            "score_dom",
            "score_len",
            "score_hidden",
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
        available_cols = [col for col in row_columns if col in sc.columns]
        row_evidence = sc.loc[:, available_cols].drop_duplicates(subset=["stable_canonical"], keep="first")
        row_evidence.rename(
            columns={
                "score": "row_score",
                "type": "row_type",
                "rows": "row_rows",
                "why": "row_why",
            },
            inplace=True,
        )

    enriched = winners_df.merge(family_evidence, on="family_id", how="left")
    enriched = enriched.merge(row_evidence, on="stable_canonical", how="left")

    evidence_order = [
        "family_id",
        "family_score",
        "family_rank",
        "section_count",
        "progression_flag",
        "last_remaining_3v",
        "any_doubles_support",
        "hot_density",
        "fam_doubles",
        "fam_section_bonus",
        "fam_progression_bonus",
        "fam_last_remaining_bonus",
        "row_score",
        "row_type",
        "row_rows",
        "row_why",
        "score_cov",
        "score_hpr",
        "score_perm",
        "score_repeat",
        "score_straight",
        "score_single",
        "score_cons",
        "score_hot",
        "score_mirror",
        "score_dom",
        "score_len",
        "score_hidden",
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
    for col in evidence_order:
        if col not in enriched.columns:
            enriched[col] = pd.NA

    # Ensure canonical helper columns appear at the end
    base_cols = [col for col in enriched.columns if col not in ("stable_winner", "stable_canonical")]
    enriched = enriched[base_cols + ["stable_winner", "stable_canonical"]]

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
            enriched[column] = enriched[column].astype("boolean")

    return enriched
