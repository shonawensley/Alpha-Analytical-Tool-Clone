#!/usr/bin/env python3
"""
Create a compact "case matrix" CSV for the Crossroads Glass-Box pack.

This is a reporting-only helper. It does not change analyzers or selection code.

Inputs:
  - A CASES.md (the deterministic teaching-case index)
  - The glass-box traces referenced by CASES.md
  - A winner-lane-rank CSV (adds lane-rank columns per outcome+strategy)

Output:
  - A single CSV row per case, with enough columns to review failures without
    hunting across multiple artifacts.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


ROOT = Path(__file__).resolve().parents[2]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)


@dataclass
class Case:
    case_id: str
    case_title: str
    header: str
    predictive_report: str
    glass_box_trace: str
    mv_report: str
    winners_html: str


def _parse_cases_md(cases_md: Path) -> List[Case]:
    text = _read_text(cases_md)
    cases: List[Case] = []
    cur: Dict[str, str] = {}
    cur_title = ""
    cur_id = ""

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("### Case "):
            if cur_id:
                cases.append(
                    Case(
                        case_id=cur_id,
                        case_title=cur_title,
                        header=cur.get("Header", ""),
                        predictive_report=cur.get("Predictive report", ""),
                        glass_box_trace=cur.get("Glass‑box trace", cur.get("Glass-box trace", "")),
                        mv_report=cur.get("MV report", ""),
                        winners_html=cur.get("Winners HTML", ""),
                    )
                )
            cur = {}
            m = re.match(r"^### Case\s+(\d+)\s+—\s+(.*)$", line)
            if not m:
                raise SystemExit(f"Unparseable case header: {line}")
            cur_id = m.group(1).strip()
            cur_title = m.group(2).strip()
            continue

        m = re.match(r"^- ([^:]+):\s+(.*)$", line)
        if m:
            key = m.group(1).strip()
            rest = m.group(2).strip()
            backticks = re.findall(r"`([^`]+)`", rest)
            if key == "Header":
                # Header line uses multiple backtick segments:
                #   `YYYY-MM-DD STATE LABEL` winner=`...` idx=`...`
                if len(backticks) >= 3:
                    cur[key] = f"{backticks[0]} winner=`{backticks[1]}` idx=`{backticks[2]}`"
                elif backticks:
                    cur[key] = backticks[0]
                else:
                    cur[key] = rest
            else:
                # For paths, the first backtick segment is the file path.
                cur[key] = backticks[0] if backticks else rest

    if cur_id:
        cases.append(
            Case(
                case_id=cur_id,
                case_title=cur_title,
                header=cur.get("Header", ""),
                predictive_report=cur.get("Predictive report", ""),
                glass_box_trace=cur.get("Glass‑box trace", cur.get("Glass-box trace", "")),
                mv_report=cur.get("MV report", ""),
                winners_html=cur.get("Winners HTML", ""),
            )
        )
    return cases


def _parse_header(header: str) -> Dict[str, str]:
    """
    Example header:
      2026-01-15 OntarioCanada4 Midday winner=`598` idx=`14`
    """
    out: Dict[str, str] = {}
    parts = header.split()
    if len(parts) >= 3:
        out["results_date"] = parts[0]
        out["state_key"] = parts[1]
        out["winner_label"] = parts[2]
    m_w = re.search(r"winner=`([^`]+)`", header)
    if m_w:
        out["winner"] = m_w.group(1).strip()
    m_i = re.search(r"idx=`([^`]+)`", header)
    if m_i:
        out["winner_vtrac_index"] = m_i.group(1).strip()
    return out


def _parse_contract_line(line: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for key in ("hit_any", "hit_any_inclusive", "vtrac_index_hit", "vtrac_index_hit_only"):
        m = re.search(rf"{re.escape(key)}=([01])", line)
        if m:
            out[key] = m.group(1)
    m_c = re.search(r"combos=(\d+)", line)
    if m_c:
        out["combos"] = m_c.group(1)
    return out


def _parse_trace(trace_md: Path) -> Dict[str, str]:
    text = _read_text(trace_md)
    out: Dict[str, str] = {"trace_path": _safe_rel(trace_md)}

    mode: Optional[str] = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            mode = line[3:].strip()
            continue

        if mode == "Winner facts" and line.startswith("- "):
            m = re.match(r"^- ([^:]+):\s+`([^`]+)`\s*$", line)
            if m:
                key = m.group(1).strip()
                val = m.group(2).strip()
                if key == "vtrac index (lane)":
                    out["winner_vtrac_index"] = val
                elif key == "winner_missing":
                    out["winner_missing"] = val
                else:
                    out[key.replace(" ", "_")] = val
                continue

        if mode == "Contracts (CU vs Play Card)" and line.startswith("- "):
            if line.startswith("- CU union:"):
                out.update({f"cu_union_{k}": v for k, v in _parse_contract_line(line).items()})
            elif line.startswith("- Play Card:"):
                out.update({f"play_{k}": v for k, v in _parse_contract_line(line).items()})
            continue

        if mode == "Bucket (where did it break?)" and line.startswith("- `") and line.endswith("`"):
            out["bucket"] = line.strip("- ").strip("`")
            continue

        if mode == "Lane allocation (computed from Play Card JSON)" and line.startswith("- "):
            m = re.match(r"^- ([^:]+):\s+`([^`]+)`\s*$", line)
            if m:
                out[m.group(1).strip()] = m.group(2).strip()
            continue

        if mode == "Pack bridge (if present)" and line.startswith("- "):
            m = re.match(r"^- ([^:]+):\s+`([^`]+)`\s*$", line)
            if m:
                out[m.group(1).strip()] = m.group(2).strip()
            continue

        if mode == "Raw artifacts to open" and line.startswith("- "):
            m = re.match(r"^- ([^:]+):\s+`([^`]+)`\s*$", line)
            if m:
                out[m.group(1).strip().lower().replace(" ", "_")] = m.group(2).strip()
            continue

    return out


def _load_lane_rank_index(lane_rank_csv: Path) -> Dict[str, Dict[str, str]]:
    """
    Key: f"{results_date}|{state_key}|{winner_label}|{strategy}|{budget_label}"
    """
    index: Dict[str, Dict[str, str]] = {}
    with lane_rank_csv.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            key = "|".join(
                [
                    (row.get("results_date") or "").strip(),
                    (row.get("state_key") or "").strip(),
                    (row.get("winner_label") or "").strip(),
                    (row.get("strategy") or "").strip(),
                    (row.get("budget_label") or "").strip(),
                ]
            )
            if key.count("|") != 4:
                continue
            index[key] = row
    return index


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--cases-md",
        default=str(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "PACKAGES"
            / "crossroads_glass_box__2026-01-15"
            / "CASES.md"
        ),
        help="Path to CASES.md (default: Crossroads Pack v1)",
    )
    ap.add_argument(
        "--strategy",
        default="v0_2_default_multi_pack_packheavy_spine4_index_tail",
        help="Strategy key to join lane-rank rows (default: Crossroads baseline)",
    )
    ap.add_argument("--budget", default="B36", help="Budget label (default: B36)")
    ap.add_argument(
        "--lane-rank-csv",
        default=str(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS"
            / "2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36.csv"
        ),
        help="Winner lane rank CSV for the window containing the cases",
    )
    ap.add_argument(
        "--out",
        default=str(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS"
            / "V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv"
        ),
        help="Output CSV path",
    )
    args = ap.parse_args()

    cases_md = Path(args.cases_md)
    lane_rank_csv = Path(args.lane_rank_csv)
    out_csv = Path(args.out)
    strategy = str(args.strategy).strip()
    budget = str(args.budget).strip()

    cases = _parse_cases_md(cases_md)
    lane_rank_index = _load_lane_rank_index(lane_rank_csv) if lane_rank_csv.exists() else {}

    rows: List[Dict[str, str]] = []
    for c in cases:
        header = _parse_header(c.header)
        trace_path = ROOT / c.glass_box_trace
        trace = _parse_trace(trace_path)

        key = "|".join(
            [
                header.get("results_date", ""),
                header.get("state_key", ""),
                header.get("winner_label", ""),
                strategy,
                budget,
            ]
        )
        lr = lane_rank_index.get(key) or {}

        row: Dict[str, str] = {
            "case_id": c.case_id,
            "case_title": c.case_title,
            "results_date": header.get("results_date", ""),
            "state_key": header.get("state_key", ""),
            "winner_label": header.get("winner_label", ""),
            "winner": trace.get("winner", header.get("winner", "")),
            "canonical": trace.get("canonical", ""),
            "winner_vtrac_index": trace.get("winner_vtrac_index", header.get("winner_vtrac_index", "")),
            "bucket": trace.get("bucket", ""),
            "cu_union_hit_any": trace.get("cu_union_hit_any", ""),
            "cu_union_vtrac_index_hit": trace.get("cu_union_vtrac_index_hit", ""),
            "cu_union_vtrac_index_hit_only": trace.get("cu_union_vtrac_index_hit_only", ""),
            "play_hit_any": trace.get("play_hit_any", ""),
            "play_hit_any_inclusive": trace.get("play_hit_any_inclusive", ""),
            "play_vtrac_index_hit": trace.get("play_vtrac_index_hit", ""),
            "play_vtrac_index_hit_only": trace.get("play_vtrac_index_hit_only", ""),
            "indices_touched_count": trace.get("indices_touched_count", ""),
            "winner_lane_present": trace.get("winner_lane_present", ""),
            "winner_lane_lines": trace.get("winner_lane_lines", ""),
            "max_lines_single_index": trace.get("max_lines_single_index", ""),
            "vtrac_pack_index": trace.get("vtrac_pack_index", ""),
            "vtrac_pack_indices": trace.get("vtrac_pack_indices", ""),
            "pack_any_correct": trace.get("pack_any_correct", ""),
            "pack_hit_any_inclusive": trace.get("pack_hit_any_inclusive", ""),
            "filler_hit_any_inclusive": trace.get("filler_hit_any_inclusive", ""),
            "lane_present": lr.get("lane_present", ""),
            "lane_rank_methods_first": lr.get("lane_rank_methods_first", ""),
            "lane_rank_packs_first": lr.get("lane_rank_packs_first", ""),
            "lane_rank_score_total_first": lr.get("lane_rank_score_total_first", ""),
            "winner_in_pack_indices": lr.get("winner_in_pack_indices", ""),
            "winner_selected_by": lr.get("winner_selected_by", ""),
            "winner_combo_source": lr.get("winner_combo_source", ""),
            "predictive_report": c.predictive_report,
            "glass_box_trace": c.glass_box_trace,
            "mv_report": c.mv_report,
            "winners_html": c.winners_html,
            "cu_json": trace.get("cu_json", ""),
            "play_card_json": trace.get("play_card_json", ""),
        }

        if not lr and lane_rank_csv.exists():
            print(
                f"warning: no lane-rank row for case {c.case_id} ({key}); check --lane-rank-csv/--strategy",
                file=sys.stderr,
            )

        rows.append(row)

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print(f"Wrote {len(rows)} cases: {_safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
