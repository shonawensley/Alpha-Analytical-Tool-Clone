#!/usr/bin/env python3
"""
Validate Profit Alerts (Control Center) contract across one or more sharepack days.

This is validation-only:
  - It does not modify analyzers.
  - It reads sharepacks/<D>/control_center/profit_alerts.csv (+ optional profit_alerts_eval.csv).

Primary goal: catch regressions that break auditability / gradeability:
  - BOX rows must have sorted canonical + explicit implied_set perms (non-promoter).
  - BOX implied_set must match the boxed family of canonical.
  - A08 must include base-candidate pointers in Evidence.
  - A11 must include star fields in Evidence.

Usage:
  python3 scripts/tools/validate_profit_alerts_contract.py --date 2025-06-21
  python3 scripts/tools/validate_profit_alerts_contract.py --start 2025-12-30 --end 2026-01-09
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[2]


CANONICAL_OPTIONAL_ALERT_IDS = {"A09"}  # lane-set plays (canonical may be blank/"-")
PROMOTER_ALERT_IDS = {"A03", "A08"}


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def daterange(start: str, end: str) -> List[str]:
    s = parse_date(start)
    e = parse_date(end)
    if e < s:
        raise SystemExit("--end must be >= --start")
    out: List[str] = []
    cur = s
    while cur <= e:
        out.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return out


def safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def is_pick3(label: str) -> bool:
    return bool(re.fullmatch(r"\d{3}", (label or "").strip()))


def canon_box_label(label: str) -> str:
    raw = (label or "").strip()
    if not is_pick3(raw):
        return ""
    return "".join(sorted(raw))


def perm_count_in_box(canonical_box: str) -> Optional[int]:
    c = (canonical_box or "").strip()
    if not is_pick3(c):
        return None
    uniq = len(set(c))
    if uniq == 1:
        return 1
    if uniq == 2:
        return 3
    return 6


def expected_implied_size(suggested_u: str, canonical: str) -> Optional[int]:
    k = (suggested_u or "").strip().upper()
    if not k:
        return None
    if k in {"OVERLAY", "SKIP"}:
        return 0
    if k == "STR8_8":
        return 8
    if k == "STR8_4OF8":
        return 4
    if k == "STR8_3":
        pc = perm_count_in_box(canon_box_label(canonical))
        return None if pc is None else min(3, pc)
    if k == "BOX":
        return perm_count_in_box(canon_box_label(canonical))
    return None


def parse_implied_set(raw: str) -> Tuple[List[str], Optional[str]]:
    s = (raw or "").strip()
    if not s or s == "-":
        return ([], None)
    try:
        obj = json.loads(s)
        if not isinstance(obj, list):
            return ([], "NOT_A_LIST")
        out: List[str] = []
        for item in obj:
            if isinstance(item, str):
                out.append(item.strip())
            else:
                out.append(str(item))
        return (out, None)
    except Exception:
        return ([], "JSON_PARSE_ERROR")


def parse_evidence(raw: str) -> Tuple[Dict[str, object], Optional[str]]:
    s = (raw or "").strip()
    if not s or s == "-":
        return ({}, None)
    try:
        obj = json.loads(s)
        if not isinstance(obj, dict):
            return ({}, "NOT_A_DICT")
        return (obj, None)
    except Exception:
        return ({}, "JSON_PARSE_ERROR")


def load_csv_rows(path: Path) -> Iterable[Dict[str, str]]:
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: (v or "") for k, v in row.items()}


@dataclass(frozen=True)
class Violation:
    results_date: str
    row_num: str
    state_key: str
    variant: str
    alert_id: str
    code: str
    detail: str


def _expected_eval_row_type(*, suggested_u: str, alert_id: str) -> str:
    if suggested_u in {"OVERLAY", "SKIP"}:
        return "PROMOTER"
    if alert_id == "A11":
        return "GOVERNOR"
    return "CANDIDATE"


def validate_day(d: str, *, sharepacks_root: Path, require_eval: bool) -> Tuple[List[Violation], Counter]:
    violations: List[Violation] = []
    counters: Counter = Counter()

    cc_dir = sharepacks_root / d / "control_center"
    board_path = cc_dir / "profit_alerts.csv"
    eval_path = cc_dir / "profit_alerts_eval.csv"

    if not board_path.exists():
        violations.append(Violation(d, "-", "-", "-", "-", "MISSING_BOARD", str(board_path)))
        return (violations, counters)

    board_rows = list(load_csv_rows(board_path))
    counters["board_rows"] += len(board_rows)

    # Map board row index -> row for eval cross-checks.
    def board_at_row_num(row_num: str) -> Optional[Dict[str, str]]:
        idx = safe_int(row_num)
        if idx is None or idx <= 0:
            return None
        if idx > len(board_rows):
            return None
        return board_rows[idx - 1]

    # --- Board contract checks ---
    for idx, br in enumerate(board_rows, start=1):
        alert_id = (br.get("AlertId") or "").strip().upper()
        suggested_u = (br.get("Suggested") or "").strip().upper()
        state_key = (br.get("StateKey") or "").strip()
        variant = (br.get("Variant") or "").strip()
        canonical = (br.get("Canonical") or "").strip()

        implied, implied_err = parse_implied_set(br.get("ImpliedSet") or "")
        evidence, evidence_err = parse_evidence(br.get("Evidence") or "")

        # Basic JSON sanity (non-fatal).
        if implied_err:
            counters[f"implied_err:{implied_err}"] += 1
        if evidence_err:
            counters[f"evidence_err:{evidence_err}"] += 1

        is_promoter = alert_id in PROMOTER_ALERT_IDS or suggested_u in {"OVERLAY", "SKIP"}
        implied_required = suggested_u.startswith("STR8_") or (suggested_u == "BOX" and not is_promoter)

        if implied and any(not is_pick3(x) for x in implied):
            violations.append(
                Violation(d, str(idx), state_key, variant, alert_id, "IMPLIED_SET_MEMBER_NOT_PICK3", "")
            )

        if implied_required:
            if implied_err is not None:
                violations.append(
                    Violation(d, str(idx), state_key, variant, alert_id, "IMPLIED_SET_PARSE_ERROR", implied_err)
                )
            if not implied:
                violations.append(Violation(d, str(idx), state_key, variant, alert_id, "MISSING_IMPLIED_SET", ""))

        if suggested_u == "BOX" and not is_promoter:
            canon_box = canon_box_label(canonical)
            if not canon_box or canonical in {"", "-"}:
                violations.append(Violation(d, str(idx), state_key, variant, alert_id, "BOX_CANONICAL_MISSING", canonical))
            elif canonical != canon_box:
                violations.append(
                    Violation(d, str(idx), state_key, variant, alert_id, "BOX_CANONICAL_NOT_SORTED", canonical)
                )
            if implied:
                if any(canon_box_label(x) != canon_box for x in implied):
                    violations.append(
                        Violation(d, str(idx), state_key, variant, alert_id, "BOX_FAMILY_MISMATCH", canon_box)
                    )
                expected = perm_count_in_box(canon_box)
                if expected is not None and len(implied) != expected:
                    violations.append(
                        Violation(
                            d,
                            str(idx),
                            state_key,
                            variant,
                            alert_id,
                            "BOX_IMPLIED_SET_SIZE_MISMATCH",
                            f"{len(implied)} != {expected}",
                        )
                    )

        if alert_id == "A08":
            base_candidates = evidence.get("base_candidates")
            base_present = evidence.get("base_candidate_present")
            ok = isinstance(base_candidates, list) and base_present in {0, 1, True, False}
            if ok:
                ok = (1 if base_candidates else 0) == (1 if base_present else 0)
            if not ok:
                violations.append(
                    Violation(
                        d,
                        str(idx),
                        state_key,
                        variant,
                        alert_id,
                        "A08_BASE_POINTER_MISSING",
                        "",
                    )
                )

        if alert_id == "A11":
            ok = ("star_level" in evidence) and ("a11_star_score" in evidence)
            if not ok:
                violations.append(Violation(d, str(idx), state_key, variant, alert_id, "A11_STAR_FIELDS_MISSING", ""))

        # Canonical required for most (board-level check).
        if alert_id not in CANONICAL_OPTIONAL_ALERT_IDS and not is_promoter:
            if suggested_u == "BOX" and not is_pick3(canonical):
                violations.append(
                    Violation(d, str(idx), state_key, variant, alert_id, "CANONICAL_NOT_PICK3", canonical)
                )
            if suggested_u.startswith("STR8_") and not is_pick3(canonical) and canonical not in {"", "-"}:
                violations.append(
                    Violation(d, str(idx), state_key, variant, alert_id, "CANONICAL_NOT_PICK3", canonical)
                )

    # --- Eval/board alignment checks ---
    if not eval_path.exists():
        if require_eval:
            violations.append(Violation(d, "-", "-", "-", "-", "MISSING_EVAL", str(eval_path)))
        return (violations, counters)

    eval_rows = list(load_csv_rows(eval_path))
    counters["eval_rows"] += len(eval_rows)
    if len(eval_rows) != len(board_rows):
        violations.append(Violation(d, "-", "-", "-", "-", "EVAL_ROWCOUNT_MISMATCH", f"{len(eval_rows)} != {len(board_rows)}"))

    for er in eval_rows:
        row_num = (er.get("row_num") or "").strip()
        br = board_at_row_num(row_num)
        if br is None:
            violations.append(Violation(d, row_num or "-", "-", "-", "-", "ROW_NUM_OUT_OF_RANGE", ""))
            continue

        state_key = (er.get("state_key") or "").strip()
        variant = (er.get("variant") or "").strip()
        alert_id = (er.get("alert_id") or "").strip().upper()
        suggested_u = (er.get("suggested") or "").strip().upper()

        if (br.get("StateKey") or "").strip() != state_key or (br.get("Variant") or "").strip() != variant or (br.get("AlertId") or "").strip().upper() != alert_id:
            violations.append(Violation(d, row_num, state_key, variant, alert_id, "BOARD_EVAL_KEY_MISMATCH", ""))

        expected_rt = _expected_eval_row_type(suggested_u=suggested_u, alert_id=alert_id)
        rt = (er.get("row_type") or "").strip().upper()
        if rt != expected_rt:
            violations.append(Violation(d, row_num, state_key, variant, alert_id, "ROW_TYPE_MISMATCH", f"{rt} != {expected_rt}"))

        # Promoters should not be graded.
        if rt == "PROMOTER":
            strict_hit = (er.get("strict_hit") or "").strip().upper()
            hit_decay = (er.get("hit_within_decay") or "").strip().upper()
            hit_any = (er.get("hit_any_within_decay") or "").strip().upper()
            if strict_hit not in {"NA", ""} or hit_decay not in {"NA", ""} or hit_any not in {"NA", ""}:
                violations.append(Violation(d, row_num, state_key, variant, alert_id, "PROMOTER_MISGRADED", ""))

        # implied_set_size must match board implied set (when applicable).
        br_suggested_u = (br.get("Suggested") or "").strip().upper()
        br_alert = (br.get("AlertId") or "").strip().upper()
        is_promoter = br_alert in PROMOTER_ALERT_IDS or br_suggested_u in {"OVERLAY", "SKIP"}
        implied_required = br_suggested_u.startswith("STR8_") or (br_suggested_u == "BOX" and not is_promoter)
        if implied_required:
            implied, implied_err = parse_implied_set(br.get("ImpliedSet") or "")
            if implied_err is None and implied:
                implied_size = safe_int(er.get("implied_set_size") or "")
                if implied_size is not None and implied_size != len(implied):
                    violations.append(
                        Violation(d, row_num, state_key, variant, alert_id, "IMPLIED_SET_SIZE_MISMATCH", f"{implied_size} != {len(implied)}")
                    )
                exp = expected_implied_size(br_suggested_u, br.get("Canonical") or "")
                if exp is not None and len(implied) != exp:
                    violations.append(
                        Violation(d, row_num, state_key, variant, alert_id, "EXPECTED_SET_SIZE_MISMATCH", f"{len(implied)} != {exp}")
                    )

        # Canonical alignment (eval canonical_raw should mirror board canonical).
        canon_raw = (er.get("canonical_raw") or "").strip()
        br_canon = (br.get("Canonical") or "").strip()
        if canon_raw != br_canon:
            violations.append(Violation(d, row_num, state_key, variant, alert_id, "CANONICAL_RAW_MISMATCH", f"{canon_raw} != {br_canon}"))

        # A11 star columns must exist and be non-zero-ish in eval.
        if alert_id == "A11":
            lvl = safe_int(er.get("a11_star_level") or "")
            if lvl is None or lvl <= 0:
                violations.append(Violation(d, row_num, state_key, variant, alert_id, "A11_STAR_LEVEL_INVALID", str(er.get("a11_star_level") or "")))

    return (violations, counters)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Profit Alerts contract across one or more sharepack days.")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="Single results date D (YYYY-MM-DD)")
    g.add_argument("--start", help="Window start date (YYYY-MM-DD)")
    parser.add_argument("--end", help="Window end date (YYYY-MM-DD) (required with --start)")
    parser.add_argument("--sharepacks-dir", default=str(ROOT / "sharepacks"), help="Sharepacks root directory")
    parser.add_argument(
        "--allow-missing-eval",
        action="store_true",
        help="Do not fail if profit_alerts_eval.csv is missing (board-only validation).",
    )
    parser.add_argument("--max-examples", type=int, default=3, help="Examples to print per violation code")
    args = parser.parse_args()

    if args.start and not args.end:
        raise SystemExit("--end is required with --start")

    dates = [args.date] if args.date else daterange(args.start, args.end)
    sharepacks_root = Path(args.sharepacks_dir)
    require_eval = not args.allow_missing_eval

    all_violations: List[Violation] = []
    counters: Counter = Counter()
    for d in dates:
        v, c = validate_day(d, sharepacks_root=sharepacks_root, require_eval=require_eval)
        all_violations.extend(v)
        counters.update(c)

    by_code: Dict[str, List[Violation]] = defaultdict(list)
    for v in all_violations:
        by_code[v.code].append(v)

    if not all_violations:
        print(f"OK: Profit Alerts contract holds for {len(dates)} day(s).")
        print(f"- board rows: {counters.get('board_rows', 0)}")
        if not args.allow_missing_eval:
            print(f"- eval rows: {counters.get('eval_rows', 0)}")
        return

    print(f"FAIL: {len(all_violations)} violation(s) across {len(dates)} day(s).")
    for code, items in sorted(by_code.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"\n[{code}] x{len(items)}")
        for ex in items[: max(1, args.max_examples)]:
            where = f"{ex.results_date} row={ex.row_num} {ex.state_key} {ex.variant} {ex.alert_id}"
            detail = f" — {ex.detail}" if ex.detail else ""
            print(f"  - {where}{detail}")

    sys.exit(1)


if __name__ == "__main__":
    main()
