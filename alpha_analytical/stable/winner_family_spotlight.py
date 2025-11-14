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

    slot_literals = {
        "midday": winners[0] if len(winners) >= 1 else "",
        "evening": winners[1] if len(winners) >= 2 else "",
    }

    def _canon(value: str) -> str:
        digits = stable_module.digits_only(value)
        return stable_module.canon(digits) if digits else ""

    slot_canons = {slot: _canon(value) for slot, value in slot_literals.items() if value}
    slot_family_ids = {
        slot: derive_vtrac_index_for_canonical(canon, get_vtrac_index)
        for slot, canon in slot_canons.items()
        if canon
    }
    target_canons = {c for c in slot_canons.values() if c}
    target_families = {fid for fid in slot_family_ids.values() if fid is not None}

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
        raw["winner_literal_midday"] = slot_literals["midday"]
        raw["winner_literal_evening"] = slot_literals["evening"]
        raw["is_exact_boxed"] = raw["Canonical"].astype(str).isin(target_canons)
        row_types = raw.get("type", pd.Series(dtype=str)).astype(str).str.lower()
        raw["is_exact_straight"] = raw["is_exact_boxed"] & row_types.eq("straight")
        raw["is_vtrac_boxed"] = raw["family_id"].isin(target_families)
    else:
        raw["winner_literal_midday"] = slot_literals["midday"]
        raw["winner_literal_evening"] = slot_literals["evening"]
        raw["is_exact_boxed"] = False
        raw["is_exact_straight"] = False
        raw["is_vtrac_boxed"] = False

    fam = pd.DataFrame()
    if df_families is not None and not df_families.empty:
        fam = df_families[df_families["family_id"].isin(fam_ids)].copy()
        fam["winner_literal_midday"] = slot_literals["midday"]
        fam["winner_literal_evening"] = slot_literals["evening"]
        fam["is_exact_boxed"] = fam["family_id"].isin(target_families)
        fam["is_vtrac_boxed"] = fam["is_exact_boxed"]
        family_exact = {}
        if not raw.empty and "family_id" in raw.columns:
            family_exact = (
                raw.dropna(subset=["family_id"])
                .groupby("family_id")["is_exact_straight"]
                .any()
                .to_dict()
            )
        fam["is_exact_straight"] = fam["family_id"].map(family_exact).fillna(False)
    else:
        fam["winner_literal_midday"] = slot_literals["midday"]
        fam["winner_literal_evening"] = slot_literals["evening"]
        fam["is_exact_boxed"] = False
        fam["is_vtrac_boxed"] = False
        fam["is_exact_straight"] = False

    raw_sorted = raw.sort_values("score", ascending=False, ignore_index=True)
    fam_sorted = fam.sort_values("family_score", ascending=False, ignore_index=True) if not fam.empty else fam
    return raw_sorted, fam_sorted
