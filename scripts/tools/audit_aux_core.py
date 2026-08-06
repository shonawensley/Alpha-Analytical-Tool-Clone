#!/usr/bin/env python3
"""Run AUX CORE across one frozen Gold Day and grade posted results."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.tools.aux_core import (  # noqa: E402
    build_aux_core,
    grade_winner,
    render_external_markdown,
    render_markdown,
    safe_rel,
    sha256_file,
    write_json,
)


def _read_winners(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        rows = [dict(row) for row in csv.DictReader(fh)]
    required = {"state", "period", "winner"}
    missing = required.difference(rows[0] if rows else {})
    if missing:
        raise ValueError(
            f"Winner manifest missing columns {sorted(missing)}: {safe_rel(path)}"
        )
    return rows


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in keys})


def _bool(value: Any) -> bool:
    if isinstance(value, (list, tuple, dict, set)):
        return bool(value)
    return bool(value)


def _roles(row: Any) -> str:
    if not isinstance(row, dict):
        return ""
    return "|".join(row.get("role_labels") or [])


def _lineages(row: Any) -> str:
    if not isinstance(row, dict):
        return ""
    return "|".join(row.get("base_source_lineages") or [])


def _burden(row: Any, key: str) -> Any:
    if not isinstance(row, dict):
        return ""
    burden = row.get("burden")
    return burden.get(key, "") if isinstance(burden, dict) else ""


def _tier(row: Any) -> str:
    if not isinstance(row, dict):
        return ""
    return str(row.get("review_tier") or "")


def _narrowed(row: Any) -> bool:
    return _tier(row) in {
        "TIER_A_INDEPENDENT_IDENTITY",
        "TIER_B_SOURCE_PLUS_STRUCTURE",
    }


def event_row(grading: Mapping[str, Any]) -> Dict[str, Any]:
    align = grading["block_alignment"]
    b1 = align["block_1_due_pairs"]
    b2 = align["block_2_boxed_combinations"]
    b3 = align["block_3_vtrac_due"]
    b4 = align["block_4_sums"]
    b5 = align["block_5_blackapple"]
    b6 = align["block_6_repeat_watch"]
    b7 = align["block_7_badge_concentration"]
    b8 = align["block_8_shortlist_convergence"]
    b9 = align["block_9_positional"]
    b10 = align["block_10_cross_block_convergence"]
    conversion = grading["conversion_read"]
    exact = b10.get("exact_literal")
    lane = b10.get("ordered_lane")
    box = b10.get("canonical_box")
    index = b10.get("vtrac_index")
    return {
        "results_date": grading["results_date"],
        "state_key": grading["state_key"],
        "period": grading["period"],
        "winner": grading["winner"],
        "winner_canonical": grading["winner_canonical"],
        "winner_vtrac_index": grading["winner_vtrac_index"],
        "winner_ordered_vcode": grading["winner_ordered_vcode"],
        "frozen_object_sha256": grading["frozen_object_sha256"],
        "b1_due_pair_alignment": b1["aligned"],
        "b1_due_pair_receipt_count": len(b1["receipts"]),
        "b2_target_variant_canonical": _bool(
            b2["target_variant_canonical_match"]
        ),
        "b3_target_variant_vtrac": _bool(b3["target_variant_index_match"]),
        "b4_target_variant_sum": _bool(b4["target_variant_sum_match"]),
        "b4_target_variant_root": _bool(b4["target_variant_root_sum_match"]),
        "b5_status": b5["status"],
        "b5_active": b5["active"],
        "b5_canonical": _bool(b5["canonical_match"]),
        "b6_active_current_index": b6["active_current_index_match"],
        "b6_last_repeat_index": b6["last_repeat_index_match"],
        "b7_selected_index": _bool(b7["selected_index_match"]),
        "b7_canonical_member": _bool(b7["canonical_member_match"]),
        "b8_positional_exact": _bool(b8["positional_exact_match"]),
        "b8_any_canonical": _bool(b8["canonical_matches"]),
        "b8_profit_alert": _bool(b8["profit_alert_matches"]),
        "b9_target_exact_positions": b9["target_variant_exact_position_count"],
        "b9_all_variant_exact_positions": b9[
            "all_variant_same_position_exact_count"
        ],
        "b9_exact_rank": b9["shortlist_exact_rank"],
        "b9_canonical_rank": b9["shortlist_canonical_rank"],
        "b9_vtrac_rank": b9["shortlist_vtrac_rank"],
        "b10_highest_specificity": conversion["highest_specificity_reached"],
        "b10_highest_specificity_tier": conversion[
            "highest_specificity_tier"
        ],
        "b10_translation_gap": conversion["translation_gap"],
        "b10_highest_narrowed_specificity": conversion[
            "highest_narrowed_specificity"
        ],
        "b10_narrowed_translation_gap": conversion[
            "narrowed_translation_gap"
        ],
        "b10_highest_untranslated_specificity": conversion[
            "highest_untranslated_specificity"
        ],
        "b10_exact": bool(exact),
        "b10_ordered_lane": bool(lane),
        "b10_canonical": bool(box),
        "b10_vtrac": bool(index),
        "b10_exact_tier": _tier(exact),
        "b10_lane_tier": _tier(lane),
        "b10_canonical_tier": _tier(box),
        "b10_vtrac_tier": _tier(index),
        "b10_exact_narrowed": _narrowed(exact),
        "b10_ordered_lane_narrowed": _narrowed(lane),
        "b10_canonical_narrowed": _narrowed(box),
        "b10_vtrac_narrowed": _narrowed(index),
        "b10_exact_lineages": _lineages(exact),
        "b10_lane_lineages": _lineages(lane),
        "b10_canonical_lineages": _lineages(box),
        "b10_vtrac_lineages": _lineages(index),
        "b10_exact_roles": _roles(exact),
        "b10_lane_roles": _roles(lane),
        "b10_canonical_roles": _roles(box),
        "b10_vtrac_roles": _roles(index),
        "b10_exact_burden": _burden(exact, "exact_literals"),
        "b10_lane_burden": _burden(lane, "exact_literals"),
        "b10_canonical_burden": _burden(box, "exact_literals"),
        "b10_vtrac_burden": _burden(index, "exact_literals"),
    }


def _rate(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 6) if denominator else 0.0


def build_rollup(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    total = len(rows)
    highest = Counter(str(row["b10_highest_specificity"]) for row in rows)
    highest_tiers = Counter(
        str(row["b10_highest_specificity_tier"]) for row in rows
    )
    gaps = Counter(str(row["b10_translation_gap"]) for row in rows)
    highest_narrowed = Counter(
        str(row["b10_highest_narrowed_specificity"]) for row in rows
    )
    narrowed_gaps = Counter(
        str(row["b10_narrowed_translation_gap"]) for row in rows
    )
    boolean_fields = [
        "b1_due_pair_alignment",
        "b2_target_variant_canonical",
        "b3_target_variant_vtrac",
        "b4_target_variant_sum",
        "b4_target_variant_root",
        "b5_canonical",
        "b6_active_current_index",
        "b6_last_repeat_index",
        "b7_selected_index",
        "b7_canonical_member",
        "b8_positional_exact",
        "b8_any_canonical",
        "b8_profit_alert",
        "b10_exact",
        "b10_ordered_lane",
        "b10_canonical",
        "b10_vtrac",
        "b10_exact_narrowed",
        "b10_ordered_lane_narrowed",
        "b10_canonical_narrowed",
        "b10_vtrac_narrowed",
    ]
    alignments = {}
    for field in boolean_fields:
        count = sum(1 for row in rows if _bool(row.get(field)))
        alignments[field] = {
            "count": count,
            "total": total,
            "rate": _rate(count, total),
        }

    by_period: Dict[str, Any] = {}
    for period in ("Midday", "Evening"):
        period_rows = [row for row in rows if row["period"] == period]
        by_period[period] = {
            "events": len(period_rows),
            "b10_exact": sum(1 for row in period_rows if _bool(row["b10_exact"])),
            "b10_ordered_lane": sum(
                1 for row in period_rows if _bool(row["b10_ordered_lane"])
            ),
            "b10_canonical": sum(
                1 for row in period_rows if _bool(row["b10_canonical"])
            ),
            "b10_vtrac": sum(1 for row in period_rows if _bool(row["b10_vtrac"])),
        }

    return {
        "schema_version": "aux_core_gold_day_rollup_v1",
        "events": total,
        "states": len({row["state_key"] for row in rows}),
        "periods": dict(Counter(str(row["period"]) for row in rows)),
        "highest_specificity_distribution": dict(sorted(highest.items())),
        "highest_specificity_tier_distribution": dict(
            sorted(highest_tiers.items())
        ),
        "translation_gap_distribution": dict(sorted(gaps.items())),
        "highest_narrowed_specificity_distribution": dict(
            sorted(highest_narrowed.items())
        ),
        "narrowed_translation_gap_distribution": dict(
            sorted(narrowed_gaps.items())
        ),
        "alignment_metrics": alignments,
        "by_period": by_period,
        "interpretation_boundary": (
            "Rates describe post-result alignment with frozen pre-result evidence. "
            "They are reverse-engineering measurements, not a claim that every "
            "qualifying row was a funded or selected final prediction."
        ),
    }


def render_rollup(
    rollup: Mapping[str, Any],
    *,
    day_dir: Path,
    winner_manifest: Path,
    manifest: Mapping[str, Any],
) -> str:
    lines = [
        "# AUX CORE Gold Day Audit",
        "",
        f"- Frozen day: `{safe_rel(day_dir)}`",
        f"- Winner manifest: `{safe_rel(winner_manifest)}`",
        f"- States: `{rollup['states']}`",
        f"- Outcomes: `{rollup['events']}`",
        f"- Errors: `{len(manifest['errors'])}`",
        "",
        "## Artifact Map",
        "",
        "- `MANIFEST.json`: frozen-object and result-grade lineage by state.",
        "- `AUX_CORE_EVENT_LEDGER.csv`: one post-result alignment row per outcome.",
        "- `AUX_CORE_GOLD_DAY_ROLLUP.json`: machine-readable Gold Day summary.",
        "- `SKIPPED_OR_ERROR_ROWS.csv`: explicit failure inventory.",
        "- `states/<STATE>/AUX_CORE__PRE_RESULT.*`: frozen Blocks 1-10.",
        "- `states/<STATE>/AUX_CORE__<PERIOD>__<WINNER>*`: separate result join.",
        "",
        "## Identity Progression",
        "",
        "| Highest specificity | Outcomes | Rate |",
        "|---|---:|---:|",
    ]
    for level, count in rollup["highest_specificity_distribution"].items():
        lines.append(
            f"| `{level}` | {count} | {_rate(int(count), int(rollup['events'])):.1%} |"
        )
    lines.extend(
        [
            "",
            "## Narrowed Identity Progression",
            "",
            "| Highest narrowed specificity | Outcomes | Rate |",
            "|---|---:|---:|",
        ]
    )
    for level, count in rollup[
        "highest_narrowed_specificity_distribution"
    ].items():
        lines.append(
            f"| `{level}` | {count} | {_rate(int(count), int(rollup['events'])):.1%} |"
        )
    lines.extend(
        [
            "",
            "## Translation Gaps",
            "",
            "| Gap | Outcomes | Rate |",
            "|---|---:|---:|",
        ]
    )
    for gap, count in rollup["translation_gap_distribution"].items():
        lines.append(
            f"| `{gap}` | {count} | {_rate(int(count), int(rollup['events'])):.1%} |"
        )
    lines.extend(
        [
            "",
            "## Narrowed-Source Translation Gaps",
            "",
            "| Gap | Outcomes | Rate |",
            "|---|---:|---:|",
        ]
    )
    for gap, count in rollup[
        "narrowed_translation_gap_distribution"
    ].items():
        lines.append(
            f"| `{gap}` | {count} | {_rate(int(count), int(rollup['events'])):.1%} |"
        )
    lines.extend(
        [
            "",
            "## Block Alignment",
            "",
            "| Receipt | Outcomes | Rate |",
            "|---|---:|---:|",
        ]
    )
    for field, metrics in rollup["alignment_metrics"].items():
        lines.append(
            f"| `{field}` | {metrics['count']} / {metrics['total']} | "
            f"{float(metrics['rate']):.1%} |"
        )
    lines.extend(
        [
            "",
            rollup["interpretation_boundary"],
            "",
            "Review ordering inside Block 10 is deterministic but explicitly "
            "`REVIEW_ORDER_NOT_CALIBRATED`; raw native scores from different "
            "source families are never added.",
            "",
        ]
    )
    return "\n".join(lines)


def _state_names(rows: Iterable[Mapping[str, str]]) -> list[str]:
    return sorted({str(row["state"]).strip() for row in rows if row.get("state")})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day-dir", required=True)
    parser.add_argument("--winner-manifest", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument(
        "--state",
        action="append",
        default=[],
        help="Optional state filter; repeat for multiple states.",
    )
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    day_dir = Path(args.day_dir).resolve()
    winner_manifest = Path(args.winner_manifest).resolve()
    out_dir = Path(args.out_dir).resolve()
    if out_dir.exists() and any(out_dir.iterdir()) and not args.force:
        raise SystemExit(f"Output directory is not empty; pass --force: {out_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)

    winner_rows = _read_winners(winner_manifest)
    if args.state:
        allowed = set(args.state)
        winner_rows = [row for row in winner_rows if row["state"] in allowed]
    if not winner_rows:
        raise SystemExit("No winner rows selected")
    by_state: Dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in winner_rows:
        by_state[row["state"]].append(row)

    event_rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    state_manifest = []
    for state_key in sorted(by_state):
        try:
            payload = build_aux_core(
                state_key=state_key,
                results_date=day_dir.name,
                day_dir=day_dir,
            )
            state_dir = out_dir / "states" / state_key
            pre_result_path = state_dir / "AUX_CORE__PRE_RESULT.json"
            compact_report_path = state_dir / "AUX_CORE__PRE_RESULT.md"
            full_report_path = state_dir / "AUX_CORE__FULL_PRE_RESULT.md"
            write_json(pre_result_path, payload)
            compact_report_path.write_text(
                render_markdown(payload),
                encoding="utf-8",
            )
            full_report_path.write_text(
                render_external_markdown(payload),
                encoding="utf-8",
            )
            state_events = []
            for winner_row in sorted(
                by_state[state_key],
                key=lambda row: row["period"],
            ):
                grading = grade_winner(
                    payload,
                    period=winner_row["period"],
                    winner=winner_row["winner"],
                )
                period = grading["period"]
                winner = grading["winner"]
                grade_path = (
                    state_dir
                    / f"AUX_CORE__{period}__{winner}__POST_RESULT.json"
                )
                grade_report_path = (
                    state_dir / f"AUX_CORE__{period}__{winner}.md"
                )
                write_json(grade_path, grading)
                grade_report_path.write_text(
                    render_markdown(payload, grading=grading),
                    encoding="utf-8",
                )
                row = event_row(grading)
                event_rows.append(row)
                state_events.append(
                    {
                        "period": period,
                        "winner": winner,
                        "grading_path": safe_rel(grade_path),
                        "grading_sha256": sha256_file(grade_path),
                        "grading_report_path": safe_rel(grade_report_path),
                        "grading_report_sha256": sha256_file(grade_report_path),
                    }
                )
            state_manifest.append(
                {
                    "state_key": state_key,
                    "frozen_object_sha256": payload["frozen_object_sha256"],
                    "pre_result_path": safe_rel(pre_result_path),
                    "pre_result_file_sha256": sha256_file(pre_result_path),
                    "compact_report_path": safe_rel(compact_report_path),
                    "compact_report_sha256": sha256_file(compact_report_path),
                    "full_report_path": safe_rel(full_report_path),
                    "full_report_sha256": sha256_file(full_report_path),
                    "events": state_events,
                }
            )
        except Exception as exc:
            errors.append(
                {
                    "state_key": state_key,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )

    _write_csv(out_dir / "AUX_CORE_EVENT_LEDGER.csv", event_rows)
    _write_csv(out_dir / "SKIPPED_OR_ERROR_ROWS.csv", errors)
    rollup = build_rollup(event_rows)
    write_json(out_dir / "AUX_CORE_GOLD_DAY_ROLLUP.json", rollup)
    manifest = {
        "schema_version": "aux_core_gold_day_manifest_v1",
        "day_dir": safe_rel(day_dir),
        "winner_manifest": {
            "path": safe_rel(winner_manifest),
            "sha256": sha256_file(winner_manifest),
            "selected_rows": len(winner_rows),
            "selected_states": _state_names(winner_rows),
        },
        "completed_states": len(state_manifest),
        "completed_events": len(event_rows),
        "states": state_manifest,
        "errors": errors,
    }
    write_json(out_dir / "MANIFEST.json", manifest)
    (out_dir / "START_HERE.md").write_text(
        render_rollup(
            rollup,
            day_dir=day_dir,
            winner_manifest=winner_manifest,
            manifest=manifest,
        ),
        encoding="utf-8",
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
