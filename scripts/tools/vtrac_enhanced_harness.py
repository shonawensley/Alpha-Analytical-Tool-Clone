#!/usr/bin/env python3
"""
VTRAC Enhanced harness (reporting-only).

Purpose
-------
Quantify VTRAC Enhanced as:
  - a direct straight caller (exact literal in top-N straights), and
  - a gateway/lane lens (winner index present / winner index rank),
stratified by winner type (unique/double/triple).

This script:
  - Reads frozen sharepack VTRAC enhanced bundles:
      sharepacks/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json
    (or an alternate --sharepacks-root, including sharepacks/_predictive/)
  - Reads official results:
      data/results/<D>.txt
  - Writes CSV + Markdown into RUNS (no sharepack writes).

Key design choice
-----------------
Do NOT exclude doubles: doubles are a first-class part of VTRAC indices.
Triples are treated as "index missing" because modules.vtrac_reference.get_vtrac_index()
intentionally returns None for triples to match legacy behavior.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


from alpha_analytical.control_center.batch_runner import parse_winner_sheet  # noqa: E402

import modules.vtrac_reference as vr  # noqa: E402


DEFAULT_STATES: List[str] = [
    "Connecticut4",
    "Delaware4",
    "Florida4",
    "Indiana4",
    "Michigan4",
    "NewJersey4",
    "NewYork4",
    "NorthCarolina4",
    "Ohio4",
    "OntarioCanada4",
    "Pennsylvania4",
    "PuertoRico4",
    "SouthCarolina4",
    "Virginia4",
]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _canon(value: str) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if len(digits) != 3:
        return ""
    return "".join(sorted(digits))


def _winner_kind(value: str) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if len(digits) != 3:
        return "missing"
    distinct = len(set(digits))
    if distinct == 1:
        return "triple"
    if distinct == 2:
        return "double"
    if distinct == 3:
        return "unique"
    return "unknown"


def _iter_dates(start: str, end: str) -> List[str]:
    a = datetime.strptime(start, "%Y-%m-%d")
    b = datetime.strptime(end, "%Y-%m-%d")
    if b < a:
        a, b = b, a
    out: List[str] = []
    cur = a
    while cur <= b:
        out.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    return out


def _parse_int_list(csv_value: str) -> List[int]:
    raw = str(csv_value or "").strip()
    if not raw:
        return []
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    out: List[int] = []
    for p in parts:
        try:
            out.append(int(p))
        except Exception:
            raise SystemExit(f"Invalid integer in list: {p!r}")
    return out


def _read_results_winners(results_date: str) -> Dict[str, Dict[str, str]]:
    """
    Return: project_state -> {"Midday": "123", "Evening": "456"} (as available).
    """
    results_path = REPO_ROOT / "data" / "results" / f"{results_date}.txt"
    if not results_path.exists():
        return {}
    entries = parse_winner_sheet(results_path.read_text(encoding="utf-8", errors="replace"))
    out: Dict[str, Dict[str, str]] = {}
    for e in entries:
        if not e.project_state:
            continue
        m: Dict[str, str] = {}
        if e.midday:
            m["Midday"] = e.midday
        if e.evening:
            m["Evening"] = e.evening
        if m:
            out[e.project_state] = m
    return out


def _find_latest_vtrac_enhanced_json(*, day_dir: Path, state: str) -> Optional[Path]:
    vdir = day_dir / state / "vtrac" / state
    if not vdir.exists():
        return None
    hits = sorted(vdir.glob(f"{state}_vtrac_enhanced_*.json"))
    return hits[-1] if hits else None


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _top_straights_from_ranked(payload: Dict[str, Any], *, top_n: int) -> List[Dict[str, Any]]:
    """
    Replicate the selection-layer intent:
    - Use straights_ranked ordering (already score-sorted).
    - Dedupe by straight literal.
    - Keep only 3-digit digit-only strings.
    Returns list[{"straight": str, "index": int, "score": float}]
    """
    ranked = payload.get("straights_ranked") or []
    if not isinstance(ranked, list):
        return []
    out: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for row in ranked:
        if not isinstance(row, dict):
            continue
        straight = str(row.get("straight") or "").strip()
        straight_digits = "".join(ch for ch in straight if ch.isdigit())
        if len(straight_digits) != 3:
            continue
        if straight_digits in seen:
            continue
        seen.add(straight_digits)
        try:
            idx = int(row.get("index"))
        except Exception:
            idx = -1
        try:
            score = float(row.get("score"))
        except Exception:
            score = 0.0
        out.append({"straight": straight_digits, "index": idx, "score": score})
        if len(out) >= top_n:
            break
    return out


def _winner_index_rank(payload: Dict[str, Any], winner_index: int) -> Dict[str, Optional[float]]:
    indices = payload.get("indices_ranked") or []
    if not isinstance(indices, list) or not indices:
        return {"rank": None, "rank_fraction": None, "score": None, "top_score": None}
    top_score: Optional[float]
    try:
        top_score = float((indices[0] or {}).get("score"))
    except Exception:
        top_score = None
    winner_rank: Optional[int] = None
    winner_score: Optional[float] = None
    for i, row in enumerate(indices, start=1):
        if not isinstance(row, dict):
            continue
        try:
            idx = int(row.get("index"))
        except Exception:
            continue
        if idx != int(winner_index):
            continue
        winner_rank = i
        try:
            winner_score = float(row.get("score"))
        except Exception:
            winner_score = None
        break
    if winner_rank is None:
        return {"rank": None, "rank_fraction": None, "score": winner_score, "top_score": top_score}
    rank_fraction = float(winner_rank - 1) / float(max(1, len(indices) - 1))
    return {"rank": float(winner_rank), "rank_fraction": rank_fraction, "score": winner_score, "top_score": top_score}


@dataclass(frozen=True)
class Opportunity:
    date: str
    state: str
    outcome: str
    winner: str


def _iter_opportunities(*, date: str, winners_by_state: Dict[str, Dict[str, str]], states: Sequence[str]) -> List[Opportunity]:
    out: List[Opportunity] = []
    for state in states:
        w = winners_by_state.get(state) or {}
        for outcome in ("Midday", "Evening"):
            if not w.get(outcome):
                continue
            out.append(Opportunity(date=date, state=state, outcome=outcome, winner=w[outcome]))
    return out


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames))
        w.writeheader()
        for r in rows:
            w.writerow({k: (r.get(k, "") if r.get(k, "") is not None else "") for k in fieldnames})


def _pct(n: int, d: int) -> str:
    return f"{(n / d):.4f}" if d else "0.0000"


def _summarize(*, rows: Sequence[Dict[str, Any]], top_ns: Sequence[int], out_path: Path, title: str) -> None:
    """
    Write a compact Markdown summary with stratification.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    def subset(kind: Optional[str]) -> List[Dict[str, Any]]:
        if kind is None:
            return list(rows)
        return [r for r in rows if r.get("winner_kind") == kind]

    lines: List[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("This is a reporting-only harness. It measures VTRAC Enhanced as a straight caller and as an index gateway lens.")
    lines.append("")
    lines.append("Winner type handling:")
    lines.append("- `unique` and `double` are included for index metrics.")
    lines.append("- `triple` has `winner_index_missing=1` by design (legacy behavior: no vtrac_index for triples).")
    lines.append("")

    for kind in (None, "unique", "double", "triple"):
        label = "ALL (winner present)" if kind is None else kind.upper()
        block = subset(kind)
        if not block:
            continue
        lines.append(f"## {label}")
        lines.append("")
        missing = sum(1 for r in block if r.get("missing_enhanced_json") == "1")
        lines.append(f"- opportunities: `{len(block)}` (missing enhanced JSON: `{missing}`)")
        lines.append("")
        lines.append("| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |")
        lines.append("|---:|---:|---:|---:|---:|")
        for n in top_ns:
            straight_hit = sum(1 for r in block if r.get(f"straight_hit_top{n}") == "1")
            canon_hit = sum(1 for r in block if r.get(f"canonical_hit_top{n}") == "1")
            idx_hit = sum(1 for r in block if r.get(f"index_hit_top{n}") == "1")
            idx_top5 = sum(1 for r in block if r.get("winner_index_in_top5") == "1")
            lines.append(
                f"| {n} | {straight_hit} ({_pct(straight_hit, len(block))}) | {canon_hit} ({_pct(canon_hit, len(block))}) | "
                f"{idx_hit} ({_pct(idx_hit, len(block))}) | {idx_top5} ({_pct(idx_top5, len(block))}) |"
            )
        lines.append("")

    out_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="VTRAC Enhanced harness (reporting-only).")
    p.add_argument("--sharepacks-root", default="sharepacks", help="Sharepacks root directory (default: sharepacks).")
    p.add_argument("--start-date", required=True, help="Start results date D (YYYY-MM-DD).")
    p.add_argument("--end-date", required=True, help="End results date D (YYYY-MM-DD).")
    p.add_argument("--states", nargs="*", help="Optional subset of states (default: tracked list).")
    p.add_argument("--top-n", default="8,12,20", help="Comma-separated top-N straights to evaluate (default: 8,12,20).")
    p.add_argument("--out-prefix", default=None, help="Override output filename prefix under RUNS.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    states = list(args.states) if args.states else list(DEFAULT_STATES)
    top_ns = _parse_int_list(args.top_n)
    if not top_ns:
        raise SystemExit("No valid --top-n values parsed.")

    dates = _iter_dates(args.start_date, args.end_date)
    rows: List[Dict[str, Any]] = []

    for date in dates:
        winners_map = _read_results_winners(date)
        if not winners_map:
            continue
        day_dir = sharepacks_root / date
        for opp in _iter_opportunities(date=date, winners_by_state=winners_map, states=states):
            winner = str(opp.winner or "").strip()
            winner_canon = _canon(winner)
            kind = _winner_kind(winner)
            winner_index = vr.get_vtrac_index(winner)
            winner_index_missing = "1" if winner_index is None else "0"

            vpath = _find_latest_vtrac_enhanced_json(day_dir=day_dir, state=opp.state)
            if not vpath or not vpath.exists():
                rows.append(
                    {
                        "results_date": date,
                        "sharepacks_root": _safe_rel(sharepacks_root),
                        "state": opp.state,
                        "outcome": opp.outcome,
                        "winner": winner,
                        "winner_canonical": winner_canon,
                        "winner_kind": kind,
                        "winner_index": "" if winner_index is None else int(winner_index),
                        "winner_index_missing": winner_index_missing,
                        "enhanced_json": "",
                        "missing_enhanced_json": "1",
                    }
                )
                continue

            payload = _load_json(vpath)

            idx_rank = {}
            if winner_index is not None:
                idx_rank = _winner_index_rank(payload, winner_index)

            indices_ranked = payload.get("indices_ranked") or []
            winner_index_in_top5 = "0"
            if winner_index is not None and isinstance(indices_ranked, list):
                for i, r in enumerate(indices_ranked[:5]):
                    try:
                        if int((r or {}).get("index")) == int(winner_index):
                            winner_index_in_top5 = "1"
                    except Exception:
                        continue

            base_row: Dict[str, Any] = {
                "results_date": date,
                "sharepacks_root": _safe_rel(sharepacks_root),
                "state": opp.state,
                "outcome": opp.outcome,
                "winner": winner,
                "winner_canonical": winner_canon,
                "winner_kind": kind,
                "winner_index": "" if winner_index is None else int(winner_index),
                "winner_index_missing": winner_index_missing,
                "enhanced_json": _safe_rel(vpath),
                "missing_enhanced_json": "0",
                "winner_index_rank": "" if winner_index is None else (int(idx_rank.get("rank") or 0) or ""),
                "winner_index_rank_fraction": "" if winner_index is None else (idx_rank.get("rank_fraction") or ""),
                "winner_index_score": "" if winner_index is None else (idx_rank.get("score") or ""),
                "top_index_score": "" if winner_index is None else (idx_rank.get("top_score") or ""),
                "winner_index_in_top5": winner_index_in_top5 if winner_index is not None else "",
            }

            for n in top_ns:
                tops = _top_straights_from_ranked(payload, top_n=int(n))
                top_straights = [t.get("straight") for t in tops if str(t.get("straight") or "").isdigit()]
                top_indices = {int(t.get("index") or -1) for t in tops if int(t.get("index") or -1) > 0}
                top_canons = {_canon(s) for s in top_straights}

                base_row[f"straight_hit_top{n}"] = "1" if winner in top_straights else "0"
                base_row[f"canonical_hit_top{n}"] = "1" if winner_canon and winner_canon in top_canons else "0"
                if winner_index is None:
                    base_row[f"index_hit_top{n}"] = ""
                else:
                    base_row[f"index_hit_top{n}"] = "1" if int(winner_index) in top_indices else "0"

            rows.append(base_row)

    window_label = f"{dates[0]}_to_{dates[-1]}" if dates else f"{args.start_date}_to_{args.end_date}"
    prefix = args.out_prefix or f"VTRAC_ENHANCED_V0__HARNESS__{window_label}"
    out_csv = _runs_dir() / f"{prefix}.csv"
    out_md = _runs_dir() / f"{prefix}.md"

    # Stable ordering
    rows_sorted = sorted(rows, key=lambda r: (r.get("results_date") or "", r.get("state") or "", r.get("outcome") or ""))

    # Build fieldnames
    fieldnames: List[str] = [
        "results_date",
        "sharepacks_root",
        "state",
        "outcome",
        "winner",
        "winner_canonical",
        "winner_kind",
        "winner_index",
        "winner_index_missing",
        "enhanced_json",
        "missing_enhanced_json",
        "winner_index_rank",
        "winner_index_rank_fraction",
        "winner_index_score",
        "top_index_score",
        "winner_index_in_top5",
    ]
    for n in top_ns:
        fieldnames.extend([f"straight_hit_top{n}", f"canonical_hit_top{n}", f"index_hit_top{n}"])

    _write_csv(out_csv, rows_sorted, fieldnames)
    _summarize(rows=rows_sorted, top_ns=top_ns, out_path=out_md, title=f"VTRAC Enhanced Harness — {window_label}")
    print(f"Wrote: {_safe_rel(out_csv)}, {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
