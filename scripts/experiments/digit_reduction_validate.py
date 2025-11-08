#!/usr/bin/env python3
"""
Digit-Reduction Analyzer V2 validation helper.

Joins analyzer outputs with known winners and emits:
    reports/DR/<stamp>/digit_reduction_metrics.csv
    reports/DR/<stamp>/digit_reduction_top_misses.csv
    reports/DR/<stamp>/DR_Perf_Summary.md
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import pandas as pd
import re
import yaml


@dataclass
class WinnerRecord:
    date: str
    state: str
    variant: str
    win: str


_VMAP = {"0": "1", "5": "1", "1": "2", "6": "2", "2": "3", "7": "3", "3": "4", "8": "4", "4": "5", "9": "5"}


def _standardize(value: str) -> str:
    return str(value).strip().upper()


def _norm3(value: str) -> str:
    digits = re.sub(r"\D", "", str(value or ""))
    if not digits:
        return ""
    digits = digits[-3:]
    return digits.zfill(3)


def _box_code(value: str) -> str:
    norm = _norm3(value)
    return "".join(sorted(norm)) if norm else ""


def _vtrac_code(value: str) -> str:
    norm = _norm3(value)
    if not norm:
        return ""
    mapped = "".join(_VMAP.get(ch, "") for ch in norm)
    return "".join(sorted(mapped)) if mapped else ""


def _match_row(row: Dict[str, str], win_codes: Dict[str, str], mode: str) -> str:
    exact_candidates = {row.get("value_norm"), row.get("pattern_norm")}
    box_candidates = {row.get("value_box"), row.get("pattern_box")}
    vtrac_candidates = {row.get("value_vtrac"), row.get("pattern_vtrac")}

    if mode in {"exact", "any"}:
        if win_codes["exact"] and win_codes["exact"] in exact_candidates:
            return "exact"
    if mode in {"box", "any"}:
        if win_codes["box"] and win_codes["box"] in (box_candidates | exact_candidates):
            return "box"
    if mode in {"vtrac", "any"}:
        if win_codes["vtrac"] and win_codes["vtrac"] in vtrac_candidates:
            return "vtrac"
    return ""


def load_winners(csv_path: Path, states: Optional[Iterable[str]] = None) -> List[WinnerRecord]:
    df = pd.read_csv(csv_path)
    wanted = {s.upper() for s in states} if states else None
    records: List[WinnerRecord] = []
    for _, row in df.iterrows():
        raw_state = str(row.get("state", "")).strip()
        state_key = raw_state.upper()
        if not raw_state:
            continue
        if wanted and state_key not in wanted:
            continue
        records.append(
            WinnerRecord(
                date=str(row.get("date", "")).strip(),
                state=raw_state,
                variant=_standardize(row.get("variant", "")),
                win=_standardize(row.get("win", "")),
            )
        )
    return records


def _score_field(cfg: Dict[str, any], df: pd.DataFrame) -> str:
    if cfg.get("lockscore", {}).get("enabled") and cfg.get("lockscore", {}).get("use_for_top"):
        if "lockscore_prob" in df.columns:
            return "lockscore_prob"
    if cfg.get("scoring_v2", {}).get("enabled") and cfg.get("scoring_v2", {}).get("use_for_top"):
        if "score_v2" in df.columns:
            return "score_v2"
    if cfg.get("scoring_linear", {}).get("enabled") and cfg.get("scoring_linear", {}).get("use_for_top"):
        if "final_prob" in df.columns:
            return "final_prob"
    return "score"


def _rank_variant(df: pd.DataFrame, score_field: str) -> pd.DataFrame:
    order_cols = [score_field]
    if score_field != "score":
        order_cols.append("score")
    ranked = df.sort_values(by=order_cols, ascending=False, na_position="last").copy()
    ranked["rank"] = range(1, len(ranked) + 1)
    return ranked


def evaluate_state(
    state: str,
    records: List[WinnerRecord],
    analysis_root: Path,
    cfg: Dict[str, any],
    match_mode: str,
) -> List[Dict[str, any]]:
    per_item_path = analysis_root / state / "analyzer_v2" / f"{state}_analyzer_v2_per_item.csv"
    if not per_item_path.exists():
        raise FileNotFoundError(f"Missing analyzer output for {state}: {per_item_path}")
    df = pd.read_csv(per_item_path, dtype=str).fillna("")
    df["section"] = df["section"].astype(str).str.upper()
    df["final_value"] = df["final_value"].astype(str).str.upper()
    df["pattern"] = df["pattern"].astype(str).str.upper()
    df["value_norm"] = df["final_value"].apply(_norm3)
    df["value_box"] = df["final_value"].apply(_box_code)
    df["value_vtrac"] = df["final_value"].apply(_vtrac_code)
    df["pattern_norm"] = df["pattern"].apply(_norm3)
    df["pattern_box"] = df["pattern"].apply(_box_code)
    df["pattern_vtrac"] = df["pattern"].apply(_vtrac_code)

    for col in ("score", "score_v2", "final_prob", "lockscore_prob"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    score_field = _score_field(cfg, df)

    slices: List[Dict[str, any]] = []
    for record in records:
        if record.state != state:
            continue
        win_codes = {
            "exact": _norm3(record.win),
            "box": _box_code(record.win),
            "vtrac": _vtrac_code(record.win),
        }
        variant_df = df[df["section"] == record.variant]
        if variant_df.empty:
            slices.append(
                {
                    "state": state,
                    "variant": record.variant,
                    "date": record.date,
                    "win": record.win,
                    "status": "no_data",
                    "rank": -1,
                }
            )
            continue
        ranked = _rank_variant(variant_df, score_field)
        match_channel = ""
        row_hit = None
        for _, cand in ranked.iterrows():
            channel = _match_row(cand, win_codes, match_mode)
            if channel:
                match_channel = channel
                row_hit = cand
                break
        if row_hit is not None:
            slices.append(
                {
                    "state": state,
                    "variant": record.variant,
                    "date": record.date,
                    "win": record.win,
                    "status": "hit",
                    "rank": int(row_hit["rank"]),
                    "match_channel": match_channel,
                    "score_used": float(row_hit.get(score_field, 0.0) or 0.0),
                    "score_baseline": float(row_hit.get("score", 0.0) or 0.0),
                    "score_v2": row_hit.get("score_v2"),
                    "final_prob": row_hit.get("final_prob"),
                    "lockscore_prob": row_hit.get("lockscore_prob"),
                    "lock_decision": row_hit.get("lock_decision", ""),
                    "cols_hit": row_hit.get("cols_hit"),
                    "earliest_exact_step": row_hit.get("earliest_exact_step"),
                    "vtrac_family": row_hit.get("pattern_vtrac") or row_hit.get("value_vtrac"),
                }
            )
        else:
            leader = ranked.iloc[0]
            slices.append(
                {
                    "state": state,
                    "variant": record.variant,
                    "date": record.date,
                    "win": record.win,
                    "status": "miss",
                    "rank": -1,
                    "top_pattern": leader.get("pattern"),
                    "top_score": float(leader.get(score_field, 0.0) or 0.0),
                    "top_lock": leader.get("lock_decision", ""),
                    "top_vtrac_family": leader.get("pattern_vtrac") or leader.get("value_vtrac"),
                    "lock_decision": "",
                }
            )
    return slices


def summarize(slices: List[Dict[str, any]]) -> pd.DataFrame:
    df = pd.DataFrame(slices)
    grouped = []
    for (state, variant), block in df.groupby(["state", "variant"]):
        total = len(block)
        hits = block[block["rank"] > 0]
        hit1 = (hits["rank"] == 1).sum()
        hit3 = (hits["rank"] <= 3).sum()
        mrr = (1 / hits["rank"]).sum()
        lock_hits = hits[hits["lock_decision"] == "lock"]
        vtrac_hits = hits[hits["match_channel"] == "vtrac"]
        v_hit1 = (vtrac_hits["rank"] == 1).sum()
        v_hit3 = (vtrac_hits["rank"] <= 3).sum()
        grouped.append(
            {
                "state": state,
                "variant": variant,
                "samples": total,
                "hit_at_1": hit1 / total if total else 0.0,
                "hit_at_3": hit3 / total if total else 0.0,
                "mrr": mrr / total if total else 0.0,
                "lock_hit_rate": len(lock_hits) / total if total else 0.0,
                 "hit_at_1_vtrac": v_hit1 / total if total else 0.0,
                 "hit_at_3_vtrac": v_hit3 / total if total else 0.0,
                "misses": int((block["rank"] <= 0).sum()),
            }
        )
    return pd.DataFrame(grouped).sort_values(by=["state", "variant"])


def write_summary_md(path: Path, metrics: pd.DataFrame) -> None:
    lines = ["# Digit-Reduction Performance Summary", ""]
    if metrics.empty:
        lines.append("No samples available.")
    else:
        overall = metrics.mean(numeric_only=True)
        lines.append("## Aggregate")
        lines.append(
            f"- Hit@1: {overall.get('hit_at_1', 0):.2%} · Hit@3: {overall.get('hit_at_3', 0):.2%} · "
            f"Hit@3 (VTRAC): {overall.get('hit_at_3_vtrac', 0):.2%} · MRR: {overall.get('mrr', 0):.3f}"
        )
        lines.append("")
        lines.append("## By State / Variant")
        for _, row in metrics.iterrows():
            lines.append(
                f"- {row['state']} {row['variant']}: Hit@1 {row['hit_at_1']:.0%}, Hit@3 {row['hit_at_3']:.0%}, "
                f"Hit@3 (VTRAC) {row.get('hit_at_3_vtrac', 0):.0%}, MRR {row['mrr']:.2f}, "
                f"Samples {int(row['samples'])}, Misses {int(row['misses'])}"
            )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Digit-Reduction analyzer against winners.")
    parser.add_argument("stamp", help="Stamp/label for the report folder (e.g., 20250617)")
    parser.add_argument("winners_csv", help="CSV containing columns date,state,variant,win")
    parser.add_argument("--analysis-root", default="data/outputs/analysis/digit_reduction")
    parser.add_argument("--states", nargs="*", help="Subset of states to evaluate")
    parser.add_argument("--config", default="alpha_analytical/digit_reduction/analyzer_v2/config.yml")
    parser.add_argument(
        "--match-mode",
        choices=["exact", "box", "vtrac", "any"],
        default="any",
        help="How to count a hit (literal triple, sorted box, VTRAC family, or any).",
    )
    args = parser.parse_args()

    winners = load_winners(Path(args.winners_csv), args.states)
    if not winners:
        raise SystemExit("No winners loaded; aborting.")

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    analysis_root = Path(args.analysis_root)
    slices: List[Dict[str, any]] = []
    for state in sorted({w.state for w in winners}):
        slices.extend(evaluate_state(state, winners, analysis_root, cfg, args.match_mode))

    report_root = Path("reports/DR") / args.stamp
    report_root.mkdir(parents=True, exist_ok=True)

    slices_df = pd.DataFrame(slices)
    slices_df.to_csv(report_root / "digit_reduction_top_misses.csv", index=False)

    metrics_df = summarize(slices)
    metrics_df.to_csv(report_root / "digit_reduction_metrics.csv", index=False)

    write_summary_md(report_root / "DR_Perf_Summary.md", metrics_df)
    print(f"Wrote reports to {report_root}")


if __name__ == "__main__":
    main()
