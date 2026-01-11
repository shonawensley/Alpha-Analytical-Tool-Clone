#!/usr/bin/env python3
"""
Build an inventory of "double" and "mirror-double" winners across the RUNS corpus.

This is a reporting-only tool:
- Reads from existing RUNS corpus exports + frozen sharepacks (Aux + Control Center).
- Does NOT re-run analyzers or regenerate tables.

Outputs (default, into RUNS/):
- DOUBLES_MIRROR_DOUBLES__INVENTORY.csv
- DOUBLES_MIRROR_DOUBLES__INVENTORY.md
- DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md

Definitions (project-specific)
------------------------------
- Winner literal: the 3-digit string from results (keep leading zeros).
- Winner canonical: sorted digits (BOX / any-order match).
- Double: exactly two digits are the same (e.g., 744).
- Triple: all three digits are the same (e.g., 777).
- Mirror mapping: VTRAC-pair mapping (difference-5): 0↔5, 1↔6, 2↔7, 3↔8, 4↔9.
- Mirror-double (strict): a non-double winner that contains at least one full mirror pair
  in its digits (e.g., 361 contains the 1/6 mirror pair; 749 contains the 4/9 pair).

Usage
-----
python3 scripts/tools/create_doubles_mirror_doubles_inventory.py
python3 scripts/tools/create_doubles_mirror_doubles_inventory.py --from-date 2026-01-05 --to-date 2026-01-09
python3 scripts/tools/create_doubles_mirror_doubles_inventory.py --include-all
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

CORPUS_SUMMARY = RUNS_DIR / "corpus_summary.csv"
CORPUS_TOOL_METRICS = RUNS_DIR / "corpus_tool_metrics.csv"

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

MIRROR_MAP: Dict[str, str] = {
    "0": "5",
    "1": "6",
    "2": "7",
    "3": "8",
    "4": "9",
    "5": "0",
    "6": "1",
    "7": "2",
    "8": "3",
    "9": "4",
}

GROUP_ORDER = ["0/5", "1/6", "2/7", "3/8", "4/9"]
DIGIT_TO_GROUP: Dict[str, str] = {
    "0": "0/5",
    "5": "0/5",
    "1": "1/6",
    "6": "1/6",
    "2": "2/7",
    "7": "2/7",
    "3": "3/8",
    "8": "3/8",
    "4": "4/9",
    "9": "4/9",
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _parse_bool(value: object) -> bool:
    s = str(value).strip().lower()
    return s in ("1", "true", "yes", "y")


def _parse_int(value: object) -> Optional[int]:
    s = str(value).strip()
    if not s:
        return None
    try:
        return int(float(s))
    except Exception:
        return None


def _parse_float(value: object) -> Optional[float]:
    s = str(value).strip()
    if not s:
        return None
    try:
        return float(s)
    except Exception:
        return None


def _normalize_pick3_literal(value: object) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    if len(digits) <= 3:
        digits = digits.zfill(3)
    return digits if len(digits) == 3 else ""


def _canon(triad: str) -> str:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return ""
    return "".join(sorted(triad))


def _is_double(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 2


def _is_triple(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 1


def _mirror_pairs_present(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    digits = set(triad)
    pairs = []
    for d, m in MIRROR_MAP.items():
        if d < m and d in digits and m in digits:
            pairs.append(DIGIT_TO_GROUP[d])
    return sorted(set(pairs), key=lambda g: GROUP_ORDER.index(g) if g in GROUP_ORDER else 999)


def _vtrac_group_family(triad: str) -> str:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return ""
    groups = {DIGIT_TO_GROUP[d] for d in triad}
    ordered = sorted(groups, key=lambda g: GROUP_ORDER.index(g) if g in GROUP_ORDER else 999)
    return "-".join(ordered)


def _read_csv_dicts(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _maybe_read_csv_dicts(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    return _read_csv_dicts(path)


def _read_due_doubles_by_date(date: str) -> Dict[Tuple[str, str], Dict[str, str]]:
    """
    Key: (StateKey, Variant) where Variant ∈ {Midday, Evening, Combined}.
    """
    p = REPO_ROOT / "sharepacks" / date / "control_center" / "due_doubles.csv"
    rows = _maybe_read_csv_dicts(p)
    out: Dict[Tuple[str, str], Dict[str, str]] = {}
    for row in rows:
        key = (row.get("StateKey", ""), row.get("Variant", ""))
        if not key[0] or not key[1]:
            continue
        out[key] = row
    return out


def _extract_due_family_labels(row: Dict[str, str]) -> List[str]:
    labels: List[str] = []
    for i in range(1, 6):
        raw = row.get(f"Family {i}", "").strip()
        if not raw:
            continue
        label = raw.split(":", 1)[0].strip()
        if label:
            labels.append(label)
    return labels


def _find_aux_draws_csv(date: str, state_key: str, period: str) -> Optional[Path]:
    """
    period: Midday | Evening
    """
    draws_dir = REPO_ROOT / "sharepacks" / date / state_key / "aux" / "draws"
    if not draws_dir.exists():
        return None
    matches = sorted(draws_dir.glob(f"*_{period}_draws.csv"))
    return matches[0] if matches else None


def _compute_draws_since_double(draws_csv: Path) -> Optional[int]:
    """
    Computes the number of draws since the most recent double/triple in the history list.

    Assumes the draw list is newest-first (as written by aux snapshot).
    """
    try:
        rows = _read_csv_dicts(draws_csv)
    except Exception:
        return None
    draws = [_normalize_pick3_literal(r.get("Draw", "")) for r in rows]
    draws = [d for d in draws if d]
    for idx, d in enumerate(draws):
        if len(set(d)) < 3:
            return idx
    return len(draws)


def _best_cu_hit_row(
    rows: Sequence[Dict[str, str]],
    *,
    hit_field: str,
    exclude_methods: Sequence[str] = (),
) -> Optional[Dict[str, str]]:
    """
    Choose the "best" pack that hit, by minimizing cost_units then combos_count.
    """
    candidates: List[Dict[str, str]] = []
    exclude = set(exclude_methods)
    for r in rows:
        if r.get("method_id", "") in exclude:
            continue
        if _parse_bool(r.get(hit_field, "")):
            candidates.append(r)
    if not candidates:
        return None

    def key(r: Dict[str, str]) -> Tuple[float, int, str, str]:
        cost = _parse_float(r.get("cost_units", "")) or 1e18
        combos = _parse_int(r.get("combos_count", "")) or 10**9
        return cost, combos, r.get("method_id", ""), r.get("pack_id", "")

    return sorted(candidates, key=key)[0]


@dataclass(frozen=True)
class _EventKey:
    date: str
    state: str
    period: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Create doubles + mirror-doubles inventory across gold-day RUNS corpus.")
    p.add_argument("--runs-dir", default=str(RUNS_DIR), help="RUNS directory (default: docs/.../RUNS)")
    p.add_argument("--out-csv", default=None, help="Override CSV output path")
    p.add_argument("--out-md", default=None, help="Override Markdown inventory output path")
    p.add_argument("--out-deep-dive", default=None, help="Override Markdown deep dive output path")
    p.add_argument("--from-date", default=None, help="Start date (YYYY-MM-DD), inclusive")
    p.add_argument("--to-date", default=None, help="End date (YYYY-MM-DD), inclusive")
    p.add_argument("--include-all", action="store_true", help="Include all winners (not just doubles/mirror-doubles)")
    return p.parse_args()


def _date_in_range(date: str, start: Optional[str], end: Optional[str]) -> bool:
    if start and date < start:
        return False
    if end and date > end:
        return False
    return True


def main() -> None:
    args = parse_args()
    runs_dir = Path(args.runs_dir)
    corpus_summary = runs_dir / "corpus_summary.csv"
    corpus_tool_metrics = runs_dir / "corpus_tool_metrics.csv"

    if not corpus_summary.exists():
        raise SystemExit(f"Missing RUNS corpus: {corpus_summary}")
    if not corpus_tool_metrics.exists():
        raise SystemExit(f"Missing tool-metrics corpus: {corpus_tool_metrics}")

    if args.from_date and not _DATE_RE.match(args.from_date.strip()):
        raise SystemExit("--from-date must be YYYY-MM-DD")
    if args.to_date and not _DATE_RE.match(args.to_date.strip()):
        raise SystemExit("--to-date must be YYYY-MM-DD")

    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / "DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / "DOUBLES_MIRROR_DOUBLES__INVENTORY.md"
    out_deep = Path(args.out_deep_dive) if args.out_deep_dive else runs_dir / "DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md"

    # Index tool metrics by (date,state,period)
    tool_rows = _read_csv_dicts(corpus_tool_metrics)
    tool_by_key: Dict[_EventKey, Dict[str, str]] = {}
    for row in tool_rows:
        key = _EventKey(row.get("date", ""), row.get("state", ""), row.get("period", ""))
        if key.date and key.state and key.period:
            tool_by_key[key] = row

    # Candidate Universe + play card grades exist only for some dates.
    cu_grade_by_key: Dict[_EventKey, List[Dict[str, str]]] = defaultdict(list)
    play_grade_by_key: Dict[_EventKey, Dict[str, str]] = {}
    for grade_path in sorted(runs_dir.glob("*__CANDIDATE_UNIVERSE_GRADE.csv")):
        date = grade_path.name.split("__", 1)[0]
        for row in _read_csv_dicts(grade_path):
            key = _EventKey(date, row.get("state_key", ""), row.get("winner_label", ""))
            if key.state and key.period:
                cu_grade_by_key[key].append(row)
    for grade_path in sorted(runs_dir.glob("*__PLAY_CARD_GRADE.csv")):
        date = grade_path.name.split("__", 1)[0]
        for row in _read_csv_dicts(grade_path):
            key = _EventKey(date, row.get("state_key", ""), row.get("winner_label", ""))
            if key.state and key.period:
                play_grade_by_key[key] = row

    summary_rows = _read_csv_dicts(corpus_summary)
    dates = sorted({r.get("date", "") for r in summary_rows if r.get("date", "")})

    due_by_date: Dict[str, Dict[Tuple[str, str], Dict[str, str]]] = {}
    for d in dates:
        if not _date_in_range(d, args.from_date, args.to_date):
            continue
        due_by_date[d] = _read_due_doubles_by_date(d)

    out_rows: List[Dict[str, str]] = []

    for row in summary_rows:
        date = row.get("date", "")
        state = row.get("state", "")
        period = row.get("period", "")
        if not date or not state or not period:
            continue
        if not _date_in_range(date, args.from_date, args.to_date):
            continue

        winner = _normalize_pick3_literal(row.get("winner", ""))
        if not winner or _parse_bool(row.get("winner_missing", "")):
            continue

        win_canon = _canon(winner)
        win_is_double = _is_double(winner)
        win_is_triple = _is_triple(winner)
        mirror_pairs = _mirror_pairs_present(winner)
        win_has_mirror_pair = bool(mirror_pairs)
        win_is_mirror_double = (not win_is_double) and (not win_is_triple) and win_has_mirror_pair
        vtrac_family = _vtrac_group_family(winner)

        if not args.include_all and not (win_is_double or win_is_triple or win_is_mirror_double):
            continue

        key = _EventKey(date, state, period)
        trow = tool_by_key.get(key, {})

        due_row = due_by_date.get(date, {}).get((state, period), {})
        due_ds = due_row.get("Draws Since Double", "").strip()
        due_family_labels = _extract_due_family_labels(due_row) if due_row else []
        due_family_rank = ""
        if vtrac_family and due_family_labels:
            for idx, label in enumerate(due_family_labels, start=1):
                if label == vtrac_family:
                    due_family_rank = str(idx)
                    break

        due_in_family_flag = ""
        if due_row:
            flag_col = "Midday Winner In Family" if period == "Midday" else "Evening Winner In Family"
            due_in_family_flag = due_row.get(flag_col, "")

        aux_draws_csv = _find_aux_draws_csv(date, state, period)
        aux_ds = _compute_draws_since_double(aux_draws_csv) if aux_draws_csv else None
        aux_ds_s = "" if aux_ds is None else str(aux_ds)

        ds_delta = ""
        try:
            if due_ds and aux_ds is not None:
                ds_delta = str(int(due_ds) - int(aux_ds))
        except Exception:
            ds_delta = ""

        # Predictive grade joins (when available)
        cu_rows = cu_grade_by_key.get(key, [])
        cu_box_methods = sorted({r.get("method_id", "") for r in cu_rows if _parse_bool(r.get("box_hit", "")) and r.get("method_id")})
        cu_box_methods_non_union = [m for m in cu_box_methods if m != "union"]
        cu_idx_methods = sorted(
            {r.get("method_id", "") for r in cu_rows if _parse_bool(r.get("vtrac_index_hit", "")) and r.get("method_id")}
        )
        cu_idx_methods_non_union = [m for m in cu_idx_methods if m != "union"]
        cu_hit_any = any(_parse_bool(r.get("hit_any", "")) for r in cu_rows)
        cu_box_hit = any(_parse_bool(r.get("box_hit", "")) for r in cu_rows)
        cu_idx_hit = any(_parse_bool(r.get("vtrac_index_hit", "")) for r in cu_rows)

        cu_best_box = _best_cu_hit_row(cu_rows, hit_field="box_hit", exclude_methods=["union"])
        cu_best_idx = _best_cu_hit_row(cu_rows, hit_field="vtrac_index_hit", exclude_methods=["union"])

        play_row = play_grade_by_key.get(key, {})
        play_hit_any = _parse_bool(play_row.get("hit_any", "")) if play_row else False
        play_box_hit = _parse_bool(play_row.get("box_hit", "")) if play_row else False
        play_idx_hit = _parse_bool(play_row.get("vtrac_index_hit", "")) if play_row else False

        run_report = Path(row.get("source_run_report", "")) if row.get("source_run_report") else None
        winners_dir = REPO_ROOT / "sharepacks" / date / state / "winners" / state
        aux_summary_json = REPO_ROOT / "sharepacks" / date / state / "aux" / state / "summary.json"
        predictive_play_card = REPO_ROOT / "sharepacks" / "_predictive" / date / state / "play_card.json"
        predictive_cu = REPO_ROOT / "sharepacks" / "_predictive" / date / state / "candidate_universe.json"

        out_rows.append(
            {
                "date": date,
                "state": state,
                "period": period,
                "winner": winner,
                "winner_canonical": win_canon,
                "type": "triple" if win_is_triple else ("double" if win_is_double else ("mirror_double" if win_is_mirror_double else "")),
                "has_mirror_pair": str(win_has_mirror_pair),
                "mirror_pairs": ",".join(mirror_pairs),
                "vtrac_group_family": vtrac_family,
                "env_verdict": row.get("env_verdict", ""),
                "drivers": row.get("drivers", ""),
                # Control Center due doubles
                "cc_due_doubles_ds": due_ds,
                "cc_due_doubles_winner_in_family": str(_parse_bool(due_in_family_flag)) if due_in_family_flag else "",
                "cc_due_doubles_family_rank_match": due_family_rank,
                "cc_due_doubles_top_families": "; ".join(due_family_labels),
                # Aux audit
                "aux_draws_csv": _safe_rel(aux_draws_csv) if aux_draws_csv else "",
                "aux_ds_since_double": aux_ds_s,
                "cc_minus_aux_ds_delta": ds_delta,
                "aux_summary_json": _safe_rel(aux_summary_json) if aux_summary_json.exists() else "",
                # Tool metrics (selected)
                "winner_vtrac_index": trow.get("winner_vtrac_index", ""),
                "stable_exact_boxed": trow.get("stable_exact_boxed", ""),
                "stable_exact_straight": trow.get("stable_exact_straight", ""),
                "stable_vt_boxed_count": trow.get("stable_vt_boxed_count", ""),
                "hz_best_rank": trow.get("hz_top_lanes_best_rank", ""),
                "dr_exact_any": trow.get("dr_stamp_exact_any", ""),
                # Predictive grades (when present)
                "cu_hit_any": str(cu_hit_any) if cu_rows else "",
                "cu_box_hit": str(cu_box_hit) if cu_rows else "",
                "cu_index_hit": str(cu_idx_hit) if cu_rows else "",
                "cu_box_methods": ",".join(cu_box_methods),
                "cu_box_methods_non_union": ",".join(cu_box_methods_non_union),
                "cu_index_methods": ",".join(cu_idx_methods),
                "cu_index_methods_non_union": ",".join(cu_idx_methods_non_union),
                "cu_best_box_method": (cu_best_box or {}).get("method_id", ""),
                "cu_best_box_cost_units": (cu_best_box or {}).get("cost_units", ""),
                "cu_best_box_combos_count": (cu_best_box or {}).get("combos_count", ""),
                "cu_best_box_pack_id": (cu_best_box or {}).get("pack_id", ""),
                "cu_best_index_method": (cu_best_idx or {}).get("method_id", ""),
                "cu_best_index_cost_units": (cu_best_idx or {}).get("cost_units", ""),
                "cu_best_index_combos_count": (cu_best_idx or {}).get("combos_count", ""),
                "cu_best_index_pack_id": (cu_best_idx or {}).get("pack_id", ""),
                "play_card_hit_any": str(play_hit_any) if play_row else "",
                "play_card_box_hit": str(play_box_hit) if play_row else "",
                "play_card_index_hit": str(play_idx_hit) if play_row else "",
                # Evidence pointers
                "run_report": _safe_rel(run_report) if run_report else "",
                "winners_dir": _safe_rel(winners_dir) if winners_dir.exists() else "",
                "predictive_candidate_universe": _safe_rel(predictive_cu) if predictive_cu.exists() else "",
                "predictive_play_card": _safe_rel(predictive_play_card) if predictive_play_card.exists() else "",
            }
        )

    out_rows.sort(key=lambda r: (r["date"], r["state"], r["period"]))

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_deep.parent.mkdir(parents=True, exist_ok=True)

    # Write CSV
    cols = list(out_rows[0].keys()) if out_rows else []
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(out_rows)

    # Aggregate stats for Markdown
    type_counts = Counter(r["type"] for r in out_rows if r.get("type"))
    mirror_pair_counts = Counter()
    for r in out_rows:
        for mp in (r.get("mirror_pairs") or "").split(","):
            if mp:
                mirror_pair_counts[mp] += 1

    # Write inventory MD
    lines: List[str] = []
    lines.append("# Doubles + Mirror-Doubles — Inventory (Gold-Day Corpus)")
    lines.append("")
    lines.append(f"- Generated: `{_now_iso()}`")
    lines.append(f"- Source corpus: `{_safe_rel(corpus_summary)}`")
    lines.append(f"- Rows (filtered): `{len(out_rows)}`")
    lines.append("")
    lines.append("## Breakdown")
    lines.append("")
    if type_counts:
        for k in ("double", "triple", "mirror_double"):
            if k in type_counts:
                lines.append(f"- {k}: `{type_counts[k]}`")
    if mirror_pair_counts:
        top = ", ".join(f"{k}:{v}" for k, v in mirror_pair_counts.most_common(5))
        lines.append(f"- Top mirror pairs (by count): `{top}`")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append(f"- CSV: `{_safe_rel(out_csv)}`")
    lines.append(f"- Deep dive: `{_safe_rel(out_deep)}`")
    lines.append("")
    lines.append("## Snapshot (first 40 rows)")
    lines.append("")
    lines.append("| Date | State | Period | Winner | Type | MirrorPairs | CC DS | Aux DS | CU Box | Play Box | Run Report |")
    lines.append("|---|---|---|---:|---|---|---:|---:|---:|---:|---|")
    for r in out_rows[:40]:
        lines.append(
            "| "
            + " | ".join(
                [
                    r.get("date", ""),
                    r.get("state", ""),
                    r.get("period", ""),
                    r.get("winner", ""),
                    r.get("type", ""),
                    r.get("mirror_pairs", ""),
                    r.get("cc_due_doubles_ds", ""),
                    r.get("aux_ds_since_double", ""),
                    r.get("cu_box_hit", ""),
                    r.get("play_card_box_hit", ""),
                    r.get("run_report", ""),
                ]
            )
            + " |"
        )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Write deep dive MD (auto-generated, evidence-first)
    dd: List[str] = []
    dd.append("# Doubles + Mirror-Doubles — Deep Dive (Evidence Pointers + Quick Audit)")
    dd.append("")
    dd.append(f"- Generated: `{_now_iso()}`")
    dd.append(f"- Rows: `{len(out_rows)}`")
    dd.append("")
    dd.append("## Interpretation notes (so we don’t contaminate)")
    dd.append("")
    dd.append("- This report is **post-results** analysis. It links to winners lens + Master Validation RUNS and also to pre-results predictive grades when available.")
    dd.append("- `aux_ds_since_double` and `cc_due_doubles_ds` are computed from the **pre-results** Aux snapshot (history workbook H = D-1), i.e. the state of the world before results date D posted.")
    dd.append("- `Type=mirror_double` means the winner contains a full VTRAC mirror pair (0/5,1/6,2/7,3/8,4/9) but is not itself a double/triple.")
    dd.append("")
    dd.append("## High-priority audit: CC vs Aux DS")
    dd.append("")
    dd.append("Rows where `cc_minus_aux_ds_delta != 0` (should be rare; investigate if recurring):")
    dd.append("")
    dd.append("| Date | State | Period | Winner | Type | CC DS | Aux DS | Delta | Aux CSV |")
    dd.append("|---|---|---|---:|---|---:|---:|---:|---|")
    mismatches = [r for r in out_rows if r.get("cc_minus_aux_ds_delta") not in ("", "0")]
    for r in mismatches[:50]:
        dd.append(
            "| "
            + " | ".join(
                [
                    r.get("date", ""),
                    r.get("state", ""),
                    r.get("period", ""),
                    r.get("winner", ""),
                    r.get("type", ""),
                    r.get("cc_due_doubles_ds", ""),
                    r.get("aux_ds_since_double", ""),
                    r.get("cc_minus_aux_ds_delta", ""),
                    r.get("aux_draws_csv", ""),
                ]
            )
            + " |"
        )
    if not mismatches:
        dd.append("| *(none)* | | | | | | | | |")
    dd.append("")
    dd.append("## Predictive coverage (when available)")
    dd.append("")
    dd.append("Rows where Candidate Universe or Play Card achieved a **BOX hit** (useful for learning which method_ids convert lane/index pressure into box coverage):")
    dd.append("")
    dd.append("| Date | State | Period | Winner | Type | CU Box | CU Best (non-union) | CU Cost | Play Box | Play Index |")
    dd.append("|---|---|---|---:|---|---:|---|---:|---:|---:|")
    hits = [r for r in out_rows if r.get("cu_box_hit") == "True" or r.get("play_card_box_hit") == "True"]
    for r in hits[:80]:
        dd.append(
            "| "
            + " | ".join(
                [
                    r.get("date", ""),
                    r.get("state", ""),
                    r.get("period", ""),
                    r.get("winner", ""),
                    r.get("type", ""),
                    r.get("cu_box_hit", ""),
                    r.get("cu_best_box_method", "") or ("union" if r.get("cu_box_hit") == "True" else ""),
                    r.get("cu_best_box_cost_units", ""),
                    r.get("play_card_box_hit", ""),
                    r.get("play_card_index_hit", ""),
                ]
            )
            + " |"
        )
    if not hits:
        dd.append("| *(none)* | | | | | | | | | |")
    dd.append("")
    dd.append("## Per-event evidence pointers")
    dd.append("")
    for r in out_rows:
        dd.append(f"### {r['date']} — {r['state']} — {r['period']} — {r['winner']} ({r.get('type','')})")
        dd.append("")
        dd.append(f"- Winner canonical: `{r.get('winner_canonical','')}`")
        dd.append(f"- Mirror pairs: `{r.get('mirror_pairs','')}` | vtrac_group_family: `{r.get('vtrac_group_family','')}`")
        dd.append(f"- Control Center due-doubles: DS=`{r.get('cc_due_doubles_ds','')}` family_rank_match=`{r.get('cc_due_doubles_family_rank_match','')}` winner_in_family=`{r.get('cc_due_doubles_winner_in_family','')}`")
        dd.append(f"- Aux DS audit: DS=`{r.get('aux_ds_since_double','')}` delta(cc-aux)=`{r.get('cc_minus_aux_ds_delta','')}` draws=`{r.get('aux_draws_csv','')}`")
        if r.get("cu_hit_any"):
            dd.append(
                "- Candidate Universe: "
                + f"box_hit=`{r.get('cu_box_hit','')}` "
                + f"idx_hit=`{r.get('cu_index_hit','')}` "
                + f"best_box=`{r.get('cu_best_box_method','')}`@`{r.get('cu_best_box_cost_units','')}` "
                + f"box_methods_non_union=`{r.get('cu_box_methods_non_union','')}`"
            )
        if r.get("play_card_hit_any"):
            dd.append(f"- Play Card: box_hit=`{r.get('play_card_box_hit','')}` idx_hit=`{r.get('play_card_index_hit','')}`")
        dd.append(f"- RUNS report: `{r.get('run_report','')}`")
        dd.append(f"- Winners lens: `{r.get('winners_dir','')}`")
        if r.get("predictive_candidate_universe"):
            dd.append(f"- Predictive Candidate Universe: `{r.get('predictive_candidate_universe','')}`")
        if r.get("predictive_play_card"):
            dd.append(f"- Predictive Play Card: `{r.get('predictive_play_card','')}`")
        dd.append("")
    out_deep.write_text("\n".join(dd) + "\n", encoding="utf-8")

    print(f"[OK] Wrote: {out_csv}")
    print(f"[OK] Wrote: {out_md}")
    print(f"[OK] Wrote: {out_deep}")


if __name__ == "__main__":
    main()
