#!/usr/bin/env python3
"""Audit survivor-pattern capture against winner HTML truth and stable arena output."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index
from scripts.tools.stable_arena import build_stable_arena_payload


TABLE_COLS: Tuple[str, ...] = ("7", "6", "5", "4", "3", "2", "1")
HTML_TRUTH_CLASSES: Tuple[str, ...] = (
    "hit-winner",
    "hit-winner-gap",
    "hit-vt-straight",
    "hit-vt-straight-gap",
    "hit-family",
    "hit-family-gap",
)
WINNER_HTML_RE = re.compile(
    r"_vtrac(?P<vtrac>\d+)_winner_(?P<winner>\d+)_(?P<stamp>\d{8}_\d{6})\.html$",
    re.IGNORECASE,
)
DIGIT_TO_VTRAC_VALUE: Dict[str, int] = {
    "0": 1,
    "5": 1,
    "1": 2,
    "6": 2,
    "2": 3,
    "7": 3,
    "3": 4,
    "8": 4,
    "4": 5,
    "9": 5,
}


def _digits_only(value: object) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _to_int(value: object, default: int = 0) -> int:
    try:
        if value is None or str(value).strip() == "":
            return int(default)
        return int(float(value))
    except Exception:
        return int(default)


def _to_bool(value: object) -> bool:
    text = str(value or "").strip().lower()
    if text in {"1", "true", "t", "yes", "y"}:
        return True
    if text in {"0", "false", "f", "no", "n", ""}:
        return False
    try:
        return float(text) != 0.0
    except Exception:
        return False


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _parse_counter_blob(value: object) -> List[Dict[str, Any]]:
    counter: Counter[str] = Counter()
    for chunk in str(value or "").split(";"):
        part = chunk.strip()
        if not part:
            continue
        if ":" in part:
            label, raw_count = part.rsplit(":", 1)
            counter[_digits_only(label)] += _to_int(raw_count, default=1)
        else:
            counter[_digits_only(part)] += 1
    items = []
    for key, count in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])):
        if key:
            items.append({"value": key, "count": int(count)})
    return items


def _parse_rows_field(value: object) -> List[str]:
    out = []
    for token in str(value or "").split(","):
        item = token.strip()
        if item:
            out.append(item)
    return out


def _is_three_value_like(value: object) -> bool:
    vals = {DIGIT_TO_VTRAC_VALUE[ch] for ch in _digits_only(value) if ch in DIGIT_TO_VTRAC_VALUE}
    return bool(vals) and len(vals) <= 3


def _winner_html_key(path: Path) -> Tuple[str, str]:
    match = WINNER_HTML_RE.search(path.name)
    if not match:
        return (path.name, "")
    return (f"{match.group('vtrac')}::{match.group('winner')}", match.group("stamp"))


def _dedupe_winner_html(paths: Sequence[Path]) -> List[Path]:
    selected: Dict[str, Tuple[str, Path]] = {}
    for path in sorted(paths):
        key, stamp = _winner_html_key(path)
        current = selected.get(key)
        if current is None or stamp > current[0]:
            selected[key] = (stamp, path)
    return sorted((item[1] for item in selected.values()), key=lambda p: p.name)


def _case_key(section: str, set_name: str, draw: str, column: str) -> Tuple[str, str, str, str]:
    return (section, set_name, draw, str(column))


def _case_key_text(key: Tuple[str, str, str, str]) -> str:
    section, set_name, draw, column = key
    return f"{section}:{set_name}:{draw}:Col{column}"


def _resolve_case_paths(sharepacks_root: Path, case_spec: str) -> Dict[str, Any]:
    if ":" not in case_spec:
        raise ValueError(f"Case must be DATE:STATE, got {case_spec!r}")
    results_date, state_key = case_spec.split(":", 1)
    state_dir = sharepacks_root / results_date / state_key
    stable_dir = state_dir / "stable" / state_key
    winners_dir = state_dir / "winners" / state_key
    if not stable_dir.exists():
        raise FileNotFoundError(f"Missing stable dir for {case_spec}: {stable_dir}")
    scores_path = stable_dir / f"{state_key}_stable_patterns_scores.csv"
    families_path = stable_dir / f"{state_key}_stable_patterns_families.csv"
    compound_path = stable_dir / f"{state_key}_stable_patterns_compound.csv"
    metrics_path = stable_dir / f"{state_key}_metrics.json"
    missing = [path for path in (scores_path, families_path, compound_path, metrics_path) if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required stable artifacts for {case_spec}: {missing}")
    winner_htmls = _dedupe_winner_html(sorted(winners_dir.glob("*.html"))) if winners_dir.exists() else []
    return {
        "case_spec": case_spec,
        "results_date": results_date,
        "state_key": state_key,
        "state_dir": state_dir,
        "scores_path": scores_path,
        "families_path": families_path,
        "compound_path": compound_path,
        "metrics_path": metrics_path,
        "winner_htmls": winner_htmls,
    }


def _parse_winner_html_truth(html_paths: Sequence[Path]) -> Dict[Tuple[str, str, str, str], Dict[str, Any]]:
    boxes: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for html_path in html_paths:
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
        for heading in soup.find_all("h2"):
            text = heading.get_text(" ", strip=True)
            if "Combined Table" not in text:
                continue
            section_match = re.search(r"\b(Midday|Evening|Combined)\b", text)
            if not section_match:
                continue
            section = section_match.group(1)
            table = heading.find_next_sibling("table")
            if table is None:
                continue
            rows = table.find_all("tr")
            if not rows:
                continue
            headers = [cell.get_text(" ", strip=True) for cell in rows[0].find_all(["th", "td"])]
            if len(headers) < 4:
                continue
            col_headers = [str(h).strip() for h in headers[3:]]
            for row in rows[1:]:
                cells = row.find_all("td")
                if len(cells) < 4:
                    continue
                set_name = cells[0].get_text(" ", strip=True)
                draw = cells[1].get_text(" ", strip=True)
                row_type = cells[2].get_text(" ", strip=True)
                if row_type not in {"R2", "R4", "R6", "R8", "CONS_STUB"}:
                    continue
                for column, cell in zip(col_headers, cells[3:]):
                    if str(column).strip() not in TABLE_COLS:
                        continue
                    cell_classes = set(cell.get("class", []))
                    descendant_counts = Counter()
                    for class_name in HTML_TRUTH_CLASSES:
                        descendant_counts[class_name] = len(cell.select(f".{class_name}"))
                    key = _case_key(section, set_name, draw, str(column).strip())
                    entry = boxes.setdefault(
                        key,
                        {
                            "html_sources": set(),
                            "row_types_ls_box": set(),
                            "row_types_hit_winner": set(),
                            "row_types_hit_vt_straight": set(),
                            "row_types_hit_family": set(),
                            "ls_box_sources": set(),
                            "winner_sources": set(),
                            "vt_sources": set(),
                            "family_sources": set(),
                            "cell_text_examples": [],
                        },
                    )
                    entry["html_sources"].add(html_path.name)
                    has_ls = "ls-box" in cell_classes or "ls-box-edge" in cell_classes
                    has_winner = descendant_counts["hit-winner"] > 0 or descendant_counts["hit-winner-gap"] > 0
                    has_vt = descendant_counts["hit-vt-straight"] > 0 or descendant_counts["hit-vt-straight-gap"] > 0
                    has_family = descendant_counts["hit-family"] > 0 or descendant_counts["hit-family-gap"] > 0
                    if has_ls:
                        entry["row_types_ls_box"].add(row_type)
                        entry["ls_box_sources"].add(html_path.name)
                    if has_winner:
                        entry["row_types_hit_winner"].add(row_type)
                        entry["winner_sources"].add(html_path.name)
                    if has_vt:
                        entry["row_types_hit_vt_straight"].add(row_type)
                        entry["vt_sources"].add(html_path.name)
                    if has_family:
                        entry["row_types_hit_family"].add(row_type)
                        entry["family_sources"].add(html_path.name)
                    if has_ls or has_winner or has_vt or has_family:
                        snippet = cell.get_text(" ", strip=True)
                        if snippet and len(entry["cell_text_examples"]) < 6:
                            entry["cell_text_examples"].append(f"{row_type}:{snippet}")

    normalized: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for key, entry in boxes.items():
        normalized[key] = {
            "html_sources": sorted(entry["html_sources"]),
            "html_source_count": len(entry["html_sources"]),
            "ls_box_any": bool(entry["row_types_ls_box"]),
            "hit_winner_any": bool(entry["row_types_hit_winner"]),
            "hit_vt_straight_any": bool(entry["row_types_hit_vt_straight"]),
            "hit_family_any": bool(entry["row_types_hit_family"]),
            "row_types_ls_box": sorted(entry["row_types_ls_box"]),
            "row_types_hit_winner": sorted(entry["row_types_hit_winner"]),
            "row_types_hit_vt_straight": sorted(entry["row_types_hit_vt_straight"]),
            "row_types_hit_family": sorted(entry["row_types_hit_family"]),
            "ls_box_source_count": len(entry["ls_box_sources"]),
            "winner_source_count": len(entry["winner_sources"]),
            "vt_source_count": len(entry["vt_sources"]),
            "family_source_count": len(entry["family_sources"]),
            "cell_text_examples": entry["cell_text_examples"],
        }
    return normalized


def _build_raw_survivor_boxes(
    *,
    score_rows: Sequence[Dict[str, str]],
    family_rows: Sequence[Dict[str, str]],
    min_rows_cov: int,
) -> Tuple[Dict[Tuple[str, str, str, str], Dict[str, Any]], Dict[Tuple[str, str, str], List[str]]]:
    score_by_box: Dict[Tuple[str, str, str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in score_rows:
        key = _case_key(
            str(row.get("section") or "").strip() or "Unknown",
            str(row.get("Set") or "").strip() or "Unknown",
            str(row.get("Draw") or "").strip() or "Unknown",
            str(row.get("Column") or "").strip() or "0",
        )
        score_by_box[key].append(row)

    eligible_family_rows: Dict[Tuple[str, str, str], List[Dict[str, str]]] = defaultdict(list)
    family_by_box: Dict[Tuple[str, str, str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in family_rows:
        if _to_int(row.get("rows_cov"), default=0) < min_rows_cov:
            continue
        key3 = (
            str(row.get("section") or "").strip() or "Unknown",
            str(row.get("Set") or "").strip() or "Unknown",
            str(row.get("Draw") or "").strip() or "Unknown",
        )
        key4 = key3 + (str(row.get("Column") or "").strip() or "0",)
        eligible_family_rows[key3].append(row)
        family_by_box[key4].append(row)

    progression_columns: Dict[Tuple[str, str, str], List[str]] = {}
    frontier_keys: Dict[Tuple[str, str, str], Tuple[str, str, str, str]] = {}
    for key3, rows in eligible_family_rows.items():
        cols = sorted({str(_to_int(row.get("Column"), default=0)) for row in rows}, key=lambda v: int(v))
        if not cols:
            continue
        progression_columns[key3] = cols
        frontier_keys[key3] = key3 + (cols[-1],)

    boxes: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for key4, rows in family_by_box.items():
        section, set_name, draw, column = key4
        score_box_rows = score_by_box.get(key4, [])
        exact3 = sorted({_digits_only(row.get("Canonical")) for row in score_box_rows if len(_digits_only(row.get("Canonical"))) == 3})
        vtrac_like = sorted({_digits_only(row.get("Canonical")) for row in score_box_rows if _is_three_value_like(row.get("Canonical"))})
        vtrac_indices = Counter()
        for value in exact3:
            try:
                idx = int(derive_vtrac_index_for_canonical(value, get_vtrac_index))
            except Exception:
                continue
            vtrac_indices[str(idx)] += 1
        family_top = sorted(
            {item["value"] for row in rows for item in _parse_counter_blob(row.get("top_canonicals")) if item.get("value")}
        )
        row_types = sorted({rt for row in score_box_rows for rt in _parse_rows_field(row.get("rows"))})
        key3 = (section, set_name, draw)
        progression_cols = progression_columns.get(key3, [column])
        frontier_key = frontier_keys.get(key3)
        boxes[key4] = {
            "section": section,
            "set": set_name,
            "draw": draw,
            "column": column,
            "box_key": _case_key_text(key4),
            "raw_box_present": True,
            "raw_family_count": len(rows),
            "raw_family_ids": sorted({_to_int(row.get("family_id"), default=0) for row in rows if _to_int(row.get("family_id"), default=0) > 0}),
            "raw_frontier": key4 == frontier_key,
            "raw_single_family_frontier": len(rows) == 1 if key4 == frontier_key else False,
            "raw_rows_cov_max": max((_to_int(row.get("rows_cov"), default=0) for row in rows), default=0),
            "raw_last_remaining_family_count": sum(1 for row in rows if _to_bool(row.get("last_remaining_3v"))),
            "raw_progression_family_count": sum(1 for row in rows if _to_bool(row.get("progression_flag"))),
            "raw_any_consensus_family_count": sum(1 for row in rows if _to_bool(row.get("any_consensus"))),
            "raw_any_vtrac_family_count": sum(1 for row in rows if _to_bool(row.get("any_vtrac_straight"))),
            "raw_any_hidden3v_family_count": sum(1 for row in rows if _to_bool(row.get("any_hidden3v"))),
            "raw_exact3digit_patterns": exact3,
            "raw_vtrac_like_patterns": vtrac_like,
            "raw_vtrac_indices": [item[0] for item in sorted(vtrac_indices.items(), key=lambda kv: (-kv[1], kv[0]))],
            "raw_hidden_terminal_patterns": sorted(value for value in family_top if len(value) > 3),
            "raw_score_row_count": len(score_box_rows),
            "raw_score_rowtypes": row_types,
            "raw_family_top_canonicals": family_top,
            "progression_columns": progression_cols,
            "progression_column_count": len(progression_cols),
            "frontier_column": frontier_key[3] if frontier_key else column,
        }
    return boxes, progression_columns


def _classify_last_remaining(raw: Dict[str, Any]) -> Tuple[str, List[str]]:
    if _to_int(raw.get("raw_last_remaining_family_count"), default=0) <= 0:
        return ("", [])

    exact_patterns = list(raw.get("raw_exact3digit_patterns") or [])
    vtrac_indices = list(raw.get("raw_vtrac_indices") or [])
    hidden_patterns = list(raw.get("raw_hidden_terminal_patterns") or [])
    tags: List[str] = ["last_remaining_present"]

    if hidden_patterns:
        tags.append("last_remaining_hidden_support")
    if len(vtrac_indices) == 1 and exact_patterns:
        tags.append("last_remaining_single_vtrac_family")
    elif len(vtrac_indices) > 1:
        tags.append("last_remaining_multi_vtrac_family")
    if len(exact_patterns) == 1:
        tags.append("last_remaining_single_exact_literal")
        profile = "exact_single_literal"
    elif len(exact_patterns) > 1 and len(vtrac_indices) == 1:
        tags.append("last_remaining_multi_literal_single_vtrac")
        profile = "multi_literal_single_vtrac_family"
    elif len(exact_patterns) > 1:
        tags.append("last_remaining_multi_literal_mixed")
        profile = "multi_literal_mixed_family"
    elif len(vtrac_indices) == 1 and raw.get("raw_vtrac_like_patterns"):
        tags.append("last_remaining_hidden_vtrac_terminal")
        profile = "hidden_single_vtrac_family"
    else:
        tags.append("last_remaining_unresolved")
        profile = "unresolved_terminal"

    if hidden_patterns and profile in {"exact_single_literal", "multi_literal_single_vtrac_family", "hidden_single_vtrac_family"}:
        profile = f"{profile}_with_hidden_support"
    return (profile, tags)


def _classify_last_remaining_truth_support(
    *,
    raw: Dict[str, Any],
    html: Dict[str, Any],
    structural_profile: str,
) -> Tuple[str, List[str], str]:
    if not structural_profile:
        return ("", [], "")

    tags: List[str] = []
    support_tokens: List[str] = []
    if html.get("hit_winner_any"):
        tags.append("last_remaining_truth_winner")
        support_tokens.append("winner")
    if html.get("hit_vt_straight_any"):
        tags.append("last_remaining_truth_vt")
        support_tokens.append("vt")
    if html.get("hit_family_any"):
        tags.append("last_remaining_truth_family")
        support_tokens.append("family")
    if raw.get("raw_hidden_terminal_patterns"):
        tags.append("last_remaining_truth_hidden")
        support_tokens.append("hidden")

    if not support_tokens:
        return ("none", tags, structural_profile)

    support_class = "_".join(support_tokens)
    enriched_profile = f"{structural_profile}__{support_class}"
    return (support_class, tags, enriched_profile)


def _build_arena_frontier_boxes(payload: Dict[str, Any]) -> Dict[Tuple[str, str, str, str], Dict[str, Any]]:
    out: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for section, block in (payload.get("sections") or {}).items():
        for frontier in block.get("survivor_frontiers") or []:
            key = _case_key(
                section,
                str(frontier.get("set") or "").strip() or "Unknown",
                str(frontier.get("draw") or "").strip() or "Unknown",
                str(frontier.get("frontier_column") or "0"),
            )
            entries = frontier.get("entries") or []
            top_canonicals = sorted(
                {
                    _digits_only(item.get("value"))
                    for entry in entries
                    for item in (entry.get("top_canonicals") or [])
                    if _digits_only(item.get("value"))
                }
            )
            frontier_pattern_summary = frontier.get("frontier_pattern_summary") or {}
            arena_exact3digit_patterns = sorted(
                {
                    _digits_only(item.get("value"))
                    for item in (frontier_pattern_summary.get("exact3digit_patterns_top") or [])
                    if _digits_only(item.get("value"))
                }
            )
            if frontier_pattern_summary.get("exact3digit_patterns_all"):
                arena_exact3digit_patterns = sorted(
                    {
                        _digits_only(item)
                        for item in (frontier_pattern_summary.get("exact3digit_patterns_all") or [])
                        if _digits_only(item)
                    }
                )
            arena_three_value_patterns = sorted(
                {
                    _digits_only(item.get("value"))
                    for item in (frontier_pattern_summary.get("three_value_like_patterns_top") or [])
                    if _digits_only(item.get("value"))
                }
            )
            if frontier_pattern_summary.get("three_value_like_patterns_all"):
                arena_three_value_patterns = sorted(
                    {
                        _digits_only(item)
                        for item in (frontier_pattern_summary.get("three_value_like_patterns_all") or [])
                        if _digits_only(item)
                    }
                )
            out[key] = {
                "arena_frontier": True,
                "arena_single_family_frontier": bool(frontier.get("is_single_family")),
                "arena_frontier_family_count": _to_int(frontier.get("frontier_family_count"), default=0),
                "arena_family_ids": sorted(_to_int(fid, default=0) for fid in (frontier.get("family_ids") or []) if _to_int(fid, default=0) > 0),
                "arena_last_remaining_entry_count": sum(1 for entry in entries if _to_bool(entry.get("last_remaining_3v"))),
                "arena_progression_entry_count": sum(1 for entry in entries if _to_bool(entry.get("progression_flag"))),
                "arena_any_vtrac_entry_count": sum(1 for entry in entries if _to_bool(entry.get("any_vtrac_straight"))),
                "arena_any_consensus_entry_count": sum(1 for entry in entries if _to_bool(entry.get("any_consensus"))),
                "arena_top_canonicals": top_canonicals,
                "arena_exact3digit_patterns": arena_exact3digit_patterns,
                "arena_three_value_like_patterns": arena_three_value_patterns,
                "arena_vtrac_indices": sorted(
                    {
                        str(item.get("value"))
                        for item in (frontier_pattern_summary.get("vtrac_indices_top") or [])
                        if str(item.get("value") or "").strip()
                    }
                )
                or sorted(
                    {
                        str(item).strip()
                        for item in (frontier_pattern_summary.get("vtrac_indices_all") or [])
                        if str(item).strip()
                    }
                ),
            }
    return out


def _build_arena_progression_map(payload: Dict[str, Any]) -> Dict[Tuple[str, str, str], Dict[str, Any]]:
    out: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for section, block in (payload.get("sections") or {}).items():
        for progression in block.get("survivor_progressions") or []:
            key = (
                section,
                str(progression.get("set") or "").strip() or "Unknown",
                str(progression.get("draw") or "").strip() or "Unknown",
            )
            out[key] = {
                "arena_progression_present": True,
                "arena_progression_columns": [str(item) for item in (progression.get("eligible_columns") or [])],
                "arena_progression_column_count": _to_int(progression.get("progression_column_count"), default=0),
                "arena_progression_frontier_column": str(progression.get("frontier_column") or ""),
                "arena_progression_has_last_remaining": bool(progression.get("has_last_remaining")),
            }
    return out


def _compare_case(
    *,
    case_paths: Dict[str, Any],
    repo_root: Path,
    sharepacks_root: Path,
    min_rows_cov: int,
) -> Dict[str, Any]:
    score_rows = _load_csv_rows(case_paths["scores_path"])
    family_rows = _load_csv_rows(case_paths["families_path"])
    raw_boxes, progression_columns = _build_raw_survivor_boxes(
        score_rows=score_rows,
        family_rows=family_rows,
        min_rows_cov=min_rows_cov,
    )
    stable_payload = build_stable_arena_payload(
        state_dir=case_paths["state_dir"],
        state_key=case_paths["state_key"],
        results_date=case_paths["results_date"],
        history_date=case_paths["results_date"],
        profile="audit",
        experiment_tag="survivor_capture_review",
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=bool(case_paths["winner_htmls"]),
        repo_root=repo_root,
        top_rows=25,
        top_pattern_ledgers=25,
        top_compound=25,
        top_families=12,
    )
    if not stable_payload:
        raise RuntimeError(f"Unable to build stable arena payload for {case_paths['case_spec']}")
    arena_boxes = _build_arena_frontier_boxes(stable_payload)
    arena_progressions = _build_arena_progression_map(stable_payload)
    html_boxes = _parse_winner_html_truth(case_paths["winner_htmls"])

    all_keys = sorted(set(raw_boxes) | set(arena_boxes) | set(html_boxes))
    ledger: List[Dict[str, Any]] = []
    tags_counter: Counter[str] = Counter()
    for key in all_keys:
        raw = raw_boxes.get(key, {})
        arena = arena_boxes.get(key, {})
        html = html_boxes.get(key, {})
        arena_progression = arena_progressions.get((key[0], key[1], key[2]), {})
        last_remaining_profile, last_remaining_tags = _classify_last_remaining(raw)
        last_remaining_support_class, last_remaining_support_tags, last_remaining_enriched_profile = (
            _classify_last_remaining_truth_support(
                raw=raw,
                html=html,
                structural_profile=last_remaining_profile,
            )
        )
        raw_exact = set(raw.get("raw_exact3digit_patterns") or [])
        arena_exact = set(arena.get("arena_exact3digit_patterns") or []) or set(arena.get("arena_top_canonicals") or [])
        missing_from_arena = sorted(raw_exact - arena_exact)
        gap_tags: List[str] = []
        if raw.get("raw_frontier") and arena.get("arena_frontier"):
            gap_tags.append("raw_frontier_preserved_in_arena")
        if html.get("ls_box_any") and raw.get("raw_frontier"):
            gap_tags.append("html_ls_box_on_raw_frontier")
        if html.get("hit_winner_any") and raw.get("raw_frontier"):
            gap_tags.append("winner_on_raw_frontier")
        if html.get("hit_vt_straight_any") and raw.get("raw_frontier"):
            gap_tags.append("vt_hit_on_raw_frontier")
        if html.get("ls_box_any") and not raw.get("raw_frontier"):
            gap_tags.append("html_ls_without_raw_frontier")
        if raw.get("raw_frontier") and not html.get("ls_box_any"):
            gap_tags.append("raw_frontier_without_html_ls")
        if raw.get("progression_column_count", 0) > 1:
            gap_tags.append("progression_chain_present")
        if raw.get("progression_column_count", 0) > 1 and arena_progression.get("arena_progression_present"):
            if list(raw.get("progression_columns") or []) == list(arena_progression.get("arena_progression_columns") or []):
                gap_tags.append("arena_progression_preserved")
            elif raw.get("raw_frontier") and arena.get("arena_frontier"):
                gap_tags.append("arena_frontier_snapshot_of_progression")
        elif raw.get("raw_frontier") and raw.get("progression_column_count", 0) > 1 and arena.get("arena_frontier"):
            gap_tags.append("arena_frontier_snapshot_of_progression")
        if raw.get("raw_frontier") and missing_from_arena:
            gap_tags.append("exact3digit_patterns_compressed_by_arena")
        if (
            raw.get("raw_frontier")
            and raw.get("raw_vtrac_like_patterns")
            and not arena.get("arena_any_vtrac_entry_count")
            and not arena.get("arena_three_value_like_patterns")
        ):
            gap_tags.append("vtrac_like_patterns_not_flagged_in_arena")
        gap_tags.extend(last_remaining_tags)
        gap_tags.extend(last_remaining_support_tags)
        for tag in gap_tags:
            tags_counter[tag] += 1
        ledger.append(
            {
                "case_spec": case_paths["case_spec"],
                "state_key": case_paths["state_key"],
                "results_date": case_paths["results_date"],
                "section": key[0],
                "set": key[1],
                "draw": key[2],
                "column": key[3],
                "box_key": _case_key_text(key),
                "raw_box_present": bool(raw),
                "raw_frontier": bool(raw.get("raw_frontier")),
                "raw_single_family_frontier": bool(raw.get("raw_single_family_frontier")),
                "raw_family_count": _to_int(raw.get("raw_family_count"), default=0),
                "raw_last_remaining_family_count": _to_int(raw.get("raw_last_remaining_family_count"), default=0),
                "raw_progression_family_count": _to_int(raw.get("raw_progression_family_count"), default=0),
                "raw_any_vtrac_family_count": _to_int(raw.get("raw_any_vtrac_family_count"), default=0),
                "raw_any_consensus_family_count": _to_int(raw.get("raw_any_consensus_family_count"), default=0),
                "progression_column_count": _to_int(raw.get("progression_column_count"), default=0),
                "progression_columns": ",".join(raw.get("progression_columns") or []),
                "raw_exact3digit_patterns": ",".join(raw.get("raw_exact3digit_patterns") or []),
                "raw_vtrac_like_patterns": ",".join(raw.get("raw_vtrac_like_patterns") or []),
                "raw_vtrac_indices": ",".join(raw.get("raw_vtrac_indices") or []),
                "raw_hidden_terminal_patterns": ",".join(raw.get("raw_hidden_terminal_patterns") or []),
                "raw_family_top_canonicals": ",".join(raw.get("raw_family_top_canonicals") or []),
                "raw_score_rowtypes": ",".join(raw.get("raw_score_rowtypes") or []),
                "arena_frontier": bool(arena.get("arena_frontier")),
                "arena_single_family_frontier": bool(arena.get("arena_single_family_frontier")),
                "arena_frontier_family_count": _to_int(arena.get("arena_frontier_family_count"), default=0),
                "arena_last_remaining_entry_count": _to_int(arena.get("arena_last_remaining_entry_count"), default=0),
                "arena_progression_entry_count": _to_int(arena.get("arena_progression_entry_count"), default=0),
                "arena_any_vtrac_entry_count": _to_int(arena.get("arena_any_vtrac_entry_count"), default=0),
                "arena_any_consensus_entry_count": _to_int(arena.get("arena_any_consensus_entry_count"), default=0),
                "arena_top_canonicals": ",".join(arena.get("arena_top_canonicals") or []),
                "arena_exact3digit_patterns": ",".join(arena.get("arena_exact3digit_patterns") or []),
                "arena_three_value_like_patterns": ",".join(arena.get("arena_three_value_like_patterns") or []),
                "arena_vtrac_indices": ",".join(arena.get("arena_vtrac_indices") or []),
                "arena_progression_present": bool(arena_progression.get("arena_progression_present")),
                "arena_progression_columns": ",".join(arena_progression.get("arena_progression_columns") or []),
                "raw_exact3digit_missing_from_arena": ",".join(missing_from_arena),
                "html_present": bool(html),
                "html_ls_box": bool(html.get("ls_box_any")),
                "html_hit_winner": bool(html.get("hit_winner_any")),
                "html_hit_vt_straight": bool(html.get("hit_vt_straight_any")),
                "html_hit_family": bool(html.get("hit_family_any")),
                "html_row_types_ls_box": ",".join(html.get("row_types_ls_box") or []),
                "html_row_types_hit_winner": ",".join(html.get("row_types_hit_winner") or []),
                "html_row_types_hit_vt_straight": ",".join(html.get("row_types_hit_vt_straight") or []),
                "html_row_types_hit_family": ",".join(html.get("row_types_hit_family") or []),
                "html_sources": ",".join(html.get("html_sources") or []),
                "last_remaining_profile": last_remaining_profile,
                "last_remaining_support_class": last_remaining_support_class,
                "last_remaining_enriched_profile": last_remaining_enriched_profile,
                "gap_tags": ",".join(gap_tags),
            }
        )

    def _count(predicate: Any) -> int:
        return sum(1 for item in ledger if predicate(item))

    def _sequence_count(tag: str) -> int:
        return len(
            {
                (item["section"], item["set"], item["draw"])
                for item in ledger
                if tag in item["gap_tags"].split(",")
            }
        )

    gap_examples = {
        "html_ls_without_raw_frontier": [item["box_key"] for item in ledger if "html_ls_without_raw_frontier" in item["gap_tags"].split(",")][:8],
        "arena_pattern_compression": [item["box_key"] for item in ledger if "exact3digit_patterns_compressed_by_arena" in item["gap_tags"].split(",")][:8],
        "progression_snapshot_boxes": [item["box_key"] for item in ledger if "arena_frontier_snapshot_of_progression" in item["gap_tags"].split(",")][:8],
        "winner_on_raw_frontier": [item["box_key"] for item in ledger if "winner_on_raw_frontier" in item["gap_tags"].split(",")][:8],
        "vt_hit_on_raw_frontier": [item["box_key"] for item in ledger if "vt_hit_on_raw_frontier" in item["gap_tags"].split(",")][:8],
        "last_remaining_profiles": [
            f"{item['box_key']}:{item['last_remaining_profile']}"
            for item in ledger
            if item["last_remaining_profile"]
        ][:8],
        "last_remaining_enriched_profiles": [
            f"{item['box_key']}:{item['last_remaining_enriched_profile']}"
            for item in ledger
            if item["last_remaining_enriched_profile"]
        ][:8],
    }

    last_remaining_profile_counts = Counter(
        item["last_remaining_profile"] for item in ledger if item.get("last_remaining_profile")
    )
    last_remaining_support_counts = Counter(
        item["last_remaining_support_class"] for item in ledger if item.get("last_remaining_support_class")
    )
    last_remaining_enriched_profile_counts = Counter(
        item["last_remaining_enriched_profile"] for item in ledger if item.get("last_remaining_enriched_profile")
    )

    summary = {
        "winner_html_files_used": len(case_paths["winner_htmls"]),
        "raw_survivor_boxes": len(raw_boxes),
        "raw_frontier_boxes": _count(lambda item: item["raw_frontier"]),
        "raw_single_family_frontiers": _count(lambda item: item["raw_frontier"] and item["raw_single_family_frontier"]),
        "raw_multi_family_frontiers": _count(lambda item: item["raw_frontier"] and not item["raw_single_family_frontier"]),
        "raw_last_remaining_boxes": _count(lambda item: item["raw_last_remaining_family_count"] > 0),
        "last_remaining_profile_counts": dict(sorted(last_remaining_profile_counts.items())),
        "last_remaining_support_counts": dict(sorted(last_remaining_support_counts.items())),
        "last_remaining_enriched_profile_counts": dict(sorted(last_remaining_enriched_profile_counts.items())),
        "raw_progression_chain_boxes": _count(lambda item: item["progression_column_count"] > 1),
        "raw_progression_sequences": sum(1 for columns in progression_columns.values() if len(columns) > 1),
        "raw_frontier_boxes_with_exact3digit_patterns": _count(lambda item: item["raw_frontier"] and bool(item["raw_exact3digit_patterns"])),
        "raw_frontier_boxes_with_vtrac_like_patterns": _count(lambda item: item["raw_frontier"] and bool(item["raw_vtrac_like_patterns"])),
        "html_truth_boxes": len(html_boxes),
        "html_ls_boxes": _count(lambda item: item["html_ls_box"]),
        "html_hit_winner_boxes": _count(lambda item: item["html_hit_winner"]),
        "html_hit_vt_straight_boxes": _count(lambda item: item["html_hit_vt_straight"]),
        "html_hit_family_boxes": _count(lambda item: item["html_hit_family"]),
        "raw_frontier_overlapping_html_ls": _count(lambda item: item["raw_frontier"] and item["html_ls_box"]),
        "raw_frontier_overlapping_html_winner": _count(lambda item: item["raw_frontier"] and item["html_hit_winner"]),
        "raw_frontier_overlapping_html_vt": _count(lambda item: item["raw_frontier"] and item["html_hit_vt_straight"]),
        "raw_last_remaining_overlapping_html_winner": _count(
            lambda item: item["raw_last_remaining_family_count"] > 0 and item["html_hit_winner"]
        ),
        "raw_last_remaining_overlapping_html_vt": _count(
            lambda item: item["raw_last_remaining_family_count"] > 0 and item["html_hit_vt_straight"]
        ),
        "raw_last_remaining_overlapping_html_family": _count(
            lambda item: item["raw_last_remaining_family_count"] > 0 and item["html_hit_family"]
        ),
        "arena_frontier_boxes": _count(lambda item: item["arena_frontier"]),
        "raw_frontier_not_in_arena": _count(lambda item: item["raw_frontier"] and not item["arena_frontier"]),
        "html_ls_without_raw_frontier": _count(lambda item: item["html_ls_box"] and not item["raw_frontier"]),
        "arena_pattern_compression_boxes": _count(
            lambda item: item["raw_frontier"] and bool(item["raw_exact3digit_missing_from_arena"])
        ),
        "arena_progression_preserved_sequences": _sequence_count("arena_progression_preserved"),
        "arena_progression_snapshot_sequences": _sequence_count("arena_frontier_snapshot_of_progression"),
        "tag_counts": dict(sorted(tags_counter.items())),
        "gap_examples": gap_examples,
    }

    return {
        "case_spec": case_paths["case_spec"],
        "results_date": case_paths["results_date"],
        "state_key": case_paths["state_key"],
        "paths": {
            "state_dir": str(case_paths["state_dir"]),
            "scores_path": str(case_paths["scores_path"]),
            "families_path": str(case_paths["families_path"]),
            "winner_htmls": [str(path) for path in case_paths["winner_htmls"]],
        },
        "summary": summary,
        "stable_arena_summary": {
            section: block.get("summary") or {}
            for section, block in (stable_payload.get("sections") or {}).items()
        },
        "ledger": ledger,
        "progression_columns": {
            f"{section}:{set_name}:{draw}": columns
            for (section, set_name, draw), columns in sorted(progression_columns.items())
        },
    }


def build_survivor_capture_audit(
    *,
    repo_root: Path,
    sharepacks_root: Path,
    case_specs: Sequence[str],
    min_rows_cov: int = 3,
) -> Dict[str, Any]:
    cases = []
    all_ledger: List[Dict[str, Any]] = []
    cohort_counter: Counter[str] = Counter()
    for case_spec in case_specs:
        case_paths = _resolve_case_paths(sharepacks_root, case_spec)
        case_payload = _compare_case(
            case_paths=case_paths,
            repo_root=repo_root,
            sharepacks_root=sharepacks_root,
            min_rows_cov=min_rows_cov,
        )
        cases.append(case_payload)
        all_ledger.extend(case_payload["ledger"])
        for tag, count in (case_payload["summary"].get("tag_counts") or {}).items():
            cohort_counter[tag] += _to_int(count, default=0)
    cohort_summary = {
        "case_count": len(cases),
        "cases": [case["case_spec"] for case in cases],
        "total_raw_frontier_boxes": sum(case["summary"]["raw_frontier_boxes"] for case in cases),
        "total_html_ls_boxes": sum(case["summary"]["html_ls_boxes"] for case in cases),
        "total_arena_pattern_compression_boxes": sum(case["summary"]["arena_pattern_compression_boxes"] for case in cases),
        "total_html_ls_without_raw_frontier": sum(case["summary"]["html_ls_without_raw_frontier"] for case in cases),
        "tag_counts": dict(sorted(cohort_counter.items())),
    }
    return {
        "schema": "stable_survivor_capture_audit_v1",
        "generated_on": date.today().isoformat(),
        "sharepacks_root": str(sharepacks_root),
        "min_rows_cov": int(min_rows_cov),
        "cohort_summary": cohort_summary,
        "cases": cases,
        "box_ledger": all_ledger,
    }


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_audit_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Stable Survivor Capture Audit")
    lines.append("")
    lines.append("Purpose: compare raw stable survivor extraction, winner HTML survivor truth, and current stable arena preservation.")
    lines.append("")
    cohort = payload.get("cohort_summary") or {}
    lines.append("## Cohort Summary")
    lines.append("")
    lines.append(f"- cases: `{', '.join(cohort.get('cases') or [])}`")
    lines.append(f"- total_raw_frontier_boxes: `{cohort.get('total_raw_frontier_boxes', 0)}`")
    lines.append(f"- total_html_ls_boxes: `{cohort.get('total_html_ls_boxes', 0)}`")
    lines.append(f"- total_arena_pattern_compression_boxes: `{cohort.get('total_arena_pattern_compression_boxes', 0)}`")
    lines.append(f"- total_html_ls_without_raw_frontier: `{cohort.get('total_html_ls_without_raw_frontier', 0)}`")
    tag_counts = cohort.get("tag_counts") or {}
    if tag_counts:
        lines.append(f"- tag_counts: `{json.dumps(tag_counts, sort_keys=True)}`")
    for case in payload.get("cases") or []:
        summary = case.get("summary") or {}
        lines.append("")
        lines.append(f"## {case.get('case_spec')}")
        lines.append("")
        lines.append(f"- winner_html_files_used: `{summary.get('winner_html_files_used', 0)}`")
        lines.append(f"- raw_survivor_boxes: `{summary.get('raw_survivor_boxes', 0)}`")
        lines.append(f"- raw_frontier_boxes: `{summary.get('raw_frontier_boxes', 0)}`")
        lines.append(f"- raw_progression_chain_boxes: `{summary.get('raw_progression_chain_boxes', 0)}`")
        lines.append(f"- raw_progression_sequences: `{summary.get('raw_progression_sequences', 0)}`")
        lines.append(f"- raw_last_remaining_boxes: `{summary.get('raw_last_remaining_boxes', 0)}`")
        profile_counts = summary.get("last_remaining_profile_counts") or {}
        if profile_counts:
            lines.append(f"- last_remaining_profile_counts: `{json.dumps(profile_counts, sort_keys=True)}`")
        support_counts = summary.get("last_remaining_support_counts") or {}
        if support_counts:
            lines.append(f"- last_remaining_support_counts: `{json.dumps(support_counts, sort_keys=True)}`")
        enriched_profile_counts = summary.get("last_remaining_enriched_profile_counts") or {}
        if enriched_profile_counts:
            lines.append(f"- last_remaining_enriched_profile_counts: `{json.dumps(enriched_profile_counts, sort_keys=True)}`")
        lines.append(f"- html_ls_boxes: `{summary.get('html_ls_boxes', 0)}`")
        lines.append(f"- html_hit_winner_boxes: `{summary.get('html_hit_winner_boxes', 0)}`")
        lines.append(f"- html_hit_vt_straight_boxes: `{summary.get('html_hit_vt_straight_boxes', 0)}`")
        lines.append(f"- raw_frontier_overlapping_html_ls: `{summary.get('raw_frontier_overlapping_html_ls', 0)}`")
        lines.append(f"- raw_frontier_overlapping_html_winner: `{summary.get('raw_frontier_overlapping_html_winner', 0)}`")
        lines.append(f"- raw_frontier_overlapping_html_vt: `{summary.get('raw_frontier_overlapping_html_vt', 0)}`")
        lines.append(f"- raw_last_remaining_overlapping_html_winner: `{summary.get('raw_last_remaining_overlapping_html_winner', 0)}`")
        lines.append(f"- raw_last_remaining_overlapping_html_vt: `{summary.get('raw_last_remaining_overlapping_html_vt', 0)}`")
        lines.append(f"- raw_last_remaining_overlapping_html_family: `{summary.get('raw_last_remaining_overlapping_html_family', 0)}`")
        lines.append(f"- arena_frontier_boxes: `{summary.get('arena_frontier_boxes', 0)}`")
        lines.append(f"- raw_frontier_not_in_arena: `{summary.get('raw_frontier_not_in_arena', 0)}`")
        lines.append(f"- arena_pattern_compression_boxes: `{summary.get('arena_pattern_compression_boxes', 0)}`")
        lines.append(f"- arena_progression_preserved_sequences: `{summary.get('arena_progression_preserved_sequences', 0)}`")
        lines.append(f"- arena_progression_snapshot_sequences: `{summary.get('arena_progression_snapshot_sequences', 0)}`")
        lines.append(f"- html_ls_without_raw_frontier: `{summary.get('html_ls_without_raw_frontier', 0)}`")
        gap_examples = summary.get("gap_examples") or {}
        if gap_examples:
            lines.append("")
            lines.append("Examples:")
            for label, items in gap_examples.items():
                if items:
                    lines.append(f"- {label}: `{', '.join(items)}`")
    return "\n".join(lines).rstrip() + "\n"


def write_audit_files(
    *,
    payload: Dict[str, Any],
    out_dir: Path,
    label: str,
) -> Dict[str, Path]:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", label).strip("_") or "survivor_capture_audit"
    stem = f"{payload.get('generated_on', date.today().isoformat())}__STABLE_SURVIVOR_CAPTURE_AUDIT__{slug}"
    json_path = out_dir / f"{stem}.json"
    md_path = out_dir / f"{stem}.md"
    csv_path = out_dir / f"{stem}__box_ledger.csv"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(build_audit_markdown(payload), encoding="utf-8")
    _write_csv(csv_path, payload.get("box_ledger") or [])
    return {"json": json_path, "md": md_path, "csv": csv_path}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sharepacks-root", type=Path, default=Path("sharepacks"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/AAT9_KIT/FINAL VALIDATION/RUNS"))
    parser.add_argument("--label", default="survivor_capture_review")
    parser.add_argument("--min-rows-cov", type=int, default=3)
    parser.add_argument(
        "--case",
        dest="cases",
        action="append",
        required=True,
        help="Case in DATE:STATE form, for example 2025-06-21:Delaware4",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    repo_root = Path(__file__).resolve().parents[2]
    payload = build_survivor_capture_audit(
        repo_root=repo_root,
        sharepacks_root=(repo_root / args.sharepacks_root).resolve() if not args.sharepacks_root.is_absolute() else args.sharepacks_root,
        case_specs=args.cases,
        min_rows_cov=args.min_rows_cov,
    )
    paths = write_audit_files(
        payload=payload,
        out_dir=(repo_root / args.out_dir).resolve() if not args.out_dir.is_absolute() else args.out_dir,
        label=args.label,
    )
    print(json.dumps({key: str(value) for key, value in paths.items()}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
