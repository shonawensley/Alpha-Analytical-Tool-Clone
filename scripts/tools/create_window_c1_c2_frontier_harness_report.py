#!/usr/bin/env python3
"""Create a C1/C2 vertical-frontier harness report for an Analysis Arena window."""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import iter_window_dates, safe_rel


DEFAULT_WINNER_HTML_ROOT = REPO_ROOT / "reports" / "stable" / "winners_by_date"
DEFAULT_TRUTH_SHAREPACKS_ROOT = REPO_ROOT / "sharepacks"

WINNER_REPORT_RE = re.compile(
    r"(?P<state>.+?)_vtrac(?P<vtrac>\d+)_winner_(?P<winner>\d{3})_(?P<stamp>\d{8}_\d{6})\.(?P<ext>json|html)$",
    re.IGNORECASE,
)

SECTION_WEIGHTS = {"Combined": 1.35, "Evening": 1.0, "Midday": 1.0}
ROW_WEIGHTS = {"R2": 1.0, "R4": 1.4, "R6": 1.9, "R8": 2.4}
COLUMN_WEIGHTS = {"1": 2.5, "2": 2.0, "3": 1.4, "4": 1.0}
TERMINAL_COLS = {"1", "2"}
FEEDER_COLS = {"3", "4"}
VALID_ROW_TYPES = tuple(ROW_WEIGHTS.keys())
TRUTH_TAGS = {
    "hit-winner",
    "hit-winner-gap",
    "hit-vt-straight",
    "hit-vt-straight-gap",
    "hit-family",
    "hit-family-gap",
    "ls-box",
    "ls-box-edge",
}
SIGNATURE_PRIORITY = (
    "DOUBLE_FRONTIER",
    "LITERAL_FRONTIER",
    "FEEDER_TO_FRONTIER",
    "HIDDEN_COMPRESSED_FRONTIER",
    "FAMILY_FRONTIER",
    "VTRAC_FRONTIER",
    "MIXED_COMPOUND_FRONTIER",
)
DOUBLE_STRENGTH_VALUE = {"WEAK": 0.35, "MEDIUM": 0.70, "STRONG": 1.0}


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--winner-html-root",
        default=str(DEFAULT_WINNER_HTML_ROOT),
        help="Root containing winner HTML/JSON outputs by date/state (default: reports/stable/winners_by_date)",
    )
    ap.add_argument(
        "--truth-sharepacks-root",
        default=str(DEFAULT_TRUTH_SHAREPACKS_ROOT),
        help="Truth sharepacks root used as a fallback winner-report source (default: sharepacks)",
    )
    ap.add_argument("--ledger-csv", default="", help="Optional performance-gap ledger CSV path.")
    ap.add_argument("--hit-roster-csv", default="", help="Optional deep-hit roster CSV path.")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-csv", default="", help="Optional frontier-cases CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> Any:
    return json.loads(_read_text(path))


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


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


def _default_outputs(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "md": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
        "csv": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv",
    }


def _default_ledger_path(window_root: Path) -> Path:
    return window_root / f"{window_root.name}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv"


def _default_hit_roster_path(window_root: Path) -> Path:
    return window_root / f"{window_root.name}__ANALYSIS_ARENA__HIT_ROSTER.csv"


def _bool01(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return int(float(text))
    except Exception:
        return default


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _clamp01(value: float) -> float:
    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value


def _pct(count: int, total: int) -> str:
    if total <= 0:
        return "0.0%"
    return f"{100.0 * count / total:.1f}%"


def _fmt_score(value: float) -> str:
    return f"{value:.3f}"


def _winner_family(winner: str) -> List[str]:
    if len(str(winner or "")) != 3:
        return []
    chars = list(str(winner))
    return sorted({"".join(p) for p in itertools.permutations(chars)})


def _winner_vtrac_values(winner: str) -> List[str]:
    import modules.vtrac_reference as vr  # type: ignore

    out: List[str] = []
    idx = vr.get_vtrac_index(str(winner or "").strip())
    if isinstance(idx, int):
        out.append(str(idx))
    return out


def _vtrac_value_set(text: str) -> set[str]:
    import modules.vtrac_reference as vr  # type: ignore

    out: set[str] = set()
    for ch in _digits_only(text):
        idx = vr.get_vtrac_index(ch * 3)
        if isinstance(idx, int):
            out.add(str(idx))
    return out


def _report_match_key(path: Path, payload: Dict[str, Any]) -> Tuple[str, str]:
    match = WINNER_REPORT_RE.search(path.name)
    if match:
        return match.group("winner"), match.group("stamp")
    winner = _digits_only(payload.get("winner_combo") or "")
    return winner, str(payload.get("timestamp") or "")


def _dedupe_report_paths(paths: Sequence[Path]) -> Dict[str, Path]:
    chosen: Dict[str, Tuple[str, Path]] = {}
    for path in sorted(paths):
        try:
            payload = _read_json(path)
        except Exception:
            continue
        winner, stamp = _report_match_key(path, payload)
        if not winner:
            continue
        current = chosen.get(winner)
        if current is None or stamp > current[0]:
            chosen[winner] = (stamp, path)
    return {winner: path for winner, (_, path) in chosen.items()}


def _report_paths_for_state_date(
    *,
    results_date: str,
    state_key: str,
    winner_html_root: Path,
    truth_sharepacks_root: Path,
) -> Dict[str, Path]:
    preferred = winner_html_root / results_date / state_key
    fallback = truth_sharepacks_root / results_date / state_key / "winners" / state_key
    paths: List[Path] = []
    for base in (preferred, fallback):
        if base.exists():
            paths.extend(sorted(base.glob("*.json")))
    return _dedupe_report_paths(paths)


def _score_weight(*, section: str, row_type: str, column: str) -> float:
    return (
        SECTION_WEIGHTS.get(section, 1.0)
        * ROW_WEIGHTS.get(row_type, 1.0)
        * COLUMN_WEIGHTS.get(column, 1.0)
    )


def _cell_tags(cell: Dict[str, Any]) -> set[str]:
    return {str(tag).strip() for tag in (cell.get("tags") or []) if str(tag).strip()}


def _cell_text(cell: Dict[str, Any]) -> str:
    return str(cell.get("text") or "").strip()


def _iter_frontier_cells(payload: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    tables = payload.get("tables") or {}
    for section, rows in tables.items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            row_type = str(row.get("RowType") or "").strip()
            if row_type not in VALID_ROW_TYPES:
                continue
            set_name = str(row.get("Set") or "").strip()
            draw = str(row.get("Draw") or "").strip()
            cells = row.get("cells") or {}
            for column in ("4", "3", "2", "1"):
                cell = cells.get(column) or {}
                text = _cell_text(cell)
                tags = _cell_tags(cell)
                yield {
                    "section": str(section),
                    "set": set_name,
                    "draw": draw,
                    "row_type": row_type,
                    "column": column,
                    "text": text,
                    "digits": _digits_only(text),
                    "tags": tags,
                }


def _channel_counts_from_tags(tags: set[str]) -> Dict[str, float]:
    return {
        "winner": 1.0 if "hit-winner" in tags else 0.0,
        "winner_gap": 1.0 if "hit-winner-gap" in tags else 0.0,
        "family": 1.0 if "hit-family" in tags else 0.0,
        "family_gap": 1.0 if "hit-family-gap" in tags else 0.0,
        "vt": 1.0 if "hit-vt-straight" in tags else 0.0,
        "vt_gap": 1.0 if "hit-vt-straight-gap" in tags else 0.0,
        "ls": 1.0 if ("ls-box" in tags or "ls-box-edge" in tags) else 0.0,
    }


def _aggregate_event_context(ledger_rows: Sequence[Dict[str, str]], hit_rows: Sequence[Dict[str, str]]) -> Dict[str, Any]:
    board_ranks = sorted(
        {_safe_int(row.get("board_rank")) for row in ledger_rows if _safe_int(row.get("board_rank")) > 0}
    )
    matched_periods = sorted({str(row.get("period") or "").strip() for row in ledger_rows if str(row.get("period") or "").strip()})
    credited_periods = sorted({str(row.get("period") or "").strip() for row in hit_rows if str(row.get("period") or "").strip()})

    def _hit_flag(rows: Sequence[Dict[str, str]], key: str) -> bool:
        return any(_bool01(row.get(key)) for row in rows)

    straight_hit_any = _hit_flag(hit_rows, "play_straight_hit")
    boxed_hit_any = _hit_flag(hit_rows, "play_box_any_hit")
    vtrac_straight_hit_any = any(_bool01(row.get("play_straight_hit")) and _bool01(row.get("play_vtrac_hit")) for row in hit_rows)
    vtrac_boxed_hit_any = any(_bool01(row.get("play_box_any_hit")) and _bool01(row.get("play_vtrac_hit")) for row in hit_rows)

    hit_labels: List[str] = []
    if straight_hit_any:
        hit_labels.append("STRAIGHT")
    if boxed_hit_any:
        hit_labels.append("BOXED")
    if vtrac_straight_hit_any:
        hit_labels.append("VTRAC_STRAIGHT")
    if vtrac_boxed_hit_any:
        hit_labels.append("VTRAC_BOXED")

    blackapple_statuses = [str(row.get("blackapple_status") or "").strip().upper() for row in hit_rows if str(row.get("blackapple_status") or "").strip()]
    best_blackapple_status = "OFF"
    for status in ("ALERT", "WATCH", "OFF"):
        if status in blackapple_statuses:
            best_blackapple_status = status
            break

    return {
        "matched_event_count": len(ledger_rows),
        "matched_periods": matched_periods,
        "credited_event_count": len(hit_rows),
        "credited_periods": credited_periods,
        "best_board_rank": board_ranks[0] if board_ranks else 0,
        "board_rank_list": ",".join(str(rank) for rank in board_ranks),
        "top_primary_target_any": any(_bool01(row.get("top_primary_target")) for row in ledger_rows),
        "secondary_target_any": any(_bool01(row.get("secondary_target")) for row in ledger_rows),
        "best_clean_host_any": any(_bool01(row.get("best_clean_host")) for row in ledger_rows),
        "highest_context_support_any": any(_bool01(row.get("highest_context_support_state")) for row in ledger_rows),
        "play_card_any_box_any": any(_bool01(row.get("play_card_any_box")) for row in ledger_rows),
        "play_card_any_exact_any": any(_bool01(row.get("play_card_any_exact")) for row in ledger_rows),
        "straight_hit_any": straight_hit_any,
        "boxed_hit_any": boxed_hit_any,
        "vtrac_straight_hit_any": vtrac_straight_hit_any,
        "vtrac_boxed_hit_any": vtrac_boxed_hit_any,
        "hit_class_rollup": "|".join(hit_labels) if hit_labels else "NONE",
        "arena_final_candidate_signature_best": next(
            (label for label in ("CLEAR_ARENA_FINALIST", "PARTIAL_ARENA_FINALIST", "LIGHT_ARENA_FINALIST") if any(str(row.get("arena_final_candidate_signature") or "") == label for row in hit_rows)),
            "CONTROL_ARM_ONLY_CATCH" if hit_rows else "",
        ),
        "blackapple_status_best": best_blackapple_status,
        "compound_event_any": any(_bool01(row.get("compound_event_present")) for row in hit_rows),
        "due_double_ranked_any": any(_safe_int(row.get("due_double_draws_since_double")) >= 3 for row in hit_rows),
        "double_context_strength_best": next(
            (label for label in ("STRONG", "MEDIUM", "WEAK") if any(str(row.get("double_context_strength") or "") == label for row in hit_rows)),
            "",
        ),
        "inventory_types": ",".join(sorted({str(row.get("inventory_type") or "").strip() for row in hit_rows if str(row.get("inventory_type") or "").strip()})),
    }


def _stats_counts(payload: Dict[str, Any], key: str) -> Dict[str, int]:
    raw = payload.get("stats", {}).get(key) or {}
    return {str(k): _safe_int(v) for k, v in raw.items()}


def _repeated_digit_flag(winner: str) -> bool:
    counts = Counter(ch for ch in str(winner or "") if ch.isdigit())
    return any(count >= 2 for count in counts.values())


def _classify_signature(
    *,
    literal: float,
    family: float,
    vtrac: float,
    hidden: float,
    feeder: float,
    double_anchor: float,
) -> str:
    if literal >= 0.34 and literal >= vtrac and literal + 0.18 >= family:
        return "LITERAL_FRONTIER"
    if hidden >= 0.56 and max(family, vtrac) >= 0.24:
        return "HIDDEN_COMPRESSED_FRONTIER"
    if family >= vtrac + 0.08 and family >= 0.26:
        return "FAMILY_FRONTIER"
    if feeder >= 0.52 and max(literal, family, vtrac) >= 0.24:
        return "FEEDER_TO_FRONTIER"
    if vtrac >= 0.22:
        return "VTRAC_FRONTIER"
    if double_anchor >= 0.72:
        return "DOUBLE_FRONTIER"
    return "MIXED_COMPOUND_FRONTIER"


def _signature_strength_label(score_100: float) -> str:
    if score_100 >= 68.0:
        return "STRONG"
    if score_100 >= 46.0:
        return "MEDIUM"
    return "WEAK"


def _case_from_payload(
    *,
    results_date: str,
    state_key: str,
    report_path: Path,
    payload: Dict[str, Any],
    ledger_rows: Sequence[Dict[str, str]],
    hit_rows: Sequence[Dict[str, str]],
) -> Dict[str, Any]:
    winner = _digits_only(payload.get("winner_combo") or "")
    family = _winner_family(winner)
    winner_vtracs = _winner_vtrac_values(winner)

    terminal_weight_possible = 0.0
    terminal_signal_cells = 0
    terminal_cells = 0
    feeder_signal_cells = 0
    feeder_cells = 0

    winner_weight = 0.0
    winner_gap_weight = 0.0
    family_weight = 0.0
    family_gap_weight = 0.0
    vtrac_weight = 0.0
    vtrac_gap_weight = 0.0
    ls_terminal_weight = 0.0
    ls_feeder_weight = 0.0

    terminal_groups: set[Tuple[str, str, str, str]] = set()
    feeder_groups: set[Tuple[str, str, str, str]] = set()
    signal_row_types: set[str] = set()
    signal_set_variants: set[Tuple[str, str]] = set()
    all_set_variants: set[Tuple[str, str]] = set()
    frontier_digits: set[str] = set()
    frontier_vtracs: set[str] = set()
    terminal_examples: List[str] = []

    c1_winner_hits = 0
    c2_winner_hits = 0
    c1_family_hits = 0
    c2_family_hits = 0
    c1_vt_hits = 0
    c2_vt_hits = 0

    for cell in _iter_frontier_cells(payload):
        section = cell["section"]
        set_name = cell["set"]
        draw = cell["draw"]
        row_type = cell["row_type"]
        column = cell["column"]
        digits = cell["digits"]
        tags = cell["tags"]
        channels = _channel_counts_from_tags(tags)
        signal_any = bool(tags & TRUTH_TAGS)
        group_key = (section, set_name, draw, row_type)
        all_set_variants.add((section, set_name))
        weight = _score_weight(section=section, row_type=row_type, column=column)

        if column in TERMINAL_COLS:
            terminal_cells += 1
            terminal_weight_possible += weight
            if signal_any:
                terminal_signal_cells += 1
                terminal_groups.add(group_key)
                signal_row_types.add(row_type)
                signal_set_variants.add((section, set_name))
                if len(terminal_examples) < 8 and digits:
                    terminal_examples.append(f"{section}/{set_name}/{draw}/{row_type}/C{column}:{digits}")
        elif column in FEEDER_COLS:
            feeder_cells += 1
            if signal_any:
                feeder_signal_cells += 1
                feeder_groups.add(group_key)

        if column in {"1", "2", "3", "4"} and signal_any and digits:
            frontier_digits.update(set(digits))
            frontier_vtracs.update(_vtrac_value_set(digits))

        if column in TERMINAL_COLS:
            winner_weight += weight * channels["winner"]
            winner_gap_weight += weight * channels["winner_gap"]
            family_weight += weight * channels["family"]
            family_gap_weight += weight * channels["family_gap"]
            vtrac_weight += weight * channels["vt"]
            vtrac_gap_weight += weight * channels["vt_gap"]
            ls_terminal_weight += weight * channels["ls"]
        elif column in FEEDER_COLS:
            ls_feeder_weight += weight * channels["ls"]

        if column == "1":
            c1_winner_hits += int(channels["winner"] + channels["winner_gap"] > 0)
            c1_family_hits += int(channels["family"] + channels["family_gap"] > 0)
            c1_vt_hits += int(channels["vt"] + channels["vt_gap"] > 0)
        if column == "2":
            c2_winner_hits += int(channels["winner"] + channels["winner_gap"] > 0)
            c2_family_hits += int(channels["family"] + channels["family_gap"] > 0)
            c2_vt_hits += int(channels["vt"] + channels["vt_gap"] > 0)

    terminal_den = terminal_weight_possible or 1.0
    literal_frontier_score = _clamp01((winner_weight + 0.60 * winner_gap_weight) / terminal_den)
    family_frontier_score = _clamp01((family_weight + 0.55 * family_gap_weight) / terminal_den)
    vtrac_frontier_base = _clamp01((vtrac_weight + 0.60 * vtrac_gap_weight) / terminal_den)
    frontier_purity_score = _clamp01(terminal_signal_cells / terminal_cells) if terminal_cells else 0.0
    vertical_stability_score = _clamp01(sum(ROW_WEIGHTS[row] for row in signal_row_types) / sum(ROW_WEIGHTS.values())) if signal_row_types else 0.0
    cross_variant_echo_score = _clamp01(len(signal_set_variants) / len(all_set_variants)) if all_set_variants else 0.0
    feeder_progression_score = _clamp01(len(feeder_groups & terminal_groups) / len(terminal_groups)) if terminal_groups else 0.0

    unique_digits = len(frontier_digits)
    unique_vtracs = len(frontier_vtracs)
    if unique_digits <= 1:
        compression_score = 0.0
    elif unique_vtracs <= 1:
        compression_score = 1.0
    else:
        compression_score = _clamp01(1.0 - ((unique_vtracs - 1) / (unique_digits - 1)))
    vtrac_frontier_score = _clamp01(0.70 * vtrac_frontier_base + 0.30 * compression_score)

    occurrence = _stats_counts(payload, "pattern_occurrence")
    persistence = _stats_counts(payload, "pattern_persistence")
    stability = _stats_counts(payload, "pattern_stability")
    straight_counts = _stats_counts(payload, "straight_counts")

    winner_occ = occurrence.get(winner, 0)
    best_family_occ = max((occurrence.get(combo, 0) for combo in family), default=0)
    best_family_persistence = max((persistence.get(combo, 0) for combo in family), default=0)
    best_family_stability = max((stability.get(combo, 0) for combo in family), default=0)
    winner_straight_count = straight_counts.get(winner, 0)
    occ_gap_ratio = _clamp01((best_family_occ - winner_occ) / max(best_family_occ, 1)) if best_family_occ else 0.0
    hidden_tag_factor = 1.0 if literal_frontier_score < 0.14 and (family_frontier_score > 0.18 or vtrac_frontier_base > 0.18) else (0.55 if winner_gap_weight > 0 else 0.0)
    hidden_winner_score = _clamp01(0.60 * occ_gap_ratio + 0.40 * hidden_tag_factor)

    event_context = _aggregate_event_context(ledger_rows, hit_rows)
    repeat_digit = _repeated_digit_flag(winner)
    double_anchor_score = _clamp01(
        0.40 * (1.0 if repeat_digit else 0.0)
        + 0.35 * DOUBLE_STRENGTH_VALUE.get(event_context["double_context_strength_best"], 0.0)
        + 0.25 * max(family_frontier_score, literal_frontier_score, feeder_progression_score)
    )

    signature_type = _classify_signature(
        literal=literal_frontier_score,
        family=family_frontier_score,
        vtrac=vtrac_frontier_score,
        hidden=hidden_winner_score,
        feeder=feeder_progression_score,
        double_anchor=double_anchor_score,
    )
    frontier_strength_score = 100.0 * (
        0.24 * max(literal_frontier_score, family_frontier_score, vtrac_frontier_score)
        + 0.14 * vertical_stability_score
        + 0.12 * cross_variant_echo_score
        + 0.12 * frontier_purity_score
        + 0.10 * compression_score
        + 0.12 * feeder_progression_score
        + 0.16 * max(hidden_winner_score, double_anchor_score)
    )
    signature_strength = _signature_strength_label(frontier_strength_score)

    fired_tests: List[str] = []
    if literal_frontier_score >= 0.22:
        fired_tests.append("literal_frontier_v1")
    if family_frontier_score >= 0.22:
        fired_tests.append("family_frontier_v1")
    if vtrac_frontier_score >= 0.22:
        fired_tests.append("vtrac_frontier_v1")
    if hidden_winner_score >= 0.45:
        fired_tests.append("hidden_mask_v1")
    if compression_score >= 0.40:
        fired_tests.append("compression_v1")
    if feeder_progression_score >= 0.42:
        fired_tests.append("feeder_progression_v1")
    if double_anchor_score >= 0.45:
        fired_tests.append("double_anchor_v1")
    if cross_variant_echo_score >= 0.45:
        fired_tests.append("cross_variant_echo_v1")
    if vertical_stability_score >= 0.45:
        fired_tests.append("vertical_stability_v1")

    return {
        "date": results_date,
        "state_key": state_key,
        "winner": winner,
        "winner_family": ",".join(family),
        "winner_vtrac_values": ",".join(winner_vtracs),
        "source_json": safe_rel(report_path),
        "winner_index": payload.get("index", ""),
        "winner_patterns_count": len(payload.get("patterns") or []),
        "matched_event_count": event_context["matched_event_count"],
        "matched_periods": ",".join(event_context["matched_periods"]),
        "credited_event_count": event_context["credited_event_count"],
        "credited_periods": ",".join(event_context["credited_periods"]),
        "best_board_rank": event_context["best_board_rank"],
        "board_rank_list": event_context["board_rank_list"],
        "top_primary_target_any": event_context["top_primary_target_any"],
        "secondary_target_any": event_context["secondary_target_any"],
        "best_clean_host_any": event_context["best_clean_host_any"],
        "highest_context_support_any": event_context["highest_context_support_any"],
        "play_card_any_box_any": event_context["play_card_any_box_any"],
        "play_card_any_exact_any": event_context["play_card_any_exact_any"],
        "straight_hit_any": event_context["straight_hit_any"],
        "boxed_hit_any": event_context["boxed_hit_any"],
        "vtrac_straight_hit_any": event_context["vtrac_straight_hit_any"],
        "vtrac_boxed_hit_any": event_context["vtrac_boxed_hit_any"],
        "hit_class_rollup": event_context["hit_class_rollup"],
        "arena_final_candidate_signature_best": event_context["arena_final_candidate_signature_best"],
        "blackapple_status_best": event_context["blackapple_status_best"],
        "compound_event_any": event_context["compound_event_any"],
        "due_double_ranked_any": event_context["due_double_ranked_any"],
        "double_context_strength_best": event_context["double_context_strength_best"],
        "inventory_types": event_context["inventory_types"],
        "terminal_cell_count": terminal_cells,
        "terminal_signal_cells": terminal_signal_cells,
        "feeder_cell_count": feeder_cells,
        "feeder_signal_cells": feeder_signal_cells,
        "c1_winner_hits": c1_winner_hits,
        "c2_winner_hits": c2_winner_hits,
        "c1_family_hits": c1_family_hits,
        "c2_family_hits": c2_family_hits,
        "c1_vt_hits": c1_vt_hits,
        "c2_vt_hits": c2_vt_hits,
        "winner_occurrence": winner_occ,
        "best_family_occurrence": best_family_occ,
        "best_family_persistence": best_family_persistence,
        "best_family_stability": best_family_stability,
        "winner_straight_count": winner_straight_count,
        "literal_frontier_score": round(literal_frontier_score, 6),
        "family_frontier_score": round(family_frontier_score, 6),
        "vtrac_frontier_score": round(vtrac_frontier_score, 6),
        "vertical_stability_score": round(vertical_stability_score, 6),
        "cross_variant_echo_score": round(cross_variant_echo_score, 6),
        "frontier_purity_score": round(frontier_purity_score, 6),
        "compression_score": round(compression_score, 6),
        "hidden_winner_score": round(hidden_winner_score, 6),
        "feeder_progression_score": round(feeder_progression_score, 6),
        "double_anchor_score": round(double_anchor_score, 6),
        "frontier_strength_score": round(frontier_strength_score, 3),
        "signature_strength": signature_strength,
        "frontier_signature_type": signature_type,
        "fired_tests": ",".join(fired_tests),
        "terminal_examples": " | ".join(terminal_examples),
    }


def _load_cases(
    *,
    window_root: Path,
    winner_html_root: Path,
    truth_sharepacks_root: Path,
    ledger_rows: Sequence[Dict[str, str]],
    hit_rows: Sequence[Dict[str, str]],
) -> Tuple[List[Dict[str, Any]], List[str]]:
    ledger_by_key: Dict[Tuple[str, str, str], List[Dict[str, str]]] = defaultdict(list)
    hit_by_key: Dict[Tuple[str, str, str], List[Dict[str, str]]] = defaultdict(list)
    states_by_date: Dict[str, set[str]] = defaultdict(set)
    for row in ledger_rows:
        date = str(row.get("date") or "").strip()
        state_key = str(row.get("state_key") or "").strip()
        winner = _digits_only(row.get("winner") or "")
        if not (date and state_key and winner):
            continue
        ledger_by_key[(date, state_key, winner)].append(row)
        states_by_date[date].add(state_key)
    for row in hit_rows:
        date = str(row.get("date") or "").strip()
        state_key = str(row.get("state_key") or "").strip()
        winner = _digits_only(row.get("winner") or "")
        if date and state_key and winner:
            hit_by_key[(date, state_key, winner)].append(row)

    warnings: List[str] = []
    cases: List[Dict[str, Any]] = []
    for results_date in iter_window_dates(window_root):
        for state_key in sorted(states_by_date.get(results_date, set())):
            reports = _report_paths_for_state_date(
                results_date=results_date,
                state_key=state_key,
                winner_html_root=winner_html_root,
                truth_sharepacks_root=truth_sharepacks_root,
            )
            if not reports:
                warnings.append(f"{results_date}:{state_key}: no winner report JSON found under preferred or fallback roots")
                continue
            for winner, report_path in sorted(reports.items()):
                matched_ledger = ledger_by_key.get((results_date, state_key, winner), [])
                if not matched_ledger:
                    continue
                try:
                    payload = _read_json(report_path)
                except Exception as exc:
                    warnings.append(f"{results_date}:{state_key}:{winner}: failed to parse {safe_rel(report_path)} ({exc})")
                    continue
                cases.append(
                    _case_from_payload(
                        results_date=results_date,
                        state_key=state_key,
                        report_path=report_path,
                        payload=payload,
                        ledger_rows=matched_ledger,
                        hit_rows=hit_by_key.get((results_date, state_key, winner), []),
                    )
                )
    cases.sort(key=lambda row: (-float(row.get("frontier_strength_score") or 0.0), row.get("date", ""), row.get("state_key", ""), row.get("winner", "")))
    return cases, warnings


def _promotion_queue(cases: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    total = len(cases)
    if total <= 0:
        return []

    def _avg(key: str) -> float:
        vals = [float(row.get(key) or 0.0) for row in cases]
        return sum(vals) / len(vals) if vals else 0.0

    def _share(pred) -> float:
        return sum(1 for row in cases if pred(row)) / total

    queue: List[Dict[str, Any]] = []
    family_share = _share(lambda row: row.get("frontier_signature_type") == "FAMILY_FRONTIER")
    if family_share >= 0.20 or _avg("family_frontier_score") >= 0.32:
        queue.append(
            {
                "promote_class": "TEST_IN_SCORING",
                "signal": "C1/C2 family-frontier persistence",
                "evidence": f"family-frontier cases {family_share:.1%}; avg family score {_avg('family_frontier_score'):.3f}",
            }
        )
    hidden_share = _share(lambda row: float(row.get("hidden_winner_score") or 0.0) >= 0.50)
    if hidden_share >= 0.15:
        queue.append(
            {
                "promote_class": "TEST_IN_TRANSLATOR",
                "signal": "Hidden compressed winner-family frontier",
                "evidence": f"hidden score >=0.50 in {hidden_share:.1%} of cases",
            }
        )
    feeder_share = _share(lambda row: float(row.get("feeder_progression_score") or 0.0) >= 0.45)
    if feeder_share >= 0.18:
        queue.append(
            {
                "promote_class": "TEST_IN_BRAIN2",
                "signal": "Feeder-to-frontier progression",
                "evidence": f"feeder progression >=0.45 in {feeder_share:.1%} of cases",
            }
        )
    double_share = _share(lambda row: float(row.get("double_anchor_score") or 0.0) >= 0.55)
    if double_share >= 0.15:
        queue.append(
            {
                "promote_class": "TEST_IN_SCORING",
                "signal": "Double-anchored frontier compression",
                "evidence": f"double-anchor >=0.55 in {double_share:.1%} of cases",
            }
        )
    vtrac_share = _share(lambda row: float(row.get("vtrac_frontier_score") or 0.0) >= 0.35)
    if vtrac_share >= 0.20:
        queue.append(
            {
                "promote_class": "MONITOR_AND_COMPARE",
                "signal": "VTRAC frontier corridor",
                "evidence": f"vtrac frontier >=0.35 in {vtrac_share:.1%} of cases",
            }
        )
    return queue


def _summary_payload(window_root: Path, cases: Sequence[Dict[str, Any]], warnings: Sequence[str]) -> Dict[str, Any]:
    signature_counts = Counter(str(row.get("frontier_signature_type") or "") for row in cases)
    signature_strength_counts = Counter(str(row.get("signature_strength") or "") for row in cases)
    hit_class_counts = Counter(str(row.get("hit_class_rollup") or "NONE") for row in cases)
    best_blackapple_counts = Counter(str(row.get("blackapple_status_best") or "OFF") for row in cases)
    inventory_type_counts = Counter()
    for row in cases:
        for item in str(row.get("inventory_types") or "").split(","):
            token = item.strip()
            if token:
                inventory_type_counts[token] += 1

    def _avg(key: str) -> float:
        vals = [float(row.get(key) or 0.0) for row in cases]
        return sum(vals) / len(vals) if vals else 0.0

    strongest = cases[:5]
    hidden = sorted(cases, key=lambda row: float(row.get("hidden_winner_score") or 0.0), reverse=True)[:5]
    feeder = sorted(cases, key=lambda row: float(row.get("feeder_progression_score") or 0.0), reverse=True)[:5]

    return {
        "metadata": {
            "window_root": safe_rel(window_root),
            "window_dates": iter_window_dates(window_root),
            "case_count": len(cases),
            "warnings": list(warnings),
        },
        "signature_mix": {
            "signature_counts": dict(sorted(signature_counts.items())),
            "signature_strength_counts": dict(sorted(signature_strength_counts.items())),
            "hit_class_counts": dict(sorted(hit_class_counts.items())),
            "blackapple_status_counts": dict(sorted(best_blackapple_counts.items())),
            "inventory_type_counts": dict(sorted(inventory_type_counts.items())),
        },
        "score_averages": {
            "literal_frontier_score": round(_avg("literal_frontier_score"), 6),
            "family_frontier_score": round(_avg("family_frontier_score"), 6),
            "vtrac_frontier_score": round(_avg("vtrac_frontier_score"), 6),
            "vertical_stability_score": round(_avg("vertical_stability_score"), 6),
            "cross_variant_echo_score": round(_avg("cross_variant_echo_score"), 6),
            "frontier_purity_score": round(_avg("frontier_purity_score"), 6),
            "compression_score": round(_avg("compression_score"), 6),
            "hidden_winner_score": round(_avg("hidden_winner_score"), 6),
            "feeder_progression_score": round(_avg("feeder_progression_score"), 6),
            "double_anchor_score": round(_avg("double_anchor_score"), 6),
            "frontier_strength_score": round(_avg("frontier_strength_score"), 3),
        },
        "notable_cases": {
            "strongest": [
                {
                    "date": row["date"],
                    "state_key": row["state_key"],
                    "winner": row["winner"],
                    "signature": row["frontier_signature_type"],
                    "strength_score": row["frontier_strength_score"],
                }
                for row in strongest
            ],
            "most_hidden": [
                {
                    "date": row["date"],
                    "state_key": row["state_key"],
                    "winner": row["winner"],
                    "hidden_winner_score": row["hidden_winner_score"],
                    "signature": row["frontier_signature_type"],
                }
                for row in hidden
            ],
            "strongest_feeder_progression": [
                {
                    "date": row["date"],
                    "state_key": row["state_key"],
                    "winner": row["winner"],
                    "feeder_progression_score": row["feeder_progression_score"],
                    "signature": row["frontier_signature_type"],
                }
                for row in feeder
            ],
        },
        "promotion_queue": _promotion_queue(cases),
    }


def _render_markdown(payload: Dict[str, Any], cases: Sequence[Dict[str, Any]]) -> str:
    meta = payload["metadata"]
    sig = payload["signature_mix"]
    avg = payload["score_averages"]
    promotion_queue = payload["promotion_queue"]

    lines: List[str] = [
        f"# {Path(meta['window_root']).name} Analysis Arena C1/C2 Frontier Analysis",
        "",
        "## Overview",
        "",
        f"- Window root: `{meta['window_root']}`",
        f"- Window dates: `{', '.join(meta['window_dates'])}`",
        f"- Frontier cases: `{meta['case_count']}`",
        "",
        "## Signature Mix",
        "",
    ]
    for label, count in sig["signature_counts"].items():
        lines.append(f"- `{label}`: `{count}`")
    lines += [
        "",
        "## Hit-Class Rollup",
        "",
    ]
    for label, count in sig["hit_class_counts"].items():
        lines.append(f"- `{label}`: `{count}`")
    lines += [
        "",
        "## Average Frontier Scores",
        "",
    ]
    for key, value in avg.items():
        lines.append(f"- `{key}`: `{_fmt_score(float(value)) if isinstance(value, (int, float)) else value}`")

    lines += [
        "",
        "## Promotion Queue",
        "",
    ]
    if promotion_queue:
        for item in promotion_queue:
            lines.append(f"- `{item['promote_class']}` {item['signal']}: {item['evidence']}")
    else:
        lines.append("- No promotion candidates crossed the current threshold on this window.")

    lines += [
        "",
        "## Notable Cases",
        "",
    ]
    for row in cases[:8]:
        lines.append(
            f"- `{row['date']} {row['state_key']} {row['winner']}` "
            f"`{row['frontier_signature_type']}` "
            f"strength=`{row['frontier_strength_score']}` "
            f"hit=`{row['hit_class_rollup']}` "
            f"rank=`{row['best_board_rank'] or '-'}`"
        )

    if meta["warnings"]:
        lines += [
            "",
            "## Warnings",
            "",
        ]
        for warning in meta["warnings"]:
            lines.append(f"- {warning}")

    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    winner_html_root = _resolve_path(args.winner_html_root)
    truth_sharepacks_root = _resolve_path(args.truth_sharepacks_root)
    outputs = _default_outputs(window_root)
    out_md = _resolve_path(args.out_md) if args.out_md else outputs["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else outputs["json"]
    out_csv = _resolve_path(args.out_csv) if args.out_csv else outputs["csv"]
    ledger_csv = _resolve_path(args.ledger_csv) if args.ledger_csv else _default_ledger_path(window_root)
    hit_roster_csv = _resolve_path(args.hit_roster_csv) if args.hit_roster_csv else _default_hit_roster_path(window_root)

    ledger_rows = _read_csv_rows(ledger_csv)
    if not ledger_rows:
        raise SystemExit(f"Missing or empty performance-gap ledger: {ledger_csv}")
    hit_rows = _read_csv_rows(hit_roster_csv)

    cases, warnings = _load_cases(
        window_root=window_root,
        winner_html_root=winner_html_root,
        truth_sharepacks_root=truth_sharepacks_root,
        ledger_rows=ledger_rows,
        hit_rows=hit_rows,
    )
    payload = _summary_payload(window_root, cases, warnings)
    payload["cases"] = cases

    _write_csv(out_csv, cases, force=bool(args.force))
    _write_json(out_json, payload, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload, cases), force=bool(args.force))

    print(safe_rel(out_md))
    print(safe_rel(out_json))
    print(safe_rel(out_csv))


if __name__ == "__main__":
    main()
