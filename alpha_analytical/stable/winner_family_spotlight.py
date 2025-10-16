from __future__ import annotations

import pandas as pd

from alpha_analytical import stable as stable_module
from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index
from modules.vtrac_reference import get_index_set


def build_winner_spotlight(
    df_scores: pd.DataFrame,
    df_families: pd.DataFrame,
    winners: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    winners = [str(w).strip() for w in winners if str(w).strip()]
    if not winners or df_scores.empty:
        return pd.DataFrame(), pd.DataFrame()

    def _winner_family_map() -> dict[int, set[str]]:
        mapping: dict[int, set[str]] = {}
        for raw in winners:
            digits = stable_module.digits_only(raw)
            if not digits:
                continue
            canonical = stable_module.canon(digits)
            fam = derive_vtrac_index_for_canonical(canonical, get_vtrac_index)
            if fam is None:
                continue
            mapping.setdefault(int(fam), set()).add(canonical)
        return mapping

    winner_family_canons = _winner_family_map()
    fam_ids = set(winner_family_canons.keys())
    if not fam_ids:
        return pd.DataFrame(), pd.DataFrame()

    def _map_family(canon: str) -> int | None:
        return derive_vtrac_index_for_canonical(str(canon), get_vtrac_index)

    def _family_canonical(family_value: int | float | None) -> str:
        if family_value is None or pd.isna(family_value):
            return ""
        fam_id = int(family_value)
        winner_canons = sorted(winner_family_canons.get(fam_id, []))
        if winner_canons:
            return winner_canons[0]
        combos = sorted(get_index_set(fam_id))
        for combo in combos:
            digits = stable_module.digits_only(combo)
            canonical = stable_module.canon(digits)
            if canonical:
                return canonical
        return ""

    scores = df_scores.copy()
    if "family_id" not in scores.columns or scores["family_id"].isna().all():
        scores["family_id"] = scores["Canonical"].map(_map_family)
    scores = scores.dropna(subset=["family_id"]).copy()
    if scores.empty:
        return pd.DataFrame(), pd.DataFrame()

    scores["family_id"] = scores["family_id"].astype("Int64")
    raw = scores[scores["family_id"].isin(fam_ids)].copy()
    if not raw.empty:
        raw["raw_canonical"] = raw["Canonical"].astype(str)
        raw["family_canonical_3v"] = raw["family_id"].map(_family_canonical)
        if "orders_modal_value" in raw.columns:
            raw["is_exact_straight"] = raw["orders_modal_value"].astype(str).isin(winners)
        else:
            raw["is_exact_straight"] = False

    fam = pd.DataFrame()
    if df_families is not None and not df_families.empty:
        fam = df_families[df_families["family_id"].isin(fam_ids)].copy()

    raw_sorted = raw.sort_values("score", ascending=False, ignore_index=True)
    fam_sorted = fam.sort_values("family_score", ascending=False, ignore_index=True) if not fam.empty else fam
    return raw_sorted, fam_sorted
