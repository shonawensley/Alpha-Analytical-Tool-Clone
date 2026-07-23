#!/usr/bin/env python3
"""Create a pure Analysis Arena finalist/candidate scorecard for a completed window."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import read_json, safe_rel
from scripts.tools.brain2_rank_contract import RANK_INTEGRITY_INVALID_STATIC_ORDER


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument("--frontier-json", default="", help="Optional frontier harness JSON path.")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
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
        "frontier": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
        "md": window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
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


def _rate(count: int, den: int) -> float:
    return count / den if den else 0.0


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _as_int(value: Any) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return 0


def _boxlike_event(row: Dict[str, str]) -> bool:
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


def _vt_like_event(row: Dict[str, str]) -> bool:
    return any(_truthy(row.get(key)) for key in ("arena_primary_vt", "sandbox_vt_seed"))


def _any_candidate_like_event(row: Dict[str, str]) -> bool:
    return _boxlike_event(row) or _vt_like_event(row) or _truthy(row.get("arena_exact_signal"))


def _finalist_bucket(row: Dict[str, str]) -> str:
    text = str(row.get("arena_final_candidate_signature") or "").strip()
    return text or "UNSPECIFIED"


def _hit_primary_class(row: Dict[str, str]) -> str:
    text = str(row.get("hit_primary_class") or "").strip()
    if text:
        return text
    if _truthy(row.get("play_straight_hit")):
        return "STRAIGHT"
    if _truthy(row.get("play_box_strict_hit")):
        return "STRICT_BOXED"
    if _truthy(row.get("play_box_any_hit")):
        return "CANONICAL_BOX"
    if _truthy(row.get("play_vtrac_only_hit")):
        return "VTRAC_ONLY"
    return "UNCLASSIFIED"


def _sorted_examples(rows: Iterable[Dict[str, str]], *, limit: int = 5) -> List[Dict[str, Any]]:
    def sort_key(row: Dict[str, str]) -> tuple[int, str, str]:
        score = _as_int(row.get("arena_final_candidate_signature_score"))
        return (
            -score,
            str(row.get("date") or ""),
            str(row.get("state_key") or row.get("state") or ""),
        )

    out: List[Dict[str, Any]] = []
    for row in sorted(rows, key=sort_key)[:limit]:
        out.append(
            {
                "date": row.get("date", ""),
                "state": row.get("state_key") or row.get("state") or "",
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "display_order": row.get("display_order", ""),
                "analytical_rank": row.get("analytical_rank", "") if _truthy(row.get("rank_signal_valid")) else "",
                "legacy_static_rank": row.get("legacy_static_rank", ""),
                "arena_final_candidate_signature": row.get("arena_final_candidate_signature", ""),
                "arena_final_candidate_signature_score": _as_int(row.get("arena_final_candidate_signature_score")),
                "hit_primary_class": _hit_primary_class(row),
                "arena_box_signal": _truthy(row.get("arena_box_signal")),
                "arena_exact_signal": _truthy(row.get("arena_exact_signal")),
                "sandbox_box_seed": _truthy(row.get("sandbox_box_seed")),
                "sandbox_exact_seed": _truthy(row.get("sandbox_exact_seed")),
                "sandbox_vt_seed": _truthy(row.get("sandbox_vt_seed")),
                "arena_primary_box": _truthy(row.get("arena_primary_box")),
                "arena_primary_vt": _truthy(row.get("arena_primary_vt")),
                "play_card_any_box": _truthy(row.get("play_card_any_box")),
                "play_card_any_exact": _truthy(row.get("play_card_any_exact")),
            }
        )
    return out


def _metric(count: int, den: int) -> Dict[str, Any]:
    return {"count": count, "denominator": den, "rate": _rate(count, den)}


def build_payload(window_root: Path, *, frontier_json: Path | None = None) -> Dict[str, Any]:
    paths = _default_paths(window_root)
    ledger_rows = _read_csv_rows(paths["ledger"])
    hit_rows = _read_csv_rows(paths["hits"])
    frontier_payload: Dict[str, Any] = {}
    frontier_path = frontier_json or paths["frontier"]
    if frontier_path.exists():
        raw = read_json(frontier_path)
        if isinstance(raw, dict):
            frontier_payload = raw

    winner_events = len(ledger_rows)
    boxlike_events = [row for row in ledger_rows if _boxlike_event(row)]
    vt_like_events = [row for row in ledger_rows if _vt_like_event(row)]
    any_candidate_events = [row for row in ledger_rows if _any_candidate_like_event(row)]
    explicit_box_events = [row for row in ledger_rows if _truthy(row.get("arena_box_signal"))]
    explicit_exact_events = [row for row in ledger_rows if _truthy(row.get("arena_exact_signal"))]
    opportunity_gaps = [row for row in ledger_rows if _truthy(row.get("opportunity_gap_box"))]
    rank_evaluable = any(
        _truthy(row.get("rank_signal_valid"))
        and bool(str(row.get("analytical_rank") or row.get("board_rank") or "").strip())
        for row in ledger_rows
    )

    hit_count = len(hit_rows)
    finalist_supported_hits = [row for row in hit_rows if _finalist_bucket(row) != "CONTROL_ARM_ONLY_CATCH"]
    clear_or_partial_hits = [
        row
        for row in hit_rows
        if _finalist_bucket(row) in {"CLEAR_ARENA_FINALIST", "PARTIAL_ARENA_FINALIST"}
    ]
    strict_box_hits = [row for row in hit_rows if _truthy(row.get("play_box_strict_hit"))]
    straight_hits = [row for row in hit_rows if _truthy(row.get("play_straight_hit"))]
    strict_box_with_finalist = [row for row in strict_box_hits if _finalist_bucket(row) != "CONTROL_ARM_ONLY_CATCH"]
    straight_with_finalist = [row for row in straight_hits if _finalist_bucket(row) != "CONTROL_ARM_ONLY_CATCH"]
    boxlike_hits = [row for row in hit_rows if _boxlike_event(row)]
    vt_like_hits = [row for row in hit_rows if _vt_like_event(row)]

    by_hit_class: Dict[str, Dict[str, Any]] = {}
    by_class_rows: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in hit_rows:
        by_class_rows[_hit_primary_class(row)].append(row)
    for hit_class, rows in sorted(by_class_rows.items()):
        by_hit_class[hit_class] = {
            "count": len(rows),
            "finalist_supported": _metric(
                sum(_finalist_bucket(row) != "CONTROL_ARM_ONLY_CATCH" for row in rows),
                len(rows),
            ),
            "clear_or_partial": _metric(
                sum(_finalist_bucket(row) in {"CLEAR_ARENA_FINALIST", "PARTIAL_ARENA_FINALIST"} for row in rows),
                len(rows),
            ),
            "boxlike_support": _metric(sum(_boxlike_event(row) for row in rows), len(rows)),
            "vt_like_support": _metric(sum(_vt_like_event(row) for row in rows), len(rows)),
        }

    gap_examples = _sorted_examples(opportunity_gaps)
    candidate_examples = _sorted_examples(
        [
            row
            for row in hit_rows
            if _finalist_bucket(row) != "CONTROL_ARM_ONLY_CATCH" and (_boxlike_event(row) or _vt_like_event(row))
        ],
        limit=8,
    )

    frontier_signatures = ((frontier_payload.get("signature_mix") or {}).get("signature_counts")) or {}
    frontier_promotions = frontier_payload.get("promotion_queue") or []

    event_layer = {
        "winner_events": winner_events,
        "any_candidate_like_events": _metric(len(any_candidate_events), winner_events),
        "vt_like_events": _metric(len(vt_like_events), winner_events),
        "boxlike_events": _metric(len(boxlike_events), winner_events),
        "explicit_arena_box_events": _metric(len(explicit_box_events), winner_events),
        "explicit_arena_exact_events": _metric(len(explicit_exact_events), winner_events),
    }
    hit_layer = {
        "credited_hits": hit_count,
        "finalist_supported_hits": _metric(len(finalist_supported_hits), hit_count),
        "clear_or_partial_hits": _metric(len(clear_or_partial_hits), hit_count),
        "strict_box_hits": _metric(len(strict_box_hits), hit_count),
        "strict_box_with_finalist_support": _metric(len(strict_box_with_finalist), len(strict_box_hits)),
        "straight_hits": _metric(len(straight_hits), hit_count),
        "straight_with_finalist_support": _metric(len(straight_with_finalist), len(straight_hits)),
        "boxlike_hits": _metric(len(boxlike_hits), hit_count),
        "vt_like_hits": _metric(len(vt_like_hits), hit_count),
        "signature_buckets": dict(Counter(_finalist_bucket(row) for row in hit_rows)),
        "by_hit_class": by_hit_class,
    }
    opportunity_layer = {
        "opportunity_gap_box_rows": _metric(len(opportunity_gaps), winner_events),
        "gap_rows_with_explicit_arena_box": _metric(
            sum(_truthy(row.get("arena_box_signal")) for row in opportunity_gaps),
            len(opportunity_gaps),
        ),
        "gap_rows_with_sandbox_box_seed": _metric(
            sum(_truthy(row.get("sandbox_box_seed")) for row in opportunity_gaps),
            len(opportunity_gaps),
        ),
        "gap_rows_with_arena_primary_box": _metric(
            sum(_truthy(row.get("arena_primary_box")) for row in opportunity_gaps),
            len(opportunity_gaps),
        ),
        "gap_rows_ranked_top5": (
            _metric(
                sum(0 < _as_int(row.get("analytical_rank") or row.get("board_rank")) <= 5 for row in opportunity_gaps),
                len(opportunity_gaps),
            )
            if rank_evaluable
            else {
                "status": "NOT_EVALUABLE",
                "evaluable": False,
                "reason": RANK_INTEGRITY_INVALID_STATIC_ORDER,
                "count": None,
                "denominator": None,
                "rate": None,
            }
        ),
    }

    interpretation = [
        (
            "The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer."
            if event_layer["vt_like_events"]["count"] > event_layer["boxlike_events"]["count"]
            else "The arena is currently preserving box-like candidate evidence at a similar scale to finalist/VTRAC territory."
        ),
        (
            "Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone."
            if hit_layer["finalist_supported_hits"]["count"] > 0
            else "Converted hits are still leaning too hard on control-arm-only expression."
        ),
        (
            "The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert."
            if opportunity_gaps
            else "No opportunity-gap box rows were recorded in this window."
        ),
    ]

    return {
        "schema_version": "analysis_arena_pure_finalist_scorecard/v1",
        "metadata": {
            "window_root": safe_rel(window_root),
            "ledger_path": safe_rel(paths["ledger"]),
            "hit_roster_path": safe_rel(paths["hits"]),
            "frontier_json_path": safe_rel(frontier_path),
            "winner_events": winner_events,
            "credited_hits": hit_count,
            "rank_evaluation": {
                "status": "EVALUABLE" if rank_evaluable else "NOT_EVALUABLE",
                "evaluable": rank_evaluable,
                "reason": None if rank_evaluable else RANK_INTEGRITY_INVALID_STATIC_ORDER,
            },
        },
        "event_layer": event_layer,
        "hit_layer": hit_layer,
        "opportunity_layer": opportunity_layer,
        "frontier_context": {
            "signature_counts": frontier_signatures,
            "promotion_queue": frontier_promotions,
        },
        "examples": {
            "candidate_supported_hits": candidate_examples,
            "opportunity_gap_examples": gap_examples,
        },
        "interpretation": interpretation,
    }


def _render_markdown(payload: Dict[str, Any]) -> str:
    meta = payload["metadata"]
    event_layer = payload["event_layer"]
    hit_layer = payload["hit_layer"]
    opp = payload["opportunity_layer"]
    frontier = payload["frontier_context"]
    examples = payload["examples"]
    lines: List[str] = []
    lines.append("# Pure Arena Finalist / Candidate Scorecard")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(f"- Window root: `{meta['window_root']}`")
    lines.append(f"- Winner-event denominator: `{meta['winner_events']}`")
    lines.append(f"- Credited-hit denominator: `{meta['credited_hits']}`")
    lines.append(f"- Performance ledger: `{meta['ledger_path']}`")
    lines.append(f"- Hit roster: `{meta['hit_roster_path']}`")
    lines.append("")
    lines.append("## 2. Event-Level Finalist Territory")
    lines.append("")
    lines.append(
        f"- Any candidate-like arena evidence: `{event_layer['any_candidate_like_events']['count']}/{event_layer['any_candidate_like_events']['denominator']}` "
        f"({_pct(event_layer['any_candidate_like_events']['rate'])})"
    )
    lines.append(
        f"- VT-like finalist territory (`arena_primary_vt` or `sandbox_vt_seed`): `{event_layer['vt_like_events']['count']}/{event_layer['vt_like_events']['denominator']}` "
        f"({_pct(event_layer['vt_like_events']['rate'])})"
    )
    lines.append(
        f"- Box-like candidate territory (`arena_box_signal` / sandbox box / arena primary box / preserved): `{event_layer['boxlike_events']['count']}/{event_layer['boxlike_events']['denominator']}` "
        f"({_pct(event_layer['boxlike_events']['rate'])})"
    )
    lines.append(
        f"- Explicit arena box / exact signals: `{event_layer['explicit_arena_box_events']['count']}` / `{event_layer['explicit_arena_exact_events']['count']}`"
    )
    lines.append("")
    lines.append("## 3. Converted-Hit Arena Support")
    lines.append("")
    lines.append(
        f"- Credited hits with non-control-arm finalist signature: `{hit_layer['finalist_supported_hits']['count']}/{hit_layer['finalist_supported_hits']['denominator']}` "
        f"({_pct(hit_layer['finalist_supported_hits']['rate'])})"
    )
    lines.append(
        f"- Credited hits with `CLEAR` or `PARTIAL` arena finalist signature: `{hit_layer['clear_or_partial_hits']['count']}/{hit_layer['clear_or_partial_hits']['denominator']}` "
        f"({_pct(hit_layer['clear_or_partial_hits']['rate'])})"
    )
    lines.append(
        f"- Straight hits with finalist support: `{hit_layer['straight_with_finalist_support']['count']}/{hit_layer['straight_with_finalist_support']['denominator']}` "
        f"({_pct(hit_layer['straight_with_finalist_support']['rate'])})"
    )
    lines.append(
        f"- Strict box hits with finalist support: `{hit_layer['strict_box_with_finalist_support']['count']}/{hit_layer['strict_box_with_finalist_support']['denominator']}` "
        f"({_pct(hit_layer['strict_box_with_finalist_support']['rate'])})"
    )
    lines.append(
        f"- Hits with box-like arena support: `{hit_layer['boxlike_hits']['count']}/{hit_layer['boxlike_hits']['denominator']}` "
        f"({_pct(hit_layer['boxlike_hits']['rate'])})"
    )
    lines.append(
        f"- Hits with VT-like arena support: `{hit_layer['vt_like_hits']['count']}/{hit_layer['vt_like_hits']['denominator']}` "
        f"({_pct(hit_layer['vt_like_hits']['rate'])})"
    )
    lines.append(
        "- Finalist signature buckets: "
        + (
            ", ".join(
                f"`{key}` x{value}" for key, value in sorted(hit_layer["signature_buckets"].items())
            )
            or "_none_"
        )
    )
    lines.append("")
    lines.append("| Hit Class | Count | Finalist Support | Clear/Partial | Box-Like Support | VT-Like Support |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for hit_class, row in hit_layer["by_hit_class"].items():
        lines.append(
            f"| `{hit_class}` | {row['count']} | "
            f"{_pct(row['finalist_supported']['rate'])} | "
            f"{_pct(row['clear_or_partial']['rate'])} | "
            f"{_pct(row['boxlike_support']['rate'])} | "
            f"{_pct(row['vt_like_support']['rate'])} |"
        )
    lines.append("")
    lines.append("## 4. Opportunity-Gap Box Layer")
    lines.append("")
    lines.append(
        f"- Opportunity-gap box rows: `{opp['opportunity_gap_box_rows']['count']}/{opp['opportunity_gap_box_rows']['denominator']}` "
        f"({_pct(opp['opportunity_gap_box_rows']['rate'])})"
    )
    lines.append(
        f"- Gap rows with explicit arena box signal: `{opp['gap_rows_with_explicit_arena_box']['count']}/{opp['gap_rows_with_explicit_arena_box']['denominator']}` "
        f"({_pct(opp['gap_rows_with_explicit_arena_box']['rate'])})"
    )
    lines.append(
        f"- Gap rows with sandbox box seed: `{opp['gap_rows_with_sandbox_box_seed']['count']}/{opp['gap_rows_with_sandbox_box_seed']['denominator']}` "
        f"({_pct(opp['gap_rows_with_sandbox_box_seed']['rate'])})"
    )
    if opp["gap_rows_ranked_top5"].get("evaluable") is False:
        lines.append("- Gap rows ranked top5: `NOT_EVALUABLE` (`INVALID_STATIC_ORDER`).")
    else:
        lines.append(
            f"- Gap rows ranked top5: `{opp['gap_rows_ranked_top5']['count']}/{opp['gap_rows_ranked_top5']['denominator']}` "
            f"({_pct(opp['gap_rows_ranked_top5']['rate'])})"
        )
    lines.append("")
    if frontier["signature_counts"]:
        lines.append("## 5. Frontier Corroboration")
        lines.append("")
        lines.append(
            "- Frontier signature mix: "
            + ", ".join(f"`{key}` x{value}" for key, value in frontier["signature_counts"].items())
        )
        if frontier["promotion_queue"]:
            promotion_names = [
                f"`{item.get('signal') or item.get('theme') or '-'}`"
                for item in frontier["promotion_queue"][:4]
            ]
            lines.append(
                "- Frontier promotion themes: "
                + ", ".join(promotion_names)
            )
        lines.append("")
    lines.append("## 6. Notable Cases")
    lines.append("")
    lines.append("- Candidate-supported hit examples:")
    for row in examples["candidate_supported_hits"]:
        lines.append(
            f"  - `{row['date']}` `{row['state']}` `{row['period']}` winner `{row['winner']}` "
            f"sig=`{row['arena_final_candidate_signature']}` "
            f"boxlike=`{row['arena_box_signal'] or row['sandbox_box_seed'] or row['arena_primary_box']}` "
            f"vtlike=`{row['sandbox_vt_seed'] or row['arena_primary_vt']}`"
        )
    lines.append("- Opportunity-gap examples:")
    for row in examples["opportunity_gap_examples"]:
        lines.append(
            f"  - `{row['date']}` `{row['state']}` `{row['period']}` winner `{row['winner']}` "
            f"arena_box=`{row['arena_box_signal']}` sandbox_box=`{row['sandbox_box_seed']}`"
        )
    lines.append("")
    lines.append("## 7. Practical Read")
    lines.append("")
    for bullet in payload["interpretation"]:
        lines.append(f"- {bullet}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    defaults = _default_paths(window_root)
    frontier_json = _resolve_path(args.frontier_json) if args.frontier_json else defaults["frontier"]
    out_md = _resolve_path(args.out_md) if args.out_md else defaults["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else defaults["json"]

    payload = build_payload(window_root, frontier_json=frontier_json)
    _write_json(out_json, payload, force=args.force)
    _write_text(out_md, _render_markdown(payload), force=args.force)
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
