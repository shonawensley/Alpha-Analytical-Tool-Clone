#!/usr/bin/env python3
"""Create a cross-window rollup for completed Analysis Arena comparison windows."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import read_json, safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-root", default=str(DEFAULT_RUNS2_ROOT), help="RUNS_2 root to scan for completed windows.")
    ap.add_argument("--window-root", action="append", default=[], help="Optional explicit window roots. Can be repeated.")
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


def _default_paths() -> Dict[str, Path]:
    stem = "AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP"
    return {
        "md": DEFAULT_FINAL_DOCS / f"{stem}.md",
        "json": DEFAULT_FINAL_DOCS / f"{stem}.json",
        "csv": DEFAULT_FINAL_DOCS / f"{stem}.csv",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _rate_value(value: Any) -> float:
    if isinstance(value, dict):
        rate = value.get("rate", 0.0)
        if isinstance(rate, str) and rate.endswith("%"):
            try:
                return float(rate[:-1]) / 100.0
            except ValueError:
                return 0.0
        try:
            return float(rate or 0.0)
        except Exception:
            return 0.0
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _load_window_payload(path: Path) -> Dict[str, Any]:
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise SystemExit(f"Expected JSON object: {path}")
    return payload


def _discover_windows(runs2_root: Path) -> List[Path]:
    windows: List[Path] = []
    for path in sorted(runs2_root.glob("WINDOW_*")):
        if "__PREALIGN_SNAPSHOT" in path.name:
            continue
        required = [
            path / f"{path.name}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
            path / f"{path.name}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json",
            path / f"{path.name}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
            path / f"{path.name}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
            path / f"{path.name}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
        ]
        if all(item.exists() for item in required):
            windows.append(path)
    return windows


def _window_row(window_root: Path) -> Dict[str, Any]:
    stem = window_root.name
    perf = _load_window_payload(window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json")
    hits = _load_window_payload(window_root / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json")
    frontier = _load_window_payload(window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json")
    pure = _load_window_payload(window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json")
    translator = _load_window_payload(window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json")

    summary_counts = perf.get("summary_counts") or {}
    summary_rates = perf.get("summary_rates") or {}
    hit_inventory = hits.get("hit_inventory") or {}
    ranking = hits.get("ranking") or {}
    signature_mix = (frontier.get("signature_mix") or {}).get("signature_counts") or {}
    event_layer = pure.get("event_layer") or {}
    hit_layer = pure.get("hit_layer") or {}
    opp_layer = pure.get("opportunity_layer") or {}
    translator_summary = translator.get("summary") or {}
    winner_events = int(summary_counts.get("winner_events", 0) or 0)
    frontier_total = sum(int(v) for v in signature_mix.values()) or 0

    def pct_count_rate(block: Dict[str, Any]) -> float:
        if not isinstance(block, dict):
            return 0.0
        return float(block.get("rate", 0.0) or 0.0)

    return {
        "window": stem.replace("WINDOW_", ""),
        "window_root": safe_rel(window_root),
        "day_count": int((perf.get("metadata") or {}).get("day_count", 0) or 0),
        "winner_events": winner_events,
        "credited_hits": int((hits.get("metadata") or {}).get("credited_hits", 0) or 0),
        "candidate_like_event_rate": pct_count_rate(event_layer.get("any_candidate_like_events") or {}),
        "vt_like_event_rate": pct_count_rate(event_layer.get("vt_like_events") or {}),
        "boxlike_event_rate": pct_count_rate(event_layer.get("boxlike_events") or {}),
        "finalist_supported_hit_rate": pct_count_rate(hit_layer.get("finalist_supported_hits") or {}),
        "straight_finalist_support_rate": pct_count_rate(hit_layer.get("straight_with_finalist_support") or {}),
        "strict_box_finalist_support_rate": pct_count_rate(hit_layer.get("strict_box_with_finalist_support") or {}),
        "opportunity_gap_box_rate": _rate_value(summary_rates.get("opportunity_gap_box", 0.0)),
        "play_card_any_box_rate": _rate_value(summary_rates.get("play_card_any_box", 0.0)),
        "candidate_universe_box_rate": _rate_value(summary_rates.get("cu_box", 0.0)),
        "candidate_universe_exact_rate": _rate_value(summary_rates.get("cu_exact", 0.0)),
        "top_primary_target_rate": _rate_value(summary_rates.get("top_primary_target", 0.0)),
        "median_rank_all_hits": float(ranking.get("median_rank_all_hits", 0.0) or 0.0),
        "median_rank_high_conviction": float(ranking.get("median_rank_high_conviction", 0.0) or 0.0),
        "strict_box_hits": int(hit_inventory.get("strict_box_hits", 0) or 0),
        "straight_hits": int(hit_inventory.get("straight_hits", 0) or 0),
        "vtrac_only_hits": int(hit_inventory.get("vtrac_only_hits", 0) or 0),
        "translator_rows": int(translator_summary.get("translator_rows", 0) or 0),
        "translator_box_gap_rows": int((translator_summary.get("cohort_counts") or {}).get("BOX_GAP", 0) or 0),
        "translator_preserved_rows": int((translator_summary.get("cohort_counts") or {}).get("PRESERVED", 0) or 0),
        "frontier_hidden_rate": (int(signature_mix.get("HIDDEN_COMPRESSED_FRONTIER", 0) or 0) / frontier_total) if frontier_total else 0.0,
        "frontier_feeder_rate": (int(signature_mix.get("FEEDER_TO_FRONTIER", 0) or 0) / frontier_total) if frontier_total else 0.0,
        "frontier_vtrac_rate": (int(signature_mix.get("VTRAC_FRONTIER", 0) or 0) / frontier_total) if frontier_total else 0.0,
        "frontier_literal_rate": (int(signature_mix.get("LITERAL_FRONTIER", 0) or 0) / frontier_total) if frontier_total else 0.0,
        "frontier_top_signature": max(signature_mix.items(), key=lambda item: int(item[1]))[0] if signature_mix else "",
        "gap_rows_with_explicit_arena_box_rate": pct_count_rate(opp_layer.get("gap_rows_with_explicit_arena_box") or {}),
    }


def build_payload(window_roots: List[Path]) -> Dict[str, Any]:
    rows = [_window_row(path) for path in window_roots]
    windows = len(rows)
    total_events = sum(int(row["winner_events"]) for row in rows)
    total_hits = sum(int(row["credited_hits"]) for row in rows)

    def avg(key: str) -> float:
        return sum(float(row[key]) for row in rows) / windows if windows else 0.0

    summary = {
        "window_count": windows,
        "winner_events": total_events,
        "credited_hits": total_hits,
        "average_candidate_like_event_rate": avg("candidate_like_event_rate"),
        "average_finalist_supported_hit_rate": avg("finalist_supported_hit_rate"),
        "average_play_card_any_box_rate": avg("play_card_any_box_rate"),
        "average_top_primary_target_rate": avg("top_primary_target_rate"),
        "average_opportunity_gap_box_rate": avg("opportunity_gap_box_rate"),
        "average_translator_box_gap_rows": avg("translator_box_gap_rows"),
    }
    interpretation = [
        "Use this rollup to compare repeated evidence across windows before changing Brain 2 or the future translator.",
        "Treat mixed replay uplift as a real result: some windows improve clearly, some stay flat, and some regress slightly.",
        "If candidate-like and finalist-supported rates stay high while realized play-card box rates stay low, the bottleneck is still downstream expression.",
    ]
    return {
        "metadata": {
            "runs2_root": safe_rel(DEFAULT_RUNS2_ROOT),
            "windows": [safe_rel(path) for path in window_roots],
        },
        "summary": summary,
        "rows": rows,
        "interpretation": interpretation,
    }


def _write_csv(path: Path, rows: List[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _render_markdown(payload: Dict[str, Any], *, csv_path: Path) -> str:
    summary = payload.get("summary") or {}
    rows = payload.get("rows") or []
    lines: List[str] = []
    lines.append("# Analysis Arena Cross-Window Rollup")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append("")
    lines.append(f"- Windows reviewed: `{summary.get('window_count', 0)}`")
    lines.append(f"- Winner events: `{summary.get('winner_events', 0)}`")
    lines.append(f"- Credited hits: `{summary.get('credited_hits', 0)}`")
    lines.append(f"- CSV roster: `{safe_rel(csv_path)}`")
    lines.append("")
    lines.append("## 2. Average Rates")
    lines.append("")
    lines.append(f"- Candidate-like event coverage: `{_pct(float(summary.get('average_candidate_like_event_rate', 0.0)))}`")
    lines.append(f"- Finalist-supported hit rate: `{_pct(float(summary.get('average_finalist_supported_hit_rate', 0.0)))}`")
    lines.append(f"- Play Card any-box rate: `{_pct(float(summary.get('average_play_card_any_box_rate', 0.0)))}`")
    lines.append(f"- Top-primary-target rate: `{_pct(float(summary.get('average_top_primary_target_rate', 0.0)))}`")
    lines.append(f"- Opportunity-gap box rate: `{_pct(float(summary.get('average_opportunity_gap_box_rate', 0.0)))}`")
    lines.append("")
    lines.append("## 3. Window Table")
    lines.append("")
    lines.append("| Window | Events | Cand. | Finalist Hits | Play Box | Top Primary | Gap Box | Translator Box Gaps | Top Frontier |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row.get("window", ""),
                    str(row.get("winner_events", 0)),
                    _pct(float(row.get("candidate_like_event_rate", 0.0))),
                    _pct(float(row.get("finalist_supported_hit_rate", 0.0))),
                    _pct(float(row.get("play_card_any_box_rate", 0.0))),
                    _pct(float(row.get("top_primary_target_rate", 0.0))),
                    _pct(float(row.get("opportunity_gap_box_rate", 0.0))),
                    str(row.get("translator_box_gap_rows", 0)),
                    row.get("frontier_top_signature", ""),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## 4. Practical Read")
    lines.append("")
    for bullet in payload.get("interpretation") or []:
        lines.append(f"- {bullet}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    defaults = _default_paths()
    runs2_root = _resolve_path(args.runs2_root)
    explicit_windows = [_resolve_path(value) for value in (args.window_root or [])]
    window_roots = explicit_windows or _discover_windows(runs2_root)
    if not window_roots:
        raise SystemExit("No completed windows found for cross-window rollup.")

    out_md = _resolve_path(args.out_md) if args.out_md else defaults["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else defaults["json"]
    out_csv = _resolve_path(args.out_csv) if args.out_csv else defaults["csv"]

    payload = build_payload(window_roots)
    payload["schema_version"] = "analysis_arena_cross_window_rollup/v1"
    payload["csv_path"] = safe_rel(out_csv)

    _write_csv(out_csv, payload.get("rows") or [], force=args.force)
    _write_json(out_json, payload, force=args.force)
    _write_text(out_md, _render_markdown(payload, csv_path=out_csv), force=args.force)
    print(f"Wrote: {safe_rel(out_csv)}")
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
