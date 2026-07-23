#!/usr/bin/env python3
"""Create the cross-window Analysis Arena tune-up diagnostics package."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import iter_window_dates, load_scoreboard, safe_rel
from scripts.tools.brain2_rank_contract import (
    RANK_INTEGRITY_INVALID_STATIC_ORDER,
    analytical_rank,
    rank_evaluation_status,
)


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-root", default=str(DEFAULT_RUNS2_ROOT), help="RUNS_2 root to scan for completed windows.")
    ap.add_argument("--window-root", action="append", default=[], help="Optional explicit window roots. Can be repeated.")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-ranking-csv", default="", help="Optional Brain 2 ranking CSV output path.")
    ap.add_argument("--out-tracker-csv", default="", help="Optional tracker-lift CSV output path.")
    ap.add_argument("--out-doubles-csv", default="", help="Optional doubles subtype CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths() -> Dict[str, Path]:
    base = DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS"
    return {
        "md": base.with_suffix(".md"),
        "json": base.with_suffix(".json"),
        "ranking_csv": DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__BRAIN2_RANKING_DIAGNOSTIC.csv",
        "tracker_csv": DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__TRACKER_LIFT_ROLLUP.csv",
        "doubles_csv": DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__DOUBLES_SUBTYPE_ROLLUP.csv",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _discover_windows(runs2_root: Path) -> List[Path]:
    out: List[Path] = []
    for path in sorted(runs2_root.glob("WINDOW_*")):
        if "__PREALIGN_SNAPSHOT" in path.name:
            continue
        stem = path.name
        required = [
            path / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
            path / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv",
            path / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv",
        ]
        if all(item.exists() for item in required):
            out.append(path)
    return out


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def _as_int(value: Any) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return 0


def _as_float(value: Any) -> float:
    try:
        return float(str(value).strip())
    except Exception:
        return 0.0


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _rate(count: int, den: int) -> float:
    return count / den if den else 0.0


def _write_csv(path: Path, rows: List[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _median(values: Sequence[int]) -> float:
    nums = [int(v) for v in values if int(v) > 0]
    return float(median(nums)) if nums else 0.0


def _rank_band(value: Any) -> str:
    rank = _as_int(value)
    if rank <= 0:
        return "NONE"
    if rank <= 3:
        return "TOP3"
    if rank <= 5:
        return "TOP5"
    if rank <= 10:
        return "TOP10"
    return "TAIL"


def _subset_rows(rows: Sequence[Dict[str, str]], predicate) -> List[Dict[str, str]]:
    return [row for row in rows if predicate(row)]


def _lift_row(signal: str, rows_all: Sequence[Dict[str, str]], subsets: Dict[str, Sequence[Dict[str, str]]], *, predicate) -> Dict[str, Any]:
    overall_hits = sum(1 for row in rows_all if predicate(row))
    overall_rate = _rate(overall_hits, len(rows_all))
    out: Dict[str, Any] = {
        "signal": signal,
        "overall_count": overall_hits,
        "overall_denominator": len(rows_all),
        "overall_rate": overall_rate,
    }
    for label, rows in subsets.items():
        hits = sum(1 for row in rows if predicate(row))
        rate = _rate(hits, len(rows))
        out[f"{label}_count"] = hits
        out[f"{label}_denominator"] = len(rows)
        out[f"{label}_rate"] = rate
        out[f"{label}_lift"] = (rate / overall_rate) if overall_rate else 0.0
    return out


def _window_stem(window_root: Path) -> str:
    return window_root.name


def build_payload(window_roots: Sequence[Path]) -> Dict[str, Any]:
    ranking_state: Dict[str, Dict[str, Any]] = defaultdict(
        lambda: {
            "winner_events": 0,
            "credited_hits": 0,
            "straight_hits": 0,
            "strict_box_hits": 0,
            "vtrac_only_hits": 0,
            "top_primary_days": 0,
            "best_clean_host_days": 0,
            "highest_context_days": 0,
            "top5_board_days": 0,
            "hit_ranks": [],
            "high_conviction_ranks": [],
            "windows": set(),
        }
    )
    tracker_event_rows: List[Dict[str, str]] = []
    tracker_hit_rows: List[Dict[str, str]] = []
    translator_rows: List[Dict[str, str]] = []
    window_summaries: List[Dict[str, Any]] = []
    ranking_contract_rows: List[Dict[str, Any]] = []

    for window_root in window_roots:
        stem = _window_stem(window_root)
        perf_rows = _read_csv_rows(window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv")
        hit_rows = _read_csv_rows(window_root / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv")
        translator_csv_rows = _read_csv_rows(window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv")
        tracker_event_rows.extend(perf_rows)
        tracker_hit_rows.extend(hit_rows)
        translator_rows.extend(translator_csv_rows)

        window_top_primary = Counter()
        for date in iter_window_dates(window_root):
            scoreboard = load_scoreboard(window_root, date)
            verdict = scoreboard.get("board_verdict") or {}
            scoreboard_rows = [
                row for row in (scoreboard.get("scoreboard_rows") or []) if isinstance(row, dict)
            ]
            ranking_contract_rows.extend(scoreboard_rows)
            day_rank_evaluation = rank_evaluation_status(scoreboard_rows)
            top_primary = (
                str(verdict.get("top_primary_target") or "").strip()
                if day_rank_evaluation["evaluable"]
                else ""
            )
            best_clean = (
                str(verdict.get("best_clean_host") or "").strip()
                if day_rank_evaluation["evaluable"]
                else ""
            )
            context = str(verdict.get("highest_context_support_state") or "").strip()
            if top_primary:
                ranking_state[top_primary]["top_primary_days"] += 1
                window_top_primary[top_primary] += 1
                ranking_state[top_primary]["windows"].add(window_root.name)
            if best_clean:
                ranking_state[best_clean]["best_clean_host_days"] += 1
                ranking_state[best_clean]["windows"].add(window_root.name)
            if context:
                ranking_state[context]["highest_context_days"] += 1
                ranking_state[context]["windows"].add(window_root.name)
            for row in scoreboard_rows:
                state_key = str(row.get("state_key") or "").strip()
                rank = analytical_rank(row)
                if state_key and rank is not None and rank <= 5:
                    ranking_state[state_key]["top5_board_days"] += 1
                    ranking_state[state_key]["windows"].add(window_root.name)

        for row in perf_rows:
            state_key = str(row.get("state_key") or "").strip()
            if not state_key:
                continue
            info = ranking_state[state_key]
            info["winner_events"] += 1
            info["windows"].add(window_root.name)
        for row in hit_rows:
            state_key = str(row.get("state_key") or "").strip()
            if not state_key:
                continue
            info = ranking_state[state_key]
            info["credited_hits"] += 1
            if _truthy(row.get("play_straight_hit")):
                info["straight_hits"] += 1
            if _truthy(row.get("play_box_strict_hit")):
                info["strict_box_hits"] += 1
            if str(row.get("hit_primary_class") or "").strip() == "VTRAC_ONLY":
                info["vtrac_only_hits"] += 1
            rank = (
                _as_int(row.get("analytical_rank") or row.get("board_rank"))
                if _truthy(row.get("rank_signal_valid"))
                else 0
            )
            if rank > 0:
                info["hit_ranks"].append(rank)
            if _truthy(row.get("play_straight_hit")) or _truthy(row.get("play_box_strict_hit")):
                if rank > 0:
                    info["high_conviction_ranks"].append(rank)

        window_summaries.append(
            {
                "window": window_root.name.replace("WINDOW_", ""),
                "winner_events": len(perf_rows),
                "credited_hits": len(hit_rows),
                "top_primary_states": dict(window_top_primary.most_common(5)),
            }
        )

    ranking_evaluation = rank_evaluation_status(ranking_contract_rows)
    ranking_rows: List[Dict[str, Any]] = []
    for state_key, info in sorted(ranking_state.items()):
        row = {
            "state_key": state_key,
            "winner_events": info["winner_events"],
            "credited_hits": info["credited_hits"],
            "straight_hits": info["straight_hits"],
            "strict_box_hits": info["strict_box_hits"],
            "vtrac_only_hits": info["vtrac_only_hits"],
            "top_primary_days": info["top_primary_days"] if ranking_evaluation["evaluable"] else None,
            "best_clean_host_days": info["best_clean_host_days"] if ranking_evaluation["evaluable"] else None,
            "highest_context_days": info["highest_context_days"],
            "top5_board_days": info["top5_board_days"] if ranking_evaluation["evaluable"] else None,
            "median_hit_rank": _median(info["hit_ranks"]) if ranking_evaluation["evaluable"] else None,
            "median_high_conviction_rank": (
                _median(info["high_conviction_ranks"]) if ranking_evaluation["evaluable"] else None
            ),
            "high_conviction_hits": info["straight_hits"] + info["strict_box_hits"],
            "top_primary_minus_high_conviction": (
                info["top_primary_days"] - (info["straight_hits"] + info["strict_box_hits"])
                if ranking_evaluation["evaluable"]
                else None
            ),
            "credited_minus_primary": (
                info["credited_hits"] - info["top_primary_days"]
                if ranking_evaluation["evaluable"]
                else None
            ),
            "window_count": len(info["windows"]),
            "rank_integrity_status": (
                "VALID" if ranking_evaluation["evaluable"] else RANK_INTEGRITY_INVALID_STATIC_ORDER
            ),
        }
        ranking_rows.append(row)

    if ranking_evaluation["evaluable"]:
        false_positive_top = sorted(
            [row for row in ranking_rows if row["top_primary_days"] > 0],
            key=lambda row: (-int(row["top_primary_minus_high_conviction"]), -int(row["top_primary_days"]), int(row["credited_hits"])),
        )[:8]
        productive_non_primary = sorted(
            [row for row in ranking_rows if row["credited_hits"] > 0 and row["top_primary_days"] <= 1],
            key=lambda row: (-int(row["credited_hits"]), float(row["median_hit_rank"] or 99.0), row["state_key"]),
        )[:8]
    else:
        false_positive_top = []
        productive_non_primary = []

    event_subsets = {
        "play_box": _subset_rows(tracker_event_rows, lambda row: _truthy(row.get("play_card_any_box"))),
        "play_exact": _subset_rows(tracker_event_rows, lambda row: _truthy(row.get("play_card_any_exact"))),
        "gap_box": _subset_rows(tracker_event_rows, lambda row: _truthy(row.get("opportunity_gap_box"))),
    }
    hit_subsets = {
        "credited": tracker_hit_rows,
        "strict_box": _subset_rows(tracker_hit_rows, lambda row: _truthy(row.get("play_box_strict_hit"))),
        "straight": _subset_rows(tracker_hit_rows, lambda row: _truthy(row.get("play_straight_hit"))),
        "vtrac_only": _subset_rows(tracker_hit_rows, lambda row: str(row.get("hit_primary_class") or "").strip() == "VTRAC_ONLY"),
    }

    event_signals = [
        ("arena_box_signal", lambda row: _truthy(row.get("arena_box_signal"))),
        ("arena_exact_signal", lambda row: _truthy(row.get("arena_exact_signal"))),
        ("arena_primary_box", lambda row: _truthy(row.get("arena_primary_box"))),
        ("arena_primary_vt", lambda row: _truthy(row.get("arena_primary_vt"))),
        ("sandbox_box_seed", lambda row: _truthy(row.get("sandbox_box_seed"))),
        ("sandbox_exact_seed", lambda row: _truthy(row.get("sandbox_exact_seed"))),
        ("sandbox_vt_seed", lambda row: _truthy(row.get("sandbox_vt_seed"))),
        ("preserved_not_budgeted", lambda row: _truthy(row.get("preserved_not_budgeted"))),
        ("profit_alert_support", lambda row: _truthy(row.get("profit_alert_support"))),
        ("compound_event_support", lambda row: _truthy(row.get("compound_event_support"))),
        ("due_double_support", lambda row: _truthy(row.get("due_double_support"))),
        ("blackapple_support", lambda row: _truthy(row.get("blackapple_support"))),
        ("r_consensus_support", lambda row: _truthy(row.get("r_consensus_support"))),
        ("survivor_support", lambda row: _truthy(row.get("survivor_support"))),
    ]
    hit_signals = [
        ("profit_alert_direct_match", lambda row: _truthy(row.get("profit_alert_direct_match"))),
        ("profit_alert_implied_match", lambda row: _truthy(row.get("profit_alert_implied_match"))),
        ("compound_event_present", lambda row: _truthy(row.get("compound_event_present"))),
        ("blackapple_alert", lambda row: str(row.get("blackapple_status") or "").strip().upper() == "ALERT"),
        ("blackapple_watch", lambda row: str(row.get("blackapple_status") or "").strip().upper() == "WATCH"),
        ("due_double_support", lambda row: _truthy(row.get("due_double_support"))),
        ("sandbox_box_seed", lambda row: _truthy(row.get("sandbox_box_seed"))),
        ("sandbox_vt_seed", lambda row: _truthy(row.get("sandbox_vt_seed"))),
        ("arena_box_signal", lambda row: _truthy(row.get("arena_box_signal"))),
        ("arena_exact_signal", lambda row: _truthy(row.get("arena_exact_signal"))),
    ]
    tracker_rows: List[Dict[str, Any]] = []
    for signal, predicate in event_signals:
        row = _lift_row(f"event::{signal}", tracker_event_rows, event_subsets, predicate=predicate)
        tracker_rows.append(row)
    for signal, predicate in hit_signals:
        row = _lift_row(f"hit::{signal}", tracker_hit_rows, hit_subsets, predicate=predicate)
        tracker_rows.append(row)

    doubles_rows: List[Dict[str, Any]] = []
    for label, source_rows in (
        ("all_hits", tracker_hit_rows),
        ("strict_box_hits", hit_subsets["strict_box"]),
        ("straight_hits", hit_subsets["straight"]),
        ("box_gap_rows", _subset_rows(translator_rows, lambda row: "BOX_GAP" in str(row.get("cohort_tags") or ""))),
    ):
        subtype_counter = Counter(str(row.get("inventory_type") or "").strip() or "none" for row in source_rows)
        strength_counter = Counter(str(row.get("double_context_strength") or "").strip() or "NONE" for row in source_rows)
        period_rank_counter = Counter(_rank_band(row.get("due_double_period_rank")) for row in source_rows)
        combined_rank_counter = Counter(_rank_band(row.get("due_double_combined_rank")) for row in source_rows)
        family_rank_counter = Counter(_rank_band(row.get("due_double_family_match_rank")) for row in source_rows)
        for counter_name, counter in (
            ("inventory_type", subtype_counter),
            ("double_context_strength", strength_counter),
            ("period_rank_band", period_rank_counter),
            ("combined_rank_band", combined_rank_counter),
            ("family_match_band", family_rank_counter),
        ):
            for value, count in sorted(counter.items(), key=lambda item: (-int(item[1]), str(item[0]))):
                doubles_rows.append(
                    {
                        "subset": label,
                        "dimension": counter_name,
                        "value": value,
                        "count": count,
                        "rate": _rate(count, len(source_rows)),
                    }
                )

    payload = {
        "metadata": {
            "runs2_root": safe_rel(DEFAULT_RUNS2_ROOT),
            "windows": [safe_rel(path) for path in window_roots],
        },
        "window_summaries": window_summaries,
        "brain2_ranking": {
            **ranking_evaluation,
            "state_rows": ranking_rows,
            "repeated_false_positive_top_states": false_positive_top,
            "productive_non_primary_states": productive_non_primary,
        },
        "tracker_lift": {
            "rows": tracker_rows,
        },
        "doubles_subtype": {
            "rows": doubles_rows,
        },
        "interpretation": [
            (
                "Use the ranking diagnostic to find states the board over-promotes versus states that keep converting without being primary."
                if ranking_evaluation["evaluable"]
                else "Brain 2 cross-state ranking diagnostics are NOT_EVALUABLE because the historical board order is INVALID_STATIC_ORDER; preserve state-level hit facts without rank claims."
            ),
            "Use the tracker-lift tables to separate sharp signals from ambient support before changing Brain 2 weights.",
            "Use the doubles subtype table to learn which double forms matter most before turning 'doubles matter' into a blunt scoring rule.",
        ],
    }
    return payload


def _render_markdown(payload: Dict[str, Any], *, ranking_csv: Path, tracker_csv: Path, doubles_csv: Path) -> str:
    ranking = payload["brain2_ranking"]
    interpretation = payload.get("interpretation") or []
    tracker_rows = payload["tracker_lift"]["rows"]
    doubles_rows = payload["doubles_subtype"]["rows"]

    def top_tracker_rows(prefix: str) -> List[Dict[str, Any]]:
        rows = [row for row in tracker_rows if str(row.get("signal") or "").startswith(prefix)]
        return sorted(rows, key=lambda row: -float(row.get("gap_box_lift", 0.0)))[:6]

    def doubles_subset(subset: str, dimension: str) -> List[Dict[str, Any]]:
        rows = [row for row in doubles_rows if row["subset"] == subset and row["dimension"] == dimension]
        return sorted(rows, key=lambda row: (-int(row["count"]), str(row["value"])))

    lines: List[str] = []
    lines.append("# Analysis Arena Tune-Up Diagnostics")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(f"- Windows reviewed: `{len(payload['metadata']['windows'])}`")
    lines.append(f"- Ranking CSV: `{safe_rel(ranking_csv)}`")
    lines.append(f"- Tracker-lift CSV: `{safe_rel(tracker_csv)}`")
    lines.append(f"- Doubles subtype CSV: `{safe_rel(doubles_csv)}`")
    lines.append("")
    lines.append("## 2. Brain 2 Ranking Diagnostic")
    lines.append("")
    if not ranking.get("evaluable"):
        lines.append("- Status: `NOT_EVALUABLE`")
        lines.append(f"- Reason: `{ranking.get('reason') or RANK_INTEGRITY_INVALID_STATIC_ORDER}`")
        lines.append("- State-level hit and tracker facts remain available; rank-derived over/under-promotion claims are suppressed.")
    else:
        lines.append("- Repeated false-positive top states:")
        for row in ranking["repeated_false_positive_top_states"][:8]:
            lines.append(
                f"  - `{row['state_key']}` top_primary_days=`{row['top_primary_days']}` "
                f"high_conviction_hits=`{row['high_conviction_hits']}` credited_hits=`{row['credited_hits']}` "
                f"median_hit_rank=`{row['median_hit_rank']:.1f}`"
            )
        lines.append("- Productive non-primary states:")
        for row in ranking["productive_non_primary_states"][:8]:
            lines.append(
                f"  - `{row['state_key']}` credited_hits=`{row['credited_hits']}` top_primary_days=`{row['top_primary_days']}` "
                f"strict_box=`{row['strict_box_hits']}` straight=`{row['straight_hits']}` "
                f"median_hit_rank=`{row['median_hit_rank']:.1f}`"
            )
    lines.append("")
    lines.append("## 3. Tracker-Family Lift")
    lines.append("")
    lines.append("- Event-layer signals with strongest gap-box lift:")
    for row in top_tracker_rows("event::"):
        lines.append(
            f"  - `{row['signal']}` overall=`{_pct(float(row['overall_rate']))}` "
            f"gap_box=`{_pct(float(row.get('gap_box_rate', 0.0)))}` "
            f"lift=`{float(row.get('gap_box_lift', 0.0)):.2f}x`"
        )
    lines.append("- Hit-layer signals with strongest strict-box lift:")
    hit_rows = [row for row in tracker_rows if str(row.get("signal") or "").startswith("hit::")]
    for row in sorted(hit_rows, key=lambda row: -float(row.get("strict_box_lift", 0.0)))[:6]:
        lines.append(
            f"  - `{row['signal']}` overall=`{_pct(float(row['overall_rate']))}` "
            f"strict_box=`{_pct(float(row.get('strict_box_rate', 0.0)))}` "
            f"lift=`{float(row.get('strict_box_lift', 0.0)):.2f}x`"
        )
    lines.append("")
    lines.append("## 4. Doubles Subtype Split")
    lines.append("")
    for subset in ("all_hits", "strict_box_hits", "box_gap_rows"):
        rows = doubles_subset(subset, "inventory_type")
        if not rows:
            continue
        lines.append(
            f"- `{subset}` inventory types: "
            + (", ".join(f"`{row['value']}` x{row['count']}" for row in rows) or "_none_")
        )
        strengths = doubles_subset(subset, "double_context_strength")
        lines.append(
            f"- `{subset}` double strength: "
            + (", ".join(f"`{row['value']}` x{row['count']}" for row in strengths) or "_none_")
        )
    lines.append("")
    lines.append("## 5. Practical Read")
    lines.append("")
    for bullet in interpretation:
        lines.append(f"- {bullet}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    defaults = _default_paths()
    runs2_root = _resolve_path(args.runs2_root)
    window_roots = [_resolve_path(value) for value in (args.window_root or [])] or _discover_windows(runs2_root)
    if not window_roots:
        raise SystemExit("No completed windows found for tune-up diagnostics.")

    out_md = _resolve_path(args.out_md) if args.out_md else defaults["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else defaults["json"]
    out_ranking_csv = _resolve_path(args.out_ranking_csv) if args.out_ranking_csv else defaults["ranking_csv"]
    out_tracker_csv = _resolve_path(args.out_tracker_csv) if args.out_tracker_csv else defaults["tracker_csv"]
    out_doubles_csv = _resolve_path(args.out_doubles_csv) if args.out_doubles_csv else defaults["doubles_csv"]

    payload = build_payload(window_roots)
    payload["schema_version"] = "analysis_arena_tuneup_diagnostics/v1"
    payload["ranking_csv"] = safe_rel(out_ranking_csv)
    payload["tracker_csv"] = safe_rel(out_tracker_csv)
    payload["doubles_csv"] = safe_rel(out_doubles_csv)

    _write_csv(out_ranking_csv, payload["brain2_ranking"]["state_rows"], force=args.force)
    _write_csv(out_tracker_csv, payload["tracker_lift"]["rows"], force=args.force)
    _write_csv(out_doubles_csv, payload["doubles_subtype"]["rows"], force=args.force)
    _write_json(out_json, payload, force=args.force)
    _write_text(out_md, _render_markdown(payload, ranking_csv=out_ranking_csv, tracker_csv=out_tracker_csv, doubles_csv=out_doubles_csv), force=args.force)
    print(f"Wrote: {safe_rel(out_ranking_csv)}")
    print(f"Wrote: {safe_rel(out_tracker_csv)}")
    print(f"Wrote: {safe_rel(out_doubles_csv)}")
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
