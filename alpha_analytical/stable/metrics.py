from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd


def _digits_only(value: str | int | float | None) -> str:
    if value is None:
        return ""
    return "".join(ch for ch in str(value) if ch.isdigit())


def _canonical(value: str | int | float | None) -> str:
    digits = _digits_only(value)
    return "".join(sorted(digits)) if digits else ""


def _to_int(value: Optional[float | int]) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _to_float(value: float | int | None) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def build_metrics(
    *,
    state: str,
    df_scores: pd.DataFrame,
    families_df: Optional[pd.DataFrame],
    winners: Iterable[str] | None = None,
    top_n_hot: int = 10,
) -> dict:
    """Compute summary metrics for a Stable extractor run."""
    total_patterns = int(df_scores.shape[0]) if df_scores is not None else 0
    families_df = families_df if isinstance(families_df, pd.DataFrame) else pd.DataFrame()
    total_families = int(families_df.shape[0]) if not families_df.empty else 0

    compression_ratio = None
    if total_patterns:
        compression_ratio = round(total_families / total_patterns, 4) if total_patterns else None

    avg_hot_density = None
    if not families_df.empty and "family_score" in families_df and "hot_density" in families_df:
        sorted_families = families_df.sort_values("family_score", ascending=False, ignore_index=True)
        density_series = sorted_families["hot_density"].head(top_n_hot).dropna()
        if not density_series.empty:
            avg_hot_density = round(float(density_series.mean()), 4)

    winners_list = [str(w).strip() for w in (winners or []) if str(w).strip()]

    # Map winner canonicals to family IDs using the highest-scoring matching row.
    detected_winners = []
    winner_family_ids: list[int] = []
    winner_rank_by_family: dict[str, Optional[int]] = {}

    if not df_scores.empty:
        # ensure we have Canonical column for lookups
        score_lookup = df_scores.reset_index(drop=True)
        score_lookup = score_lookup.sort_values("score", ascending=False, ignore_index=True)
        families_rank_map: dict[int, int] = {}
        if not families_df.empty and "family_id" in families_df and "family_score" in families_df:
            ranked = families_df.sort_values("family_score", ascending=False, ignore_index=True)
            families_rank_map = {
                _to_int(row.family_id): idx + 1
                for idx, row in ranked.iterrows()
                if _to_int(row.family_id) is not None
            }

        for winner in winners_list:
            canonical = _canonical(winner)
            if not canonical:
                winner_rank_by_family[winner] = None
                continue
            matches = score_lookup[score_lookup["Canonical"] == canonical]
            if matches.empty:
                winner_rank_by_family[winner] = None
                continue
            detected_winners.append(winner)
            best_row = matches.iloc[0]
            fam_id = _to_int(best_row.get("family_id"))
            if fam_id is not None:
                winner_family_ids.append(fam_id)
                winner_rank_by_family[winner] = families_rank_map.get(fam_id)
            else:
                winner_rank_by_family[winner] = None

    best_straight_rank = None
    if not df_scores.empty and "type" in df_scores.columns:
        sorted_rows = df_scores.sort_values("score", ascending=False, ignore_index=True)
        for idx, row_type in enumerate(sorted_rows["type"].tolist()):
            if str(row_type).lower() == "straight":
                best_straight_rank = idx + 1
                break

    spotlight_rate = None
    if winners_list:
        spotlight_rate = round(len(detected_winners) / len(winners_list), 4)

    metrics = {
        "state": state,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_patterns": total_patterns,
        "total_families": total_families,
        "compression_ratio": compression_ratio,
        "avg_top_hot_density": avg_hot_density,
        "winners": winners_list,
        "winner_family_ids": sorted(set(winner_family_ids)),
        "winner_family_best_rank": {winner: rank for winner, rank in winner_rank_by_family.items()},
        "best_straight_rank": best_straight_rank,
        "spotlight_rate": spotlight_rate,
    }

    return metrics


def write_metrics(out_dir: Path, state: str, metrics: dict) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = out_dir / f"{state}_metrics.json"
    metrics_path.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    return metrics_path
