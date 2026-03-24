#!/usr/bin/env python3
"""Deep reverse-engineer harness for R-Consensus string-table events."""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Sequence, Set, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ROW_TYPES: Tuple[str, ...] = ("R2", "R4", "R6", "R8")
TABLE_COLS: Tuple[str, ...] = ("7", "6", "5", "4", "3", "2", "1")
DRAW_ORDER: Dict[str, int] = {"Midday": 0, "Evening": 1}
MIRROR_DIGITS: Dict[str, str] = {
    "0": "5",
    "5": "0",
    "1": "6",
    "6": "1",
    "2": "7",
    "7": "2",
    "3": "8",
    "8": "3",
    "4": "9",
    "9": "4",
}
DIGIT_TO_VTRAC_VALUE: Dict[str, str] = {
    "0": "1",
    "5": "1",
    "1": "2",
    "6": "2",
    "2": "3",
    "7": "3",
    "3": "4",
    "8": "4",
    "4": "5",
    "9": "5",
}
VARIANT_KEY_MAP: Dict[str, str] = {
    "Midday": "midday",
    "Evening": "evening",
    "Combined": "combined",
}


def _digits_only(value: object) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _truthy(value: object) -> bool:
    text = str(value or "").strip().lower()
    if text in {"1", "true", "t", "y", "yes"}:
        return True
    if text in {"0", "false", "f", "n", "no", ""}:
        return False
    try:
        return float(text) != 0.0
    except Exception:
        return False


def _safe_int(value: object, default: int = 0) -> int:
    try:
        if value is None or str(value).strip() == "":
            return default
        return int(float(value))
    except Exception:
        return default


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        if value is None or str(value).strip() == "":
            return default
        return float(value)
    except Exception:
        return default


def _canon(value: object) -> str:
    return "".join(sorted(_digits_only(value)))


def _combo_to_vtrac_seq(combo: str) -> str:
    return "".join(DIGIT_TO_VTRAC_VALUE.get(ch, "") for ch in _digits_only(combo))


def _combo_to_vtrac_index(value: object) -> Optional[int]:
    digits = _canon(value)
    if len(digits) != 3:
        return None
    try:
        return int(get_vtrac_index(digits))
    except Exception:
        return None


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(fieldnames))
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _date_dirs(sharepacks_root: Path) -> List[Path]:
    return sorted(
        path for path in sharepacks_root.iterdir() if path.is_dir() and DATE_RE.match(path.name)
    )


def _iter_states_for_date(date_dir: Path) -> Iterable[Path]:
    for path in sorted(date_dir.iterdir()):
        if path.is_dir() and not path.name.startswith("_") and path.name != "control_center":
            yield path


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_latest_winner_artifacts(winners_dir: Path) -> Dict[str, Dict[str, str]]:
    out: Dict[str, Dict[str, str]] = {}
    if not winners_dir.exists():
        return out
    files = sorted(winners_dir.glob("*.json"))
    by_combo: Dict[str, Path] = {}
    for path in files:
        match = re.search(r"_winner_(\d+)_\d{8}_\d{6}\.json$", path.name)
        if not match:
            continue
        combo = match.group(1)
        prev = by_combo.get(combo)
        if prev is None or path.name > prev.name:
            by_combo[combo] = path
    for combo, json_path in by_combo.items():
        html_path = json_path.with_suffix(".html")
        payload = _load_json(json_path)
        out[combo] = {
            "winner_combo": combo,
            "winner_json": str(json_path),
            "winner_html": str(html_path) if html_path.exists() else "",
            "winner_vtrac_index": str(payload.get("index") or ""),
            "winner_patterns": ",".join(payload.get("patterns") or []),
        }
    return out


def _parse_draw_snapshot_head(draws_dir: Path, suffix: str) -> str:
    matches = sorted(draws_dir.glob(f"*{suffix}"))
    if not matches:
        return ""
    lines = matches[0].read_text(encoding="utf-8").splitlines()
    if len(lines) < 2:
        return ""
    return _digits_only(lines[1])


def _load_case_winners_from_aux(state_dir: Path) -> Dict[str, Dict[str, str]]:
    draws_dir = state_dir / "aux" / "draws"
    midday = _parse_draw_snapshot_head(draws_dir, "_Midday_draws.csv")
    evening = _parse_draw_snapshot_head(draws_dir, "_Evening_draws.csv")
    out: Dict[str, Dict[str, str]] = {}
    if midday:
        out["Midday"] = {
            "combo": midday,
            "canonical": _canon(midday),
            "vtrac_seq": _combo_to_vtrac_seq(midday),
            "vtrac_index": str(_combo_to_vtrac_index(midday) or ""),
        }
    if evening:
        out["Evening"] = {
            "combo": evening,
            "canonical": _canon(evening),
            "vtrac_seq": _combo_to_vtrac_seq(evening),
            "vtrac_index": str(_combo_to_vtrac_index(evening) or ""),
        }
    return out


def _build_state_draw_timeline(sharepacks_root: Path) -> Dict[str, List[Dict[str, Any]]]:
    out: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)
    for date_dir in _date_dirs(sharepacks_root):
        for state_dir in _iter_states_for_date(date_dir):
            winners = _load_case_winners_from_aux(state_dir)
            for draw_name in ("Midday", "Evening"):
                info = winners.get(draw_name)
                if not info:
                    continue
                out[state_dir.name].append(
                    {
                        "date": date_dir.name,
                        "draw": draw_name,
                        "combo": info["combo"],
                        "canonical": info["canonical"],
                        "vtrac_seq": info["vtrac_seq"],
                        "vtrac_index": info["vtrac_index"],
                    }
                )
    for state_key, rows in out.items():
        rows.sort(key=lambda row: (row["date"], DRAW_ORDER.get(row["draw"], 99)))
    return dict(out)


def _load_profit_alert_rows(date_dir: Path) -> Dict[str, List[Dict[str, Any]]]:
    path = date_dir / "control_center" / "profit_alerts.csv"
    if not path.exists():
        return {}
    out: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in _read_csv_rows(path):
        evidence_text = row.get("Evidence") or ""
        try:
            evidence = json.loads(evidence_text) if evidence_text else {}
        except Exception:
            evidence = {"raw": evidence_text}
        record = dict(row)
        record["EvidenceParsed"] = evidence
        out[str(row.get("StateKey") or "")].append(record)
    return dict(out)


def _load_case_context(date_dir: Path, state_dir: Path, profit_rows: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    state_key = state_dir.name
    tables_path = state_dir / "json" / f"{state_key}_tables.json"
    stable_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_scores.csv"
    aux_summary_path = state_dir / "aux" / state_key / "summary.json"
    tables = _load_json(tables_path)
    stable_rows = _read_csv_rows(stable_path)
    aux_summary = _load_json(aux_summary_path) if aux_summary_path.exists() else {}
    winners_by_combo = _load_latest_winner_artifacts(state_dir / "winners" / state_key)
    same_day_winners = _load_case_winners_from_aux(state_dir)
    stable_box_index: DefaultDict[Tuple[str, str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    stable_minitable_index: DefaultDict[Tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in stable_rows:
        section = str(row.get("section") or "")
        set_name = str(row.get("Set") or "")
        draw_name = str(row.get("Draw") or "")
        column = str(row.get("Column") or "")
        row["__score"] = _safe_float(row.get("score"))
        row["__cons_full"] = _truthy(row.get("cons_full"))
        row["__cons_3v"] = _truthy(row.get("cons_3v"))
        row["__cons_stub"] = _truthy(row.get("cons_stub"))
        row["__rowcov"] = len([item for item in str(row.get("rows") or "").split(",") if item.strip()])
        row["__canonical_digits"] = _digits_only(row.get("Canonical"))
        row["__family_id"] = str(row.get("family_id") or "")
        row["__orders_digits"] = _digits_only(row.get("orders_modal_value"))
        stable_box_index[(section, set_name, draw_name, column)].append(row)
        stable_minitable_index[(section, set_name, draw_name)].append(row)
    return {
        "results_date": date_dir.name,
        "state_key": state_key,
        "state_dir": state_dir,
        "tables_path": tables_path,
        "stable_path": stable_path,
        "aux_summary_path": aux_summary_path,
        "tables": tables,
        "stable_rows": stable_rows,
        "stable_box_index": stable_box_index,
        "stable_minitable_index": stable_minitable_index,
        "aux_summary": aux_summary,
        "winners_by_combo": winners_by_combo,
        "same_day_winners": same_day_winners,
        "profit_rows": list(profit_rows),
    }


def _column_index(column: str) -> int:
    return TABLE_COLS.index(str(column))


def _raw_box_value(pattern_variations: Dict[str, List[str]], row_type: str, column: str) -> str:
    values = pattern_variations.get(row_type) or []
    idx = _column_index(column)
    if idx >= len(values):
        return ""
    return str(values[idx] or "")


def _common_suffix_class(values: Sequence[str]) -> Tuple[str, str]:
    digits = [_digits_only(value) for value in values]
    if any(not value for value in digits):
        return ("", "")
    tails2 = [value[-2:] if len(value) >= 2 else "" for value in digits]
    if tails2 and len(set(tails2)) == 1 and tails2[0]:
        return (tails2[0], "two-digit")
    tails1 = [value[-1:] for value in digits if value]
    if tails1 and len(tails1) == len(digits) and len(set(tails1)) == 1 and tails1[0]:
        return (tails1[0], "single-digit")
    return ("", "")


def _discover_case_events(case: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    sections = (case["tables"].get("sections") or {})
    for section_name, section_payload in sections.items():
        sets = section_payload.get("sets") or {}
        for set_name, set_payload in sets.items():
            for draw_name, draw_payload in (set_payload or {}).items():
                pattern_variations = draw_payload.get("pattern_variations") or {}
                for column in ("1", "2"):
                    raw_rows = {row_type: _raw_box_value(pattern_variations, row_type, column) for row_type in ROW_TYPES}
                    tail_value, event_class = _common_suffix_class(list(raw_rows.values()))
                    box_rows = case["stable_box_index"].get((section_name, set_name, draw_name, column), [])
                    if not tail_value and not any(row.get("__cons_stub") for row in box_rows):
                        continue
                    if not tail_value:
                        stub_rows = [row for row in box_rows if row.get("__cons_stub")]
                        if stub_rows:
                            tail_value = _digits_only(stub_rows[0].get("Canonical"))
                            event_class = "two-digit" if len(tail_value) >= 2 else "single-digit"
                    if not tail_value:
                        continue
                    box_key = f"{section_name}:{set_name}:{draw_name}:Col{column}"
                    out.append(
                        {
                            "event_key": f"{case['results_date']}/{case['state_key']}/{section_name}/{set_name}/{draw_name}/C{column}/{tail_value}",
                            "results_date": case["results_date"],
                            "state_key": case["state_key"],
                            "section": section_name,
                            "set_name": set_name,
                            "draw_name": draw_name,
                            "column": column,
                            "tail_value": tail_value,
                            "event_class": event_class,
                            "raw_rows": raw_rows,
                            "box_key": box_key,
                            "stable_flags": {
                                "cons_full": any(row.get("__cons_full") for row in box_rows),
                                "cons_3v": any(row.get("__cons_3v") for row in box_rows),
                                "cons_stub": any(row.get("__cons_stub") for row in box_rows),
                            },
                            "stable_box_rows": box_rows,
                        }
                    )
    return out


def _event_counts_by_state_day(events: Sequence[Dict[str, Any]]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    out: Dict[Tuple[str, str], Dict[str, Any]] = {}
    buckets: DefaultDict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[(event["results_date"], event["state_key"])].append(event)
    for key, rows in buckets.items():
        sections = Counter(row["section"] for row in rows)
        out[key] = {
            "total_events": len(rows),
            "section_counts": dict(sections),
            "cross_variant_count": sum(1 for _name, count in sections.items() if count > 0),
            "max_same_variant_events": max(sections.values()) if sections else 0,
        }
    return out


def _top_rows(rows: Sequence[Dict[str, Any]], limit: int = 8, column_filter: Optional[Set[str]] = None) -> List[Dict[str, Any]]:
    filtered = []
    for row in rows:
        if row.get("type") == "consensus_stub":
            continue
        if column_filter is not None and str(row.get("Column") or "") not in column_filter:
            continue
        digits = row.get("__canonical_digits") or ""
        if len(digits) < 2:
            continue
        filtered.append(row)
    filtered.sort(
        key=lambda row: (
            -row.get("__score", 0.0),
            -len(row.get("__canonical_digits") or ""),
            str(row.get("Column") or ""),
            str(row.get("Canonical") or ""),
        )
    )
    return filtered[:limit]


def _rows_to_compact(rows: Sequence[Dict[str, Any]], limit: int = 8) -> List[Dict[str, Any]]:
    compact: List[Dict[str, Any]] = []
    for row in rows[:limit]:
        compact.append(
            {
                "canonical": str(row.get("Canonical") or ""),
                "score": round(_safe_float(row.get("score")), 2),
                "column": str(row.get("Column") or ""),
                "rows": str(row.get("rows") or ""),
                "orders": str(row.get("orders_modal_value") or ""),
                "family_id": str(row.get("family_id") or ""),
                "why": str(row.get("why") or ""),
            }
        )
    return compact


def _candidate_sets(rows: Sequence[Dict[str, Any]], limit: int = 12) -> Dict[str, List[str]]:
    exacts: List[str] = []
    canonicals: List[str] = []
    vtrac_indices: List[str] = []
    vtrac_sequences: List[str] = []
    for row in _top_rows(rows, limit=limit):
        canonical = _canon(row.get("Canonical"))
        orders = _digits_only(row.get("orders_modal_value"))
        exact = orders if len(orders) == 3 else canonical if len(canonical) == 3 else ""
        if exact and exact not in exacts:
            exacts.append(exact)
        if len(canonical) == 3 and canonical not in canonicals:
            canonicals.append(canonical)
        fam = str(row.get("__family_id") or row.get("family_id") or "")
        if fam and fam not in vtrac_indices:
            vtrac_indices.append(fam)
        if exact:
            seq = _combo_to_vtrac_seq(exact)
            if seq and seq not in vtrac_sequences:
                vtrac_sequences.append(seq)
    return {
        "exact": exacts,
        "boxed": canonicals,
        "vtrac_straight": vtrac_sequences,
        "vtrac_boxed": vtrac_indices,
    }


def _group_family_support(rows: Sequence[Dict[str, Any]], limit: int = 8) -> List[Dict[str, Any]]:
    counter: DefaultDict[str, Dict[str, Any]] = defaultdict(lambda: {"score": 0.0, "count": 0, "canonicals": []})
    for row in _top_rows(rows, limit=24):
        family_id = str(row.get("__family_id") or row.get("family_id") or "")
        if not family_id:
            continue
        entry = counter[family_id]
        entry["score"] += _safe_float(row.get("score"))
        entry["count"] += 1
        canonical = _canon(row.get("Canonical"))
        if canonical and canonical not in entry["canonicals"]:
            entry["canonicals"].append(canonical)
    items = [
        {
            "family_id": family_id,
            "aggregate_score": round(data["score"], 2),
            "row_count": data["count"],
            "canonicals": data["canonicals"][:4],
        }
        for family_id, data in counter.items()
    ]
    items.sort(key=lambda item: (-item["aggregate_score"], -item["row_count"], item["family_id"]))
    return items[:limit]


def _set_name_delta(set_name: str, delta: int) -> str:
    match = re.search(r"(\d+)$", set_name)
    if not match:
        return set_name
    base = int(match.group(1)) + delta
    if base <= 0:
        return ""
    return f"Set{base}"


def _collect_surrounding_rows(case: Dict[str, Any], section: str, set_name: str, draw_name: str) -> Dict[str, List[Dict[str, Any]]]:
    local = case["stable_minitable_index"].get((section, set_name, draw_name), [])
    above = case["stable_minitable_index"].get((section, _set_name_delta(set_name, -1), draw_name), [])
    below = case["stable_minitable_index"].get((section, _set_name_delta(set_name, 1), draw_name), [])
    hot_band = [row for row in local + above + below if str(row.get("Column") or "") in {"1", "2"}]
    return {"local": local, "above": above, "below": below, "hot_band": hot_band}


def _build_nearby_keys(
    tail_value: str,
    section_tables: Dict[str, Any],
    set_name: str,
    draw_name: str,
    column: str,
) -> Dict[str, Any]:
    draw_payload = (((section_tables.get("sets") or {}).get(set_name) or {}).get(draw_name) or {})
    pattern_variations = draw_payload.get("pattern_variations") or {}
    nearby_columns = {"1", "2", "3"} if column in {"1", "2"} else {column}
    digit_counts: Counter[str] = Counter()
    provenance: DefaultDict[str, Set[str]] = defaultdict(set)
    consensus_digits = set(_digits_only(tail_value))
    for row_type in ROW_TYPES:
        for col in nearby_columns:
            raw_value = _raw_box_value(pattern_variations, row_type, col)
            for digit in _digits_only(raw_value):
                if digit in consensus_digits:
                    continue
                weight = 3 if col == "1" else 2 if col == "2" else 1
                digit_counts[digit] += weight
                provenance[digit].add(f"{row_type}:Col{col}")
    nearby = [digit for digit, _count in digit_counts.most_common()][:3]
    return {
        "nearby_keys": nearby,
        "selection_method": "same-mini-table col1-3 weighted frequency excluding consensus digits",
        "provenance": {digit: sorted(provenance.get(digit, set())) for digit in nearby},
    }


def _unique_preserve(values: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    out: List[str] = []
    for value in values:
        if value and value not in seen:
            out.append(value)
            seen.add(value)
    return out


def _classic_doubles_shortlist(tail_value: str, nearby_keys: Sequence[str]) -> Dict[str, List[str]]:
    anchors = sorted(set(_digits_only(tail_value)))
    exacts: List[str] = []
    mirrors: List[str] = []
    for anchor in anchors:
        for key_digit in nearby_keys:
            if not key_digit:
                continue
            base = [anchor, anchor, key_digit]
            exacts.extend("".join(parts) for parts in sorted(set(itertools.permutations(base, 3))))
            mirror_anchor = MIRROR_DIGITS.get(anchor)
            if mirror_anchor:
                mirror_base = [mirror_anchor, mirror_anchor, key_digit]
                mirrors.extend("".join(parts) for parts in sorted(set(itertools.permutations(mirror_base, 3))))
    exacts = _unique_preserve(exacts)
    mirrors = _unique_preserve(mirrors)
    return {
        "exact": exacts,
        "boxed": _unique_preserve(_canon(combo) for combo in exacts),
        "vtrac_straight": _unique_preserve(_combo_to_vtrac_seq(combo) for combo in exacts),
        "vtrac_boxed": _unique_preserve(str(_combo_to_vtrac_index(combo) or "") for combo in exacts),
        "mirror_exact": mirrors,
        "mirror_boxed": _unique_preserve(_canon(combo) for combo in mirrors),
    }


def _find_first_hit(
    draw_window: Sequence[Dict[str, Any]],
    exact_candidates: Sequence[str],
    boxed_candidates: Sequence[str],
    vtrac_straight_candidates: Sequence[str],
    vtrac_boxed_candidates: Sequence[str],
) -> Dict[str, Any]:
    exact_set = set(_digits_only(item) for item in exact_candidates if _digits_only(item))
    boxed_set = set(_canon(item) for item in boxed_candidates if _canon(item))
    vt_straight_set = set(_digits_only(item) for item in vtrac_straight_candidates if _digits_only(item))
    vt_boxed_set = set(str(item) for item in vtrac_boxed_candidates if str(item))

    def _hit(criteria: str, entry: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "criteria": criteria,
            "date": entry["date"],
            "draw": entry["draw"],
            "combo": entry["combo"],
            "offset": entry["offset"],
        }

    results: Dict[str, Any] = {
        "exact_straight": None,
        "exact_boxed": None,
        "vtrac_straight": None,
        "vtrac_boxed": None,
    }
    for entry in draw_window:
        if results["exact_straight"] is None and entry["combo"] in exact_set:
            results["exact_straight"] = _hit("exact_straight", entry)
        if results["exact_boxed"] is None and entry["canonical"] in boxed_set:
            results["exact_boxed"] = _hit("exact_boxed", entry)
        if results["vtrac_straight"] is None and entry["vtrac_seq"] in vt_straight_set:
            results["vtrac_straight"] = _hit("vtrac_straight", entry)
        if results["vtrac_boxed"] is None and str(entry["vtrac_index"]) in vt_boxed_set:
            results["vtrac_boxed"] = _hit("vtrac_boxed", entry)
    hit_count = sum(1 for value in results.values() if value)
    results["hit_count"] = hit_count
    results["first_hit"] = min(
        (value for key, value in results.items() if key in {"exact_straight", "exact_boxed", "vtrac_straight", "vtrac_boxed"} and value),
        key=lambda item: item["offset"],
        default=None,
    )
    return results


def _event_draw_window(
    timeline_by_state: Dict[str, List[Dict[str, Any]]],
    state_key: str,
    results_date: str,
    section: str,
    max_draws: int = 8,
) -> List[Dict[str, Any]]:
    timeline = timeline_by_state.get(state_key) or []
    if not timeline:
        return []
    if section == "Evening":
        start_key = (results_date, "Evening")
    else:
        start_key = (results_date, "Midday")
    start_idx = None
    for idx, entry in enumerate(timeline):
        if (entry["date"], entry["draw"]) == start_key:
            start_idx = idx
            break
    if start_idx is None:
        for idx, entry in enumerate(timeline):
            if entry["date"] == results_date:
                start_idx = idx
                break
    if start_idx is None:
        return []
    out = []
    for offset, entry in enumerate(timeline[start_idx : start_idx + max_draws]):
        item = dict(entry)
        item["offset"] = offset
        out.append(item)
    return out


def _same_day_window(draw_window: Sequence[Dict[str, Any]], results_date: str) -> List[Dict[str, Any]]:
    return [entry for entry in draw_window if entry["date"] == results_date]


def _match_profit_alerts(profit_rows: Sequence[Dict[str, Any]], section: str, tail_value: str, column: str) -> Dict[str, Any]:
    matching: List[Dict[str, Any]] = []
    all_variant_rows: List[str] = []
    for row in profit_rows:
        variant = str(row.get("Variant") or "")
        alert_id = str(row.get("AlertId") or "")
        if alert_id:
            all_variant_rows.append(f"{variant}:{alert_id}")
        if variant not in {section, "Combined"}:
            continue
        evidence = row.get("EvidenceParsed") or {}
        evidence_tail = _digits_only(evidence.get("tail"))
        evidence_col = str(evidence.get("col") or "")
        if evidence_tail == _digits_only(tail_value) and evidence_col == str(column):
            matching.append(
                {
                    "alert_id": alert_id,
                    "variant": variant,
                    "strength": str(row.get("Strength") or ""),
                    "suggested": str(row.get("Suggested") or ""),
                    "cap_lines": str(row.get("CapLines") or ""),
                    "decay_draws": str(row.get("DecayDraws") or ""),
                    "badges": str(row.get("Badges") or ""),
                    "canonical": str(row.get("Canonical") or ""),
                }
            )
    return {"matching": matching, "all_alert_ids": sorted(set(all_variant_rows))}


def _extract_aux_context(aux_summary: Dict[str, Any], section: str, shortlist: Dict[str, List[str]]) -> Dict[str, Any]:
    variant_key = VARIANT_KEY_MAP.get(section, "combined")
    positional = ((aux_summary.get("positional") or {}).get("shortlist_report") or {})
    positional_notes = list((positional.get("consensus_notes") or [])[:6])
    double_notes = list((positional.get("double_pressure_notes") or [])[:4])
    doubles_top = (((aux_summary.get("doubles") or {}).get("top_by_variant") or {}).get(variant_key) or [])[:8]
    pairs_top = (((aux_summary.get("pairs") or {}).get("top_by_variant") or {}).get(variant_key) or {})
    sums_top = (((aux_summary.get("sums") or {}).get("top_by_variant") or {}).get(variant_key) or [])[:8]
    vtrac_top = (((aux_summary.get("vtrac") or {}).get("overlay_top") or {}).get(variant_key) or [])[:8]
    blackapple_top = (((aux_summary.get("blackapple") or {}).get("top_by_variant") or {}).get(variant_key) or [])[:8]
    due_double_match = [item["combo"] for item in doubles_top if _canon(item.get("combo")) in set(shortlist["boxed"])]
    pair_match = []
    for bucket in ("repeating", "non_repeating"):
        for item in pairs_top.get(bucket, [])[:10]:
            pair_value = _digits_only(item.get("pair"))
            if pair_value and pair_value in {_digits_only(value) for value in shortlist["boxed"]}:
                pair_match.append(pair_value)
    vtrac_match = [str(item.get("index")) for item in vtrac_top if str(item.get("index")) in set(shortlist["vtrac_boxed"])]
    blackapple_match = [item.get("combo") for item in blackapple_top if _canon(item.get("combo")) in set(shortlist["boxed"])]
    return {
        "positional_notes": positional_notes,
        "double_pressure_notes": double_notes,
        "due_double_match": _unique_preserve(due_double_match),
        "pair_match": _unique_preserve(pair_match),
        "sum_flags": [str(item.get("sum")) for item in sums_top if (item.get("flags") or {}).get("red")][:6],
        "vtrac_match": _unique_preserve(vtrac_match),
        "blackapple_match": _unique_preserve(_digits_only(item) for item in blackapple_match),
    }


def _cross_variant_summary(case: Dict[str, Any], section: str, set_name: str, draw_name: str, local_candidates: Dict[str, List[str]]) -> Dict[str, Any]:
    local_boxed = set(local_candidates["boxed"])
    local_vt = set(local_candidates["vtrac_boxed"])
    other_sections = []
    for other in ("Midday", "Evening", "Combined"):
        if other == section:
            continue
        rows = case["stable_minitable_index"].get((other, set_name, draw_name), [])
        if not rows:
            continue
        other_candidates = _candidate_sets(rows, limit=12)
        shared_boxed = sorted(local_boxed & set(other_candidates["boxed"]))
        shared_vt = sorted(local_vt & set(other_candidates["vtrac_boxed"]))
        if shared_boxed or shared_vt:
            other_sections.append(
                {
                    "section": other,
                    "shared_boxed": shared_boxed[:6],
                    "shared_vtrac": shared_vt[:6],
                }
            )
    positional_notes = ((case["aux_summary"].get("positional") or {}).get("shortlist_report") or {}).get("consensus_notes") or []
    xvar_notes = [note for note in positional_notes if "XVAR-Cons" in str(note)][:6]
    return {
        "other_sections": other_sections,
        "xvar_notes": xvar_notes,
        "shared_section_count": len(other_sections),
    }


def _local_trace(local_rows: Sequence[Dict[str, Any]], winner_info: Dict[str, str]) -> Dict[str, Any]:
    winner_boxed = winner_info.get("canonical") or ""
    winner_vt = winner_info.get("vtrac_index") or ""
    exact_hits = _rows_to_compact([row for row in _top_rows(local_rows, limit=20) if _canon(row.get("Canonical")) == winner_boxed], limit=4)
    vt_hits = _rows_to_compact([row for row in _top_rows(local_rows, limit=20) if str(row.get("__family_id") or row.get("family_id") or "") == winner_vt], limit=4)
    return {
        "winner_rows": exact_hits,
        "winner_vtrac_rows": vt_hits,
        "winner_present": bool(exact_hits),
        "winner_vtrac_present": bool(vt_hits),
    }


def _explanation_label(
    classic_same_day: Dict[str, Any],
    local_same_day: Dict[str, Any],
    surrounding_same_day: Dict[str, Any],
    cross_variant: Dict[str, Any],
) -> str:
    if local_same_day.get("hit_count", 0) > classic_same_day.get("hit_count", 0) and local_same_day.get("hit_count", 0) >= 2:
        return "strong local pattern presence"
    if classic_same_day.get("exact_straight"):
        return "consensus + nearby key"
    if local_same_day.get("vtrac_boxed") or local_same_day.get("vtrac_straight"):
        return "strong local VTRAC presence"
    if surrounding_same_day.get("hit_count", 0) >= 2:
        return "surrounding / hot-zone reinforcement"
    if cross_variant.get("shared_section_count", 0) >= 2:
        return "cross-variant reinforcement"
    if classic_same_day.get("hit_count", 0) > 0 or local_same_day.get("hit_count", 0) > 0:
        return "compound mix"
    return "consensus digit only"


def _strength_class(primary_function: str, classic_any: Dict[str, Any], local_any: Dict[str, Any]) -> str:
    score = 0
    if classic_any.get("hit_count", 0) >= 2:
        score += 2
    if local_any.get("hit_count", 0) >= 2:
        score += 2
    if classic_any.get("first_hit") and classic_any["first_hit"]["offset"] <= 1:
        score += 1
    if local_any.get("first_hit") and local_any["first_hit"]["offset"] <= 1:
        score += 1
    if primary_function == "mixed":
        score += 1
    if score >= 4:
        return "high"
    if score >= 2:
        return "medium"
    return "weak / noisy"


def _primary_function(
    classic_same_day: Dict[str, Any],
    local_same_day: Dict[str, Any],
    surrounding_any: Dict[str, Any],
    cross_variant: Dict[str, Any],
) -> str:
    if classic_same_day.get("hit_count", 0) > 0 and local_same_day.get("hit_count", 0) == 0:
        return "doubles trigger"
    if local_same_day.get("hit_count", 0) > classic_same_day.get("hit_count", 0):
        return "pattern-cluster amplifier"
    if local_same_day.get("vtrac_boxed") or local_same_day.get("vtrac_straight"):
        return "VTRAC-index amplifier"
    if cross_variant.get("shared_section_count", 0) >= 2:
        return "cross-variant amplifier"
    if surrounding_any.get("first_hit") and surrounding_any["first_hit"]["offset"] >= 2:
        return "carryover / decay signal"
    return "mixed"


def _per_event_markdown(event: Dict[str, Any]) -> str:
    lines = [
        f"# R-Consensus Event — {event['event_id']}",
        "",
        "## 1. Event Identity",
        "",
        f"- Event ID: `{event['event_id']}`",
        f"- Results date: `{event['results_date']}`",
        f"- State: `{event['state_key']}`",
        f"- Draw under review: `{event['section']}`",
        f"- Gold-day / cohort label: `{event['cohort_label']}`",
        "- Primary source files:",
        f"  - winners HTML: `{event['winner_artifacts'].get('winner_html','')}`",
        f"  - winners JSON: `{event['winner_artifacts'].get('winner_json','')}`",
        f"  - stable scores: `{event['stable_path']}`",
        f"  - aux / control-center sharepack: `{event['aux_summary_path']}`",
        "",
        "## 2. R-Consensus Lock",
        "",
        f"- Variant: `{event['section']}`",
        f"- Section: `{event['section']}`",
        f"- Set: `{event['set_name']}`",
        f"- Draw: `{event['draw_name']}`",
        f"- Column: `{event['column']}`",
        f"- Raw tail values: `R2={event['raw_rows']['R2']}` / `R4={event['raw_rows']['R4']}` / `R6={event['raw_rows']['R6']}` / `R8={event['raw_rows']['R8']}`",
        f"- Star-stripped tail value: `{event['tail_value']}`",
        f"- Tail length: `{len(event['tail_value'])}`",
        f"- Event class: `{event['event_class']}`",
        f"- Stable-style flags present: `cons_full={int(event['stable_flags']['cons_full'])}` / `cons_3v={int(event['stable_flags']['cons_3v'])}` / `cons_stub={int(event['stable_flags']['cons_stub'])}`",
        "",
        "## 3. Board Multiplicity",
        "",
        f"- Total R-Consensus count across all variants: `{event['multiplicity']['total_events']}`",
        f"- Same-variant multiple consensus?: `{event['multiplicity']['same_variant_multiple']}`",
        f"- Same-day multiple consensus?: `{event['multiplicity']['same_day_multiple']}`",
        f"- Cross-variant multiplicity?: `{event['multiplicity']['cross_variant_multiple']}`",
        f"- Multiplicity notes: `{event['multiplicity']['notes']}`",
        "",
        "## 4. Local Mini-Table Read",
        "",
        f"- Full mini string table identity: `{event['section']} / {event['set_name']} / {event['draw_name']}`",
        f"- Strongest exact patterns in the mini table: `{', '.join(event['local_cluster']['exact'][:8])}`",
        f"- Strongest boxed families / canonicals: `{', '.join(event['local_cluster']['boxed'][:8])}`",
        f"- Strongest VTRAC-related patterns: `{', '.join(event['local_cluster']['vtrac_boxed'][:8])}`",
        f"- Persistence / progression clues: `{event['local_progression_notes']}`",
        f"- Permutation clues: `{', '.join(event['local_cluster']['exact'][:6])}`",
        f"- Survivor / lingering clues: `{event['local_survivor_notes']}`",
        f"- Does winner appear directly in the mini table?: `{event['trace']['winner_present']}`",
        f"- Does winner VTRAC appear directly in the mini table?: `{event['trace']['winner_vtrac_present']}`",
        "",
        "## 5. Nearby Key Extraction",
        "",
        f"- Nearby key digits: `{', '.join(event['nearby_keys']['nearby_keys'])}`",
        f"- How keys were selected: `{event['nearby_keys']['selection_method']}`",
        f"- Nearby support VTRAC digits: `{', '.join(event['local_cluster']['vtrac_boxed'][:6])}`",
        f"- Consensus doubles shortlist generated: `{', '.join(event['classic_shortlist']['exact'][:18])}`",
        f"- Related mirror-double shortlist: `{', '.join(event['classic_shortlist']['mirror_exact'][:18])}`",
        "",
        "## 6. Consensus Method Evaluation",
        "",
        f"- Doubles shortlist exact-straight result: `{event['classic_same_day']['exact_straight']}`",
        f"- Doubles shortlist exact-boxed result: `{event['classic_same_day']['exact_boxed']}`",
        f"- Doubles shortlist VTRAC-straight result: `{event['classic_same_day']['vtrac_straight']}`",
        f"- Doubles shortlist VTRAC-boxed result: `{event['classic_same_day']['vtrac_boxed']}`",
        f"- Pair-right but 3rd-digit-missed?: `{event['pair_right_miss']}`",
        f"- Did the full related boxed VTRAC index look stronger than the narrow list?: `{event['vtrac_index_stronger']}`",
        "",
        "## 7. Local Pattern-Cluster Evaluation",
        "",
        f"- Highest-value exact cluster: `{', '.join(event['local_cluster']['exact'][:6])}`",
        f"- Highest-value boxed family cluster: `{', '.join(event['local_cluster']['boxed'][:6])}`",
        f"- Highest-value VTRAC lane cluster: `{', '.join(event['local_cluster']['vtrac_boxed'][:6])}`",
        f"- Double / mirror-double pressure: `{event['aux_context']['double_pressure_notes']}`",
        f"- Hidden-family or hidden-terminal clues: `{event['hidden_clues']}`",
        f"- Best direct pattern support for the eventual hit: `{event['best_direct_support']}`",
        "",
        "## 8. Surrounding Structure Read",
        "",
        f"- Mini table above carry-in clues: `{event['surrounding']['above_boxed']}`",
        f"- Mini table below carry-forward clues: `{event['surrounding']['below_boxed']}`",
        f"- Hot zone / near-column-1 influence: `{event['surrounding']['hot_band_boxed']}`",
        f"- Repeating into nearby boxes: `{event['surrounding']['repeat_notes']}`",
        f"- Cross-box persistence / progression: `{event['local_progression_notes']}`",
        f"- Nearby VTRAC relation: `{event['surrounding']['hot_band_vtrac']}`",
        "",
        "## 9. Cross-Variant Read",
        "",
        f"- Survivor relation with other variants: `{event['cross_variant']['other_sections']}`",
        f"- Column 1-2 cluster relation with other variants: `{event['cross_variant']['other_sections']}`",
        f"- Family / lane echo with other variants: `{event['cross_variant']['other_sections']}`",
        f"- XVAR-Cons positional reinforcement: `{event['cross_variant']['xvar_notes']}`",
        f"- Cross-variant depth / accumulation notes: `{event['cross_variant']['shared_section_count']}`",
        "",
        "## 10. Trace Analysis",
        "",
        f"- Winner trace through the consensus mini table: `{event['trace']['winner_rows']}`",
        f"- Winner-VTRAC trace through the consensus mini table: `{event['trace']['winner_vtrac_rows']}`",
        f"- Best explanation of why the converting list or cluster worked: `{event['best_explanation']}`",
        f"- Notes: `{event['trace_notes']}`",
        "",
        "## 11. Profit / Aux / Control Center Context",
        "",
        f"- Profit alerts fired: `{event['profit_context']['all_alert_ids']}`",
        f"- Consensus-adjacent alert relation: `{event['profit_context']['matching']}`",
        f"- Due doubles relation: `{event['aux_context']['due_double_match']}`",
        f"- Positional / XVAR-Cons relation: `{event['cross_variant']['xvar_notes']}`",
        f"- Pairs relation: `{event['aux_context']['pair_match']}`",
        f"- Sums relation: `{event['aux_context']['sum_flags']}`",
        f"- VTRAC index relation: `{event['aux_context']['vtrac_match']}`",
        f"- Blackapple relation: `{event['aux_context']['blackapple_match']}`",
        f"- Other Aux context: `{event['aux_context']['positional_notes']}`",
        "",
        "## 12. Same-Day And Decay Window",
        "",
        f"- Variant where event was present: `{event['section']}`",
        f"- Draw where conversion happened: `{event['first_conversion_draw']}`",
        f"- Same-day conversion?: `{event['same_day_any']}`",
        f"- Midday / Evening crossover?: `{event['crossover_any']}`",
        f"- 4-day decay conversion window findings: `{event['decay_notes']}`",
        "",
        "## 13. Event Verdict",
        "",
        f"- Primary function of this event: `{event['primary_function']}`",
        f"- Strength class: `{event['strength_class']}`",
        "",
        "## 14. Integration Notes",
        "",
        f"- What should be preserved upstream: `{event['integration_notes']['preserve']}`",
        f"- What should be scored later: `{event['integration_notes']['score']}`",
        f"- What should remain research-only for now: `{event['integration_notes']['research_only']}`",
        f"- Candidate later translator implication: `{event['integration_notes']['translator']}`",
        "",
        "## 15. Second-Pass Review",
        "",
        f"- Second-pass interpretation: `{event['second_pass']['interpretation']}`",
        f"- What was easy to miss on first pass: `{event['second_pass']['easy_to_miss']}`",
        f"- Strongest measurable feature: `{event['second_pass']['strongest_feature']}`",
        f"- Strongest integration lesson: `{event['second_pass']['integration_lesson']}`",
        "",
    ]
    return "\n".join(lines)


def _integration_notes(primary_function: str, event: Dict[str, Any]) -> Dict[str, str]:
    preserve = [
        "R-Consensus tail value",
        "multiplicity count",
        "nearby key digits",
        "local exact cluster",
        "local VTRAC cluster",
    ]
    if event["profit_context"]["matching"]:
        preserve.append("consensus-adjacent profit alerts")
    score = []
    if event["local_any"]["hit_count"] > 0:
        score.append("local mini-table cluster strength")
    if event["classic_any"]["hit_count"] > 0:
        score.append("classic doubles shortlist conversion")
    if event["cross_variant"]["shared_section_count"] > 0:
        score.append("cross-variant reinforcement depth")
    research_only = []
    if event["classic_any"]["hit_count"] == 0 and event["local_any"]["hit_count"] == 0:
        research_only.append("direct translator behavior")
    else:
        research_only.append("specialized consensus translator promotion")
    translator = "bounded consensus-trial translator" if primary_function in {"doubles trigger", "mixed"} else "none yet"
    return {
        "preserve": "; ".join(preserve),
        "score": "; ".join(score) if score else "none yet",
        "research_only": "; ".join(research_only),
        "translator": translator,
    }


def _second_pass(primary_function: str, event: Dict[str, Any], best_explanation: str) -> Dict[str, str]:
    if primary_function == "doubles trigger":
        interpretation = "The event behaved like a constrained doubles trigger more than a broad cluster amplifier."
    elif primary_function == "pattern-cluster amplifier":
        interpretation = "The event strengthened the mini-table cluster more than the classic doubles shortlist."
    elif primary_function == "VTRAC-index amplifier":
        interpretation = "The event pointed more clearly through VTRAC family pressure than direct literal closure."
    elif primary_function == "cross-variant amplifier":
        interpretation = "The event needed cross-variant support to look genuinely live."
    elif primary_function == "carryover / decay signal":
        interpretation = "The event looked more like a carryover/decay effect than a same-day trigger."
    else:
        interpretation = "The event showed mixed behavior across shortlist and local-cluster pathways."
    easy_to_miss = "The local mini-table cluster and nearby/hot-band structures mattered more than the bare tail value."
    strongest_feature = best_explanation
    integration_lesson = (
        "Preserve R-Consensus as a special upstream event family, then score local cluster strength and multiplicity before any translator promotion."
    )
    return {
        "interpretation": interpretation,
        "easy_to_miss": easy_to_miss,
        "strongest_feature": strongest_feature,
        "integration_lesson": integration_lesson,
    }


def _build_event_record(
    event: Dict[str, Any],
    case: Dict[str, Any],
    state_day_counts: Dict[Tuple[str, str], Dict[str, Any]],
    timeline_by_state: Dict[str, List[Dict[str, Any]]],
    cohort_label: str,
) -> Dict[str, Any]:
    section = event["section"]
    set_name = event["set_name"]
    draw_name = event["draw_name"]
    surrounding = _collect_surrounding_rows(case, section, set_name, draw_name)
    local_candidates = _candidate_sets(surrounding["local"])
    surrounding_candidates = _candidate_sets(surrounding["hot_band"])
    nearby_keys = _build_nearby_keys(
        event["tail_value"],
        (case["tables"].get("sections") or {}).get(section) or {},
        set_name,
        draw_name,
        event["column"],
    )
    classic_shortlist = _classic_doubles_shortlist(event["tail_value"], nearby_keys["nearby_keys"])
    aux_context = _extract_aux_context(case["aux_summary"], section, classic_shortlist)
    cross_variant = _cross_variant_summary(case, section, set_name, draw_name, local_candidates)
    draw_window = _event_draw_window(timeline_by_state, case["state_key"], case["results_date"], section, max_draws=8)
    same_day_window = _same_day_window(draw_window, case["results_date"])
    classic_same_day = _find_first_hit(
        same_day_window,
        classic_shortlist["exact"],
        classic_shortlist["boxed"],
        classic_shortlist["vtrac_straight"],
        classic_shortlist["vtrac_boxed"],
    )
    classic_any = _find_first_hit(
        draw_window,
        classic_shortlist["exact"],
        classic_shortlist["boxed"],
        classic_shortlist["vtrac_straight"],
        classic_shortlist["vtrac_boxed"],
    )
    local_same_day = _find_first_hit(
        same_day_window,
        local_candidates["exact"],
        local_candidates["boxed"],
        local_candidates["vtrac_straight"],
        local_candidates["vtrac_boxed"],
    )
    local_any = _find_first_hit(
        draw_window,
        local_candidates["exact"],
        local_candidates["boxed"],
        local_candidates["vtrac_straight"],
        local_candidates["vtrac_boxed"],
    )
    surrounding_same_day = _find_first_hit(
        same_day_window,
        surrounding_candidates["exact"],
        surrounding_candidates["boxed"],
        surrounding_candidates["vtrac_straight"],
        surrounding_candidates["vtrac_boxed"],
    )
    surrounding_any = _find_first_hit(
        draw_window,
        surrounding_candidates["exact"],
        surrounding_candidates["boxed"],
        surrounding_candidates["vtrac_straight"],
        surrounding_candidates["vtrac_boxed"],
    )
    winner_target = case["same_day_winners"].get(section if section in {"Midday", "Evening"} else "Evening") or next(
        iter(case["same_day_winners"].values()),
        {"combo": "", "canonical": "", "vtrac_index": "", "vtrac_seq": ""},
    )
    trace = _local_trace(surrounding["local"], winner_target)
    best_explanation = _explanation_label(classic_same_day, local_same_day, surrounding_same_day, cross_variant)
    primary_function = _primary_function(classic_same_day, local_same_day, surrounding_any, cross_variant)
    strength_class = _strength_class(primary_function, classic_any, local_any)
    counts = state_day_counts[(case["results_date"], case["state_key"])]
    same_variant_count = counts["section_counts"].get(section, 0)
    profit_context = _match_profit_alerts(case["profit_rows"], section, event["tail_value"], event["column"])
    winner_combo = winner_target.get("combo") or ""
    winner_artifacts = case["winners_by_combo"].get(winner_combo, {})
    first_conversion = min(
        (
            item
            for item in [
                classic_any.get("first_hit"),
                local_any.get("first_hit"),
                surrounding_any.get("first_hit"),
            ]
            if item
        ),
        key=lambda item: item["offset"],
        default=None,
    )
    pair_right_miss = bool(
        not classic_same_day.get("exact_straight")
        and classic_same_day.get("exact_boxed")
        and not local_same_day.get("exact_straight")
    )
    vtrac_index_stronger = bool(
        classic_same_day.get("vtrac_boxed")
        and not classic_same_day.get("exact_boxed")
    )
    local_progression_notes = "; ".join(
        _unique_preserve(
            str(row.get("why") or "")
            for row in _top_rows(surrounding["local"], limit=10)
            if "set_chain" in str(row.get("why") or "") or "draw_chain" in str(row.get("why") or "") or "hp_repeat" in str(row.get("why") or "")
        )
    ) or "none notable"
    local_survivor_notes = "; ".join(
        _unique_preserve(
            str(row.get("why") or "")
            for row in _top_rows(surrounding["local"], limit=10)
            if "single_left" in str(row.get("why") or "") or "dom_last" in str(row.get("why") or "")
        )
    ) or "no explicit stable frontier tag"
    hidden_clues = "; ".join(
        _unique_preserve(
            str(row.get("Canonical") or "")
            for row in _top_rows(surrounding["local"], limit=12)
            if _truthy(row.get("hidden3v"))
        )
    ) or "none explicit"
    best_direct_support = ", ".join(local_candidates["boxed"][:4]) or "none"
    trace_notes = "Winner trace uses stable top rows in the event mini table, not only the raw tail box."
    integration_notes = _integration_notes(primary_function, {
        "classic_any": classic_any,
        "local_any": local_any,
        "cross_variant": cross_variant,
        "profit_context": profit_context,
    })
    second_pass = _second_pass(primary_function, {
        "classic_any": classic_any,
        "local_any": local_any,
    }, best_explanation)
    record = {
        "event_id": f"{case['results_date']}__{case['state_key']}__{section}__{set_name}__{draw_name}__col{event['column']}__tail{event['tail_value']}",
        "event_key": event["event_key"],
        "results_date": case["results_date"],
        "state_key": case["state_key"],
        "section": section,
        "set_name": set_name,
        "draw_name": draw_name,
        "column": event["column"],
        "cohort_label": cohort_label,
        "tail_value": event["tail_value"],
        "event_class": event["event_class"],
        "raw_rows": event["raw_rows"],
        "stable_flags": event["stable_flags"],
        "stable_path": str(case["stable_path"]),
        "aux_summary_path": str(case["aux_summary_path"]),
        "winner_artifacts": winner_artifacts,
        "same_day_winner": winner_target,
        "multiplicity": {
            "total_events": counts["total_events"],
            "same_variant_multiple": same_variant_count > 1,
            "same_day_multiple": counts["total_events"] > 1,
            "cross_variant_multiple": counts["cross_variant_count"] > 1,
            "notes": f"section_count={same_variant_count}; cross_variant_count={counts['cross_variant_count']}",
        },
        "local_cluster": local_candidates,
        "local_family_support": _group_family_support(surrounding["local"]),
        "local_progression_notes": local_progression_notes,
        "local_survivor_notes": local_survivor_notes,
        "nearby_keys": nearby_keys,
        "classic_shortlist": classic_shortlist,
        "classic_same_day": classic_same_day,
        "classic_any": classic_any,
        "local_same_day": local_same_day,
        "local_any": local_any,
        "surrounding_same_day": surrounding_same_day,
        "surrounding_any": surrounding_any,
        "surrounding": {
            "above_boxed": _candidate_sets(surrounding["above"])["boxed"][:8],
            "below_boxed": _candidate_sets(surrounding["below"])["boxed"][:8],
            "hot_band_boxed": surrounding_candidates["boxed"][:8],
            "hot_band_vtrac": surrounding_candidates["vtrac_boxed"][:8],
            "repeat_notes": "; ".join(
                _unique_preserve(
                    str(row.get("why") or "")
                    for row in _top_rows(surrounding["hot_band"], limit=12)
                    if "hp_repeat" in str(row.get("why") or "") or "draw_chain" in str(row.get("why") or "")
                )
            ) or "none notable",
        },
        "cross_variant": cross_variant,
        "trace": trace,
        "profit_context": profit_context,
        "aux_context": aux_context,
        "draw_window": draw_window,
        "same_day_window": same_day_window,
        "first_conversion_draw": f"{first_conversion['date']} {first_conversion['draw']}" if first_conversion else "none",
        "same_day_any": bool(
            classic_same_day.get("first_hit") or local_same_day.get("first_hit") or surrounding_same_day.get("first_hit")
        ),
        "crossover_any": bool(
            first_conversion
            and first_conversion["date"] == case["results_date"]
            and ((section == "Midday" and first_conversion["draw"] == "Evening") or section == "Combined")
        ),
        "decay_notes": f"classic_first={classic_any.get('first_hit')}; local_first={local_any.get('first_hit')}; surrounding_first={surrounding_any.get('first_hit')}",
        "pair_right_miss": pair_right_miss,
        "vtrac_index_stronger": vtrac_index_stronger,
        "best_explanation": best_explanation,
        "hidden_clues": hidden_clues,
        "best_direct_support": best_direct_support,
        "trace_notes": trace_notes,
        "primary_function": primary_function,
        "strength_class": strength_class,
        "integration_notes": integration_notes,
        "second_pass": second_pass,
    }
    return record


def _rollup(events: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(events)
    function_counts = Counter(event["primary_function"] for event in events)
    strength_counts = Counter(event["strength_class"] for event in events)
    class_counts = Counter(event["event_class"] for event in events)
    section_counts = Counter(event["section"] for event in events)
    same_day_hits = sum(1 for event in events if event["same_day_any"])
    crossover_hits = sum(1 for event in events if event["crossover_any"])
    classic_hits = sum(1 for event in events if event["classic_any"].get("hit_count", 0) > 0)
    local_hits = sum(1 for event in events if event["local_any"].get("hit_count", 0) > 0)
    surrounding_hits = sum(1 for event in events if event["surrounding_any"].get("hit_count", 0) > 0)
    multiple_events = sum(1 for event in events if event["multiplicity"]["same_day_multiple"])
    breakdowns: Dict[str, Dict[str, Dict[str, int]]] = {}
    for label, key_fn in {
        "event_class": lambda item: item["event_class"],
        "section": lambda item: item["section"],
        "multiplicity": lambda item: "multiple" if item["multiplicity"]["same_day_multiple"] else "single",
    }.items():
        bucket: Dict[str, Dict[str, int]] = {}
        for event in events:
            key = key_fn(event)
            stats = bucket.setdefault(
                key,
                {
                    "events": 0,
                    "same_day_hits": 0,
                    "classic_window_hits": 0,
                    "local_window_hits": 0,
                    "surrounding_window_hits": 0,
                },
            )
            stats["events"] += 1
            stats["same_day_hits"] += 1 if event["same_day_any"] else 0
            stats["classic_window_hits"] += 1 if event["classic_any"].get("hit_count", 0) > 0 else 0
            stats["local_window_hits"] += 1 if event["local_any"].get("hit_count", 0) > 0 else 0
            stats["surrounding_window_hits"] += 1 if event["surrounding_any"].get("hit_count", 0) > 0 else 0
        breakdowns[label] = bucket
    return {
        "total_events": total,
        "event_class_counts": dict(class_counts),
        "section_counts": dict(section_counts),
        "primary_function_counts": dict(function_counts),
        "strength_counts": dict(strength_counts),
        "same_day_hit_events": same_day_hits,
        "crossover_hit_events": crossover_hits,
        "classic_window_hit_events": classic_hits,
        "local_window_hit_events": local_hits,
        "surrounding_window_hit_events": surrounding_hits,
        "multi_consensus_events": multiple_events,
        "breakdowns": breakdowns,
    }


def _rollup_markdown(payload: Dict[str, Any]) -> str:
    rollup = payload["rollup"]
    lines = [
        "# R-Consensus Harness Rollup",
        "",
        f"- corpus label: `{payload['cohort_label']}`",
        f"- total events: `{rollup['total_events']}`",
        f"- event classes: `{rollup['event_class_counts']}`",
        f"- sections: `{rollup['section_counts']}`",
        f"- primary functions: `{rollup['primary_function_counts']}`",
        f"- strength classes: `{rollup['strength_counts']}`",
        f"- same-day hit events: `{rollup['same_day_hit_events']}`",
        f"- crossover hit events: `{rollup['crossover_hit_events']}`",
        f"- classic shortlist window hits: `{rollup['classic_window_hit_events']}`",
        f"- local cluster window hits: `{rollup['local_window_hit_events']}`",
        f"- surrounding cluster window hits: `{rollup['surrounding_window_hit_events']}`",
        f"- multi-consensus events: `{rollup['multi_consensus_events']}`",
        "",
        "## Integration Read",
        "",
        "- `R-Consensus` should remain a dedicated upstream event family, not generic convergence.",
        "- The rollup is measuring both classic doubles-trigger behavior and broader mini-table amplification behavior.",
        "- Any production scoring or translator promotion should wait for these cohort findings, not precede them.",
        "",
        "## Breakdown Snapshots",
        "",
    ]
    for label in ("event_class", "section", "multiplicity"):
        lines.append(f"### {label.replace('_', ' ').title()}")
        lines.append("")
        for key, stats in sorted(rollup["breakdowns"].get(label, {}).items()):
            lines.append(
                f"- `{key}`: events=`{stats['events']}`, same_day=`{stats['same_day_hits']}`, classic_window=`{stats['classic_window_hits']}`, local_window=`{stats['local_window_hits']}`, surrounding_window=`{stats['surrounding_window_hits']}`"
            )
        lines.append("")
    return "\n".join(lines)


def _roster_rows(events: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for event in events:
        rows.append(
            {
                "event_id": event["event_id"],
                "results_date": event["results_date"],
                "state_key": event["state_key"],
                "section": event["section"],
                "set_name": event["set_name"],
                "draw_name": event["draw_name"],
                "column": event["column"],
                "tail_value": event["tail_value"],
                "event_class": event["event_class"],
                "cons_full": "1" if event["stable_flags"]["cons_full"] else "0",
                "cons_3v": "1" if event["stable_flags"]["cons_3v"] else "0",
                "cons_stub": "1" if event["stable_flags"]["cons_stub"] else "0",
                "same_day_any": "1" if event["same_day_any"] else "0",
                "crossover_any": "1" if event["crossover_any"] else "0",
                "classic_window_hits": str(event["classic_any"]["hit_count"]),
                "local_window_hits": str(event["local_any"]["hit_count"]),
                "surrounding_window_hits": str(event["surrounding_any"]["hit_count"]),
                "primary_function": event["primary_function"],
                "strength_class": event["strength_class"],
            }
        )
    return rows


def build_r_consensus_harness(
    repo_root: Path,
    sharepacks_root: Path,
    *,
    date_filter: Optional[Sequence[str]] = None,
    state_filter: Optional[Sequence[str]] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    target_dates = set(date_filter or [])
    target_states = set(state_filter or [])
    timeline_by_state = _build_state_draw_timeline(sharepacks_root)
    profit_by_date: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
    raw_events: List[Tuple[Dict[str, Any], Dict[str, Any]]] = []

    for date_dir in _date_dirs(sharepacks_root):
        if target_dates and date_dir.name not in target_dates:
            continue
        profit_by_date[date_dir.name] = _load_profit_alert_rows(date_dir)
        for state_dir in _iter_states_for_date(date_dir):
            if target_states and state_dir.name not in target_states:
                continue
            tables_path = state_dir / "json" / f"{state_dir.name}_tables.json"
            stable_path = state_dir / "stable" / state_dir.name / f"{state_dir.name}_stable_patterns_scores.csv"
            aux_summary_path = state_dir / "aux" / state_dir.name / "summary.json"
            if not (tables_path.exists() and stable_path.exists() and aux_summary_path.exists()):
                continue
            case = _load_case_context(date_dir, state_dir, profit_by_date[date_dir.name].get(state_dir.name, []))
            for event in _discover_case_events(case):
                raw_events.append((event, case))
                if limit is not None and len(raw_events) >= limit:
                    break
            if limit is not None and len(raw_events) >= limit:
                break
        if limit is not None and len(raw_events) >= limit:
            break

    state_day_counts = _event_counts_by_state_day([event for event, _case in raw_events])
    cohort_label = "gold_days_root_sharepacks"
    events = [
        _build_event_record(event, case, state_day_counts, timeline_by_state, cohort_label)
        for event, case in raw_events
    ]
    payload = {
        "generated_at": date.today().isoformat(),
        "cohort_label": cohort_label,
        "event_count": len(events),
        "rollup": _rollup(events),
        "events": events,
    }
    return payload


def write_r_consensus_harness_outputs(
    payload: Dict[str, Any],
    *,
    output_dir: Path,
    prefix_date: Optional[str] = None,
) -> Dict[str, str]:
    stamp = prefix_date or date.today().isoformat()
    output_dir.mkdir(parents=True, exist_ok=True)
    events_dir = output_dir / f"{stamp}__R_CONSENSUS_EVENTS"
    events_dir.mkdir(parents=True, exist_ok=True)

    roster_path = output_dir / f"{stamp}__R_CONSENSUS_EVENT_ROSTER.csv"
    rollup_md_path = output_dir / f"{stamp}__R_CONSENSUS_HARNESS_ROLLUP.md"
    rollup_csv_path = output_dir / f"{stamp}__R_CONSENSUS_HARNESS_ROLLUP.csv"
    rollup_json_path = output_dir / f"{stamp}__R_CONSENSUS_HARNESS_ROLLUP.json"

    roster_rows = _roster_rows(payload["events"])
    _write_csv(
        roster_path,
        roster_rows,
        [
            "event_id",
            "results_date",
            "state_key",
            "section",
            "set_name",
            "draw_name",
            "column",
            "tail_value",
            "event_class",
            "cons_full",
            "cons_3v",
            "cons_stub",
            "same_day_any",
            "crossover_any",
            "classic_window_hits",
            "local_window_hits",
            "surrounding_window_hits",
            "primary_function",
            "strength_class",
        ],
    )
    _write_text(rollup_md_path, _rollup_markdown(payload))
    _write_csv(
        rollup_csv_path,
        [payload["rollup"]],
        [
            "total_events",
            "event_class_counts",
            "section_counts",
            "primary_function_counts",
            "strength_counts",
            "same_day_hit_events",
            "crossover_hit_events",
            "classic_window_hit_events",
            "local_window_hit_events",
            "surrounding_window_hit_events",
            "multi_consensus_events",
            "breakdowns",
        ],
    )
    _write_text(rollup_json_path, json.dumps(payload, indent=2, sort_keys=True))

    for event in payload["events"]:
        event_md = events_dir / f"{event['event_id']}.md"
        event_json = events_dir / f"{event['event_id']}.json"
        _write_text(event_md, _per_event_markdown(event))
        _write_text(event_json, json.dumps(event, indent=2, sort_keys=True))

    return {
        "roster_csv": str(roster_path),
        "rollup_md": str(rollup_md_path),
        "rollup_csv": str(rollup_csv_path),
        "rollup_json": str(rollup_json_path),
        "events_dir": str(events_dir),
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sharepacks-root", default="sharepacks", help="Root sharepacks directory.")
    parser.add_argument(
        "--output-dir",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS",
        help="Directory for harness outputs.",
    )
    parser.add_argument("--date", action="append", dest="dates", help="Restrict to one or more results dates.")
    parser.add_argument("--state", action="append", dest="states", help="Restrict to one or more states.")
    parser.add_argument("--limit", type=int, default=None, help="Optional limit on discovered events.")
    args = parser.parse_args(argv)

    repo_root = PROJECT_ROOT
    sharepacks_root = (repo_root / args.sharepacks_root).resolve()
    output_dir = (repo_root / args.output_dir).resolve()

    payload = build_r_consensus_harness(
        repo_root=repo_root,
        sharepacks_root=sharepacks_root,
        date_filter=args.dates,
        state_filter=args.states,
        limit=args.limit,
    )
    paths = write_r_consensus_harness_outputs(payload, output_dir=output_dir)
    print(json.dumps({"event_count": payload["event_count"], "paths": paths}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
