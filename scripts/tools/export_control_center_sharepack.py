#!/usr/bin/env python3
"""
Export a sharepack-aligned Control Center (Brain-2) bundle for a results date D.

This intentionally reads ONLY from the frozen sharepack day folder to avoid drift:
  - Inputs:  sharepacks/<D>/<STATE>/aux/<STATE>/summary.json
             sharepacks/<D>/<STATE>/aux/draws/*_draws.csv
             data/results/<D>.txt
  - Outputs: sharepacks/<D>/control_center/...

Run:
  python3 scripts/tools/export_control_center_sharepack.py --date 2025-06-21
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from itertools import permutations
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd

from modules.aux_loaders import load_state_draws
from modules.blackapple import ba_status_label
from modules.draw_catalog import draws_since_last_double
from modules.vtrac_reference import INDEX_BY_VTRAC, get_vtrac_index
from modules.vtrac_straight_map import VSTRAIGHTS
from src.core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
from src.core.vtrac_families import COMBO_TO_FAMILY
from src.core.vtrac_family_ranker import rank_double_families

VARIANT_SPECS: List[Tuple[str, str]] = [
    ("Combined", "combined"),
    ("Midday", "midday"),
    ("Evening", "evening"),
]
VARIANT_ORDER = {key: idx for idx, (_, key) in enumerate(VARIANT_SPECS)}
VARIANT_BADGES = {"combined": "C", "midday": "M", "evening": "E"}

_INDEX_TO_VCODE: Dict[int, str] = {}
for _vcode, _idx in INDEX_BY_VTRAC.items():
    _INDEX_TO_VCODE.setdefault(int(_idx), str(_vcode))


def _norm_state(label: str) -> str:
    return "".join(ch for ch in (label or "").lower() if ch.isalpha())


def _canon_draw(draw: str) -> str:
    value = (draw or "").strip()
    if len(value) != 3 or not value.isdigit():
        return ""
    return "".join(sorted(value))


def _parse_results(results_file: Path) -> Dict[str, Dict[str, str]]:
    """Parse data/results/<D>.txt into {norm_state: {"Midday": "123", "Evening": "456"}}."""
    winners: Dict[str, Dict[str, str]] = {}
    with results_file.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh, delimiter="\t")
        for row in reader:
            if not row:
                continue
            state_raw = (row[0] or "").strip()
            if not state_raw or state_raw.lower() == "state":
                continue
            if state_raw.lower() in {"midday", "evening"}:
                continue
            if len(row) < 3:
                continue
            midday = (row[1] or "").strip()
            evening = (row[2] or "").strip()
            entry: Dict[str, str] = {}
            if midday.isdigit() and 1 <= len(midday) <= 3:
                entry["Midday"] = midday.zfill(3)
            if evening.isdigit() and 1 <= len(evening) <= 3:
                entry["Evening"] = evening.zfill(3)
            if entry:
                winners[_norm_state(state_raw)] = entry
    return winners


def _render_ba_triggers(triggers: Dict[str, Any]) -> str:
    if not triggers:
        return "-"
    parts: List[str] = []
    if triggers.get("mirror"):
        parts.append("Mirror")
    roots = triggers.get("root_due") or []
    if roots:
        parts.append("Root " + "/".join(str(r) for r in roots))
    pattern = triggers.get("pattern") or {}
    if pattern.get("extreme_due"):
        parts.append("SSS/TTT")
    if pattern.get("mixed_due"):
        parts.append("SST/STS/TSS")
    floats = triggers.get("floating") or []
    if floats:
        parts.append("Float " + "".join(str(d) for d in floats))
    pairs = triggers.get("pairs") or {}
    remaining = pairs.get("remaining_count")
    if isinstance(remaining, int):
        parts.append(f"Pairs {remaining}")
    return ", ".join(parts) if parts else "-"


def _summarize_hits(combo: str, winners: Dict[str, str]) -> Dict[str, str]:
    summary: Dict[str, str] = {}
    combo = (combo or "").strip()
    if len(combo) != 3 or not combo.isdigit():
        return {k: "-" for k in winners.keys()}
    combo_sorted = "".join(sorted(combo))
    combo_index = get_vtrac_index(combo)
    for period, winner in winners.items():
        winner = (winner or "").strip()
        if len(winner) != 3 or not winner.isdigit():
            summary[period] = "-"
            continue
        flags: List[str] = []
        if combo == winner:
            flags.append("Straight")
        winner_sorted = "".join(sorted(winner))
        if combo_sorted == winner_sorted and combo != winner:
            flags.append("Boxed")
        winner_index = get_vtrac_index(winner)
        if combo_index is not None and winner_index is not None and combo_index == winner_index:
            flags.append("VTRAC")
        summary[period] = ", ".join(flags) if flags else "-"
    return summary


def _aggregate_period_hits(hits: List[Dict[str, str]]) -> Dict[str, str]:
    agg: Dict[str, List[str]] = {}
    for entry in hits:
        for period, label in entry.items():
            if not label or label == "-":
                continue
            agg.setdefault(period, []).append(label)
    return {period: ", ".join(sorted(set(labels))) if labels else "-" for period, labels in agg.items()}


def _render_family_display(entry: dict) -> str:
    label = entry.get("label") or "-"
    members = entry.get("members") or []
    tokens: List[Tuple[str, int, str]] = []
    for member in members:
        combo = member.get("combo")
        severity = member.get("severity") or ""
        variant_key = member.get("variant") or ""
        badge = VARIANT_BADGES.get(variant_key, (variant_key[:1].upper() if variant_key else ""))
        draws_since = int(member.get("draws_since") or 0)
        token = f"{combo}({severity}{badge}:{draws_since})"
        tokens.append((severity, draws_since, token))
    tokens.sort(key=lambda item: (item[0] != "R", -item[1]))
    rendered = " ".join(token for _, _, token in tokens)
    return f"{label}: {rendered}" if rendered else f"{label}: -"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


@dataclass(frozen=True)
class SharepackState:
    state_key: str
    state_dir: Path
    aux_state_label: str
    aux_summary_path: Path
    aux_draws_dir: Path
    excel_path: str
    summary: Dict[str, Any]
    winners: Dict[str, str]


def _discover_states(day_dir: Path) -> List[SharepackState]:
    states: List[SharepackState] = []
    for state_dir in sorted([p for p in day_dir.iterdir() if p.is_dir()]):
        if state_dir.name == "control_center":
            continue
        aux_summary = next(state_dir.glob("aux/*/summary.json"), None)
        aux_draws_dir = state_dir / "aux" / "draws"
        if not aux_summary or not aux_draws_dir.exists():
            continue
        summary = json.loads(aux_summary.read_text(encoding="utf-8"))
        meta = (summary.get("draw_sources") or {}).get("snapshot_meta") or {}
        aux_state_label = meta.get("aux_state_label") or ""
        excel_path = meta.get("excel_path") or ""
        if not aux_state_label or not excel_path:
            continue
        states.append(
            SharepackState(
                state_key=state_dir.name,
                state_dir=state_dir,
                aux_state_label=aux_state_label,
                aux_summary_path=aux_summary,
                aux_draws_dir=aux_draws_dir,
                excel_path=excel_path,
                summary=summary,
                winners={},
            )
        )
    return states


def _write_df_outputs(df: pd.DataFrame, *, csv_path: Path, md_path: Path, title: str) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)

    display = df.copy()
    display = display.fillna("-")
    lines = [f"# {title}", "", f"- Generated: `{datetime.now(timezone.utc).isoformat()}`", ""]
    lines.append("```")
    lines.append(display.to_string(index=False))
    lines.append("```")
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def _build_blackapple_df(states: List[SharepackState]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    for st in states:
        ba = (st.summary.get("blackapple") or {}).get("by_variant") or {}
        for variant_title, variant_key in VARIANT_SPECS:
            analysis = ba.get(variant_key) or {}
            score = int(analysis.get("score") or 0)
            candidates = analysis.get("candidates") or []
            winners_for_variant: Dict[str, str] = {}
            if variant_key == "midday":
                if st.winners.get("Midday"):
                    winners_for_variant = {"Midday": st.winners.get("Midday", "")}
            elif variant_key == "evening":
                if st.winners.get("Evening"):
                    winners_for_variant = {"Evening": st.winners.get("Evening", "")}
            else:
                winners_for_variant = dict(st.winners)

            hits: List[Dict[str, str]] = []
            for cand in candidates:
                combo = cand.get("combo")
                if combo:
                    hits.append(_summarize_hits(combo, winners_for_variant))
            agg_hits = _aggregate_period_hits(hits)

            rows.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": variant_title,
                    "BA-Score": score,
                    "Status": ba_status_label(score),
                    "Triggers": _render_ba_triggers(analysis.get("triggers") or {}),
                    "#Candidates": len(candidates),
                    "Examples": " ".join((c.get("combo") or "") for c in candidates[:3]).strip() or "-",
                    "Winner Midday": st.winners.get("Midday", "-") or "-",
                    "Winner Evening": st.winners.get("Evening", "-") or "-",
                    "Midday Hits": agg_hits.get("Midday", "-"),
                    "Evening Hits": agg_hits.get("Evening", "-"),
                }
            )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["VariantOrder"] = df["Variant"].map(lambda v: VARIANT_ORDER.get(v.lower(), 99) if isinstance(v, str) else 99)
    df.sort_values(["BA-Score", "VariantOrder", "State"], ascending=[False, True, True], inplace=True)
    return df.drop(columns=["VariantOrder"], errors="ignore")


def _build_due_doubles_df(states: List[SharepackState]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    for st in states:
        variant_draws: Dict[str, List[str]] = {}
        for _, variant_key in VARIANT_SPECS:
            draws, _ = load_state_draws(st.state_key, variant=variant_key, base=st.aux_draws_dir, max_n=1000)
            if draws:
                variant_draws[variant_key] = draws
        rankings = (
            rank_double_families(
                variant_draws,
                red_threshold=COMBO_DOUBLE_VERY_LATE,
                blue_threshold=COMBO_DOUBLE_LATE,
                limit=5,
            )
            if variant_draws
            else []
        )
        family_cols = {f"Family {i+1}": (_render_family_display(rankings[i]) if i < len(rankings) else "-") for i in range(5)}
        family_member_combos = {m.get("combo") for r in rankings for m in (r.get("members") or []) if m.get("combo")}
        midday_canon = _canon_draw(st.winners.get("Midday", ""))
        evening_canon = _canon_draw(st.winners.get("Evening", ""))
        for variant_title, variant_key in VARIANT_SPECS:
            draws = variant_draws.get(variant_key) or []
            if not draws:
                continue
            ds, _ = draws_since_last_double(draws)
            rows.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": variant_title,
                    "Draws Since Double": ds,
                    **family_cols,
                    "Winner Midday": st.winners.get("Midday", "-") or "-",
                    "Winner Evening": st.winners.get("Evening", "-") or "-",
                    "Midday Winner In Family": bool(midday_canon and midday_canon in family_member_combos),
                    "Evening Winner In Family": bool(evening_canon and evening_canon in family_member_combos),
                }
            )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["VariantOrder"] = df["Variant"].map(lambda v: VARIANT_ORDER.get(v.lower(), 99) if isinstance(v, str) else 99)
    df.sort_values(["Draws Since Double", "VariantOrder", "State"], ascending=[False, True, True], inplace=True)
    return df.drop(columns=["VariantOrder"], errors="ignore")


def _best_heat_index(heatboard: Dict[str, Dict[str, Any]]) -> Tuple[str | int, float, Optional[float]]:
    best_idx: str | int = "-"
    best_hazard = 0.0
    best_avg_gap: Optional[float] = None
    candidates: List[Tuple[int, Dict[str, Any]]] = []
    for idx_str, metrics in (heatboard or {}).items():
        try:
            idx = int(idx_str)
        except (TypeError, ValueError):
            continue
        if not isinstance(metrics, dict):
            continue
        if not metrics.get("sample_size", 0):
            continue
        candidates.append((idx, metrics))
    if not candidates:
        return best_idx, best_hazard, best_avg_gap
    idx_best, metrics_best = max(
        candidates,
        key=lambda item: (float(item[1].get("hazard", 0.0) or 0.0), int(item[1].get("ds", 0) or 0)),
    )
    best_idx = idx_best
    best_hazard = float(metrics_best.get("hazard", 0.0) or 0.0)
    avg = metrics_best.get("avg_gap")
    best_avg_gap = float(avg) if isinstance(avg, (int, float)) else None
    return best_idx, best_hazard, best_avg_gap


def _build_vtrac_repeat_watch_df(states: List[SharepackState]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    for st in states:
        repeat = st.summary.get("repeat_watch") or {}
        vtrac = st.summary.get("vtrac") or {}
        heat_by_variant = vtrac.get("heatboard_by_variant") or {}
        for variant_title, variant_key in VARIANT_SPECS:
            rep = repeat.get(variant_key) or {}
            heatboard = heat_by_variant.get(variant_key) or {}
            heat_idx, heat_hazard, heat_avg_gap = _best_heat_index(heatboard)
            winner = "-"
            if variant_key == "midday":
                winner = st.winners.get("Midday", "-") or "-"
            elif variant_key == "evening":
                winner = st.winners.get("Evening", "-") or "-"
            winner_index = get_vtrac_index(winner) if winner and winner != "-" else None
            current_index = rep.get("current_index")
            matches = bool(winner_index is not None and current_index is not None and winner_index == current_index)
            rows.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": variant_title,
                    "Current Index": current_index if current_index is not None else "-",
                    "Current Streak": rep.get("current_streak", 0),
                    "Heat Index": heat_idx,
                    "Heat Hazard": round(heat_hazard, 3) if heat_hazard else 0.0,
                    "Heat Avg Gap": round(heat_avg_gap, 1) if heat_avg_gap else "-",
                    "Last Repeat (draws)": rep.get("last_repeat_gap"),
                    "Last Repeat Index": rep.get("last_repeat_index") if rep.get("last_repeat_index") is not None else "-",
                    "Max Streak": rep.get("max_streak", 0),
                    "Window": rep.get("window", 0),
                    "Winner": winner,
                    "Winner VTRAC": winner_index if winner_index is not None else "-",
                    "Current==WinnerVTRAC": matches,
                }
            )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["VariantKey"] = df["Variant"].str.lower()
    df["VariantOrder"] = df["VariantKey"].map(lambda v: VARIANT_ORDER.get(v, 99))
    df.sort_values(
        ["Current Streak", "Last Repeat (draws)", "VariantOrder", "State"],
        ascending=[False, True, True, True],
        inplace=True,
    )
    return df.drop(columns=["VariantKey", "VariantOrder"], errors="ignore")


def _digits_only(value: Any) -> str:
    text = "" if value is None else str(value)
    return "".join(ch for ch in text if ch.isdigit())


def _permutations3(value: Any) -> set[str]:
    digits = _digits_only(value)
    if len(digits) != 3:
        return set()
    return {"".join(p) for p in set(permutations(digits, 3))}


def _vstraights_for_index(index: Any) -> List[str]:
    try:
        idx = int(index)
    except Exception:
        return []
    vcode = _INDEX_TO_VCODE.get(idx)
    if not vcode:
        return []
    return list(VSTRAIGHTS.get(f"v{vcode}", []))


def _vstraights_for_combo(combo: Any) -> List[str]:
    digits = _digits_only(combo)
    if len(digits) != 3:
        return []
    idx = get_vtrac_index(digits)
    if idx is None:
        return []
    return _vstraights_for_index(idx)


def _clamp_vstraights(*, vstraights: List[str], orders_modal_value: Any, clamp_size: int) -> List[str]:
    """
    Deterministic v0 clamp for VSTRAIGHTS lanes.

    Important:
    - This is not claiming to implement the full "allow_p*" clamp math from the Profit spec.
    - It is a safe, auditable clamp rule suitable for Master Validation:
        - STR8_4of8: fix first digit to orders_modal_value[0] (4 combos)
        - STR8_2of8: fix first two digits to orders_modal_value[:2] (2 combos)
        - STR8_1of8: fix all digits to orders_modal_value (1 combo)
    """
    orders = _digits_only(orders_modal_value).zfill(3)
    if len(orders) != 3 or not orders.isdigit():
        return []
    if not vstraights:
        return []

    if clamp_size <= 1:
        return [orders] if orders in vstraights else []

    if clamp_size <= 2:
        prefix = orders[:2]
        return [c for c in vstraights if c.startswith(prefix)]

    if clamp_size <= 4:
        lead = orders[0]
        return [c for c in vstraights if c and c[0] == lead]

    return list(vstraights)


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    text = str(value).strip().lower()
    return text in {"1", "true", "t", "y", "yes"}


def _stable_scores_path(st: SharepackState) -> Path:
    return st.state_dir / "stable" / st.state_key / f"{st.state_key}_stable_patterns_scores.csv"


def _stable_scores_df(st: SharepackState) -> pd.DataFrame:
    path = _stable_scores_path(st)
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(
        path,
        dtype={
            "section": str,
            "Set": str,
            "Draw": str,
            "Column": str,
            "Canonical": str,
            "type": str,
            "rows": str,
            "why": str,
            "orders_modal_value": str,
        },
        keep_default_na=False,
    )


def _rowcov(row: pd.Series) -> int:
    rows = (row.get("rows") or "").strip()
    if not rows:
        return 0
    return len([token for token in rows.split(",") if token.strip()])


def _contains_all_digits(canonical: str, required_digits: str) -> bool:
    canon = _digits_only(canonical)
    return all(d in canon for d in required_digits)


def _build_profit_alerts_df(states: List[SharepackState], *, df_due: pd.DataFrame, df_repeat: pd.DataFrame) -> pd.DataFrame:
    """
    Practical v0 Profit Alerts (A01–A12) exported as a sharepack-aligned board.

    This is intentionally conservative: it emits a small number of alert rows per state/day
    using evidence already present in frozen sharepack artifacts (Stable/DR/Hot Zones/Aux),
    without modifying analyzer logic.
    """

    due_combined = df_due[df_due.get("Variant", "") == "Combined"].copy() if not df_due.empty else pd.DataFrame()
    due_rank: Dict[str, int] = {}
    if not due_combined.empty and "Draws Since Double" in due_combined.columns:
        due_combined["_ds"] = pd.to_numeric(due_combined["Draws Since Double"], errors="coerce").fillna(-1).astype(int)
        due_combined.sort_values(["_ds"], ascending=False, inplace=True, ignore_index=True)
        for idx, row in due_combined.iterrows():
            due_rank[_norm_state(str(row.get("StateKey") or row.get("State") or ""))] = idx + 1

    repeat_index: Dict[Tuple[str, str], Any] = {}
    if not df_repeat.empty:
        for _, row in df_repeat.iterrows():
            state_key = _norm_state(str(row.get("StateKey") or ""))
            variant = str(row.get("Variant") or "")
            repeat_index[(state_key, variant)] = row.get("Current Index")

    rows_out: List[Dict[str, Any]] = []

    for st in states:
        stable = _stable_scores_df(st)
        if stable.empty:
            continue

        stable["_score"] = pd.to_numeric(stable.get("score"), errors="coerce").fillna(0.0)
        stable["_perm"] = pd.to_numeric(stable.get("perm_count_in_box"), errors="coerce").fillna(0).astype(int)
        stable["_hspan"] = pd.to_numeric(stable.get("horizontal_persistence_repeat"), errors="coerce").fillna(0).astype(int)
        stable["_orders_rows"] = pd.to_numeric(stable.get("orders_modal_rows"), errors="coerce").fillna(0).astype(int)
        stable["_set_persist"] = pd.to_numeric(stable.get("persistence_set_count"), errors="coerce").fillna(0).astype(int)
        stable["_cons_stub"] = stable.get("cons_stub", "").map(_truthy) if "cons_stub" in stable.columns else False
        stable["_cons_full"] = stable.get("cons_full", "").map(_truthy) if "cons_full" in stable.columns else False

        ba_by_variant = (st.summary.get("blackapple") or {}).get("by_variant") or {}
        ba_score: Dict[str, int] = {}
        ba_pairs_remaining: Dict[str, Any] = {}
        ba_mirror_latest: Dict[str, bool] = {}
        for variant_title, variant_key in VARIANT_SPECS:
            info = ba_by_variant.get(variant_key) or {}
            score = int(info.get("score") or 0)
            ba_score[variant_title] = score
            trig = info.get("triggers") or {}
            pairs = trig.get("pairs") or {}
            ba_pairs_remaining[variant_title] = pairs.get("remaining_count")
            ba_mirror_latest[variant_title] = bool(trig.get("mirror"))

        # Consensus stubs (tail) live as special rows; derive tail consensus flavors per section/column.
        stub_rows = stable[stable.get("type") == "consensus_stub"].copy()
        stub_rows = stub_rows[stub_rows["Column"].isin(["1", "2"])].copy()

        tail_by_variant_col: Dict[Tuple[str, str], str] = {}
        for _, r in stub_rows.iterrows():
            sec = str(r.get("section") or "")
            col = str(r.get("Column") or "")
            tail = _digits_only(r.get("Canonical"))
            if len(tail) != 2:
                continue
            tail_by_variant_col[(sec, col)] = tail

        # A03 cross-variant tail consensus: same tail pair appears in >=2 sections (any of col1/2).
        tail_to_sections: Dict[Tuple[str, str], set[str]] = {}
        for (sec, col), tail in tail_by_variant_col.items():
            key = ("".join(sorted(tail)), col)
            tail_to_sections.setdefault(key, set()).add(sec)
        best_key: Optional[Tuple[str, str]] = None
        best_sections: set[str] = set()
        for key, sections in tail_to_sections.items():
            if len(sections) > len(best_sections):
                best_key = key
                best_sections = set(sections)
        cross_sections = len(best_sections)
        if best_key is not None and cross_sections >= 2:
            tail_sorted, col = best_key
            rows_out.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": "Combined",
                    "AlertId": "A03",
                    "Strength": 4 if cross_sections == 3 else 3,
                    "Suggested": "OVERLAY",
                    "CapLines": 8,
                    "DecayDraws": 2,
                    "Badges": "CONS/XVAR",
                    "Canonical": "-",
                    "ImpliedSet": "",
                    "Evidence": json.dumps(
                        {
                            "cons_cross_sections": cross_sections,
                            "tail": tail_sorted,
                            "col": col,
                            "sections": sorted(best_sections),
                        },
                        separators=(",", ":"),
                    ),
                    "Winner Midday": st.winners.get("Midday", "-") or "-",
                    "Winner Evening": st.winners.get("Evening", "-") or "-",
                    "Midday Hits": "-",
                    "Evening Hits": "-",
                }
            )

        # Stable candidate helpers (top rows in col1/2 by section).
        cand = stable[stable["Column"].isin(["1", "2"])].copy()
        cand["_rowcov"] = cand.apply(_rowcov, axis=1)
        cand["_canon_digits"] = cand["Canonical"].map(_digits_only)
        cand["_is_pick3"] = cand["_canon_digits"].map(lambda s: len(s) == 3)
        cand["_orders_digits"] = cand["orders_modal_value"].map(_digits_only) if "orders_modal_value" in cand.columns else ""
        cand["_orders_is_pick3"] = cand["_orders_digits"].map(lambda s: len(s) == 3) if "orders_modal_value" in cand.columns else False
        cand["_is_3v"] = cand["_canon_digits"].map(lambda s: len(s) == 3 and len(set(s)) == 3)
        cand["_is_double"] = cand["_canon_digits"].map(lambda s: len(s) == 3 and len(set(s)) == 2)

        def _best_row(mask: pd.Series) -> Optional[pd.Series]:
            subset = cand[mask].copy()
            if subset.empty:
                return None
            subset.sort_values(["_score"], ascending=False, inplace=True, ignore_index=True)
            return subset.iloc[0]

        # A01 / A02: tail consensus in col1/2 + supporting stable row.
        for section_name in ["Midday", "Evening", "Combined"]:
            for col in ["1", "2"]:
                tail = tail_by_variant_col.get((section_name, col))
                if not tail:
                    continue
                tail_digits = "".join(sorted(set(tail)))
                if len(tail_digits) == 2:
                    # A01 dual-tail + 3-value support
                    best = _best_row(
                        (cand["section"] == section_name)
                        & (cand["Column"] == col)
                        & (cand["_is_3v"])
                        & (cand["_rowcov"] >= 3)
                        & (cand["_canon_digits"].map(lambda s, td=tail_digits: _contains_all_digits(s, td)))
                    )
                    if best is not None:
                        ba = ba_score.get(section_name, 0)
                        strength = 4 + (1 if ba >= 3 else 0)
                        implied_box = sorted(_permutations3(best.get("Canonical") or ""))
                        rows_out.append(
                            {
                                "State": st.aux_state_label,
                                "StateKey": st.state_key,
                                "Variant": section_name,
                                "AlertId": "A01",
                                "Strength": min(5, strength),
                                "Suggested": "BOX",
                                "CapLines": 12,
                                "DecayDraws": 3,
                                "Badges": "CONS/3V" + ("/BA" if ba >= 2 else ""),
                                "Canonical": best.get("Canonical") or "-",
                                "ImpliedSet": json.dumps(implied_box, separators=(",", ":")) if implied_box else "",
                                "Evidence": json.dumps(
                                    {
                                        "tail": tail,
                                        "col": col,
                                        "rowcov": int(best.get("_rowcov") or 0),
                                        "perm": int(best.get("_perm") or 0),
                                        "ba_score": ba,
                                    },
                                    separators=(",", ":"),
                                ),
                                "Winner Midday": st.winners.get("Midday", "-") or "-",
                                "Winner Evening": st.winners.get("Evening", "-") or "-",
                                "Midday Hits": "Boxed" if _canon_draw(st.winners.get("Midday", "")) == _canon_draw(best.get("Canonical")) else "-",
                                "Evening Hits": "Boxed" if _canon_draw(st.winners.get("Evening", "")) == _canon_draw(best.get("Canonical")) else "-",
                            }
                        )
                else:
                    # A02 single-tail (double tail) + doubles bias (v0: best double in col1/2)
                    best = _best_row(
                        (cand["section"] == section_name)
                        & (cand["Column"] == col)
                        & (cand["_is_double"])
                        & (cand["_rowcov"] >= 3)
                        & (cand["_canon_digits"].map(lambda s, d=tail_digits: d and d[0] in s))
                    )
                    if best is not None:
                        ba = ba_score.get(section_name, 0)
                        rank = due_rank.get(_norm_state(st.state_key.rstrip("4")), None)
                        strength = 3 + (1 if (rank is not None and rank <= 3) else 0) + (1 if ba >= 3 else 0)
                        implied_str8 = sorted(_permutations3(best.get("Canonical") or ""))
                        rows_out.append(
                            {
                                "State": st.aux_state_label,
                                "StateKey": st.state_key,
                                "Variant": section_name,
                                "AlertId": "A02",
                                "Strength": min(5, strength),
                                "Suggested": "STR8_3",
                                "CapLines": 6,
                                "DecayDraws": 2,
                                "Badges": "CONS/DBL" + ("/A10" if (rank is not None and rank <= 3) else "") + ("/BA" if ba >= 2 else ""),
                                "Canonical": best.get("Canonical") or "-",
                                "ImpliedSet": json.dumps(implied_str8, separators=(",", ":")) if implied_str8 else "",
                                "Evidence": json.dumps(
                                    {
                                        "tail": tail,
                                        "col": col,
                                        "rowcov": int(best.get("_rowcov") or 0),
                                        "perm": int(best.get("_perm") or 0),
                                        "due_doubles_rank": rank,
                                        "ba_score": ba,
                                    },
                                    separators=(",", ":"),
                                ),
                                "Winner Midday": st.winners.get("Midday", "-") or "-",
                                "Winner Evening": st.winners.get("Evening", "-") or "-",
                                "Midday Hits": "Straight"
                                if (st.winners.get("Midday", "") in _permutations3(best.get("Canonical")))
                                else "-",
                                "Evening Hits": "Straight"
                                if (st.winners.get("Evening", "") in _permutations3(best.get("Canonical")))
                                else "-",
                            }
                        )

        # A04: set persistence carry on a 3-value (v0: any canonical with persistence across >=2 sets)
        best_a04 = _best_row(cand["_is_3v"] & (cand["_set_persist"] >= 2) & (cand["_rowcov"] >= 2))
        if best_a04 is not None:
            sec = str(best_a04.get("section") or "Combined")
            ba = ba_score.get(sec, 0)
            implied_box = sorted(_permutations3(best_a04.get("Canonical") or ""))
            rows_out.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": sec,
                    "AlertId": "A04",
                    "Strength": 3 + (1 if ba >= 3 else 0),
                    "Suggested": "BOX",
                    "CapLines": 12,
                    "DecayDraws": 3,
                    "Badges": "PERSIST" + ("/BA" if ba >= 2 else ""),
                    "Canonical": best_a04.get("Canonical") or "-",
                    "ImpliedSet": json.dumps(implied_box, separators=(",", ":")) if implied_box else "",
                    "Evidence": json.dumps(
                        {
                            "persistence_set_count": int(best_a04.get("_set_persist") or 0),
                            "rowcov": int(best_a04.get("_rowcov") or 0),
                            "ba_score": ba,
                        },
                        separators=(",", ":"),
                    ),
                    "Winner Midday": st.winners.get("Midday", "-") or "-",
                    "Winner Evening": st.winners.get("Evening", "-") or "-",
                    "Midday Hits": "Boxed" if _canon_draw(st.winners.get("Midday", "")) == _canon_draw(best_a04.get("Canonical")) else "-",
                    "Evening Hits": "Boxed" if _canon_draw(st.winners.get("Evening", "")) == _canon_draw(best_a04.get("Canonical")) else "-",
                }
            )

        # A05: horizontal straight drift (perm=1 with horiz span >=2).
        best_a05 = _best_row((cand["_perm"] == 1) & (cand["_hspan"] >= 2) & (cand["_rowcov"] >= 2) & (cand["_is_pick3"]) & (cand["_orders_is_pick3"]))
        if best_a05 is not None:
            sec = str(best_a05.get("section") or "Combined")
            suggested = "STR8_8" if bool(best_a05.get("_is_3v")) else "STR8_3"
            orders_modal_value = best_a05.get("orders_modal_value") or ""
            implied_set: List[str] = []
            if suggested == "STR8_8":
                implied_set = _vstraights_for_combo(orders_modal_value)
            else:
                implied_set = sorted(_permutations3(orders_modal_value or best_a05.get("Canonical") or ""))
            rows_out.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": sec,
                    "AlertId": "A05",
                    "Strength": 4,
                    "Suggested": suggested,
                    "CapLines": 8 if bool(best_a05.get("_is_3v")) else 3,
                    "DecayDraws": 2,
                    "Badges": f"PERM/HP{int(best_a05.get('_hspan') or 0)}",
                    "Canonical": best_a05.get("Canonical") or "-",
                    "ImpliedSet": json.dumps(implied_set, separators=(",", ":")) if implied_set else "",
                    "Evidence": json.dumps(
                        {
                            "horiz_span": int(best_a05.get("_hspan") or 0),
                            "orders_modal_value": orders_modal_value,
                            "orders_modal_rows": int(best_a05.get("_orders_rows") or 0),
                            "lane_size": len(implied_set) if implied_set else 0,
                        },
                        separators=(",", ":"),
                    ),
                    "Winner Midday": st.winners.get("Midday", "-") or "-",
                    "Winner Evening": st.winners.get("Evening", "-") or "-",
                    "Midday Hits": "Straight" if (st.winners.get("Midday", "") in implied_set) else "-",
                    "Evening Hits": "Straight" if (st.winners.get("Evening", "") in implied_set) else "-",
                }
            )

        # A08: BA remaining pairs foundation (v0: BA status + pairs remaining count).
        for variant_title, _ in VARIANT_SPECS:
            pr = ba_pairs_remaining.get(variant_title)
            if pr is None:
                continue
            ba = ba_score.get(variant_title, 0)
            if ba >= 2 and int(pr or 0) == 0:
                rows_out.append(
                    {
                        "State": st.aux_state_label,
                        "StateKey": st.state_key,
                        "Variant": variant_title,
                        "AlertId": "A08",
                        "Strength": 3 + (1 if ba >= 3 else 0),
                        "Suggested": "OVERLAY",
                        "CapLines": 0,
                        "DecayDraws": 2,
                        "Badges": "BA/TEMPO",
                        "Canonical": "-",
                        "ImpliedSet": "",
                        "Evidence": json.dumps(
                            {"ba_score": ba, "pairs_remaining": pr, "promoter_only": 1, "requires_base_box": 1},
                            separators=(",", ":"),
                        ),
                        "Winner Midday": st.winners.get("Midday", "-") or "-",
                        "Winner Evening": st.winners.get("Evening", "-") or "-",
                        "Midday Hits": "-",
                        "Evening Hits": "-",
                    }
                )

        # A09: VTRAC repeat risk (v0: current streak >=2).
        rep = st.summary.get("repeat_watch") or {}
        for variant_title, variant_key in VARIANT_SPECS:
            r = rep.get(variant_key) or {}
            if int(r.get("current_streak") or 0) >= 2:
                idx = r.get("current_index")
                implied_set = _vstraights_for_index(idx) if idx is not None else []
                vcode = _INDEX_TO_VCODE.get(int(idx)) if idx is not None else None
                rows_out.append(
                    {
                        "State": st.aux_state_label,
                        "StateKey": st.state_key,
                        "Variant": variant_title,
                        "AlertId": "A09",
                        "Strength": 4,
                        "Suggested": "STR8_8",
                        "CapLines": 8,
                        "DecayDraws": 1,
                        "Badges": "VTRAC/REP",
                        "Canonical": "-",
                        "ImpliedSet": json.dumps(implied_set, separators=(",", ":")) if implied_set else "",
                        "Evidence": json.dumps(
                            {"current_index": idx, "current_streak": r.get("current_streak"), "vcode": f"v{vcode}" if vcode else None, "lane_size": len(implied_set)},
                            separators=(",", ":"),
                        ),
                        "Winner Midday": st.winners.get("Midday", "-") or "-",
                        "Winner Evening": st.winners.get("Evening", "-") or "-",
                        "Midday Hits": "VTRAC" if (variant_key == "midday" and idx is not None and get_vtrac_index(st.winners.get("Midday", "")) == idx) else "-",
                        "Evening Hits": "VTRAC" if (variant_key == "evening" and idx is not None and get_vtrac_index(st.winners.get("Evening", "")) == idx) else "-",
                    }
                )

        # A10: due doubles Top-3 (Combined stream).
        rank = due_rank.get(_norm_state(st.state_key.rstrip("4")), None)
        if rank is not None and rank <= 3:
            draws_combined, _ = load_state_draws(st.state_key, variant="combined", base=st.aux_draws_dir, max_n=2000)
            seen_first: Dict[str, int] = {}
            for i, draw in enumerate(draws_combined):
                canon = _canon_draw(draw)
                if canon and canon not in seen_first:
                    seen_first[canon] = i
            default_gap = len(draws_combined)
            best_due = ""
            best_gap = -1
            for canon in COMBO_TO_FAMILY.keys():
                gap = seen_first.get(canon, default_gap)
                if gap > best_gap:
                    best_due = canon
                    best_gap = gap
            implied_set = sorted(_permutations3(best_due)) if best_due else []
            fam = COMBO_TO_FAMILY.get(best_due) if best_due else None
            rows_out.append(
                {
                    "State": st.aux_state_label,
                    "StateKey": st.state_key,
                    "Variant": "Combined",
                    "AlertId": "A10",
                    "Strength": 4 if rank == 1 else 3,
                    "Suggested": "STR8_3",
                    "CapLines": 3,
                    "DecayDraws": 3,
                    "Badges": f"DBL/RANK{rank}",
                    "Canonical": best_due or "-",
                    "ImpliedSet": json.dumps(implied_set, separators=(",", ":")) if implied_set else "",
                    "Evidence": json.dumps(
                        {
                            "due_doubles_rank": rank,
                            "due_doubles_canonical": best_due or "",
                            "due_doubles_gap": best_gap if best_gap >= 0 else None,
                            "due_doubles_unseen": bool(best_due and best_due not in seen_first),
                            "due_doubles_family": fam.label if fam is not None else None,
                        },
                        separators=(",", ":"),
                    ),
                    "Winner Midday": st.winners.get("Midday", "-") or "-",
                    "Winner Evening": st.winners.get("Evening", "-") or "-",
                    "Midday Hits": "Straight" if (st.winners.get("Midday", "") in implied_set) else "-",
                    "Evening Hits": "Straight" if (st.winners.get("Evening", "") in implied_set) else "-",
                }
            )

        # A12: permutation clamp (order dominance) for non-straights.
        best_a12 = _best_row((cand["_perm"] > 1) & (cand["_rowcov"] >= 3) & (cand["_orders_rows"] > 0) & (cand["_is_pick3"]) & (cand["_orders_is_pick3"]))
        if best_a12 is not None:
            dom = 0.0
            if int(best_a12.get("_rowcov") or 0) > 0:
                dom = float(int(best_a12.get("_orders_rows") or 0)) / float(int(best_a12.get("_rowcov") or 0))
            if dom >= 0.75:
                sec = str(best_a12.get("section") or "Combined")
                orders_modal_value = best_a12.get("orders_modal_value") or ""
                vstraights = _vstraights_for_combo(orders_modal_value)
                implied_set = _clamp_vstraights(vstraights=vstraights, orders_modal_value=orders_modal_value, clamp_size=4)
                if implied_set:
                    rows_out.append(
                        {
                            "State": st.aux_state_label,
                            "StateKey": st.state_key,
                            "Variant": sec,
                            "AlertId": "A12",
                            "Strength": 3 if dom < 0.9 else 4,
                            "Suggested": "STR8_4of8",
                            "CapLines": 5,
                            "DecayDraws": 2,
                            "Badges": "PERM/CLAMP",
                            "Canonical": best_a12.get("Canonical") or "-",
                            "ImpliedSet": json.dumps(implied_set, separators=(",", ":")),
                            "Evidence": json.dumps(
                                {
                                    "order_dominance": round(dom, 3),
                                    "orders_modal_value": orders_modal_value,
                                    "orders_modal_rows": int(best_a12.get("_orders_rows") or 0),
                                    "rowcov": int(best_a12.get("_rowcov") or 0),
                                    "clamp_rule": "STR8_4of8:first_digit",
                                    "lane_size": len(implied_set),
                                },
                                separators=(",", ":"),
                            ),
                            "Winner Midday": st.winners.get("Midday", "-") or "-",
                            "Winner Evening": st.winners.get("Evening", "-") or "-",
                            "Midday Hits": "Straight" if (st.winners.get("Midday", "") in implied_set) else "-",
                            "Evening Hits": "Straight" if (st.winners.get("Evening", "") in implied_set) else "-",
                        }
                    )

        # A06: DR survivor (v0: same 3-value top candidate appears across >=2 variants).
        dr_path = st.state_dir / "digit_reduction" / st.state_key / "analyzer_v2" / f"{st.state_key}_analyzer_v2_top_candidates.csv"
        if dr_path.exists():
            try:
                dr = pd.read_csv(dr_path, dtype={"best_pattern": str, "variant": str}, keep_default_na=False)
                if not dr.empty and "best_pattern" in dr.columns and "variant" in dr.columns:
                    dr["_pattern"] = dr["best_pattern"].map(lambda v: _digits_only(v).zfill(3))
                    dr["_rank"] = pd.to_numeric(dr.get("rank"), errors="coerce").fillna(999).astype(int)
                    dr["_is_3v"] = dr["_pattern"].map(lambda s: len(s) == 3 and len(set(s)) == 3)
                    top = dr[dr["_is_3v"] & (dr["_rank"] <= 5)].copy()
                    if not top.empty:
                        candidates: List[Tuple[int, int, str, List[str]]] = []
                        for pattern, grp in top.groupby("_pattern"):
                            variants = sorted({str(v) for v in grp["variant"].tolist() if v})
                            if len(variants) < 2:
                                continue
                            best_rank = int(grp["_rank"].min())
                            candidates.append((len(variants), best_rank, pattern, variants))
                            if candidates:
                                candidates.sort(key=lambda t: (-t[0], t[1], t[2]))
                                vcount, best_rank, pattern, variants = candidates[0]
                                implied_box = sorted(_permutations3(pattern))
                                rows_out.append(
                                    {
                                        "State": st.aux_state_label,
                                        "StateKey": st.state_key,
                                        "Variant": "Combined",
                                        "AlertId": "A06",
                                        "Strength": 4 if vcount == 3 else 3,
                                        "Suggested": "BOX",
                                        "CapLines": 12,
                                        "DecayDraws": 2,
                                        "Badges": "DR/3V",
                                        "Canonical": pattern,
                                        "ImpliedSet": json.dumps(implied_box, separators=(",", ":")) if implied_box else "",
                                        "Evidence": json.dumps({"dr_survivor_3v": 1, "variants": variants, "best_rank": best_rank}, separators=(",", ":")),
                                        "Winner Midday": st.winners.get("Midday", "-") or "-",
                                        "Winner Evening": st.winners.get("Evening", "-") or "-",
                                        "Midday Hits": "Boxed" if _canon_draw(st.winners.get("Midday", "")) == _canon_draw(pattern) else "-",
                                        "Evening Hits": "Boxed" if _canon_draw(st.winners.get("Evening", "")) == _canon_draw(pattern) else "-",
                                }
                            )
            except Exception:
                pass

        # A07: Mirror echo (v0: BA mirror + mirror-of-last-draw tail appears as tail consensus stub).
        mirror_map = {"0": "5", "5": "0", "1": "6", "6": "1", "2": "7", "7": "2", "3": "8", "8": "3", "4": "9", "9": "4"}
        draws_combined, _ = load_state_draws(st.state_key, variant="combined", base=st.aux_draws_dir, max_n=1)
        last_draw = draws_combined[0] if draws_combined else ""
        if len(last_draw) == 3 and last_draw.isdigit():
            mirror_tail = "".join(mirror_map.get(d, d) for d in last_draw[-2:])
            mirror_tail_key = "".join(sorted(mirror_tail))
            for section_name in ["Midday", "Evening", "Combined"]:
                if not ba_mirror_latest.get(section_name, False):
                    continue
                for col in ["1", "2"]:
                    tail = tail_by_variant_col.get((section_name, col))
                    if not tail:
                        continue
                    if "".join(sorted(tail)) != mirror_tail_key:
                        continue
                    best = _best_row(
                        (cand["section"] == section_name)
                        & (cand["Column"] == col)
                        & (cand["_is_3v"])
                        & (cand["_rowcov"] >= 2)
                        & (cand["_canon_digits"].map(lambda s, td=mirror_tail_key: _contains_all_digits(s, td)))
                    )
                    canon = best.get("Canonical") if best is not None else "-"
                    implied_box = sorted(_permutations3(canon or ""))
                    rows_out.append(
                        {
                            "State": st.aux_state_label,
                            "StateKey": st.state_key,
                            "Variant": section_name,
                            "AlertId": "A07",
                            "Strength": 4,
                            "Suggested": "BOX",
                            "CapLines": 12,
                            "DecayDraws": 2,
                            "Badges": "BA/MIRROR",
                            "Canonical": canon or "-",
                            "ImpliedSet": json.dumps(implied_box, separators=(",", ":")) if implied_box else "",
                            "Evidence": json.dumps(
                                {"ba_mirror_latest": 1, "last_draw": last_draw, "mirror_tail": mirror_tail, "tail": tail, "col": col},
                                separators=(",", ":"),
                            ),
                            "Winner Midday": st.winners.get("Midday", "-") or "-",
                            "Winner Evening": st.winners.get("Evening", "-") or "-",
                            "Midday Hits": "Boxed" if canon and _canon_draw(st.winners.get("Midday", "")) == _canon_draw(canon) else "-",
                            "Evening Hits": "Boxed" if canon and _canon_draw(st.winners.get("Evening", "")) == _canon_draw(canon) else "-",
                        }
                    )

        # A11: Hot-Zone × Consensus overlap (v0: top hot lane in col1/2 + tail consensus stub exists in same column).
        hz_path = st.state_dir / "hot_zones" / st.state_key / f"{st.state_key}_hot_zones_top_lanes.csv"
        if hz_path.exists():
            try:
                hz = pd.read_csv(hz_path, dtype={"triad": str, "evidence_tags": str}, keep_default_na=False, nrows=40)
                if not hz.empty and "evidence_tags" in hz.columns:
                    hz["_score"] = pd.to_numeric(hz.get("score_max"), errors="coerce").fillna(0.0)
                    hz.sort_values(["_score"], ascending=False, inplace=True, ignore_index=True)
                    top = hz.iloc[0]
                    tags = str(top.get("evidence_tags") or "")
                    star_level = 2 if "superhot_set1" in tags else 1
                    score_max = pd.to_numeric(top.get("score_max"), errors="coerce")
                    star_score = float(score_max) if pd.notna(score_max) else 0.0
                    col = "2" if "col2" in tags else ("1" if "col1" in tags else None)
                    if col and tail_by_variant_col.get(("Combined", col)):
                        best = _best_row((cand["section"] == "Combined") & (cand["Column"] == col) & (cand["_is_3v"]) & (cand["_rowcov"] >= 3))
                        canon = best.get("Canonical") if best is not None else "-"
                        triad = _digits_only(top.get("triad")).zfill(3)
                        implied_box = sorted(_permutations3(canon or ""))
                        rows_out.append(
                            {
                                "State": st.aux_state_label,
                                "StateKey": st.state_key,
                                "Variant": "Combined",
                                "AlertId": "A11",
                                "Strength": min(5, 3 + star_level),
                                "Suggested": "BOX",
                                "CapLines": 12,
                                "DecayDraws": 2,
                                "Badges": "HOT/CONS",
                                "Canonical": canon or "-",
                                "ImpliedSet": json.dumps(implied_box, separators=(",", ":")) if implied_box else "",
                                "Evidence": json.dumps(
                                    {
                                        "triad": triad,
                                        "col": col,
                                        "evidence_tags": tags,
                                        "star_level": star_level,
                                        "a11_star_score": round(star_score, 3),
                                    },
                                    separators=(",", ":"),
                                ),
                                "Winner Midday": st.winners.get("Midday", "-") or "-",
                                "Winner Evening": st.winners.get("Evening", "-") or "-",
                                "Midday Hits": "Boxed" if canon and _canon_draw(st.winners.get("Midday", "")) == _canon_draw(canon) else "-",
                                "Evening Hits": "Boxed" if canon and _canon_draw(st.winners.get("Evening", "")) == _canon_draw(canon) else "-",
                            }
                        )
            except Exception:
                pass

    df = pd.DataFrame(rows_out)
    if df.empty:
        return df
    df.sort_values(["AlertId", "Strength", "State", "Variant"], ascending=[True, False, True, True], inplace=True)
    return df


def _write_report(
    *,
    out_dir: Path,
    results_date: str,
    results_file: Path,
    history_excel_path: str,
    state_rows: List[SharepackState],
    artifacts: Dict[str, str],
) -> None:
    lines: List[str] = []
    lines.append(f"# Control Center Export — {results_date}")
    lines.append("")
    lines.append(f"- Generated: `{datetime.now(timezone.utc).isoformat()}`")
    lines.append(f"- Results date (D): `{results_date}`")
    lines.append(f"- Results file: `{_safe_rel(results_file)}`")
    lines.append(f"- History workbook (D-1): `{history_excel_path}`")
    lines.append(f"- States: `{len(state_rows)}`")
    lines.append("")
    lines.append("## Artifacts")
    for label, rel_path in artifacts.items():
        lines.append(f"- {label}: `{rel_path}`")
    lines.append("")
    lines.append("## Notes")
    lines.append("- This export is sharepack-aligned: it reads frozen Aux snapshots under `sharepacks/<D>/<STATE>/aux/...`.")
    lines.append("- It does not depend on Streamlit UI state or live `data/cleaned/*` folders.")
    lines.append("")
    (out_dir / "control_center_report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export sharepack-aligned Control Center (Brain-2) artifacts")
    parser.add_argument("--date", required=True, help="Results date D (sharepacks/<D>/...)")
    parser.add_argument(
        "--results-file",
        default=None,
        help="Path to results file (default: data/results/<D>.txt)",
    )
    parser.add_argument(
        "--sharepacks-root",
        default=str(ROOT / "sharepacks"),
        help="Sharepacks root directory (default: sharepacks/)",
    )
    args = parser.parse_args()

    results_date = args.date.strip()
    sharepacks_root = Path(args.sharepacks_root)
    day_dir = sharepacks_root / results_date
    if not day_dir.exists():
        raise SystemExit(f"Sharepack day folder not found: {day_dir}")

    results_file = Path(args.results_file) if args.results_file else (ROOT / "data" / "results" / f"{results_date}.txt")
    if not results_file.exists():
        raise SystemExit(f"Results file not found: {results_file}")

    winners_by_state = _parse_results(results_file)

    states = _discover_states(day_dir)
    if not states:
        raise SystemExit(f"No sharepack states found under: {day_dir}")

    # Attach winners deterministically via Aux state label.
    enriched: List[SharepackState] = []
    for st in states:
        winners = winners_by_state.get(_norm_state(st.aux_state_label), {})
        enriched.append(
            SharepackState(
                **{**st.__dict__, "winners": winners}  # type: ignore[arg-type]
            )
        )

    excel_paths = sorted({st.excel_path for st in enriched if st.excel_path})
    history_excel_path = excel_paths[0] if excel_paths else "-"

    out_dir = day_dir / "control_center"
    out_dir.mkdir(parents=True, exist_ok=True)

    df_ba = _build_blackapple_df(enriched)
    df_due = _build_due_doubles_df(enriched)
    df_repeat = _build_vtrac_repeat_watch_df(enriched)
    df_profit = _build_profit_alerts_df(enriched, df_due=df_due, df_repeat=df_repeat)

    artifacts = {
        "blackapple_alerts.csv": _safe_rel(out_dir / "blackapple_alerts.csv"),
        "blackapple_alerts.md": _safe_rel(out_dir / "blackapple_alerts.md"),
        "due_doubles.csv": _safe_rel(out_dir / "due_doubles.csv"),
        "due_doubles.md": _safe_rel(out_dir / "due_doubles.md"),
        "vtrac_repeat_watch.csv": _safe_rel(out_dir / "vtrac_repeat_watch.csv"),
        "vtrac_repeat_watch.md": _safe_rel(out_dir / "vtrac_repeat_watch.md"),
        "profit_alerts.csv": _safe_rel(out_dir / "profit_alerts.csv"),
        "profit_alerts.md": _safe_rel(out_dir / "profit_alerts.md"),
        "meta.json": _safe_rel(out_dir / "meta.json"),
        "README.md": _safe_rel(out_dir / "README.md"),
        "control_center_report.md": _safe_rel(out_dir / "control_center_report.md"),
    }

    _write_df_outputs(df_ba, csv_path=out_dir / "blackapple_alerts.csv", md_path=out_dir / "blackapple_alerts.md", title="Blackapple Alerts")
    _write_df_outputs(df_due, csv_path=out_dir / "due_doubles.csv", md_path=out_dir / "due_doubles.md", title="Due Doubles")
    _write_df_outputs(
        df_repeat,
        csv_path=out_dir / "vtrac_repeat_watch.csv",
        md_path=out_dir / "vtrac_repeat_watch.md",
        title="VTRAC Repeat Watch",
    )
    _write_df_outputs(
        df_profit,
        csv_path=out_dir / "profit_alerts.csv",
        md_path=out_dir / "profit_alerts.md",
        title="Profit Alerts (A01–A12)",
    )

    history_date = None
    match = re.search(r"Pick3StatsC4_(\d{4})[-_](\d{2})[-_](\d{2})", history_excel_path or "")
    if match:
        history_date = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

    meta = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "results_date": results_date,
        "results_file": _safe_rel(results_file),
        "history_excel_path": history_excel_path,
        "history_date": history_date,
        "sharepack_day_dir": _safe_rel(day_dir),
        "states": [
            {
                "state_key": st.state_key,
                "aux_state_label": st.aux_state_label,
                "aux_summary": _safe_rel(st.aux_summary_path),
                "aux_draws_dir": _safe_rel(st.aux_draws_dir),
                "winners": st.winners,
            }
            for st in enriched
        ],
        "artifacts": artifacts,
        "script": _safe_rel(Path(__file__).resolve()),
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    readme_lines = [
        f"# Control Center Sharepack Export — {results_date}",
        "",
        f"Evaluating Pick3StatsC4 `D-1={history_date or '?'} -> D={results_date}`",
        "",
        "This folder is the **Brain-2 / Control Center** export for the frozen day sharepack.",
        "",
        "## Inputs (frozen, drift-proof)",
        f"- Results file: `{_safe_rel(results_file)}`",
        f"- History workbook: `{history_excel_path}`",
        "- Per-state Aux summaries: `sharepacks/<D>/<STATE>/aux/<STATE>/summary.json`",
        "- Per-state Aux draw snapshots: `sharepacks/<D>/<STATE>/aux/draws/*_draws.csv`",
        "",
        "## Outputs",
        "- `blackapple_alerts.csv` / `.md`",
        "- `due_doubles.csv` / `.md`",
        "- `vtrac_repeat_watch.csv` / `.md`",
        "- `profit_alerts.csv` / `.md`",
        "- `profit_alerts_eval.csv` / `.md` (optional; windowed evaluation harness)",
        "- `profit_alerts_eval_merged.csv` (optional; deduped play-sets)",
        "- `control_center_report.md`",
        "- `meta.json`",
        "",
        "## Regenerate",
        f"```bash\npython3 scripts/tools/export_control_center_sharepack.py --date {results_date}\n```",
        "",
        "## Evaluate (optional; windowed)",
        f"```bash\npython3 scripts/tools/evaluate_profit_alerts.py --date {results_date}\n```",
        "",
    ]
    (out_dir / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")

    _write_report(
        out_dir=out_dir,
        results_date=results_date,
        results_file=results_file,
        history_excel_path=history_excel_path,
        state_rows=enriched,
        artifacts=artifacts,
    )

    day_readme = day_dir / "README.md"
    if not day_readme.exists():
        day_lines = [
            f"# Sharepacks — {results_date}",
            "",
            f"Evaluating Pick3StatsC4 `D-1={history_date or '?'} -> D={results_date}`",
            "",
            "This folder is the frozen day snapshot used for Master Validation.",
            "",
            "## Contents",
            "- Per-state bundles: `<STATE>/` (Stable, Digit Reduction, VTRAC, Hot Zones, Aux, winners lens, tables/json)",
            "- Global VTRAC day summaries: `summary.md`, `summary.csv`, `vtrac_compact_report.*`",
            "- Brain-2 Control Center export: `control_center/`",
            "",
        ]
        day_readme.write_text("\n".join(day_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
