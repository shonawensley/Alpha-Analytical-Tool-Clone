#!/usr/bin/env python3
"""Bounded Aux / Control Center parity audit for frozen gold-day sharepacks.

This verifies that a small audited set of sharepack state-days can be regenerated
from the recorded workbook snapshot and still match the frozen sharepack Aux and
Control Center outputs.

Scope:
- compare regenerated Aux draw snapshots vs sharepack Aux draw snapshots
- compare regenerated Aux summary sections vs sharepack summary sections
- compare regenerated Control Center rows vs sharepack Control Center CSV rows

The audit is intentionally bounded and diagnostic. It does not rewrite sharepacks.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from modules.aux_loaders import load_state_draws
from scripts.tools.aux_sharepack_summary import build_summary
from scripts.tools.export_control_center_sharepack import (
    SharepackState,
    _build_blackapple_df,
    _build_due_doubles_df,
    _build_profit_alerts_df,
    _build_vtrac_repeat_watch_df,
    _discover_states,
    _norm_state,
    _parse_results,
)

RUNS_DIR = ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
DEFAULT_SAMPLES = (
    "2025-12-30:NorthCarolina4",
    "2025-12-31:NewJersey4",
    "2026-01-09:Pennsylvania4",
)
VARIANTS: Tuple[Tuple[str, str], ...] = (
    ("Combined", "combined"),
    ("Midday", "midday"),
    ("Evening", "evening"),
)
SUMMARY_SECTION_KEYS: Tuple[str, ...] = (
    "repeat_watch",
    "positional",
    "doubles",
    "pairs",
    "vtrac",
    "sums",
    "blackapple",
)
CONTROL_CENTER_ARTIFACTS: Tuple[Tuple[str, str], ...] = (
    ("blackapple_alerts", "blackapple_alerts.csv"),
    ("due_doubles", "due_doubles.csv"),
    ("vtrac_repeat_watch", "vtrac_repeat_watch.csv"),
    ("profit_alerts", "profit_alerts.csv"),
)


@dataclass(frozen=True)
class AuditSample:
    date: str
    state_key: str


def _parse_sample(text: str) -> AuditSample:
    raw = (text or "").strip()
    if ":" not in raw:
        raise ValueError(f"Sample must be DATE:STATEKEY, got: {raw!r}")
    date, state_key = raw.split(":", 1)
    date = date.strip()
    state_key = state_key.strip()
    if not date or not state_key:
        raise ValueError(f"Sample must be DATE:STATEKEY, got: {raw!r}")
    return AuditSample(date=date, state_key=state_key)


def _safe_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except Exception:
        return str(path)


def _infer_limit(summary: Dict[str, Any]) -> int:
    max_len = 0
    doubles = ((summary.get("doubles") or {}).get("top_by_variant") or {}).values()
    max_len = max([max_len, *[len(rows or []) for rows in doubles]])

    pairs = ((summary.get("pairs") or {}).get("top_by_variant") or {}).values()
    for payload in pairs:
        payload = payload or {}
        max_len = max(max_len, len(payload.get("repeating") or []), len(payload.get("non_repeating") or []))

    vtrac = summary.get("vtrac") or {}
    for bucket in ("overlay_top", "heatboard_top"):
        for rows in ((vtrac.get(bucket) or {}).values()):
            max_len = max(max_len, len(rows or []))

    sums = ((summary.get("sums") or {}).get("top_by_variant") or {}).values()
    max_len = max([max_len, *[len(rows or []) for rows in sums]])

    blackapple = ((summary.get("blackapple") or {}).get("top_by_variant") or {}).values()
    max_len = max([max_len, *[len(rows or []) for rows in blackapple]])
    return max_len or 10


def _summary_signature(summary: Dict[str, Any]) -> Dict[str, Any]:
    meta = ((summary.get("draw_sources") or {}).get("snapshot_meta") or {}).copy()
    excel_path = meta.get("excel_path")
    if excel_path:
        try:
            excel_rel = _safe_rel(Path(str(excel_path)))
        except Exception:
            excel_rel = str(excel_path)
    else:
        excel_rel = None
    meta = {
        "mode": meta.get("mode"),
        "ok": meta.get("ok"),
        "excel_path": excel_rel,
        "state_key": meta.get("state_key"),
        "aux_state_label": meta.get("aux_state_label"),
    }
    payload = {
        "snapshot_meta": meta,
        "config": summary.get("config") or {},
        **{key: summary.get(key) or {} for key in SUMMARY_SECTION_KEYS},
    }
    return _normalize_jsonish(payload)


def _normalize_jsonish(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _normalize_jsonish(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_normalize_jsonish(item) for item in value]
    return value


def _normalize_scalar(value: Any) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "True" if value else "False"
    if value is None:
        return ""
    if isinstance(value, float):
        text = f"{value:.12f}".rstrip("0").rstrip(".")
        return text or "0"
    if isinstance(value, str) and "." in value:
        try:
            number = float(value)
        except ValueError:
            return value
        text = f"{number:.12f}".rstrip("0").rstrip(".")
        return text or "0"
    return str(value)


def _normalize_df_rows(df: pd.DataFrame, *, state_key: str) -> List[Dict[str, str]]:
    if df.empty:
        return []
    rows = df.copy()
    if "StateKey" in rows.columns:
        rows = rows[rows["StateKey"] == state_key].copy()
    if rows.empty:
        return []
    rows = rows.fillna("")
    for col in rows.columns:
        rows[col] = rows[col].map(_normalize_scalar)
    rows = rows.sort_values(list(rows.columns), kind="mergesort").reset_index(drop=True)
    return rows.to_dict(orient="records")


def _diff_json(expected: Any, actual: Any, path: str = "") -> List[str]:
    if type(expected) is not type(actual):
        return [f"{path or '$'}: type {type(expected).__name__} != {type(actual).__name__}"]
    if isinstance(expected, dict):
        diffs: List[str] = []
        for key in sorted(set(expected.keys()) | set(actual.keys()), key=lambda item: str(item)):
            child = f"{path}.{key}" if path else str(key)
            if key not in expected:
                diffs.append(f"{child}: missing in expected")
                continue
            if key not in actual:
                diffs.append(f"{child}: missing in actual")
                continue
            diffs.extend(_diff_json(expected[key], actual[key], child))
            if len(diffs) >= 12:
                return diffs
        return diffs
    if isinstance(expected, list):
        if len(expected) != len(actual):
            return [f"{path or '$'}: len {len(expected)} != {len(actual)}"]
        diffs: List[str] = []
        for idx, (exp_item, act_item) in enumerate(zip(expected, actual)):
            child = f"{path}[{idx}]"
            diffs.extend(_diff_json(exp_item, act_item, child))
            if len(diffs) >= 12:
                return diffs
        return diffs
    if expected != actual:
        return [f"{path or '$'}: {expected!r} != {actual!r}"]
    return []


def _load_draws(base: Path, state_key: str) -> Dict[str, List[str]]:
    payload: Dict[str, List[str]] = {}
    for _, variant_key in VARIANTS:
        draws, _ = load_state_draws(state_key, variant=variant_key, base=base, max_n=1000)
        payload[variant_key] = draws
    return payload


def _build_states_with_winners(day_dir: Path, *, results_file: Path) -> List[SharepackState]:
    winners_by_state = _parse_results(results_file)
    states = _discover_states(day_dir)
    with_winners: List[SharepackState] = []
    for st in states:
        winners = winners_by_state.get(_norm_state(st.aux_state_label), {})
        with_winners.append(replace(st, winners=winners))
    return with_winners


def _compare_control_center_rows(
    *,
    day_dir: Path,
    sample: AuditSample,
    regenerated_summary: Dict[str, Any],
    regenerated_draws_dir: Path,
) -> Dict[str, Dict[str, Any]]:
    results_file = ROOT / "data" / "results" / f"{sample.date}.txt"
    states = _build_states_with_winners(day_dir, results_file=results_file)
    target = next((st for st in states if st.state_key == sample.state_key), None)
    if target is None:
        raise FileNotFoundError(f"State {sample.state_key} not found under {day_dir}")
    patched_states: List[SharepackState] = []
    for st in states:
        if st.state_key == sample.state_key:
            patched_states.append(
                replace(
                    st,
                    aux_draws_dir=regenerated_draws_dir,
                    summary=regenerated_summary,
                )
            )
        else:
            patched_states.append(st)

    df_due = _build_due_doubles_df(patched_states)
    df_repeat = _build_vtrac_repeat_watch_df(patched_states)
    artifact_frames: Dict[str, pd.DataFrame] = {
        "blackapple_alerts": _build_blackapple_df(patched_states),
        "due_doubles": df_due,
        "vtrac_repeat_watch": df_repeat,
        "profit_alerts": _build_profit_alerts_df(patched_states, df_due=df_due, df_repeat=df_repeat),
    }

    results: Dict[str, Dict[str, Any]] = {}
    cc_dir = day_dir / "control_center"
    for label, filename in CONTROL_CENTER_ARTIFACTS:
        sharepack_path = cc_dir / filename
        sharepack_df = pd.read_csv(sharepack_path, dtype=str, keep_default_na=False) if sharepack_path.exists() else pd.DataFrame()
        expected_rows = _normalize_df_rows(sharepack_df, state_key=sample.state_key)
        actual_rows = _normalize_df_rows(artifact_frames[label], state_key=sample.state_key)
        pass_flag = expected_rows == actual_rows
        diff = [] if pass_flag else _diff_json(expected_rows, actual_rows)
        results[label] = {
            "pass": pass_flag,
            "expected_rows": len(expected_rows),
            "actual_rows": len(actual_rows),
            "diff": diff[:8],
            "sharepack_csv": _safe_rel(sharepack_path),
        }
    return results


def _audit_sample(sample: AuditSample) -> Dict[str, Any]:
    day_dir = ROOT / "sharepacks" / sample.date
    state_dir = day_dir / sample.state_key
    if not day_dir.exists():
        raise FileNotFoundError(f"Missing sharepack day dir: {day_dir}")
    if not state_dir.exists():
        raise FileNotFoundError(f"Missing state dir: {state_dir}")
    summary_path = state_dir / "aux" / sample.state_key / "summary.json"
    if not summary_path.exists():
        raise FileNotFoundError(f"Missing Aux summary: {summary_path}")

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    snapshot_meta = ((summary.get("draw_sources") or {}).get("snapshot_meta") or {}).copy()
    excel_path = snapshot_meta.get("excel_path")
    if not excel_path:
        raise ValueError(f"No excel_path recorded in {summary_path}")
    excel_path_abs = ROOT / excel_path
    if not excel_path_abs.exists():
        raise FileNotFoundError(f"Recorded excel snapshot missing: {excel_path_abs}")

    max_n = int((summary.get("config") or {}).get("max_n_used") or 1000)
    positional_window = int((summary.get("config") or {}).get("positional_window_used") or 360)
    pairs_window = int((summary.get("config") or {}).get("pairs_window_used") or 360)
    sums_window = int((summary.get("config") or {}).get("sums_window_used") or 100)
    limit = _infer_limit(summary)

    sharepack_draws_dir = state_dir / "aux" / "draws"
    sharepack_draws = _load_draws(sharepack_draws_dir, sample.state_key)

    with tempfile.TemporaryDirectory(prefix=f"aux_parity_{sample.date}_{sample.state_key}_") as tmpdir:
        regenerated_summary = build_summary(
            sample.state_key,
            sample.date,
            snapshot_dir=Path(tmpdir),
            max_n=max_n,
            limit=limit,
            sums_window=sums_window,
            pairs_window=pairs_window,
            positional_window=positional_window,
            excel_path=str(excel_path_abs),
        )
        regenerated_draws = _load_draws(Path(tmpdir), sample.state_key)

        draw_results: Dict[str, Dict[str, Any]] = {}
        draw_pass = True
        for variant_title, variant_key in VARIANTS:
            exp_draws = sharepack_draws.get(variant_key) or []
            act_draws = regenerated_draws.get(variant_key) or []
            variant_pass = exp_draws == act_draws
            draw_pass = draw_pass and variant_pass
            draw_results[variant_title] = {
                "pass": variant_pass,
                "expected_count": len(exp_draws),
                "actual_count": len(act_draws),
                "expected_head": exp_draws[:5],
                "actual_head": act_draws[:5],
            }

        expected_signature = _summary_signature(summary)
        actual_signature = _summary_signature(regenerated_summary)
        summary_diff = _diff_json(expected_signature, actual_signature)
        summary_pass = not summary_diff

        control_center_results = _compare_control_center_rows(
            day_dir=day_dir,
            sample=sample,
            regenerated_summary=regenerated_summary,
            regenerated_draws_dir=Path(tmpdir),
        )
        cc_pass = all(section.get("pass") for section in control_center_results.values())

    return {
        "date": sample.date,
        "state_key": sample.state_key,
        "excel_path": excel_path,
        "summary_path": _safe_rel(summary_path),
        "aux_draws_dir": _safe_rel(sharepack_draws_dir),
        "limit_inferred": limit,
        "draw_parity_pass": draw_pass,
        "draw_results": draw_results,
        "summary_parity_pass": summary_pass,
        "summary_diff": summary_diff[:12],
        "control_center_parity_pass": cc_pass,
        "control_center_results": control_center_results,
        "overall_pass": draw_pass and summary_pass and cc_pass,
    }


def _render_md(results: Sequence[Dict[str, Any]]) -> str:
    total = len(results)
    passed = sum(1 for row in results if row.get("overall_pass"))
    lines: List[str] = [
        "# Aux / Control Center Parity Audit",
        "",
        "- Purpose: verify that selected frozen gold-day Aux / Control Center artifacts can be regenerated from the recorded workbook snapshot without drift.",
        f"- Samples audited: `{total}`",
        f"- Overall PASS: `{passed}/{total}`",
        "",
    ]
    for row in results:
        lines.append(f"## {row['date']} / {row['state_key']}")
        lines.append(f"- Workbook snapshot: `{row['excel_path']}`")
        lines.append(f"- Aux summary: `{row['summary_path']}`")
        lines.append(f"- Aux draws: `{row['aux_draws_dir']}`")
        lines.append(f"- Inferred top-list limit: `{row['limit_inferred']}`")
        lines.append(f"- Draw parity: `{'PASS' if row['draw_parity_pass'] else 'FAIL'}`")
        for variant, payload in (row.get("draw_results") or {}).items():
            lines.append(
                f"  - {variant}: `{'PASS' if payload.get('pass') else 'FAIL'}` "
                f"counts `{payload.get('expected_count')}=={payload.get('actual_count')}`"
            )
        lines.append(f"- Summary parity: `{'PASS' if row['summary_parity_pass'] else 'FAIL'}`")
        if row.get("summary_diff"):
            lines.append("  - Summary diffs:")
            for diff in row["summary_diff"][:6]:
                lines.append(f"    - `{diff}`")
        lines.append(f"- Control Center parity: `{'PASS' if row['control_center_parity_pass'] else 'FAIL'}`")
        for label, payload in (row.get("control_center_results") or {}).items():
            lines.append(
                f"  - {label}: `{'PASS' if payload.get('pass') else 'FAIL'}` "
                f"rows `{payload.get('expected_rows')}=={payload.get('actual_rows')}` "
                f"file `{payload.get('sharepack_csv')}`"
            )
            for diff in (payload.get("diff") or [])[:3]:
                lines.append(f"    - `{diff}`")
        lines.append(f"- Overall: `{'PASS' if row['overall_pass'] else 'FAIL'}`")
        lines.append("")
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Audit Aux / Control Center regeneration parity on frozen sharepacks.")
    ap.add_argument(
        "--sample",
        action="append",
        default=[],
        help="Sample to audit as DATE:STATEKEY. Repeat to audit multiple samples. Defaults to a representative trio.",
    )
    ap.add_argument(
        "--out-prefix",
        default="2026-03-20__AUX_CONTROL_CENTER__PARITY_AUDIT",
        help="Output prefix under docs/AAT9_KIT/FINAL VALIDATION/RUNS/ (default: %(default)s)",
    )
    args = ap.parse_args(list(argv) if argv is not None else None)

    raw_samples = args.sample or list(DEFAULT_SAMPLES)
    samples = [_parse_sample(item) for item in raw_samples]

    results = [_audit_sample(sample) for sample in samples]
    output_prefix = RUNS_DIR / args.out_prefix
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    md_path = output_prefix.with_suffix(".md")
    json_path = output_prefix.with_suffix(".json")
    md_path.write_text(_render_md(results), encoding="utf-8")
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(f"[aux-cc-parity] wrote {_safe_rel(md_path)}")
    print(f"[aux-cc-parity] wrote {_safe_rel(json_path)}")
    failing = [row for row in results if not row.get("overall_pass")]
    if failing:
        print(f"[aux-cc-parity] FAIL: {len(failing)} sample(s) had drift")
        return 1
    print(f"[aux-cc-parity] PASS: {len(results)}/{len(results)} sample(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
