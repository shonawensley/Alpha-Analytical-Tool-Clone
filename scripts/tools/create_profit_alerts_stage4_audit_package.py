#!/usr/bin/env python3
"""
Create a bounded Stage-4 audit package for Profit Alerts (A01–A12) revamp validation.

This package is designed to:
- eliminate "manual hunting" by pre-extracting each case's board/eval/evidence facts,
- add contract guardrails (Charter + Grading Matrix SSOT),
- embed machine-readable environment snapshots (JSON tables row-ends at the Stable locator column),
- and produce a ChatGPT Pro prompt + artifacts that are portable (GitHub-visible) and deterministic.

Inputs:
- One or more Profit Alerts evidence packs, each containing:
  - CASES.csv
  - sharepacks/<D>/... mirrors (control_center boards/evals, winners HTML/JSON, json tables, stable excerpts)

Outputs:
- docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_stage4_audit__<STAMP>__<LABEL>/
  - AUDIT_SHEET.csv
  - SUMMARY.md
  - CHATGPT_PRO_PROMPT.md
  - MANIFEST.md
  - case_packets/*.md

Hard invariants (project scope):
- Profit Alerts remain quarantined (no reintegration into tool_only selection).
- No analyzer edits (Stable/DR/Hot Zones/VTRAC are treated as frozen inputs).
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]


PROMOTER_ALERT_IDS = {"A03", "A08"}
SET_BASED_SUGGESTED_PREFIXES = ("STR8_",)


def clean_label(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    out = []
    for ch in raw.replace(" ", "_"):
        if ch.isalnum() or ch in {"_", "-"}:
            out.append(ch)
    cleaned = "".join(out).strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --label: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def relpath(path: Path) -> str:
    """
    Prefer repo-relative paths for portability (zips / Deep Research),
    but fall back to absolute if the path is outside the repo root.
    """
    try:
        return path.relative_to(ROOT).as_posix()
    except Exception:
        return path.as_posix()


def safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def safe_float(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    v = str(value).strip()
    if not v or v == "-":
        return None
    try:
        return float(v)
    except Exception:
        return None


def load_csv_dicts(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [{k: (v or "") for k, v in row.items()} for row in reader]


def load_board_row_by_row_num(board_csv: Path, row_num: str) -> Optional[Dict[str, str]]:
    """
    Board CSVs do not carry an explicit row_num column; they are indexed by CSV row number (1-based, excluding header),
    matching profit_alerts_eval.csv's row_num.
    """
    idx = safe_int(row_num)
    if idx is None or idx <= 0:
        return None
    if not board_csv.exists():
        return None
    with board_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            if i == idx:
                return {k: (v or "") for k, v in row.items()}
    return None


def load_eval_row_by_row_num(eval_csv: Path, row_num: str) -> Optional[Dict[str, str]]:
    if not eval_csv.exists():
        return None
    want = (row_num or "").strip()
    if not want:
        return None
    with eval_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row.get("row_num") or "").strip() == want:
                return {k: (v or "") for k, v in row.items()}
    return None


def parse_json_obj(raw: str) -> Dict[str, object]:
    s = (raw or "").strip()
    if not s or s == "-":
        return {}
    try:
        obj = json.loads(s)
        return obj if isinstance(obj, dict) else {}
    except Exception:
        return {}


def parse_json_list(raw: str) -> Tuple[List[str], Optional[str]]:
    s = (raw or "").strip()
    if not s or s == "-":
        return ([], None)
    try:
        obj = json.loads(s)
        if isinstance(obj, list):
            out: List[str] = []
            for item in obj:
                if item is None:
                    continue
                out.append(str(item).strip())
            return (out, None)
        return ([], "not_a_list")
    except Exception as e:
        return ([], f"json_error:{e.__class__.__name__}")


def last3_digits(value: str) -> str:
    digits = "".join(re.findall(r"\d", value or ""))
    return digits[-3:] if len(digits) >= 3 else ""


def digits_only(value: str) -> str:
    return "".join(re.findall(r"\d", value or ""))


@dataclass(frozen=True)
class JsonEnvSnapshot:
    ok: bool
    error: str
    section: str
    set_name: str
    draw_name: str
    col: int
    arr_len: int
    arr_idx: int
    r2: str
    r4: str
    r6: str
    r8: str
    r2_last3: str
    r4_last3: str
    r6_last3: str
    r8_last3: str


def extract_json_env_snapshot(
    *,
    json_tables: Path,
    section: str,
    set_name: str,
    draw_name: str,
    col: int,
) -> JsonEnvSnapshot:
    if not json_tables.exists():
        return JsonEnvSnapshot(
            ok=False,
            error=f"missing_json_tables:{json_tables}",
            section=section,
            set_name=set_name,
            draw_name=draw_name,
            col=col,
            arr_len=0,
            arr_idx=-1,
            r2="",
            r4="",
            r6="",
            r8="",
            r2_last3="",
            r4_last3="",
            r6_last3="",
            r8_last3="",
        )
    try:
        obj = json.loads(json_tables.read_text(encoding="utf-8", errors="ignore"))
    except Exception as e:
        return JsonEnvSnapshot(
            ok=False,
            error=f"json_parse_error:{e.__class__.__name__}",
            section=section,
            set_name=set_name,
            draw_name=draw_name,
            col=col,
            arr_len=0,
            arr_idx=-1,
            r2="",
            r4="",
            r6="",
            r8="",
            r2_last3="",
            r4_last3="",
            r6_last3="",
            r8_last3="",
        )

    try:
        sect = obj["sections"][section]["sets"][set_name][draw_name]
        pv = sect["pattern_variations"]
        r2_arr = pv["R2"]
        r4_arr = pv["R4"]
        r6_arr = pv["R6"]
        r8_arr = pv["R8"]
        if not (isinstance(r2_arr, list) and isinstance(r4_arr, list) and isinstance(r6_arr, list) and isinstance(r8_arr, list)):
            raise KeyError("pattern_variations_not_lists")
        arr_len = len(r2_arr)
        # Column numbering is 1-based and in the "rightmost = Column 1" mental model.
        # JSON mirror stores the column progression left->right, so col=1 corresponds to the last element.
        arr_idx = arr_len - col
        if arr_idx < 0 or arr_idx >= arr_len:
            raise IndexError(f"col_out_of_range:{col} len={arr_len}")
        r2 = str(r2_arr[arr_idx])
        r4 = str(r4_arr[arr_idx])
        r6 = str(r6_arr[arr_idx])
        r8 = str(r8_arr[arr_idx])
        return JsonEnvSnapshot(
            ok=True,
            error="",
            section=section,
            set_name=set_name,
            draw_name=draw_name,
            col=col,
            arr_len=arr_len,
            arr_idx=arr_idx,
            r2=r2,
            r4=r4,
            r6=r6,
            r8=r8,
            r2_last3=last3_digits(r2),
            r4_last3=last3_digits(r4),
            r6_last3=last3_digits(r6),
            r8_last3=last3_digits(r8),
        )
    except Exception as e:
        return JsonEnvSnapshot(
            ok=False,
            error=f"json_path_error:{e}",
            section=section,
            set_name=set_name,
            draw_name=draw_name,
            col=col,
            arr_len=0,
            arr_idx=-1,
            r2="",
            r4="",
            r6="",
            r8="",
            r2_last3="",
            r4_last3="",
            r6_last3="",
            r8_last3="",
        )


def stable_excerpt_path(pack_root: Path, *, results_date: str, state_key: str) -> Path:
    return (
        pack_root
        / "sharepacks"
        / results_date
        / state_key
        / "stable"
        / state_key
        / f"{state_key}_stable_patterns_scores__profit_alerts_excerpt.csv"
    )


def find_stable_excerpt_row(
    *,
    excerpt_csv: Path,
    section: str,
    set_name: str,
    draw_name: str,
    col: str,
    canonical: str,
) -> Optional[Dict[str, str]]:
    if not excerpt_csv.exists():
        return None
    want = (section, set_name, draw_name, str(col).strip(), canonical.strip())
    with excerpt_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (
                (row.get("section") or "").strip(),
                (row.get("Set") or "").strip(),
                (row.get("Draw") or "").strip(),
                (row.get("Column") or "").strip(),
                (row.get("Canonical") or "").strip(),
            )
            if key == want:
                return {k: (v or "") for k, v in row.items()}
    return None


def pick_winner_html(winners_dir: Path, canonical: str) -> str:
    """
    If present, pick an HTML file that appears to match the canonical (e.g., ..._winner_089_...html).
    Returns a pack-relative path string if found, else "".
    """
    if not winners_dir.exists() or not canonical or canonical == "-":
        return ""
    want = f"_winner_{canonical}_"
    for p in sorted(winners_dir.glob("*.html")):
        if want in p.name:
            return relpath(p)
    return ""


def yn(value: bool) -> str:
    return "Y" if value else "N"


def na_if_empty(value: str) -> str:
    v = (value or "").strip()
    return v if v else "NA"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def format_md_table(rows: List[Tuple[str, str]]) -> str:
    out = ["| Field | Value |", "|---|---|"]
    for k, v in rows:
        out.append(f"| {k} | {v} |")
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Stage-4 audit package from one or more Profit Alerts evidence packs.")
    parser.add_argument(
        "--evidence-pack",
        action="append",
        required=True,
        help="Evidence pack root, as KEY=PATH (PATH is a folder containing CASES.csv + sharepacks mirror). Repeatable.",
    )
    parser.add_argument("--stamp", default=dt.date.today().isoformat(), help="Stamp used in output folder name")
    parser.add_argument("--label", default="stage4_auto_v1", help="Optional label appended to output folder name")
    parser.add_argument(
        "--packages-dir",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "PACKAGES"),
        help="Packages output directory",
    )
    args = parser.parse_args()

    stamp = (args.stamp or "").strip()
    if not stamp:
        raise SystemExit("--stamp must be non-empty")
    label = clean_label(args.label)
    label_suffix = f"__{label}" if label else ""

    packages_root = Path(args.packages_dir)
    packages_root.mkdir(parents=True, exist_ok=True)

    out_dir = packages_root / f"profit_alerts_stage4_audit__{stamp}{label_suffix}"
    ensure_dir(out_dir)
    packets_dir = out_dir / "case_packets"
    ensure_dir(packets_dir)

    packs: List[Tuple[str, Path]] = []
    for raw in args.evidence_pack:
        if "=" not in raw:
            raise SystemExit(f"--evidence-pack must be KEY=PATH, got: {raw!r}")
        key, path_raw = raw.split("=", 1)
        key = (key or "").strip()
        if not key:
            raise SystemExit(f"Invalid pack key in --evidence-pack: {raw!r}")
        pack_root = Path(path_raw).resolve()
        if not pack_root.exists():
            raise SystemExit(f"Evidence pack not found: {pack_root}")
        if pack_root.is_file():
            pack_root = pack_root.parent
        cases_csv = pack_root / "CASES.csv"
        if not cases_csv.exists():
            raise SystemExit(f"Evidence pack missing CASES.csv: {pack_root}")
        packs.append((key, pack_root))

    # Build combined audit sheet rows.
    audit_rows: List[Dict[str, str]] = []
    fail_reason_counts: Counter[str] = Counter()
    verdict_counts: Counter[str] = Counter()

    case_key_to_packet: Dict[str, str] = {}

    for pack_key, pack_root in packs:
        cases_csv = pack_root / "CASES.csv"
        cases = load_csv_dicts(cases_csv)
        if not cases:
            raise SystemExit(f"No cases in {cases_csv}")

        for case in cases:
            case_num = (case.get("case_num") or "").strip()
            case_key = f"{pack_key} Case {case_num}".strip()
            results_date = (case.get("results_date") or "").strip()
            state_key = (case.get("state_key") or "").strip()
            variant = (case.get("variant") or "").strip()
            alert_id = (case.get("alert_id") or "").strip().upper()
            row_num = (case.get("row_num") or "").strip()
            status = (case.get("status") or "").strip().upper()
            suggested = (case.get("suggested") or "").strip()
            canonical = (case.get("canonical") or "").strip()
            badges = (case.get("badges") or "").strip()

            # Resolve file pointers (relative to pack root).
            board_csv_rel = (case.get("board_csv") or "").strip()
            eval_csv_rel = (case.get("eval_csv") or "").strip()
            winners_dir_rel = (case.get("winners_dir") or "").strip()
            winners_digest_rel = (case.get("winners_digest") or "").strip()
            json_tables_rel = (case.get("json_tables") or "").strip()

            board_csv = pack_root / board_csv_rel if board_csv_rel else Path()
            eval_csv = pack_root / eval_csv_rel if eval_csv_rel else Path()
            winners_dir = pack_root / winners_dir_rel if winners_dir_rel else Path()
            winners_digest = pack_root / winners_digest_rel if winners_digest_rel else Path()
            json_tables = pack_root / json_tables_rel if json_tables_rel else Path()

            board_row = load_board_row_by_row_num(board_csv, row_num) if board_csv_rel else None
            eval_row = load_eval_row_by_row_num(eval_csv, row_num) if eval_csv_rel else None

            evidence = parse_json_obj(board_row.get("Evidence", "") if board_row else "")
            implied_set_raw = (board_row.get("ImpliedSet", "") if board_row else "") or ""
            implied_set, implied_set_err = parse_json_list(implied_set_raw)

            expected_row_type = "PROMOTER" if (alert_id in PROMOTER_ALERT_IDS or status == "PROMOTER") else "CANDIDATE"
            eval_row_type = (eval_row.get("row_type") or "").strip().upper() if eval_row else ""

            # Stable locator fields (from CASES.csv; evidence JSON should match).
            stable_section = (case.get("stable_section") or "").strip()
            stable_set = (case.get("stable_set") or "").strip()
            stable_draw = (case.get("stable_draw") or "").strip()
            stable_column = (case.get("stable_column") or "").strip()
            stable_family_id = (case.get("stable_family_id") or "").strip()
            stable_why = (case.get("stable_why") or "").strip()

            stub_section = (case.get("stub_section") or "").strip()
            stub_set = (case.get("stub_set") or "").strip()
            stub_draw = (case.get("stub_draw") or "").strip()
            stub_column = (case.get("stub_column") or "").strip()

            stable_loc_present = bool(stable_section and stable_set and stable_draw and stable_column and canonical and canonical != "-")

            excerpt_csv = stable_excerpt_path(pack_root, results_date=results_date, state_key=state_key) if stable_loc_present else Path()
            stable_row = (
                find_stable_excerpt_row(
                    excerpt_csv=excerpt_csv,
                    section=stable_section,
                    set_name=stable_set,
                    draw_name=stable_draw,
                    col=stable_column,
                    canonical=canonical,
                )
                if stable_loc_present
                else None
            )

            # JSON environment snapshot at stable locator (preferred), else stub locator.
            env_section = stable_section or stub_section
            env_set = stable_set or stub_set
            env_draw = stable_draw or stub_draw
            env_col = safe_int(stable_column or stub_column or "")
            env_snapshot: Optional[JsonEnvSnapshot] = None
            if env_section and env_set and env_draw and env_col and json_tables_rel:
                env_snapshot = extract_json_env_snapshot(
                    json_tables=json_tables,
                    section=env_section,
                    set_name=env_set,
                    draw_name=env_draw,
                    col=env_col,
                )

            # --- Contract checks + auto verdict ---
            fail_reasons: List[str] = []
            ambig_reasons: List[str] = []

            def fail(code: str) -> None:
                if code not in fail_reasons:
                    fail_reasons.append(code)

            def ambig(code: str) -> None:
                if code not in ambig_reasons and code not in fail_reasons:
                    ambig_reasons.append(code)

            if board_row is None:
                fail("BOARD_ROW_MISSING")
            if eval_row is None:
                fail("EVAL_ROW_MISSING")

            if expected_row_type and eval_row is not None:
                if eval_row_type != expected_row_type:
                    fail("ROW_TYPE_MISMATCH")

            # Promoter locks: do not grade as candidate.
            if expected_row_type == "PROMOTER" and eval_row is not None:
                strict_hit = (eval_row.get("strict_hit") or "").strip().upper()
                hit_decay = (eval_row.get("hit_within_decay") or "").strip().upper()
                if strict_hit not in {"NA", ""} or hit_decay not in {"NA", ""}:
                    fail("PROMOTER_MISGRADED")

            suggested_u = suggested.strip().upper()
            implied_set_required = suggested_u.startswith(SET_BASED_SUGGESTED_PREFIXES)
            if implied_set_required:
                if implied_set_err is not None:
                    fail("IMPLIED_SET_PARSE_ERROR")
                if not implied_set:
                    fail("MISSING_IMPLIED_SET")
                else:
                    implied_set_size = safe_int(case.get("implied_set_size") or "")
                    if implied_set_size is not None and implied_set_size != len(implied_set):
                        fail("IMPLIED_SET_SIZE_MISMATCH")

            # Stable locator must be resolvable when present.
            if stable_loc_present:
                if not excerpt_csv.exists():
                    fail("STABLE_EXCERPT_MISSING")
                if stable_row is None:
                    fail("STABLE_LOCATOR_ROW_MISSING")
                else:
                    if stable_family_id and (stable_row.get("family_id") or "").strip() != stable_family_id:
                        fail("STABLE_ROW_FAMILY_ID_MISMATCH")
                    if stable_why and (stable_row.get("why") or "").strip() != stable_why:
                        fail("STABLE_ROW_WHY_MISMATCH")

            # JSON snapshot should exist for stable-locator cases (audit mirror).
            if stable_loc_present:
                if not json_tables.exists():
                    fail("JSON_TABLES_MISSING")
                if env_snapshot is None:
                    fail("JSON_SNAPSHOT_MISSING")
                elif not env_snapshot.ok:
                    fail(f"JSON_SNAPSHOT_ERROR:{env_snapshot.error}")

            # A12 clamp: verify dominance math agrees with environment row-ends.
            a12_dom_ok = "NA"
            evidence_modal_value = ""
            evidence_dom = ""
            evidence_modal_rows = ""
            computed_modal_rows = ""
            computed_dom = ""
            if alert_id == "A12":
                evidence_modal_value = str(evidence.get("orders_modal_value") or "").strip()
                evidence_dom = str(evidence.get("order_dominance") or "").strip()
                evidence_modal_rows = str(evidence.get("orders_modal_rows") or "").strip()
                if env_snapshot is None or not env_snapshot.ok:
                    fail("A12_ENV_SNAPSHOT_MISSING")
                if not evidence_modal_value:
                    fail("A12_MODAL_VALUE_MISSING")
                if env_snapshot is not None and env_snapshot.ok and evidence_modal_value:
                    # Important nuance:
                    # - JSON row-end tokens can be >3 digits at the Stable locator column (e.g. "5541**").
                    # - Stable's `orders_modal_value` is a 3-digit literal (e.g. "554") and may appear as a contiguous
                    #   substring within a longer token (e.g. "5541"), not necessarily as the token's *last* 3 digits.
                    # So for A12, count "modal rows" by containment in the digits stream, not last3 equality.
                    modal_rows = sum(
                        1
                        for tok in [env_snapshot.r2, env_snapshot.r4, env_snapshot.r6, env_snapshot.r8]
                        if evidence_modal_value in digits_only(tok)
                    )
                    dom = modal_rows / 4.0
                    computed_modal_rows = str(modal_rows)
                    computed_dom = f"{dom:.2f}"
                    ev_dom = safe_float(evidence_dom)
                    ev_rows = safe_int(evidence_modal_rows)
                    if ev_rows is not None and ev_rows != modal_rows:
                        fail("A12_DOMINANCE_ROWS_MISMATCH")
                    if ev_dom is not None and abs(ev_dom - dom) > 0.001:
                        fail("A12_DOMINANCE_VALUE_MISMATCH")
                    a12_dom_ok = "Y" if not any(r.startswith("A12_DOMINANCE_") for r in fail_reasons) else "N"

            auto_verdict = "FAIL" if fail_reasons else ("AMBIG" if ambig_reasons else "PASS")
            verdict_counts[auto_verdict] += 1
            for code in fail_reasons:
                fail_reason_counts[code] += 1

            # Packet filename
            slug = re.sub(r"[^A-Za-z0-9_-]+", "_", f"{case_key}_{alert_id}_{state_key}_{variant}_{results_date}").strip("_")
            packet_rel = Path("case_packets") / f"{slug}.md"
            packet_path = out_dir / packet_rel

            winner_html = pick_winner_html(winners_dir, canonical)

            # Packet contents
            md: List[str] = []
            md.append(f"# Profit Alerts Stage-4 Audit Packet — {case_key}")
            md.append("")
            md.append("## Case metadata")
            md.append(
                format_md_table(
                    [
                        ("Evidence pack key", pack_key),
                        ("Case number", case_num),
                        ("AlertId", alert_id),
                        ("StateKey", state_key),
                        ("Variant", variant),
                        ("Results date D", results_date),
                        ("Status", status),
                        ("Suggested", suggested),
                        ("Canonical", canonical),
                        ("Badges", badges),
                        ("RowNum (eval/board)", row_num),
                        ("AutoVerdict", auto_verdict),
                        ("FailReasons", ";".join(fail_reasons) if fail_reasons else ""),
                    ]
                )
            )
            md.append("")

            md.append("## Files to open (portable)")
            md.append("- Board CSV: " + (relpath(board_csv) if board_csv_rel else ""))
            md.append("- Eval CSV: " + (relpath(eval_csv) if eval_csv_rel else ""))
            md.append("- Winners digest: " + (relpath(winners_digest) if winners_digest_rel else ""))
            md.append("- Winners dir: " + (relpath(winners_dir) if winners_dir_rel else ""))
            if winner_html:
                md.append(f"- Winner HTML (best guess): {winner_html}")
            md.append("- JSON tables: " + (relpath(json_tables) if json_tables_rel else ""))
            if stable_loc_present:
                md.append("- Stable excerpt: " + relpath(excerpt_csv))
            md.append("")

            md.append("## Board row (extracted)")
            if board_row is None:
                md.append("- Missing board row.")
            else:
                md.append(
                    format_md_table(
                        [
                            ("StateKey", board_row.get("StateKey", "")),
                            ("Variant", board_row.get("Variant", "")),
                            ("AlertId", board_row.get("AlertId", "")),
                            ("Strength", board_row.get("Strength", "")),
                            ("Suggested", board_row.get("Suggested", "")),
                            ("CapLines", board_row.get("CapLines", "")),
                            ("DecayDraws", board_row.get("DecayDraws", "")),
                            ("Badges", board_row.get("Badges", "")),
                            ("Canonical", board_row.get("Canonical", "")),
                            ("ImpliedSet", board_row.get("ImpliedSet", "")),
                            ("Winner Midday", board_row.get("Winner Midday", "")),
                            ("Winner Evening", board_row.get("Winner Evening", "")),
                        ]
                    )
                )
            md.append("")

            md.append("## Eval row (extracted)")
            if eval_row is None:
                md.append("- Missing eval row.")
            else:
                md.append(
                    format_md_table(
                        [
                            ("row_type", eval_row.get("row_type", "")),
                            ("strict_hit (D-only)", eval_row.get("strict_hit", "")),
                            ("hit_within_decay (primary)", eval_row.get("hit_within_decay", "")),
                            ("hit_any_within_decay (diagnostic)", eval_row.get("hit_any_within_decay", "")),
                            ("hit_within_7", eval_row.get("hit_within_7", "")),
                            ("hit_within_14", eval_row.get("hit_within_14", "")),
                            ("hit_type", eval_row.get("hit_type", "")),
                            ("hit_any_type", eval_row.get("hit_any_type", "")),
                            ("start_when", eval_row.get("start_when", "")),
                            ("expiry_when", eval_row.get("expiry_when", "")),
                            ("hit_when", eval_row.get("hit_when", "")),
                            ("time_to_hit_steps", eval_row.get("time_to_hit_steps", "")),
                        ]
                    )
                )
            md.append("")

            md.append("## Evidence JSON (pretty)")
            if not evidence:
                md.append("```json\n{}\n```")
            else:
                md.append("```json")
                md.append(json.dumps(evidence, sort_keys=True, indent=2))
                md.append("```")
            md.append("")

            md.append("## Stable locator + excerpt row (if applicable)")
            if not stable_loc_present:
                md.append("- No stable locator for this case (expected for some alerts, e.g., promoters / lane-only signals).")
            else:
                md.append(
                    format_md_table(
                        [
                            ("stable_section", stable_section),
                            ("stable_set", stable_set),
                            ("stable_draw", stable_draw),
                            ("stable_column", stable_column),
                            ("stable_family_id", stable_family_id),
                            ("stable_why", stable_why),
                        ]
                    )
                )
                md.append("")
                if stable_row is None:
                    md.append("- Stable excerpt row not found at locator.")
                else:
                    # Keep excerpt display short; full row exists in CSV.
                    md.append(
                        format_md_table(
                            [
                                ("type", stable_row.get("type", "")),
                                ("score", stable_row.get("score", "")),
                                ("rows", stable_row.get("rows", "")),
                                ("orders_modal_value", stable_row.get("orders_modal_value", "")),
                                ("orders_modal_rows", stable_row.get("orders_modal_rows", "")),
                                ("order dominance (computed later)", ""),
                                ("why", stable_row.get("why", "")),
                            ]
                        )
                    )
            md.append("")

            md.append("## JSON environment snapshot at locator (audit mirror)")
            if env_snapshot is None:
                md.append("- No JSON snapshot extracted (no locator available or json file missing).")
            elif not env_snapshot.ok:
                md.append(f"- JSON snapshot error: `{env_snapshot.error}`")
            else:
                md.append(
                    format_md_table(
                        [
                            ("json_section", env_snapshot.section),
                            ("json_set", env_snapshot.set_name),
                            ("json_draw", env_snapshot.draw_name),
                            ("json_col", str(env_snapshot.col)),
                            ("json_arr_len", str(env_snapshot.arr_len)),
                            ("json_arr_idx", str(env_snapshot.arr_idx)),
                            ("R2 @col", env_snapshot.r2),
                            ("R4 @col", env_snapshot.r4),
                            ("R6 @col", env_snapshot.r6),
                            ("R8 @col", env_snapshot.r8),
                            ("R2 last3", env_snapshot.r2_last3),
                            ("R4 last3", env_snapshot.r4_last3),
                            ("R6 last3", env_snapshot.r6_last3),
                            ("R8 last3", env_snapshot.r8_last3),
                        ]
                    )
                )
            md.append("")

            md.append("## Contract checks (auto)")
            checks: List[Tuple[str, str]] = []
            checks.append(("expected_row_type", expected_row_type))
            checks.append(("eval_row_type", eval_row_type or ""))
            checks.append(("row_type_ok", "Y" if (eval_row_type == expected_row_type) else ("N" if eval_row else "")))
            checks.append(("implied_set_required", yn(implied_set_required)))
            checks.append(("implied_set_parse_error", implied_set_err or ""))
            checks.append(("implied_set_size", str(len(implied_set)) if implied_set else "0"))
            checks.append(("stable_locator_present", yn(stable_loc_present)))
            checks.append(("stable_excerpt_row_found", "Y" if stable_row else ("N" if stable_loc_present else "NA")))
            checks.append(("json_snapshot_ok", "Y" if (env_snapshot and env_snapshot.ok) else ("N" if stable_loc_present else "NA")))
            if alert_id == "A12":
                checks.append(("A12 orders_modal_value", evidence_modal_value))
                checks.append(("A12 orders_modal_rows (evidence)", evidence_modal_rows))
                checks.append(("A12 order_dominance (evidence)", evidence_dom))
                checks.append(("A12 modal_rows (computed)", computed_modal_rows))
                checks.append(("A12 dominance (computed)", computed_dom))
                checks.append(("A12 dominance ok", a12_dom_ok))
            md.append(format_md_table(checks))
            md.append("")

            md.append("## Audit questions (yes/no)")
            if alert_id == "A12":
                md.append("1) Do JSON row-ends at the locator show the same modal order in 3 of 4 rows?")
                md.append("2) Do Stable excerpt + Evidence JSON agree on modal order + dominance fields?")
                md.append("3) Is `ImpliedSet` consistent with clamp_rule + modal order (no guessing by evaluator)?")
            elif expected_row_type == "PROMOTER":
                md.append("1) Is this row typed as PROMOTER and not graded like a candidate?")
                md.append("2) Does the Evidence JSON contain enough context to understand what it is promoting?")
            else:
                md.append("1) Does the Stable excerpt row exist at the locator and match Evidence fields?")
                md.append("2) Does the JSON environment at that locator ‘look consistent’ with the alert’s intended meaning?")
            md.append("")

            md.append("## Notes / overrides (human / Deep Research)")
            md.append("- HumanVerdict: (PASS/FAIL/AMBIG)  ")
            md.append("- HumanNotes:  ")
            md.append("- ProposedFix (if FAIL):  ")

            write_text(packet_path, "\n".join(md))
            case_key_to_packet[case_key] = packet_rel.as_posix()

            audit_rows.append(
                {
                    "pack_key": pack_key,
                    "case_num": case_num,
                    "case_key": case_key,
                    "alert_id": alert_id,
                    "state_key": state_key,
                    "variant": variant,
                    "results_date": results_date,
                    "row_num": row_num,
                    "status": status,
                    "suggested": suggested,
                    "canonical": canonical,
                    "strength": (case.get("strength") or "").strip(),
                    "decay_draws": (case.get("decay_draws") or "").strip(),
                    "badges": badges,
                    "expected_row_type": expected_row_type,
                    "eval_row_type": eval_row_type,
                    "row_type_ok": "Y" if (eval_row and eval_row_type == expected_row_type) else ("N" if eval_row else ""),
                    "implied_set_required": yn(implied_set_required),
                    "implied_set_parse_error": implied_set_err or "",
                    "implied_set_size": str(len(implied_set)) if implied_set else "0",
                    "stable_locator_present": yn(stable_loc_present),
                    "stable_excerpt_row_found": "Y" if stable_row else ("N" if stable_loc_present else "NA"),
                    "json_snapshot_ok": "Y" if (env_snapshot and env_snapshot.ok) else ("N" if stable_loc_present else "NA"),
                    "json_r2_end": env_snapshot.r2 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r4_end": env_snapshot.r4 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r6_end": env_snapshot.r6 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r8_end": env_snapshot.r8 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r2_last3": env_snapshot.r2_last3 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r4_last3": env_snapshot.r4_last3 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r6_last3": env_snapshot.r6_last3 if (env_snapshot and env_snapshot.ok) else "",
                    "json_r8_last3": env_snapshot.r8_last3 if (env_snapshot and env_snapshot.ok) else "",
                    "a12_orders_modal_value": evidence_modal_value if alert_id == "A12" else "",
                    "a12_orders_modal_rows_evidence": evidence_modal_rows if alert_id == "A12" else "",
                    "a12_order_dominance_evidence": evidence_dom if alert_id == "A12" else "",
                    "a12_modal_rows_computed": computed_modal_rows if alert_id == "A12" else "",
                    "a12_dominance_computed": computed_dom if alert_id == "A12" else "",
                    "a12_dom_ok": a12_dom_ok if alert_id == "A12" else "NA",
                    "auto_verdict": auto_verdict,
                    "fail_reasons": ";".join(fail_reasons),
                    "ambig_reasons": ";".join(ambig_reasons),
                    "packet_path": packet_rel.as_posix(),
                    "board_csv": relpath(board_csv) if board_csv_rel else "",
                    "eval_csv": relpath(eval_csv) if eval_csv_rel else "",
                    "json_tables": relpath(json_tables) if json_tables_rel else "",
                    "stable_excerpt": relpath(excerpt_csv) if stable_loc_present else "",
                    "winners_dir": relpath(winners_dir) if winners_dir_rel else "",
                    "winners_digest": relpath(winners_digest) if winners_digest_rel else "",
                    "winner_html_best_guess": winner_html,
                }
            )

    # Write AUDIT_SHEET.csv
    fieldnames = [
        "pack_key",
        "case_num",
        "case_key",
        "alert_id",
        "state_key",
        "variant",
        "results_date",
        "row_num",
        "status",
        "suggested",
        "canonical",
        "strength",
        "decay_draws",
        "badges",
        "expected_row_type",
        "eval_row_type",
        "row_type_ok",
        "implied_set_required",
        "implied_set_parse_error",
        "implied_set_size",
        "stable_locator_present",
        "stable_excerpt_row_found",
        "json_snapshot_ok",
        "json_r2_end",
        "json_r4_end",
        "json_r6_end",
        "json_r8_end",
        "json_r2_last3",
        "json_r4_last3",
        "json_r6_last3",
        "json_r8_last3",
        "a12_orders_modal_value",
        "a12_orders_modal_rows_evidence",
        "a12_order_dominance_evidence",
        "a12_modal_rows_computed",
        "a12_dominance_computed",
        "a12_dom_ok",
        "auto_verdict",
        "fail_reasons",
        "ambig_reasons",
        "packet_path",
        "board_csv",
        "eval_csv",
        "json_tables",
        "stable_excerpt",
        "winners_dir",
        "winners_digest",
        "winner_html_best_guess",
    ]
    audit_csv = out_dir / "AUDIT_SHEET.csv"
    with audit_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(audit_rows)

    # SUMMARY.md
    summary_lines: List[str] = []
    summary_lines.append("# Profit Alerts — Stage-4 Audit Summary")
    summary_lines.append("")
    summary_lines.append(f"Stamp: `{stamp}`")
    summary_lines.append("")
    summary_lines.append("## Counts")
    for k in ["PASS", "FAIL", "AMBIG"]:
        summary_lines.append(f"- {k}: {verdict_counts.get(k, 0)}")
    summary_lines.append("")
    summary_lines.append("## Failure reasons (top)")
    for code, n in fail_reason_counts.most_common(30):
        summary_lines.append(f"- {code}: {n}")
    summary_lines.append("")
    summary_lines.append("## Entry points")
    summary_lines.append(f"- Audit sheet: `{relpath(audit_csv)}`")
    summary_lines.append(f"- Case packets: `{relpath(packets_dir)}`")
    write_text(out_dir / "SUMMARY.md", "\n".join(summary_lines))

    # MANIFEST.md
    manifest: List[str] = []
    manifest.append("# Manifest — Profit Alerts Stage-4 Audit Package")
    manifest.append("")
    manifest.append("Entry points:")
    manifest.append(f"- `AUDIT_SHEET.csv`")
    manifest.append(f"- `SUMMARY.md`")
    manifest.append(f"- `CHATGPT_PRO_PROMPT.md`")
    manifest.append(f"- `case_packets/`")
    manifest.append(f"- `ssot/` (Charter + Grading Matrix + roster copy)")
    manifest.append("")
    manifest.append("Evidence packs used:")
    for k, p in packs:
        manifest.append(f"- `{k}`: `{relpath(p)}`")
    write_text(out_dir / "MANIFEST.md", "\n".join(manifest))

    # SSOT copies (Deep Research portability)
    ssot_dir = out_dir / "ssot"
    ensure_dir(ssot_dir)
    ssot_sources = [
        ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "final docs"
        / "AAT9_Profit_Alerts_Evaluation_Charter.md",
        ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "final docs"
        / "AAT9_Profit_Alerts_Grading_Matrix.md",
        ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "RUNS"
        / "V0_3__PROFIT_ALERTS__REVAMP_STAGE4_AUDIT_ROSTER__2026-02-22.md",
    ]
    for src in ssot_sources:
        if src.exists():
            shutil.copy2(src, ssot_dir / src.name)

    # CHATGPT_PRO_PROMPT.md (generated, SSOT-anchored)
    prompt_lines: List[str] = []
    prompt_lines.append("# ChatGPT Pro — Deep Research Prompt (Profit Alerts Stage-4 Audit)")
    prompt_lines.append("")
    prompt_lines.append("## Mission")
    prompt_lines.append("Verify Profit Alerts revamp correctness by reviewing a bounded, evidence-linked Stage-4 audit package.")
    prompt_lines.append("Focus on **mapping/intent correctness**, not reintegration or tuning.")
    prompt_lines.append("")
    prompt_lines.append("## Hard constraints (do not violate)")
    prompt_lines.append("- Do not recommend analyzer edits (Stable/DR/Hot Zones/VTRAC are out of scope).")
    prompt_lines.append("- Profit Alerts are quarantined; do not recommend enabling them in `tool_only` defaults.")
    prompt_lines.append("- Treat Combined as a **lens**, not an outcome stream.")
    prompt_lines.append("- Promoters (A03/A08) are not graded as candidate callers.")
    prompt_lines.append("")
    prompt_lines.append("## SSOT rules (must follow)")
    prompt_lines.append("- Charter (copy): `ssot/AAT9_Profit_Alerts_Evaluation_Charter.md`")
    prompt_lines.append("- Grading Matrix (copy): `ssot/AAT9_Profit_Alerts_Grading_Matrix.md`")
    prompt_lines.append("")
    prompt_lines.append("## What you are given")
    prompt_lines.append("- Audit package manifest: `MANIFEST.md`")
    prompt_lines.append("- Audit sheet (prefilled): `AUDIT_SHEET.csv`")
    prompt_lines.append("- Per-case packets (prefilled): `case_packets/`")
    prompt_lines.append("- SSOT copies: `ssot/`")
    prompt_lines.append("")
    prompt_lines.append("## How to review (repeatable)")
    prompt_lines.append("For each case packet:")
    prompt_lines.append("1) Read the extracted board row + eval row.")
    prompt_lines.append("2) Check the contract locks:")
    prompt_lines.append("   - row_type matches expected (PROMOTER vs CANDIDATE)")
    prompt_lines.append("   - STR8_* rows have explicit ImpliedSet (no guessing)")
    prompt_lines.append("3) If the case has a Stable locator:")
    prompt_lines.append("   - confirm Stable excerpt row exists at that locator")
    prompt_lines.append("   - confirm JSON environment snapshot row-ends at the same locator match the intended pattern story")
    prompt_lines.append("4) Confirm the packet’s AutoVerdict (PASS/FAIL/AMBIG) is correct, or explain why it should change.")
    prompt_lines.append("")
    prompt_lines.append("## Required deliverable back to us")
    prompt_lines.append("- A short report with:")
    prompt_lines.append("  - PASS/FAIL/AMBIG counts you agree with (or corrected)")
    prompt_lines.append("  - Any cases where AutoVerdict is wrong and why")
    prompt_lines.append("  - A failure taxonomy: mapping bug vs semantics misunderstanding vs missing evidence vs expectation mismatch")
    prompt_lines.append("  - Optional: 1–3 minimal evidence-schema improvements (only if audits are ambiguous), e.g. A08 base-candidate context pointer.")
    prompt_lines.append("")
    prompt_lines.append("## Tier-1 recommendation (review these first)")
    prompt_lines.append("Start with HIT + PROMOTER cases (highest ROI). The audit roster is:")
    prompt_lines.append("- `ssot/V0_3__PROFIT_ALERTS__REVAMP_STAGE4_AUDIT_ROSTER__2026-02-22.md`")
    prompt_lines.append("")
    prompt_lines.append("Tier-1 quick links (open these packets first):")
    for k in [
        "W1 Case 2",
        "W1 Case 5",
        "W2 Case 3",
        "W2 Case 10",
        "W1 Case 10",
        "W1 Case 11",
    ]:
        packet = case_key_to_packet.get(k)
        if packet:
            prompt_lines.append(f"- `{packet}`")
    prompt_lines.append("")
    write_text(out_dir / "CHATGPT_PRO_PROMPT.md", "\n".join(prompt_lines))


if __name__ == "__main__":
    main()
