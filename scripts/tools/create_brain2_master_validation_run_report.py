#!/usr/bin/env python3
"""
Create a per-date Brain 2 Master Validation run report for the analysis-arena branch.

This is a reporting/helper utility only:
- Reads frozen sharepack tracker artifacts for the results date.
- Reads derived Brain 2 runtime receipts (board bundle / scoreboard / shadow DPL /
  translation sandbox manifest).
- Produces a board-level post-results validation shell with useful auto-captured anchors.

It does NOT rerun analyzers, rebuild tables, or claim final analytical verdicts.
The output is intentionally a hybrid:
- locked artifact references and bounded summaries are auto-filled
- section conclusions remain for analyst review
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
RUNS2_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
TEMPLATE_PATH = (
    REPO_ROOT
    / "docs"
    / "AAT9_KIT"
    / "FINAL VALIDATION"
    / "final docs"
    / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
)

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


@dataclass(frozen=True)
class DayArtifacts:
    bundle_md: Path
    bundle_json: Path
    scoreboard_md: Path
    scoreboard_json: Path
    overlay_md: Path
    overlay_json: Path
    shadow_md: Path
    shadow_json: Path
    sandbox_md: Path
    sandbox_json: Path


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def safe_int(value: Any) -> int | None:
    try:
        return int(str(value).strip())
    except Exception:
        return None


def safe_float(value: Any) -> float | None:
    try:
        return float(str(value).strip())
    except Exception:
        return None


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _normalize_pick3_literal(value: Any) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _is_double(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 2


def _is_triple(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 1


def _mirror_pairs_present(triad: str) -> list[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    digits = set(triad)
    out: list[str] = []
    for d, m in MIRROR_MAP.items():
        if d < m and d in digits and m in digits:
            out.append(f"{d}/{m}")
    return sorted(set(out))


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        value = str(value).strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _analysis_artifacts(analysis_arena_dir: Path, *, results_date: str, board_name: str) -> DayArtifacts:
    stem = board_name
    return DayArtifacts(
        bundle_md=analysis_arena_dir / f"{results_date}__BOARD_REVIEW_BUNDLE__{stem}.md",
        bundle_json=analysis_arena_dir / f"{results_date}__BOARD_REVIEW_BUNDLE__{stem}.json",
        scoreboard_md=analysis_arena_dir / f"{results_date}__BOARD_SCOREBOARD__{stem}.md",
        scoreboard_json=analysis_arena_dir / f"{results_date}__BOARD_SCOREBOARD__{stem}.json",
        overlay_md=analysis_arena_dir / f"{results_date}__BOARD_SPILLOVER_OVERLAY__{stem}.md",
        overlay_json=analysis_arena_dir / f"{results_date}__BOARD_SPILLOVER_OVERLAY__{stem}.json",
        shadow_md=analysis_arena_dir / f"{results_date}__SHADOW_DECISION_POLICY__{stem}.md",
        shadow_json=analysis_arena_dir / f"{results_date}__SHADOW_DECISION_POLICY__{stem}.json",
        sandbox_md=analysis_arena_dir / f"{results_date}__TRANSLATION_SANDBOX_SEED__{stem}.md",
        sandbox_json=analysis_arena_dir / f"{results_date}__TRANSLATION_SANDBOX_SEED__{stem}.json",
    )


def _fmt_path(path: Path) -> str:
    return f"`{_safe_rel(path)}`" if path.exists() else f"`{_safe_rel(path)}` (missing)"


def _fmt_list(items: Sequence[str], *, empty: str = "_none_") -> str:
    ordered = _ordered_unique(items)
    if not ordered:
        return empty
    return ", ".join(f"`{item}`" for item in ordered)


def _top_scoreboard_rows(rows: Sequence[dict[str, Any]], *, limit: int = 5) -> list[str]:
    out: list[str] = []
    for row in sorted(rows, key=lambda r: int(r.get("score_rank") or 9999))[:limit]:
        canon = ", ".join((row.get("top_canonicals") or [])[:3]) or "-"
        out.append(
            f"`#{row.get('score_rank')} {row.get('state_key')}` role=`{row.get('role')}` "
            f"bucket=`{row.get('targeting_bucket')}` tracker=`{row.get('tracker_posture')}` "
            f"canonicals=`{canon}`"
        )
    return out


def _scoreboard_state_rank_map(rows: Sequence[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        state_key = str(row.get("state_key") or "").strip()
        rank = safe_int(row.get("score_rank"))
        if state_key and rank is not None:
            out[state_key] = rank
    return out


def _group_profit_alerts(rows: Sequence[dict[str, str]]) -> list[str]:
    by_state: dict[str, dict[str, Any]] = {}
    for row in rows:
        state_key = (row.get("StateKey") or "").strip()
        if not state_key:
            continue
        slot = by_state.setdefault(state_key, {"count": 0, "strength": 0.0, "alerts": set(), "suggested": set()})
        slot["count"] += 1
        slot["strength"] += safe_float(row.get("Strength")) or 0.0
        if row.get("AlertId"):
            slot["alerts"].add(row["AlertId"].strip())
        if row.get("Suggested"):
            slot["suggested"].add(row["Suggested"].strip())
    ranked = sorted(
        by_state.items(),
        key=lambda item: (-item[1]["strength"], -item[1]["count"], item[0].lower()),
    )
    out: list[str] = []
    for state_key, info in ranked[:5]:
        out.append(
            f"`{state_key}` alerts=`{info['count']}` strength_sum=`{info['strength']:.1f}` "
            f"ids=`{','.join(sorted(info['alerts'])) or '-'}` suggested=`{','.join(sorted(info['suggested'])) or '-'}`"
        )
    return out


def _group_compound_events(rows: Sequence[dict[str, str]]) -> list[str]:
    ranked = sorted(
        rows,
        key=lambda row: (-(safe_int(row.get("priority")) or -1), row.get("state_key", ""), row.get("variant", "")),
    )
    out: list[str] = []
    for row in ranked[:6]:
        out.append(
            f"`{row.get('state_key','')}` `{row.get('variant','')}` top_event=`{row.get('top_event','')}` "
            f"priority=`{row.get('priority','')}` candidates=`{row.get('candidate_alert_ids','') or '-'}`"
        )
    return out


def _group_blackapple(rows: Sequence[dict[str, str]], *, status: str) -> list[str]:
    ranked = [
        row
        for row in rows
        if (row.get("Status") or "").strip().upper() == status.upper()
    ]
    ranked.sort(key=lambda row: (-(safe_int(row.get("BA-Score")) or -1), row.get("StateKey", ""), row.get("Variant", "")))
    out: list[str] = []
    for row in ranked[:8]:
        out.append(
            f"`{row.get('StateKey','')}` `{row.get('Variant','')}` BA=`{row.get('BA-Score','')}` "
            f"examples=`{row.get('Examples','') or '-'}`"
        )
    return out


def _combined_due_rows(rows: Sequence[dict[str, str]]) -> list[dict[str, str]]:
    out = [row for row in rows if (row.get("Variant") or "").strip() == "Combined"]
    out.sort(key=lambda row: (-(safe_int(row.get("Draws Since Double")) or -1), row.get("StateKey", "")))
    return out


def _due_threshold_rows(rows: Sequence[dict[str, str]], *, minimum: int = 3) -> list[dict[str, str]]:
    return [row for row in _combined_due_rows(rows) if (safe_int(row.get("Draws Since Double")) or -1) >= minimum]


def _due_converting_rows(rows: Sequence[dict[str, str]]) -> list[str]:
    out: list[str] = []
    for row in _due_threshold_rows(rows):
        if (row.get("Midday Winner In Family") or "").strip() == "True" or (row.get("Evening Winner In Family") or "").strip() == "True":
            out.append(
                f"`{row.get('StateKey','')}` DS=`{row.get('Draws Since Double','')}` "
                f"midday_in_family=`{row.get('Midday Winner In Family','')}` "
                f"evening_in_family=`{row.get('Evening Winner In Family','')}`"
            )
    return out


def _daily_double_events(
    rows: Sequence[dict[str, str]],
    *,
    rank_by_state: dict[str, int],
) -> list[str]:
    out: list[str] = []
    for row in _combined_due_rows(rows):
        state_key = (row.get("StateKey") or "").strip()
        ds = row.get("Draws Since Double", "")
        for period_key, winner_key in (("Midday", "Winner Midday"), ("Evening", "Winner Evening")):
            winner = _normalize_pick3_literal(row.get(winner_key, ""))
            if not winner:
                continue
            mirror_pairs = _mirror_pairs_present(winner)
            if _is_triple(winner):
                kind = "triple"
            elif _is_double(winner):
                kind = "double"
            elif mirror_pairs:
                kind = "mirror_double"
            else:
                continue
            out.append(
                f"`{state_key}` `{period_key}` winner=`{winner}` type=`{kind}` "
                f"rank=`{rank_by_state.get(state_key, '-')}` DS=`{ds}` mirror_pairs=`{','.join(mirror_pairs) or '-'}`"
            )
    return out


def _top_reason_codes(state_decisions: Sequence[dict[str, Any]], *, limit: int = 8) -> list[str]:
    counts: Counter[str] = Counter()
    for row in state_decisions:
        for code in row.get("reason_codes") or []:
            code = str(code).strip()
            if code:
                counts[code] += 1
    return [f"`{code}` x{count}" for code, count in counts.most_common(limit)]


def _load_translation_learning(translation_manifest_json: Path) -> dict[str, list[str]]:
    if not translation_manifest_json.exists():
        return {
            "boxed": [],
            "straight": [],
            "vt_box": [],
            "positional": [],
            "blackapple": [],
            "profit": [],
            "due": [],
            "preserved": [],
        }

    manifest = read_json(translation_manifest_json)
    receipts = manifest.get("state_receipts") if isinstance(manifest, dict) else []
    boxed: Counter[str] = Counter()
    straight: Counter[str] = Counter()
    vt_box: Counter[str] = Counter()
    positional: Counter[str] = Counter()
    blackapple: Counter[str] = Counter()
    profit: Counter[str] = Counter()
    due: Counter[str] = Counter()
    preserved: Counter[str] = Counter()

    for receipt in receipts if isinstance(receipts, list) else []:
        seed_path_raw = str(receipt.get("seed_json") or "").strip()
        if not seed_path_raw:
            continue
        seed_path = REPO_ROOT / seed_path_raw
        if not seed_path.exists():
            continue
        try:
            seed = read_json(seed_path)
        except Exception:
            continue
        sand = seed.get("sandbox_hypotheses") if isinstance(seed.get("sandbox_hypotheses"), dict) else {}
        brain2 = seed.get("brain2_context") if isinstance(seed.get("brain2_context"), dict) else {}
        control_arm = seed.get("control_arm") if isinstance(seed.get("control_arm"), dict) else {}

        for item in sand.get("diagnostic_boxed_seed") or []:
            value = str(item.get("value") or "").strip()
            if value:
                boxed[value] += 1
        for item in sand.get("diagnostic_straight_seed") or []:
            value = str(item.get("value") or "").strip()
            if value:
                straight[value] += 1
        for item in sand.get("diagnostic_vt_box_seed") or []:
            value = str(item.get("value") or "").strip()
            if value:
                vt_box[value] += 1

        for item in brain2.get("positional_shortlist_top") or []:
            value = str(item.get("canonical") or item.get("combo") or "").strip()
            if value:
                positional[value] += 1
        for value in brain2.get("blackapple_recommended_canonicals") or []:
            value = str(value).strip()
            if value:
                blackapple[value] += 1
        for value in brain2.get("profit_alert_implied_canonicals") or []:
            value = str(value).strip()
            if value:
                profit[value] += 1
        for value in brain2.get("due_double_example_canonicals") or []:
            value = str(value).strip()
            if value:
                due[value] += 1
        for value in control_arm.get("preserved_not_budgeted_canonicals_top") or []:
            value = str(value).strip()
            if value:
                preserved[value] += 1

    def pack(counter: Counter[str]) -> list[str]:
        return [f"`{value}` x{count}" for value, count in counter.most_common(6)]

    return {
        "boxed": pack(boxed),
        "straight": pack(straight),
        "vt_box": pack(vt_box),
        "positional": pack(positional),
        "blackapple": pack(blackapple),
        "profit": pack(profit),
        "due": pack(due),
        "preserved": pack(preserved),
    }


def build_brain2_master_validation_report(
    *,
    results_date: str,
    history_date: str,
    artifacts: DayArtifacts,
    template_path: Path,
    board_scope_states: Sequence[str],
    scoreboard_rows: Sequence[dict[str, Any]],
    board_verdict: dict[str, Any],
    duplicate_pairs: Sequence[dict[str, Any]],
    shadow_verdict: dict[str, Any],
    state_decisions: Sequence[dict[str, Any]],
    profit_alert_rows: Sequence[dict[str, str]],
    compound_rows: Sequence[dict[str, str]],
    blackapple_rows: Sequence[dict[str, str]],
    due_rows: Sequence[dict[str, str]],
    tracker_rows: Sequence[dict[str, str]],
    translation_learning: dict[str, list[str]],
    control_center_dir: Path,
    control_arm_runs_dir: Path,
    doubles_inventory_md: Path | None = None,
    doubles_inventory_csv: Path | None = None,
) -> str:
    rank_by_state = _scoreboard_state_rank_map(scoreboard_rows)
    top_rows = _top_scoreboard_rows(scoreboard_rows)
    direct_receipts = board_verdict.get("direct_cross_state_receipts") or []
    strongest_pairs = []
    for pair in list(duplicate_pairs)[:5]:
        strongest_pairs.append(
            f"`{pair.get('state_a')}` + `{pair.get('state_b')}` score=`{pair.get('pair_score')}` "
            f"types=`{','.join(pair.get('relationship_types') or []) or '-'}`"
        )

    due_threshold = [
        f"`{row.get('StateKey','')}` DS=`{row.get('Draws Since Double','')}`"
        for row in _due_threshold_rows(due_rows)
    ]
    daily_double_events = _daily_double_events(due_rows, rank_by_state=rank_by_state)
    repeat_hits = [
        f"`{row.get('StateKey','')}` `{row.get('Variant','')}` idx=`{row.get('Current Index','')}`"
        for row in tracker_rows
        if (row.get("Current==WinnerVTRAC") or "").strip() == "True"
    ]

    play_states = shadow_verdict.get("play_states") or []
    watch_states = shadow_verdict.get("watch_states") or []
    skip_states = shadow_verdict.get("skip_states") or []

    lines: list[str] = []
    lines.append(f"# Brain 2 Master Validation Run Report — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Reference template:")
    lines.append(f"- `{_safe_rel(template_path)}`")
    lines.append("")
    lines.append("Relationship to the arena-era workflow:")
    lines.append(f"- Board runtime template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`")
    lines.append(f"- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`")
    lines.append(f"- Translation sandbox template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`")
    lines.append("")
    lines.append("## Scope")
    lines.append(f"- Results date (D): `{results_date}`")
    lines.append(f"- History workbook date (H): `{history_date}`")
    lines.append(f"- Board scope states ({len(board_scope_states)}): {_fmt_list(board_scope_states)}")
    lines.append("- Full-day tracker scope: `all states represented in the frozen control_center sharepack tables`")
    lines.append("")
    lines.append("## Locked Artifacts")
    lines.append(f"- Board review bundle: {_fmt_path(artifacts.bundle_md)} / {_fmt_path(artifacts.bundle_json)}")
    lines.append(f"- Board scoreboard: {_fmt_path(artifacts.scoreboard_md)} / {_fmt_path(artifacts.scoreboard_json)}")
    lines.append(f"- Board spillover overlay: {_fmt_path(artifacts.overlay_md)} / {_fmt_path(artifacts.overlay_json)}")
    lines.append(f"- Shadow DPL: {_fmt_path(artifacts.shadow_md)} / {_fmt_path(artifacts.shadow_json)}")
    lines.append(f"- Translation sandbox day manifest: {_fmt_path(artifacts.sandbox_md)} / {_fmt_path(artifacts.sandbox_json)}")
    lines.append(f"- Control Center root: `{_safe_rel(control_center_dir)}`")
    lines.append(f"- Control-arm grade directory: `{_safe_rel(control_arm_runs_dir)}`")
    if doubles_inventory_md or doubles_inventory_csv:
        lines.append(
            "- Window doubles inventory: "
            + " / ".join(
                item
                for item in (
                    _fmt_path(doubles_inventory_md) if doubles_inventory_md else "",
                    _fmt_path(doubles_inventory_csv) if doubles_inventory_csv else "",
                )
                if item
            )
        )
    lines.append("")
    lines.append("## Quick Auto-Captured Anchors")
    lines.append(f"- Top scoreboard rows: {'; '.join(top_rows) if top_rows else '_none_'}")
    lines.append(f"- Board verdict top_primary_target: `{board_verdict.get('top_primary_target') or '-'}`")
    lines.append(f"- Board verdict secondary_target: `{board_verdict.get('secondary_target') or '-'}`")
    lines.append(f"- Board verdict best_clean_host: `{board_verdict.get('best_clean_host') or '-'}`")
    lines.append(f"- Board verdict highest_context_support_state: `{board_verdict.get('highest_context_support_state') or '-'}`")
    lines.append(f"- Shadow DPL play states: {_fmt_list(play_states)}")
    lines.append(f"- Shadow DPL watch states: {_fmt_list(watch_states)}")
    lines.append(f"- Daily doubles / mirror doubles detected: {_fmt_list(daily_double_events, empty='_none detected_')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    def add_section(title: str, bullets: Sequence[str], prompts: Sequence[str]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("Auto-captured anchors:")
        for bullet in bullets or ["- _none_"]:
            lines.append(f"- {bullet}" if not bullet.startswith("- ") else bullet)
        lines.append("")
        lines.append("Analyst conclusion:")
        for prompt in prompts:
            lines.append(f"- {prompt}")
        lines.append("")

    add_section(
        "Part A — File Lock And Scope",
        [
            f"board scope states: {_fmt_list(board_scope_states)}",
            f"full-day tracker artifacts: `{_safe_rel(control_center_dir / 'profit_alerts.csv')}`, `{_safe_rel(control_center_dir / 'profit_compound_events.csv')}`, `{_safe_rel(control_center_dir / 'blackapple_alerts.csv')}`, `{_safe_rel(control_center_dir / 'due_doubles.csv')}`, `{_safe_rel(control_center_dir / 'vtrac_repeat_watch.csv')}`",
            "sharepack remains the frozen raw day snapshot; board artifacts are derived arena-era receipts on top of it",
        ],
        [
            "board scope notes: `...`",
            "full-day tracker scope notes: `...`",
            "missing artifact notes: `...`",
        ],
    )

    add_section(
        "Part B — Board Outcome Map",
        [
            f"top scoreboard anchors: {'; '.join(top_rows[:3]) if top_rows else '_none_'}",
            f"daily doubles / mirror doubles on the day: {_fmt_list(daily_double_events, empty='_none_')}",
            f"direct cross-state receipts surfaced by board verdict: {_fmt_list([str(x) for x in direct_receipts], empty='_none_')}",
        ],
        [
            "actual strongest day states: `...`",
            "states that converted meaningful structure: `...`",
            "states that were mostly echo / ambient only: `...`",
            "day-level structural class: `...`",
            "most important truth-side board insight: `...`",
        ],
    )

    add_section(
        "Part C — Scoreboard And Ranking Evaluation",
        [
            f"top scoreboard rows that mattered: {'; '.join(top_rows) if top_rows else '_none_'}",
            f"top_primary_target=`{board_verdict.get('top_primary_target') or '-'}` secondary_target=`{board_verdict.get('secondary_target') or '-'}`",
            f"best_clean_host=`{board_verdict.get('best_clean_host') or '-'}` highest_context_support_state=`{board_verdict.get('highest_context_support_state') or '-'}`",
            f"tight_core_states={_fmt_list(board_verdict.get('tight_core_states') or [], empty='-')}",
            f"watch_only_states={_fmt_list(board_verdict.get('watch_only_states') or [], empty='-')}",
            f"small_shoulder_states={_fmt_list(board_verdict.get('small_shoulder_states') or [], empty='-')}",
        ],
        [
            "highest-converting actual state rank(s): `...`",
            "bucket quality notes: `...`",
            "did the scoreboard ranking help or distort the day?: `...`",
            "most important scoreboard lesson: `...`",
        ],
    )

    add_section(
        "Part D — Shared Complexes, Carryover, And Spillover",
        [
            f"strongest overlap pairs: {'; '.join(strongest_pairs) if strongest_pairs else '_none_'}",
            f"direct cross-state receipts: {_fmt_list([str(x) for x in direct_receipts], empty='_none_')}",
            f"best relationship source: `{board_verdict.get('best_relationship_source') or '-'}`",
        ],
        [
            "most important shared complexes: `...`",
            "most important host state: `...`",
            "most important echo state: `...`",
            "most important cross-state carryover receipt: `...`",
            "did the board correctly treat the day as a shared pending complex?: `...`",
            "most important spillover lesson: `...`",
        ],
    )

    add_section(
        "Part E — Aggregate Tracker Inventory",
        [
            f"highest-value alert states: {'; '.join(_group_profit_alerts(profit_alert_rows)) or '_none_'}",
            f"compound-event leaders: {'; '.join(_group_compound_events(compound_rows)) or '_none_'}",
            f"Blackapple ALERT states: {'; '.join(_group_blackapple(blackapple_rows, status='ALERT')) or '_none_'}",
            f"due-double threshold states (DS>=3): {'; '.join(due_threshold[:8]) if due_threshold else '_none_'}",
            f"repeat-watch exact hits: {'; '.join(repeat_hits) if repeat_hits else '_none_'}",
        ],
        [
            "most important board-scope tracker states: `...`",
            "most important full-day tracker states outside the board: `...`",
            "did tracker posture materially explain the day?: `...`",
            "most important aggregate-tracker insight: `...`",
        ],
    )

    add_section(
        "Part F — Profit Alerts And Special Compound Events",
        [
            f"highest-value alert states: {'; '.join(_group_profit_alerts(profit_alert_rows)) or '_none_'}",
            f"top compound-event rows: {'; '.join(_group_compound_events(compound_rows)) or '_none_'}",
            f"profit alerts source: `{_safe_rel(control_center_dir / 'profit_alerts.csv')}`",
            f"compound events source: `{_safe_rel(control_center_dir / 'profit_compound_events.csv')}`",
        ],
        [
            "most important alert IDs: `...`",
            "implied-set conversions: `...`",
            "most important special compound events: `...`",
            "alert-rich but structurally weak states: `...`",
            "did profit alerts / compound events materially improve Brain 2?: `...`",
            "most important alert-layer lesson: `...`",
        ],
    )

    add_section(
        "Part G — Blackapple Board Review",
        [
            f"BA ALERT states: {'; '.join(_group_blackapple(blackapple_rows, status='ALERT')) or '_none_'}",
            f"BA WATCH states: {'; '.join(_group_blackapple(blackapple_rows, status='WATCH')) or '_none_'}",
            f"Blackapple source: `{_safe_rel(control_center_dir / 'blackapple_alerts.csv')}`",
        ],
        [
            "important BA recommendation carries: `...`",
            "states where BA looked stronger than the board gave credit for: `...`",
            "did BA function mainly as host indicator / echo amplifier / shortlist helper / noise / mixed?: `...`",
            "most important BA lesson: `...`",
        ],
    )

    add_section(
        "Part H — Due Doubles Ranked-State Evaluation",
        [
            f"ranked due states reviewed (DS>=3): {'; '.join(due_threshold) if due_threshold else '_none_'}",
            f"top due states that converted in-family: {'; '.join(_due_converting_rows(due_rows)) or '_none_'}",
            f"due doubles source: `{_safe_rel(control_center_dir / 'due_doubles.csv')}`",
        ],
        [
            "top due states that failed: `...`",
            "threshold states (3 draws missing) that converted: `...`",
            "important due families / examples that converted: `...`",
            "conversion class notes: `...`",
            "most important due-doubles ranking lesson: `...`",
        ],
    )

    add_section(
        "Part I — All Daily Doubles And Mirror Doubles Evidence Audit",
        [
            f"daily doubles / mirror doubles reviewed: {'; '.join(daily_double_events) if daily_double_events else '_none_'}",
            f"support sources: due-doubles=`{_safe_rel(control_center_dir / 'due_doubles.csv')}` BA=`{_safe_rel(control_center_dir / 'blackapple_alerts.csv')}` alerts=`{_safe_rel(control_center_dir / 'profit_alerts.csv')}`",
            f"window doubles inventory: {(' / '.join(x for x in (_fmt_path(doubles_inventory_md) if doubles_inventory_md else '', _fmt_path(doubles_inventory_csv) if doubles_inventory_csv else '') if x)) if (doubles_inventory_md or doubles_inventory_csv) else '_not provided_'}",
        ],
        [
            "most important strong-evidence double: `...`",
            "most important weak-evidence double: `...`",
            "most important doubles / mirror-doubles lesson: `...`",
        ],
    )

    add_section(
        "Part J — Shadow DPL And Board Posture Evaluation",
        [
            f"play states: {_fmt_list(play_states)}",
            f"watch states: {_fmt_list(watch_states)}",
            f"skip states: {_fmt_list(skip_states)}",
            f"top useful reason codes: {'; '.join(_top_reason_codes(state_decisions)) or '_none_'}",
            f"top_play_state=`{shadow_verdict.get('top_play_state') or '-'}` top_watch_state=`{shadow_verdict.get('top_watch_state') or '-'}`",
        ],
        [
            "watch states that should maybe have been play: `...`",
            "play states that were overpromoted: `...`",
            "mode / cap quality: `...`",
            "most important misleading reason codes: `...`",
            "most important DPL lesson: `...`",
        ],
    )

    add_section(
        "Part K — Translation Sandbox / Combination Learning Capture",
        [
            f"strongest boxed themes: {'; '.join(translation_learning.get('boxed') or []) or '_none_'}",
            f"strongest straight themes: {'; '.join(translation_learning.get('straight') or []) or '_none_'}",
            f"strongest VT-box themes: {'; '.join(translation_learning.get('vt_box') or []) or '_none_'}",
            f"repeated positional shortlist carries: {'; '.join(translation_learning.get('positional') or []) or '_none_'}",
            f"repeated Blackapple carries: {'; '.join(translation_learning.get('blackapple') or []) or '_none_'}",
            f"profit-alert implied carries: {'; '.join(translation_learning.get('profit') or []) or '_none_'}",
            f"due-double carries: {'; '.join(translation_learning.get('due') or []) or '_none_'}",
            f"preserved-not-budgeted canonicals: {'; '.join(translation_learning.get('preserved') or []) or '_none_'}",
        ],
        [
            "most important preserved-not-budgeted cluster: `...`",
            "strongest translator-learning note: `...`",
        ],
    )

    add_section(
        "Part L — Control-Arm Comparison",
        [
            f"candidate-universe grade: `{_safe_rel(control_arm_runs_dir / f'{results_date}__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md')}`",
            f"play-card grade: `{_safe_rel(control_arm_runs_dir / f'{results_date}__PLAY_CARD_GRADE__tool_only__arena_v0.md')}`",
            "B12/B24/B36 remain the baseline/control-arm comparison surface, not the arena branch truth",
        ],
        [
            "most important control-arm success: `...`",
            "most important control-arm suppression: `...`",
            "did the control arm outperform, underperform, or mostly lag Brain 2 truth?: `...`",
            "most important control-arm lesson: `...`",
        ],
    )

    add_section(
        "Part M — Final Board Lessons And Promotions",
        [
            f"top board runtime artifacts locked above; use this section to end with board-level lessons rather than state-by-state repetition",
        ],
        [
            "strongest board-level insight: `...`",
            "strongest tracker insight: `...`",
            "strongest cross-state carryover insight: `...`",
            "strongest doubles / mirror-doubles insight: `...`",
            "strongest translation-learning insight: `...`",
            "one thing that deserves later promotion: `...`",
            "one thing that should remain research-only for now: `...`",
            "one structural follow-up target: `...`",
            "one thing to watch on the next fresh runs: `...`",
        ],
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--analysis-arena-dir",
        required=True,
        help="Directory containing the Brain 2 runtime artifacts for the day",
    )
    ap.add_argument(
        "--board-name",
        default="analysis_arena_day_review",
        help="Board artifact suffix/name (default: analysis_arena_day_review)",
    )
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/<D>__BRAIN2_MASTER_VALIDATION.md)",
    )
    ap.add_argument(
        "--control-arm-runs-dir",
        default=str(RUNS_DIR),
        help="Directory holding Candidate Universe / Play Card grades (default legacy RUNS dir)",
    )
    ap.add_argument("--doubles-inventory-md", help="Optional doubles inventory Markdown path")
    ap.add_argument("--doubles-inventory-csv", help="Optional doubles inventory CSV path")
    ap.add_argument("--force", action="store_true", help="Overwrite output if it already exists")
    args = ap.parse_args()

    results_date = parse_iso_date(args.date).isoformat()
    analysis_arena_dir = Path(args.analysis_arena_dir)
    out_path = Path(args.out) if args.out else (RUNS2_DIR / f"{results_date}__BRAIN2_MASTER_VALIDATION.md")
    control_arm_runs_dir = Path(args.control_arm_runs_dir)
    doubles_inventory_md = Path(args.doubles_inventory_md) if args.doubles_inventory_md else None
    doubles_inventory_csv = Path(args.doubles_inventory_csv) if args.doubles_inventory_csv else None

    if out_path.exists() and not args.force:
        raise SystemExit(f"Output already exists: {out_path}. Use --force to overwrite.")

    artifacts = _analysis_artifacts(analysis_arena_dir, results_date=results_date, board_name=args.board_name)
    control_center_dir = REPO_ROOT / "sharepacks" / results_date / "control_center"
    meta_path = control_center_dir / "meta.json"
    history_date = (parse_iso_date(results_date) - timedelta(days=1)).isoformat()
    if meta_path.exists():
        meta = read_json(meta_path)
        if isinstance(meta, dict):
            history_date = str(meta.get("history_date") or history_date)

    scoreboard = read_json(artifacts.scoreboard_json) if artifacts.scoreboard_json.exists() else {}
    bundle = read_json(artifacts.bundle_json) if artifacts.bundle_json.exists() else {}
    shadow = read_json(artifacts.shadow_json) if artifacts.shadow_json.exists() else {}

    scoreboard_rows = scoreboard.get("scoreboard_rows") if isinstance(scoreboard, dict) else []
    scoreboard_rows = scoreboard_rows if isinstance(scoreboard_rows, list) else []
    board_verdict = scoreboard.get("board_verdict") if isinstance(scoreboard, dict) else {}
    if not isinstance(board_verdict, dict):
        board_verdict = {}
    duplicate_pairs = scoreboard.get("duplicate_pairs") if isinstance(scoreboard, dict) else []
    duplicate_pairs = duplicate_pairs if isinstance(duplicate_pairs, list) else []
    shadow_verdict = shadow.get("shadow_verdict") if isinstance(shadow, dict) else {}
    if not isinstance(shadow_verdict, dict):
        shadow_verdict = {}
    state_decisions = shadow.get("state_decisions") if isinstance(shadow, dict) else []
    state_decisions = state_decisions if isinstance(state_decisions, list) else []

    report = build_brain2_master_validation_report(
        results_date=results_date,
        history_date=history_date,
        artifacts=artifacts,
        template_path=TEMPLATE_PATH,
        board_scope_states=[str(row.get("state_key") or "") for row in scoreboard_rows],
        scoreboard_rows=scoreboard_rows,
        board_verdict=board_verdict,
        duplicate_pairs=duplicate_pairs,
        shadow_verdict=shadow_verdict,
        state_decisions=state_decisions,
        profit_alert_rows=load_csv_rows(control_center_dir / "profit_alerts.csv"),
        compound_rows=load_csv_rows(control_center_dir / "profit_compound_events.csv"),
        blackapple_rows=load_csv_rows(control_center_dir / "blackapple_alerts.csv"),
        due_rows=load_csv_rows(control_center_dir / "due_doubles.csv"),
        tracker_rows=load_csv_rows(control_center_dir / "vtrac_repeat_watch.csv"),
        translation_learning=_load_translation_learning(artifacts.sandbox_json),
        control_center_dir=control_center_dir,
        control_arm_runs_dir=control_arm_runs_dir,
        doubles_inventory_md=doubles_inventory_md,
        doubles_inventory_csv=doubles_inventory_csv,
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
