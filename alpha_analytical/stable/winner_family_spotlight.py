from __future__ import annotations

import pandas as pd

from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index


def build_winner_spotlight(
    df_scores: pd.DataFrame,
    df_families: pd.DataFrame,
    winners: list[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    winners = [str(w).strip() for w in winners if str(w).strip()]
    if not winners or df_scores.empty:
        return pd.DataFrame(), pd.DataFrame()

    vtix = {w: get_vtrac_index(w) for w in winners if len(w) == 3 and w.isdigit()}
    fam_ids = {idx for idx in vtix.values() if idx is not None}
    if not fam_ids:
        return pd.DataFrame(), pd.DataFrame()

    def _map_family(canon: str) -> int | None:
        return derive_vtrac_index_for_canonical(str(canon), get_vtrac_index)

    scores = df_scores.copy()
    scores["family_id"] = scores["Canonical"].map(_map_family)
    raw = scores[scores["family_id"].isin(fam_ids)].copy()
    if not raw.empty:
        raw["is_exact_straight"] = raw["orders_modal_value"].astype(str).isin(winners)

    fam = pd.DataFrame()
    if df_families is not None and not df_families.empty:
        fam = df_families[df_families["family_id"].isin(fam_ids)].copy()

    return raw.sort_values("score", ascending=False), fam.sort_values("family_score", ascending=False)
