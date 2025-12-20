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
from modules.vtrac_reference import get_vtrac_index
from src.core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
from src.core.vtrac_family_ranker import rank_double_families

VARIANT_SPECS: List[Tuple[str, str]] = [
    ("Combined", "combined"),
    ("Midday", "midday"),
    ("Evening", "evening"),
]
VARIANT_ORDER = {key: idx for idx, (_, key) in enumerate(VARIANT_SPECS)}
VARIANT_BADGES = {"combined": "C", "midday": "M", "evening": "E"}


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

    artifacts = {
        "blackapple_alerts.csv": _safe_rel(out_dir / "blackapple_alerts.csv"),
        "blackapple_alerts.md": _safe_rel(out_dir / "blackapple_alerts.md"),
        "due_doubles.csv": _safe_rel(out_dir / "due_doubles.csv"),
        "due_doubles.md": _safe_rel(out_dir / "due_doubles.md"),
        "vtrac_repeat_watch.csv": _safe_rel(out_dir / "vtrac_repeat_watch.csv"),
        "vtrac_repeat_watch.md": _safe_rel(out_dir / "vtrac_repeat_watch.md"),
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

    history_date = None
    match = re.search(r"Pick3StatsC4_(\d{4})_(\d{2})_(\d{2})", history_excel_path or "")
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
        "- `control_center_report.md`",
        "- `meta.json`",
        "",
        "## Regenerate",
        f"```bash\npython3 scripts/tools/export_control_center_sharepack.py --date {results_date}\n```",
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
