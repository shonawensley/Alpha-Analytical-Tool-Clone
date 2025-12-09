#!/usr/bin/env python3
"""
Control Center sanity snapshot

Read-only helper that:
- Checks freshness between the Aux draws CSV and Combined_Combined.csv tables.
- Computes draws-since-double per state (newest-first CSVs).
- Optionally tags whether the provided results file contains a double draw.

Outputs a JSON + CSV summary under reports/control_center/.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Sequence, Dict, Any

ROOT = Path(__file__).resolve().parents[2]
DRAW_CLEAN_DIR = ROOT / "data" / "cleaned" / "draws"
TABLES_DIR = ROOT / "data" / "outputs" / "tables"
REPORT_DIR = ROOT / "reports" / "control_center"
CONTROL_CENTER_MD = REPORT_DIR / "control_center.md"
ALERT_SCHEMA_PATH = REPORT_DIR / "alert_schema.json"
DEFAULT_STATE_MAP_PATH = REPORT_DIR / "state_map.json"

# Ensure project root on sys.path for modules imports (VTRAC reference)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Lazy import to keep top-level fast; guarded in main
vtrac_reference = None  # type: ignore

def _read_draws(csv_path: Path) -> list[str]:
    """Return newest-first list of 3-char strings."""
    rows: list[str] = []
    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        for row in reader:
            for token in row:
                token = token.strip()
                if len(token) == 3 and token.isdigit():
                    rows.append(token.zfill(3))
                    break
    return rows


def _is_double(draw: str) -> bool:
    """True if draw contains at least one repeated digit (double or triple)."""
    return len(set(draw)) <= 2


def _draws_since_double(draws: Sequence[str]) -> Optional[int]:
    for idx, d in enumerate(draws):
        if _is_double(d):
            return idx
    return None


def _read_tables_latest(table_path: Path) -> tuple[Optional[str], Optional[str]]:
    """
    Attempt to read the latest Combined table row (Set1/Draw1 draw_data)
    and return (col1, col2). If parsing fails, returns (None, None).
    """
    if not table_path.exists():
        return None, None
    with table_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        col1_name = None
        col2_name = None
        for name in reader.fieldnames or []:
            lower = name.lower()
            if "col1" == lower or lower.endswith("col1"):
                col1_name = name
            if "col2" == lower or lower.endswith("col2"):
                col2_name = name
        for row in reader:
            rowtype = row.get("RowType") or row.get("rowtype") or row.get("Rowtype")
            draw_num = row.get("Draw") or row.get("DrawNum") or row.get("draw")
            if (rowtype or "").lower() == "draw_data" and (draw_num or "1") == "1":
                v1 = row.get(col1_name, "").strip().zfill(3) if col1_name else None
                v2 = row.get(col2_name, "").strip().zfill(3) if col2_name else None
                return v1 or None, v2 or None
        # fallback: first data row
        fh.seek(0)
        reader2 = csv.reader(fh)
        next(reader2, None)  # header
        for row in reader2:
            if len(row) >= 2:
                return row[-2].strip().zfill(3), row[-1].strip().zfill(3)
    return None, None


def _parse_results_file(results_path: Optional[Path]) -> list[str]:
    """Return list of 3-digit tokens found in results file."""
    if not results_path or not results_path.exists():
        return []
    tokens: list[str] = []
    with results_path.open(encoding="utf-8") as fh:
        for line in fh:
            for part in line.replace(",", " ").split():
                part = part.strip()
                if len(part) == 3 and part.isdigit():
                    tokens.append(part.zfill(3))
    return tokens


def _norm_state(name: str) -> str:
    """Normalize state label for loose matching (strip digits/space/underscore, lower)."""
    return "".join(ch for ch in name.lower() if ch.isalpha())


def _parse_results_by_state(results_path: Optional[Path]) -> Dict[str, Dict[str, str]]:
    """
    Parse a structured results file (state rows with Midday/Evening columns).
    Returns {normalized_state: {"Midday": "123", "Evening": "456"}}.
    """
    if not results_path or not results_path.exists():
        return {}
    rows: Dict[str, Dict[str, str]] = {}
    with results_path.open(encoding="utf-8") as fh:
        header_seen = False
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            if not header_seen:
                # Skip until header row
                if line.lower().startswith("state"):
                    header_seen = True
                continue
            parts = [p.strip() for p in line.split("\t")]
            if len(parts) < 3:
                continue
            state_raw, midday_raw, eve_raw = parts[0], parts[1], parts[2]
            if not state_raw:
                continue
            norm_state = _norm_state(state_raw)
            entry: Dict[str, str] = {}
            if midday_raw and len(midday_raw) == 3 and midday_raw.isdigit():
                entry["Midday"] = midday_raw.zfill(3)
            if eve_raw and len(eve_raw) == 3 and eve_raw.isdigit():
                entry["Evening"] = eve_raw.zfill(3)
            if entry:
                rows[norm_state] = entry
    return rows


def _build_state_map(results_by_state: Dict[str, Dict[str, str]], draws_paths: list[Path]) -> Dict[str, str]:
    """
    Build a map from normalized state token -> draws filename stem for better matching.
    """
    from collections import defaultdict

    stem_map: Dict[str, str] = {}
    norm_to_candidates: Dict[str, set[str]] = defaultdict(set)
    for p in draws_paths:
        stem = p.name.replace("_draws.csv", "")
        norm = _norm_state(stem.rstrip("4"))
        norm_to_candidates[norm].add(stem)
    for norm, candidates in norm_to_candidates.items():
        if norm in candidates:
            stem_map[norm] = norm
        else:
            stem_map[norm] = sorted(candidates)[0]
    for norm in results_by_state.keys():
        if norm not in stem_map:
            stem_map[norm] = norm
    return stem_map

def _parse_control_center_md(md_path: Path) -> Dict[str, list[Dict[str, Any]]]:
    """
    Parse control_center.md (if present) to extract BA rows.
    Assumes a table with columns: State | Variant | BA-Score | Status | Triggers | #Candidates | Examples
    Returns {state: [rows]}
    """
    out: Dict[str, list[Dict[str, Any]]] = {}
    if not md_path.exists():
        return out
    lines = md_path.read_text(encoding="utf-8").splitlines()
    in_table = False
    headers: list[str] = []
    for line in lines:
        if line.strip().startswith("| State") and "BA-Score" in line:
            in_table = True
            headers = [h.strip() for h in line.strip("| \n").split("|")]
            continue
        if in_table:
            if not line.strip().startswith("|"):
                in_table = False
                continue
            parts = [p.strip() for p in line.strip("| \n").split("|")]
            if len(parts) != len(headers):
                continue
            row = dict(zip(headers, parts))
            state = row.get("State")
            if not state:
                continue
            state_list = out.setdefault(state, [])
            state_list.append(row)
    return out


def _parse_ba_csv(csv_path: Path) -> Dict[str, list[Dict[str, Any]]]:
    out: Dict[str, list[Dict[str, Any]]] = {}
    if not csv_path.exists():
        return out
    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            state = row.get("State")
            if not state:
                continue
            out.setdefault(state, []).append(row)
    return out


def _parse_ba_json(json_path: Path) -> Dict[str, list[Dict[str, Any]]]:
    out: Dict[str, list[Dict[str, Any]]] = {}
    if not json_path.exists():
        return out
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception:
        return out
    if isinstance(data, list):
        for row in data:
            state = row.get("State") or row.get("state")
            if not state:
                continue
            out.setdefault(state, []).append(row)
    elif isinstance(data, dict):
        for state, rows in data.items():
            if isinstance(rows, list):
                out.setdefault(state, []).extend(rows)
    return out


def _load_state_map(path: Optional[Path]) -> Dict[str, str]:
    if path and path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return { _norm_state(k): v for k, v in data.items() }
        except Exception:
            return {}
    return {}


def _parse_results_by_state(results_path: Optional[Path]) -> Dict[str, Dict[str, str]]:
    """
    Parse the structured results file (state rows with Midday/Evening columns).
    Returns {normalized_state: {"Midday": "123", "Evening": "456"}}.
    """
    if not results_path or not results_path.exists():
        return {}
    rows: Dict[str, Dict[str, str]] = {}
    with results_path.open(encoding="utf-8") as fh:
        header_seen = False
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            if not header_seen:
                # Skip header lines until we see the two-line header
                if line.lower().startswith("state"):
                    header_seen = True
                continue
            parts = [p.strip() for p in line.split("\t")]
            if len(parts) < 3:
                continue
            state_raw, midday_raw, eve_raw = parts[0], parts[1], parts[2]
            if not state_raw:
                continue
            norm_state = _norm_state(state_raw)
            entry: Dict[str, str] = {}
            if midday_raw and len(midday_raw) == 3 and midday_raw.isdigit():
                entry["Midday"] = midday_raw.zfill(3)
            if eve_raw and len(eve_raw) == 3 and eve_raw.isdigit():
                entry["Evening"] = eve_raw.zfill(3)
            if entry:
                rows[norm_state] = entry
    return rows


def _norm_state(name: str) -> str:
    """Normalize state label for loose matching (strip digits/space/underscore, lower)."""
    return "".join(ch for ch in name.lower() if ch.isalpha())


def _vtrac_index(draw: str) -> Optional[int]:
    if vtrac_reference is None:
        return None
    try:
        idx = vtrac_reference.get_vtrac_index(draw)
        return int(idx) if idx is not None else None
    except Exception:
        return None


def _vtrac_straights(idx: int) -> set[str]:
    if vtrac_reference is None:
        return set()
    try:
        straights = vtrac_reference.get_index_straights(idx)
        return set(s.zfill(3) for s in straights)
    except Exception:
        return set()


def analyze_result_token(token: str) -> Dict[str, Any]:
    idx = _vtrac_index(token)
    vt_boxed = idx is not None
    vt_straight = False
    if idx is not None:
        vt_straight = token in _vtrac_straights(idx)
    return {
        "draw": token,
        "exact_hit": True,
        "boxed_hit": True,  # token itself is the box hit
        "vt_boxed_hit": vt_boxed,
        "vt_straight_hit": vt_straight,
        "vtrac_index": idx,
    }


@dataclass
class StateSnapshot:
    state: str
    draws_path: str
    tables_path: Optional[str]
    latest_draw: Optional[str]
    tables_col1: Optional[str]
    tables_col2: Optional[str]
    freshness_match: Optional[bool]
    draws_since_double: Optional[int]
    is_double_in_results: Optional[bool]
    hits_exact: int
    hits_boxed: int
    hits_vt_boxed: int
    hits_vt_straight: int


@dataclass
class AlertRow:
    id: str
    state: str
    variant: str
    date: Optional[str]
    strength: Optional[float]
    evidence: Dict[str, Any]
    hits: Dict[str, int]


def build_snapshot(results_tokens: list[str]) -> dict:
    results_analysis = [analyze_result_token(t) for t in results_tokens]
    results_by_state: Dict[str, Dict[str, str]] = {}
    if ARGS.results_file:
        results_by_state = _parse_results_by_state(ARGS.results_file)
    ba_rows: Dict[str, list[Dict[str, Any]]] = {}
    ba_rows.update(_parse_control_center_md(CONTROL_CENTER_MD))
    if ARGS.ba_csv:
        ba_rows.update(_parse_ba_csv(ARGS.ba_csv))
    if ARGS.ba_json:
        ba_rows.update(_parse_ba_json(ARGS.ba_json))
    if not ba_rows and not CONTROL_CENTER_MD.exists() and not (ARGS.ba_csv or ARGS.ba_json):
        print("[WARN] No BA data found (control_center.md missing and no BA CSV/JSON provided)")
    snapshots: list[StateSnapshot] = []
    draws_paths = sorted(DRAW_CLEAN_DIR.glob("*_draws.csv"))
    state_map = _load_state_map(ARGS.state_map) or _build_state_map(results_by_state, draws_paths)
    alerts: list[AlertRow] = []
    for draws_path in draws_paths:
        state = draws_path.name.replace("_draws.csv", "")
        norm_state = _norm_state(state.rstrip("4"))
        mapped_state = state_map.get(norm_state, state)
        draws = _read_draws(draws_path)
        latest_draw = draws[0] if draws else None
        table_path = TABLES_DIR / state / "Combined_Combined.csv"
        col1, col2 = _read_tables_latest(table_path)
        freshness = None
        if latest_draw and col2:
            freshness = latest_draw == col2
        ds_double = _draws_since_double(draws) if draws else None
        state_results = results_by_state.get(norm_state, {}) or results_by_state.get(_norm_state(mapped_state), {})
        state_result_tokens = list(state_results.values())
        result_hits = [analyze_result_token(t) for t in state_result_tokens]
        is_double_hit = None
        if state_result_tokens:
            is_double_hit = any(_is_double(t) for t in state_result_tokens)
        hits_agg = {
            "exact": sum(1 for h in result_hits if h["exact_hit"]),
            "boxed": sum(1 for h in result_hits if h["boxed_hit"]),
            "vt_boxed": sum(1 for h in result_hits if h["vt_boxed_hit"]),
            "vt_straight": sum(1 for h in result_hits if h["vt_straight_hit"]),
        }
        snapshots.append(
            StateSnapshot(
                state=state,
                draws_path=str(draws_path.relative_to(ROOT)),
                tables_path=str(table_path.relative_to(ROOT)) if table_path.exists() else None,
                latest_draw=latest_draw,
                tables_col1=col1,
                tables_col2=col2,
                freshness_match=freshness,
                draws_since_double=ds_double,
                is_double_in_results=is_double_hit,
                hits_exact=hits_agg["exact"],
                hits_boxed=hits_agg["boxed"],
                hits_vt_boxed=hits_agg["vt_boxed"],
                hits_vt_straight=hits_agg["vt_straight"],
            )
        )
        # Alerts: due-doubles (Combined), VTRAC repeat (Combined)
        if ds_double is not None:
            alerts.append(
                AlertRow(
                    id="due_doubles",
                    state=state,
                    variant="Combined",
                    date=ARGS.results_file.name if ARGS.results_file else None,
                    strength=float(ds_double),
                    evidence={"draws_since_double": ds_double},
                    hits=hits_agg,
                )
            )
        if len(draws) >= 2:
            last_idx = _vtrac_index(draws[0])
            prev_idx = _vtrac_index(draws[1])
            if last_idx is not None and prev_idx is not None and last_idx == prev_idx:
                alerts.append(
                    AlertRow(
                        id="vtrac_repeat",
                        state=state,
                        variant="Combined",
                        date=ARGS.results_file.name if ARGS.results_file else None,
                        strength=1.0,
                        evidence={
                            "last_index": last_idx,
                            "prev_index": prev_idx,
                            "repeat": True,
                        },
                        hits=hits_agg,
                    )
                )
        for ba_row in ba_rows.get(state, []):
            try:
                strength = float(ba_row.get("BA-Score", "") or 0.0)
            except Exception:
                strength = None
            alerts.append(
                AlertRow(
                    id="blackapple",
                    state=state,
                    variant=ba_row.get("Variant", "Combined"),
                    date=ARGS.results_file.name if ARGS.results_file else None,
                    strength=strength,
                    evidence={
                        "status": ba_row.get("Status"),
                        "triggers": ba_row.get("Triggers"),
                        "num_candidates": ba_row.get("#Candidates"),
                        "examples": ba_row.get("Examples"),
                    },
                    hits=hits_agg,
                )
            )

    ranked_by_double = sorted(
        [s for s in snapshots if s.draws_since_double is not None],
        key=lambda s: s.draws_since_double,
        reverse=True,
    )
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results_tokens": results_tokens,
        "results_analysis": results_analysis,
        "alerts": [asdict(a) for a in alerts],
        "snapshots": [asdict(s) for s in snapshots],
        "rank_by_draws_since_double": [s.state for s in ranked_by_double],
    }
    return summary


def write_outputs(summary: dict, out_stem: str) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REPORT_DIR / f"{out_stem}.json"
    csv_path = REPORT_DIR / f"{out_stem}.csv"
    summary_md_path = REPORT_DIR / f"{out_stem}_summary.md"
    with json_path.open("w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)

    # Flatten key fields for quick scan
    rows = summary["snapshots"]
    fieldnames = [
        "state",
        "draws_path",
        "tables_path",
        "latest_draw",
        "tables_col1",
        "tables_col2",
        "freshness_match",
        "draws_since_double",
        "is_double_in_results",
        "hits_exact",
        "hits_boxed",
        "hits_vt_boxed",
        "hits_vt_straight",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fieldnames})

    # Optional summary per alert id
    alert_counts: Dict[str, Dict[str, int]] = {}
    alert_counts_by_variant: Dict[str, Dict[str, Dict[str, int]]] = {}
    for a in summary.get("alerts", []):
        aid = a.get("id", "unknown")
        alert_counts.setdefault(aid, {"count": 0, "hits_exact": 0, "hits_boxed": 0, "hits_vt_boxed": 0, "hits_vt_straight": 0})
        alert_counts[aid]["count"] += 1
        hits = a.get("hits", {}) or {}
        alert_counts[aid]["hits_exact"] += hits.get("exact", 0)
        alert_counts[aid]["hits_boxed"] += hits.get("boxed", 0)
        alert_counts[aid]["hits_vt_boxed"] += hits.get("vt_boxed", 0)
        alert_counts[aid]["hits_vt_straight"] += hits.get("vt_straight", 0)
        variant = a.get("variant", "Unknown")
        vc = alert_counts_by_variant.setdefault(variant, {})
        vc.setdefault(aid, {"count": 0, "hits_exact": 0, "hits_boxed": 0, "hits_vt_boxed": 0, "hits_vt_straight": 0})
        vc[aid]["count"] += 1
        vc[aid]["hits_exact"] += hits.get("exact", 0)
        vc[aid]["hits_boxed"] += hits.get("boxed", 0)
        vc[aid]["hits_vt_boxed"] += hits.get("vt_boxed", 0)
        vc[aid]["hits_vt_straight"] += hits.get("vt_straight", 0)
    summary_path = REPORT_DIR / f"{out_stem}_alerts.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["alert_id", "count", "hits_exact", "hits_boxed", "hits_vt_boxed", "hits_vt_straight"])
        for aid, stats in alert_counts.items():
            writer.writerow([aid, stats["count"], stats["hits_exact"], stats["hits_boxed"], stats["hits_vt_boxed"], stats["hits_vt_straight"]])
    # per-variant breakdown
    by_variant_path = REPORT_DIR / f"{out_stem}_alerts_by_variant.csv"
    with by_variant_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["variant", "alert_id", "count", "hits_exact", "hits_boxed", "hits_vt_boxed", "hits_vt_straight"])
        for variant, alerts in alert_counts_by_variant.items():
            for aid, stats in alerts.items():
                writer.writerow([variant, aid, stats["count"], stats["hits_exact"], stats["hits_boxed"], stats["hits_vt_boxed"], stats["hits_vt_straight"]])
    # Validate alerts against schema if available
    if ALERT_SCHEMA_PATH.exists():
        try:
            schema = json.loads(ALERT_SCHEMA_PATH.read_text(encoding="utf-8"))
            try:
                from jsonschema import validate  # type: ignore
            except ImportError:
                validate = None  # type: ignore
            if validate:
                for alert in summary.get("alerts", []):
                    validate(instance=alert, schema=schema)
        except Exception as exc:  # pragma: no cover
            print(f"[WARN] Alert schema validation failed: {exc}")
    # Markdown summary
    freshness_bad = [s for s in summary["snapshots"] if s.get("freshness_match") is False]
    due_sorted = sorted(
        [s for s in summary["snapshots"] if s.get("draws_since_double") is not None],
        key=lambda x: x["draws_since_double"],
        reverse=True,
    )[:5]
    alert_counts_lines = []
    for aid, stats in alert_counts.items():
        alert_counts_lines.append(
            f"- {aid}: count={stats['count']}, hits (exact/boxed/vt_boxed/vt_straight) = "
            f"{stats['hits_exact']}/{stats['hits_boxed']}/{stats['hits_vt_boxed']}/{stats['hits_vt_straight']}"
        )
    summary_md = [
        f"# Control Center Snapshot {out_stem}",
        "",
        f"- Generated at: {summary['generated_at']}",
        f"- Results tokens: {summary.get('results_tokens', [])}",
        "",
        "## Freshness mismatches",
    ]
    if freshness_bad:
        for s in freshness_bad:
            summary_md.append(
                f"- {s['state']}: draws={s['latest_draw']} vs tables col2={s['tables_col2']}"
            )
    else:
        summary_md.append("- None")
    summary_md.append("")
    summary_md.append("## Top 5 states by draws-since-double")
    for s in due_sorted:
        summary_md.append(f"- {s['state']}: draws_since_double={s['draws_since_double']}")
    summary_md.append("")
    summary_md.append("## Alerts")
    summary_md.extend(alert_counts_lines or ["- None"])
    summary_md_path.write_text("\n".join(summary_md), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Control Center sanity snapshot")
    parser.add_argument(
        "--results-file",
        type=Path,
        default=ROOT / "data" / "results" / "2025-06-21.txt",
        help="Structured results file with Midday/Evening columns (for hit tagging)",
    )
    parser.add_argument(
        "--state-map",
        type=Path,
        default=DEFAULT_STATE_MAP_PATH,
        help="Optional state mapping JSON (normalized state -> draws stem)",
    )
    parser.add_argument(
        "--ba-csv",
        type=Path,
        help="Optional CSV file with BA rows (State, Variant, BA-Score, Status, Triggers, #Candidates, Examples)",
    )
    parser.add_argument(
        "--ba-json",
        type=Path,
        help="Optional JSON file with BA rows (list or dict format)",
    )
    args = parser.parse_args()
    global ARGS
    ARGS = args

    results_tokens = _parse_results_file(args.results_file) if args.results_file else []
    summary = build_snapshot(results_tokens)
    out_stem = f"cc_snapshot_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
    write_outputs(summary, out_stem)
    print(f"Wrote {out_stem}.json/csv under {REPORT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
