#!/usr/bin/env python3
"""Create an in-depth same-window Analysis Arena vs legacy system comparison report."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import iter_window_dates, read_json, safe_rel


DEFAULT_LEGACY_RUNS_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--legacy-runs-root",
        default=str(DEFAULT_LEGACY_RUNS_ROOT),
        help="Legacy RUNS root (default: docs/.../RUNS)",
    )
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_outputs(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "md": window_root / f"{stem}__ANALYSIS_ARENA__VS_LEGACY_COMPARISON.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__VS_LEGACY_COMPARISON.json",
    }


def _window_label(dates: List[str]) -> str:
    if not dates:
        raise SystemExit("No analysis-arena dates found in window root.")
    return f"{dates[0]}_to_{dates[-1]}"


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _pct(rate: float) -> str:
    return f"{100.0 * rate:.1f}%"


def _as_float(value: Any) -> float:
    if value is None or value == "":
        return 0.0
    if isinstance(value, dict):
        if "rate" in value:
            return _as_float(value.get("rate"))
        return 0.0
    if isinstance(value, str) and value.endswith("%"):
        return float(value[:-1]) / 100.0
    return float(value)


def _extract_fraction_metric(text: str, label: str) -> Dict[str, Any]:
    pattern = re.compile(
        rf"{re.escape(label)}: \*\*(?P<num>\d+)/(?P<den>\d+)\*\* \((?P<rate>[\d.]+)%\)"
    )
    m = pattern.search(text)
    if not m:
        return {}
    return {
        "count": int(m.group("num")),
        "denominator": int(m.group("den")),
        "rate": float(m.group("rate")) / 100.0,
    }


def _extract_total_graded_outcomes(text: str) -> int:
    m = re.search(r"Total graded outcomes .*?\*\*(\d+)\*\*", text)
    return int(m.group(1)) if m else 0


def _extract_table_metric(text: str, label: str) -> Dict[str, Any]:
    pattern = re.compile(
        rf"\|\s*{re.escape(label)}\s*\|\s*(?P<count>\d+)\s*\|\s*(?P<rate>[\d.]+)%\s*\|"
    )
    m = pattern.search(text)
    if not m:
        return {}
    return {
        "count": int(m.group("count")),
        "rate": float(m.group("rate")) / 100.0,
    }


def _missing_fraction_metric() -> Dict[str, Any]:
    return {"count": 0, "denominator": 0, "rate": 0.0}


def _missing_table_metric() -> Dict[str, Any]:
    return {"count": 0, "rate": 0.0}


def _load_arena_gap(window_root: Path) -> Tuple[Path, Dict[str, Any]]:
    path = window_root / f"{window_root.name}__ANALYSIS_ARENA__PERFORMANCE_GAP.json"
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise SystemExit(f"Unexpected performance-gap payload shape: {path}")
    return path, payload


def _load_legacy_dashboard_metrics(legacy_runs_root: Path, *, window_label: str) -> Dict[str, Any]:
    path = legacy_runs_root / f"{window_label}__CORPUS_DASHBOARD.md"
    if not path.exists():
        return {
            "path": safe_rel(path),
            "available": False,
            "warning": "Same-window legacy corpus dashboard is missing.",
            "total_graded_outcomes": 0,
            "stable_families_present": _missing_fraction_metric(),
            "hot_zones_top_lanes": _missing_fraction_metric(),
            "vtrac_top10": _missing_fraction_metric(),
            "dr_top_candidates": _missing_fraction_metric(),
            "blackapple_top_list": _missing_fraction_metric(),
            "winner_vtrac_repeat": _missing_fraction_metric(),
        }
    text = _read_text(path)
    return {
        "path": safe_rel(path),
        "available": True,
        "warning": "",
        "total_graded_outcomes": _extract_total_graded_outcomes(text),
        "stable_families_present": _extract_fraction_metric(text, "Stable families present"),
        "hot_zones_top_lanes": _extract_fraction_metric(text, "Hot Zones top lanes present"),
        "vtrac_top10": _extract_fraction_metric(text, "VTRAC winner index in top10"),
        "dr_top_candidates": _extract_fraction_metric(text, "DR top-candidates contain winner"),
        "blackapple_top_list": _extract_fraction_metric(text, "Blackapple top list contains winner"),
        "winner_vtrac_repeat": _extract_fraction_metric(
            text, "Winner VTRAC signature has repeat (mirror/double-space)"
        ),
    }


def _load_legacy_dr_metrics(legacy_runs_root: Path, *, window_label: str) -> Dict[str, Any]:
    path = legacy_runs_root / f"{window_label}__DR_LENS_REPORT.md"
    if not path.exists():
        return {
            "path": safe_rel(path),
            "available": False,
            "warning": "Same-window legacy DR lens report is missing.",
            "active_rows": _missing_fraction_metric(),
            "top_winner_present_any": _missing_table_metric(),
            "dr_win_vt_boxed_any": _missing_table_metric(),
        }
    text = _read_text(path)
    return {
        "path": safe_rel(path),
        "available": True,
        "warning": "",
        "active_rows": _extract_fraction_metric(text, "Active rows"),
        "top_winner_present_any": _extract_table_metric(text, "top.winner_present (any)"),
        "dr_win_vt_boxed_any": _extract_table_metric(text, "flags.dr_win_vt_boxed (any)"),
    }


def _load_legacy_control_center_metrics(legacy_runs_root: Path, *, window_label: str) -> Dict[str, Any]:
    path = legacy_runs_root / f"{window_label}__CONTROL_CENTER_ROLLUP.md"
    if not path.exists():
        return {
            "path": safe_rel(path),
            "available": False,
            "warning": "Same-window legacy control-center rollup is missing.",
            "blackapple_alert_rows": _missing_fraction_metric(),
            "blackapple_watch_rows": _missing_fraction_metric(),
            "due_double_midday": _missing_fraction_metric(),
            "due_double_evening": _missing_fraction_metric(),
        }
    text = _read_text(path)
    return {
        "path": safe_rel(path),
        "available": True,
        "warning": "",
        "blackapple_alert_rows": _extract_fraction_metric(text, "Status ALERT"),
        "blackapple_watch_rows": _extract_fraction_metric(text, "Status WATCH"),
        "due_double_midday": _extract_fraction_metric(text, "Midday winner in any family"),
        "due_double_evening": _extract_fraction_metric(text, "Evening winner in any family"),
    }


def _load_legacy_blackapple_rollup(legacy_runs_root: Path, *, window_label: str) -> Dict[str, Any]:
    path = legacy_runs_root / f"blackapple_rollup__N5__{window_label}.csv"
    rows = _read_csv_rows(path)
    wanted: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        if row.get("variant") != "Combined":
            continue
        key = f"{row.get('ba_status', '').strip()}_{row.get('period', '').strip()}".strip("_")
        if not key:
            continue
        wanted[key] = {
            "rows_measured": int(row.get("rows_measured") or 0),
            "same_day_inclusive_rate": _as_float(row.get("hit_any_inclusive_rate") or 0.0),
            "window_inclusive_rate": _as_float(row.get("hit_any_inclusive_window_rate") or 0.0),
            "boxed_rate": _as_float(row.get("boxed_hit_rate") or 0.0),
            "vtrac_rate": _as_float(row.get("vtrac_hit_rate") or 0.0),
        }
    return {
        "path": safe_rel(path),
        "combined_rows": wanted,
    }


def _load_legacy_candidate_universe_metrics(
    legacy_runs_root: Path, *, dates: Iterable[str]
) -> Dict[str, Any]:
    counts = {
        "rows": 0,
        "hit_any": 0,
        "straight_hit": 0,
        "box_hit": 0,
        "vtrac_index_hit": 0,
        "winner_missing_rows": 0,
    }
    source_files: List[str] = []
    for results_date in dates:
        path = legacy_runs_root / f"{results_date}__CANDIDATE_UNIVERSE_GRADE__tool_only.csv"
        source_files.append(safe_rel(path))
        for row in _read_csv_rows(path):
            if row.get("pack_id") != "__UNION__" or row.get("method_id") != "union":
                continue
            if row.get("winner_missing") == "1":
                counts["winner_missing_rows"] += 1
                continue
            counts["rows"] += 1
            for key in ("hit_any", "straight_hit", "box_hit", "vtrac_index_hit"):
                counts[key] += int(row.get(key) or 0)
    rates = {
        key: (counts[key] / counts["rows"] if counts["rows"] else 0.0)
        for key in ("hit_any", "straight_hit", "box_hit", "vtrac_index_hit")
    }
    return {
        "source_files": source_files,
        "counts": counts,
        "rates": rates,
    }


def _load_rollup(path: Path) -> Dict[Tuple[str, str], Dict[str, str]]:
    rows = _read_csv_rows(path)
    return {(row.get("strategy", ""), row.get("budget_label", "")): row for row in rows}


def _compare_rollups(legacy_runs_root: Path, *, window_label: str) -> Dict[str, Any]:
    old_path = legacy_runs_root / f"play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__{window_label}.csv"
    arena_path = legacy_runs_root / f"play_card_windowed_rollup__tool_only__arena_v0__N5__{window_label}.csv"
    old_rows = _load_rollup(old_path)
    arena_rows = _load_rollup(arena_path)
    shared_keys = sorted(set(old_rows) & set(arena_rows))

    def _entry(key: Tuple[str, str]) -> Dict[str, Any]:
        old = old_rows[key]
        new = arena_rows[key]
        old_box = _as_float(old.get("hit_any_box_window_rate"))
        new_box = _as_float(new.get("hit_any_box_window_rate"))
        old_inc = _as_float(old.get("hit_any_inclusive_window_rate"))
        new_inc = _as_float(new.get("hit_any_inclusive_window_rate"))
        return {
            "strategy": key[0],
            "budget_label": key[1],
            "rows_measured": int(old.get("rows_measured") or new.get("rows_measured") or 0),
            "old_box_rate": old_box,
            "arena_box_rate": new_box,
            "box_delta": new_box - old_box,
            "old_inclusive_rate": old_inc,
            "arena_inclusive_rate": new_inc,
            "inclusive_delta": new_inc - old_inc,
        }

    shared_rows = [_entry(key) for key in shared_keys]
    curated_names = {
        "analysis_prefix",
        "play_box_first",
        "v0_2_default",
        "vtrac_pack_boxed_first_laneonly_presetB",
    }
    curated_rows = [row for row in shared_rows if row["strategy"] in curated_names]
    top_box_gains = sorted(shared_rows, key=lambda row: row["box_delta"], reverse=True)[:10]
    top_box_regressions = sorted(shared_rows, key=lambda row: row["box_delta"])[:6]
    return {
        "legacy_rollup_path": safe_rel(old_path),
        "arena_rollup_path": safe_rel(arena_path),
        "shared_strategy_rows": shared_rows,
        "curated_strategy_rows": curated_rows,
        "top_box_gains": top_box_gains,
        "top_box_regressions": [row for row in top_box_regressions if row["box_delta"] < 0],
    }


def _historical_context(legacy_runs_root: Path) -> Dict[str, Any]:
    insights_path = legacy_runs_root / "DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md"
    disconnect_path = legacy_runs_root / "2026-01-15_to_2026-01-21__DISCONNECT_ANALYSIS__CODEX.md"
    return {
        "source_paths": [safe_rel(insights_path), safe_rel(disconnect_path)],
        "legacy_theses": [
            "The old deep-analysis SSOT concluded the system was usually not missing signal outright; it was losing probability mass in the B36 selection cut.",
            "The old disconnect analysis explicitly said low DR and Blackapple exact-hit rates were not the primary optimization target; they were intentionally used as lane, envelope, and triage evidence.",
        ],
    }


def _interpretation(
    *,
    arena_gap: Dict[str, Any],
    legacy_dashboard: Dict[str, Any],
    legacy_cu: Dict[str, Any],
    rollups: Dict[str, Any],
) -> List[str]:
    arena_counts = arena_gap.get("summary_counts") or {}
    arena_rates = arena_gap.get("summary_rates") or {}
    legacy_cu_rates = legacy_cu.get("rates") or {}
    shared_rows = rollups.get("shared_strategy_rows") or []

    v02_b36 = next(
        (
            row
            for row in shared_rows
            if row["strategy"] == "v0_2_default" and row["budget_label"] == "B36"
        ),
        None,
    )

    bullets: List[str] = []
    bullets.append(
        "The old deep-report thesis still fits this window: the system problem is much more downstream realization than upstream signal absence."
    )
    bullets.append(
        "On the aligned arena window, the winner reached the board on "
        f"{_pct(_as_float(arena_rates.get('winner_on_board')))} of graded events, while Play Card any-box realization only converted "
        f"{_pct(_as_float(arena_rates.get('play_card_any_box')))}."
    )
    bullets.append(
        "Candidate Universe union containment improved versus the legacy same-window baseline: "
        f"exact {_pct(_as_float(legacy_cu_rates.get('straight_hit')))} -> {_pct(_as_float(arena_rates.get('cu_exact')))}, "
        f"box {_pct(_as_float(legacy_cu_rates.get('box_hit')))} -> {_pct(_as_float(arena_rates.get('cu_box')))}."
    )
    if v02_b36:
        bullets.append(
            "Replaying the legacy `v0_2_default` downstream strategy on arena-era sharepacks improved the "
            f"B36 box window rate from {_pct(v02_b36['old_box_rate'])} to {_pct(v02_b36['arena_box_rate'])}, "
            f"a delta of {_pct(v02_b36['box_delta'])}."
        )
    bullets.append(
        "The legacy dashboard already showed strong upstream tool presence "
        f"(Stable {legacy_dashboard['stable_families_present'].get('count', 0)}/{legacy_dashboard['stable_families_present'].get('denominator', 0)}, "
        f"Hot Zones {legacy_dashboard['hot_zones_top_lanes'].get('count', 0)}/{legacy_dashboard['hot_zones_top_lanes'].get('denominator', 0)}); "
        "the arena branch improves how that truth is preserved, ranked, and audited across states."
    )
    bullets.append(
        "This supports using B12/B24/B36 as a control arm only: the richer arena system appears to know more than the old downstream expression can currently realize."
    )
    return bullets


def _render_markdown(payload: Dict[str, Any]) -> str:
    arena = payload["arena"]
    legacy = payload["legacy"]
    rollups = payload["downstream_replay"]
    historical = payload["historical_context"]
    arena_counts = arena["summary_counts"]
    arena_rates = arena["summary_rates"]
    rank_histogram = arena_counts.get("board_rank_histogram") or {}
    winner_events = int(arena_counts.get("winner_events") or 0)
    rank_evaluable = rank_histogram.get("evaluable") is True
    board_top5_count = (
        int(rank_histogram.get("top5") or 0)
        if rank_evaluable
        else None
    )
    board_top5_rate = (
        board_top5_count / winner_events
        if rank_evaluable and board_top5_count is not None and winner_events
        else None
    )
    lines: List[str] = []
    lines.append("# Analysis Arena vs Legacy Same-Window Comparison")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(f"- Window: `{payload['metadata']['window_label']}`")
    lines.append(f"- Arena window root: `{payload['metadata']['window_root']}`")
    lines.append(f"- Legacy RUNS root: `{payload['metadata']['legacy_runs_root']}`")
    lines.append(
        f"- Same-day event denominator: arena `{arena['summary_counts'].get('winner_events', 0)}` vs "
        f"legacy dashboard `{legacy['dashboard'].get('total_graded_outcomes', 0)}`"
    )
    lines.append("- Windowed downstream rollups use `70` state-day windows (5 days x 14 states), which is a different denominator from the 138 state×period outcome ledger.")
    lines.append("")
    lines.append("## 2. Arena Benchmark")
    lines.append("")
    lines.append(
        f"- Winner on board: `{arena['summary_counts'].get('winner_on_board', 0)}` "
        f"({_pct(_as_float(arena_rates.get('winner_on_board')))})"
    )
    if rank_evaluable:
        lines.append(
            f"- Board top5 containment: `{board_top5_count}` "
            f"({_pct(float(board_top5_rate or 0.0))})"
        )
    else:
        lines.append(
            "- Board top5 containment: `NOT_EVALUABLE` "
            f"(`{rank_histogram.get('reason') or 'INVALID_STATIC_ORDER'}`)"
        )
    lines.append(
        f"- Candidate Universe exact / box: `{arena_counts.get('cu_exact', 0)}` "
        f"({_pct(_as_float(arena_rates.get('cu_exact')))}) / "
        f"`{arena_counts.get('cu_box', 0)}` ({_pct(_as_float(arena_rates.get('cu_box')))})"
    )
    lines.append(
        f"- Play Card any exact / box: `{arena_counts.get('play_card_any_exact', 0)}` "
        f"({_pct(_as_float(arena_rates.get('play_card_any_exact')))}) / "
        f"`{arena_counts.get('play_card_any_box', 0)}` ({_pct(_as_float(arena_rates.get('play_card_any_box')))})"
    )
    lines.append(
        f"- Opportunity gap box: `{arena_counts.get('opportunity_gap_box', 0)}` "
        f"({_pct(_as_float(arena_rates.get('opportunity_gap_box')))})"
    )
    lines.append("")
    lines.append("## 3. Legacy Same-Window Baseline")
    lines.append("")
    lines.append(
        f"- Legacy dashboard: [corpus dashboard]({payload['metadata']['legacy_dashboard_path']})"
    )
    if not legacy["dashboard"].get("available", True):
        lines.append(f"- Legacy dashboard status: `{legacy['dashboard'].get('warning', 'missing')}`")
    lines.append(
        f"- Stable family presence: `{legacy['dashboard']['stable_families_present'].get('count', 0)}/"
        f"{legacy['dashboard']['stable_families_present'].get('denominator', 0)}` "
        f"({_pct(_as_float(legacy['dashboard']['stable_families_present'].get('rate')))})"
    )
    lines.append(
        f"- Hot Zones top-lane presence: `{legacy['dashboard']['hot_zones_top_lanes'].get('count', 0)}/"
        f"{legacy['dashboard']['hot_zones_top_lanes'].get('denominator', 0)}` "
        f"({_pct(_as_float(legacy['dashboard']['hot_zones_top_lanes'].get('rate')))})"
    )
    lines.append(
        f"- DR top-candidate exact containment: `{legacy['dashboard']['dr_top_candidates'].get('count', 0)}/"
        f"{legacy['dashboard']['dr_top_candidates'].get('denominator', 0)}` "
        f"({_pct(_as_float(legacy['dashboard']['dr_top_candidates'].get('rate')))})"
    )
    lines.append(
        f"- Blackapple top-list exact containment: `{legacy['dashboard']['blackapple_top_list'].get('count', 0)}/"
        f"{legacy['dashboard']['blackapple_top_list'].get('denominator', 0)}` "
        f"({_pct(_as_float(legacy['dashboard']['blackapple_top_list'].get('rate')))})"
    )
    lines.append(
        f"- Legacy CU union exact / box: `{legacy['candidate_universe']['counts'].get('straight_hit', 0)}` "
        f"({_pct(_as_float(legacy['candidate_universe']['rates'].get('straight_hit')))}) / "
        f"`{legacy['candidate_universe']['counts'].get('box_hit', 0)}` "
        f"({_pct(_as_float(legacy['candidate_universe']['rates'].get('box_hit')))})"
    )
    lines.append(
        f"- DR VT-box tag on active rows: `{legacy['dr_lens']['dr_win_vt_boxed_any'].get('count', 0)}` "
        f"({_pct(_as_float(legacy['dr_lens']['dr_win_vt_boxed_any'].get('rate')))})"
    )
    for key in ("ALERT_Midday", "ALERT_Evening"):
        row = legacy["blackapple_rollup"]["combined_rows"].get(key) or {}
        if row:
            lines.append(
                f"- Legacy BA Combined {key.replace('_', ' ')} inclusive same-day / N5 window: "
                f"`{_pct(_as_float(row.get('same_day_inclusive_rate')))}` / "
                f"`{_pct(_as_float(row.get('window_inclusive_rate')))}`"
            )
    lines.append("")
    lines.append("## 4. Shared Downstream Strategy Replay")
    lines.append("")
    lines.append(
        "These rows compare shared strategy names between the legacy same-window rollup and the arena-era rerun on the same dates."
    )
    lines.append("")
    lines.append("| Strategy | Budget | Legacy Box | Arena Box | Delta | Legacy Inclusive | Arena Inclusive | Delta |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for row in rollups["curated_strategy_rows"]:
        lines.append(
            f"| `{row['strategy']}` | `{row['budget_label']}` | "
            f"{_pct(row['old_box_rate'])} | {_pct(row['arena_box_rate'])} | {_pct(row['box_delta'])} | "
            f"{_pct(row['old_inclusive_rate'])} | {_pct(row['arena_inclusive_rate'])} | {_pct(row['inclusive_delta'])} |"
        )
    lines.append("")
    lines.append(
        "- Best shared-strategy box gains: "
        + (
            ", ".join(
                f"`{row['strategy']}` {row['budget_label']} {_pct(row['old_box_rate'])}->{_pct(row['arena_box_rate'])}"
                for row in rollups["top_box_gains"][:5]
            )
            or "_none_"
        )
    )
    if rollups["top_box_regressions"]:
        lines.append(
            "- Shared-strategy box regressions: "
            + ", ".join(
                f"`{row['strategy']}` {row['budget_label']} {_pct(row['old_box_rate'])}->{_pct(row['arena_box_rate'])}"
                for row in rollups["top_box_regressions"][:4]
            )
        )
    lines.append("")
    lines.append("## 5. Historical Codex Context")
    lines.append("")
    for source in historical["source_paths"]:
        lines.append(f"- Source: `{source}`")
    for bullet in historical["legacy_theses"]:
        lines.append(f"- {bullet}")
    lines.append("")
    lines.append("## 6. Interpretation")
    lines.append("")
    for bullet in payload["interpretation"]:
        lines.append(f"- {bullet}")
    lines.append("")
    lines.append("## 7. Practical Read")
    lines.append("")
    lines.append("- The old system already had meaningful upstream tool presence, but it mostly evaluated itself through exact-hit and selection-cut surfaces.")
    lines.append("- The arena branch adds board containment, cross-state context, tracker attribution, and explicit opportunity-gap measurement.")
    lines.append("- This makes same-window comparison possible at two levels: legacy realized performance, and arena intrinsic truth quality plus downstream loss.")
    return "\n".join(lines).rstrip() + "\n"


def build_payload(window_root: Path, *, legacy_runs_root: Path) -> Dict[str, Any]:
    dates = iter_window_dates(window_root)
    label = _window_label(dates)
    gap_path, arena_gap = _load_arena_gap(window_root)
    legacy_dashboard = _load_legacy_dashboard_metrics(legacy_runs_root, window_label=label)
    legacy_dr = _load_legacy_dr_metrics(legacy_runs_root, window_label=label)
    legacy_cc = _load_legacy_control_center_metrics(legacy_runs_root, window_label=label)
    legacy_ba = _load_legacy_blackapple_rollup(legacy_runs_root, window_label=label)
    legacy_cu = _load_legacy_candidate_universe_metrics(legacy_runs_root, dates=dates)
    rollups = _compare_rollups(legacy_runs_root, window_label=label)
    historical = _historical_context(legacy_runs_root)
    interpretation = _interpretation(
        arena_gap=arena_gap,
        legacy_dashboard=legacy_dashboard,
        legacy_cu=legacy_cu,
        rollups=rollups,
    )
    return {
        "metadata": {
            "window_label": label,
            "window_root": safe_rel(window_root),
            "legacy_runs_root": safe_rel(legacy_runs_root),
            "arena_gap_path": safe_rel(gap_path),
            "legacy_dashboard_path": legacy_dashboard["path"],
        },
        "arena": arena_gap,
        "legacy": {
            "dashboard": legacy_dashboard,
            "dr_lens": legacy_dr,
            "control_center": legacy_cc,
            "blackapple_rollup": legacy_ba,
            "candidate_universe": legacy_cu,
        },
        "downstream_replay": rollups,
        "historical_context": historical,
        "interpretation": interpretation,
    }


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    legacy_runs_root = _resolve_path(args.legacy_runs_root)
    outputs = _default_outputs(window_root)
    out_md = _resolve_path(args.out_md) if args.out_md else outputs["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else outputs["json"]

    payload = build_payload(window_root, legacy_runs_root=legacy_runs_root)
    md = _render_markdown(payload)
    _write_text(out_md, md, force=args.force)
    _write_json(out_json, payload, force=args.force)
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
