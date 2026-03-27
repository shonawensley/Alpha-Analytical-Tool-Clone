#!/usr/bin/env python3
"""
Build an inventory of "double" and "mirror-double" winners across a gold-day window.

This is a reporting-only tool:
- Enumerates winner events from frozen `data/results/<D>.txt` files.
- Optionally enriches those events from RUNS corpus exports + frozen sharepacks
  (Aux + Control Center + predictive grades).
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
RESULTS_DIR = REPO_ROOT / "data" / "results"

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


def _pick_winners_json(winners_dir: Path, *, winner_literal: str) -> Optional[Path]:
    """
    Winners lens JSON files are named like:
      <STATE>_vtrac<IDX>_winner_<WINNER>_<STAMP>.json
    """
    if not winners_dir.exists():
        return None
    w = _normalize_pick3_literal(winner_literal)
    if not w:
        return None
    matches = sorted(winners_dir.glob(f"*winner_{w}_*.json"))
    return matches[-1] if matches else None


def _draw_num(draw_label: str) -> Optional[int]:
    m = re.match(r"^Draw(?P<n>\d+)$", str(draw_label).strip())
    if not m:
        return None
    try:
        return int(m.group("n"))
    except Exception:
        return None


def _winners_lens_set1_col12_metrics(winners_json: Path, *, focus_variant: str) -> Dict[str, str]:
    """
    Extract a few stable, comparable metrics from the winners JSON "string table lens".

    Focus region:
    - variant = focus_variant (Midday or Evening)
    - Set1 only
    - RowType in {R2,R4,R6,R8}
    - columns 1 and 2 only (col1/col2 ladder lens)
    """
    try:
        obj = json.loads(winners_json.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return {}
    tables = obj.get("tables") if isinstance(obj, dict) else None
    if not isinstance(tables, dict):
        return {}

    variants = [v for v in ("Midday", "Evening", "Combined") if v in tables]
    focus_rows = tables.get(focus_variant, [])
    if not isinstance(focus_rows, list):
        focus_rows = []

    tag_counts = Counter()
    draws_with_family = set()
    draws_with_winner = set()
    samples: List[str] = []

    def scan_variant(rows: Sequence[Dict[str, object]]) -> Tuple[bool, bool]:
        any_family = False
        any_winner = False
        for r in rows:
            if not isinstance(r, dict):
                continue
            if r.get("Set") != "Set1":
                continue
            if r.get("RowType") not in ("R2", "R4", "R6", "R8"):
                continue
            draw = str(r.get("Draw") or "")
            cells = r.get("cells") if isinstance(r.get("cells"), dict) else {}
            for col in ("1", "2"):
                cell = cells.get(col) if isinstance(cells, dict) else None
                if not isinstance(cell, dict):
                    continue
                tags = cell.get("tags") if isinstance(cell.get("tags"), list) else []
                tags = [str(t) for t in tags]
                if "hit-family" in tags:
                    any_family = True
                if "hit-winner" in tags:
                    any_winner = True
        return any_family, any_winner

    # focus variant metrics + samples
    for r in focus_rows:
        if not isinstance(r, dict):
            continue
        if r.get("Set") != "Set1":
            continue
        if r.get("RowType") not in ("R2", "R4", "R6", "R8"):
            continue
        draw = str(r.get("Draw") or "")
        cells = r.get("cells") if isinstance(r.get("cells"), dict) else {}
        for col in ("1", "2"):
            cell = cells.get(col) if isinstance(cells, dict) else None
            if not isinstance(cell, dict):
                continue
            tags = cell.get("tags") if isinstance(cell.get("tags"), list) else []
            tags = [str(t) for t in tags]
            if not tags:
                continue
            for t in tags:
                tag_counts[t] += 1
            if "hit-family" in tags:
                draws_with_family.add(draw)
            if "hit-winner" in tags:
                draws_with_winner.add(draw)
            if any(t.startswith("hit-") for t in tags) and len(samples) < 6:
                txt = str(cell.get("text") or "")
                txt = txt.replace("\n", " ").strip()
                if len(txt) > 36:
                    txt = txt[:36] + "…"
                samples.append(f"{draw}:{r.get('RowType')} col{col} {txt} [{','.join(tags)}]")

    # Cross-variant presence (family/winner hits) in the same Set1 col1/2 region.
    xvar_family = 0
    xvar_winner = 0
    for v in variants:
        rows = tables.get(v, [])
        if not isinstance(rows, list):
            continue
        any_family, any_winner = scan_variant(rows)
        xvar_family += 1 if any_family else 0
        xvar_winner += 1 if any_winner else 0

    # Draw recency summary
    family_draw_nums = [_draw_num(d) for d in draws_with_family]
    family_draw_nums = [n for n in family_draw_nums if n is not None]
    winner_draw_nums = [_draw_num(d) for d in draws_with_winner]
    winner_draw_nums = [n for n in winner_draw_nums if n is not None]

    def fmt_min(nums: Sequence[int]) -> str:
        return str(min(nums)) if nums else ""

    return {
        "winners_json": _safe_rel(winners_json),
        "winners_index": str(obj.get("index", "")) if isinstance(obj, dict) else "",
        "wl_focus_set1_col12_hit_family_cells": str(tag_counts.get("hit-family", 0)),
        "wl_focus_set1_col12_hit_winner_cells": str(tag_counts.get("hit-winner", 0)),
        "wl_focus_set1_col12_hit_vt_straight_cells": str(tag_counts.get("hit-vt-straight", 0)),
        "wl_focus_set1_col12_ls_box_cells": str(tag_counts.get("ls-box", 0)),
        "wl_focus_set1_col12_family_draws_count": str(len(draws_with_family)),
        "wl_focus_set1_col12_winner_draws_count": str(len(draws_with_winner)),
        "wl_focus_set1_col12_family_recentest_draw": fmt_min(family_draw_nums),
        "wl_focus_set1_col12_winner_recentest_draw": fmt_min(winner_draw_nums),
        "wl_xvar_set1_col12_family_variants": str(xvar_family),
        "wl_xvar_set1_col12_winner_variants": str(xvar_winner),
        "wl_focus_set1_col12_samples": " | ".join(samples),
    }


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


@dataclass(frozen=True)
class _Winner:
    midday: Optional[str]
    evening: Optional[str]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _load_results_winners(results_file: Path) -> Dict[str, _Winner]:
    """
    Parse data/results/<D>.txt into {StateKey: Winner(midday, evening)} using the
    project's canonical state mapping.
    """
    if not results_file.exists():
        return {}
    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        _PROJECT_STATE_CANDIDATES,
        parse_winner_sheet,
    )

    entries = parse_winner_sheet(_read_text(results_file))
    winners: Dict[str, _Winner] = {}
    for entry in entries:
        canonical = getattr(entry, "canonical", None)
        midday = getattr(entry, "midday", None)
        evening = getattr(entry, "evening", None)
        if not canonical:
            continue
        candidates = _PROJECT_STATE_CANDIDATES.get(canonical)
        if not candidates:
            project_state = getattr(entry, "project_state", None)
            candidates = (project_state,) if project_state else ()
        for state_key in candidates:
            if not state_key:
                continue
            winners[state_key] = _Winner(
                midday=_normalize_pick3_literal(midday or ""),
                evening=_normalize_pick3_literal(evening or ""),
            )
    return winners


def _state_has_sharepack(
    *,
    date: str,
    state: str,
    predictive_sharepacks_root: Path,
    truth_sharepacks_root: Path,
) -> bool:
    return (
        (predictive_sharepacks_root / date / state).exists()
        or (truth_sharepacks_root / date / state).exists()
    )


def _iter_result_events(
    *,
    results_root: Path,
    predictive_sharepacks_root: Path,
    truth_sharepacks_root: Path,
    start: Optional[str],
    end: Optional[str],
) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for results_file in sorted(results_root.glob("*.txt")):
        date = results_file.stem
        if not _DATE_RE.match(date):
            continue
        if not _date_in_range(date, start, end):
            continue
        winners = _load_results_winners(results_file)
        for state, winner in sorted(winners.items()):
            if not _state_has_sharepack(
                date=date,
                state=state,
                predictive_sharepacks_root=predictive_sharepacks_root,
                truth_sharepacks_root=truth_sharepacks_root,
            ):
                continue
            for period, literal in (("Midday", winner.midday or ""), ("Evening", winner.evening or "")):
                literal = _normalize_pick3_literal(literal)
                if not literal:
                    continue
                rows.append(
                    {
                        "date": date,
                        "state": state,
                        "period": period,
                        "winner": literal,
                    }
                )
    return rows


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Create doubles + mirror-doubles inventory across gold-day RUNS corpus.")
    p.add_argument("--runs-dir", default=str(RUNS_DIR), help="RUNS directory (default: docs/.../RUNS)")
    p.add_argument("--grades-runs-dir", default=str(RUNS_DIR), help="RUNS directory holding predictive grade CSVs (default: docs/.../RUNS)")
    p.add_argument("--results-root", default=str(RESULTS_DIR), help="Root containing data/results/<D>.txt files (default: data/results)")
    p.add_argument("--predictive-sharepacks-root", default="sharepacks/_predictive", help="Predictive sharepacks root used to filter to active arena states")
    p.add_argument("--truth-sharepacks-root", default="sharepacks", help="Truth/frozen sharepacks root used to filter to active arena states")
    p.add_argument("--corpus-summary", default="", help="Optional corpus_summary.csv for legacy MV enrichment")
    p.add_argument("--corpus-tool-metrics", default="", help="Optional corpus_tool_metrics.csv for tool-metric enrichment")
    p.add_argument("--run-report-dir", default=None, help="Optional directory containing per-state validation reports to prefer for run_report links")
    p.add_argument("--out-csv", default=None, help="Override CSV output path")
    p.add_argument("--out-md", default=None, help="Override Markdown inventory output path")
    p.add_argument("--out-deep-dive", default=None, help="Override Markdown deep dive output path")
    p.add_argument("--out-study-queue", default=None, help="Override Markdown study queue output path")
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
    grades_runs_dir = Path(args.grades_runs_dir)
    results_root = Path(args.results_root)
    predictive_sharepacks_root = Path(args.predictive_sharepacks_root)
    truth_sharepacks_root = Path(args.truth_sharepacks_root)
    corpus_summary = Path(args.corpus_summary) if args.corpus_summary else None
    corpus_tool_metrics = Path(args.corpus_tool_metrics) if args.corpus_tool_metrics else None
    run_report_dir = Path(args.run_report_dir) if args.run_report_dir else None

    if not results_root.exists():
        raise SystemExit(f"Missing results root: {results_root}")
    if not predictive_sharepacks_root.exists():
        raise SystemExit(f"Missing predictive sharepacks root: {predictive_sharepacks_root}")
    if not truth_sharepacks_root.exists():
        raise SystemExit(f"Missing truth sharepacks root: {truth_sharepacks_root}")

    if args.from_date and not _DATE_RE.match(args.from_date.strip()):
        raise SystemExit("--from-date must be YYYY-MM-DD")
    if args.to_date and not _DATE_RE.match(args.to_date.strip()):
        raise SystemExit("--to-date must be YYYY-MM-DD")

    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / "DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / "DOUBLES_MIRROR_DOUBLES__INVENTORY.md"
    out_deep = Path(args.out_deep_dive) if args.out_deep_dive else runs_dir / "DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md"
    out_study = Path(args.out_study_queue) if args.out_study_queue else runs_dir / "DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md"

    # Optional legacy MV enrichment by (date,state,period)
    summary_meta: Dict[_EventKey, Dict[str, str]] = {}
    if corpus_summary and corpus_summary.exists():
        for row in _read_csv_dicts(corpus_summary):
            key = _EventKey(row.get("date", ""), row.get("state", ""), row.get("period", ""))
            if key.date and key.state and key.period:
                summary_meta[key] = row

    # Optional tool-metrics enrichment by (date,state,period)
    tool_rows = _read_csv_dicts(corpus_tool_metrics) if corpus_tool_metrics and corpus_tool_metrics.exists() else []
    tool_by_key: Dict[_EventKey, Dict[str, str]] = {}
    for row in tool_rows:
        key = _EventKey(row.get("date", ""), row.get("state", ""), row.get("period", ""))
        if key.date and key.state and key.period:
            tool_by_key[key] = row

    # Candidate Universe + play card grades exist only for some dates.
    cu_grade_by_key: Dict[_EventKey, List[Dict[str, str]]] = defaultdict(list)
    play_grade_by_key: Dict[_EventKey, Dict[str, str]] = {}
    for grade_path in sorted(grades_runs_dir.glob("*__CANDIDATE_UNIVERSE_GRADE.csv")):
        date = grade_path.name.split("__", 1)[0]
        for row in _read_csv_dicts(grade_path):
            key = _EventKey(date, row.get("state_key", ""), row.get("winner_label", ""))
            if key.state and key.period:
                cu_grade_by_key[key].append(row)
    for grade_path in sorted(grades_runs_dir.glob("*__PLAY_CARD_GRADE.csv")):
        date = grade_path.name.split("__", 1)[0]
        for row in _read_csv_dicts(grade_path):
            key = _EventKey(date, row.get("state_key", ""), row.get("winner_label", ""))
            if key.state and key.period:
                play_grade_by_key[key] = row

    result_rows = _iter_result_events(
        results_root=results_root,
        predictive_sharepacks_root=predictive_sharepacks_root,
        truth_sharepacks_root=truth_sharepacks_root,
        start=args.from_date,
        end=args.to_date,
    )
    dates = sorted({r.get("date", "") for r in result_rows if r.get("date", "")})

    due_by_date: Dict[str, Dict[Tuple[str, str], Dict[str, str]]] = {}
    for d in dates:
        if not _date_in_range(d, args.from_date, args.to_date):
            continue
        due_by_date[d] = _read_due_doubles_by_date(d)

    out_rows: List[Dict[str, str]] = []
    wl_defaults: Dict[str, str] = {
        "winners_json": "",
        "winners_index": "",
        "wl_focus_set1_col12_hit_family_cells": "",
        "wl_focus_set1_col12_hit_winner_cells": "",
        "wl_focus_set1_col12_hit_vt_straight_cells": "",
        "wl_focus_set1_col12_ls_box_cells": "",
        "wl_focus_set1_col12_family_draws_count": "",
        "wl_focus_set1_col12_winner_draws_count": "",
        "wl_focus_set1_col12_family_recentest_draw": "",
        "wl_focus_set1_col12_winner_recentest_draw": "",
        "wl_xvar_set1_col12_family_variants": "",
        "wl_xvar_set1_col12_winner_variants": "",
        "wl_focus_set1_col12_samples": "",
    }

    for row in result_rows:
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
        srow = summary_meta.get(key, {})

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

        preferred_run_report = None
        if run_report_dir:
            candidate = run_report_dir / f"{date}__{state}.md"
            if candidate.exists():
                preferred_run_report = candidate
        run_report = preferred_run_report or (Path(srow.get("source_run_report", "")) if srow.get("source_run_report") else None)
        winners_dir = REPO_ROOT / "sharepacks" / date / state / "winners" / state
        winners_json = _pick_winners_json(winners_dir, winner_literal=winner)
        aux_summary_json = REPO_ROOT / "sharepacks" / date / state / "aux" / state / "summary.json"
        predictive_play_card = REPO_ROOT / "sharepacks" / "_predictive" / date / state / "play_card.json"
        predictive_cu = REPO_ROOT / "sharepacks" / "_predictive" / date / state / "candidate_universe.json"

        winners_lens = dict(wl_defaults)
        if winners_json:
            winners_lens.update(_winners_lens_set1_col12_metrics(winners_json, focus_variant=period))

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
                "env_verdict": srow.get("env_verdict", ""),
                "pack": srow.get("pack", ""),
                "drivers": srow.get("drivers", ""),
                "fix_later": srow.get("fix_later", ""),
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
                **winners_lens,
            }
        )

    out_rows.sort(key=lambda r: (r["date"], r["state"], r["period"]))

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_deep.parent.mkdir(parents=True, exist_ok=True)

    # Write CSV
    cols: List[str] = []
    for r in out_rows:
        for k in r.keys():
            if k not in cols:
                cols.append(k)
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
    lines.append(f"- Event source: `{_safe_rel(results_root)}` (`data/results/<D>.txt`)")
    lines.append(f"- Grade joins source: `{_safe_rel(grades_runs_dir)}`")
    if corpus_summary and corpus_summary.exists():
        lines.append(f"- Optional MV enrichment corpus: `{_safe_rel(corpus_summary)}`")
    if corpus_tool_metrics and corpus_tool_metrics.exists():
        lines.append(f"- Optional tool-metrics corpus: `{_safe_rel(corpus_tool_metrics)}`")
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
    deep_line_by_key: Dict[_EventKey, int] = {}
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
    dd.append("## Winners lens quick stats (Set1 col1/2 ladder)")
    dd.append("")
    dd.append("Computed from the winners JSON lens for the same event (focus variant = period).")
    dd.append("")
    dd.append("| Type | Rows | Any hit-family | Any hit-winner | Any hit-vt-straight | Any ls-box | Avg family cells | Avg winner cells | Avg xvar family | Avg xvar winner |")
    dd.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    def wl_i(r: Dict[str, str], key: str) -> int:
        return _parse_int(r.get(key, "")) or 0

    def wl_avg(rows: Sequence[Dict[str, str]], key: str) -> str:
        if not rows:
            return ""
        return f"{sum(wl_i(r, key) for r in rows) / len(rows):.2f}"

    for t in ("double", "triple", "mirror_double"):
        trows = [r for r in out_rows if r.get("type") == t and r.get("winners_json")]
        if not trows:
            continue
        dd.append(
            "| "
            + " | ".join(
                [
                    t,
                    str(len(trows)),
                    str(sum(1 for r in trows if wl_i(r, "wl_focus_set1_col12_hit_family_cells") > 0)),
                    str(sum(1 for r in trows if wl_i(r, "wl_focus_set1_col12_hit_winner_cells") > 0)),
                    str(sum(1 for r in trows if wl_i(r, "wl_focus_set1_col12_hit_vt_straight_cells") > 0)),
                    str(sum(1 for r in trows if wl_i(r, "wl_focus_set1_col12_ls_box_cells") > 0)),
                    wl_avg(trows, "wl_focus_set1_col12_hit_family_cells"),
                    wl_avg(trows, "wl_focus_set1_col12_hit_winner_cells"),
                    wl_avg(trows, "wl_xvar_set1_col12_family_variants"),
                    wl_avg(trows, "wl_xvar_set1_col12_winner_variants"),
                ]
            )
            + " |"
        )
    dd.append("")
    dd.append("## Per-event evidence pointers")
    dd.append("")
    for r in out_rows:
        deep_line_by_key[_EventKey(r["date"], r["state"], r["period"])] = len(dd) + 1
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
        dd.append(f"- Winners lens dir: `{r.get('winners_dir','')}`")
        if r.get("winners_json"):
            dd.append(f"- Winners lens JSON: `{r.get('winners_json','')}` (index `{r.get('winners_index','')}`)")
            dd.append(
                "- Winners lens Set1 col1/2 (focus variant = period): "
                + f"hit-family-cells=`{r.get('wl_focus_set1_col12_hit_family_cells','')}` "
                + f"hit-winner-cells=`{r.get('wl_focus_set1_col12_hit_winner_cells','')}` "
                + f"hit-vt-straight-cells=`{r.get('wl_focus_set1_col12_hit_vt_straight_cells','')}` "
                + f"ls-box-cells=`{r.get('wl_focus_set1_col12_ls_box_cells','')}` "
                + f"xvar-family-variants=`{r.get('wl_xvar_set1_col12_family_variants','')}` "
                + f"xvar-winner-variants=`{r.get('wl_xvar_set1_col12_winner_variants','')}`"
            )
            dd.append(
                "- Set1 col1/2 draw recency: "
                + f"family_draws=`{r.get('wl_focus_set1_col12_family_draws_count','')}` "
                + f"winner_draws=`{r.get('wl_focus_set1_col12_winner_draws_count','')}` "
                + f"family_recentest_draw=`{r.get('wl_focus_set1_col12_family_recentest_draw','')}` "
                + f"winner_recentest_draw=`{r.get('wl_focus_set1_col12_winner_recentest_draw','')}`"
            )
            if r.get("wl_focus_set1_col12_samples"):
                dd.append(f"- Winners lens samples: `{r.get('wl_focus_set1_col12_samples','')}`")
        if r.get("predictive_candidate_universe"):
            dd.append(f"- Predictive Candidate Universe: `{r.get('predictive_candidate_universe','')}`")
        if r.get("predictive_play_card"):
            dd.append(f"- Predictive Play Card: `{r.get('predictive_play_card','')}`")
        dd.append("")
    out_deep.write_text("\n".join(dd) + "\n", encoding="utf-8")

    # Write study queue MD (mirror-double index-hit -> box-miss)
    out_study.parent.mkdir(parents=True, exist_ok=True)
    queue = [
        r
        for r in out_rows
        if r.get("type") == "mirror_double"
        and r.get("cu_index_hit") == "True"
        and r.get("cu_box_hit") != "True"
    ]

    def wl_i(r: Dict[str, str], key: str) -> int:
        return _parse_int(r.get(key, "")) or 0

    def date_i(d: str) -> int:
        try:
            return int(str(d).replace("-", ""))
        except Exception:
            return 0

    def sort_key(r: Dict[str, str]) -> Tuple[int, int, int, int, str, str]:
        return (
            -wl_i(r, "wl_focus_set1_col12_hit_family_cells"),
            -wl_i(r, "wl_focus_set1_col12_hit_winner_cells"),
            -wl_i(r, "wl_focus_set1_col12_hit_vt_straight_cells"),
            -date_i(r.get("date", "")),
            r.get("state", ""),
            r.get("period", ""),
        )

    queue_sorted = sorted(queue, key=sort_key)

    sq: List[str] = []
    sq.append("# Doubles + Mirror-Doubles — Study Queue (Index Hit → Box Miss)")
    sq.append("")
    sq.append(f"- Generated: `{_now_iso()}`")
    sq.append(f"- Source: `{_safe_rel(out_csv)}`")
    sq.append("")
    sq.append(
        "Purpose: review **mirror-double** events where the predictive **Candidate Universe hit the VTRAC/index lane** (`cu_index_hit=True`) but **missed the exact box** (`cu_box_hit=False`)."
    )
    sq.append("These are the highest-leverage examples for designing **bounded closure packs** that convert “lane hits” into “box hits” without changing analyzers.")
    sq.append("")
    sq.append("How to use each row:")
    sq.append("- Open the deep-dive section (line pointer) for winners-lens Set1 col1/2 samples + evidence paths.")
    sq.append("- Open the Master Validation run report for the full post-results analysis context.")
    sq.append("- Open the predictive artifacts for the same day/state (`candidate_universe.json`, `play_card.json`) to see what we actually played pre-results.")
    sq.append("")
    sq.append(
        "| Rank | Date | State | Period | Winner | Canon | MirrorPair | VTRAC idx | WL family cells | WL winner cells | WL vt-straight cells | Best CU index method | Play idx hit | Deep dive | Run report | Predictive CU | Predictive Play Card |"
    )
    sq.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for rank, r in enumerate(queue_sorted, start=1):
        key = _EventKey(r.get("date", ""), r.get("state", ""), r.get("period", ""))
        line = deep_line_by_key.get(key)
        deep_ptr = f"{_safe_rel(out_deep)}:{int(line)}" if line else _safe_rel(out_deep)
        sq.append(
            "| "
            + " | ".join(
                [
                    str(rank),
                    r.get("date", ""),
                    r.get("state", ""),
                    r.get("period", ""),
                    r.get("winner", ""),
                    r.get("winner_canonical", ""),
                    r.get("mirror_pairs", ""),
                    r.get("winner_vtrac_index", ""),
                    r.get("wl_focus_set1_col12_hit_family_cells", ""),
                    r.get("wl_focus_set1_col12_hit_winner_cells", ""),
                    r.get("wl_focus_set1_col12_hit_vt_straight_cells", ""),
                    r.get("cu_best_index_method", ""),
                    r.get("play_card_index_hit", ""),
                    f"`{deep_ptr}`",
                    f"`{r.get('run_report','')}`",
                    f"`{r.get('predictive_candidate_universe','')}`",
                    f"`{r.get('predictive_play_card','')}`",
                ]
            )
            + " |"
        )
    out_study.write_text("\n".join(sq).rstrip() + "\n", encoding="utf-8")

    print(f"[OK] Wrote: {out_csv}")
    print(f"[OK] Wrote: {out_md}")
    print(f"[OK] Wrote: {out_deep}")
    print(f"[OK] Wrote: {out_study}")


if __name__ == "__main__":
    main()
