#!/usr/bin/env python3
"""Create a translator-learning ledger for a completed Analysis Arena window."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import read_json, safe_rel


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-csv", default="", help="Optional CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "ledger": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
        "hits": window_root / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv",
        "frontier": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv",
        "md": window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
        "csv": window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv",
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


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def _as_int(value: Any) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return 0


def _rate(count: int, den: int) -> float:
    return count / den if den else 0.0


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _join(values: Iterable[str]) -> str:
    cleaned = [str(value).strip() for value in values if str(value).strip()]
    return "|".join(cleaned)


def _event_key(row: Dict[str, str]) -> Tuple[str, str, str, str]:
    return (
        str(row.get("date") or "").strip(),
        str(row.get("state_key") or row.get("state") or "").strip(),
        str(row.get("period") or "").strip(),
        str(row.get("winner") or "").strip(),
    )


def _frontier_key(row: Dict[str, str]) -> Tuple[str, str, str]:
    return (
        str(row.get("date") or "").strip(),
        str(row.get("state_key") or "").strip(),
        str(row.get("winner") or "").strip(),
    )


def _boxlike(row: Dict[str, str]) -> bool:
    return any(
        _truthy(row.get(key))
        for key in (
            "arena_box_signal",
            "sandbox_box_seed",
            "sandbox_exact_seed",
            "arena_primary_box",
            "preserved_not_budgeted",
        )
    )


def _vtlike(row: Dict[str, str]) -> bool:
    return any(_truthy(row.get(key)) for key in ("arena_primary_vt", "sandbox_vt_seed"))


def _should_include(row: Dict[str, str]) -> bool:
    return any(
        _truthy(row.get(key))
        for key in (
            "opportunity_gap_box",
            "opportunity_gap_exact",
            "preserved_not_budgeted",
            "arena_box_signal",
            "arena_exact_signal",
            "arena_primary_box",
            "arena_primary_vt",
            "sandbox_box_seed",
            "sandbox_exact_seed",
            "sandbox_vt_seed",
            "play_card_any_exact",
            "play_card_any_box",
        )
    )


def _cohort_tags(row: Dict[str, str]) -> List[str]:
    tags: List[str] = []
    if _truthy(row.get("opportunity_gap_box")):
        tags.append("BOX_GAP")
    if _truthy(row.get("opportunity_gap_exact")):
        tags.append("EXACT_GAP")
    if _truthy(row.get("play_card_any_exact")) and (_truthy(row.get("arena_exact_signal")) or _truthy(row.get("sandbox_exact_seed"))):
        tags.append("EXACT_CONVERTED")
    if _truthy(row.get("play_card_any_box")) and _boxlike(row):
        tags.append("BOX_CONVERTED")
    if _truthy(row.get("play_vtrac_only_hit")) and _vtlike(row):
        tags.append("VT_CONVERTED")
    if _truthy(row.get("preserved_not_budgeted")):
        tags.append("PRESERVED")
    if _truthy(row.get("arena_box_signal")) or _truthy(row.get("arena_exact_signal")):
        tags.append("ARENA_EXPLICIT")
    if _vtlike(row):
        tags.append("VT_FINALIST")
    if _boxlike(row):
        tags.append("BOX_FINALIST")
    return tags


def _primary_cohort(tags: List[str]) -> str:
    priority = [
        "BOX_GAP",
        "EXACT_GAP",
        "EXACT_CONVERTED",
        "BOX_CONVERTED",
        "VT_CONVERTED",
        "PRESERVED",
        "ARENA_EXPLICIT",
        "BOX_FINALIST",
        "VT_FINALIST",
    ]
    for item in priority:
        if item in tags:
            return item
    return "UNCLASSIFIED"


def _support_score(row: Dict[str, str]) -> int:
    return sum(
        int(_truthy(row.get(key)))
        for key in (
            "arena_box_signal",
            "arena_exact_signal",
            "arena_primary_box",
            "arena_primary_vt",
            "sandbox_box_seed",
            "sandbox_exact_seed",
            "sandbox_vt_seed",
            "preserved_not_budgeted",
            "play_card_any_exact",
            "play_card_any_box",
        )
    )


def _sorted_examples(rows: Iterable[Dict[str, str]], *, limit: int = 6) -> List[Dict[str, Any]]:
    def sort_key(row: Dict[str, str]) -> Tuple[int, int, str, str, str]:
        rank = _as_int(row.get("board_rank"))
        return (
            0 if "GAP" in str(row.get("primary_cohort") or "") else 1,
            rank if rank > 0 else 999,
            -_as_int(row.get("translator_support_score")),
            str(row.get("date") or ""),
            str(row.get("state_key") or ""),
        )

    out: List[Dict[str, Any]] = []
    for row in sorted(rows, key=sort_key)[:limit]:
        out.append(
            {
                "date": row.get("date", ""),
                "state": row.get("state_key", ""),
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "board_rank": _as_int(row.get("board_rank")),
                "primary_cohort": row.get("primary_cohort", ""),
                "cohort_tags": row.get("cohort_tags", "").split("|") if row.get("cohort_tags") else [],
                "arena_final_candidate_signature": row.get("arena_final_candidate_signature", ""),
                "frontier_signature_type": row.get("frontier_signature_type", ""),
                "double_context_strength": row.get("double_context_strength", ""),
                "translator_support_score": _as_int(row.get("translator_support_score")),
            }
        )
    return out


def build_payload(window_root: Path) -> Dict[str, Any]:
    paths = _default_paths(window_root)
    perf_rows = _read_csv_rows(paths["ledger"])
    hit_rows = _read_csv_rows(paths["hits"])
    frontier_rows = _read_csv_rows(paths["frontier"])

    hit_lookup = {_event_key(row): row for row in hit_rows}
    frontier_lookup = {_frontier_key(row): row for row in frontier_rows}

    output_rows: List[Dict[str, str]] = []
    cohort_counter: Counter[str] = Counter()
    signature_counter: Counter[str] = Counter()
    frontier_counter: Counter[str] = Counter()
    top_state_counter: Counter[str] = Counter()

    for perf_row in perf_rows:
        if not _should_include(perf_row):
            continue
        key = _event_key(perf_row)
        merged: Dict[str, str] = dict(perf_row)
        hit_row = hit_lookup.get(key) or {}
        for k, v in hit_row.items():
            if k not in merged or not merged[k]:
                merged[k] = v
        frontier_row = frontier_lookup.get((key[0], key[1], key[3])) or {}
        for src, dest in (
            ("frontier_signature_type", "frontier_signature_type"),
            ("signature_strength", "frontier_signature_strength"),
            ("frontier_strength_score", "frontier_strength_score"),
            ("hidden_winner_score", "hidden_winner_score"),
            ("feeder_progression_score", "feeder_progression_score"),
            ("vtrac_frontier_score", "vtrac_frontier_score"),
            ("double_anchor_score", "double_anchor_score"),
            ("cross_variant_echo_score", "cross_variant_echo_score"),
        ):
            merged[dest] = str(frontier_row.get(src) or "")

        tags = _cohort_tags(merged)
        merged["cohort_tags"] = _join(tags)
        merged["primary_cohort"] = _primary_cohort(tags)
        merged["translator_support_score"] = str(_support_score(merged))
        output_rows.append(merged)
        cohort_counter.update(tags)
        signature_counter[str(merged.get("arena_final_candidate_signature") or "").strip() or "UNSPECIFIED"] += 1
        frontier_counter[str(merged.get("frontier_signature_type") or "").strip() or "UNSPECIFIED"] += 1
        state_key = str(merged.get("state_key") or "").strip()
        if state_key:
            top_state_counter[state_key] += 1

    summary = {
        "winner_events": len(perf_rows),
        "translator_rows": len(output_rows),
        "cohort_counts": dict(cohort_counter.most_common()),
        "finalist_signature_counts": dict(signature_counter.most_common()),
        "frontier_signature_counts": dict(frontier_counter.most_common()),
        "top_states": [{"value": value, "count": count} for value, count in top_state_counter.most_common(8)],
        "rates": {
            "translator_rows": _rate(len(output_rows), len(perf_rows)),
            "box_gap_rows": _rate(cohort_counter.get("BOX_GAP", 0), len(perf_rows)),
            "exact_gap_rows": _rate(cohort_counter.get("EXACT_GAP", 0), len(perf_rows)),
            "box_converted_rows": _rate(cohort_counter.get("BOX_CONVERTED", 0), len(perf_rows)),
            "vt_converted_rows": _rate(cohort_counter.get("VT_CONVERTED", 0), len(perf_rows)),
            "preserved_rows": _rate(cohort_counter.get("PRESERVED", 0), len(perf_rows)),
        },
    }

    examples = {
        "priority_rows": _sorted_examples(output_rows, limit=8),
        "gap_rows": _sorted_examples(
            [row for row in output_rows if "GAP" in str(row.get("primary_cohort") or "")],
            limit=8,
        ),
        "converted_rows": _sorted_examples(
            [row for row in output_rows if str(row.get("primary_cohort") or "").endswith("CONVERTED")],
            limit=8,
        ),
    }

    interpretation = [
        "Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.",
        "Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.",
        "Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.",
    ]
    if cohort_counter.get("BOX_GAP", 0):
        interpretation.append(
            f"Current window produced `{cohort_counter.get('BOX_GAP', 0)}` explicit box-gap rows worth preserving for translator study."
        )
    if cohort_counter.get("PRESERVED", 0):
        interpretation.append(
            f"Preserved-not-budgeted rows (`{cohort_counter.get('PRESERVED', 0)}`) remain useful as a reserve cohort for later combo/budget design."
        )

    return {
        "metadata": {
            "window_root": safe_rel(window_root),
            "window_dates": window_root.name.replace("WINDOW_", "").split("_to_") if "_to_" in window_root.name else [],
            "performance_gap_ledger": safe_rel(paths["ledger"]),
            "hit_roster": safe_rel(paths["hits"]),
            "frontier_cases": safe_rel(paths["frontier"]),
        },
        "summary": summary,
        "examples": examples,
        "interpretation": interpretation,
        "rows": output_rows,
    }


def _render_markdown(payload: Dict[str, Any], *, csv_path: Path) -> str:
    summary = payload.get("summary") or {}
    examples = payload.get("examples") or {}
    lines: List[str] = []
    lines.append("# Analysis Arena Translator-Learning Ledger")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(f"- Window root: `{payload.get('metadata', {}).get('window_root', '')}`")
    dates = payload.get("metadata", {}).get("window_dates") or []
    if len(dates) == 2:
        lines.append(f"- Dates: `{dates[0]}` to `{dates[1]}`")
    lines.append(f"- Winner-event denominator: `{summary.get('winner_events', 0)}`")
    lines.append(f"- Translator-learning rows: `{summary.get('translator_rows', 0)}`")
    lines.append(f"- CSV roster: `{safe_rel(csv_path)}`")
    lines.append("")
    lines.append("## 2. Cohort Counts")
    lines.append("")
    for key, count in (summary.get("cohort_counts") or {}).items():
        lines.append(f"- {key}: `{count}`")
    lines.append("")
    lines.append("## 3. Signature Mix")
    lines.append("")
    lines.append(
        "- Arena finalist signatures: "
        + (", ".join(f"`{k}` x{v}" for k, v in (summary.get("finalist_signature_counts") or {}).items()) or "_none_")
    )
    lines.append(
        "- Frontier signatures: "
        + (", ".join(f"`{k}` x{v}" for k, v in (summary.get("frontier_signature_counts") or {}).items()) or "_none_")
    )
    lines.append(
        "- Top states in the teaching cohort: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in (summary.get("top_states") or [])) or "_none_")
    )
    lines.append("")
    lines.append("## 4. Priority Examples")
    lines.append("")
    for row in examples.get("priority_rows") or []:
        lines.append(
            f"- `{row.get('date', '')}` `{row.get('state', '')}` `{row.get('period', '')}` winner=`{row.get('winner', '')}` "
            f"rank=`{row.get('board_rank', 0)}` cohort=`{row.get('primary_cohort', '')}` "
            f"frontier=`{row.get('frontier_signature_type', '')}` sig=`{row.get('arena_final_candidate_signature', '')}` "
            f"double=`{row.get('double_context_strength', '') or '-'}`"
        )
    lines.append("")
    lines.append("## 5. Practical Read")
    lines.append("")
    for bullet in payload.get("interpretation") or []:
        lines.append(f"- {bullet}")
    return "\n".join(lines) + "\n"


def _write_csv(path: Path, rows: List[Dict[str, str]], *, force: bool) -> None:
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


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    defaults = _default_paths(window_root)
    out_md = _resolve_path(args.out_md) if args.out_md else defaults["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else defaults["json"]
    out_csv = _resolve_path(args.out_csv) if args.out_csv else defaults["csv"]

    payload = build_payload(window_root)
    payload["schema_version"] = "analysis_arena_translator_learning_ledger/v1"
    payload["csv_path"] = safe_rel(out_csv)

    _write_csv(out_csv, payload.get("rows") or [], force=args.force)
    _write_json(out_json, payload, force=args.force)
    _write_text(out_md, _render_markdown(payload, csv_path=out_csv), force=args.force)
    print(f"Wrote: {safe_rel(out_csv)}")
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
