#!/usr/bin/env python3
"""Create an Analysis Arena window performance / opportunity gap report."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import (
    REPO_ROOT as UTILS_REPO_ROOT,
    WinnerEvent,
    analysis_dir,
    diagnostic_membership,
    dominant_box_signal,
    exact_signal,
    extract_candidate_universe_metrics,
    iter_window_dates,
    load_scoreboard,
    load_shadow,
    load_state_seed_from_manifest_entry,
    load_translation_manifest,
    read_json,
    safe_rel,
    validation_dir,
    winner_events_for_state,
    winners_for_date,
)


DEFAULT_RESULTS_ROOT = REPO_ROOT / "data" / "results"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--results-root",
        default=str(DEFAULT_RESULTS_ROOT),
        help="Results truth root (default: data/results)",
    )
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-ledger", default="", help="Optional CSV ledger output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _window_root_from_arg(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_output_paths(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "md": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
        "ledger": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
    }


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _inventory_rows(window_root: Path) -> List[Dict[str, str]]:
    matches = sorted(validation_dir(window_root).glob("*__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"))
    return _read_csv_rows(matches[0]) if matches else []


def _inventory_map(window_root: Path) -> Dict[tuple[str, str, str, str], Dict[str, str]]:
    out: Dict[tuple[str, str, str, str], Dict[str, str]] = {}
    for row in _inventory_rows(window_root):
        key = (
            row.get("date", "").strip(),
            row.get("state", "").strip(),
            row.get("period", "").strip(),
            row.get("winner", "").strip(),
        )
        if all(key):
            out[key] = row
    return out


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


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


def _pct(num: int, den: int) -> str:
    if den <= 0:
        return "0.0%"
    return f"{(100.0 * num / den):.1f}%"


def _hint_present(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    text = str(value or "").strip()
    if not text:
        return False
    return text.lower() not in {"-", "_none_", "none", "n/a", "na"}


def _maybe_load_json(rel_path: str) -> Dict[str, Any]:
    if not rel_path:
        return {}
    path = (UTILS_REPO_ROOT / rel_path).resolve()
    if not path.exists():
        return {}
    raw = read_json(path)
    return raw if isinstance(raw, dict) else {}


def _extract_play_card_metrics_all_strategies(play_card: Dict[str, Any], winner: WinnerEvent) -> Dict[str, bool]:
    out: Dict[str, bool] = {
        "play_card_any_exact": False,
        "play_card_any_box": False,
    }
    for budget in ("B12", "B24", "B36"):
        out[f"{budget.lower()}_exact"] = False
        out[f"{budget.lower()}_box"] = False
    strategies = play_card.get("strategies") or {}
    if not isinstance(strategies, dict):
        return out
    for strategy in strategies.values():
        if not isinstance(strategy, dict):
            continue
        for budget in ("B12", "B24", "B36"):
            pack = strategy.get(budget) or {}
            if not isinstance(pack, dict):
                continue
            combos = {str(v).strip() for v in (pack.get("combos") or []) if str(v).strip()}
            boxed = {str(v).strip() for v in (pack.get("boxed_canonicals") or []) if str(v).strip()}
            exact = winner.literal in combos
            box = winner.canonical in boxed
            out[f"{budget.lower()}_exact"] = out[f"{budget.lower()}_exact"] or exact
            out[f"{budget.lower()}_box"] = out[f"{budget.lower()}_box"] or box
            out["play_card_any_exact"] = out["play_card_any_exact"] or exact
            out["play_card_any_box"] = out["play_card_any_box"] or box
    return out


def _seed_signal_lists(seed: Dict[str, Any]) -> Dict[str, List[str]]:
    sandbox = seed.get("sandbox_hypotheses") or {}
    control_arm = seed.get("control_arm") or {}
    return {
        "boxed": [
            str(item.get("value")).strip()
            for item in (sandbox.get("diagnostic_boxed_seed") or [])
            if isinstance(item, dict) and str(item.get("value")).strip()
        ],
        "straight": [
            str(item.get("value")).strip()
            for item in (sandbox.get("diagnostic_straight_seed") or [])
            if isinstance(item, dict) and str(item.get("value")).strip()
        ],
        "vt_box": [
            str(item.get("value")).strip()
            for item in (sandbox.get("diagnostic_vt_box_seed") or [])
            if isinstance(item, dict) and str(item.get("value")).strip()
        ],
        "preserved_not_budgeted": [
            str(v).strip()
            for v in (control_arm.get("preserved_not_budgeted_canonicals_top") or [])
            if str(v).strip()
        ],
    }


def _counter_top(counter: Counter[str], *, limit: int = 8) -> List[Dict[str, Any]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _metadata_from_first_date(window_root: Path, dates: List[str]) -> Dict[str, Any]:
    if not dates:
        return {}
    scoreboard = load_scoreboard(window_root, dates[0])
    metadata = scoreboard.get("metadata") or {}
    return metadata if isinstance(metadata, dict) else {}


def _build_ledger(window_root: Path, *, results_root: Path) -> Dict[str, Any]:
    dates = iter_window_dates(window_root)
    inventory_map = _inventory_map(window_root)
    rows: List[Dict[str, Any]] = []
    boxed_counter: Counter[str] = Counter()
    straight_counter: Counter[str] = Counter()
    vt_box_counter: Counter[str] = Counter()
    preserved_counter: Counter[str] = Counter()

    for results_date in dates:
        winners_by_state = winners_for_date(results_root=results_root, results_date=results_date)
        scoreboard = load_scoreboard(window_root, results_date)
        shadow = load_shadow(window_root, results_date)
        manifest = load_translation_manifest(window_root, results_date)
        board_verdict = scoreboard.get("board_verdict") or {}
        scoreboard_rows = scoreboard.get("scoreboard_rows") or []
        scoreboard_by_state = {
            str(row.get("state_key") or "").strip(): row
            for row in scoreboard_rows
            if isinstance(row, dict) and str(row.get("state_key") or "").strip()
        }
        state_decisions = shadow.get("state_decisions") or []
        shadow_by_state = {
            str(row.get("state_key") or "").strip(): row
            for row in state_decisions
            if isinstance(row, dict) and str(row.get("state_key") or "").strip()
        }
        state_receipts = manifest.get("state_receipts") or []
        manifest_by_state = {
            str(entry.get("state_key") or "").strip(): entry
            for entry in state_receipts
            if isinstance(entry, dict) and str(entry.get("state_key") or "").strip()
        }

        for state_key in sorted(winners_by_state.keys()):
            winner_events = winner_events_for_state(
                date=results_date,
                state_key=state_key,
                winners_by_state=winners_by_state,
            )
            if not winner_events:
                continue
            scoreboard_row = scoreboard_by_state.get(state_key, {})
            shadow_row = shadow_by_state.get(state_key, {})
            manifest_entry = manifest_by_state.get(state_key, {})
            seed = load_state_seed_from_manifest_entry(manifest_entry) if manifest_entry else {}
            flags = diagnostic_membership(seed, winner_events[0]) if seed else {}
            seed_signals = _seed_signal_lists(seed) if seed else {
                "boxed": [],
                "straight": [],
                "vt_box": [],
                "preserved_not_budgeted": [],
            }
            for value in seed_signals["boxed"]:
                boxed_counter[value] += 1
            for value in seed_signals["straight"]:
                straight_counter[value] += 1
            for value in seed_signals["vt_box"]:
                vt_box_counter[value] += 1
            for value in seed_signals["preserved_not_budgeted"]:
                preserved_counter[value] += 1

            candidate_universe = _maybe_load_json(
                str(((seed.get("control_arm") or {}).get("candidate_universe") or {}).get("path") or "")
            )
            play_card = _maybe_load_json(str(((seed.get("control_arm") or {}).get("play_card") or {}).get("path") or ""))

            for winner in winner_events:
                row_flags = diagnostic_membership(seed, winner) if seed else {}
                cu_metrics = extract_candidate_universe_metrics(candidate_universe, winner) if candidate_universe else {
                    "cu_exact": False,
                    "cu_box": False,
                }
                play_metrics = _extract_play_card_metrics_all_strategies(play_card, winner) if play_card else {
                    "play_card_any_exact": False,
                    "play_card_any_box": False,
                    "b12_exact": False,
                    "b12_box": False,
                    "b24_exact": False,
                    "b24_box": False,
                    "b36_exact": False,
                    "b36_box": False,
                }
                inventory = inventory_map.get((results_date, state_key, winner.period, winner.literal), {})
                priority_score = scoreboard_row.get("priority_score")
                ledger_row: Dict[str, Any] = {
                    "date": results_date,
                    "state_key": state_key,
                    "period": winner.period,
                    "winner": winner.literal,
                    "winner_canonical": winner.canonical,
                    "winner_vtrac_index": winner.vtrac_index if winner.vtrac_index is not None else "",
                    "winner_on_board": bool(scoreboard_row),
                    "board_rank": scoreboard_row.get("score_rank", ""),
                    "board_priority_score": priority_score if priority_score is not None else "",
                    "board_role": scoreboard_row.get("role", ""),
                    "board_bucket": scoreboard_row.get("targeting_bucket", ""),
                    "board_tracker_posture": scoreboard_row.get("tracker_posture", ""),
                    "shadow_posture": shadow_row.get("posture", ""),
                    "shadow_mode": shadow_row.get("mode", ""),
                    "shadow_cap_class": shadow_row.get("cap_class", ""),
                    "translator_route": shadow_row.get("translator_route", ""),
                    "reason_codes": ",".join(shadow_row.get("reason_codes") or []),
                    "top_primary_target": board_verdict.get("top_primary_target") == state_key,
                    "secondary_target": board_verdict.get("secondary_target") == state_key,
                    "best_clean_host": board_verdict.get("best_clean_host") == state_key,
                    "highest_context_support_state": board_verdict.get("highest_context_support_state") == state_key,
                    "arena_primary_box": row_flags.get("arena_primary_box", False),
                    "arena_context_box": row_flags.get("arena_context_box", False),
                    "arena_primary_vt": row_flags.get("arena_primary_vt", False),
                    "sandbox_box_seed": row_flags.get("sandbox_box_seed", False),
                    "sandbox_exact_seed": row_flags.get("sandbox_exact_seed", False),
                    "sandbox_vt_seed": row_flags.get("sandbox_vt_seed", False),
                    "preserved_not_budgeted": row_flags.get("preserved_not_budgeted", False),
                    "arena_box_signal": dominant_box_signal(row_flags),
                    "arena_exact_signal": exact_signal(row_flags),
                    "cu_exact": cu_metrics.get("cu_exact", False),
                    "cu_box": cu_metrics.get("cu_box", False),
                    **play_metrics,
                    "profit_alert_support": _hint_present(scoreboard_row.get("profit_alert_hint")),
                    "compound_event_support": _hint_present(scoreboard_row.get("compound_event_hint")),
                    "due_double_support": _hint_present(scoreboard_row.get("due_double_hint")),
                    "blackapple_support": _hint_present(scoreboard_row.get("blackapple_reco_hint")),
                    "positional_support": _hint_present(scoreboard_row.get("positional_hint")),
                    "r_consensus_support": _hint_present(scoreboard_row.get("r_consensus_hint")),
                    "survivor_support": _hint_present(scoreboard_row.get("survivor_hint")),
                    "inventory_type": inventory.get("type", ""),
                    "inventory_has_mirror_pair": inventory.get("has_mirror_pair", ""),
                    "inventory_mirror_pairs": inventory.get("mirror_pairs", ""),
                    "opportunity_gap_box": dominant_box_signal(row_flags) and not play_metrics.get("play_card_any_box", False),
                    "opportunity_gap_exact": exact_signal(row_flags) and not play_metrics.get("play_card_any_exact", False),
                }
                rows.append(ledger_row)

    return {
        "dates": dates,
        "rows": rows,
        "boxed_counter": boxed_counter,
        "straight_counter": straight_counter,
        "vt_box_counter": vt_box_counter,
        "preserved_counter": preserved_counter,
    }


def _count_truthy(rows: Iterable[Dict[str, Any]], key: str) -> int:
    return sum(1 for row in rows if bool(row.get(key)))


def _rank_histogram(rows: List[Dict[str, Any]]) -> Dict[str, int]:
    out = {"top3": 0, "top5": 0, "top8": 0, "off_board": 0}
    for row in rows:
        try:
            rank = int(str(row.get("board_rank") or "").strip())
        except Exception:
            out["off_board"] += 1
            continue
        if rank <= 3:
            out["top3"] += 1
        if rank <= 5:
            out["top5"] += 1
        if rank <= 8:
            out["top8"] += 1
    return out


def _tracker_attribution(rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    out: Dict[str, Dict[str, int]] = {}
    for tracker in (
        "profit_alert_support",
        "compound_event_support",
        "due_double_support",
        "blackapple_support",
        "positional_support",
        "r_consensus_support",
        "survivor_support",
    ):
        subset = [row for row in rows if bool(row.get(tracker))]
        out[tracker] = {
            "events": len(subset),
            "arena_box_signal": _count_truthy(subset, "arena_box_signal"),
            "cu_box": _count_truthy(subset, "cu_box"),
            "play_card_box": _count_truthy(subset, "play_card_any_box"),
            "opportunity_gap_box": _count_truthy(subset, "opportunity_gap_box"),
        }
    return out


def _aggregate(window_root: Path, ledger_payload: Dict[str, Any]) -> Dict[str, Any]:
    rows = ledger_payload["rows"]
    total = len(rows)
    metadata = _metadata_from_first_date(window_root, ledger_payload["dates"])
    rank_hist = _rank_histogram(rows)
    role_counter = Counter(str(row.get("board_role") or "").strip() or "_missing_" for row in rows)
    posture_counter = Counter(str(row.get("shadow_posture") or "").strip() or "_missing_" for row in rows)
    type_counter = Counter(str(row.get("inventory_type") or "").strip() or "_none_" for row in rows)

    summary = {
        "winner_events": total,
        "winner_on_board": _count_truthy(rows, "winner_on_board"),
        "top_primary_target": _count_truthy(rows, "top_primary_target"),
        "secondary_target": _count_truthy(rows, "secondary_target"),
        "best_clean_host": _count_truthy(rows, "best_clean_host"),
        "highest_context_support_state": _count_truthy(rows, "highest_context_support_state"),
        "arena_box_signal": _count_truthy(rows, "arena_box_signal"),
        "arena_exact_signal": _count_truthy(rows, "arena_exact_signal"),
        "arena_primary_vt": _count_truthy(rows, "arena_primary_vt"),
        "cu_exact": _count_truthy(rows, "cu_exact"),
        "cu_box": _count_truthy(rows, "cu_box"),
        "play_card_any_exact": _count_truthy(rows, "play_card_any_exact"),
        "play_card_any_box": _count_truthy(rows, "play_card_any_box"),
        "b12_exact": _count_truthy(rows, "b12_exact"),
        "b12_box": _count_truthy(rows, "b12_box"),
        "b24_exact": _count_truthy(rows, "b24_exact"),
        "b24_box": _count_truthy(rows, "b24_box"),
        "b36_exact": _count_truthy(rows, "b36_exact"),
        "b36_box": _count_truthy(rows, "b36_box"),
        "preserved_not_budgeted": _count_truthy(rows, "preserved_not_budgeted"),
        "opportunity_gap_box": _count_truthy(rows, "opportunity_gap_box"),
        "opportunity_gap_exact": _count_truthy(rows, "opportunity_gap_exact"),
        "mirror_or_double_results": sum(
            1 for row in rows if str(row.get("inventory_type") or "").strip() in {"double", "mirror_double", "triple"}
        ),
        "board_rank_histogram": rank_hist,
    }
    rates = {key: {"count": value, "rate": _pct(value, total)} for key, value in summary.items() if isinstance(value, int)}
    return {
        "metadata": {
            "window_root": safe_rel(window_root),
            "analysis_dir": safe_rel(analysis_dir(window_root)),
            "validation_dir": safe_rel(validation_dir(window_root)),
            "window_dates": ledger_payload["dates"],
            "day_count": len(ledger_payload["dates"]),
            "profile": metadata.get("profile", ""),
            "experiment_tag": metadata.get("experiment_tag", ""),
        },
        "summary_counts": summary,
        "summary_rates": rates,
        "role_counts": dict(role_counter.most_common()),
        "posture_counts": dict(posture_counter.most_common()),
        "result_type_counts": dict(type_counter.most_common()),
        "tracker_attribution": _tracker_attribution(rows),
        "translator_learning": {
            "diagnostic_boxed_seed_top": _counter_top(ledger_payload["boxed_counter"]),
            "diagnostic_straight_seed_top": _counter_top(ledger_payload["straight_counter"]),
            "diagnostic_vt_box_seed_top": _counter_top(ledger_payload["vt_box_counter"]),
            "preserved_not_budgeted_top": _counter_top(ledger_payload["preserved_counter"]),
        },
    }


def _render_markdown(payload: Dict[str, Any], *, ledger_path: Path) -> str:
    md = payload["metadata"]
    counts = payload["summary_counts"]
    rates = payload["summary_rates"]
    tracker = payload["tracker_attribution"]
    learning = payload["translator_learning"]
    lines: List[str] = []
    lines.append("# Analysis Arena Window Performance / Opportunity Gap Report")
    lines.append("")
    lines.append("## 1. Window Metadata")
    lines.append("")
    lines.append(f"- Window root: `{md['window_root']}`")
    lines.append(f"- Dates: `{md['window_dates'][0]}` to `{md['window_dates'][-1]}`" if md["window_dates"] else "- Dates: _none_")
    lines.append(f"- Day count: `{md['day_count']}`")
    lines.append(f"- Profile: `{md.get('profile') or 'tool_only'}`")
    lines.append(f"- Experiment tag: `{md.get('experiment_tag') or 'arena_v0'}`")
    lines.append(f"- Ledger: `{safe_rel(ledger_path)}`")
    lines.append("")
    lines.append("## 2. Arena Intrinsic Quality")
    lines.append("")
    lines.append(f"- Winner events: `{counts['winner_events']}`")
    lines.append(f"- Winner on board: `{counts['winner_on_board']}` ({rates['winner_on_board']['rate']})")
    lines.append(f"- Board top3 containment: `{counts['board_rank_histogram']['top3']}` ({_pct(counts['board_rank_histogram']['top3'], counts['winner_events'])})")
    lines.append(f"- Board top5 containment: `{counts['board_rank_histogram']['top5']}` ({_pct(counts['board_rank_histogram']['top5'], counts['winner_events'])})")
    lines.append(f"- Top primary target hits: `{counts['top_primary_target']}` ({rates['top_primary_target']['rate']})")
    lines.append(f"- Best clean host hits: `{counts['best_clean_host']}` ({rates['best_clean_host']['rate']})")
    lines.append(f"- Arena box signal present: `{counts['arena_box_signal']}` ({rates['arena_box_signal']['rate']})")
    lines.append(f"- Arena exact signal present: `{counts['arena_exact_signal']}` ({rates['arena_exact_signal']['rate']})")
    lines.append(f"- Arena VTRAC signal present: `{counts['arena_primary_vt']}` ({rates['arena_primary_vt']['rate']})")
    lines.append("")
    lines.append("## 3. Control-Arm Realized Performance")
    lines.append("")
    lines.append(f"- Candidate Universe exact: `{counts['cu_exact']}` ({rates['cu_exact']['rate']})")
    lines.append(f"- Candidate Universe box: `{counts['cu_box']}` ({rates['cu_box']['rate']})")
    lines.append(f"- Play Card any exact: `{counts['play_card_any_exact']}` ({rates['play_card_any_exact']['rate']})")
    lines.append(f"- Play Card any box: `{counts['play_card_any_box']}` ({rates['play_card_any_box']['rate']})")
    lines.append(f"- B12 box: `{counts['b12_box']}` ({rates['b12_box']['rate']})")
    lines.append(f"- B24 box: `{counts['b24_box']}` ({rates['b24_box']['rate']})")
    lines.append(f"- B36 box: `{counts['b36_box']}` ({rates['b36_box']['rate']})")
    lines.append("")
    lines.append("## 4. Opportunity Gap")
    lines.append("")
    lines.append(f"- Preserved-not-budgeted winner canonicals: `{counts['preserved_not_budgeted']}` ({rates['preserved_not_budgeted']['rate']})")
    lines.append(f"- Arena box signal but Play Card box miss: `{counts['opportunity_gap_box']}` ({rates['opportunity_gap_box']['rate']})")
    lines.append(f"- Arena exact signal but Play Card exact miss: `{counts['opportunity_gap_exact']}` ({rates['opportunity_gap_exact']['rate']})")
    lines.append("")
    lines.append("## 5. Tracker / Context Attribution")
    lines.append("")
    for key, value in tracker.items():
        label = key.replace("_support", "").replace("_", " ")
        lines.append(
            f"- {label}: events=`{value['events']}` arena_box=`{value['arena_box_signal']}` "
            f"cu_box=`{value['cu_box']}` play_box=`{value['play_card_box']}` "
            f"gap_box=`{value['opportunity_gap_box']}`"
        )
    lines.append("")
    lines.append("## 6. Translator-Learning Signals")
    lines.append("")
    lines.append(
        "- Diagnostic boxed seeds: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in learning["diagnostic_boxed_seed_top"]) or "_none_")
    )
    lines.append(
        "- Diagnostic straight seeds: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in learning["diagnostic_straight_seed_top"]) or "_none_")
    )
    lines.append(
        "- Diagnostic VT-box seeds: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in learning["diagnostic_vt_box_seed_top"]) or "_none_")
    )
    lines.append(
        "- Preserved-not-budgeted canonicals: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in learning["preserved_not_budgeted_top"]) or "_none_")
    )
    lines.append("")
    lines.append("## 7. Final Promotions / Warnings")
    lines.append("")
    lines.append("- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.")
    lines.append("- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.")
    lines.append("- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    window_root = _window_root_from_arg(args.window_root)
    results_root = _window_root_from_arg(args.results_root)
    defaults = _default_output_paths(window_root)
    out_md = _window_root_from_arg(args.out_md) if args.out_md else defaults["md"]
    out_json = _window_root_from_arg(args.out_json) if args.out_json else defaults["json"]
    out_ledger = _window_root_from_arg(args.out_ledger) if args.out_ledger else defaults["ledger"]

    ledger_payload = _build_ledger(window_root, results_root=results_root)
    aggregate = _aggregate(window_root, ledger_payload)
    aggregate["ledger_path"] = safe_rel(out_ledger)
    aggregate["schema_version"] = "analysis_arena_window_performance_gap/v1"
    _write_csv(out_ledger, ledger_payload["rows"], force=args.force)
    _write_json(out_json, aggregate, force=args.force)
    _write_text(out_md, _render_markdown(aggregate, ledger_path=out_ledger), force=args.force)
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")
    print(f"Wrote: {safe_rel(out_ledger)}")


if __name__ == "__main__":
    main()
