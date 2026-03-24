#!/usr/bin/env python3
"""Build a Stable-only analysis arena from frozen sharepack artifacts.

The arena is intentionally budget-blind. It preserves detailed Stable evidence
and richer per-variant rollups so example review can inspect what Stable saw
before any candidate compression or budgeting happens downstream.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index


ROW_SCORE_PART_COLUMNS: Tuple[str, ...] = (
    "score_cov",
    "score_hpr",
    "score_perm",
    "score_repeat",
    "score_straight",
    "score_single",
    "score_cons",
    "score_hot",
    "score_mirror",
    "score_dom",
    "score_len",
    "score_hidden",
    "score_vtrac_straight",
    "score_persistence_set",
    "score_persistence_draw",
    "score_double_mirror",
)

ROW_FLAG_COLUMNS: Tuple[str, ...] = (
    "straight2",
    "straight3",
    "single_left",
    "cons_full",
    "cons_3v",
    "cons_stub",
    "dom_last",
    "dom_pair",
    "hidden3v",
    "double_mirror",
)

ROW_COUNT_COLUMNS: Tuple[str, ...] = (
    "perm_count_in_box",
    "repeat_extras_in_box",
    "horizontal_persistence_repeat",
    "persistence_set_count",
    "persistence_draw_run",
)

FAMILY_BREAKDOWN_COLUMNS: Tuple[str, ...] = (
    "fam_cov",
    "fam_hpr",
    "fam_perm",
    "fam_repeat",
    "fam_cons",
    "fam_hot",
    "fam_straight2",
    "fam_straight3",
    "fam_doubles",
    "fam_vtrac",
    "fam_hidden",
    "fam_double_mirror",
    "fam_persistence",
    "fam_section_bonus",
    "fam_progression_bonus",
    "fam_last_remaining_bonus",
)

SAFE_METRICS_KEYS: Tuple[str, ...] = (
    "state",
    "generated_at",
    "total_patterns",
    "total_families",
    "compression_ratio",
    "avg_top_hot_density",
    "health",
    "evidence_schema_version",
    "stable_contract_version",
    "compound_schema_version",
    "signals",
)

SECTION_ORDER: Tuple[str, ...] = ("Midday", "Evening", "Combined")
TABLE_COLS: Tuple[str, ...] = ("7", "6", "5", "4", "3", "2", "1")
ROW_TYPE_ORDER: Tuple[str, ...] = ("R2", "R4", "R6", "R8", "CONS_STUB")
R_CONSENSUS_ROW_TYPES: Tuple[str, ...] = ("R2", "R4", "R6", "R8")
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
MIRROR_MAP: Dict[str, str] = {
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


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _safe_rel(path: Path, repo_root: Path) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _digits_only(value: object) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        if value is None or str(value).strip() == "":
            return float(default)
        return float(value)
    except Exception:
        return float(default)


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
        return [dict(r) for r in csv.DictReader(fh)]


def _hash_inputs(paths: Sequence[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(str(path.name).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _split_why(value: object) -> List[str]:
    return [tok for tok in str(value or "").split("|") if tok]


def _parse_counter_blob(value: object) -> Counter[str]:
    out: Counter[str] = Counter()
    for chunk in str(value or "").split(";"):
        part = chunk.strip()
        if not part:
            continue
        if ":" in part:
            label, raw_count = part.rsplit(":", 1)
            out[label.strip()] += _to_int(raw_count, default=1)
        else:
            out[part] += 1
    return out


def _counter_top(counter: Counter[str], top_n: int = 6) -> List[Dict[str, Any]]:
    items = sorted(counter.items(), key=lambda kv: (-int(kv[1]), kv[0]))
    return [{"value": key, "count": int(count)} for key, count in items[:top_n]]


def _section_sort_key(section: str) -> Tuple[int, str]:
    try:
        return (SECTION_ORDER.index(section), section)
    except ValueError:
        return (len(SECTION_ORDER), section)


def _rowtype_sort_key(row_type: str) -> Tuple[int, str]:
    try:
        return (ROW_TYPE_ORDER.index(row_type), row_type)
    except ValueError:
        return (len(ROW_TYPE_ORDER), row_type)


def _canonical(value: object) -> str:
    return "".join(sorted(_digits_only(value)))


def _normalize_pick3_literal(value: object) -> str:
    digits = _digits_only(value)
    return digits if len(digits) == 3 else ""


def _common_suffix_class(values: Sequence[object]) -> Tuple[str, str]:
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


def _vtrac_values(value: object) -> List[int]:
    return [DIGIT_TO_VTRAC_VALUE[ch] for ch in _digits_only(value) if ch in DIGIT_TO_VTRAC_VALUE]


def _is_three_value_like(value: object) -> bool:
    vals = set(_vtrac_values(value))
    return bool(vals) and len(vals) <= 3


def _hot_level_for_literal(literal: str) -> int:
    if "**" in literal:
        return 2
    if "*" in literal:
        return 1
    return 0


def _is_subsequence(needle: str, haystack: str) -> bool:
    if not needle:
        return False
    cursor = 0
    for ch in haystack:
        if cursor < len(needle) and needle[cursor] == ch:
            cursor += 1
            if cursor == len(needle):
                return True
    return cursor == len(needle)


def _unique_perms(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    return sorted({"".join(p) for p in permutations(triad, 3)})


def _mirror_digit(digit: str) -> str:
    return MIRROR_MAP[digit]


def _r_perm_4(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    a, b, c = triad
    return sorted({a + b + c, a + c + b, b + c + a, c + b + a})


def _keep_pair_mirror_third(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    a, b, c = triad
    return sorted({a + b + _mirror_digit(c), a + c + _mirror_digit(b), b + c + _mirror_digit(a)})


def _method1_pair_mirror_12(triad: str) -> List[str]:
    combos: List[str] = []
    for triad_variant in _keep_pair_mirror_third(triad):
        combos.extend(_r_perm_4(triad_variant))
    return sorted(set(combos))


def _vt8_expand_ordered(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    pools: List[List[str]] = []
    for digit in triad:
        pools.append(sorted({digit, _mirror_digit(digit)}))
    out: List[str] = []
    for a in pools[0]:
        for b in pools[1]:
            for c in pools[2]:
                out.append(a + b + c)
    return sorted(set(out))


def _is_double(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 2


def _double_pack_mirror_single_6(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    if not _is_double(triad):
        return _r_perm_4(triad)
    digits = list(triad)
    counts = {digit: digits.count(digit) for digit in set(digits)}
    repeated = next(digit for digit, count in counts.items() if count == 2)
    single = next(digit for digit, count in counts.items() if count == 1)
    mirrored_single = _mirror_digit(single)
    return sorted(set(_unique_perms(triad) + _unique_perms(repeated + repeated + mirrored_single)))


def _double_pack_mirror_double_6(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    if not _is_double(triad):
        return _r_perm_4(triad)
    digits = list(triad)
    counts = {digit: digits.count(digit) for digit in set(digits)}
    repeated = next(digit for digit, count in counts.items() if count == 2)
    single = next(digit for digit, count in counts.items() if count == 1)
    mirrored_repeated = _mirror_digit(repeated)
    return sorted(set(_unique_perms(triad) + _unique_perms(mirrored_repeated + mirrored_repeated + single)))


def _collapse_order_seed(value: object) -> str:
    digits = _digits_only(value)
    if len(digits) == 3:
        return digits
    if len(digits) > 3 and len(set(digits)) == 2:
        return digits[:3]
    seen: List[str] = []
    for ch in digits:
        if ch not in seen:
            seen.append(ch)
        if len(seen) == 3:
            return "".join(seen)
    return ""


@lru_cache(maxsize=8192)
def _family_for_fragment(canonical: str) -> Optional[int]:
    if not canonical:
        return None
    return derive_vtrac_index_for_canonical(canonical, get_vtrac_index)


def _parse_source_literals_blob(value: object) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for chunk in str(value or "").split(";"):
        part = chunk.strip()
        if not part:
            continue
        if "=" in part:
            row_type, literal = part.split("=", 1)
        else:
            row_type, literal = "", part
        row_type = row_type.strip()
        literal = literal.strip()
        digits = _digits_only(literal)
        out.append(
            {
                "row_type": row_type,
                "literal": literal,
                "digits": digits,
                "digit_count": len(digits),
                "unique_digit_count": len(set(digits)),
                "hot_level": _hot_level_for_literal(literal),
            }
        )
    out.sort(key=lambda item: _rowtype_sort_key(str(item.get("row_type") or "")))
    return out


def _load_source_table_lookup(state_dir: Path, state_key: str) -> Dict[Tuple[str, str, str, str, str], str]:
    tables_dir = state_dir / "tables"
    if not tables_dir.exists():
        return {}
    candidates = {
        "Combined": [tables_dir / f"{state_key}_Combined_Combined.csv", tables_dir / "Combined_Combined.csv"],
        "Midday": [tables_dir / f"{state_key}_Midday_Combined.csv", tables_dir / "Midday_Combined.csv"],
        "Evening": [tables_dir / f"{state_key}_Evening_Combined.csv", tables_dir / "Evening_Combined.csv"],
    }
    lookup: Dict[Tuple[str, str, str, str, str], str] = {}
    for section, paths in candidates.items():
        table_path = next((path for path in paths if path.exists()), None)
        if table_path is None:
            continue
        for row in _load_csv_rows(table_path):
            set_name = str(row.get("Set") or "").strip()
            draw = str(row.get("Draw") or "").strip()
            row_type = str(row.get("RowType") or "").strip()
            for column in TABLE_COLS:
                literal = str(row.get(column) or "")
                if literal == "":
                    continue
                lookup[(section, set_name, draw, row_type, column)] = literal
    return lookup


def _source_cells_for_row(
    row: Dict[str, str],
    *,
    source_lookup: Dict[Tuple[str, str, str, str, str], str],
) -> List[Dict[str, Any]]:
    parsed = _parse_source_literals_blob(row.get("source_literals"))
    if parsed:
        return parsed
    section = str(row.get("section") or "Unknown").strip() or "Unknown"
    set_name = str(row.get("Set") or "").strip()
    draw = str(row.get("Draw") or "").strip()
    column = str(row.get("Column") or "").strip()
    row_types = [tok for tok in str(row.get("rows") or "").split(",") if tok]
    out: List[Dict[str, Any]] = []
    for row_type in sorted(row_types, key=_rowtype_sort_key):
        literal = source_lookup.get((section, set_name, draw, row_type, column))
        if literal is None:
            continue
        digits = _digits_only(literal)
        out.append(
            {
                "row_type": row_type,
                "literal": literal,
                "digits": digits,
                "digit_count": len(digits),
                "unique_digit_count": len(set(digits)),
                "hot_level": _hot_level_for_literal(literal),
            }
        )
    return out


def _build_hidden_family_reveal(
    *,
    canonical: str,
    family_id: Optional[int],
    modal_order: str,
    column: str,
    source_cells: Sequence[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    if family_id is None or family_id <= 0 or not source_cells:
        return None

    all_digit_anchors: Counter[str] = Counter()
    all_value_anchors: Counter[str] = Counter()
    fragment_rollups: Dict[Tuple[str, str], Dict[str, Any]] = {}
    source_examples: List[Dict[str, Any]] = []

    for source in source_cells:
        row_type = str(source.get("row_type") or "")
        literal = str(source.get("literal") or "")
        digits = str(source.get("digits") or "")
        if len(digits) < 3:
            continue
        digit_counts = Counter(digits)
        value_counts = Counter(str(value) for value in _vtrac_values(digits))
        for digit, count in digit_counts.items():
            if count >= 2:
                all_digit_anchors[digit] += count
        for value, count in value_counts.items():
            if count >= 2:
                all_value_anchors[value] += count

        source_examples.append(
            {
                "row_type": row_type,
                "literal": literal,
                "digits": digits,
                "digit_count": len(digits),
                "hot_level": int(source.get("hot_level") or 0),
            }
        )

        seen_fragments: set[Tuple[str, int, int, int]] = set()
        max_window_end = len(digits)
        for start in range(len(digits)):
            for end in range(start + 3, min(max_window_end, start + 6) + 1):
                window = digits[start:end]
                drop_plans: List[Tuple[int, Tuple[int, ...]]] = [(0, tuple())]
                for drop_count in (1, 2):
                    if len(window) - drop_count < 3:
                        continue
                    for removed in combinations(range(len(window)), drop_count):
                        drop_plans.append((drop_count, removed))
                for drop_count, removed in drop_plans:
                    fragment = "".join(ch for idx, ch in enumerate(window) if idx not in removed)
                    if len(fragment) < 3 or not _is_three_value_like(fragment):
                        continue
                    # Hidden-family evidence should come from an actual long-literal reveal
                    # or reduction, not from a plain same-length order variant.
                    if drop_count == 0 and len(digits) == len(fragment):
                        continue
                    dedupe_key = (fragment, start, end, drop_count)
                    if dedupe_key in seen_fragments:
                        continue
                    seen_fragments.add(dedupe_key)
                    family_match = _family_for_fragment(_canonical(fragment))
                    if family_match != family_id:
                        continue
                    clutter_gap = max(0, len(digits) - len(fragment))
                    if drop_count == 0 and clutter_gap == 0 and fragment == canonical:
                        continue
                    is_exact_modal = bool(modal_order) and fragment == modal_order
                    is_modal_subsequence = bool(modal_order) and not is_exact_modal and _is_subsequence(fragment, modal_order)
                    digit_anchor_strength = sum(max(0, count - 1) for count in Counter(fragment).values())
                    value_anchor_strength = sum(max(0, count - 1) for count in Counter(str(v) for v in _vtrac_values(fragment)).values())
                    support_signal_count = 0
                    if drop_count > 0:
                        support_signal_count += 1
                    if len(fragment) > 3:
                        support_signal_count += 1
                    if digit_anchor_strength > 0 or value_anchor_strength > 0:
                        support_signal_count += 1
                    if is_exact_modal or is_modal_subsequence:
                        support_signal_count += 1
                    if support_signal_count == 0:
                        continue
                    fragment_score = (
                        float(len(fragment))
                        + float(digit_anchor_strength)
                        + float(value_anchor_strength)
                        + (2.0 if is_exact_modal else 1.0 if is_modal_subsequence else 0.0)
                        + (1.0 if drop_count == 0 else 0.0)
                        + (1.0 if clutter_gap > 0 else 0.0)
                    )
                    roll_key = (fragment, row_type)
                    roll = fragment_rollups.setdefault(
                        roll_key,
                        {
                            "fragment": fragment,
                            "row_type": row_type,
                            "count": 0,
                            "best_score": 0.0,
                            "best_literal": literal,
                            "best_window": window,
                            "best_start": start,
                            "best_end": end,
                            "drop_count": drop_count,
                            "contiguous_hits": 0,
                            "reduced_hits": 0,
                            "modal_exact_hits": 0,
                            "modal_subsequence_hits": 0,
                            "digit_anchor_strength": 0,
                            "value_anchor_strength": 0,
                            "clutter_gap_max": 0,
                        },
                    )
                    roll["count"] += 1
                    roll["best_score"] = max(float(roll["best_score"]), fragment_score)
                    if fragment_score >= float(roll["best_score"]):
                        roll["best_literal"] = literal
                        roll["best_window"] = window
                        roll["best_start"] = start
                        roll["best_end"] = end
                        roll["drop_count"] = drop_count
                    if drop_count == 0:
                        roll["contiguous_hits"] += 1
                    else:
                        roll["reduced_hits"] += 1
                    if is_exact_modal:
                        roll["modal_exact_hits"] += 1
                    if is_modal_subsequence:
                        roll["modal_subsequence_hits"] += 1
                    roll["digit_anchor_strength"] += digit_anchor_strength
                    roll["value_anchor_strength"] += value_anchor_strength
                    roll["clutter_gap_max"] = max(int(roll["clutter_gap_max"]), clutter_gap)

    top_fragments = sorted(
        fragment_rollups.values(),
        key=lambda item: (
            -float(item["best_score"]),
            -int(item["count"]),
            -int(len(str(item["fragment"]))),
            str(item["fragment"]),
        ),
    )[:8]
    if not top_fragments:
        return None

    contiguous_hits = sum(int(item["contiguous_hits"]) for item in top_fragments)
    reduced_hits = sum(int(item["reduced_hits"]) for item in top_fragments)
    modal_exact_hits = sum(int(item["modal_exact_hits"]) for item in top_fragments)
    modal_subsequence_hits = sum(int(item["modal_subsequence_hits"]) for item in top_fragments)
    digit_anchor_strength = sum(max(0, count - 1) for count in all_digit_anchors.values())
    value_anchor_strength = sum(max(0, count - 1) for count in all_value_anchors.values())
    frontier_bonus = 1.0 if str(column) in {"1", "2"} else 0.0
    reveal_score = round(
        float(len(top_fragments))
        + float(contiguous_hits)
        + (0.5 * float(reduced_hits))
        + float(modal_exact_hits * 2 + modal_subsequence_hits)
        + float(digit_anchor_strength)
        + float(value_anchor_strength)
        + frontier_bonus,
        3,
    )

    explanation_tags: List[str] = ["hidden_family"]
    if contiguous_hits:
        explanation_tags.append("contiguous_family_fragment")
    if reduced_hits:
        explanation_tags.append("reduced_family_fragment")
    if modal_exact_hits:
        explanation_tags.append("modal_order_exact")
    elif modal_subsequence_hits:
        explanation_tags.append("modal_order_subsequence")
    if digit_anchor_strength:
        explanation_tags.append("digit_anchor")
    if value_anchor_strength:
        explanation_tags.append("value_anchor")
    if frontier_bonus:
        explanation_tags.append("frontier_source")

    return {
        "target_family_id": int(family_id),
        "row_canonical": canonical,
        "modal_order": modal_order,
        "source_cell_count": len(source_examples),
        "source_examples": source_examples[:4],
        "top_fragments": [
            {
                "fragment": str(item["fragment"]),
                "row_type": str(item["row_type"]),
                "count": int(item["count"]),
                "best_score": round(float(item["best_score"]), 3),
                "best_literal": str(item["best_literal"]),
                "best_window": str(item["best_window"]),
                "best_start": int(item["best_start"]),
                "best_end": int(item["best_end"]),
                "drop_count": int(item["drop_count"]),
                "contiguous_hits": int(item["contiguous_hits"]),
                "reduced_hits": int(item["reduced_hits"]),
                "modal_exact_hits": int(item["modal_exact_hits"]),
                "modal_subsequence_hits": int(item["modal_subsequence_hits"]),
                "digit_anchor_strength": int(item["digit_anchor_strength"]),
                "value_anchor_strength": int(item["value_anchor_strength"]),
                "clutter_gap_max": int(item["clutter_gap_max"]),
            }
            for item in top_fragments
        ],
        "digit_anchors": _counter_top(all_digit_anchors, top_n=6),
        "value_anchors": _counter_top(all_value_anchors, top_n=6),
        "reveal_score_components": {
            "fragment_count": int(len(top_fragments)),
            "contiguous_hits": int(contiguous_hits),
            "reduced_hits": int(reduced_hits),
            "modal_exact_hits": int(modal_exact_hits),
            "modal_subsequence_hits": int(modal_subsequence_hits),
            "digit_anchor_strength": int(digit_anchor_strength),
            "value_anchor_strength": int(value_anchor_strength),
            "frontier_bonus": float(frontier_bonus),
        },
        "reveal_score": reveal_score,
        "explanation_tags": explanation_tags,
    }


def _build_transform_candidates(seed: str) -> List[Dict[str, Any]]:
    candidates: List[Dict[str, Any]] = []
    direct = _unique_perms(seed)
    if direct:
        candidates.append(
            {
                "method_id": "direct_perms",
                "play_mode": "STRAIGHT",
                "cost_units": len(direct),
                "combos_count": len(direct),
                "combos": direct,
            }
        )

    if len(set(seed)) == 3:
        vt8 = _vt8_expand_ordered(seed)
        if vt8:
            candidates.append(
                {
                    "method_id": "vt8_expand_ordered",
                    "play_mode": "STRAIGHT",
                    "cost_units": len(vt8),
                    "combos_count": len(vt8),
                    "combos": vt8,
                }
            )
        mirror_12 = _method1_pair_mirror_12(seed)
        if mirror_12:
            candidates.append(
                {
                    "method_id": "pair_mirror_third_12",
                    "play_mode": "STRAIGHT",
                    "cost_units": len(mirror_12),
                    "combos_count": len(mirror_12),
                    "combos": mirror_12,
                }
            )
    elif _is_double(seed):
        single_6 = _double_pack_mirror_single_6(seed)
        if single_6:
            candidates.append(
                {
                    "method_id": "double_mirror_single_6",
                    "play_mode": "STRAIGHT",
                    "cost_units": len(single_6),
                    "combos_count": len(single_6),
                    "combos": single_6,
                }
            )
        double_6 = _double_pack_mirror_double_6(seed)
        if double_6:
            candidates.append(
                {
                    "method_id": "double_mirror_double_6",
                    "play_mode": "STRAIGHT",
                    "cost_units": len(double_6),
                    "combos_count": len(double_6),
                    "combos": double_6,
                }
            )

    method_rank = {
        "direct_perms": 0,
        "double_mirror_single_6": 1,
        "double_mirror_double_6": 2,
        "vt8_expand_ordered": 3,
        "pair_mirror_third_12": 4,
    }
    candidates.sort(key=lambda item: (int(item["cost_units"]), method_rank.get(str(item["method_id"]), 99)))
    return candidates


def _build_order_transform_hints(
    *,
    canonical: str,
    family_id: Optional[int],
    modal_order: str,
    modal_rows: int,
    hidden_family_reveal: Optional[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    if family_id is None or family_id <= 0:
        return None

    by_seed: Dict[str, Dict[str, Any]] = {}

    def add_seed_support(
        *,
        raw_value: str,
        source_type: str,
        support_count: int,
        modal_hits: int,
        digit_anchor_strength: int,
        value_anchor_strength: int,
        example_literal: str,
        row_type: str,
    ) -> None:
        seed = _collapse_order_seed(raw_value)
        if not seed:
            return
        seed_family = get_vtrac_index(seed)
        if seed_family != family_id:
            return
        support_score = (
            float(max(1, support_count))
            + float(max(0, len(_digits_only(raw_value)) - 3))
            + float(max(0, modal_hits))
            + float(max(0, digit_anchor_strength))
            + float(max(0, value_anchor_strength))
            + (1.5 if source_type == "modal_order" else 0.0)
        )
        entry = by_seed.setdefault(
            seed,
            {
                "seed": seed,
                "family_id": int(family_id),
                "support_score": 0.0,
                "support_count": 0,
                "source_types": Counter(),
                "raw_fragments": Counter(),
                "pair_anchor_strength": 0,
                "value_anchor_strength": 0,
                "modal_hits": 0,
                "example_rows": [],
            },
        )
        entry["support_score"] += support_score
        entry["support_count"] += max(1, support_count)
        entry["source_types"][source_type] += max(1, support_count)
        raw_digits = _digits_only(raw_value)
        if raw_digits:
            entry["raw_fragments"][raw_digits] += max(1, support_count)
        entry["pair_anchor_strength"] += max(0, digit_anchor_strength)
        entry["value_anchor_strength"] += max(0, value_anchor_strength)
        entry["modal_hits"] += max(0, modal_hits)
        entry["example_rows"].append(
            {
                "source_type": source_type,
                "raw_value": raw_digits,
                "example_literal": example_literal,
                "row_type": row_type,
                "support_count": max(1, support_count),
            }
        )

    if modal_order:
        add_seed_support(
            raw_value=modal_order,
            source_type="modal_order",
            support_count=max(1, modal_rows),
            modal_hits=max(1, modal_rows),
            digit_anchor_strength=sum(max(0, count - 1) for count in Counter(_digits_only(modal_order)).values()),
            value_anchor_strength=sum(
                max(0, count - 1) for count in Counter(str(v) for v in _vtrac_values(modal_order)).values()
            ),
            example_literal=modal_order,
            row_type="modal",
        )

    if isinstance(hidden_family_reveal, dict):
        for fragment in hidden_family_reveal.get("top_fragments") or []:
            add_seed_support(
                raw_value=str(fragment.get("fragment") or ""),
                source_type="hidden_fragment",
                support_count=_to_int(fragment.get("count"), default=1),
                modal_hits=_to_int(fragment.get("modal_exact_hits"), default=0)
                + _to_int(fragment.get("modal_subsequence_hits"), default=0),
                digit_anchor_strength=_to_int(fragment.get("digit_anchor_strength"), default=0),
                value_anchor_strength=_to_int(fragment.get("value_anchor_strength"), default=0),
                example_literal=str(fragment.get("best_literal") or ""),
                row_type=str(fragment.get("row_type") or ""),
            )

    if not by_seed:
        return None

    ranked_seeds: List[Dict[str, Any]] = []
    method_inventory: Counter[str] = Counter()
    top_transforms: List[Dict[str, Any]] = []
    for seed_entry in sorted(
        by_seed.values(),
        key=lambda item: (-float(item["support_score"]), -int(item["support_count"]), item["seed"]),
    )[:6]:
        seed = str(seed_entry["seed"])
        transforms = _build_transform_candidates(seed)
        for transform in transforms:
            method_inventory[str(transform["method_id"])] += 1
            top_transforms.append(
                {
                    "seed": seed,
                    "family_id": int(family_id),
                    "support_score": round(float(seed_entry["support_score"]), 3),
                    "support_count": int(seed_entry["support_count"]),
                    "pair_anchor_strength": int(seed_entry["pair_anchor_strength"]),
                    "value_anchor_strength": int(seed_entry["value_anchor_strength"]),
                    "source_types": _counter_top(seed_entry["source_types"], top_n=4),
                    "method_id": str(transform["method_id"]),
                    "play_mode": str(transform["play_mode"]),
                    "cost_units": int(transform["cost_units"]),
                    "combos_count": int(transform["combos_count"]),
                    "combos": list(transform["combos"]),
                }
            )
        ranked_seeds.append(
            {
                "seed": seed,
                "family_id": int(family_id),
                "support_score": round(float(seed_entry["support_score"]), 3),
                "support_count": int(seed_entry["support_count"]),
                "pair_anchor_strength": int(seed_entry["pair_anchor_strength"]),
                "value_anchor_strength": int(seed_entry["value_anchor_strength"]),
                "modal_hits": int(seed_entry["modal_hits"]),
                "source_types": _counter_top(seed_entry["source_types"], top_n=4),
                "raw_fragments": _counter_top(seed_entry["raw_fragments"], top_n=6),
                "method_ids": [item["method_id"] for item in transforms],
                "example_rows": sorted(
                    seed_entry["example_rows"],
                    key=lambda item: (-int(item["support_count"]), item["source_type"], item["raw_value"]),
                )[:3],
            }
        )

    top_transforms.sort(
        key=lambda item: (
            -float(item["support_score"]),
            int(item["cost_units"]),
            str(item["method_id"]),
            str(item["seed"]),
        )
    )

    return {
        "target_family_id": int(family_id),
        "row_canonical": canonical,
        "top_seeds": ranked_seeds[:6],
        "top_transforms": top_transforms[:8],
        "method_inventory": _counter_top(method_inventory, top_n=6),
        "support_score_total": round(sum(float(item["support_score"]) for item in ranked_seeds), 3),
        "support_score_max": round(max(float(item["support_score"]) for item in ranked_seeds), 3),
    }


def _top_transform_examples(items: Sequence[Dict[str, Any]], top_n: int = 4) -> List[Dict[str, Any]]:
    ordered = sorted(
        items,
        key=lambda item: (
            -float(item.get("support_score", 0.0)),
            _to_int(item.get("cost_units")),
            str(item.get("method_id") or ""),
            str(item.get("seed") or ""),
        ),
    )
    out: List[Dict[str, Any]] = []
    seen_methods: set[str] = set()
    for item in ordered:
        method_id = str(item.get("method_id") or "")
        if not method_id or method_id in seen_methods:
            continue
        out.append(item)
        seen_methods.add(method_id)
        if len(out) >= top_n:
            return out
    for item in ordered:
        if item in out:
            continue
        out.append(item)
        if len(out) >= top_n:
            break
    return out


def _enrich_score_rows(
    rows: Sequence[Dict[str, str]],
    *,
    source_lookup: Dict[Tuple[str, str, str, str, str], str],
) -> List[Dict[str, Any]]:
    enriched: List[Dict[str, Any]] = []
    for row in rows:
        item: Dict[str, Any] = dict(row)
        source_cells = _source_cells_for_row(item, source_lookup=source_lookup)
        item["__source_cells"] = source_cells
        item["__hidden_family_reveal"] = _build_hidden_family_reveal(
            canonical=_digits_only(item.get("Canonical")),
            family_id=_to_int(item.get("family_id"), default=0) or None,
            modal_order=str(item.get("orders_modal_value") or ""),
            column=str(item.get("Column") or ""),
            source_cells=source_cells,
        )
        item["__order_transform_hints"] = _build_order_transform_hints(
            canonical=_digits_only(item.get("Canonical")),
            family_id=_to_int(item.get("family_id"), default=0) or None,
            modal_order=str(item.get("orders_modal_value") or ""),
            modal_rows=_to_int(item.get("orders_modal_rows"), default=1),
            hidden_family_reveal=item.get("__hidden_family_reveal"),
        )
        enriched.append(item)
    return enriched

def _row_locator(row: Dict[str, str]) -> str:
    section = str(row.get("section") or "Unknown").strip() or "Unknown"
    set_name = str(row.get("Set") or "?").strip() or "?"
    draw = str(row.get("Draw") or "?").strip() or "?"
    column = str(row.get("Column") or "?").strip() or "?"
    rows = str(row.get("rows") or "-").strip() or "-"
    return f"{section}:{set_name}:{draw}:Col{column}:{rows}"


def _box_label(set_name: str, draw: str, column: str) -> str:
    return f"{set_name}/{draw}/Col{column}"


def _row_payload(row: Dict[str, str]) -> Dict[str, Any]:
    canonical = _digits_only(row.get("Canonical"))
    return {
        "locator": _row_locator(row),
        "section": str(row.get("section") or ""),
        "set": str(row.get("Set") or ""),
        "draw": str(row.get("Draw") or ""),
        "column": str(row.get("Column") or ""),
        "rows": [tok for tok in str(row.get("rows") or "").split(",") if tok],
        "canonical": canonical,
        "canonical_length": len(canonical),
        "unique_digit_count": len(set(canonical)),
        "long_canonical": len(canonical) > 3,
        "type": str(row.get("type") or ""),
        "family_id": _to_int(row.get("family_id"), default=0) or None,
        "score": _to_float(row.get("score")),
        "why": str(row.get("why") or ""),
        "why_tags": _split_why(row.get("why")),
        "hot_level": _to_int(row.get("hot")),
        "score_breakdown": {key: _to_float(row.get(key)) for key in ROW_SCORE_PART_COLUMNS},
        "flags": {key: _to_bool(row.get(key)) for key in ROW_FLAG_COLUMNS},
        "counts": {key: _to_float(row.get(key)) for key in ROW_COUNT_COLUMNS},
        "modal_order": {
            "value": str(row.get("orders_modal_value") or ""),
            "rows": _to_int(row.get("orders_modal_rows")),
        },
        "source_cells": list(row.get("__source_cells") or []),
        "hidden_family_reveal": row.get("__hidden_family_reveal"),
        "order_transform_hints": row.get("__order_transform_hints"),
    }


def _pick3_canonical_from_row(row: Dict[str, Any]) -> str:
    modal_order = _normalize_pick3_literal(row.get("orders_modal_value"))
    if modal_order:
        return _canonical(modal_order)
    return _canonical(_normalize_pick3_literal(row.get("Canonical")))


def _compound_payload(row: Dict[str, str]) -> Dict[str, Any]:
    canonical = _digits_only(row.get("Canonical"))
    return {
        "canonical": canonical,
        "canonical_length": len(canonical),
        "unique_digit_count": len(set(canonical)),
        "long_canonical": len(canonical) > 3,
        "family_id": _to_int(row.get("family_id"), default=0) or None,
        "compound_score": _to_float(row.get("compound_score")),
        "base_max_score": _to_float(row.get("base_max_score")),
        "set_chain_depth": _to_int(row.get("set_chain_depth")),
        "draw_chain_depth": _to_int(row.get("draw_chain_depth")),
        "rows_covered": _to_int(row.get("rows_covered")),
        "funnel_precol1": _to_bool(row.get("funnel_precol1")),
        "vt_only_lane": _to_bool(row.get("vt_only_lane")),
        "hot1_count": _to_int(row.get("hot1_count")),
        "hot2_count": _to_int(row.get("hot2_count")),
        "col1_hits": _to_int(row.get("col1_hits")),
        "consensus_hits": _to_int(row.get("consensus_hits")),
        "hidden3v_hits": _to_int(row.get("hidden3v_hits")),
        "vtrac_straight_hits": _to_int(row.get("vtrac_straight_hits")),
        "double_mirror_hits": _to_int(row.get("double_mirror_hits")),
        "compound_why": str(row.get("compound_why") or ""),
        "compound_why_tags": _split_why(row.get("compound_why")),
        "examples": [tok for tok in str(row.get("examples") or "").split(";") if tok],
    }


def _family_box_payload(row: Dict[str, str]) -> Dict[str, Any]:
    return {
        "set": str(row.get("Set") or ""),
        "draw": str(row.get("Draw") or ""),
        "column": str(row.get("Column") or ""),
        "family_id": _to_int(row.get("family_id"), default=0) or None,
        "family_score": _to_float(row.get("family_score")),
        "best_compound_score": _to_float(row.get("best_compound_score")),
        "last_remaining_3v": _to_bool(row.get("last_remaining_3v")),
        "progression_flag": _to_bool(row.get("progression_flag")),
        "any_dom_last": _to_bool(row.get("any_dom_last")),
        "any_consensus": _to_bool(row.get("any_consensus")),
        "any_hidden3v": _to_bool(row.get("any_hidden3v")),
        "any_vtrac_straight": _to_bool(row.get("any_vtrac_straight")),
        "top_canonicals": _counter_top(_parse_counter_blob(row.get("top_canonicals")), top_n=6),
        "top_modal_orders": _counter_top(_parse_counter_blob(row.get("top_modal_orders")), top_n=6),
    }


def _build_compound_lookup(compound_rows: Sequence[Dict[str, str]]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    lookup: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for row in compound_rows:
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        canonical = _digits_only(row.get("Canonical"))
        if not canonical:
            continue
        payload = _compound_payload(row)
        key = (section, canonical)
        current = lookup.get(key)
        if current is None or float(payload.get("compound_score") or 0.0) > float(current.get("compound_score") or 0.0):
            lookup[key] = payload
    return lookup


def _build_pattern_ledgers(
    rows: Sequence[Dict[str, str]],
    compound_rows: Sequence[Dict[str, str]],
    top_n: int,
) -> Dict[str, List[Dict[str, Any]]]:
    compound_lookup = _build_compound_lookup(compound_rows)
    by_key: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for row in rows:
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        canonical = _digits_only(row.get("Canonical"))
        if not canonical:
            continue
        key = (section, canonical)
        entry = by_key.setdefault(
            key,
            {
                "section": section,
                "canonical": canonical,
                "row_hits": 0,
                "score_total": 0.0,
                "score_max": 0.0,
                "family_ids": Counter(),
                "sets": set(),
                "draws": set(),
                "columns": set(),
                "boxes": set(),
                "box_rollups": {},
                "why_tags": Counter(),
                "flags": Counter(),
                "hot_counts": Counter(),
                "modal_orders": Counter(),
                "part_sums": defaultdict(float),
                "part_max": defaultdict(float),
                "part_peaks": {},
                "frontier_columns": Counter(),
                "hidden_reveal_row_hits": 0,
                "hidden_reveal_score_total": 0.0,
                "hidden_reveal_score_max": 0.0,
                "hidden_fragments": Counter(),
                "hidden_digit_anchors": Counter(),
                "hidden_value_anchors": Counter(),
                "hidden_examples": [],
                "order_transform_row_hits": 0,
                "order_transform_support_total": 0.0,
                "order_transform_support_max": 0.0,
                "order_transform_seeds": Counter(),
                "order_transform_methods": Counter(),
                "order_transform_examples": [],
                "examples": [],
            },
        )
        score = _to_float(row.get("score"))
        set_name = str(row.get("Set") or "")
        draw = str(row.get("Draw") or "")
        column = str(row.get("Column") or "")
        column_int = _to_int(column, default=-1)
        locator = _row_locator(row)
        entry["row_hits"] += 1
        entry["score_total"] += score
        entry["score_max"] = max(float(entry["score_max"]), score)
        if row.get("family_id") not in (None, ""):
            entry["family_ids"][_to_int(row.get("family_id"))] += 1
        entry["sets"].add(set_name)
        entry["draws"].add(draw)
        entry["columns"].add(column)
        entry["boxes"].add((set_name, draw, column))
        box_key = (set_name, draw, column)
        box_roll = entry["box_rollups"].setdefault(
            box_key,
            {
                "set": set_name,
                "draw": draw,
                "column": column,
                "row_hits": 0,
                "score_total": 0.0,
                "score_max": 0.0,
                "why_tags": Counter(),
                "locators": [],
            },
        )
        box_roll["row_hits"] += 1
        box_roll["score_total"] += score
        box_roll["score_max"] = max(float(box_roll["score_max"]), score)
        box_roll["why_tags"].update(_split_why(row.get("why")))
        box_roll["locators"].append({"locator": locator, "score": score})
        entry["why_tags"].update(_split_why(row.get("why")))
        entry["hot_counts"][_to_int(row.get("hot"))] += 1
        modal_order = str(row.get("orders_modal_value") or "").strip()
        if modal_order:
            entry["modal_orders"][modal_order] += max(1, _to_int(row.get("orders_modal_rows"), default=1))
        if column_int in {1, 2}:
            entry["frontier_columns"][f"col_{column_int}"] += 1
        hidden_reveal = row.get("__hidden_family_reveal")
        if isinstance(hidden_reveal, dict):
            entry["hidden_reveal_row_hits"] += 1
            reveal_score = _to_float(hidden_reveal.get("reveal_score"))
            entry["hidden_reveal_score_total"] += reveal_score
            entry["hidden_reveal_score_max"] = max(float(entry["hidden_reveal_score_max"]), reveal_score)
            for frag in hidden_reveal.get("top_fragments") or []:
                fragment = str(frag.get("fragment") or "").strip()
                if fragment:
                    entry["hidden_fragments"][fragment] += max(1, _to_int(frag.get("count"), default=1))
            for anchor in hidden_reveal.get("digit_anchors") or []:
                value = str(anchor.get("value") or "").strip()
                if value:
                    entry["hidden_digit_anchors"][value] += max(1, _to_int(anchor.get("count"), default=1))
            for anchor in hidden_reveal.get("value_anchors") or []:
                value = str(anchor.get("value") or "").strip()
                if value:
                    entry["hidden_value_anchors"][value] += max(1, _to_int(anchor.get("count"), default=1))
            source_example = (hidden_reveal.get("source_examples") or [{}])[0]
            top_fragment = (hidden_reveal.get("top_fragments") or [{}])[0]
            entry["hidden_examples"].append(
                {
                    "locator": locator,
                    "reveal_score": reveal_score,
                    "source_literal": str(source_example.get("literal") or ""),
                    "fragment": str(top_fragment.get("fragment") or ""),
                    "row_type": str(top_fragment.get("row_type") or source_example.get("row_type") or ""),
                }
            )
        order_transform = row.get("__order_transform_hints")
        if isinstance(order_transform, dict):
            entry["order_transform_row_hits"] += 1
            support_score = _to_float(order_transform.get("support_score_max"))
            entry["order_transform_support_total"] += _to_float(order_transform.get("support_score_total"))
            entry["order_transform_support_max"] = max(float(entry["order_transform_support_max"]), support_score)
            for seed in order_transform.get("top_seeds") or []:
                seed_value = str(seed.get("seed") or "").strip()
                if seed_value:
                    entry["order_transform_seeds"][seed_value] += max(1, _to_int(seed.get("support_count"), default=1))
            for method in order_transform.get("method_inventory") or []:
                method_id = str(method.get("value") or method.get("method_id") or "").strip()
                if method_id:
                    entry["order_transform_methods"][method_id] += max(1, _to_int(method.get("count"), default=1))
            for top_transform in (order_transform.get("top_transforms") or [])[:4]:
                entry["order_transform_examples"].append(
                    {
                        "locator": locator,
                        "seed": str(top_transform.get("seed") or ""),
                        "method_id": str(top_transform.get("method_id") or ""),
                        "cost_units": _to_int(top_transform.get("cost_units")),
                        "support_score": _to_float(top_transform.get("support_score")),
                        "combos": list(top_transform.get("combos") or [])[:8],
                    }
                )
        for flag in ROW_FLAG_COLUMNS:
            if _to_bool(row.get(flag)):
                entry["flags"][flag] += 1
        for part in ROW_SCORE_PART_COLUMNS:
            value = _to_float(row.get(part))
            entry["part_sums"][part] += value
            if value > float(entry["part_max"][part]):
                entry["part_max"][part] = value
            peak = entry["part_peaks"].get(part)
            if peak is None or value > float(peak["value"]):
                entry["part_peaks"][part] = {
                    "value": value,
                    "locator": locator,
                    "set": set_name,
                    "draw": draw,
                    "column": column,
                    "rows": [tok for tok in str(row.get("rows") or "").split(",") if tok],
                }
        entry["examples"].append(
            {
                "locator": locator,
                "score": score,
                "why": str(row.get("why") or ""),
            }
        )

    by_section: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for (_, canonical), entry in by_key.items():
        row_hits = int(entry["row_hits"])
        columns_present = sorted(entry["columns"], key=lambda value: (_to_int(value, default=999), value))
        top_box_contributions = []
        frontier_box_count = 0
        for box_key, box_roll in entry["box_rollups"].items():
            column = str(box_roll["column"])
            is_frontier = column in {"1", "2"}
            if is_frontier:
                frontier_box_count += 1
            top_box_contributions.append(
                {
                    "set": str(box_roll["set"]),
                    "draw": str(box_roll["draw"]),
                    "column": column,
                    "box_label": _box_label(str(box_roll["set"]), str(box_roll["draw"]), column),
                    "row_hits": int(box_roll["row_hits"]),
                    "score_total": round(float(box_roll["score_total"]), 3),
                    "score_max": round(float(box_roll["score_max"]), 3),
                    "frontier_box": is_frontier,
                    "top_why_tags": _counter_top(box_roll["why_tags"], top_n=4),
                    "example_locators": [
                        item["locator"]
                        for item in sorted(
                            box_roll["locators"],
                            key=lambda item: (-float(item["score"]), item["locator"]),
                        )[:3]
                    ],
                }
            )
        top_box_contributions.sort(
            key=lambda item: (
                -float(item["score_total"]),
                -float(item["score_max"]),
                -int(item["row_hits"]),
                item["box_label"],
            )
        )

        score_breakdown_peaks = {}
        for part in ROW_SCORE_PART_COLUMNS:
            peak = entry["part_peaks"].get(part)
            if peak is None:
                score_breakdown_peaks[part] = {
                    "value": 0.0,
                    "locator": "",
                    "set": "",
                    "draw": "",
                    "column": "",
                    "rows": [],
                }
            else:
                score_breakdown_peaks[part] = {
                    "value": round(float(peak["value"]), 3),
                    "locator": str(peak["locator"]),
                    "set": str(peak["set"]),
                    "draw": str(peak["draw"]),
                    "column": str(peak["column"]),
                    "rows": list(peak["rows"]),
                }

        compound_context = compound_lookup.get((entry["section"], canonical))
        if compound_context is not None:
            compound_context = dict(compound_context)
            compound_context["compound_lift_over_base_max"] = round(
                float(compound_context["compound_score"]) - float(compound_context["base_max_score"]),
                3,
            )

        payload = {
            "canonical": canonical,
            "canonical_length": len(canonical),
            "unique_digit_count": len(set(canonical)),
            "long_canonical": len(canonical) > 3,
            "row_hits": row_hits,
            "box_count": len(entry["boxes"]),
            "set_count": len(entry["sets"]),
            "draw_count": len(entry["draws"]),
            "column_count": len(entry["columns"]),
            "span": {
                "sets": sorted(entry["sets"]),
                "draws": sorted(entry["draws"]),
                "columns": columns_present,
            },
            "score_total": round(float(entry["score_total"]), 3),
            "score_max": round(float(entry["score_max"]), 3),
            "score_mean": round(float(entry["score_total"]) / row_hits, 3) if row_hits else 0.0,
            "dominant_family_id": None,
            "family_ids": [
                {"family_id": int(fid), "row_hits": int(cnt)}
                for fid, cnt in sorted(entry["family_ids"].items(), key=lambda kv: (-int(kv[1]), int(kv[0])))
            ],
            "top_why_tags": _counter_top(entry["why_tags"], top_n=8),
            "top_modal_orders": _counter_top(entry["modal_orders"], top_n=8),
            "flag_counts": {flag: int(entry["flags"].get(flag, 0)) for flag in ROW_FLAG_COLUMNS},
            "hot_counts": {
                f"hot_{level}": int(entry["hot_counts"].get(level, 0)) for level in sorted(entry["hot_counts"])
            },
            "frontier_summary": {
                "col1_row_hits": int(entry["frontier_columns"].get("col_1", 0)),
                "col2_row_hits": int(entry["frontier_columns"].get("col_2", 0)),
                "frontier_row_hits": int(entry["frontier_columns"].get("col_1", 0))
                + int(entry["frontier_columns"].get("col_2", 0)),
                "frontier_box_count": int(frontier_box_count),
            },
            "score_breakdown_sums": {
                key: round(float(entry["part_sums"][key]), 3) for key in ROW_SCORE_PART_COLUMNS
            },
            "score_breakdown_max": {
                key: round(float(entry["part_max"][key]), 3) for key in ROW_SCORE_PART_COLUMNS
            },
            "score_breakdown_peaks": score_breakdown_peaks,
            "top_box_contributions": top_box_contributions[:5],
            "compound_context": compound_context,
            "hidden_family_reveal_summary": {
                "row_hits": int(entry["hidden_reveal_row_hits"]),
                "reveal_score_total": round(float(entry["hidden_reveal_score_total"]), 3),
                "reveal_score_max": round(float(entry["hidden_reveal_score_max"]), 3),
                "top_fragments": _counter_top(entry["hidden_fragments"], top_n=6),
                "digit_anchors": _counter_top(entry["hidden_digit_anchors"], top_n=6),
                "value_anchors": _counter_top(entry["hidden_value_anchors"], top_n=6),
                "example_rows": sorted(
                    entry["hidden_examples"],
                    key=lambda item: (-float(item["reveal_score"]), item["locator"]),
                )[:3],
            },
            "order_transform_summary": {
                "row_hits": int(entry["order_transform_row_hits"]),
                "support_score_total": round(float(entry["order_transform_support_total"]), 3),
                "support_score_max": round(float(entry["order_transform_support_max"]), 3),
                "top_seeds": _counter_top(entry["order_transform_seeds"], top_n=6),
                "top_methods": _counter_top(entry["order_transform_methods"], top_n=6),
                "top_transforms": _top_transform_examples(entry["order_transform_examples"], top_n=4),
            },
            "example_rows": sorted(
                entry["examples"],
                key=lambda item: (-float(item["score"]), item["locator"]),
            )[:3],
        }
        if payload["family_ids"]:
            payload["dominant_family_id"] = int(payload["family_ids"][0]["family_id"])
        by_section[entry["section"]].append(payload)

    for section, items in by_section.items():
        items.sort(
            key=lambda item: (
                -float(item["score_total"]),
                -float(item["score_max"]),
                -int(item["row_hits"]),
                item["canonical"],
            )
        )
        by_section[section] = items[:top_n]
    return dict(by_section)


def _build_hidden_family_rollups(score_rows: Sequence[Dict[str, Any]]) -> Dict[Tuple[str, int], Dict[str, Any]]:
    rollups: Dict[Tuple[str, int], Dict[str, Any]] = {}
    for row in score_rows:
        family_id = _to_int(row.get("family_id"), default=0)
        if family_id <= 0:
            continue
        hidden_reveal = row.get("__hidden_family_reveal")
        if not isinstance(hidden_reveal, dict):
            continue
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        key = (section, family_id)
        entry = rollups.setdefault(
            key,
            {
                "row_hits": 0,
                "reveal_score_total": 0.0,
                "reveal_score_max": 0.0,
                "top_fragments": Counter(),
                "digit_anchors": Counter(),
                "value_anchors": Counter(),
                "examples": [],
            },
        )
        reveal_score = _to_float(hidden_reveal.get("reveal_score"))
        entry["row_hits"] += 1
        entry["reveal_score_total"] += reveal_score
        entry["reveal_score_max"] = max(float(entry["reveal_score_max"]), reveal_score)
        for frag in hidden_reveal.get("top_fragments") or []:
            fragment = str(frag.get("fragment") or "").strip()
            if fragment:
                entry["top_fragments"][fragment] += max(1, _to_int(frag.get("count"), default=1))
        for anchor in hidden_reveal.get("digit_anchors") or []:
            value = str(anchor.get("value") or "").strip()
            if value:
                entry["digit_anchors"][value] += max(1, _to_int(anchor.get("count"), default=1))
        for anchor in hidden_reveal.get("value_anchors") or []:
            value = str(anchor.get("value") or "").strip()
            if value:
                entry["value_anchors"][value] += max(1, _to_int(anchor.get("count"), default=1))
        source_example = (hidden_reveal.get("source_examples") or [{}])[0]
        top_fragment = (hidden_reveal.get("top_fragments") or [{}])[0]
        entry["examples"].append(
            {
                "locator": _row_locator(row),
                "canonical": _digits_only(row.get("Canonical")),
                "reveal_score": reveal_score,
                "source_literal": str(source_example.get("literal") or ""),
                "fragment": str(top_fragment.get("fragment") or ""),
            }
        )
    return rollups


def _build_order_transform_rollups(score_rows: Sequence[Dict[str, Any]]) -> Dict[Tuple[str, int], Dict[str, Any]]:
    rollups: Dict[Tuple[str, int], Dict[str, Any]] = {}
    for row in score_rows:
        family_id = _to_int(row.get("family_id"), default=0)
        if family_id <= 0:
            continue
        order_transform = row.get("__order_transform_hints")
        if not isinstance(order_transform, dict):
            continue
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        key = (section, family_id)
        entry = rollups.setdefault(
            key,
            {
                "row_hits": 0,
                "support_score_total": 0.0,
                "support_score_max": 0.0,
                "top_seeds": Counter(),
                "top_methods": Counter(),
                "examples": [],
            },
        )
        support_score = _to_float(order_transform.get("support_score_max"))
        entry["row_hits"] += 1
        entry["support_score_total"] += _to_float(order_transform.get("support_score_total"))
        entry["support_score_max"] = max(float(entry["support_score_max"]), support_score)
        for seed in order_transform.get("top_seeds") or []:
            seed_value = str(seed.get("seed") or "").strip()
            if seed_value:
                entry["top_seeds"][seed_value] += max(1, _to_int(seed.get("support_count"), default=1))
        for method in order_transform.get("method_inventory") or []:
            method_id = str(method.get("value") or method.get("method_id") or "").strip()
            if method_id:
                entry["top_methods"][method_id] += max(1, _to_int(method.get("count"), default=1))
        for top_transform in (order_transform.get("top_transforms") or [])[:4]:
            entry["examples"].append(
                {
                    "locator": _row_locator(row),
                    "canonical": _digits_only(row.get("Canonical")),
                    "seed": str(top_transform.get("seed") or ""),
                    "method_id": str(top_transform.get("method_id") or ""),
                    "cost_units": _to_int(top_transform.get("cost_units")),
                    "support_score": _to_float(top_transform.get("support_score")),
                    "combos": list(top_transform.get("combos") or [])[:8],
                }
            )
    return rollups


def _build_family_rollups(
    rows: Sequence[Dict[str, str]],
    *,
    top_n: int,
    hidden_family_rollups: Optional[Dict[Tuple[str, int], Dict[str, Any]]] = None,
    order_transform_rollups: Optional[Dict[Tuple[str, int], Dict[str, Any]]] = None,
) -> Dict[str, List[Dict[str, Any]]]:
    by_key: Dict[Tuple[str, int], Dict[str, Any]] = {}
    for row in rows:
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        family_id = _to_int(row.get("family_id"), default=0)
        if family_id <= 0:
            continue
        key = (section, family_id)
        entry = by_key.setdefault(
            key,
            {
                "section": section,
                "family_id": family_id,
                "box_rows": 0,
                "family_score_total": 0.0,
                "family_score_max": 0.0,
                "best_compound_score_max": 0.0,
                "sets": set(),
                "draws": set(),
                "columns": set(),
                "boxes": set(),
                "top_canonicals": Counter(),
                "top_modal_orders": Counter(),
                "flags": Counter(),
                "breakdown_sums": defaultdict(float),
                "examples": [],
            },
        )
        set_name = str(row.get("Set") or "")
        draw = str(row.get("Draw") or "")
        column = str(row.get("Column") or "")
        score = _to_float(row.get("family_score"))
        best_compound = _to_float(row.get("best_compound_score"))
        entry["box_rows"] += 1
        entry["family_score_total"] += score
        entry["family_score_max"] = max(float(entry["family_score_max"]), score)
        entry["best_compound_score_max"] = max(float(entry["best_compound_score_max"]), best_compound)
        entry["sets"].add(set_name)
        entry["draws"].add(draw)
        entry["columns"].add(column)
        entry["boxes"].add((set_name, draw, column))
        entry["top_canonicals"].update(_parse_counter_blob(row.get("top_canonicals")))
        entry["top_modal_orders"].update(_parse_counter_blob(row.get("top_modal_orders")))
        if _to_bool(row.get("last_remaining_3v")):
            entry["flags"]["last_remaining_3v"] += 1
        if _to_bool(row.get("progression_flag")):
            entry["flags"]["progression_flag"] += 1
        if _to_bool(row.get("any_dom_last")):
            entry["flags"]["any_dom_last"] += 1
        if _to_bool(row.get("any_consensus")):
            entry["flags"]["any_consensus"] += 1
        if _to_bool(row.get("any_hidden3v")):
            entry["flags"]["any_hidden3v"] += 1
        if _to_bool(row.get("any_vtrac_straight")):
            entry["flags"]["any_vtrac_straight"] += 1
        for part in FAMILY_BREAKDOWN_COLUMNS:
            entry["breakdown_sums"][part] += _to_float(row.get(part))
        entry["examples"].append(
            {
                "set": set_name,
                "draw": draw,
                "column": column,
                "family_score": score,
                "top_canonicals": _counter_top(_parse_counter_blob(row.get("top_canonicals")), top_n=4),
                "last_remaining_3v": _to_bool(row.get("last_remaining_3v")),
            }
        )

    by_section: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for (_, family_id), entry in by_key.items():
        hidden_summary_raw = (hidden_family_rollups or {}).get((entry["section"], int(family_id)), {})
        transform_summary_raw = (order_transform_rollups or {}).get((entry["section"], int(family_id)), {})
        payload = {
            "family_id": int(family_id),
            "box_rows": int(entry["box_rows"]),
            "box_count": len(entry["boxes"]),
            "set_count": len(entry["sets"]),
            "draw_count": len(entry["draws"]),
            "column_count": len(entry["columns"]),
            "family_score_total": round(float(entry["family_score_total"]), 3),
            "family_score_max": round(float(entry["family_score_max"]), 3),
            "best_compound_score_max": round(float(entry["best_compound_score_max"]), 3),
            "last_remaining_count": int(entry["flags"].get("last_remaining_3v", 0)),
            "progression_count": int(entry["flags"].get("progression_flag", 0)),
            "dom_last_count": int(entry["flags"].get("any_dom_last", 0)),
            "consensus_count": int(entry["flags"].get("any_consensus", 0)),
            "hidden3v_count": int(entry["flags"].get("any_hidden3v", 0)),
            "vtrac_straight_count": int(entry["flags"].get("any_vtrac_straight", 0)),
            "top_canonicals": _counter_top(entry["top_canonicals"], top_n=8),
            "top_modal_orders": _counter_top(entry["top_modal_orders"], top_n=8),
            "breakdown_sums": {
                part: round(float(entry["breakdown_sums"][part]), 3) for part in FAMILY_BREAKDOWN_COLUMNS
            },
            "example_boxes": sorted(
                entry["examples"],
                key=lambda item: (-float(item["family_score"]), item["set"], item["draw"], item["column"]),
            )[:3],
            "hidden_family_reveal_summary": {
                "row_hits": int(hidden_summary_raw.get("row_hits", 0)),
                "reveal_score_total": round(float(hidden_summary_raw.get("reveal_score_total", 0.0)), 3),
                "reveal_score_max": round(float(hidden_summary_raw.get("reveal_score_max", 0.0)), 3),
                "top_fragments": _counter_top(hidden_summary_raw.get("top_fragments", Counter()), top_n=6),
                "digit_anchors": _counter_top(hidden_summary_raw.get("digit_anchors", Counter()), top_n=6),
                "value_anchors": _counter_top(hidden_summary_raw.get("value_anchors", Counter()), top_n=6),
                "example_rows": sorted(
                    hidden_summary_raw.get("examples", []),
                    key=lambda item: (-float(item["reveal_score"]), item["locator"]),
                )[:3],
            },
            "order_transform_summary": {
                "row_hits": int(transform_summary_raw.get("row_hits", 0)),
                "support_score_total": round(float(transform_summary_raw.get("support_score_total", 0.0)), 3),
                "support_score_max": round(float(transform_summary_raw.get("support_score_max", 0.0)), 3),
                "top_seeds": _counter_top(transform_summary_raw.get("top_seeds", Counter()), top_n=6),
                "top_methods": _counter_top(transform_summary_raw.get("top_methods", Counter()), top_n=6),
                "top_transforms": _top_transform_examples(transform_summary_raw.get("examples", []), top_n=4),
            },
        }
        by_section[entry["section"]].append(payload)

    for section, items in by_section.items():
        items.sort(
            key=lambda item: (
                -float(item["family_score_total"]),
                -float(item["family_score_max"]),
                -int(item["last_remaining_count"]),
                int(item["family_id"]),
            )
        )
        by_section[section] = items[:top_n]
    return dict(by_section)


def _build_survivor_frontiers(
    rows: Sequence[Dict[str, str]],
    *,
    score_rows_by_box: Optional[Dict[Tuple[str, str, str, str], List[Dict[str, Any]]]] = None,
) -> Dict[str, List[Dict[str, Any]]]:
    by_group: Dict[Tuple[str, str, str], List[Tuple[int, Dict[str, str]]]] = defaultdict(list)
    for row in rows:
        rows_cov = _to_int(row.get("rows_cov"))
        column_int = _to_int(row.get("Column"), default=-1)
        if rows_cov < 3 or column_int < 0:
            continue
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        set_name = str(row.get("Set") or "")
        draw = str(row.get("Draw") or "")
        by_group[(section, set_name, draw)].append((column_int, row))

    by_section: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for (section, set_name, draw), bucket in by_group.items():
        frontier_column = max(col for col, _ in bucket)
        frontier_rows = [row for col, row in bucket if col == frontier_column]
        frontier_rows.sort(
            key=lambda row: (
                -_to_float(row.get("family_score")),
                -_to_bool(row.get("last_remaining_3v")),
                _to_int(row.get("family_id"), default=9999),
            )
        )
        family_ids = [_to_int(row.get("family_id"), default=0) for row in frontier_rows if _to_int(row.get("family_id"), default=0) > 0]
        score_summary = _build_survivor_pattern_summary(
            (score_rows_by_box or {}).get((section, set_name, draw, str(frontier_column)), [])
        )
        by_section[section].append(
            {
                "set": set_name,
                "draw": draw,
                "frontier_column": int(frontier_column),
                "stable_box_rows": len(bucket),
                "eligible_columns": sorted({int(col) for col, _ in bucket}),
                "progression_column_count": len({int(col) for col, _ in bucket}),
                "frontier_family_count": len(family_ids),
                "is_single_family": len(set(family_ids)) == 1 if family_ids else False,
                "family_ids": sorted(set(int(fid) for fid in family_ids)),
                "frontier_pattern_summary": score_summary,
                "entries": [_family_box_payload(row) for row in frontier_rows],
            }
        )

    for section, items in by_section.items():
        items.sort(key=lambda item: (item["set"], item["draw"], int(item["frontier_column"])))
    return dict(by_section)


def _group_score_rows_by_box(rows: Sequence[Dict[str, Any]]) -> Dict[Tuple[str, str, str, str], List[Dict[str, Any]]]:
    grouped: Dict[Tuple[str, str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (
            str(row.get("section") or "Unknown").strip() or "Unknown",
            str(row.get("Set") or "").strip() or "",
            str(row.get("Draw") or "").strip() or "",
            str(row.get("Column") or "").strip() or "",
        )
        grouped[key].append(row)
    return grouped


def _build_survivor_pattern_summary(rows: Sequence[Dict[str, Any]], *, top_n: int = 10) -> Dict[str, Any]:
    exact_counter: Counter[str] = Counter()
    three_value_counter: Counter[str] = Counter()
    hidden_terminal_counter: Counter[str] = Counter()
    vtrac_index_counter: Counter[str] = Counter()
    row_type_counter: Counter[str] = Counter()
    top_patterns: List[Dict[str, Any]] = []
    ordered = sorted(
        rows,
        key=lambda row: (
            -_to_float(row.get("score")),
            -len(_digits_only(row.get("Canonical"))),
            _digits_only(row.get("Canonical")),
            _row_locator(row),
        ),
    )
    for row in ordered:
        canonical = _digits_only(row.get("Canonical"))
        if not canonical:
            continue
        if len(canonical) == 3:
            exact_counter[canonical] += 1
            try:
                vtrac_index_counter[str(derive_vtrac_index_for_canonical(canonical, get_vtrac_index))] += 1
            except Exception:
                pass
        elif len(canonical) > 3:
            hidden_terminal_counter[canonical] += 1
        if _is_three_value_like(canonical):
            three_value_counter[canonical] += 1
        for row_type in [tok for tok in str(row.get("rows") or "").split(",") if tok]:
            row_type_counter[row_type] += 1
        if len(top_patterns) < top_n:
            top_patterns.append(
                {
                    "canonical": canonical,
                    "score": _to_float(row.get("score")),
                    "rows": [tok for tok in str(row.get("rows") or "").split(",") if tok],
                    "family_id": _to_int(row.get("family_id"), default=0) or None,
                    "why_tags": _split_why(row.get("why")),
                    "vtrac_index": _to_int(derive_vtrac_index_for_canonical(canonical, get_vtrac_index), default=0)
                    or None
                    if len(canonical) == 3
                    else None,
                }
            )
    return {
        "row_count": len(rows),
        "row_types": _counter_top(row_type_counter, top_n=6),
        "exact3digit_patterns_all": sorted(exact_counter.keys()),
        "exact3digit_patterns_top": _counter_top(exact_counter, top_n=top_n),
        "three_value_like_patterns_all": sorted(three_value_counter.keys()),
        "three_value_like_patterns_top": _counter_top(three_value_counter, top_n=top_n),
        "hidden_terminal_patterns_all": sorted(hidden_terminal_counter.keys()),
        "hidden_terminal_patterns_top": _counter_top(hidden_terminal_counter, top_n=top_n),
        "vtrac_indices_all": sorted(vtrac_index_counter.keys(), key=lambda value: int(value)),
        "vtrac_indices_top": _counter_top(vtrac_index_counter, top_n=8),
        "top_patterns": top_patterns,
    }


def _build_survivor_progressions(
    family_rows: Sequence[Dict[str, str]],
    *,
    score_rows_by_box: Dict[Tuple[str, str, str, str], List[Dict[str, Any]]],
) -> Dict[str, List[Dict[str, Any]]]:
    by_group: Dict[Tuple[str, str, str], List[Tuple[int, Dict[str, str]]]] = defaultdict(list)
    for row in family_rows:
        rows_cov = _to_int(row.get("rows_cov"))
        column_int = _to_int(row.get("Column"), default=-1)
        if rows_cov < 3 or column_int < 0:
            continue
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        set_name = str(row.get("Set") or "")
        draw = str(row.get("Draw") or "")
        by_group[(section, set_name, draw)].append((column_int, row))

    by_section: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for (section, set_name, draw), bucket in by_group.items():
        columns = sorted({col for col, _ in bucket})
        if not columns:
            continue
        frontier_column = max(columns)
        column_summaries: List[Dict[str, Any]] = []
        for column_int in columns:
            column_rows = [row for col, row in bucket if col == column_int]
            family_ids = [
                _to_int(row.get("family_id"), default=0)
                for row in column_rows
                if _to_int(row.get("family_id"), default=0) > 0
            ]
            top_counter: Counter[str] = Counter()
            for row in column_rows:
                for item in _parse_counter_blob(row.get("top_canonicals")).items():
                    top_counter[item[0]] += int(item[1])
            score_summary = _build_survivor_pattern_summary(
                score_rows_by_box.get((section, set_name, draw, str(column_int)), [])
            )
            column_summaries.append(
                {
                    "column": int(column_int),
                    "family_count": len(family_ids),
                    "family_ids": sorted(set(int(fid) for fid in family_ids)),
                    "is_single_family": len(set(family_ids)) == 1 if family_ids else False,
                    "last_remaining_count": sum(1 for row in column_rows if _to_bool(row.get("last_remaining_3v"))),
                    "progression_family_count": sum(1 for row in column_rows if _to_bool(row.get("progression_flag"))),
                    "any_vtrac_family_count": sum(1 for row in column_rows if _to_bool(row.get("any_vtrac_straight"))),
                    "any_consensus_family_count": sum(1 for row in column_rows if _to_bool(row.get("any_consensus"))),
                    "top_canonicals": _counter_top(top_counter, top_n=8),
                    "pattern_summary": score_summary,
                }
            )
        frontier_summary = next(item for item in column_summaries if item["column"] == frontier_column)
        by_section[section].append(
            {
                "set": set_name,
                "draw": draw,
                "eligible_columns": [int(value) for value in columns],
                "progression_column_count": len(columns),
                "frontier_column": int(frontier_column),
                "frontier_family_ids": list(frontier_summary["family_ids"]),
                "is_frontier_single_family": bool(frontier_summary["is_single_family"]),
                "has_last_remaining": bool(frontier_summary["last_remaining_count"] > 0),
                "column_summaries": column_summaries,
            }
        )
    for section, items in by_section.items():
        items.sort(key=lambda item: (item["set"], item["draw"], int(item["frontier_column"])))
    return dict(by_section)


def _build_r_consensus_context(
    rows: Sequence[Dict[str, Any]],
    *,
    source_lookup: Dict[Tuple[str, str, str, str, str], str],
) -> Dict[str, Any]:
    box_rows: Dict[Tuple[str, str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        column = str(row.get("Column") or "").strip()
        if column not in {"1", "2"}:
            continue
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        set_name = str(row.get("Set") or "").strip()
        draw = str(row.get("Draw") or "").strip()
        box_rows[(section, set_name, draw, column)].append(row)

    if not box_rows:
        return {
            "available": False,
            "event_count": 0,
            "trial_eligible": False,
            "signal_strength_class": "none",
            "section_summaries": {},
        }

    events: List[Dict[str, Any]] = []
    tail_counter: Counter[str] = Counter()
    support_canonical_counter: Counter[str] = Counter()
    support_vtrac_counter: Counter[str] = Counter()
    tail_sections: Dict[str, set[str]] = defaultdict(set)
    section_summaries: Dict[str, Dict[str, Any]] = {}

    for (section, set_name, draw, column), bucket in sorted(
        box_rows.items(),
        key=lambda item: (
            _section_sort_key(item[0][0]),
            str(item[0][1]),
            str(item[0][2]),
            _to_int(item[0][3], default=999),
        ),
    ):
        source_values = [
            source_lookup.get((section, set_name, draw, row_type, column), "")
            for row_type in R_CONSENSUS_ROW_TYPES
        ]
        tail_value, event_class = _common_suffix_class(source_values)

        cons_full = any(_to_bool(row.get("cons_full")) for row in bucket)
        cons_3v = any(_to_bool(row.get("cons_3v")) for row in bucket)
        cons_stub = any(_to_bool(row.get("cons_stub")) for row in bucket)
        if not tail_value and not any((cons_full, cons_3v, cons_stub)):
            continue

        if not tail_value:
            flagged_digits = [
                _digits_only(row.get("Canonical") or row.get("orders_modal_value"))
                for row in bucket
                if _to_bool(row.get("cons_full")) or _to_bool(row.get("cons_3v")) or _to_bool(row.get("cons_stub"))
            ]
            flagged_digits = [digits for digits in flagged_digits if digits]
            tail_value, event_class = _common_suffix_class(flagged_digits)
            if not tail_value and flagged_digits:
                flagged_digits.sort(key=lambda value: (len(value), value))
                shortest = flagged_digits[0]
                tail_value = shortest[-2:] if len(shortest) >= 2 else shortest[-1:]
                event_class = "two-digit" if len(tail_value) >= 2 else "single-digit"
        if not tail_value:
            continue

        ranked_rows = sorted(
            [row for row in bucket if str(row.get("type") or "") != "consensus_stub"],
            key=lambda row: (
                -_to_float(row.get("score")),
                -len(_digits_only(row.get("Canonical"))),
                str(row.get("Canonical") or ""),
            ),
        )
        support_canonicals: List[str] = []
        support_vtrac_indices: List[str] = []
        local_examples: List[Dict[str, Any]] = []
        for row in ranked_rows[:8]:
            canonical = _pick3_canonical_from_row(row)
            if canonical and canonical not in support_canonicals:
                support_canonicals.append(canonical)
            family_id = str(_to_int(row.get("family_id"), default=0) or "").strip()
            if family_id and family_id not in support_vtrac_indices:
                support_vtrac_indices.append(family_id)
            local_examples.append(
                {
                    "canonical": canonical or _digits_only(row.get("Canonical")),
                    "type": str(row.get("type") or ""),
                    "score": round(_to_float(row.get("score")), 3),
                    "family_id": _to_int(row.get("family_id"), default=0) or None,
                    "why_tags": _split_why(row.get("why"))[:4],
                }
            )

        signal_score = (
            (3 if cons_full else 0)
            + (2 if cons_3v else 0)
            + (1 if cons_stub else 0)
            + (2 if event_class == "two-digit" else 1)
            + (2 if column == "1" else 1)
            + min(3, len(support_canonicals))
        )
        events.append(
            {
                "section": section,
                "set": set_name,
                "draw": draw,
                "column": _to_int(column, default=0),
                "box_label": _box_label(set_name, draw, column),
                "tail_value": tail_value,
                "event_class": event_class,
                "cons_full": cons_full,
                "cons_3v": cons_3v,
                "cons_stub": cons_stub,
                "top_support_canonicals": support_canonicals[:6],
                "top_support_vtrac_indices": support_vtrac_indices[:6],
                "local_examples": local_examples[:4],
                "signal_score": int(signal_score),
            }
        )

        tail_counter[tail_value] += 1
        tail_sections[tail_value].add(section)
        for rank, canonical in enumerate(support_canonicals[:6], start=1):
            support_canonical_counter[canonical] += max(1, signal_score - (rank - 1))
        for rank, value in enumerate(support_vtrac_indices[:6], start=1):
            support_vtrac_counter[value] += max(1, signal_score - (rank - 1))

        summary = section_summaries.setdefault(
            section,
            {
                "event_count": 0,
                "col1_count": 0,
                "col2_count": 0,
                "single_digit_count": 0,
                "two_digit_count": 0,
                "cons_full_event_count": 0,
                "cons_3v_event_count": 0,
                "cons_stub_event_count": 0,
            },
        )
        summary["event_count"] += 1
        summary[f"col{column}_count"] += 1
        summary[f"{event_class.replace('-', '_')}_count"] += 1
        if cons_full:
            summary["cons_full_event_count"] += 1
        if cons_3v:
            summary["cons_3v_event_count"] += 1
        if cons_stub:
            summary["cons_stub_event_count"] += 1

    if not events:
        return {
            "available": False,
            "event_count": 0,
            "trial_eligible": False,
            "signal_strength_class": "none",
            "section_summaries": {},
        }

    section_counts = {section: summary["event_count"] for section, summary in section_summaries.items()}
    cross_variant_tail_values = sorted(tail for tail, sections in tail_sections.items() if len(sections) >= 2)
    event_count = len(events)
    two_digit_count = sum(1 for event in events if event["event_class"] == "two-digit")
    single_digit_count = sum(1 for event in events if event["event_class"] == "single-digit")
    col1_count = sum(1 for event in events if int(event["column"]) == 1)
    col2_count = sum(1 for event in events if int(event["column"]) == 2)
    cons_full_event_count = sum(1 for event in events if bool(event["cons_full"]))
    cons_3v_event_count = sum(1 for event in events if bool(event["cons_3v"]))
    cons_stub_event_count = sum(1 for event in events if bool(event["cons_stub"]))

    if (two_digit_count > 0 and cross_variant_tail_values) or cons_full_event_count >= 2 or event_count >= 4:
        signal_strength_class = "strong"
    elif two_digit_count > 0 or cross_variant_tail_values or event_count >= 2:
        signal_strength_class = "moderate"
    else:
        signal_strength_class = "light"
    trial_eligible = bool(
        event_count > 0
        and (
            signal_strength_class in {"moderate", "strong"}
            or (cons_full_event_count > 0 and col1_count > 0)
        )
    )

    events.sort(
        key=lambda item: (
            -int(item["signal_score"]),
            0 if str(item["section"]) == "Combined" else 1,
            str(item["section"]),
            str(item["set"]),
            str(item["draw"]),
            int(item["column"]),
            str(item["tail_value"]),
        )
    )

    return {
        "available": True,
        "event_count": int(event_count),
        "single_digit_count": int(single_digit_count),
        "two_digit_count": int(two_digit_count),
        "col1_count": int(col1_count),
        "col2_count": int(col2_count),
        "cons_full_event_count": int(cons_full_event_count),
        "cons_3v_event_count": int(cons_3v_event_count),
        "cons_stub_event_count": int(cons_stub_event_count),
        "section_counts": dict(sorted(section_counts.items(), key=lambda kv: _section_sort_key(kv[0]))),
        "section_summaries": {
            section: section_summaries[section]
            for section in sorted(section_summaries.keys(), key=_section_sort_key)
        },
        "cross_variant_tail_values": cross_variant_tail_values[:10],
        "top_tail_values": [value for value, _count in tail_counter.most_common(10)],
        "top_support_canonicals": [value for value, _count in support_canonical_counter.most_common(10)],
        "top_support_vtrac_indices": [value for value, _count in support_vtrac_counter.most_common(10)],
        "signal_strength_class": signal_strength_class,
        "trial_eligible": trial_eligible,
        "events_top": events[:12],
    }


def _build_metrics_summary(metrics: Dict[str, Any]) -> Dict[str, Any]:
    summary: Dict[str, Any] = {}
    for key in SAFE_METRICS_KEYS:
        if key in metrics:
            summary[key] = metrics[key]
    return summary


def build_stable_arena_payload(
    *,
    state_dir: Path,
    state_key: str,
    results_date: str,
    history_date: str,
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    contains_winners_artifacts: bool,
    repo_root: Path,
    top_rows: int = 25,
    top_pattern_ledgers: int = 25,
    top_compound: int = 25,
    top_families: int = 10,
) -> Optional[Dict[str, Any]]:
    stable_dir = state_dir / "stable" / state_key
    scores_path = stable_dir / f"{state_key}_stable_patterns_scores.csv"
    compound_path = stable_dir / f"{state_key}_stable_patterns_compound.csv"
    families_path = stable_dir / f"{state_key}_stable_patterns_families.csv"
    metrics_path = stable_dir / f"{state_key}_metrics.json"
    required = [scores_path, compound_path, families_path, metrics_path]
    if not all(path.exists() for path in required):
        return None

    score_rows = _load_csv_rows(scores_path)
    compound_rows = _load_csv_rows(compound_path)
    family_rows = _load_csv_rows(families_path)
    if not score_rows and not compound_rows and not family_rows:
        return None
    metrics = _read_json(metrics_path)
    source_lookup = _load_source_table_lookup(state_dir, state_key)
    enriched_score_rows = _enrich_score_rows(score_rows, source_lookup=source_lookup)
    score_rows_by_box = _group_score_rows_by_box(enriched_score_rows)

    top_rows_by_section: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in enriched_score_rows:
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        top_rows_by_section[section].append(_row_payload(row))
    for section, items in top_rows_by_section.items():
        items.sort(
            key=lambda item: (
                -float(item["score"]),
                -int(item["canonical_length"]),
                item["canonical"],
                item["locator"],
            )
        )
        top_rows_by_section[section] = items[:top_rows]

    compound_by_section: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in compound_rows:
        section = str(row.get("section") or "Unknown").strip() or "Unknown"
        compound_by_section[section].append(_compound_payload(row))
    for section, items in compound_by_section.items():
        items.sort(
            key=lambda item: (
                -float(item["compound_score"]),
                -float(item["base_max_score"]),
                item["canonical"],
            )
        )
        compound_by_section[section] = items[:top_compound]

    pattern_ledgers = _build_pattern_ledgers(enriched_score_rows, compound_rows, top_n=top_pattern_ledgers)
    hidden_family_rollups = _build_hidden_family_rollups(enriched_score_rows)
    order_transform_rollups = _build_order_transform_rollups(enriched_score_rows)
    family_rollups = _build_family_rollups(
        family_rows,
        top_n=top_families,
        hidden_family_rollups=hidden_family_rollups,
        order_transform_rollups=order_transform_rollups,
    )
    survivor_frontiers = _build_survivor_frontiers(family_rows, score_rows_by_box=score_rows_by_box)
    survivor_progressions = _build_survivor_progressions(
        family_rows,
        score_rows_by_box=score_rows_by_box,
    )
    r_consensus_context = _build_r_consensus_context(enriched_score_rows, source_lookup=source_lookup)

    all_sections = sorted(
        {
            *(str(row.get("section") or "Unknown").strip() or "Unknown" for row in score_rows),
            *(str(row.get("section") or "Unknown").strip() or "Unknown" for row in compound_rows),
            *(str(row.get("section") or "Unknown").strip() or "Unknown" for row in family_rows),
        },
        key=_section_sort_key,
    )

    sections: Dict[str, Any] = {}
    for section in all_sections:
        section_score_rows = [row for row in score_rows if (str(row.get("section") or "").strip() or "Unknown") == section]
        section_family_rows = [row for row in family_rows if (str(row.get("section") or "").strip() or "Unknown") == section]
        section_consensus = (
            r_consensus_context.get("section_summaries", {}).get(section)
            if isinstance(r_consensus_context.get("section_summaries"), dict)
            else {}
        )
        sections[section] = {
            "summary": {
                "row_evidence_count": len(section_score_rows),
                "unique_canonicals": len({_digits_only(row.get("Canonical")) for row in section_score_rows if _digits_only(row.get("Canonical"))}),
                "long_canonical_rows": sum(1 for row in section_score_rows if len(_digits_only(row.get("Canonical"))) > 3),
                "compound_rows": sum(1 for row in compound_rows if (str(row.get("section") or "").strip() or "Unknown") == section),
                "family_box_rows": len(section_family_rows),
                "unique_family_ids": len({_to_int(row.get("family_id"), default=0) for row in section_family_rows if _to_int(row.get("family_id"), default=0) > 0}),
                "last_remaining_rows": sum(1 for row in section_family_rows if _to_bool(row.get("last_remaining_3v"))),
                "survivor_frontiers": len(survivor_frontiers.get(section, [])),
                "survivor_progressions": len(survivor_progressions.get(section, [])),
                "r_consensus_events": _to_int((section_consensus or {}).get("event_count"), 0),
                "r_consensus_col1": _to_int((section_consensus or {}).get("col1_count"), 0),
                "r_consensus_col2": _to_int((section_consensus or {}).get("col2_count"), 0),
                "r_consensus_two_digit": _to_int((section_consensus or {}).get("two_digit_count"), 0),
            },
            "top_row_patterns": top_rows_by_section.get(section, []),
            "pattern_ledgers_top": pattern_ledgers.get(section, []),
            "top_compound_patterns": compound_by_section.get(section, []),
            "family_rollups_top": family_rollups.get(section, []),
            "survivor_frontiers": survivor_frontiers.get(section, []),
            "survivor_progressions": survivor_progressions.get(section, []),
        }

    return {
        "schema": "stable_arena_v1",
        "generated_at": metrics.get("generated_at") or "",
        "results_date": results_date,
        "history_date": history_date,
        "profile": profile,
        "experiment_tag": experiment_tag,
        "state_key": state_key,
        "sharepack_root": _safe_rel(sharepacks_root, repo_root),
        "sharepack_state_dir": _safe_rel(state_dir, repo_root),
        "contains_winners_artifacts": bool(contains_winners_artifacts),
        "inputs_hash": _hash_inputs(required),
        "evidence_paths": [_safe_rel(path, repo_root) for path in required],
        "metrics_summary": _build_metrics_summary(metrics),
        "r_consensus_context": r_consensus_context,
        "sections": sections,
    }


def build_stable_arena_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = []
    state_key = str(payload.get("state_key") or "?")
    results_date = str(payload.get("results_date") or "?")
    profile = str(payload.get("profile") or "?")
    lines.append(f"# Stable Arena — {state_key} — D={results_date} ({profile})")
    lines.append("")
    lines.append("Purpose: preserve Stable evidence before candidate compression and budgeting.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- inputs_hash: `{payload.get('inputs_hash') or '-'}`")
    lines.append(f"- evidence_paths: `{', '.join(payload.get('evidence_paths') or [])}`")
    metrics_summary = payload.get("metrics_summary") or {}
    if isinstance(metrics_summary, dict):
        total_patterns = metrics_summary.get("total_patterns")
        total_families = metrics_summary.get("total_families")
        if total_patterns is not None:
            lines.append(f"- total_patterns: `{total_patterns}`")
        if total_families is not None:
            lines.append(f"- total_families: `{total_families}`")
    r_consensus_context = payload.get("r_consensus_context") if isinstance(payload.get("r_consensus_context"), dict) else {}
    if r_consensus_context.get("available"):
        lines.append(f"- r_consensus_events: `{r_consensus_context.get('event_count', 0)}`")
        lines.append(f"- r_consensus_strength: `{r_consensus_context.get('signal_strength_class', '-')}`")
        lines.append(f"- r_consensus_trial_eligible: `{r_consensus_context.get('trial_eligible')}`")
        lines.append(f"- r_consensus_top_tails: `{', '.join(r_consensus_context.get('top_tail_values') or []) or '-'}`")
        lines.append(f"- r_consensus_cross_variant_tails: `{', '.join(r_consensus_context.get('cross_variant_tail_values') or []) or '-'}`")

    def _top_parts_text(item: Dict[str, Any], top_n: int = 3) -> str:
        parts = sorted(
            (
                (name, float(value))
                for name, value in (item.get("score_breakdown_sums") or {}).items()
                if float(value) > 0.0
            ),
            key=lambda kv: (-kv[1], kv[0]),
        )[:top_n]
        if not parts:
            return "-"
        return ", ".join(f"{name.replace('score_', '')}:{value:g}" for name, value in parts)

    def _top_box_text(item: Dict[str, Any]) -> str:
        box = (item.get("top_box_contributions") or [{}])[0]
        label = str(box.get("box_label") or "-")
        total = box.get("score_total")
        if total in (None, ""):
            return label
        return f"{label}:{total}"

    def _reveal_text(item: Dict[str, Any]) -> str:
        reveal = item.get("hidden_family_reveal_summary") or item.get("hidden_family_reveal") or {}
        if not isinstance(reveal, dict):
            return "-"
        top_fragment = (reveal.get("top_fragments") or [{}])[0]
        fragment = str(top_fragment.get("value") or top_fragment.get("fragment") or "").strip()
        score = reveal.get("reveal_score_max", reveal.get("reveal_score"))
        if not fragment:
            return "-"
        if score in (None, ""):
            return fragment
        return f"{fragment}:{score}"

    def _transform_text(item: Dict[str, Any]) -> str:
        transform = item.get("order_transform_summary") or item.get("order_transform_hints") or {}
        if not isinstance(transform, dict):
            return "-"
        top = (transform.get("top_transforms") or [{}])[0]
        seed = str(top.get("seed") or "").strip()
        method_id = str(top.get("method_id") or "").strip()
        cost_units = top.get("cost_units")
        if not seed or not method_id:
            return "-"
        label_map = {
            "direct_perms": "perm",
            "vt8_expand_ordered": "vt8",
            "pair_mirror_third_12": "m12",
            "double_mirror_single_6": "dm_s6",
            "double_mirror_double_6": "dm_d6",
        }
        label = label_map.get(method_id, method_id)
        if cost_units in (None, ""):
            return f"{seed}->{label}"
        return f"{seed}->{label}:{cost_units}"

    sections = payload.get("sections") or {}
    ordered_sections = sorted(sections.keys(), key=_section_sort_key)
    for section in ordered_sections:
        block = sections.get(section) or {}
        summary = block.get("summary") or {}
        lines.append("")
        lines.append(f"## {section}")
        lines.append("")
        lines.append(f"- row_evidence_count: `{summary.get('row_evidence_count', 0)}`")
        lines.append(f"- unique_canonicals: `{summary.get('unique_canonicals', 0)}`")
        lines.append(f"- long_canonical_rows: `{summary.get('long_canonical_rows', 0)}`")
        lines.append(f"- family_box_rows: `{summary.get('family_box_rows', 0)}`")
        lines.append(f"- survivor_frontiers: `{summary.get('survivor_frontiers', 0)}`")
        lines.append(f"- survivor_progressions: `{summary.get('survivor_progressions', 0)}`")
        lines.append(f"- r_consensus_events: `{summary.get('r_consensus_events', 0)}`")
        lines.append(f"- r_consensus_col1/col2: `{summary.get('r_consensus_col1', 0)}/{summary.get('r_consensus_col2', 0)}`")
        lines.append(f"- r_consensus_two_digit: `{summary.get('r_consensus_two_digit', 0)}`")

        lines.append("")
        lines.append("Top row patterns:")
        lines.append("")
        lines.append("| Canonical | Score | Set | Draw | Col | Family | Why | Reveal | Transform |")
        lines.append("|---|---:|---|---|---:|---:|---|---|---|")
        for item in (block.get("top_row_patterns") or [])[:10]:
            family_id = item.get("family_id")
            why = ",".join(item.get("why_tags") or [])
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(item.get("canonical") or "-"),
                        str(item.get("score") or 0),
                        str(item.get("set") or "-"),
                        str(item.get("draw") or "-"),
                        str(item.get("column") or "-"),
                        str(family_id if family_id is not None else "-"),
                        why or "-",
                        _reveal_text(item),
                        _transform_text(item),
                    ]
                )
                + " |"
            )

        lines.append("")
        lines.append("Top pattern ledgers:")
        lines.append("")
        lines.append("| Canonical | Total | Compound | Rows | Boxes | C1/C2 | Top Parts | Top Box | Reveal | Transform |")
        lines.append("|---|---:|---:|---:|---:|---|---|---|---|---|")
        for item in (block.get("pattern_ledgers_top") or [])[:10]:
            compound_score = "-"
            compound_context = item.get("compound_context") or {}
            if compound_context:
                compound_score = str(compound_context.get("compound_score") or 0)
            frontier = item.get("frontier_summary") or {}
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(item.get("canonical") or "-"),
                        str(item.get("score_total") or 0),
                        compound_score,
                        str(item.get("row_hits") or 0),
                        str(item.get("box_count") or 0),
                        f"{frontier.get('col1_row_hits', 0)}/{frontier.get('col2_row_hits', 0)}",
                        _top_parts_text(item),
                        _top_box_text(item),
                        _reveal_text(item),
                        _transform_text(item),
                    ]
                )
                + " |"
            )

        lines.append("")
        lines.append("Top family rollups:")
        lines.append("")
        lines.append("| Family | Score Total | Score Max | Boxes | Last Remaining | Top Canonicals | Hidden | Transform |")
        lines.append("|---:|---:|---:|---:|---:|---|---|---|")
        for item in (block.get("family_rollups_top") or [])[:10]:
            canonicals = ", ".join(
                f"{entry.get('value')}:{entry.get('count')}"
                for entry in (item.get("top_canonicals") or [])[:4]
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(item.get("family_id") or "-"),
                        str(item.get("family_score_total") or 0),
                        str(item.get("family_score_max") or 0),
                        str(item.get("box_count") or 0),
                        str(item.get("last_remaining_count") or 0),
                        canonicals or "-",
                        _reveal_text(item),
                        _transform_text(item),
                    ]
                )
                + " |"
            )

        frontier_count = len(block.get("survivor_frontiers") or [])
        lines.append("")
        lines.append(f"Survivor frontiers recorded: `{frontier_count}`")
        for frontier in (block.get("survivor_frontiers") or [])[:10]:
            family_ids = ",".join(str(fid) for fid in (frontier.get("family_ids") or []))
            frontier_patterns = ", ".join(
                entry.get("value") or "-"
                for entry in ((frontier.get("frontier_pattern_summary") or {}).get("exact3digit_patterns_top") or [])[:4]
            )
            lines.append(
                f"- {frontier.get('set')}/{frontier.get('draw')} -> col {frontier.get('frontier_column')} "
                f"(families={frontier.get('frontier_family_count')}, single_family={frontier.get('is_single_family')}, ids={family_ids or '-'}, exact3={frontier_patterns or '-'})"
            )

        progression_count = len(block.get("survivor_progressions") or [])
        lines.append("")
        lines.append(f"Survivor progressions recorded: `{progression_count}`")
        for progression in (block.get("survivor_progressions") or [])[:10]:
            cols = ",".join(str(item) for item in (progression.get("eligible_columns") or []))
            lines.append(
                f"- {progression.get('set')}/{progression.get('draw')} -> cols [{cols}] "
                f"(frontier={progression.get('frontier_column')}, single_family={progression.get('is_frontier_single_family')}, last_remaining={progression.get('has_last_remaining')})"
            )

    if r_consensus_context.get("available"):
        lines.append("")
        lines.append("## R-Consensus Context")
        lines.append("")
        lines.append(f"- event_count: `{r_consensus_context.get('event_count', 0)}`")
        lines.append(f"- single_digit_count: `{r_consensus_context.get('single_digit_count', 0)}`")
        lines.append(f"- two_digit_count: `{r_consensus_context.get('two_digit_count', 0)}`")
        lines.append(f"- col1/col2: `{r_consensus_context.get('col1_count', 0)}/{r_consensus_context.get('col2_count', 0)}`")
        lines.append(f"- signal_strength_class: `{r_consensus_context.get('signal_strength_class', '-')}`")
        lines.append(f"- trial_eligible: `{r_consensus_context.get('trial_eligible')}`")
        lines.append(f"- top_tail_values: `{', '.join(r_consensus_context.get('top_tail_values') or []) or '-'}`")
        lines.append(f"- cross_variant_tail_values: `{', '.join(r_consensus_context.get('cross_variant_tail_values') or []) or '-'}`")
        lines.append(f"- top_support_canonicals: `{', '.join(r_consensus_context.get('top_support_canonicals') or []) or '-'}`")
        lines.append(f"- top_support_vtrac_indices: `{', '.join(r_consensus_context.get('top_support_vtrac_indices') or []) or '-'}`")
        for item in (r_consensus_context.get("events_top") or [])[:10]:
            lines.append(
                f"- {item.get('section')}/{item.get('set')}/{item.get('draw')}/Col{item.get('column')} "
                f"tail={item.get('tail_value')} ({item.get('event_class')}) "
                f"flags=full:{item.get('cons_full')} 3v:{item.get('cons_3v')} stub:{item.get('cons_stub')} "
                f"support={','.join(item.get('top_support_canonicals') or []) or '-'}"
            )

    return "\n".join(lines).rstrip() + "\n"


def write_stable_arena_files(
    *,
    out_json_path: Path,
    payload: Dict[str, Any],
    write_md: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_json_path.parent.mkdir(parents=True, exist_ok=True)
    out_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path: Optional[Path] = None
    if write_md:
        md_path = out_json_path.with_suffix(".md")
        md_path.write_text(build_stable_arena_markdown(payload), encoding="utf-8")
    return out_json_path, md_path


__all__ = [
    "build_stable_arena_markdown",
    "build_stable_arena_payload",
    "write_stable_arena_files",
]
