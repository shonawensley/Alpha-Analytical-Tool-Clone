#!/usr/bin/env python3
"""Create a deep hit-analysis report for an Analysis Arena window."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import iter_window_dates, safe_rel
from scripts.tools.brain2_rank_contract import RANK_INTEGRITY_INVALID_STATIC_ORDER


DEFAULT_RUNS_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
DEFAULT_SHAREPACKS_ROOT = REPO_ROOT / "sharepacks" / "_predictive"

BUDGET_ORDER = {"B12": 1, "B24": 2, "B36": 3}
STATUS_ORDER = {"OFF": 0, "WATCH": 1, "ALERT": 2}
MIRROR_DIGITS = {"0": "5", "1": "6", "2": "7", "3": "8", "4": "9", "5": "0", "6": "1", "7": "2", "8": "3", "9": "4"}


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--runs-root",
        default=str(DEFAULT_RUNS_ROOT),
        help="RUNS root containing daily grading outputs (default: docs/.../RUNS)",
    )
    ap.add_argument(
        "--sharepacks-root",
        default=str(DEFAULT_SHAREPACKS_ROOT),
        help="Predictive sharepacks root (default: sharepacks/_predictive)",
    )
    ap.add_argument("--profile", default="tool_only", help="Profile suffix used by daily grading files (default: tool_only)")
    ap.add_argument("--experiment-tag", default="arena_v0", help="Experiment tag suffix used by arena grading files (default: arena_v0)")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-csv", default="", help="Optional hit-roster CSV output path.")
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
        "md": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json",
        "csv": window_root / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
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


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> Any:
    return json.loads(_read_text(path))


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _bool01(value: Any) -> bool:
    text = str(value or "").strip().lower()
    return text in {"1", "true", "yes", "y"}


def _pct(num: int, den: int) -> str:
    if den <= 0:
        return "0.0%"
    return f"{100.0 * num / den:.1f}%"


def _safe_int(value: Any) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return 0


def _budget_min(existing: str, candidate: str) -> str:
    if not candidate:
        return existing
    if not existing:
        return candidate
    return candidate if BUDGET_ORDER.get(candidate, 99) < BUDGET_ORDER.get(existing, 99) else existing


def _rate(count: int, den: int) -> float:
    return count / den if den else 0.0


def _status_value(status: str) -> int:
    return STATUS_ORDER.get(str(status or "").strip().upper(), 0)


def _normalize_status(status: str) -> str:
    text = str(status or "").strip().upper()
    return text if text in STATUS_ORDER else "OFF"


def _mirror_pair_from_repeated_digit(winner: str) -> str:
    counts = Counter(ch for ch in str(winner) if ch.isdigit())
    repeated = [digit for digit, count in counts.items() if count >= 2]
    if not repeated:
        return ""
    digit = sorted(repeated)[0]
    other = MIRROR_DIGITS.get(digit, "")
    if not other:
        return ""
    lo, hi = sorted((digit, other))
    return f"{lo}/{hi}"


def _canonical_pair_key(value: str) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    if "/" in text:
        try:
            a, b = [part.strip() for part in text.split("/", 1)]
            lo, hi = sorted((a, b))
            return f"{lo}/{hi}"
        except Exception:
            return text
    return text


def _family_match_rank(pair_key: str, row: Dict[str, str]) -> int:
    if not pair_key:
        return 0
    for idx in range(1, 6):
        text = row.get(f"Family {idx}", "")
        if pair_key and pair_key in str(text):
            return idx
    return 0


def _parse_json_list(text: str) -> List[str]:
    raw = str(text or "").strip()
    if not raw:
        return []
    try:
        value = json.loads(raw)
    except Exception:
        return []
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def _board_rank_tier(rank: str) -> str:
    try:
        value = int(str(rank).strip())
    except Exception:
        return "OFF_BOARD"
    if value <= 3:
        return "TOP3"
    if value <= 5:
        return "TOP5"
    if value <= 8:
        return "MID_BOARD"
    return "LOW_BOARD"


def _primary_hit_class(event: Dict[str, Any]) -> str:
    if event.get("play_straight_hit"):
        return "STRAIGHT"
    if event.get("play_box_strict_hit"):
        return "STRICT_BOXED"
    if event.get("play_box_any_hit"):
        return "CANONICAL_BOX"
    if event.get("play_vtrac_only_hit"):
        return "VTRAC_ONLY"
    if event.get("play_vtrac_hit"):
        return "VTRAC_LANE"
    return "NONE"


def _credit_signature(event: Dict[str, Any]) -> str:
    if event.get("play_straight_hit") and event.get("play_vtrac_hit"):
        return "STRAIGHT+VTRAC"
    if event.get("play_box_strict_hit") and event.get("play_vtrac_hit"):
        return "STRICT_BOXED+VTRAC"
    if event.get("play_box_any_hit") and event.get("play_vtrac_hit"):
        return "CANONICAL_BOX+VTRAC"
    if event.get("play_straight_hit"):
        return "STRAIGHT"
    if event.get("play_box_strict_hit"):
        return "STRICT_BOXED"
    if event.get("play_box_any_hit"):
        return "CANONICAL_BOX"
    if event.get("play_vtrac_only_hit"):
        return "VTRAC_ONLY"
    if event.get("play_vtrac_hit"):
        return "VTRAC_LANE"
    return "NONE"


def _hit_path_signature(event: Dict[str, Any]) -> str:
    if event.get("arena_exact_signal") and event.get("play_straight_hit"):
        return "ARENA_EXACT_TO_PLAY"
    if event.get("arena_box_signal") and event.get("play_box_any_hit"):
        return "ARENA_BOX_TO_PLAY"
    if event.get("candidate_box_hit") and event.get("play_box_any_hit"):
        return "CU_TO_PLAY"
    if event.get("play_vtrac_only_hit"):
        return "LANE_ONLY"
    return "MIXED"


def _signature_strength(event: Dict[str, Any]) -> Tuple[int, str]:
    score = 0
    if event.get("sandbox_box_seed_match"):
        score += 1
    if event.get("sandbox_straight_seed_match"):
        score += 1
    if event.get("sandbox_vt_seed_match"):
        score += 1
    if event.get("preserved_not_budgeted_match"):
        score += 1
    if event.get("profit_alert_direct_match") or event.get("profit_alert_implied_match"):
        score += 1
    if event.get("blackapple_status") == "ALERT":
        score += 1
    if event.get("compound_event_present"):
        score += 1
    if score >= 4:
        return score, "CLEAR_ARENA_FINALIST"
    if score >= 2:
        return score, "PARTIAL_ARENA_FINALIST"
    if score >= 1:
        return score, "LIGHT_ARENA_FINALIST"
    return score, "CONTROL_ARM_ONLY_CATCH"


def _double_context_strength(event: Dict[str, Any]) -> str:
    kind = str(event.get("inventory_type") or "").strip()
    if kind not in {"double", "mirror_double", "triple"}:
        return ""
    score = 0
    if _safe_int(event.get("due_double_draws_since_double")) >= 3:
        score += 1
    fam_rank = _safe_int(event.get("due_double_family_match_rank"))
    if fam_rank == 1:
        score += 2
    elif fam_rank in {2, 3}:
        score += 1
    if "DBL" in str(event.get("profit_alert_badges") or ""):
        score += 1
    if str(event.get("blackapple_status") or "") == "ALERT":
        score += 1
    if event.get("arena_box_signal") or event.get("arena_exact_signal"):
        score += 1
    if score >= 4:
        return "STRONG"
    if score >= 2:
        return "MEDIUM"
    return "WEAK"


def _daily_play_card_grade_path(runs_root: Path, results_date: str, *, profile: str, experiment_tag: str) -> Path:
    return runs_root / f"{results_date}__PLAY_CARD_GRADE__{profile}__{experiment_tag}.csv"


def _daily_candidate_grade_path(runs_root: Path, results_date: str, *, profile: str, experiment_tag: str) -> Path:
    return runs_root / f"{results_date}__CANDIDATE_UNIVERSE_GRADE__{profile}__{experiment_tag}.csv"


def _load_play_card_events(
    runs_root: Path,
    *,
    dates: Sequence[str],
    profile: str,
    experiment_tag: str,
) -> Dict[Tuple[str, str, str, str], Dict[str, Any]]:
    events: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for results_date in dates:
        path = _daily_play_card_grade_path(runs_root, results_date, profile=profile, experiment_tag=experiment_tag)
        for row in _read_csv_rows(path):
            if row.get("winner_missing") == "1":
                continue
            key = (
                results_date,
                row.get("state_key", ""),
                row.get("winner_label", ""),
                row.get("winner", ""),
            )
            event = events.setdefault(
                key,
                {
                    "play_straight_hit": False,
                    "play_box_strict_hit": False,
                    "play_box_any_hit": False,
                    "play_vtrac_hit": False,
                    "play_inclusive_hit": False,
                    "play_vtrac_only_hit": False,
                    "play_vtrac_and_box_hit": False,
                    "play_vtrac_and_straight_hit": False,
                    "min_budget_straight": "",
                    "min_budget_box_strict": "",
                    "min_budget_box_any": "",
                    "min_budget_inclusive": "",
                    "min_budget_vtrac": "",
                    "strategy_hits": defaultdict(list),
                },
            )
            budget = str(row.get("budget_label") or "").strip()
            strategy = str(row.get("strategy") or "").strip()
            straight = _bool01(row.get("straight_hit"))
            box_strict = _bool01(row.get("box_hit"))
            box_any = _bool01(row.get("hit_any_box"))
            vtrac = _bool01(row.get("vtrac_index_hit"))
            inclusive = _bool01(row.get("hit_any_inclusive"))

            if straight:
                event["play_straight_hit"] = True
                event["min_budget_straight"] = _budget_min(event["min_budget_straight"], budget)
                event["strategy_hits"]["straight"].append(f"{strategy}:{budget}")
            if box_strict:
                event["play_box_strict_hit"] = True
                event["min_budget_box_strict"] = _budget_min(event["min_budget_box_strict"], budget)
                event["strategy_hits"]["strict_box"].append(f"{strategy}:{budget}")
            if box_any:
                event["play_box_any_hit"] = True
                event["min_budget_box_any"] = _budget_min(event["min_budget_box_any"], budget)
                event["strategy_hits"]["box_any"].append(f"{strategy}:{budget}")
            if vtrac:
                event["play_vtrac_hit"] = True
                event["min_budget_vtrac"] = _budget_min(event["min_budget_vtrac"], budget)
                event["strategy_hits"]["vtrac"].append(f"{strategy}:{budget}")
            if inclusive:
                event["play_inclusive_hit"] = True
                event["min_budget_inclusive"] = _budget_min(event["min_budget_inclusive"], budget)
                event["strategy_hits"]["inclusive"].append(f"{strategy}:{budget}")

    for event in events.values():
        event["play_vtrac_only_hit"] = bool(event["play_vtrac_hit"] and not event["play_box_any_hit"])
        event["play_vtrac_and_box_hit"] = bool(event["play_vtrac_hit"] and event["play_box_any_hit"])
        event["play_vtrac_and_straight_hit"] = bool(event["play_vtrac_hit"] and event["play_straight_hit"])
        event["strategy_hits"] = {
            key: sorted(set(values)) for key, values in event["strategy_hits"].items() if values
        }
    return events


def _load_candidate_events(
    runs_root: Path,
    *,
    dates: Sequence[str],
    profile: str,
    experiment_tag: str,
) -> Dict[Tuple[str, str, str, str], Dict[str, Any]]:
    events: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for results_date in dates:
        path = _daily_candidate_grade_path(runs_root, results_date, profile=profile, experiment_tag=experiment_tag)
        for row in _read_csv_rows(path):
            if row.get("winner_missing") == "1":
                continue
            if row.get("pack_id") != "__UNION__" or row.get("method_id") != "union":
                continue
            key = (
                results_date,
                row.get("state_key", ""),
                row.get("winner_label", ""),
                row.get("winner", ""),
            )
            events[key] = {
                "candidate_hit_any": _bool01(row.get("hit_any")),
                "candidate_straight_hit": _bool01(row.get("straight_hit")),
                "candidate_box_hit": _bool01(row.get("box_hit")),
                "candidate_vtrac_hit": _bool01(row.get("vtrac_index_hit")),
                "candidate_vtrac_only_hit": _bool01(row.get("vtrac_index_hit_only")),
            }
    return events


def _load_due_doubles_map(
    sharepacks_root: Path, *, dates: Sequence[str]
) -> Dict[str, Dict[Tuple[str, str], Dict[str, Any]]]:
    out: Dict[str, Dict[Tuple[str, str], Dict[str, Any]]] = {}
    for results_date in dates:
        path = sharepacks_root / results_date / "control_center" / "due_doubles.csv"
        daily: Dict[Tuple[str, str], Dict[str, Any]] = {}
        variant_rank: Dict[str, int] = defaultdict(int)
        for row in _read_csv_rows(path):
            variant = str(row.get("Variant") or "").strip()
            state_key = str(row.get("StateKey") or "").strip()
            if not variant or not state_key:
                continue
            variant_rank[variant] += 1
            daily[(state_key, variant)] = {
                "rank": variant_rank[variant],
                "draws_since_double": _safe_int(row.get("Draws Since Double")),
                "families": [str(row.get(f"Family {idx}") or "") for idx in range(1, 6)],
            }
        out[results_date] = daily
    return out


def _select_due_double_row(daily: Dict[Tuple[str, str], Dict[str, Any]], *, state_key: str, period: str) -> Dict[str, Any]:
    period_row = daily.get((state_key, period), {})
    combined_row = daily.get((state_key, "Combined"), {})
    chosen = period_row or combined_row
    return {
        "period_rank": period_row.get("rank", ""),
        "combined_rank": combined_row.get("rank", ""),
        "draws_since_double": chosen.get("draws_since_double", ""),
        "families": chosen.get("families", []),
        "variant_used": period if period_row else ("Combined" if combined_row else ""),
    }


def _load_blackapple_map(
    sharepacks_root: Path, *, dates: Sequence[str]
) -> Dict[str, Dict[Tuple[str, str], List[Dict[str, str]]]]:
    out: Dict[str, Dict[Tuple[str, str], List[Dict[str, str]]]] = {}
    for results_date in dates:
        path = sharepacks_root / results_date / "control_center" / "blackapple_alerts.csv"
        daily: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
        for row in _read_csv_rows(path):
            state_key = str(row.get("StateKey") or "").strip()
            variant = str(row.get("Variant") or "").strip()
            if state_key and variant:
                daily[(state_key, variant)].append(row)
        out[results_date] = daily
    return out


def _best_blackapple_row(daily: Dict[Tuple[str, str], List[Dict[str, str]]], *, state_key: str, period: str) -> Dict[str, str]:
    candidates: List[Dict[str, str]] = []
    for variant in (period, "Combined"):
        candidates.extend(daily.get((state_key, variant), []))
    if not candidates:
        return {}
    return max(
        candidates,
        key=lambda row: (
            _status_value(_normalize_status(row.get("Status") or "")),
            _safe_int(row.get("BA-Score")),
            1 if str(row.get("Variant") or "").strip() == period else 0,
        ),
    )


def _load_profit_alerts_map(
    sharepacks_root: Path, *, dates: Sequence[str]
) -> Dict[str, Dict[Tuple[str, str], List[Dict[str, str]]]]:
    out: Dict[str, Dict[Tuple[str, str], List[Dict[str, str]]]] = {}
    for results_date in dates:
        path = sharepacks_root / results_date / "control_center" / "profit_alerts.csv"
        daily: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
        for row in _read_csv_rows(path):
            state_key = str(row.get("StateKey") or "").strip()
            variant = str(row.get("Variant") or "").strip()
            if state_key and variant:
                daily[(state_key, variant)].append(row)
        out[results_date] = daily
    return out


def _relevant_profit_alert_rows(
    daily: Dict[Tuple[str, str], List[Dict[str, str]]], *, state_key: str, period: str
) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for variant in (period, "Combined"):
        rows.extend(daily.get((state_key, variant), []))
    dedup: Dict[Tuple[str, str, str], Dict[str, str]] = {}
    for row in rows:
        key = (
            str(row.get("AlertId") or "").strip(),
            str(row.get("Variant") or "").strip(),
            str(row.get("Canonical") or "").strip(),
        )
        dedup[key] = row
    return list(dedup.values())


def _load_compound_map(
    sharepacks_root: Path, *, dates: Sequence[str]
) -> Dict[str, Dict[Tuple[str, str], List[Dict[str, str]]]]:
    out: Dict[str, Dict[Tuple[str, str], List[Dict[str, str]]]] = {}
    for results_date in dates:
        path = sharepacks_root / results_date / "control_center" / "profit_compound_events.csv"
        daily: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
        for row in _read_csv_rows(path):
            state_key = str(row.get("state_key") or "").strip()
            variant = str(row.get("variant") or "").strip()
            if state_key and variant:
                daily[(state_key, variant)].append(row)
        out[results_date] = daily
    return out


def _best_compound_row(daily: Dict[Tuple[str, str], List[Dict[str, str]]], *, state_key: str, period: str) -> Dict[str, str]:
    candidates: List[Dict[str, str]] = []
    for variant in (period, "Combined"):
        candidates.extend(daily.get((state_key, variant), []))
    if not candidates:
        return {}
    return max(candidates, key=lambda row: (_safe_int(row.get("priority")), 1 if str(row.get("variant") or "").strip() == period else 0))


def _load_ledger_rows(window_root: Path) -> List[Dict[str, str]]:
    path = window_root / f"{window_root.name}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv"
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty performance-gap ledger: {path}")
    return rows


def _load_inventory_map(window_root: Path) -> Dict[Tuple[str, str, str, str], Dict[str, str]]:
    matches = sorted((window_root / "VALIDATION").glob("*__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"))
    rows = _read_csv_rows(matches[0]) if matches else []
    out: Dict[Tuple[str, str, str, str], Dict[str, str]] = {}
    for row in rows:
        key = (
            row.get("date", ""),
            row.get("state", ""),
            row.get("period", ""),
            row.get("winner", ""),
        )
        out[key] = row
    return out


def _top_counter(counter: Counter[str], *, limit: int = 10) -> List[Dict[str, Any]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _median_rank(rows: Sequence[Dict[str, Any]]) -> Optional[float]:
    values = sorted(_safe_int(row.get("board_rank")) for row in rows if str(row.get("board_rank") or "").strip())
    if not values:
        return None
    mid = len(values) // 2
    if len(values) % 2 == 1:
        return float(values[mid])
    return (values[mid - 1] + values[mid]) / 2.0


def _format_float(value: Optional[float]) -> str:
    if value is None:
        return ""
    if math.isfinite(value):
        return f"{value:.1f}"
    return ""


def _signal_lift(rows_all: Sequence[Dict[str, Any]], rows_subset: Sequence[Dict[str, Any]], key: str) -> Dict[str, Any]:
    total = len(rows_all)
    subset_total = len(rows_subset)
    all_count = sum(1 for row in rows_all if _bool01(row.get(key)))
    subset_count = sum(1 for row in rows_subset if _bool01(row.get(key)))
    all_rate = _rate(all_count, total)
    subset_rate = _rate(subset_count, subset_total)
    lift = (subset_rate / all_rate) if all_rate > 0 else None
    return {
        "all_count": all_count,
        "all_rate": all_rate,
        "subset_count": subset_count,
        "subset_rate": subset_rate,
        "lift": lift,
    }


def _build_roster(
    *,
    window_root: Path,
    runs_root: Path,
    sharepacks_root: Path,
    profile: str,
    experiment_tag: str,
) -> Dict[str, Any]:
    dates = iter_window_dates(window_root)
    ledger_rows = _load_ledger_rows(window_root)
    ledger_by_key = {
        (row.get("date", ""), row.get("state_key", ""), row.get("period", ""), row.get("winner", "")): row
        for row in ledger_rows
    }
    inventory_by_key = _load_inventory_map(window_root)
    play_by_key = _load_play_card_events(runs_root, dates=dates, profile=profile, experiment_tag=experiment_tag)
    candidate_by_key = _load_candidate_events(runs_root, dates=dates, profile=profile, experiment_tag=experiment_tag)
    due_doubles_by_date = _load_due_doubles_map(sharepacks_root, dates=dates)
    blackapple_by_date = _load_blackapple_map(sharepacks_root, dates=dates)
    profit_by_date = _load_profit_alerts_map(sharepacks_root, dates=dates)
    compound_by_date = _load_compound_map(sharepacks_root, dates=dates)

    event_rows: List[Dict[str, Any]] = []
    for key, ledger in ledger_by_key.items():
        date, state_key, period, winner = key
        play = play_by_key.get(key, {})
        candidate = candidate_by_key.get(key, {})
        inventory = inventory_by_key.get((date, state_key, period, winner), {})
        daily_due = due_doubles_by_date.get(date, {})
        due = _select_due_double_row(daily_due, state_key=state_key, period=period)
        ba = _best_blackapple_row(blackapple_by_date.get(date, {}), state_key=state_key, period=period)
        profit_rows = _relevant_profit_alert_rows(profit_by_date.get(date, {}), state_key=state_key, period=period)
        compound = _best_compound_row(compound_by_date.get(date, {}), state_key=state_key, period=period)

        pair_key = _canonical_pair_key(
            inventory.get("mirror_pairs")
            or _mirror_pair_from_repeated_digit(winner if str(inventory.get("type") or "").strip() in {"double", "triple"} else "")
        )
        family_match_rank = _family_match_rank(pair_key, {f"Family {i + 1}": due["families"][i] if i < len(due["families"]) else "" for i in range(5)})

        profit_direct = False
        profit_implied = False
        profit_badges: List[str] = []
        profit_ids: List[str] = []
        profit_canonicals: List[str] = []
        top_strength = 0
        for row in profit_rows:
            canonical = str(row.get("Canonical") or "").strip()
            implied = _parse_json_list(row.get("ImpliedSet") or "")
            if canonical and canonical == ledger.get("winner_canonical"):
                profit_direct = True
            if winner in implied:
                profit_implied = True
            if canonical:
                profit_canonicals.append(canonical)
            if row.get("AlertId"):
                profit_ids.append(str(row.get("AlertId") or "").strip())
            badges = str(row.get("Badges") or "").strip()
            if badges:
                profit_badges.extend(part.strip() for part in badges.split("/") if part.strip())
            top_strength = max(top_strength, _safe_int(row.get("Strength")))

        event: Dict[str, Any] = {
            **ledger,
            **candidate,
            **play,
            "board_rank_tier": (
                _board_rank_tier(ledger.get("analytical_rank") or ledger.get("board_rank", ""))
                if _bool01(ledger.get("rank_signal_valid"))
                else "NOT_EVALUABLE"
            ),
            "inventory_type": inventory.get("type", ledger.get("inventory_type", "")),
            "inventory_has_mirror_pair": inventory.get("has_mirror_pair", ledger.get("inventory_has_mirror_pair", "")),
            "inventory_mirror_pairs": inventory.get("mirror_pairs", ledger.get("inventory_mirror_pairs", "")),
            "due_double_period_rank": due.get("period_rank", ""),
            "due_double_combined_rank": due.get("combined_rank", ""),
            "due_double_variant_used": due.get("variant_used", ""),
            "due_double_draws_since_double": due.get("draws_since_double", ""),
            "due_double_pair_key": pair_key,
            "due_double_family_match_rank": family_match_rank,
            "blackapple_status": _normalize_status(ba.get("Status") or ba.get("ba_status_label") or ""),
            "blackapple_score": _safe_int(ba.get("BA-Score") or ba.get("ba_score")),
            "blackapple_variant": str(ba.get("Variant") or "").strip(),
            "blackapple_examples": str(ba.get("Examples") or "").strip(),
            "blackapple_triggers": str(ba.get("Triggers") or "").strip(),
            "profit_alert_count": len(profit_rows),
            "profit_alert_top_strength": top_strength,
            "profit_alert_ids": ",".join(sorted(set(profit_ids))),
            "profit_alert_badges": ",".join(sorted(set(profit_badges))),
            "profit_alert_canonicals": ",".join(sorted(set(profit_canonicals))),
            "profit_alert_direct_match": profit_direct,
            "profit_alert_implied_match": profit_implied,
            "compound_event_present": bool(compound),
            "compound_top_event": str(compound.get("top_event") or "").strip(),
            "compound_priority": _safe_int(compound.get("priority")),
            "compound_watchlist_tags": str(compound.get("watchlist_tags") or "").strip(),
            "compound_candidate_alert_ids": str(compound.get("candidate_alert_ids") or "").strip(),
            "compound_promoter_alert_ids": str(compound.get("promoter_alert_ids") or "").strip(),
        }

        event["arena_final_candidate_signature_score"], event["arena_final_candidate_signature"] = _signature_strength(
            {
                "sandbox_box_seed_match": _bool01(event.get("sandbox_box_seed")),
                "sandbox_straight_seed_match": _bool01(event.get("sandbox_exact_seed")),
                "sandbox_vt_seed_match": _bool01(event.get("sandbox_vt_seed")),
                "preserved_not_budgeted_match": _bool01(event.get("preserved_not_budgeted")),
                "profit_alert_direct_match": profit_direct,
                "profit_alert_implied_match": profit_implied,
                "blackapple_status": event.get("blackapple_status"),
                "compound_event_present": bool(compound),
            }
        )
        event["hit_primary_class"] = _primary_hit_class(event)
        event["hit_class"] = event["hit_primary_class"]
        event["credit_signature"] = _credit_signature(event)
        event["budget_floor"] = event.get("min_budget_inclusive", "")
        event["high_conviction_budget_floor"] = event.get("min_budget_box_any", "") or event.get("min_budget_straight", "")
        event["hit_path_signature"] = _hit_path_signature(event)
        event["double_context_strength"] = _double_context_strength(event)
        event_rows.append(event)

    hit_rows = [row for row in event_rows if _bool01(row.get("play_inclusive_hit"))]
    return {
        "dates": dates,
        "all_rows": event_rows,
        "hit_rows": hit_rows,
    }


def _summary_payload(window_root: Path, roster_payload: Dict[str, Any]) -> Dict[str, Any]:
    all_rows = roster_payload["all_rows"]
    hits = roster_payload["hit_rows"]
    high_conf = [row for row in hits if _bool01(row.get("play_box_any_hit"))]
    vtrac_only = [row for row in hits if _bool01(row.get("play_vtrac_only_hit"))]
    exact = [row for row in hits if _bool01(row.get("play_straight_hit"))]
    strict_box = [row for row in hits if _bool01(row.get("play_box_strict_hit"))]
    doubles = [row for row in hits if str(row.get("inventory_type") or "").strip() in {"double", "mirror_double", "triple"}]
    rank_evaluable = any(
        _bool01(row.get("rank_signal_valid"))
        and bool(str(row.get("analytical_rank") or row.get("board_rank") or "").strip())
        for row in all_rows
    )

    def _budget_dist(rows: Sequence[Dict[str, Any]], key: str) -> Dict[str, int]:
        counter = Counter(str(row.get(key) or "").strip() or "_none_" for row in rows)
        return dict(counter)

    status_counter = Counter(str(row.get("blackapple_status") or "").strip() or "OFF" for row in hits)
    compound_counter = Counter(str(row.get("compound_top_event") or "").strip() or "_none_" for row in hits if row.get("compound_top_event"))
    hit_class_counter = Counter(str(row.get("hit_primary_class") or "NONE") for row in hits)
    credit_signature_counter = Counter(str(row.get("credit_signature") or "NONE") for row in hits)
    rank_tier_counter = (
        Counter(str(row.get("board_rank_tier") or "OFF_BOARD") for row in hits)
        if rank_evaluable
        else Counter()
    )
    double_strength_counter = Counter(str(row.get("double_context_strength") or "_none_") for row in doubles)

    signal_keys = [
        "arena_box_signal",
        "arena_exact_signal",
        "candidate_box_hit",
        "candidate_straight_hit",
        "candidate_vtrac_hit",
        "sandbox_box_seed",
        "sandbox_exact_seed",
        "sandbox_vt_seed",
        "preserved_not_budgeted",
        "profit_alert_direct_match",
        "profit_alert_implied_match",
        "compound_event_present",
    ]
    lifts = {
        key: {
            "all": _signal_lift(all_rows, hits, key),
            "high_conviction": _signal_lift(all_rows, high_conf, key),
            "vtrac_only": _signal_lift(all_rows, vtrac_only, key),
        }
        for key in signal_keys
    }

    def _best_rows(rows: Sequence[Dict[str, Any]], *, limit: int = 8) -> List[Dict[str, Any]]:
        ordered = sorted(
            rows,
            key=lambda row: (
                -_safe_int(row.get("arena_final_candidate_signature_score")),
                BUDGET_ORDER.get(str(row.get("min_budget_box_any") or row.get("min_budget_inclusive") or ""), 99),
                str(row.get("date") or ""),
                str(row.get("state_key") or ""),
            ),
        )
        return ordered[:limit]

    def _low_rank_rows(rows: Sequence[Dict[str, Any]], *, limit: int = 8) -> List[Dict[str, Any]]:
        if not rank_evaluable:
            return []
        ordered = sorted(rows, key=lambda row: (_safe_int(row.get("board_rank")) * -1, -_safe_int(row.get("arena_final_candidate_signature_score"))))
        return ordered[:limit]

    return {
        "metadata": {
            "window_root": safe_rel(window_root),
            "window_dates": roster_payload["dates"],
            "day_count": len(roster_payload["dates"]),
            "total_events": len(all_rows),
            "credited_hits": len(hits),
        },
        "hit_inventory": {
            "credited_hits": len(hits),
            "straight_hits": len(exact),
            "strict_box_hits": len(strict_box),
            "box_any_hits": len(high_conf),
            "vtrac_hits": sum(1 for row in hits if _bool01(row.get("play_vtrac_hit"))),
            "vtrac_only_hits": len(vtrac_only),
            "hit_class_counts": dict(hit_class_counter),
            "credit_signature_counts": dict(credit_signature_counter),
        },
        "ranking": {
            "status": "EVALUABLE" if rank_evaluable else "NOT_EVALUABLE",
            "evaluable": rank_evaluable,
            "reason": None if rank_evaluable else RANK_INTEGRITY_INVALID_STATIC_ORDER,
            "rank_tier_counts": dict(rank_tier_counter),
            "median_rank_all_hits": _median_rank(hits) if rank_evaluable else None,
            "median_rank_high_conviction": _median_rank(high_conf) if rank_evaluable else None,
            "median_rank_vtrac_only": _median_rank(vtrac_only) if rank_evaluable else None,
            "top_primary_target_hits": (
                sum(1 for row in hits if _bool01(row.get("top_primary_target")))
                if rank_evaluable
                else None
            ),
            "secondary_target_hits": (
                sum(1 for row in hits if _bool01(row.get("secondary_target")))
                if rank_evaluable
                else None
            ),
            "best_clean_host_hits": (
                sum(1 for row in hits if _bool01(row.get("best_clean_host")))
                if rank_evaluable
                else None
            ),
            "highest_context_support_hits": sum(1 for row in hits if _bool01(row.get("highest_context_support_state"))),
        },
        "budgets": {
            "min_budget_inclusive": _budget_dist(hits, "min_budget_inclusive"),
            "min_budget_box_any": _budget_dist(high_conf, "min_budget_box_any"),
            "min_budget_straight": _budget_dist(exact, "min_budget_straight"),
        },
        "morphology": {
            "inventory_types": dict(Counter(str(row.get("inventory_type") or "").strip() or "_none_" for row in hits)),
            "double_context_strength": dict(double_strength_counter),
            "blackapple_status": dict(status_counter),
            "compound_top_events": dict(compound_counter),
        },
        "signal_lift": lifts,
        "arena_finalist_signatures": {
            "signature_buckets": dict(Counter(str(row.get("arena_final_candidate_signature") or "") for row in hits)),
            "top_signature_hits": _best_rows(hits),
            "low_rank_hits": _low_rank_rows(high_conf if high_conf else hits),
            "vtrac_only_examples": _best_rows(vtrac_only),
            "double_examples": _best_rows(doubles),
        },
    }


def _render_markdown(payload: Dict[str, Any], *, roster_csv_path: Path) -> str:
    meta = payload["metadata"]
    inv = payload["hit_inventory"]
    ranking = payload["ranking"]
    budgets = payload["budgets"]
    morph = payload["morphology"]
    lifts = payload["signal_lift"]
    sig = payload["arena_finalist_signatures"]

    def _lift_text(block: Dict[str, Any]) -> str:
        lift = block.get("lift")
        lift_text = f"{lift:.2f}x" if isinstance(lift, (int, float)) else "n/a"
        return (
            f"{block['subset_count']}/{meta['credited_hits']} ({_pct(block['subset_count'], meta['credited_hits'])}) "
            f"vs {block['all_count']}/{meta['total_events']} ({_pct(block['all_count'], meta['total_events'])}); lift {lift_text}"
        )

    lines: List[str] = []
    lines.append("# Analysis Arena Deep Hit Analysis")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(f"- Window root: `{meta['window_root']}`")
    lines.append(f"- Dates: `{meta['window_dates'][0]}` to `{meta['window_dates'][-1]}`" if meta["window_dates"] else "- Dates: _none_")
    lines.append(f"- Total graded events: `{meta['total_events']}`")
    lines.append(f"- Credited hit roster CSV: `{safe_rel(roster_csv_path)}`")
    lines.append("- Hit universe: any event with `play_inclusive_hit == True`.")
    lines.append("- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.")
    lines.append("- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.")
    lines.append("")
    lines.append("## 2. Hit Inventory")
    lines.append("")
    lines.append(f"- Credited hits: `{inv['credited_hits']}` ({_pct(inv['credited_hits'], meta['total_events'])})")
    lines.append(f"- Straight hits: `{inv['straight_hits']}` ({_pct(inv['straight_hits'], meta['total_events'])})")
    lines.append(f"- Strict boxed hits: `{inv['strict_box_hits']}` ({_pct(inv['strict_box_hits'], meta['total_events'])})")
    lines.append(f"- Canonical / any-box hits: `{inv['box_any_hits']}` ({_pct(inv['box_any_hits'], meta['total_events'])})")
    lines.append(f"- VTRAC hits: `{inv['vtrac_hits']}` ({_pct(inv['vtrac_hits'], meta['total_events'])})")
    lines.append(f"- VTRAC-only hits: `{inv['vtrac_only_hits']}` ({_pct(inv['vtrac_only_hits'], meta['total_events'])})")
    lines.append(
        "- Primary hit classes: "
        + (", ".join(f"`{k}` x{v}" for k, v in sorted(inv["hit_class_counts"].items())) or "_none_")
    )
    lines.append(
        "- Credit signatures: "
        + (", ".join(f"`{k}` x{v}" for k, v in sorted(inv["credit_signature_counts"].items())) or "_none_")
    )
    lines.append("")
    lines.append("## 3. Ranking / State Targeting")
    lines.append("")
    if not ranking.get("evaluable"):
        lines.append("- Cross-state rank tiers, median winner rank, and rank-derived target hits: `NOT_EVALUABLE`.")
        lines.append(f"- Reason: `{ranking.get('reason') or RANK_INTEGRITY_INVALID_STATIC_ORDER}`.")
    else:
        lines.append(
            "- Rank tiers across credited hits: "
            + (", ".join(f"`{k}` x{v}" for k, v in sorted(ranking["rank_tier_counts"].items())) or "_none_")
        )
        lines.append(f"- Median board rank, all hits: `{_format_float(ranking['median_rank_all_hits']) or 'n/a'}`")
        lines.append(f"- Median board rank, high-conviction hits: `{_format_float(ranking['median_rank_high_conviction']) or 'n/a'}`")
        lines.append(f"- Median board rank, VTRAC-only hits: `{_format_float(ranking['median_rank_vtrac_only']) or 'n/a'}`")
        lines.append(f"- Top-primary-target hits: `{ranking['top_primary_target_hits']}`")
        lines.append(f"- Secondary-target hits: `{ranking['secondary_target_hits']}`")
        lines.append(f"- Best-clean-host hits: `{ranking['best_clean_host_hits']}`")
    lines.append(f"- Highest-context-support hits: `{ranking['highest_context_support_hits']}`")
    lines.append("")
    lines.append("## 4. Budget Floor")
    lines.append("")
    lines.append(
        "- Minimum budget for inclusive hits: "
        + (", ".join(f"`{k}` x{v}" for k, v in budgets["min_budget_inclusive"].items()) or "_none_")
    )
    lines.append(
        "- Minimum budget for box-any hits: "
        + (", ".join(f"`{k}` x{v}" for k, v in budgets["min_budget_box_any"].items()) or "_none_")
    )
    lines.append(
        "- Minimum budget for straight hits: "
        + (", ".join(f"`{k}` x{v}" for k, v in budgets["min_budget_straight"].items()) or "_none_")
    )
    lines.append("")
    lines.append("## 5. Hit Morphology")
    lines.append("")
    lines.append(
        "- Inventory types: "
        + (", ".join(f"`{k}` x{v}" for k, v in morph["inventory_types"].items()) or "_none_")
    )
    lines.append(
        "- Double-context strength: "
        + (", ".join(f"`{k}` x{v}" for k, v in morph["double_context_strength"].items() if k != "_none_") or "_none_")
    )
    lines.append(
        "- Blackapple status across hits: "
        + (", ".join(f"`{k}` x{v}" for k, v in morph["blackapple_status"].items()) or "_none_")
    )
    lines.append(
        "- Top compound-event tags across hits: "
        + (", ".join(f"`{k}` x{v}" for k, v in sorted(morph["compound_top_events"].items(), key=lambda item: (-item[1], item[0]))[:8]) or "_none_")
    )
    lines.append("")
    lines.append("## 6. Signal Lift")
    lines.append("")
    for key in (
        "arena_box_signal",
        "arena_exact_signal",
        "candidate_box_hit",
        "candidate_straight_hit",
        "candidate_vtrac_hit",
        "profit_alert_direct_match",
        "profit_alert_implied_match",
        "compound_event_present",
        "sandbox_box_seed",
        "sandbox_exact_seed",
        "sandbox_vt_seed",
        "preserved_not_budgeted",
    ):
        label = key.replace("_", " ")
        lines.append(f"- `{label}`: {_lift_text(lifts[key]['all'])}")
    lines.append("")
    lines.append("## 7. Arena Final-Candidate Signatures")
    lines.append("")
    lines.append(
        "- Signature buckets: "
        + (", ".join(f"`{k}` x{v}" for k, v in sig["signature_buckets"].items()) or "_none_")
    )
    lines.append(
        "- Top signature hits: "
        + (
            ", ".join(
                f"`{row['date']} {row['state_key']} {row['period']} {row['winner']}`[{row['hit_primary_class']}, {row['arena_final_candidate_signature']}]"
                for row in sig["top_signature_hits"][:8]
            )
            or "_none_"
        )
    )
    lines.append(
        (
            "- Low-rank but converted hits: "
            if ranking.get("evaluable")
            else "- Low-rank converted-hit analysis: `NOT_EVALUABLE`; "
        )
        + (
            ", ".join(
                f"`{row['date']} {row['state_key']} {row['period']} {row['winner']}`[{row['hit_primary_class']}, analytical rank {row['board_rank'] or 'n/a'}]"
                for row in sig["low_rank_hits"][:8]
            )
            or "_none_"
        )
    )
    lines.append(
        "- VTRAC-only examples: "
        + (
            ", ".join(
                f"`{row['date']} {row['state_key']} {row['period']} {row['winner']}`[min {row['min_budget_inclusive'] or 'n/a'}]"
                for row in sig["vtrac_only_examples"][:8]
            )
            or "_none_"
        )
    )
    lines.append(
        "- Double / mirror examples: "
        + (
            ", ".join(
                f"`{row['date']} {row['state_key']} {row['period']} {row['winner']}`[{row['inventory_type']}, due rank {row['due_double_period_rank'] or row['due_double_combined_rank'] or 'n/a'}, {row['double_context_strength'] or 'n/a'}]"
                for row in sig["double_examples"][:8]
            )
            or "_none_"
        )
    )
    lines.append("")
    lines.append("## 8. Design Read")
    lines.append("")
    lines.append("- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.")
    lines.append("- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.")
    lines.append("- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.")
    return "\n".join(lines).rstrip() + "\n"


def build_payload(
    *,
    window_root: Path,
    runs_root: Path,
    sharepacks_root: Path,
    profile: str,
    experiment_tag: str,
) -> Dict[str, Any]:
    roster = _build_roster(
        window_root=window_root,
        runs_root=runs_root,
        sharepacks_root=sharepacks_root,
        profile=profile,
        experiment_tag=experiment_tag,
    )
    summary = _summary_payload(window_root, roster)
    return {
        "roster_rows": roster["hit_rows"],
        **summary,
    }


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    runs_root = _resolve_path(args.runs_root)
    sharepacks_root = _resolve_path(args.sharepacks_root)
    outputs = _default_outputs(window_root)
    out_md = _resolve_path(args.out_md) if args.out_md else outputs["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else outputs["json"]
    out_csv = _resolve_path(args.out_csv) if args.out_csv else outputs["csv"]

    payload = build_payload(
        window_root=window_root,
        runs_root=runs_root,
        sharepacks_root=sharepacks_root,
        profile=str(args.profile or "tool_only").strip(),
        experiment_tag=str(args.experiment_tag or "arena_v0").strip(),
    )
    md = _render_markdown(payload, roster_csv_path=out_csv)
    _write_csv(out_csv, payload["roster_rows"], force=args.force)
    _write_text(out_md, md, force=args.force)
    json_payload = dict(payload)
    json_payload["roster_csv_path"] = safe_rel(out_csv)
    _write_json(out_json, json_payload, force=args.force)
    print(f"Wrote: {safe_rel(out_csv)}")
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
