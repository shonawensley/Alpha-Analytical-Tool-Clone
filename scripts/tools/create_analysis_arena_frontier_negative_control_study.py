#!/usr/bin/env python3
"""Create a cross-window frontier negative-control study for Analysis Arena."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
CONTROL_LABEL = "no_conversion"
COHORT_ORDER = ("strict_box", "straight", "box_gap", "vt_only", CONTROL_LABEL, "low_conviction_control")


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-root", default=str(DEFAULT_RUNS2_ROOT), help="RUNS_2 root to scan for completed windows.")
    ap.add_argument("--window-root", action="append", default=[], help="Optional explicit window roots. Can be repeated.")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-cases-csv", default="", help="Optional enriched case roster CSV output path.")
    ap.add_argument("--out-lifts-csv", default="", help="Optional feature-lift CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths() -> Dict[str, Path]:
    stem = "AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY"
    return {
        "md": DEFAULT_FINAL_DOCS / f"{stem}.md",
        "json": DEFAULT_FINAL_DOCS / f"{stem}.json",
        "cases_csv": DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_CASES.csv",
        "lifts_csv": DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_LIFTS.csv",
    }


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def _as_int(value: Any) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return 0


def _as_float(value: Any) -> float:
    try:
        return float(str(value).strip())
    except Exception:
        return 0.0


def _rate(count: int, denominator: int) -> float:
    return count / denominator if denominator else 0.0


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _discover_windows(runs2_root: Path) -> List[Path]:
    out: List[Path] = []
    for path in sorted(runs2_root.glob("WINDOW_*")):
        if "__PREALIGN_SNAPSHOT" in path.name:
            continue
        stem = path.name
        required = [
            path / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv",
            path / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv",
            path / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv",
        ]
        if all(item.exists() for item in required):
            out.append(path)
    return out


def _case_key(row: Dict[str, str]) -> Tuple[str, str, str]:
    return (
        str(row.get("date") or "").strip(),
        str(row.get("state_key") or "").strip(),
        str(row.get("winner") or "").strip(),
    )


def _cohort_tags(rows: Sequence[Dict[str, str]]) -> set[str]:
    tags: set[str] = set()
    for row in rows:
        for token in str(row.get("cohort_tags") or "").split("|"):
            token = token.strip()
            if token:
                tags.add(token)
        primary = str(row.get("primary_cohort") or "").strip()
        if primary:
            tags.add(primary)
    return tags


def _best_string(rows: Sequence[Dict[str, str]], key: str, *, order: Sequence[str] | None = None) -> str:
    values = [str(row.get(key) or "").strip() for row in rows if str(row.get(key) or "").strip()]
    if not values:
        return ""
    if order:
        for item in order:
            if item in values:
                return item
    return values[0]


def _best_float(rows: Sequence[Dict[str, str]], key: str) -> float:
    vals = [_as_float(row.get(key)) for row in rows if str(row.get(key) or "").strip()]
    return max(vals) if vals else 0.0


def _parse_frontier_case(window_root: Path, row: Dict[str, str], hit_rows: Sequence[Dict[str, str]], translator_rows: Sequence[Dict[str, str]]) -> Dict[str, Any]:
    fired_tests = {token.strip() for token in str(row.get("fired_tests") or "").split(",") if token.strip()}
    tags = _cohort_tags(translator_rows)
    strict_box = any(_truthy(item.get("play_box_strict_hit")) for item in hit_rows)
    straight = any(_truthy(item.get("play_straight_hit")) for item in hit_rows)
    any_box = any(_truthy(item.get("play_box_any_hit")) for item in hit_rows) or _truthy(row.get("boxed_hit_any"))
    vt_only = any(
        str(item.get("hit_primary_class") or "").strip() == "VTRAC_ONLY" or _truthy(item.get("play_vtrac_only_hit"))
        for item in hit_rows
    ) and not strict_box and not straight
    box_gap = "BOX_GAP" in tags
    exact_gap = "EXACT_GAP" in tags
    any_credit = _as_int(row.get("credited_event_count")) > 0 or bool(hit_rows)
    no_conversion = not any_credit and not box_gap and not exact_gap
    low_conviction_control = no_conversion or vt_only

    enriched = {
        "window": window_root.name.replace("WINDOW_", ""),
        "window_root": safe_rel(window_root),
        "date": str(row.get("date") or "").strip(),
        "state_key": str(row.get("state_key") or "").strip(),
        "winner": str(row.get("winner") or "").strip(),
        "rank_evaluation_status": str(row.get("rank_evaluation_status") or "NOT_EVALUABLE"),
        "rank_evaluation_reason": str(row.get("rank_evaluation_reason") or "INVALID_STATIC_ORDER"),
        "board_rank": (
            _as_int(row.get("best_board_rank"))
            if str(row.get("rank_evaluation_status") or "") == "EVALUABLE"
            else None
        ),
        "frontier_signature_type": str(row.get("frontier_signature_type") or "").strip(),
        "signature_strength": str(row.get("signature_strength") or "").strip(),
        "literal_frontier_score": _as_float(row.get("literal_frontier_score")),
        "family_frontier_score": _as_float(row.get("family_frontier_score")),
        "vtrac_frontier_score": _as_float(row.get("vtrac_frontier_score")),
        "frontier_purity_score": _as_float(row.get("frontier_purity_score")),
        "vertical_stability_score": _as_float(row.get("vertical_stability_score")),
        "cross_variant_echo_score": _as_float(row.get("cross_variant_echo_score")),
        "compression_score": _as_float(row.get("compression_score")),
        "hidden_winner_score": _as_float(row.get("hidden_winner_score")),
        "feeder_progression_score": _as_float(row.get("feeder_progression_score")),
        "double_anchor_score": _as_float(row.get("double_anchor_score")),
        "frontier_strength_score": _as_float(row.get("frontier_strength_score")),
        "credited_event_count": _as_int(row.get("credited_event_count")),
        "hit_class_rollup": str(row.get("hit_class_rollup") or "").strip(),
        "arena_final_candidate_signature_best": str(row.get("arena_final_candidate_signature_best") or "").strip(),
        "double_context_strength_best": str(row.get("double_context_strength_best") or "").strip(),
        "inventory_types": str(row.get("inventory_types") or "").strip(),
        "translator_tag_count": len(tags),
        "translator_tags": "|".join(sorted(tags)),
        "translator_primary_cohort": _best_string(
            translator_rows,
            "primary_cohort",
            order=("BOX_GAP", "EXACT_GAP", "EXACT_CONVERTED", "BOX_CONVERTED", "VT_CONVERTED", "PRESERVED", "ARENA_EXPLICIT", "BOX_FINALIST", "VT_FINALIST"),
        ),
        "translator_support_score_max": _best_float(translator_rows, "translator_support_score"),
        "strict_box": strict_box,
        "straight": straight,
        "vt_only": vt_only,
        "strict_box_hit": strict_box,
        "straight_hit": straight,
        "any_box_hit": any_box,
        "vt_only_hit": vt_only,
        "box_gap": box_gap,
        "exact_gap": exact_gap,
        "no_conversion": no_conversion,
        "low_conviction_control": low_conviction_control,
        "feature_sig_hidden": str(row.get("frontier_signature_type") or "") == "HIDDEN_COMPRESSED_FRONTIER",
        "feature_sig_feeder": str(row.get("frontier_signature_type") or "") == "FEEDER_TO_FRONTIER",
        "feature_sig_vtrac": str(row.get("frontier_signature_type") or "") == "VTRAC_FRONTIER",
        "feature_sig_family": str(row.get("frontier_signature_type") or "") == "FAMILY_FRONTIER",
        "feature_sig_literal": str(row.get("frontier_signature_type") or "") == "LITERAL_FRONTIER",
        "feature_test_hidden_mask": "hidden_mask_v1" in fired_tests,
        "feature_test_feeder": "feeder_progression_v1" in fired_tests,
        "feature_test_vtrac": "vtrac_frontier_v1" in fired_tests,
        "feature_test_family": "family_frontier_v1" in fired_tests,
        "feature_test_literal": "literal_frontier_v1" in fired_tests,
        "feature_test_double_anchor": "double_anchor_v1" in fired_tests,
        "feature_test_cross_variant": "cross_variant_echo_v1" in fired_tests,
        "feature_hidden_ge_050": _as_float(row.get("hidden_winner_score")) >= 0.50,
        "feature_feeder_ge_045": _as_float(row.get("feeder_progression_score")) >= 0.45,
        "feature_vtrac_ge_035": _as_float(row.get("vtrac_frontier_score")) >= 0.35,
        "feature_family_ge_030": _as_float(row.get("family_frontier_score")) >= 0.30,
        "feature_literal_ge_020": _as_float(row.get("literal_frontier_score")) >= 0.20,
        "feature_double_anchor_ge_055": _as_float(row.get("double_anchor_score")) >= 0.55,
        "feature_cross_variant_ge_045": _as_float(row.get("cross_variant_echo_score")) >= 0.45,
        "feature_strength_ge_070": _as_float(row.get("frontier_strength_score")) >= 70.0,
    }
    return enriched


def _feature_definitions() -> List[Tuple[str, str]]:
    return [
        ("feature_sig_hidden", "Signature: HIDDEN_COMPRESSED_FRONTIER"),
        ("feature_sig_feeder", "Signature: FEEDER_TO_FRONTIER"),
        ("feature_sig_vtrac", "Signature: VTRAC_FRONTIER"),
        ("feature_sig_family", "Signature: FAMILY_FRONTIER"),
        ("feature_sig_literal", "Signature: LITERAL_FRONTIER"),
        ("feature_test_hidden_mask", "Test: hidden_mask_v1"),
        ("feature_test_feeder", "Test: feeder_progression_v1"),
        ("feature_test_vtrac", "Test: vtrac_frontier_v1"),
        ("feature_test_family", "Test: family_frontier_v1"),
        ("feature_test_literal", "Test: literal_frontier_v1"),
        ("feature_test_double_anchor", "Test: double_anchor_v1"),
        ("feature_test_cross_variant", "Test: cross_variant_echo_v1"),
        ("feature_hidden_ge_050", "Score threshold: hidden_winner_score >= 0.50"),
        ("feature_feeder_ge_045", "Score threshold: feeder_progression_score >= 0.45"),
        ("feature_vtrac_ge_035", "Score threshold: vtrac_frontier_score >= 0.35"),
        ("feature_family_ge_030", "Score threshold: family_frontier_score >= 0.30"),
        ("feature_literal_ge_020", "Score threshold: literal_frontier_score >= 0.20"),
        ("feature_double_anchor_ge_055", "Score threshold: double_anchor_score >= 0.55"),
        ("feature_cross_variant_ge_045", "Score threshold: cross_variant_echo_score >= 0.45"),
        ("feature_strength_ge_070", "Score threshold: frontier_strength_score >= 70"),
    ]


def _lift(target_rate: float, control_rate: float) -> float:
    if control_rate <= 0.0:
        return 999.0 if target_rate > 0.0 else 0.0
    return target_rate / control_rate


def build_payload(window_roots: Sequence[Path]) -> Dict[str, Any]:
    cases: List[Dict[str, Any]] = []
    warnings: List[str] = []
    for window_root in window_roots:
        stem = window_root.name
        frontier_rows = _read_csv_rows(window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv")
        hit_rows = _read_csv_rows(window_root / f"{stem}__ANALYSIS_ARENA__HIT_ROSTER.csv")
        translator_rows = _read_csv_rows(window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv")
        hit_lookup: Dict[Tuple[str, str, str], List[Dict[str, str]]] = defaultdict(list)
        translator_lookup: Dict[Tuple[str, str, str], List[Dict[str, str]]] = defaultdict(list)
        for row in hit_rows:
            hit_lookup[_case_key(row)].append(row)
        for row in translator_rows:
            translator_lookup[_case_key(row)].append(row)
        if not frontier_rows:
            warnings.append(f"{window_root.name}: frontier cases CSV missing or empty")
            continue
        for row in frontier_rows:
            cases.append(
                _parse_frontier_case(
                    window_root,
                    row,
                    hit_lookup.get(_case_key(row), []),
                    translator_lookup.get(_case_key(row), []),
                )
            )

    feature_rows: List[Dict[str, Any]] = []
    cohort_counts: Dict[str, int] = {label: 0 for label in COHORT_ORDER}
    for label in COHORT_ORDER:
        cohort_counts[label] = sum(1 for row in cases if bool(row.get(label)))
    cohorts: Dict[str, List[Dict[str, Any]]] = {label: [row for row in cases if bool(row.get(label))] for label in COHORT_ORDER}

    for feature_key, feature_label in _feature_definitions():
        overall_count = sum(1 for row in cases if bool(row.get(feature_key)))
        feature_row: Dict[str, Any] = {
            "feature_key": feature_key,
            "feature_label": feature_label,
            "overall_count": overall_count,
            "overall_denominator": len(cases),
            "overall_rate": _rate(overall_count, len(cases)),
        }
        control_rows = cohorts[CONTROL_LABEL]
        control_count = sum(1 for row in control_rows if bool(row.get(feature_key)))
        control_rate = _rate(control_count, len(control_rows))
        feature_row[f"{CONTROL_LABEL}_count"] = control_count
        feature_row[f"{CONTROL_LABEL}_denominator"] = len(control_rows)
        feature_row[f"{CONTROL_LABEL}_rate"] = control_rate
        for cohort in ("strict_box", "straight", "box_gap", "vt_only", "low_conviction_control"):
            rows = cohorts[cohort]
            count = sum(1 for row in rows if bool(row.get(feature_key)))
            rate = _rate(count, len(rows))
            feature_row[f"{cohort}_count"] = count
            feature_row[f"{cohort}_denominator"] = len(rows)
            feature_row[f"{cohort}_rate"] = rate
            feature_row[f"{cohort}_lift_vs_{CONTROL_LABEL}"] = _lift(rate, control_rate)
            feature_row[f"{cohort}_minus_{CONTROL_LABEL}"] = rate - control_rate
        feature_rows.append(feature_row)

    def _score_summary(label: str) -> Dict[str, float]:
        rows = cohorts[label]
        if not rows:
            return {}
        keys = (
            "literal_frontier_score",
            "family_frontier_score",
            "vtrac_frontier_score",
            "frontier_purity_score",
            "vertical_stability_score",
            "cross_variant_echo_score",
            "compression_score",
            "hidden_winner_score",
            "feeder_progression_score",
            "double_anchor_score",
            "frontier_strength_score",
        )
        return {
            key: round(sum(float(row.get(key) or 0.0) for row in rows) / len(rows), 6)
            for key in keys
        }

    def _signature_mix(label: str) -> Dict[str, int]:
        rows = cohorts[label]
        return dict(sorted(Counter(str(row.get("frontier_signature_type") or "") for row in rows).items()))

    def _top_features(cohort: str, *, limit: int = 6) -> List[Dict[str, Any]]:
        ranked = [
            row
            for row in feature_rows
            if row.get(f"{cohort}_count", 0) and row.get(f"{cohort}_rate", 0.0) >= 0.10
        ]
        ranked.sort(
            key=lambda row: (
                float(row.get(f"{cohort}_lift_vs_{CONTROL_LABEL}", 0.0)),
                float(row.get(f"{cohort}_minus_{CONTROL_LABEL}", 0.0)),
                float(row.get(f"{cohort}_rate", 0.0)),
            ),
            reverse=True,
        )
        out: List[Dict[str, Any]] = []
        for row in ranked[:limit]:
            out.append(
                {
                    "feature_label": row["feature_label"],
                    "cohort_rate": round(float(row.get(f"{cohort}_rate", 0.0)), 6),
                    "control_rate": round(float(row.get(f"{CONTROL_LABEL}_rate", 0.0)), 6),
                    "lift_vs_control": round(float(row.get(f"{cohort}_lift_vs_{CONTROL_LABEL}", 0.0)), 6),
                    "delta_vs_control": round(float(row.get(f"{cohort}_minus_{CONTROL_LABEL}", 0.0)), 6),
                }
            )
        return out

    ambient_features = [
        {
            "feature_label": row["feature_label"],
            "control_rate": round(float(row.get(f"{CONTROL_LABEL}_rate", 0.0)), 6),
            "strict_box_lift": round(float(row.get("strict_box_lift_vs_no_conversion", 0.0)), 6),
            "box_gap_lift": round(float(row.get("box_gap_lift_vs_no_conversion", 0.0)), 6),
        }
        for row in feature_rows
        if float(row.get(f"{CONTROL_LABEL}_rate", 0.0)) >= 0.35
        and float(row.get("strict_box_lift_vs_no_conversion", 0.0)) <= 1.35
        and float(row.get("box_gap_lift_vs_no_conversion", 0.0)) <= 1.35
    ]
    ambient_features.sort(key=lambda row: (-float(row["control_rate"]), row["feature_label"]))

    payload = {
        "metadata": {
            "runs2_root": safe_rel(DEFAULT_RUNS2_ROOT),
            "windows": [safe_rel(path) for path in window_roots],
            "case_count": len(cases),
            "warnings": warnings,
        },
        "cohort_counts": cohort_counts,
        "cohort_score_averages": {label: _score_summary(label) for label in COHORT_ORDER},
        "signature_mix": {label: _signature_mix(label) for label in COHORT_ORDER},
        "top_discriminative_features": {
            "strict_box_vs_no_conversion": _top_features("strict_box"),
            "straight_vs_no_conversion": _top_features("straight"),
            "box_gap_vs_no_conversion": _top_features("box_gap"),
            "vt_only_vs_no_conversion": _top_features("vt_only"),
        },
        "ambient_features": ambient_features[:8],
        "feature_rows": feature_rows,
        "cases": cases,
    }
    return payload


def _render_markdown(payload: Dict[str, Any], *, cases_csv: Path, lifts_csv: Path) -> str:
    meta = payload.get("metadata") or {}
    cohort_counts = payload.get("cohort_counts") or {}
    score_averages = payload.get("cohort_score_averages") or {}
    signature_mix = payload.get("signature_mix") or {}
    top_features = payload.get("top_discriminative_features") or {}
    ambient_features = payload.get("ambient_features") or []
    case_count = int(meta.get("case_count", 0) or 0)
    lines: List[str] = [
        "# Analysis Arena Frontier Negative-Control Study",
        "",
        "## 1. Scope",
        "",
        f"- Windows reviewed: `{len(meta.get('windows') or [])}`",
        f"- Frontier cases reviewed: `{case_count}`",
        f"- Enriched case roster: `{safe_rel(cases_csv)}`",
        f"- Feature lift table: `{safe_rel(lifts_csv)}`",
        "",
        "## 2. Cohort Inventory",
        "",
    ]
    for label in COHORT_ORDER:
        count = int(cohort_counts.get(label, 0) or 0)
        lines.append(f"- `{label}`: `{count}` (`{_pct(_rate(count, case_count))}`)")

    lines += [
        "",
        "## 3. Cohort Score Averages",
        "",
        "| Cohort | Strength | Hidden | Feeder | VTRAC | Family | Literal | Double |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for label in COHORT_ORDER:
        block = score_averages.get(label) or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    f"{float(block.get('frontier_strength_score', 0.0)):.2f}",
                    f"{float(block.get('hidden_winner_score', 0.0)):.3f}",
                    f"{float(block.get('feeder_progression_score', 0.0)):.3f}",
                    f"{float(block.get('vtrac_frontier_score', 0.0)):.3f}",
                    f"{float(block.get('family_frontier_score', 0.0)):.3f}",
                    f"{float(block.get('literal_frontier_score', 0.0)):.3f}",
                    f"{float(block.get('double_anchor_score', 0.0)):.3f}",
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## 4. Signature Mix",
        "",
    ]
    for label in ("strict_box", "straight", "box_gap", "vt_only", CONTROL_LABEL):
        mix = signature_mix.get(label) or {}
        mix_text = ", ".join(f"`{key}` x{value}" for key, value in mix.items()) or "_none_"
        lines.append(f"- `{label}`: {mix_text}")

    lines += [
        "",
        "## 5. Discriminative Frontier Features",
        "",
    ]
    for label, header in (
        ("strict_box_vs_no_conversion", "Strict box vs no-conversion"),
        ("straight_vs_no_conversion", "Straight vs no-conversion"),
        ("box_gap_vs_no_conversion", "Box-gap vs no-conversion"),
        ("vt_only_vs_no_conversion", "VT-only vs no-conversion"),
    ):
        lines.append(f"### {header}")
        lines.append("")
        rows = top_features.get(label) or []
        if not rows:
            lines.append("- No features crossed the current reporting threshold.")
            lines.append("")
            continue
        for row in rows:
            lines.append(
                f"- `{row['feature_label']}` cohort=`{_pct(float(row['cohort_rate']))}` "
                f"control=`{_pct(float(row['control_rate']))}` "
                f"lift=`{row['lift_vs_control']:.2f}x` "
                f"delta=`{_pct(float(row['delta_vs_control']))}`"
            )
        lines.append("")

    lines += [
        "## 6. Ambient / Non-Discriminative Frontier Features",
        "",
    ]
    if ambient_features:
        for row in ambient_features:
            lines.append(
                f"- `{row['feature_label']}` control=`{_pct(float(row['control_rate']))}` "
                f"strict-box lift=`{row['strict_box_lift']:.2f}x` "
                f"box-gap lift=`{row['box_gap_lift']:.2f}x`"
            )
    else:
        lines.append("- No broad ambient frontier traits crossed the current reporting threshold.")

    if meta.get("warnings"):
        lines += ["", "## Warnings", ""]
        for warning in meta.get("warnings") or []:
            lines.append(f"- {warning}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    runs2_root = _resolve_path(args.runs2_root)
    window_roots = [_resolve_path(value) for value in list(args.window_root or [])] or _discover_windows(runs2_root)
    outputs = _default_paths()
    out_md = _resolve_path(args.out_md) if args.out_md else outputs["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else outputs["json"]
    out_cases_csv = _resolve_path(args.out_cases_csv) if args.out_cases_csv else outputs["cases_csv"]
    out_lifts_csv = _resolve_path(args.out_lifts_csv) if args.out_lifts_csv else outputs["lifts_csv"]

    payload = build_payload(window_roots)
    _write_csv(out_cases_csv, payload.get("cases") or [], force=bool(args.force))
    _write_csv(out_lifts_csv, payload.get("feature_rows") or [], force=bool(args.force))
    _write_json(out_json, payload, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload, cases_csv=out_cases_csv, lifts_csv=out_lifts_csv), force=bool(args.force))

    print(safe_rel(out_md))
    print(safe_rel(out_json))
    print(safe_rel(out_cases_csv))
    print(safe_rel(out_lifts_csv))


if __name__ == "__main__":
    main()
