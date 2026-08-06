#!/usr/bin/env python3
"""Create a post-result VTRAC corridor summary for deep review.

This is a review-only diagnostic. It reads frozen winner-side artifacts and
does not mutate predictive sharepacks, Analysis Arena JSON, or VTRAC Enhanced
scoring outputs.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import itertools
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_index_set, get_vtrac_index
from modules.vtrac_straight_map import (
    ordered_vcode_for_combo,
    vstraight_lane_for_combo,
    vstraight_lanes_for_index,
)


COLUMN_KEYS = tuple(str(i) for i in range(1, 8))
PATTERN_ROW_TYPES = {"r2", "r4", "r6", "r8"}


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _permutations3(value: Any) -> List[str]:
    digits = _digits_only(value)
    if len(digits) != 3:
        return []
    return sorted({"".join(parts) for parts in itertools.permutations(digits, 3)})


def _gap_regex(token: str) -> re.Pattern[str]:
    a, b, c = token
    return re.compile(fr"{a}\d?{b}\d?{c}")


def _overlap_count(cleaned: str, token: str) -> int:
    if not token:
        return 0
    return sum(1 for _ in re.finditer(fr"(?={re.escape(token)})", cleaned))


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


@dataclass(frozen=True)
class CellRecord:
    variant: str
    set_name: str
    draw: str
    row_type: str
    column: str
    text: str
    tags: Tuple[str, ...]


def iter_winner_cells(winner_payload: Dict[str, Any]) -> Iterator[CellRecord]:
    tables = winner_payload.get("tables") or {}
    if not isinstance(tables, dict):
        return

    for variant, rows in tables.items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            set_name = str(row.get("Set") or "")
            draw = str(row.get("Draw") or "")
            row_type = str(row.get("RowType") or "")
            cells = row.get("cells") or {}
            if not isinstance(cells, dict):
                continue
            for column in COLUMN_KEYS:
                cell = cells.get(column) or {}
                if not isinstance(cell, dict):
                    continue
                tags = tuple(str(tag) for tag in (cell.get("tags") or []))
                yield CellRecord(
                    variant=str(variant),
                    set_name=set_name,
                    draw=draw,
                    row_type=row_type,
                    column=f"C{column}",
                    text=str(cell.get("text") or ""),
                    tags=tags,
                )


def _sorted_counter(counter: Counter[str]) -> Dict[str, int]:
    return {key: counter[key] for key in sorted(counter, key=lambda k: (-counter[k], k))}


def _top_counter(counter: Counter[str], limit: int = 20) -> List[Dict[str, Any]]:
    return [{"value": key, "count": value} for key, value in counter.most_common(limit)]


def _summarize_group(cells: Sequence[CellRecord], tokens: Sequence[str]) -> Dict[str, Any]:
    token_set = set(tokens)
    regexes = {token: _gap_regex(token) for token in token_set}
    strict_cell_hits = 0
    gap_cell_hits = 0
    strict_occurrences = 0
    token_cell_hits: Counter[str] = Counter()
    token_occurrences: Counter[str] = Counter()
    token_gap_cell_hits: Counter[str] = Counter()
    by_variant: Counter[str] = Counter()
    by_set: Counter[str] = Counter()
    by_column: Counter[str] = Counter()
    by_row_type: Counter[str] = Counter()
    by_variant_set: Counter[str] = Counter()
    by_variant_column: Counter[str] = Counter()
    examples: List[Dict[str, Any]] = []

    for cell in cells:
        cleaned = _digits_only(cell.text)
        if len(cleaned) < 3:
            continue

        strict_tokens: List[str] = []
        gap_tokens: List[str] = []
        for token in sorted(token_set):
            occurrences = _overlap_count(cleaned, token)
            if occurrences:
                strict_tokens.append(token)
                token_cell_hits[token] += 1
                token_occurrences[token] += occurrences
                strict_occurrences += occurrences
            elif regexes[token].search(cleaned):
                gap_tokens.append(token)
                token_gap_cell_hits[token] += 1

        if strict_tokens:
            strict_cell_hits += 1
            by_variant[cell.variant] += 1
            by_set[cell.set_name] += 1
            by_column[cell.column] += 1
            by_row_type[cell.row_type] += 1
            by_variant_set[f"{cell.variant}:{cell.set_name}"] += 1
            by_variant_column[f"{cell.variant}:{cell.column}"] += 1
            if len(examples) < 25:
                examples.append(
                    {
                        "variant": cell.variant,
                        "set": cell.set_name,
                        "draw": cell.draw,
                        "row_type": cell.row_type,
                        "column": cell.column,
                        "text": cell.text,
                        "strict_tokens": strict_tokens[:12],
                        "tags": list(cell.tags),
                    }
                )
        elif gap_tokens:
            gap_cell_hits += 1

    return {
        "token_count": len(token_set),
        "strict_cell_hits": strict_cell_hits,
        "gap_cell_hits_without_strict": gap_cell_hits,
        "strict_occurrences": strict_occurrences,
        "tokens_seen": sorted(token_cell_hits),
        "top_tokens_by_cell_hits": _top_counter(token_cell_hits),
        "top_tokens_by_occurrences": _top_counter(token_occurrences),
        "top_gap_tokens_without_strict": _top_counter(token_gap_cell_hits),
        "by_variant": _sorted_counter(by_variant),
        "by_set": _sorted_counter(by_set),
        "by_column": _sorted_counter(by_column),
        "by_row_type": _sorted_counter(by_row_type),
        "by_variant_set": _sorted_counter(by_variant_set),
        "by_variant_column": _sorted_counter(by_variant_column),
        "examples": examples,
    }


def _scope_cells(cells: Sequence[CellRecord], scope: str) -> List[CellRecord]:
    normalized = str(scope or "").strip().lower()
    if normalized == "pattern_rows_only":
        return [cell for cell in cells if cell.row_type.strip().lower() in PATTERN_ROW_TYPES]
    if normalized == "draw_data_only":
        return [cell for cell in cells if cell.row_type.strip().lower() == "draw_data"]
    return list(cells)


def _summarize_scopes(cells: Sequence[CellRecord], tokens: Sequence[str]) -> Dict[str, Any]:
    return {
        "pattern_rows_only": _summarize_group(_scope_cells(cells, "pattern_rows_only"), tokens),
        "draw_data_only": _summarize_group(_scope_cells(cells, "draw_data_only"), tokens),
        "all_rows_inclusive": _summarize_group(_scope_cells(cells, "all_rows_inclusive"), tokens),
    }


def _tag_counts(cells: Sequence[CellRecord]) -> Dict[str, int]:
    counts: Counter[str] = Counter()
    for cell in cells:
        for tag in cell.tags:
            counts[tag] += 1
    return _sorted_counter(counts)


def _enhanced_summary(enhanced_payload: Optional[Dict[str, Any]], *, index: int, ordered_lane: Sequence[str], literal_permutations: Sequence[str], corridor: Sequence[str]) -> Dict[str, Any]:
    if not enhanced_payload:
        return {"available": False}

    index_entry = None
    index_rank = None
    for pos, row in enumerate(enhanced_payload.get("indices_ranked") or [], start=1):
        try:
            row_index = int(row.get("index"))
        except Exception:
            continue
        if row_index == int(index):
            index_entry = row
            index_rank = pos
            break

    top_straights = enhanced_payload.get("straights_ranked") or []
    top_straight_values = [str(row.get("straight") or "") for row in top_straights if isinstance(row, dict)]
    top_corridor = [value for value in top_straight_values if value in set(corridor)]
    top_ordered_lane = [value for value in top_straight_values if value in set(ordered_lane)]
    top_literal_permutations = [value for value in top_straight_values if value in set(literal_permutations)]

    raw = {}
    order_counts: Dict[str, Any] = {}
    if isinstance(index_entry, dict):
        raw = (((index_entry.get("evidence") or {}).get("raw")) or {})
        if isinstance(raw.get("order_counts"), dict):
            order_counts = raw.get("order_counts") or {}

    def order_slice(values: Sequence[str]) -> Dict[str, Any]:
        return {value: order_counts.get(value, 0) for value in values}

    return {
        "available": True,
        "target_index_rank": index_rank,
        "target_index_score": index_entry.get("score") if isinstance(index_entry, dict) else None,
        "target_index_raw": {
            key: raw.get(key)
            for key in (
                "presence_score",
                "sections",
                "set_presence",
                "hot_hits",
                "super_hot_hits",
                "first_col",
                "max_streak",
                "total_hits",
                "reduction_hits",
                "columns_by_ring",
                "order_counts",
            )
            if key in raw
        },
        "top_corridor_straights": top_corridor[:20],
        "top_ordered_lane_straights": top_ordered_lane[:20],
        "top_literal_permutation_straights": top_literal_permutations[:20],
        "ordered_lane_order_counts": order_slice(ordered_lane),
        "literal_permutation_order_counts": order_slice(literal_permutations),
        "corridor_order_counts_present": {value: order_counts[value] for value in sorted(set(corridor) & set(order_counts))},
    }


def create_corridor_summary(
    *,
    winner_json_path: Path,
    enhanced_json_path: Optional[Path] = None,
    date: Optional[str] = None,
    state: Optional[str] = None,
    winner: Optional[str] = None,
) -> Dict[str, Any]:
    winner_payload = _read_json(winner_json_path)
    if not isinstance(winner_payload, dict):
        raise ValueError(f"winner JSON must contain an object: {winner_json_path}")

    winner_literal = _digits_only(winner or winner_payload.get("winner_combo"))
    if len(winner_literal) != 3:
        raise ValueError("winner literal must be a 3-digit Pick-3 value")

    target_state = state or str(winner_payload.get("state") or "")
    raw_index = winner_payload.get("index") or get_vtrac_index(winner_literal)
    if raw_index is None:
        raise ValueError(
            f"winner {winner_literal} has no boxed VTRAC index in the current reference"
        )
    target_index = int(raw_index)
    ordered_vcode = ordered_vcode_for_combo(winner_literal)
    ordered_lane = vstraight_lane_for_combo(winner_literal)
    literal_permutations = _permutations3(winner_literal)
    boxed_corridor = sorted(get_index_set(target_index))
    ordered_lanes_for_index = vstraight_lanes_for_index(target_index)

    cells = list(iter_winner_cells(winner_payload))
    tag_counts = _tag_counts(cells)
    literal_scopes = _summarize_scopes(cells, literal_permutations)
    ordered_scopes = _summarize_scopes(cells, ordered_lane)
    corridor_scopes = _summarize_scopes(cells, boxed_corridor)
    literal_summary = literal_scopes["all_rows_inclusive"]
    ordered_summary = ordered_scopes["all_rows_inclusive"]
    corridor_summary = corridor_scopes["all_rows_inclusive"]
    ordered_pattern_summary = ordered_scopes["pattern_rows_only"]
    corridor_pattern_summary = corridor_scopes["pattern_rows_only"]
    corridor_draw_summary = corridor_scopes["draw_data_only"]

    enhanced_payload = _read_json(enhanced_json_path) if enhanced_json_path and enhanced_json_path.exists() else None
    enhanced = _enhanced_summary(
        enhanced_payload if isinstance(enhanced_payload, dict) else None,
        index=target_index,
        ordered_lane=ordered_lane,
        literal_permutations=literal_permutations,
        corridor=boxed_corridor,
    )

    renderer_vt_tags = int(tag_counts.get("hit-vt-straight", 0)) + int(tag_counts.get("hit-vt-straight-gap", 0))
    renderer_gap = bool(corridor_summary["strict_cell_hits"] and renderer_vt_tags == 0)
    analyzer_gap = False
    if enhanced.get("available"):
        ordered_order_counts = enhanced.get("ordered_lane_order_counts") or {}
        analyzer_gap = bool(
            enhanced.get("target_index_rank") is not None
            and ordered_summary["strict_cell_hits"] > 0
            and not any(float(value or 0) > 0 for value in ordered_order_counts.values())
        )
    strong_corridor = bool(corridor_summary["strict_cell_hits"] >= 50 and len(corridor_summary["by_variant"]) >= 2)
    weak_corridor = bool(corridor_summary["strict_cell_hits"] > 0 and not strong_corridor)
    draw_data_inflation_warning = bool(
        corridor_draw_summary["strict_cell_hits"] > 0
        and corridor_summary["strict_cell_hits"] > corridor_pattern_summary["strict_cell_hits"]
    )

    return {
        "schema": "aat9.vtrac_corridor_summary.v1",
        "review_only": True,
        "inputs": {
            "winner_json": str(winner_json_path),
            "enhanced_json": str(enhanced_json_path) if enhanced_json_path else None,
        },
        "case": {
            "date": date,
            "state": target_state,
            "winner_literal": winner_literal,
            "boxed_vtrac_index": target_index,
            "ordered_vcode": ordered_vcode,
            "ordered_lane_8": ordered_lane,
            "literal_permutations": literal_permutations,
            "boxed_corridor_size": len(boxed_corridor),
            "boxed_corridor_48": boxed_corridor,
            "ordered_vcodes_for_index": sorted(ordered_lanes_for_index),
        },
        "winner_json_evidence": {
            "renderer_tag_counts": tag_counts,
            "literal_permutation_exposure": literal_summary,
            "ordered_lane_exposure": ordered_summary,
            "boxed_index_corridor_exposure": corridor_summary,
            "row_scope_breakout": {
                "literal_permutation_exposure": literal_scopes,
                "ordered_lane_exposure": ordered_scopes,
                "boxed_index_corridor_exposure": corridor_scopes,
            },
        },
        "enhanced_vtrac_comparison": enhanced,
        "interpretation_flags": {
            "renderer_gap": renderer_gap,
            "analyzer_gap": analyzer_gap,
            "strong_corridor": strong_corridor,
            "weak_corridor": weak_corridor,
            "pattern_row_corridor_present": bool(corridor_pattern_summary["strict_cell_hits"] > 0),
            "ordered_lane_pattern_row_present": bool(ordered_pattern_summary["strict_cell_hits"] > 0),
            "draw_data_corridor_support": bool(corridor_draw_summary["strict_cell_hits"] > 0),
            "draw_data_inflation_warning": draw_data_inflation_warning,
        },
        "interpretation": _build_interpretation(
            winner_literal=winner_literal,
            ordered_vcode=ordered_vcode or "",
            index=target_index,
            ordered_summary=ordered_summary,
            corridor_summary=corridor_summary,
            tag_counts=tag_counts,
            enhanced=enhanced,
            flags={
                "renderer_gap": renderer_gap,
                "analyzer_gap": analyzer_gap,
                "strong_corridor": strong_corridor,
                "weak_corridor": weak_corridor,
                "draw_data_inflation_warning": draw_data_inflation_warning,
            },
        ),
    }


def _build_interpretation(
    *,
    winner_literal: str,
    ordered_vcode: str,
    index: int,
    ordered_summary: Dict[str, Any],
    corridor_summary: Dict[str, Any],
    tag_counts: Dict[str, int],
    enhanced: Dict[str, Any],
    flags: Dict[str, bool],
) -> List[str]:
    lines: List[str] = []
    lines.append(
        f"{winner_literal} maps to ordered lane {ordered_vcode} and boxed VTRAC index {index}; these are separate semantics."
    )
    lines.append(
        f"Winner JSON strict corridor cells: {corridor_summary['strict_cell_hits']}; ordered-lane strict cells: {ordered_summary['strict_cell_hits']}."
    )
    if flags.get("renderer_gap"):
        lines.append(
            "Renderer gap: corridor evidence exists, but legacy hit-vt-straight tags are absent or insufficient."
        )
    if enhanced.get("available"):
        lines.append(
            f"VTRAC Enhanced target index rank: {enhanced.get('target_index_rank')} with score {enhanced.get('target_index_score')}."
        )
        if flags.get("analyzer_gap"):
            lines.append(
                "Analyzer gap: enhanced payload preserved the boxed index but did not carry positive order_counts for this exact ordered lane."
            )
    if flags.get("strong_corridor"):
        lines.append("Corridor read: strong boxed-index corridor evidence for deep-review purposes.")
    elif flags.get("weak_corridor"):
        lines.append("Corridor read: present but not strong by this diagnostic threshold.")
    else:
        lines.append("Corridor read: no meaningful strict corridor exposure found.")
    vt_tags = int(tag_counts.get("hit-vt-straight", 0)) + int(tag_counts.get("hit-vt-straight-gap", 0))
    lines.append(f"Legacy hit-vt-straight tag total: {vt_tags}; do not use this alone as full ordered-lane proof.")
    if flags.get("draw_data_inflation_warning"):
        lines.append(
            "Row-scope warning: draw_data contributes corridor evidence; use R2/R4/R6/R8 pattern rows as the primary predictive scope."
        )
    return lines


def _render_counter_table(title: str, rows: Dict[str, int]) -> List[str]:
    out = [f"### {title}", "", "| Value | Count |", "|---|---:|"]
    if not rows:
        out.append("| _none_ | 0 |")
    else:
        for key, value in rows.items():
            out.append(f"| `{key}` | {value} |")
    out.append("")
    return out


def render_markdown(summary: Dict[str, Any]) -> str:
    case = summary["case"]
    evidence = summary["winner_json_evidence"]
    enhanced = summary["enhanced_vtrac_comparison"]
    flags = summary["interpretation_flags"]

    lines = [
        f"# VTRAC Corridor Summary - {case.get('date') or 'unknown-date'} {case.get('state') or 'unknown-state'} {case['winner_literal']}",
        "",
        "Review-only diagnostic. This artifact is post-result and must not be treated as a live predictive output.",
        "",
        "## Case",
        "",
        f"- Winner literal: `{case['winner_literal']}`",
        f"- Boxed VTRAC index: `{case['boxed_vtrac_index']}`",
        f"- Ordered VSTRAIGHTS lane: `{case['ordered_vcode']}`",
        f"- Ordered lane members: `{', '.join(case['ordered_lane_8'])}`",
        f"- Literal permutations: `{', '.join(case['literal_permutations'])}`",
        f"- Full boxed-index corridor size: `{case['boxed_corridor_size']}`",
        f"- Ordered vcodes for index: `{', '.join(case['ordered_vcodes_for_index'])}`",
        "",
        "## Interpretation Flags",
        "",
        f"- renderer_gap: `{flags['renderer_gap']}`",
        f"- analyzer_gap: `{flags['analyzer_gap']}`",
        f"- strong_corridor: `{flags['strong_corridor']}`",
        f"- weak_corridor: `{flags['weak_corridor']}`",
        f"- pattern_row_corridor_present: `{flags.get('pattern_row_corridor_present')}`",
        f"- ordered_lane_pattern_row_present: `{flags.get('ordered_lane_pattern_row_present')}`",
        f"- draw_data_corridor_support: `{flags.get('draw_data_corridor_support')}`",
        f"- draw_data_inflation_warning: `{flags.get('draw_data_inflation_warning')}`",
        "",
        "## Interpretation",
        "",
    ]
    lines.extend(f"- {item}" for item in summary["interpretation"])
    lines.append("")

    literal = evidence["literal_permutation_exposure"]
    ordered = evidence["ordered_lane_exposure"]
    corridor = evidence["boxed_index_corridor_exposure"]

    lines.extend(
        [
            "## Exposure Summary",
            "",
            "| Group | Token Count | Strict Cell Hits | Gap-Only Cell Hits | Strict Occurrences |",
            "|---|---:|---:|---:|---:|",
            f"| Literal permutations | {literal['token_count']} | {literal['strict_cell_hits']} | {literal['gap_cell_hits_without_strict']} | {literal['strict_occurrences']} |",
            f"| Ordered lane | {ordered['token_count']} | {ordered['strict_cell_hits']} | {ordered['gap_cell_hits_without_strict']} | {ordered['strict_occurrences']} |",
            f"| Boxed-index corridor | {corridor['token_count']} | {corridor['strict_cell_hits']} | {corridor['gap_cell_hits_without_strict']} | {corridor['strict_occurrences']} |",
            "",
        ]
    )

    scopes = evidence.get("row_scope_breakout") if isinstance(evidence.get("row_scope_breakout"), dict) else {}
    if scopes:
        lines.extend(
            [
                "## Row-Scope Exposure Summary",
                "",
                "Primary predictive interpretation should use `pattern_rows_only` (`R2/R4/R6/R8`). `draw_data_only` is context/support and `all_rows_inclusive` is audit context.",
                "",
                "| Group | Pattern Rows Strict Cells | Draw Data Strict Cells | All Rows Strict Cells | Pattern Rows Occurrences | Draw Data Occurrences | All Rows Occurrences |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for label, key in (
            ("Literal permutations", "literal_permutation_exposure"),
            ("Ordered lane", "ordered_lane_exposure"),
            ("Boxed-index corridor", "boxed_index_corridor_exposure"),
        ):
            row = scopes.get(key) if isinstance(scopes.get(key), dict) else {}
            pattern = row.get("pattern_rows_only") if isinstance(row.get("pattern_rows_only"), dict) else {}
            draw = row.get("draw_data_only") if isinstance(row.get("draw_data_only"), dict) else {}
            all_rows = row.get("all_rows_inclusive") if isinstance(row.get("all_rows_inclusive"), dict) else {}
            lines.append(
                f"| {label} | {pattern.get('strict_cell_hits', 0)} | {draw.get('strict_cell_hits', 0)} | {all_rows.get('strict_cell_hits', 0)} | {pattern.get('strict_occurrences', 0)} | {draw.get('strict_occurrences', 0)} | {all_rows.get('strict_occurrences', 0)} |"
            )
        lines.append("")

    lines.extend(_render_counter_table("Renderer Tag Counts", evidence["renderer_tag_counts"]))
    lines.extend(_render_counter_table("Corridor By Variant", corridor["by_variant"]))
    lines.extend(_render_counter_table("Corridor By Set", corridor["by_set"]))
    lines.extend(_render_counter_table("Corridor By Column", corridor["by_column"]))
    lines.extend(_render_counter_table("Corridor By R Row", corridor["by_row_type"]))

    lines.extend(["### Top Same-Index Corridor Witnesses", "", "| Token | Cell Hits |", "|---|---:|"])
    for row in corridor["top_tokens_by_cell_hits"][:20]:
        lines.append(f"| `{row['value']}` | {row['count']} |")
    lines.append("")

    lines.extend(["### Top Ordered-Lane Witnesses", "", "| Token | Cell Hits |", "|---|---:|"])
    if ordered["top_tokens_by_cell_hits"]:
        for row in ordered["top_tokens_by_cell_hits"][:20]:
            lines.append(f"| `{row['value']}` | {row['count']} |")
    else:
        lines.append("| _none_ | 0 |")
    lines.append("")

    lines.extend(["## Enhanced VTRAC Comparison", ""])
    if not enhanced.get("available"):
        lines.append("- Enhanced VTRAC JSON was not provided or unavailable.")
    else:
        lines.extend(
            [
                f"- Target index rank: `{enhanced.get('target_index_rank')}`",
                f"- Target index score: `{enhanced.get('target_index_score')}`",
                f"- Top corridor straights in enhanced ranking: `{', '.join(enhanced.get('top_corridor_straights') or []) or '-'}`",
                f"- Top ordered-lane straights in enhanced ranking: `{', '.join(enhanced.get('top_ordered_lane_straights') or []) or '-'}`",
                f"- Top literal permutations in enhanced ranking: `{', '.join(enhanced.get('top_literal_permutation_straights') or []) or '-'}`",
            ]
        )
    lines.append("")
    lines.extend(
        [
            "## Inputs",
            "",
            f"- Winner JSON: `{summary['inputs']['winner_json']}`",
            f"- Enhanced JSON: `{summary['inputs'].get('enhanced_json') or '-'}`",
            "",
        ]
    )
    return "\n".join(lines)


def _default_out_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "DEEP_EXAMPLE_REVIEW_PREP" / "VTRAC_CORRIDOR_SUMMARIES"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--winner-json", required=True, type=Path)
    parser.add_argument("--enhanced-json", type=Path)
    parser.add_argument("--date")
    parser.add_argument("--state")
    parser.add_argument("--winner")
    parser.add_argument("--out-dir", type=Path, default=_default_out_dir())
    parser.add_argument("--stem")
    args = parser.parse_args(argv)

    summary = create_corridor_summary(
        winner_json_path=args.winner_json,
        enhanced_json_path=args.enhanced_json,
        date=args.date,
        state=args.state,
        winner=args.winner,
    )

    case = summary["case"]
    stem = args.stem or f"{case.get('date') or 'unknown-date'}__{case.get('state') or 'unknown-state'}__{case['winner_literal']}__VTRAC_CORRIDOR_SUMMARY"
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / f"{stem}.json"
    md_path = args.out_dir / f"{stem}.md"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    md_path.write_text(render_markdown(summary), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
