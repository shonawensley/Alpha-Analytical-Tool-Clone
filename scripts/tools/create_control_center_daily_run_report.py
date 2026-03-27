#!/usr/bin/env python3
"""
Create an arena-native Control Center daily run report.

This report bridges:
- predictive-day Control Center tables under `sharepacks/_predictive/<D>/control_center`
- post-results evaluation tables under `sharepacks/<D>/control_center` when available
- Brain 2 carry-through recovered from per-state translation sandbox seeds

It does NOT rerun analyzers or rebuild tables.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS2_VALIDATION_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2" / "VALIDATION"
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

CONTROL_CENTER_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_Control_Center_Daily_Template.md"
BRAIN2_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
BRAIN2_MV_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
CONTEXT_FEED_PATH = FINAL_DOCS_DIR / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"
SYSTEM_MAP_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md"
ARENA_CONTRACT_PATH = RUNS_DIR / "2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md"
ARENA_HANDOFF_PATH = RUNS_DIR / "2026-03-16__AUX_CONTROL_CENTER__HANDOFF.md"
ARENA_EXPORT_SLICE_PATH = RUNS_DIR / "2026-03-16__AUX_CONTROL_CENTER__EXPORT_SLICE.md"


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def try_read_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    return read_json(path)


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def safe_int(value: Any) -> int | None:
    try:
        return int(str(value).strip())
    except Exception:
        return None


def safe_float(value: Any) -> float | None:
    try:
        return float(str(value).strip())
    except Exception:
        return None


def normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    return raw.replace(" ", "_")


def _profile_suffix(profile: str) -> str:
    p = str(profile or "mixed").strip()
    return "" if p == "mixed" else f"__{p}"


def _tag_suffix(experiment_tag: str) -> str:
    return f"__{experiment_tag}" if experiment_tag else ""


def _preferred_path(base_dir: Path, stem: str, ext: str, *, profile: str, experiment_tag: str) -> Path:
    out_suffix = _profile_suffix(profile)
    tagged = base_dir / f"{stem}{out_suffix}{_tag_suffix(experiment_tag)}.{ext}"
    if tagged.exists():
        return tagged
    return base_dir / f"{stem}{out_suffix}.{ext}"


def _fmt_path(path: Path) -> str:
    suffix = "" if path.exists() else " (missing)"
    return f"`{safe_rel(path)}`{suffix}"


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        value = str(value or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _fmt_items(values: Sequence[str], *, empty: str = "_none_") -> str:
    items = _ordered_unique(values)
    if not items:
        return empty
    return ", ".join(f"`{item}`" for item in items)


def load_history_date(control_center_dir: Path, *, results_date: str) -> str:
    meta_path = control_center_dir / "meta.json"
    raw = try_read_json(meta_path)
    if isinstance(raw, Mapping):
        history_date = str(raw.get("history_date") or "").strip()
        if history_date:
            return history_date
    return (parse_iso_date(results_date) - timedelta(days=1)).isoformat()


def _board_rows_from_sandbox_seeds(day_dir: Path, *, profile: str, experiment_tag: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for state_dir in sorted([p for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"], key=lambda p: p.name):
        sandbox_path = _preferred_path(
            state_dir / "analysis",
            "translation_sandbox_seed",
            "json",
            profile=profile,
            experiment_tag=experiment_tag,
        )
        seed = try_read_json(sandbox_path)
        if not isinstance(seed, Mapping):
            continue
        brain2 = seed.get("brain2_context") or {}
        if not isinstance(brain2, Mapping):
            continue
        scoreboard = brain2.get("scoreboard_row") or {}
        if not isinstance(scoreboard, Mapping):
            continue
        row = {
            "state_key": state_dir.name,
            "score_rank": safe_int(scoreboard.get("score_rank")) or 9999,
            "role": str(scoreboard.get("role") or "").strip(),
            "bucket": str(scoreboard.get("targeting_bucket") or "").strip(),
            "tracker": str(scoreboard.get("tracker_posture") or "").strip(),
            "top_canonicals": [str(x) for x in (scoreboard.get("top_canonicals") or []) if str(x).strip()],
            "positional_hint": str(scoreboard.get("positional_hint") or "").strip(),
            "profit_alert_hint": str(scoreboard.get("profit_alert_hint") or "").strip(),
            "due_double_hint": str(scoreboard.get("due_double_hint") or "").strip(),
            "blackapple_hint": str(scoreboard.get("blackapple_reco_hint") or "").strip(),
            "survivor_hint": str(scoreboard.get("survivor_hint") or "").strip(),
            "r_consensus_hint": str(scoreboard.get("r_consensus_hint") or "").strip(),
        }
        rows.append(row)
    rows.sort(key=lambda row: (row["score_rank"], row["state_key"]))
    return rows


def _summarize_blackapple(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Rows missing."]
    status_counts: dict[str, int] = {}
    for row in rows:
        status = (row.get("Status") or "").strip() or "?"
        status_counts[status] = status_counts.get(status, 0) + 1
    top_alert = sorted(
        [row for row in rows if (row.get("Status") or "").strip().upper() == "ALERT"],
        key=lambda row: (-(safe_int(row.get("BA-Score")) or -1), row.get("StateKey", ""), row.get("Variant", "")),
    )[:5]
    return [
        f"rows={len(rows)}",
        "status_counts=" + ",".join(f"{k}={v}" for k, v in sorted(status_counts.items())),
        "top_alert=" + "; ".join(
            f"{row.get('StateKey','')}:{row.get('Variant','')}:{row.get('BA-Score','')}:{row.get('Examples','') or '-'}"
            for row in top_alert
        )
        if top_alert
        else "top_alert=-",
    ]


def _summarize_due_doubles(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Rows missing."]
    combined = [row for row in rows if (row.get("Variant") or "").strip() == "Combined"]
    ranked = sorted(
        combined,
        key=lambda row: (-(safe_int(row.get("Draws Since Double")) or -1), row.get("StateKey", "")),
    )[:6]
    return [
        f"rows={len(rows)}",
        f"combined_rows={len(combined)}",
        "top_combined="
        + "; ".join(
            f"{row.get('StateKey','')}:{row.get('Draws Since Double','')}:{row.get('Family 1','').split(':',1)[0]}"
            for row in ranked
        )
        if ranked
        else "top_combined=-",
    ]


def _summarize_vtrac_repeat_watch(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Rows missing."]
    hits = [row for row in rows if (row.get("Current==WinnerVTRAC") or "").strip() == "True"]
    return [
        f"rows={len(rows)}",
        f"current_equals_winner_vtrac={len(hits)}",
        "hit_rows="
        + "; ".join(
            f"{row.get('StateKey','')}:{row.get('Variant','')}:{row.get('Current Index','')}"
            for row in hits[:6]
        )
        if hits
        else "hit_rows=-",
    ]


def _summarize_profit_alerts(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Rows missing."]
    ranked = sorted(
        rows,
        key=lambda row: (-(safe_int(row.get("Strength")) or -1), row.get("StateKey", ""), row.get("Variant", "")),
    )[:8]
    return [
        f"rows={len(rows)}",
        "top_alerts="
        + "; ".join(
            f"{row.get('StateKey','')}:{row.get('Variant','')}:{row.get('AlertId','')}:{row.get('Canonical','')}:{row.get('Suggested','')}"
            for row in ranked
        )
        if ranked
        else "top_alerts=-",
    ]


def _summarize_compound_events(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Rows missing."]
    ranked = sorted(
        rows,
        key=lambda row: (-(safe_int(row.get("priority")) or -1), row.get("state_key", ""), row.get("variant", "")),
    )[:8]
    return [
        f"rows={len(rows)}",
        "top_events="
        + "; ".join(
            f"{row.get('state_key','')}:{row.get('variant','')}:{row.get('top_event','')}:P{row.get('priority','')}"
            for row in ranked
        )
        if ranked
        else "top_events=-",
    ]


def _summarize_profit_eval(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Eval rows missing."]
    hit_decay = sum(1 for row in rows if (row.get("hit_within_decay") or "").strip() == "Y")
    hit_any_decay = sum(1 for row in rows if (row.get("hit_any_within_decay") or "").strip() == "Y")
    return [
        f"rows={len(rows)}",
        f"hit_decay={hit_decay}",
        f"hit_any_decay={hit_any_decay}",
    ]


def _summarize_profit_merged(rows: Sequence[Mapping[str, str]]) -> list[str]:
    if not rows:
        return ["Merged rows missing."]
    hit_decay = sum(1 for row in rows if (row.get("status") or "").strip() == "HIT")
    hit_any_decay = sum(1 for row in rows if (row.get("hit_any_within_decay") or "").strip() == "Y")
    ranked = sorted(
        [row for row in rows if (row.get("status") or "").strip() == "HIT"],
        key=lambda row: (-(safe_int(row.get("strength_max")) or -1), row.get("state_key", "")),
    )[:6]
    return [
        f"rows={len(rows)}",
        f"hit_decay={hit_decay}",
        f"hit_any_decay={hit_any_decay}",
        "top_hits="
        + "; ".join(
            f"{row.get('state_key','')}:{row.get('variant','')}:{row.get('alert_ids','')}:{row.get('promoters','')}"
            for row in ranked
        )
        if ranked
        else "top_hits=-",
    ]


def build_control_center_daily_report(
    *,
    results_date: str,
    profile: str,
    experiment_tag: str,
    predictive_sharepacks_root: Path,
    truth_sharepacks_root: Path,
) -> str:
    predictive_day_dir = predictive_sharepacks_root / results_date
    predictive_cc_dir = predictive_day_dir / "control_center"
    truth_cc_dir = truth_sharepacks_root / results_date / "control_center"
    history_date = load_history_date(predictive_cc_dir, results_date=results_date)
    board_rows = _board_rows_from_sandbox_seeds(
        predictive_day_dir,
        profile=profile,
        experiment_tag=experiment_tag,
    )

    ba_rows = load_csv_rows(predictive_cc_dir / "blackapple_alerts.csv")
    dd_rows = load_csv_rows(predictive_cc_dir / "due_doubles.csv")
    vt_rows = load_csv_rows(predictive_cc_dir / "vtrac_repeat_watch.csv")
    profit_rows = load_csv_rows(predictive_cc_dir / "profit_alerts.csv")
    compound_rows = load_csv_rows(predictive_cc_dir / "profit_compound_events.csv")
    eval_rows = load_csv_rows(truth_cc_dir / "profit_alerts_eval.csv")
    merged_rows = load_csv_rows(truth_cc_dir / "profit_alerts_eval_merged.csv")

    lines: list[str] = []
    lines.append(f"# Analysis Arena Control Center Daily Run Report — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Review the full-day Control Center tables for the Analysis Arena branch from both the predictive-day snapshot and the post-results evaluation side.")
    lines.append("- Surface how Control Center state trackers carried into Brain 2 board posture and translation-sandbox state receipts.")
    lines.append("- This is an arena-native daily report, not the older standalone board shell.")
    lines.append("")
    lines.append("Template / SSOT anchors")
    lines.append(f"- Control Center daily template: {_fmt_path(CONTROL_CENTER_TEMPLATE_PATH)}")
    lines.append(f"- Brain 2 operating template: {_fmt_path(BRAIN2_TEMPLATE_PATH)}")
    lines.append(f"- Brain 2 Master Validation template: {_fmt_path(BRAIN2_MV_TEMPLATE_PATH)}")
    lines.append(f"- Context-tool arena feed: {_fmt_path(CONTEXT_FEED_PATH)}")
    lines.append(f"- Arena system map: {_fmt_path(SYSTEM_MAP_PATH)}")
    lines.append(f"- Aux / Control Center arena contract: {_fmt_path(ARENA_CONTRACT_PATH)}")
    lines.append(f"- Aux / Control Center handoff: {_fmt_path(ARENA_HANDOFF_PATH)}")
    lines.append(f"- Aux / Control Center export slice: {_fmt_path(ARENA_EXPORT_SLICE_PATH)}")
    lines.append("")
    lines.append("## 0) Provenance")
    lines.append(f"- Results date `D`: `{results_date}`")
    lines.append(f"- History date `H`: `{history_date}`")
    lines.append(f"- Predictive sharepacks root: `{safe_rel(predictive_sharepacks_root)}`")
    lines.append(f"- Predictive Control Center dir: `{safe_rel(predictive_cc_dir)}`")
    lines.append(f"- Truth Control Center dir: `{safe_rel(truth_cc_dir)}`")
    lines.append(f"- Profile: `{profile}`")
    lines.append(f"- Experiment tag: `{experiment_tag or 'untagged'}`")
    lines.append("")
    lines.append("## 1) Brain 2 Carry-Through Snapshot")
    lines.append("")
    if board_rows:
        for row in board_rows[:8]:
            hints = " | ".join(
                part
                for part in [
                    row["positional_hint"],
                    row["profit_alert_hint"],
                    row["due_double_hint"],
                    row["blackapple_hint"],
                    row["survivor_hint"],
                    row["r_consensus_hint"],
                ]
                if part
            )
            lines.append(
                f"- **{row['state_key']}**: `#{row['score_rank']}` role=`{row['role'] or '-'}` bucket=`{row['bucket'] or '-'}` tracker=`{row['tracker'] or '-'}` canonicals=`{','.join(row['top_canonicals'][:3]) or '-'}` hints=`{hints or '-'}`"
            )
    else:
        lines.append("- No Brain 2 carry-through rows found in translation sandbox seeds.")
    lines.append("")
    lines.append("## 2) Core Control Center Boards")
    lines.append("")
    lines.append(f"- Blackapple: {_fmt_items(_summarize_blackapple(ba_rows))}")
    lines.append(f"- Due doubles: {_fmt_items(_summarize_due_doubles(dd_rows))}")
    lines.append(f"- VTRAC repeat watch: {_fmt_items(_summarize_vtrac_repeat_watch(vt_rows))}")
    lines.append(f"- Profit alerts: {_fmt_items(_summarize_profit_alerts(profit_rows))}")
    lines.append(f"- Profit compound events: {_fmt_items(_summarize_compound_events(compound_rows))}")
    lines.append("")
    lines.append("## 3) Post-Results Profit Alert Evaluation")
    lines.append("")
    lines.append(f"- Eval CSV: {_fmt_path(truth_cc_dir / 'profit_alerts_eval.csv')}")
    lines.append(f"- Eval merged CSV: {_fmt_path(truth_cc_dir / 'profit_alerts_eval_merged.csv')}")
    lines.append(f"- Eval summary: {_fmt_items(_summarize_profit_eval(eval_rows))}")
    lines.append(f"- Merged summary: {_fmt_items(_summarize_profit_merged(merged_rows))}")
    lines.append("")
    lines.append("## 4) Cross-State Synthesis")
    lines.append("")
    lines.append("- Strongest board-level Control Center carry-through: `...`")
    lines.append("- Strongest tracker-rich state that Brain 2 elevated correctly: `...`")
    lines.append("- Strongest tracker-rich state that still feels underused or overused: `...`")
    lines.append("- How profit alerts / compound events aligned with board posture: `...`")
    lines.append("- Due doubles / mirror-double family notes: `...`")
    lines.append("")
    lines.append("## 5) Fix-Now Vs Fix-Later")
    lines.append("")
    lines.append("- Fix-now: `...`")
    lines.append("- Fix-later: `...`")
    lines.append("- Next run / next window watch item: `...`")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Create an arena-native Control Center daily run report.")
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--predictive-sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--truth-sharepacks-root", default="sharepacks")
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: RUNS_2/VALIDATION/<D>__CONTROL_CENTER.md)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite an existing report.")
    args = ap.parse_args()

    results_date = parse_iso_date(args.date).isoformat()
    predictive_sharepacks_root = Path(args.predictive_sharepacks_root)
    if not predictive_sharepacks_root.is_absolute():
        predictive_sharepacks_root = (REPO_ROOT / predictive_sharepacks_root).resolve()
    truth_sharepacks_root = Path(args.truth_sharepacks_root)
    if not truth_sharepacks_root.is_absolute():
        truth_sharepacks_root = (REPO_ROOT / truth_sharepacks_root).resolve()

    RUNS2_VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else (RUNS2_VALIDATION_DIR / f"{results_date}__CONTROL_CENTER.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Control Center run report already exists: {safe_rel(out_path)} (use --force to overwrite).")

    report = build_control_center_daily_report(
        results_date=results_date,
        profile=str(args.profile or "tool_only").strip(),
        experiment_tag=normalize_tag(args.experiment_tag),
        predictive_sharepacks_root=predictive_sharepacks_root,
        truth_sharepacks_root=truth_sharepacks_root,
    )
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {safe_rel(out_path)}")


if __name__ == "__main__":
    main()
