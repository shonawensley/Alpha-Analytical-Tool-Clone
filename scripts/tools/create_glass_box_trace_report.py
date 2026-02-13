#!/usr/bin/env python3
"""
Create a single-outcome "glass box" trace report.

Why:
- When the system feels like jargon, we need a deterministic, end-to-end
  explainer for one (date, state, period, strategy, budget).
- This report is selection-layer oriented:
  - reads existing grade outputs (CU + Play Card)
  - reads sharepack JSONs (CU + Play Card) for raw inspection links
  - computes lane allocation directly from the Play Card JSON

Writes:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__GLASS_BOX_TRACE__<STATE>__<LABEL>__<strategy>__<budget>__<tag>.md
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import modules.vtrac_reference as vr  # noqa: E402


def _normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    return cleaned[:60]


def bool01(value: object) -> int:
    s = str(value or "").strip().lower()
    if s in {"1", "true", "yes", "y"}:
        return 1
    if s in {"0", "false", "no", "n", ""}:
        return 0
    try:
        return 1 if int(s) else 0
    except Exception:
        return 0


def safe_int(value: object) -> Optional[int]:
    try:
        s = str(value or "").strip()
        if not s:
            return None
        return int(s)
    except Exception:
        return None


def load_json(path: Path) -> Dict[str, object]:
    with path.open("r", encoding="utf-8", errors="replace") as f:
        raw = json.load(f)
    return raw if isinstance(raw, dict) else {}


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


@dataclass(frozen=True)
class CuUnionRow:
    hit_any: str
    vtrac_index_hit: str
    vtrac_index_hit_only: str
    combos_count: str
    candidate_universe_path: str


@dataclass(frozen=True)
class PlayCardRow:
    winner: str
    winner_canonical: str
    winner_vtrac_index: str
    winner_missing: str
    hit_any: str
    hit_any_inclusive: str
    straight_hit: str
    box_hit: str
    canon_hit_any_perm: str
    vtrac_index_hit: str
    vtrac_index_hit_only: str
    vtrac_pack_index: str
    vtrac_pack_indices: str
    pack_any_correct: str
    pack_straight_hit: str
    pack_canon_hit_any_perm: str
    pack_vtrac_index_hit: str
    pack_hit_any_inclusive: str
    filler_hit_any_inclusive: str
    play_card_path: str
    combos_count: str


def _cu_grade_path(*, date: str, profile: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date}__CANDIDATE_UNIVERSE_GRADE__{profile}{suffix}.csv"


def _play_grade_path(*, date: str, profile: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date}__PLAY_CARD_GRADE__{profile}{suffix}.csv"


def _bucket(*, winner_missing: str, cu_union_hit_any: str, cu_union_vtrac_index_hit: str, play_hit_any_inclusive: str) -> str:
    if bool01(winner_missing) == 1:
        return "CENSORED"
    if not str(cu_union_hit_any or "").strip() and not str(cu_union_vtrac_index_hit or "").strip():
        return "NO_CU_JOIN"
    if bool01(play_hit_any_inclusive) == 1:
        return "HIT_INCLUSIVE"
    if bool01(cu_union_hit_any) == 1:
        return "CU_EXACT_BUT_PLAY_MISS"
    if bool01(cu_union_vtrac_index_hit) == 1:
        return "CU_LANE_BUT_PLAY_MISS"
    return "CU_MISS"


def _compute_lane_allocation(*, play_card_json: Path, strategy: str, budget_label: str, winner_index: Optional[int]) -> Dict[str, object]:
    payload = load_json(play_card_json)
    strategies = payload.get("strategies")
    if not isinstance(strategies, dict):
        return {"error": "missing strategies in play card json"}
    strat = strategies.get(strategy)
    if not isinstance(strat, dict):
        return {"error": f"missing strategy: {strategy}"}
    bud = strat.get(budget_label)
    if not isinstance(bud, dict):
        return {"error": f"missing budget: {budget_label}"}
    combos_raw = bud.get("combos")
    combos = [str(x) for x in combos_raw] if isinstance(combos_raw, list) else []

    counts_by_idx: Dict[int, int] = {}
    combos_without_index = 0
    for c in combos:
        idx = vr.get_vtrac_index(str(c))
        if isinstance(idx, int):
            counts_by_idx[int(idx)] = counts_by_idx.get(int(idx), 0) + 1
        else:
            combos_without_index += 1

    indices_touched = len(counts_by_idx)
    max_lines_single_index = max(counts_by_idx.values()) if counts_by_idx else 0
    top_indices = sorted(counts_by_idx.items(), key=lambda kv: (-kv[1], kv[0]))

    winner_lane_lines: Optional[int] = None
    if isinstance(winner_index, int):
        winner_lane_lines = counts_by_idx.get(int(winner_index), 0)

    return {
        "combos_count": len(combos),
        "combos_without_index_count": combos_without_index,
        "indices_touched_count": indices_touched,
        "max_lines_single_index": max_lines_single_index,
        "winner_lane_lines": winner_lane_lines,
        "winner_lane_present": (winner_lane_lines is not None and winner_lane_lines > 0),
        "top_indices_by_lines": top_indices[:12],
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a single-outcome glass-box trace report (selection-layer).")
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD).")
    ap.add_argument("--state", required=True, help="State key (e.g., OntarioCanada4).")
    ap.add_argument("--winner-label", required=True, help="Winner label / period (Midday/Evening/Combined).")
    ap.add_argument("--profile", default="tool_only", help="Profile (default: tool_only).")
    ap.add_argument("--experiment-tag", default="stable10", help="Experiment tag suffix (default: stable10).")
    ap.add_argument("--strategy", required=True, help="Play Card strategy to trace.")
    ap.add_argument("--budget", default="B36", help="Budget label (default: B36).")
    ap.add_argument("--out", default=None, help="Override output path (md).")
    args = ap.parse_args()

    date = str(args.date).strip()
    state = str(args.state).strip()
    winner_label = str(args.winner_label).strip()
    profile = str(args.profile).strip() or "tool_only"
    experiment_tag = _normalize_tag(args.experiment_tag)
    strategy = str(args.strategy).strip()
    budget_label = str(args.budget).strip() or "B36"

    cu_csv = _cu_grade_path(date=date, profile=profile, experiment_tag=experiment_tag)
    pc_csv = _play_grade_path(date=date, profile=profile, experiment_tag=experiment_tag)
    if not cu_csv.exists():
        raise SystemExit(f"Missing CU grade CSV: {cu_csv}")
    if not pc_csv.exists():
        raise SystemExit(f"Missing Play Card grade CSV: {pc_csv}")

    cu_rows = load_csv_rows(cu_csv)
    cu_match = [
        r
        for r in cu_rows
        if (r.get("state_key") or "") == state
        and (r.get("winner_label") or "") == winner_label
        and (r.get("pack_id") or "") == "__UNION__"
    ]
    if not cu_match:
        raise SystemExit(f"Missing CU __UNION__ row for: date={date} state={state} label={winner_label}")
    cu = cu_match[0]
    cu_union = CuUnionRow(
        hit_any=(cu.get("hit_any") or "").strip(),
        vtrac_index_hit=(cu.get("vtrac_index_hit") or "").strip(),
        vtrac_index_hit_only=(cu.get("vtrac_index_hit_only") or "").strip(),
        combos_count=(cu.get("combos_count") or "").strip(),
        candidate_universe_path=(cu.get("candidate_universe_path") or "").strip(),
    )

    pc_rows = load_csv_rows(pc_csv)
    pc_match = [
        r
        for r in pc_rows
        if (r.get("state_key") or "") == state
        and (r.get("winner_label") or "") == winner_label
        and (r.get("strategy") or "") == strategy
        and (r.get("budget_label") or "") == budget_label
    ]
    if not pc_match:
        raise SystemExit(
            f"Missing Play Card grade row for: date={date} state={state} label={winner_label} strategy={strategy} budget={budget_label}"
        )
    pc = pc_match[0]
    play = PlayCardRow(
        winner=(pc.get("winner") or "").strip(),
        winner_canonical=(pc.get("winner_canonical") or "").strip(),
        winner_vtrac_index=(pc.get("winner_vtrac_index") or "").strip(),
        winner_missing=(pc.get("winner_missing") or "").strip(),
        hit_any=(pc.get("hit_any") or "").strip(),
        hit_any_inclusive=(pc.get("hit_any_inclusive") or "").strip(),
        straight_hit=(pc.get("straight_hit") or "").strip(),
        box_hit=(pc.get("box_hit") or "").strip(),
        canon_hit_any_perm=(pc.get("canon_hit_any_perm") or "").strip(),
        vtrac_index_hit=(pc.get("vtrac_index_hit") or "").strip(),
        vtrac_index_hit_only=(pc.get("vtrac_index_hit_only") or "").strip(),
        vtrac_pack_index=(pc.get("vtrac_pack_index") or "").strip(),
        vtrac_pack_indices=(pc.get("vtrac_pack_indices") or "").strip(),
        pack_any_correct=(pc.get("pack_any_correct") or "").strip(),
        pack_straight_hit=(pc.get("pack_straight_hit") or "").strip(),
        pack_canon_hit_any_perm=(pc.get("pack_canon_hit_any_perm") or "").strip(),
        pack_vtrac_index_hit=(pc.get("pack_vtrac_index_hit") or "").strip(),
        pack_hit_any_inclusive=(pc.get("pack_hit_any_inclusive") or "").strip(),
        filler_hit_any_inclusive=(pc.get("filler_hit_any_inclusive") or "").strip(),
        play_card_path=(pc.get("play_card_path") or "").strip(),
        combos_count=(pc.get("combos_count") or "").strip(),
    )

    bucket = _bucket(
        winner_missing=play.winner_missing,
        cu_union_hit_any=cu_union.hit_any,
        cu_union_vtrac_index_hit=cu_union.vtrac_index_hit,
        play_hit_any_inclusive=play.hit_any_inclusive,
    )

    pc_path = (REPO_ROOT / play.play_card_path).resolve()
    if not pc_path.exists():
        raise SystemExit(f"Missing play card JSON: {pc_path}")

    winner_idx = safe_int(play.winner_vtrac_index)
    alloc = _compute_lane_allocation(play_card_json=pc_path, strategy=strategy, budget_label=budget_label, winner_index=winner_idx)

    out_path = Path(args.out) if args.out else None
    if out_path is None:
        tag = f"__{experiment_tag}" if experiment_tag else ""
        safe_state = re.sub(r"[^A-Za-z0-9_-]+", "_", state).strip("_")
        safe_label = re.sub(r"[^A-Za-z0-9_-]+", "_", winner_label).strip("_")
        safe_strategy = re.sub(r"[^A-Za-z0-9_-]+", "_", strategy).strip("_")
        out_path = RUNS_DIR / f"{date}__GLASS_BOX_TRACE__{safe_state}__{safe_label}__{safe_strategy}__{budget_label}{tag}.md"
    if not out_path.is_absolute():
        out_path = (REPO_ROOT / out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Links to raw artifacts (best-effort; do not assert existence beyond play_card_json)
    cu_json = Path(cu_union.candidate_universe_path) if cu_union.candidate_universe_path else None
    cu_evidence_csv = (
        Path(str(cu_json).replace("candidate_universe", "candidate_universe_evidence").replace(".json", ".csv"))
        if cu_json
        else None
    )
    signals_bundle = Path(str(cu_json).replace("candidate_universe", "signals_bundle")) if cu_json else None

    lines: List[str] = []
    lines.append(f"# Glass‑Box Trace — {state} ({date} • {winner_label})")
    lines.append("")
    lines.append("Scope:")
    lines.append(f"- profile: `{profile}`")
    if experiment_tag:
        lines.append(f"- experiment_tag: `{experiment_tag}`")
    lines.append(f"- strategy: `{strategy}` @ `{budget_label}`")
    lines.append("")
    winners_digest = RUNS_DIR / f"{date}__WINNERS_DIGEST.md"
    results_txt = REPO_ROOT / "data" / "results" / f"{date}.txt"
    lines.append("## Quick links")
    if winners_digest.exists():
        lines.append(f"- Winners digest: `{winners_digest.relative_to(REPO_ROOT)}`")
    if results_txt.exists():
        lines.append(f"- Results file: `{results_txt.relative_to(REPO_ROOT)}`")
    lines.append("")
    lines.append("## Winner facts")
    lines.append(f"- winner: `{play.winner}`")
    lines.append(f"- canonical: `{play.winner_canonical}`")
    lines.append(f"- vtrac index (lane): `{play.winner_vtrac_index}`")
    lines.append(f"- winner_missing: `{play.winner_missing}`")
    lines.append("")
    lines.append("## Contracts (CU vs Play Card)")
    lines.append(f"- CU union: `hit_any={cu_union.hit_any}` `vtrac_index_hit={cu_union.vtrac_index_hit}` `vtrac_index_hit_only={cu_union.vtrac_index_hit_only}` (combos={cu_union.combos_count})")
    lines.append(f"- Play Card: `hit_any={play.hit_any}` `hit_any_inclusive={play.hit_any_inclusive}` `vtrac_index_hit={play.vtrac_index_hit}` `vtrac_index_hit_only={play.vtrac_index_hit_only}` (combos={play.combos_count})")
    lines.append("")
    lines.append("## Bucket (where did it break?)")
    lines.append(f"- `{bucket}`")
    lines.append("")
    lines.append("## Lane allocation (computed from Play Card JSON)")
    if "error" in alloc:
        lines.append(f"- ERROR: `{alloc['error']}`")
    else:
        lines.append(f"- indices_touched_count: `{alloc.get('indices_touched_count')}`")
        lines.append(f"- winner_lane_present: `{1 if alloc.get('winner_lane_present') else 0}`")
        lines.append(f"- winner_lane_lines: `{alloc.get('winner_lane_lines')}`")
        lines.append(f"- combos_without_index_count: `{alloc.get('combos_without_index_count')}`")
        lines.append(f"- max_lines_single_index: `{alloc.get('max_lines_single_index')}`")
        top_indices = alloc.get("top_indices_by_lines") or []
        if isinstance(top_indices, list) and top_indices:
            rendered = ", ".join(f"{idx}:{cnt}" for idx, cnt in top_indices)
            lines.append(f"- top_indices_by_lines: `{rendered}`")
    lines.append("")
    lines.append("## Pack bridge (if present)")
    if play.vtrac_pack_indices:
        lines.append(f"- vtrac_pack_index: `{play.vtrac_pack_index}`")
        lines.append(f"- vtrac_pack_indices: `{play.vtrac_pack_indices}`")
        lines.append(f"- pack_any_correct: `{play.pack_any_correct}`")
        lines.append(f"- pack_hit_any_inclusive: `{play.pack_hit_any_inclusive}`")
        lines.append(f"- filler_hit_any_inclusive: `{play.filler_hit_any_inclusive}`")
    else:
        lines.append("- (no vtrac_pack fields present for this strategy/budget)")
    lines.append("")
    lines.append("## Raw artifacts to open")
    lines.append(f"- CU grade: `{cu_csv.relative_to(REPO_ROOT)}`")
    lines.append(f"- Play Card grade: `{pc_csv.relative_to(REPO_ROOT)}`")
    if cu_json:
        lines.append(f"- CU JSON: `{cu_json}`")
    if cu_evidence_csv:
        lines.append(f"- CU evidence: `{cu_evidence_csv}`")
    if signals_bundle:
        lines.append(f"- Signals bundle: `{signals_bundle}`")
    lines.append(f"- Play Card JSON: `{play.play_card_path}`")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", errors="replace")

    rel = out_path.relative_to(REPO_ROOT) if out_path.is_relative_to(REPO_ROOT) else out_path
    print(str(rel))


if __name__ == "__main__":
    main()
