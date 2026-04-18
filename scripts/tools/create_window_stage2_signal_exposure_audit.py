#!/usr/bin/env python3
"""Create Stage-2 signal exposure and false-positive proxy reports.

Stage 1 asks: "did the completed window preserve winner-relevant evidence?"
Stage 2 asks: "how much total candidate exposure did those signals create?"

This script is intentionally read-only against prediction artifacts. It does not
change scoring, candidate generation, or budgeting. It converts completed window
artifacts into denominators that can safely teach future translator work.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import (  # type: ignore
    iter_window_dates,
    load_scoreboard,
    load_state_seed_from_manifest_entry,
    load_translation_manifest,
    safe_rel,
)
from scripts.tools.create_window_evidence_utilization_audit import (  # type: ignore
    SignalValue,
    _event_id,
    _match_value,
    _safe_float,
    _safe_int,
    _signals_from_seed,
    _truthy,
)


FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_PRO_FILES = [
    REPO_ROOT / "tasks" / "PRO_92.txt",
    REPO_ROOT / "tasks" / "PRO_93.txt",
]
PRIMARY_PLAY_CARD_STRATEGIES = (
    "analysis_prefix",
    "v0_2_default",
    "play_box_first",
    "conversion_box_first",
)


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root.")
    ap.add_argument(
        "--final-docs-dir",
        default=str(FINAL_DOCS_DIR),
        help="Directory containing repeatable Analysis Arena protocol docs.",
    )
    ap.add_argument(
        "--pro-feedback",
        action="append",
        default=[],
        help="Optional PRO feedback file. Can be passed multiple times.",
    )
    ap.add_argument(
        "--include-control-pack-combos",
        action="store_true",
        help="Also expose candidate-universe pack combos. Defaults to canonical pack exposure only.",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _read_json(path: Path) -> Any:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


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
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _default_paths(window_root: Path, final_docs_dir: Path) -> Dict[str, Path]:
    stem = window_root.name
    prefix = f"{stem}__ANALYSIS_ARENA"
    return {
        "perf": window_root / f"{prefix}__PERFORMANCE_GAP__ledger.csv",
        "util": window_root / f"{prefix}__EVIDENCE_UTILIZATION_LEDGER.csv",
        "audit_json": window_root / f"{prefix}__EVIDENCE_UTILIZATION_AUDIT.json",
        "attribution": window_root / f"{prefix}__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv",
        "interpretation": window_root / f"{prefix}__AUDIT_INTERPRETATION_PASS.json",
        "priority_cases": window_root / f"{prefix}__AUDIT_INTERPRETATION_PRIORITY_CASES.csv",
        "signal_decisions": window_root / f"{prefix}__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv",
        "decay_json": window_root / f"{prefix}__DECAY_CARRYOVER_SCORECARD.json",
        "frontier_json": window_root / f"{prefix}__C1_C2_FRONTIER_ANALYSIS.json",
        "baseline_ssot_md": window_root / f"{prefix}__AUDIT_BASELINE_SSOT.md",
        "baseline_ssot_json": window_root / f"{prefix}__AUDIT_BASELINE_SSOT.json",
        "exposure_csv": window_root / f"{prefix}__STAGE2_SIGNAL_EXPOSURE_LEDGER.csv",
        "scorecard_md": window_root / f"{prefix}__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.md",
        "scorecard_json": window_root / f"{prefix}__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.json",
        "decision_csv": window_root / f"{prefix}__STAGE2_SIGNAL_PROMOTION_DECISION_MATRIX.csv",
        "lane_md": window_root / f"{prefix}__STAGE2_LANE_SHARPNESS_REPORT.md",
        "fixture_csv": window_root / f"{prefix}__STAGE2_TRANSLATOR_FIXTURE_CANDIDATES.csv",
        "stage2_md": window_root / f"{prefix}__STAGE2_AUDIT_INTERPRETATION.md",
        "stage2_json": window_root / f"{prefix}__STAGE2_AUDIT_INTERPRETATION.json",
        "protocol_md": final_docs_dir / "AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md",
    }


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _canon(value: Any) -> str:
    digits = _digits_only(value)
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return "".join(sorted(digits)) if len(digits) == 3 else ""


def _pct(count: int | float, total: int | float) -> str:
    return f"{100.0 * float(count) / float(total):.1f}%" if total else "0.0%"


def _rate(count: int | float, total: int | float) -> float:
    return float(count) / float(total) if total else 0.0


def _median(values: Sequence[int]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _avg(values: Sequence[int]) -> float:
    return sum(values) / len(values) if values else 0.0


def _ordered_unique(values: Iterable[Any]) -> List[str]:
    out: List[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _join_ids(values: Iterable[Any]) -> str:
    return ";".join(_ordered_unique(str(value or "") for value in values))


def _split_ids(value: Any) -> List[str]:
    raw = str(value or "").strip()
    if not raw:
        return []
    if ";" in raw:
        return [part for part in raw.split(";") if part]
    return [raw]


def _source_key(row: Dict[str, Any]) -> str:
    return f"{row.get('source_family')}:{row.get('source_tool')}"


def _event_key(row: Dict[str, Any]) -> str:
    if row.get("event_id"):
        return str(row.get("event_id"))
    return f"{row.get('date', '')}|{row.get('state_key', '')}|{row.get('period', '')}|{row.get('winner', '')}"


def _state_day_key(date: str, state_key: str) -> str:
    return f"{date}|{state_key}"


def _infer_target_lane(signal: SignalValue) -> str:
    tool = signal.source_tool.lower()
    path = signal.source_path.lower()
    if signal.value_kind == "vtrac_index" or "vtrac" in tool or "vt_" in tool:
        return "vtrac"
    if signal.value_kind == "literal" or "straight" in tool or "combo" in tool:
        return "straight"
    if "context" in tool and signal.value_kind != "canonical":
        return "context"
    return "boxed"


def _rough_space_size(value_kind: str, target_lane: str) -> int:
    if value_kind == "vtrac_index" or target_lane == "vtrac":
        return 35
    if value_kind == "literal" or target_lane == "straight":
        return 1000
    return 220


def _decision_for_scorecard(row: Dict[str, Any]) -> Tuple[str, str]:
    active_days = _safe_int(row.get("active_state_days"))
    avg_pool = _safe_float(row.get("avg_pool_size"))
    lane_rate = _safe_float(row.get("lane_hit_value_rate"))
    event_rate = _safe_float(row.get("winner_event_support_rate"))
    lift = _safe_float(row.get("rough_lift_vs_naive"))
    target_lane = str(row.get("target_lane") or "")
    source_tool = str(row.get("source_tool") or "")

    if active_days < 10:
        return (
            "sample_too_small",
            "Keep as fixture/context only until a broader denominator exists.",
        )
    if "candidate_universe_union" in source_tool or avg_pool >= 80:
        return (
            "denominator_only_broad_control",
            "Useful as a control-arm exposure denominator; too broad for direct promotion.",
        )
    if target_lane == "vtrac":
        if lane_rate >= 0.20 or lift >= 1.8 or event_rate >= 0.35:
            return (
                "vtrac_watch_decay_only_until_box_pairing",
                "Territory signal is live, but must pair with boxed/straight evidence before promotion.",
            )
        return (
            "vtrac_context_only",
            "VTRAC evidence remains context until it sharpens or pairs with box evidence.",
        )
    if target_lane == "straight":
        if lane_rate >= 0.015 and lift >= 2.5 and avg_pool <= 40:
            return (
                "straight_fixture_candidate",
                "Rare enough and sharp enough to become a straight-lane teaching fixture.",
            )
        if lane_rate >= 0.008 and lift >= 1.5:
            return (
                "straight_supporting_gate",
                "Straight signal has value but should support stricter gates instead of standalone promotion.",
            )
        return (
            "straight_context_or_negative_control",
            "Straight exposure did not clear promotion thresholds in this window.",
        )
    if target_lane == "boxed":
        if lane_rate >= 0.04 and lift >= 1.8 and avg_pool <= 30:
            return (
                "boxed_fixture_candidate",
                "Box signal has usable sharpness and bounded exposure.",
            )
        if lane_rate >= 0.02 or event_rate >= 0.20:
            return (
                "boxed_supporting_gate",
                "Box signal is useful but should be combined with other evidence before spending.",
            )
        return (
            "boxed_context_or_negative_control",
            "Box signal did not clear promotion thresholds in this window.",
        )
    return (
        "context_only",
        "Context signal should not promote directly without sharper lane evidence.",
    )


def _signal_to_dict(signal: SignalValue) -> Dict[str, Any]:
    payload = asdict(signal)
    payload["target_lane"] = _infer_target_lane(signal)
    return payload


def _load_json_rel(path_text: Any) -> Any:
    raw = str(path_text or "").strip()
    if not raw:
        return {}
    path = Path(raw)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return _read_json(path)


def _append_list_signals(
    signals: List[SignalValue],
    values: Iterable[Any],
    *,
    source_family: str,
    source_tool: str,
    source_path: str,
    value_kind: str,
    promoted_stage: str,
    badge_or_alert: str = "",
    source_tags: str = "",
) -> None:
    for idx, value in enumerate(values, start=1):
        text = str(value or "").strip()
        if not text:
            continue
        signals.append(
            SignalValue(
                source_family=source_family,
                source_tool=source_tool,
                source_path=source_path,
                value=text,
                value_kind=value_kind,
                rank=str(idx),
                badge_or_alert=badge_or_alert,
                source_tags=source_tags,
                promoted_stage=promoted_stage,
            )
        )


def _append_pack_signals(
    signals: List[SignalValue],
    packs: Iterable[Any],
    *,
    include_combos: bool,
) -> None:
    for pack_idx, pack in enumerate(packs, start=1):
        if not isinstance(pack, dict):
            continue
        method_id = str(pack.get("method_id") or "unknown").strip()
        pack_id = str(pack.get("pack_id") or method_id or "unknown").strip()
        tags = pack.get("why_tags") or []
        tag_text = "|".join(str(tag) for tag in tags if str(tag).strip()) if isinstance(tags, list) else str(tags or "")
        stage = "candidate_universe"
        mode = str(pack.get("play_mode") or "")
        for idx, value in enumerate(pack.get("canonicals") or [], start=1):
            signals.append(
                SignalValue(
                    source_family="old_candidate_universe",
                    source_tool=f"pack_method:{method_id}:canonical",
                    source_path=f"candidate_universe.packs.{pack_id}.canonicals",
                    value=str(value),
                    value_kind="canonical",
                    rank=f"{pack_idx}.{idx}",
                    badge_or_alert=mode,
                    source_tags=tag_text,
                    promoted_stage=stage,
                )
            )
        if not include_combos:
            continue
        for idx, value in enumerate(pack.get("combos") or [], start=1):
            signals.append(
                SignalValue(
                    source_family="old_candidate_universe",
                    source_tool=f"pack_method:{method_id}:combo",
                    source_path=f"candidate_universe.packs.{pack_id}.combos",
                    value=str(value),
                    value_kind="literal",
                    rank=f"{pack_idx}.{idx}",
                    badge_or_alert=mode,
                    source_tags=tag_text,
                    promoted_stage=stage,
                )
            )


def _append_play_card_strategy_signals(signals: List[SignalValue], play_card: Dict[str, Any]) -> None:
    strategies = play_card.get("strategies") or {}
    if not isinstance(strategies, dict):
        return
    for strategy_name in PRIMARY_PLAY_CARD_STRATEGIES:
        strategy = strategies.get(strategy_name) or {}
        if not isinstance(strategy, dict):
            continue
        for budget in ("B12", "B24", "B36"):
            pack = strategy.get(budget) or {}
            if not isinstance(pack, dict):
                continue
            source_prefix = f"strategy:{strategy_name}:{budget}"
            _append_list_signals(
                signals,
                pack.get("boxed_canonicals") or [],
                source_family="old_play_card",
                source_tool=f"{source_prefix}:boxed_canonicals",
                source_path=f"play_card.strategies.{strategy_name}.{budget}.boxed_canonicals",
                value_kind="canonical",
                promoted_stage="play_card",
                badge_or_alert=budget,
                source_tags=strategy_name,
            )
            _append_list_signals(
                signals,
                pack.get("combos") or [],
                source_family="old_play_card",
                source_tool=f"{source_prefix}:combos",
                source_path=f"play_card.strategies.{strategy_name}.{budget}.combos",
                value_kind="literal",
                promoted_stage="play_card",
                badge_or_alert=budget,
                source_tags=strategy_name,
            )


def _augment_full_control_signals(seed: Dict[str, Any], *, include_control_pack_combos: bool) -> Tuple[List[SignalValue], List[str]]:
    signals: List[SignalValue] = []
    warnings: List[str] = []
    control = seed.get("control_arm") or {}
    cu_ref = control.get("candidate_universe") or {}
    pc_ref = control.get("play_card") or {}

    candidate_universe = _load_json_rel(cu_ref.get("path"))
    if isinstance(candidate_universe, dict) and candidate_universe:
        _append_list_signals(
            signals,
            candidate_universe.get("union_combos") or [],
            source_family="old_candidate_universe",
            source_tool="candidate_universe_union_combo",
            source_path="candidate_universe.union_combos",
            value_kind="literal",
            promoted_stage="candidate_universe",
        )
        _append_pack_signals(
            signals,
            candidate_universe.get("packs") or [],
            include_combos=include_control_pack_combos,
        )
    elif cu_ref.get("path"):
        warnings.append(f"Missing candidate universe file: {cu_ref.get('path')}")

    play_card = _load_json_rel(pc_ref.get("path"))
    if isinstance(play_card, dict) and play_card:
        _append_play_card_strategy_signals(signals, play_card)
    elif pc_ref.get("path"):
        warnings.append(f"Missing play card file: {pc_ref.get('path')}")
    return signals, warnings


def _load_scoreboard_rows(window_root: Path, dates: Sequence[str]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    out: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for date in dates:
        try:
            scoreboard = load_scoreboard(window_root, date)
        except Exception:
            continue
        for row in scoreboard.get("scoreboard_rows") or []:
            if not isinstance(row, dict):
                continue
            state_key = str(row.get("state_key") or "").strip()
            if state_key:
                out[(date, state_key)] = row
    return out


def _load_seed_entries(window_root: Path, dates: Sequence[str]) -> List[Tuple[str, str, Dict[str, Any], Dict[str, Any]]]:
    out: List[Tuple[str, str, Dict[str, Any], Dict[str, Any]]] = []
    for date in dates:
        try:
            manifest = load_translation_manifest(window_root, date)
        except Exception:
            continue
        for entry in manifest.get("state_receipts") or []:
            if not isinstance(entry, dict):
                continue
            state_key = str(entry.get("state_key") or "").strip()
            if not state_key:
                continue
            seed = load_state_seed_from_manifest_entry(entry)
            if isinstance(seed, dict) and seed:
                out.append((date, state_key, entry, seed))
    return out


def _events_by_state_day(perf_rows: Sequence[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    out: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in perf_rows:
        date = str(row.get("date") or "").strip()
        state_key = str(row.get("state_key") or "").strip()
        winner = _digits_only(row.get("winner"))
        if not date or not state_key or len(winner) != 3:
            continue
        event = dict(row)
        event["winner"] = winner
        event["event_id"] = _event_id(event)
        if not event.get("winner_canonical"):
            event["winner_canonical"] = _canon(winner)
        out[_state_day_key(date, state_key)].append(event)
    return out


def _best_match_for_signal(signal: SignalValue, events: Sequence[Dict[str, str]]) -> Dict[str, Any]:
    matched_event_ids: List[str] = []
    exact_event_ids: List[str] = []
    box_event_ids: List[str] = []
    vt_straight_event_ids: List[str] = []
    vt_box_event_ids: List[str] = []
    modes: set[str] = set()

    for event in events:
        match = _match_value(signal.value, signal.value_kind, event)
        if not match.get("matched_any"):
            continue
        event_id = _event_key(event)
        matched_event_ids.append(event_id)
        for mode in str(match.get("match_modes") or "").split("|"):
            if mode:
                modes.add(mode)
        if match.get("match_exact"):
            exact_event_ids.append(event_id)
        if match.get("match_box"):
            box_event_ids.append(event_id)
        if match.get("match_vtrac_straight"):
            vt_straight_event_ids.append(event_id)
        if match.get("match_vtrac_box"):
            vt_box_event_ids.append(event_id)

    best = ""
    for mode in ("EXACT", "BOX", "VTRAC_STRAIGHT", "VTRAC_BOX"):
        if mode in modes:
            best = mode
            break

    return {
        "matched_event_ids": _ordered_unique(matched_event_ids),
        "exact_event_ids": _ordered_unique(exact_event_ids),
        "box_event_ids": _ordered_unique(box_event_ids),
        "vt_straight_event_ids": _ordered_unique(vt_straight_event_ids),
        "vt_box_event_ids": _ordered_unique(vt_box_event_ids),
        "match_modes": "|".join(mode for mode in ("EXACT", "BOX", "VTRAC_STRAIGHT", "VTRAC_BOX") if mode in modes),
        "best_match_mode": best,
    }


def _lane_hit(match: Dict[str, Any], target_lane: str) -> bool:
    if target_lane == "straight":
        return bool(match["exact_event_ids"])
    if target_lane == "boxed":
        return bool(match["exact_event_ids"] or match["box_event_ids"])
    if target_lane == "vtrac":
        return bool(match["vt_straight_event_ids"] or match["vt_box_event_ids"])
    return bool(match["matched_event_ids"])


def _build_exposure_rows(
    *,
    window_root: Path,
    dates: Sequence[str],
    perf_rows: Sequence[Dict[str, str]],
    include_control_pack_combos: bool,
) -> Tuple[List[Dict[str, Any]], List[str], Dict[str, Any]]:
    warnings: List[str] = []
    rows: List[Dict[str, Any]] = []
    events_lookup = _events_by_state_day(perf_rows)
    scoreboard_rows = _load_scoreboard_rows(window_root, dates)
    seed_entries = _load_seed_entries(window_root, dates)

    signal_pools: Dict[Tuple[str, str, str, str, str, str], List[SignalValue]] = defaultdict(list)
    seed_count = 0
    for date, state_key, entry, seed in seed_entries:
        seed_count += 1
        scoreboard_row = scoreboard_rows.get((date, state_key)) or {}
        signals = list(_signals_from_seed(seed, scoreboard_row))
        full_control_signals, control_warnings = _augment_full_control_signals(
            seed,
            include_control_pack_combos=include_control_pack_combos,
        )
        signals.extend(full_control_signals)
        warnings.extend(f"{date}|{state_key}: {warning}" for warning in control_warnings)

        deduped: Dict[Tuple[str, str, str, str, str], SignalValue] = {}
        for signal in signals:
            text = str(signal.value or "").strip()
            if not text:
                continue
            key = (
                signal.source_family,
                signal.source_tool,
                signal.source_path,
                signal.value_kind,
                text,
            )
            deduped.setdefault(key, signal)
        for signal in deduped.values():
            pool_key = (
                date,
                state_key,
                signal.source_family,
                signal.source_tool,
                signal.source_path,
                signal.value_kind,
            )
            signal_pools[pool_key].append(signal)

    pool_sizes = {key: len(value) for key, value in signal_pools.items()}
    for pool_key, signals in signal_pools.items():
        date, state_key, source_family, source_tool, source_path, value_kind = pool_key
        state_day = _state_day_key(date, state_key)
        events = events_lookup.get(state_day) or []
        event_ids = [_event_key(event) for event in events]
        for signal in signals:
            target_lane = _infer_target_lane(signal)
            match = _best_match_for_signal(signal, events)
            lane_hit = _lane_hit(match, target_lane)
            exact_count = len(match["exact_event_ids"])
            box_count = len(match["box_event_ids"])
            vt_count = len(_ordered_unique(match["vt_straight_event_ids"] + match["vt_box_event_ids"]))
            rows.append(
                {
                    "date": date,
                    "state_key": state_key,
                    "state_day_key": state_day,
                    "source_family": source_family,
                    "source_tool": source_tool,
                    "source_key": f"{source_family}:{source_tool}",
                    "source_path": source_path,
                    "signal_value": signal.value,
                    "signal_value_kind": value_kind,
                    "signal_rank": signal.rank,
                    "raw_score": signal.raw_score,
                    "badge_or_alert": signal.badge_or_alert,
                    "support_count": signal.support_count,
                    "source_tags": signal.source_tags,
                    "promoted_stage": signal.promoted_stage,
                    "target_lane": target_lane,
                    "pool_size": pool_sizes[pool_key],
                    "same_day_winner_event_count": len(events),
                    "same_day_winner_event_ids": _join_ids(event_ids),
                    "matched_same_day_any": str(bool(match["matched_event_ids"])),
                    "matched_event_count": len(match["matched_event_ids"]),
                    "matched_event_ids": _join_ids(match["matched_event_ids"]),
                    "exact_event_count": exact_count,
                    "box_event_count": box_count,
                    "vtrac_event_count": vt_count,
                    "lane_hit": str(lane_hit),
                    "same_day_false_positive_proxy": str(not bool(match["matched_event_ids"])),
                    "best_match_mode": match["best_match_mode"],
                    "match_modes": match["match_modes"],
                    "board_rank": scoreboard_rows.get((date, state_key), {}).get("score_rank", ""),
                    "board_priority_score": scoreboard_rows.get((date, state_key), {}).get("priority_score", ""),
                    "board_tracker_posture": scoreboard_rows.get((date, state_key), {}).get("tracker_posture", ""),
                }
            )

    metadata = {
        "seed_state_days": seed_count,
        "signal_pool_count": len(signal_pools),
        "state_day_with_winners": len(events_lookup),
        "winner_events": sum(len(events) for events in events_lookup.values()),
        "include_control_pack_combos": include_control_pack_combos,
    }
    return rows, warnings, metadata


def _scorecard_rows(exposure_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    groups: Dict[Tuple[str, str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in exposure_rows:
        groups[
            (
                str(row.get("source_family") or ""),
                str(row.get("source_tool") or ""),
                str(row.get("signal_value_kind") or ""),
                str(row.get("target_lane") or ""),
            )
        ].append(row)

    out: List[Dict[str, Any]] = []
    for (family, tool, value_kind, target_lane), rows in groups.items():
        source_key = f"{family}:{tool}"
        source_paths = sorted({str(row.get("source_path") or "") for row in rows if row.get("source_path")})
        active_state_days = {str(row.get("state_day_key") or "") for row in rows if row.get("state_day_key")}
        pool_by_state_day: Dict[str, int] = {}
        winner_events_by_state_day: Dict[str, List[str]] = {}
        supported_event_ids: set[str] = set()
        for row in rows:
            state_day = str(row.get("state_day_key") or "")
            pool_by_state_day[state_day] = _safe_int(row.get("pool_size"))
            events = _split_ids(row.get("same_day_winner_event_ids"))
            if events:
                winner_events_by_state_day[state_day] = events
            for event_id in _split_ids(row.get("matched_event_ids")):
                if event_id:
                    supported_event_ids.add(event_id)
        total_winner_events = len({event for events in winner_events_by_state_day.values() for event in events})
        exposure_count = len(rows)
        matched_value_count = sum(1 for row in rows if _truthy(row.get("matched_same_day_any")))
        exact_value_count = sum(1 for row in rows if _safe_int(row.get("exact_event_count")) > 0)
        box_value_count = sum(1 for row in rows if _safe_int(row.get("box_event_count")) > 0)
        vt_value_count = sum(1 for row in rows if _safe_int(row.get("vtrac_event_count")) > 0)
        lane_value_count = sum(1 for row in rows if _truthy(row.get("lane_hit")))
        pool_sizes = [size for size in pool_by_state_day.values() if size]
        rough_space = _rough_space_size(value_kind, target_lane)
        rough_naive = _rate(total_winner_events, max(1, len(active_state_days) * rough_space))
        lane_rate = _rate(lane_value_count, exposure_count)
        lift = lane_rate / rough_naive if rough_naive else 0.0
        decision_payload = {
            "active_state_days": len(active_state_days),
            "avg_pool_size": _avg(pool_sizes),
            "lane_hit_value_rate": lane_rate,
            "winner_event_support_rate": _rate(len(supported_event_ids), total_winner_events),
            "rough_lift_vs_naive": lift,
            "target_lane": target_lane,
            "source_tool": tool,
        }
        decision, rationale = _decision_for_scorecard(decision_payload)
        out.append(
            {
                "source_family": family,
                "source_tool": tool,
                "source_key": source_key,
                "source_path": "|".join(source_paths[:8]),
                "source_path_count": len(source_paths),
                "signal_value_kind": value_kind,
                "target_lane": target_lane,
                "active_state_days": len(active_state_days),
                "total_winner_events_in_active_days": total_winner_events,
                "supported_winner_event_count": len(supported_event_ids),
                "winner_event_support_rate": _rate(len(supported_event_ids), total_winner_events),
                "total_exposure_values": exposure_count,
                "matched_same_day_value_count": matched_value_count,
                "same_day_value_match_rate": _rate(matched_value_count, exposure_count),
                "false_positive_proxy_value_count": exposure_count - matched_value_count,
                "false_positive_proxy_rate": _rate(exposure_count - matched_value_count, exposure_count),
                "exact_value_hit_count": exact_value_count,
                "box_value_hit_count": box_value_count,
                "vtrac_value_hit_count": vt_value_count,
                "lane_hit_value_count": lane_value_count,
                "lane_hit_value_rate": lane_rate,
                "avg_pool_size": _avg(pool_sizes),
                "median_pool_size": _median(pool_sizes),
                "max_pool_size": max(pool_sizes) if pool_sizes else 0,
                "unique_signal_values": len({str(row.get("signal_value") or "") for row in rows}),
                "rough_naive_space_size": rough_space,
                "rough_naive_value_rate": rough_naive,
                "rough_lift_vs_naive": lift,
                "stage2_decision": decision,
                "decision_rationale": rationale,
            }
        )
    out.sort(
        key=lambda row: (
            str(row["stage2_decision"]).startswith("denominator_only"),
            -_safe_float(row["rough_lift_vs_naive"]),
            -_safe_float(row["lane_hit_value_rate"]),
            _safe_float(row["avg_pool_size"]),
            str(row["source_key"]),
        )
    )
    return out


def _lane_panels(score_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    panels: List[Dict[str, Any]] = []
    for lane in ("straight", "boxed", "vtrac", "context"):
        scoped = [row for row in score_rows if row.get("target_lane") == lane]
        if not scoped:
            continue
        exposure = sum(_safe_int(row.get("total_exposure_values")) for row in scoped)
        lane_hits = sum(_safe_int(row.get("lane_hit_value_count")) for row in scoped)
        supported_events = len(
            {
                event
                for row in scoped
                for event in str(row.get("supported_event_ids") or "").split("|")
                if event
            }
        )
        decisions = Counter(str(row.get("stage2_decision") or "") for row in scoped)
        panels.append(
            {
                "lane": lane,
                "source_count": len(scoped),
                "total_exposure_values": exposure,
                "lane_hit_value_count": lane_hits,
                "lane_hit_value_rate": _rate(lane_hits, exposure),
                "avg_source_pool_size": _avg([int(round(_safe_float(row.get("avg_pool_size")))) for row in scoped]),
                "top_decisions": dict(decisions.most_common(8)),
                "note": "Supported-events field is intentionally omitted from lane panels because source rows can overlap heavily.",
                "supported_event_count_deprecated": supported_events,
            }
        )
    return panels


def _decision_matrix_rows(score_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in score_rows:
        decision = str(row.get("stage2_decision") or "")
        if decision in {"boxed_fixture_candidate", "straight_fixture_candidate"}:
            next_action = "promote_to_translator_fixture_review"
        elif "supporting_gate" in decision:
            next_action = "test_as_pairing_gate_not_standalone"
        elif decision.startswith("vtrac"):
            next_action = "keep_watch_decay_until_box_or_exact_pair"
        elif decision.startswith("denominator"):
            next_action = "keep_as_control_denominator"
        elif decision == "sample_too_small":
            next_action = "carry_forward_until_more_windows"
        else:
            next_action = "keep_context_or_negative_control"
        rows.append(
            {
                "source_key": row.get("source_key", ""),
                "target_lane": row.get("target_lane", ""),
                "active_state_days": row.get("active_state_days", ""),
                "avg_pool_size": row.get("avg_pool_size", ""),
                "lane_hit_value_rate": row.get("lane_hit_value_rate", ""),
                "winner_event_support_rate": row.get("winner_event_support_rate", ""),
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", ""),
                "rough_lift_vs_naive": row.get("rough_lift_vs_naive", ""),
                "stage2_decision": decision,
                "next_action": next_action,
                "rationale": row.get("decision_rationale", ""),
            }
        )
    return rows


def _fixture_candidates(
    priority_rows: Sequence[Dict[str, str]],
    attribution_rows: Sequence[Dict[str, str]],
    score_rows: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    decision_by_source = {str(row.get("source_key") or ""): str(row.get("stage2_decision") or "") for row in score_rows}
    event_sources: Dict[str, Counter[str]] = defaultdict(Counter)
    for row in attribution_rows:
        event_sources[_event_key(row)][_source_key(row)] += 1

    out: List[Dict[str, Any]] = []
    for row in priority_rows:
        event_id = _event_key(row)
        source_counts = event_sources.get(event_id) or Counter()
        fixture_sources = []
        supporting_sources = []
        watch_sources = []
        for source, _count in source_counts.most_common(12):
            decision = decision_by_source.get(source, "")
            if "fixture_candidate" in decision:
                fixture_sources.append(source)
            elif "supporting_gate" in decision:
                supporting_sources.append(source)
            elif "vtrac" in decision:
                watch_sources.append(source)
        outcome = str(row.get("outcome_class") or "")
        status = str(row.get("evidence_status") or "")
        if outcome in {"BOX_GAP", "EXACT_GAP"}:
            fixture_use = "translator_gap_teacher"
        elif status == "CAPTURED_AND_USED":
            fixture_use = "positive_regression_fixture"
        elif status == "CAPTURED_BUT_WRONG_LANE":
            fixture_use = "wrong_lane_restraint_fixture"
        elif status == "DECAY_VALIDATED":
            fixture_use = "decay_carryforward_fixture"
        else:
            fixture_use = "hypothesis_probe"
        out.append(
            {
                "priority": row.get("priority", ""),
                "fixture_use": fixture_use,
                "event_id": event_id,
                "date": row.get("date", ""),
                "state_key": row.get("state_key", ""),
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "outcome_class": outcome,
                "evidence_status": status,
                "board_rank": row.get("board_rank", ""),
                "sharp_signal_count": row.get("sharp_signal_count", ""),
                "territory_signal_count": row.get("territory_signal_count", ""),
                "stage2_fixture_sources": "|".join(fixture_sources),
                "stage2_supporting_sources": "|".join(supporting_sources),
                "stage2_watch_sources": "|".join(watch_sources),
                "top_attribution_sources": "|".join(source for source, _ in source_counts.most_common(10)),
                "recommended_next_review": (
                    "Compare this event against source exposure rows before changing weights; "
                    "use as a test case for translator routing."
                ),
            }
        )
    return out


def _bucket_counts(rows: Sequence[Dict[str, str]], field: str) -> Dict[str, int]:
    return dict(Counter(str(row.get(field) or "") for row in rows).most_common())


def _file_count(path: Path, *, kind: str) -> int:
    if not path.exists():
        return 0
    if kind == "csv":
        return len(_read_csv_rows(path))
    if kind == "json":
        data = _read_json(path)
        if isinstance(data, list):
            return len(data)
        if isinstance(data, dict):
            for key in ("rows", "cases", "priority_cases", "scorecard"):
                if isinstance(data.get(key), list):
                    return len(data[key])
        return 1
    return 1


def _build_baseline_ssot(
    *,
    window_root: Path,
    paths: Dict[str, Path],
    util_rows: Sequence[Dict[str, str]],
    attribution_rows: Sequence[Dict[str, str]],
    exposure_rows: Sequence[Dict[str, Any]],
    score_rows: Sequence[Dict[str, Any]],
    decision_rows: Sequence[Dict[str, Any]],
    fixture_rows: Sequence[Dict[str, Any]],
    pro_files: Sequence[Path],
) -> Tuple[str, Dict[str, Any]]:
    files = [
        ("performance_gap_ledger", paths["perf"], "csv", "headline"),
        ("evidence_utilization_ledger", paths["util"], "csv", "headline"),
        ("evidence_utilization_audit", paths["audit_json"], "json", "headline"),
        ("winner_signal_attribution_ledger", paths["attribution"], "csv", "teaching"),
        ("audit_interpretation_pass", paths["interpretation"], "json", "headline"),
        ("priority_cases", paths["priority_cases"], "csv", "teaching"),
        ("signal_decisions", paths["signal_decisions"], "csv", "teaching"),
        ("decay_scorecard", paths["decay_json"], "json", "diagnostic"),
        ("frontier_analysis", paths["frontier_json"], "json", "diagnostic"),
        ("stage2_signal_exposure_ledger", paths["exposure_csv"], "csv", "headline"),
        ("stage2_false_positive_scorecard", paths["scorecard_json"], "json", "headline"),
        ("stage2_promotion_decision_matrix", paths["decision_csv"], "csv", "teaching"),
        ("stage2_lane_sharpness_report", paths["lane_md"], "md", "diagnostic"),
        ("stage2_translator_fixture_candidates", paths["fixture_csv"], "csv", "teaching"),
        ("stage2_audit_interpretation", paths["stage2_json"], "json", "headline"),
    ]
    count_overrides = {
        paths["exposure_csv"]: len(exposure_rows),
        paths["scorecard_json"]: len(score_rows),
        paths["decision_csv"]: len(decision_rows),
        paths["fixture_csv"]: len(fixture_rows),
    }
    authoritative_files = [
        {
            "name": name,
            "path": safe_rel(path),
            "exists": path.exists(),
            "row_or_object_count": count_overrides.get(path, _file_count(path, kind=kind)),
            "metric_role": role,
        }
        for name, path, kind, role in files
    ]
    metric_map = [
        {
            "metric_layer": "Arena truth",
            "role": "headline",
            "read": "Measures whether Analysis Arena preserved winner territory/evidence.",
            "primary_files": "evidence_utilization_ledger; pure finalist scorecard; audit interpretation pass",
        },
        {
            "metric_layer": "Stage 2 exposure",
            "role": "headline",
            "read": "Measures denominator and false-positive proxy burden for signals before scoring changes.",
            "primary_files": "stage2_signal_exposure_ledger; stage2_false_positive_scorecard",
        },
        {
            "metric_layer": "Brain2 ranking",
            "role": "diagnostic",
            "read": "Evaluates rank/static-board behavior; should not be treated as pure Arena weakness.",
            "primary_files": "board scoreboards; Brain2 tracker ledgers; Stage 2 lane report",
        },
        {
            "metric_layer": "Old control-arm conversion",
            "role": "diagnostic",
            "read": "Grades how old CU/play-card infrastructure expressed Arena-era evidence.",
            "primary_files": "performance gap ledger; translator learning ledger",
        },
        {
            "metric_layer": "Translator opportunity",
            "role": "teaching-only",
            "read": "Finds gap/wrong-lane/decay fixtures; not a raw performance scoreboard.",
            "primary_files": "priority cases; case dossiers; Stage 2 fixture candidates",
        },
        {
            "metric_layer": "Decay/carryforward",
            "role": "diagnostic",
            "read": "Measures short-horizon resolution separately from same-day scoring.",
            "primary_files": "decay carryover scorecard and rows",
        },
    ]
    payload = {
        "schema_version": "analysis_arena_audit_baseline_ssot/v1",
        "window_root": safe_rel(window_root),
        "authoritative_files": authoritative_files,
        "counts": {
            "winner_events": len(util_rows),
            "winner_signal_attribution_rows": len(attribution_rows),
            "stage2_exposure_rows": len(exposure_rows),
            "stage2_scorecard_sources": len(score_rows),
            "evidence_status_counts": _bucket_counts(util_rows, "evidence_status"),
            "outcome_class_counts": _bucket_counts(util_rows, "outcome_class"),
        },
        "metric_map": metric_map,
        "pro_feedback_integrated": [safe_rel(path) for path in pro_files if path.exists()],
        "supersession_rule": (
            "Intermediate chat/log counts are superseded by the latest regenerated files listed in this SSOT."
        ),
        "guardrail": (
            "Stage 2 creates denominators and teaching labels. It does not authorize live scoring/budget changes by itself."
        ),
    }
    lines = [
        "# Analysis Arena Audit Baseline SSOT",
        "",
        "Purpose: freeze the authoritative March/window audit package before Stage 2 is used as a teaching baseline.",
        "",
        "## Authoritative Counts",
        "",
        f"- Winner events: `{len(util_rows)}`",
        f"- Winner signal attribution rows: `{len(attribution_rows)}`",
        f"- Stage 2 exposure rows: `{len(exposure_rows)}`",
        f"- Stage 2 scorecard source rows: `{len(score_rows)}`",
        "",
        "Evidence status counts:",
    ]
    for key, count in payload["counts"]["evidence_status_counts"].items():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "Outcome class counts:"])
    for key, count in payload["counts"]["outcome_class_counts"].items():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Metric Map", ""])
    for item in metric_map:
        lines.append(f"- `{item['metric_layer']}` [{item['role']}]: {item['read']}")
    lines.extend(["", "## Authoritative Files", ""])
    for item in authoritative_files:
        exists = "yes" if item["exists"] else "no"
        lines.append(
            f"- `{item['name']}` [{item['metric_role']}]: `{item['path']}` exists=`{exists}` rows=`{item['row_or_object_count']}`"
        )
    lines.extend(
        [
            "",
            "## Supersession Rule",
            "",
            "- Intermediate conversation/log counts are not the SSOT. Use the regenerated files listed here.",
            "- Teaching-only metrics should not be read as raw system performance.",
            "- Stage 2 denominators are required before any new scoring or budget promotion.",
            "",
            "## PRO Feedback Integration",
            "",
        ]
    )
    for path in pro_files:
        if path.exists():
            lines.append(f"- Integrated governance/context from `{safe_rel(path)}`")
    lines.append("")
    return "\n".join(lines), payload


def _render_scorecard_md(score_rows: Sequence[Dict[str, Any]], metadata: Dict[str, Any]) -> str:
    decisions = Counter(str(row.get("stage2_decision") or "") for row in score_rows)
    lines = [
        "# Stage 2 Signal False-Positive Scorecard",
        "",
        "Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.",
        "",
        "Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.",
        "",
        "## Denominators",
        "",
        f"- Seed state-days audited: `{metadata.get('seed_state_days', 0)}`",
        f"- Winner events in audited state-days: `{metadata.get('winner_events', 0)}`",
        f"- Signal exposure rows: `{metadata.get('exposure_rows', 0)}`",
        f"- Source scorecard rows: `{len(score_rows)}`",
        f"- Signal pools: `{metadata.get('signal_pool_count', 0)}`",
        f"- Candidate-universe pack combos included: `{metadata.get('include_control_pack_combos', False)}`",
        "",
        "## Decision Mix",
        "",
    ]
    for decision, count in decisions.most_common():
        lines.append(f"- `{decision}`: `{count}`")
    lines.extend(["", "## Top Fixture/Support Candidates", ""])
    candidate_rows = [
        row
        for row in score_rows
        if str(row.get("stage2_decision") or "") in {"boxed_fixture_candidate", "straight_fixture_candidate", "boxed_supporting_gate", "straight_supporting_gate"}
    ][:20]
    for row in candidate_rows:
        lines.append(
            "- "
            f"`{row.get('source_key')}` lane=`{row.get('target_lane')}` "
            f"active=`{row.get('active_state_days')}` avg_pool=`{_safe_float(row.get('avg_pool_size')):.1f}` "
            f"lane_rate=`{_pct(_safe_float(row.get('lane_hit_value_rate')), 1)}` "
            f"lift=`{_safe_float(row.get('rough_lift_vs_naive')):.2f}` "
            f"decision=`{row.get('stage2_decision')}`"
        )
    lines.extend(["", "## Broad Control / Context Sources", ""])
    broad_rows = [
        row
        for row in score_rows
        if str(row.get("stage2_decision") or "").startswith("denominator")
        or str(row.get("stage2_decision") or "").endswith("context_only")
    ][:20]
    for row in broad_rows:
        lines.append(
            "- "
            f"`{row.get('source_key')}` lane=`{row.get('target_lane')}` "
            f"exposures=`{row.get('total_exposure_values')}` avg_pool=`{_safe_float(row.get('avg_pool_size')):.1f}` "
            f"false_proxy=`{_pct(_safe_float(row.get('false_positive_proxy_rate')), 1)}` "
            f"decision=`{row.get('stage2_decision')}`"
        )
    lines.extend(
        [
            "",
            "## Guardrail",
            "",
            "- This scorecard is a promotion filter, not a scoring rewrite.",
            "- A source can support a translator fixture without being safe as a standalone bet selector.",
            "- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_lane_md(lane_panels: Sequence[Dict[str, Any]], score_rows: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "# Stage 2 Lane Sharpness Report",
        "",
        "Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.",
        "",
        "## Lane Panels",
        "",
    ]
    for panel in lane_panels:
        lines.append(
            f"- `{panel['lane']}`: sources=`{panel['source_count']}`, "
            f"exposures=`{panel['total_exposure_values']}`, "
            f"lane_hit_rate=`{_pct(panel['lane_hit_value_count'], panel['total_exposure_values'])}`, "
            f"avg_source_pool=`{_safe_float(panel['avg_source_pool_size']):.1f}`"
        )
    lines.extend(["", "## Best Per-Lane Sources", ""])
    for lane in ("straight", "boxed", "vtrac"):
        scoped = [row for row in score_rows if row.get("target_lane") == lane]
        scoped.sort(
            key=lambda row: (
                -_safe_float(row.get("rough_lift_vs_naive")),
                -_safe_float(row.get("lane_hit_value_rate")),
                _safe_float(row.get("avg_pool_size")),
            )
        )
        lines.append(f"### {lane.title()}")
        if not scoped:
            lines.append("- No sources.")
            continue
        for row in scoped[:10]:
            lines.append(
                "- "
                f"`{row.get('source_key')}` decision=`{row.get('stage2_decision')}` "
                f"lane_rate=`{_pct(_safe_float(row.get('lane_hit_value_rate')), 1)}` "
                f"event_support=`{_pct(_safe_float(row.get('winner_event_support_rate')), 1)}` "
                f"avg_pool=`{_safe_float(row.get('avg_pool_size')):.1f}` "
                f"lift=`{_safe_float(row.get('rough_lift_vs_naive')):.2f}`"
            )
        lines.append("")
    return "\n".join(lines)


def _render_stage2_interpretation_md(
    *,
    metadata: Dict[str, Any],
    score_rows: Sequence[Dict[str, Any]],
    lane_panels: Sequence[Dict[str, Any]],
    fixture_rows: Sequence[Dict[str, Any]],
    warnings: Sequence[str],
) -> str:
    decision_counts = Counter(str(row.get("stage2_decision") or "") for row in score_rows)
    lines = [
        "# Stage 2 Audit Interpretation",
        "",
        "Purpose: interpret signal exposure denominators before scoring or translator promotion.",
        "",
        "## Executive Read",
        "",
        "- Stage 2 confirms the right next discipline: separate evidence visibility from exposure burden.",
        "- Broad control-arm and VTRAC signals can be valuable territory without being safe direct promotion signals.",
        "- Fixture candidates should now be reviewed against false-positive proxy burden before any weighting experiment.",
        "",
        "## Denominators",
        "",
        f"- Seed state-days audited: `{metadata.get('seed_state_days', 0)}`",
        f"- Winner events: `{metadata.get('winner_events', 0)}`",
        f"- Signal exposure rows: `{metadata.get('exposure_rows', 0)}`",
        f"- Scorecard source rows: `{len(score_rows)}`",
        f"- Translator fixture candidate rows: `{len(fixture_rows)}`",
        "",
        "## Decision Counts",
        "",
    ]
    for decision, count in decision_counts.most_common():
        lines.append(f"- `{decision}`: `{count}`")
    lines.extend(["", "## Lane Read", ""])
    for panel in lane_panels:
        lines.append(
            f"- `{panel['lane']}` lane: exposure rows `{panel['total_exposure_values']}`, "
            f"lane-hit rate `{_pct(panel['lane_hit_value_count'], panel['total_exposure_values'])}`."
        )
    lines.extend(
        [
            "",
            "## Recommended Next Actions",
            "",
            "1. Review `boxed_fixture_candidate` and `straight_fixture_candidate` sources against the 23 gap teachers.",
            "2. Keep `boxed_supporting_gate` and `straight_supporting_gate` as pair/gate candidates, not standalone weights.",
            "3. Keep VTRAC decisions in watch/decay mode until a boxed or exact source confirms the lane.",
            "4. Treat broad control-arm sources as denominator controls and negative-control surfaces.",
            "5. Run the same Stage 2 generator on older windows before locking any permanent scoring weights.",
            "",
            "## Warnings",
            "",
        ]
    )
    if warnings:
        for warning in warnings[:25]:
            lines.append(f"- `{warning}`")
        if len(warnings) > 25:
            lines.append(f"- Additional warnings omitted: `{len(warnings) - 25}`")
    else:
        lines.append("- No missing-control-artifact warnings.")
    lines.append("")
    return "\n".join(lines)


def _protocol_text() -> str:
    return """# Analysis Arena Post-Run Audit Protocol

Purpose: make post-window learning repeatable, so high-value findings are not left only in narrative chat or one-off reports.

## 1. Required Inputs

- Completed Analysis Arena window root under `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/`.
- Performance gap ledger.
- Hit roster.
- Translator learning ledger.
- C1/C2 frontier cases with non-zero case count.
- Decay carryover rows with tail coverage noted.
- Per-day board scoreboard JSON.
- Per-day translation sandbox seed manifest and seed JSONs.
- Stage 1 audit outputs before Stage 2 is run.
- Stage 2 outputs before Stage 2B is run.

## 2. Run Commands

```bash
python3 scripts/tools/create_window_evidence_utilization_audit.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_audit_interpretation_report.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_stage2_signal_exposure_audit.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_stage2b_signal_stack_analysis.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_stage2b_cross_window_stack_rollup.py --force
```

## 3. Required Outputs

- Evidence utilization ledger CSV.
- Evidence utilization audit Markdown/JSON.
- Winner signal attribution ledger CSV.
- Winner signal attribution scorecard Markdown.
- Case dossiers Markdown.
- Translator redesign lessons Markdown.
- Signal source dictionary Markdown.
- Audit interpretation pass Markdown/JSON.
- Audit interpretation priority cases CSV.
- Audit interpretation signal decisions CSV.
- Audit baseline SSOT Markdown/JSON.
- Stage 2 signal exposure ledger CSV.
- Stage 2 false-positive scorecard Markdown/JSON.
- Stage 2 signal promotion decision matrix CSV.
- Stage 2 lane sharpness report Markdown.
- Stage 2 translator fixture candidates CSV.
- Stage 2 audit interpretation Markdown/JSON.
- Stage 2 executive readout Markdown.
- Stage 2 source-family ranking CSV.
- Stage 2 denominator risk map CSV.
- Stage 2B signal pairing ledger CSV.
- Stage 2B signal stack scorecard Markdown/JSON.
- Stage 2B promotion candidates CSV.
- Stage 2B negative-control stacks CSV.
- Translator fixture deep review Markdown.
- Gap teacher stacks CSV.
- Wrong-lane restraint rules Markdown.
- Positive conversion regression set CSV.
- Decay carryforward teaching set CSV.
- Translator rule hypothesis queue Markdown/CSV.
- Stage 2 cross-window readiness Markdown.
- Stage 2B overnight work log Markdown.
- Stage 2B cross-window stack rollup Markdown/JSON.
- Stage 2B cross-window stack confirmation CSV.
- Stage 2B cross-window hypothesis confirmation CSV.
- Stage 2B cross-window source confirmation CSV.

## 4. Review Order

1. Confirm event count equals the window performance-gap denominator.
2. Confirm winner signal attribution has both pre-draw and post-result rows.
3. Review captured-but-underused and wrong-lane cases before judging final candidate quality.
4. Review box-gap and exact-gap dossiers as translator training examples.
5. Review source dictionary coverage before assuming an indicator was absent.
6. Run and review the audit interpretation pass before choosing future candidate/Brain scoring experiments.
7. Use interpretation priority cases as fixture candidates, not as immediate scoring weights.
8. Freeze the audit baseline SSOT before Stage 2 interpretation.
9. Review Stage 2 exposure denominators before promoting any signal.
10. Run Stage 2B stack analysis after Stage 2 denominators are frozen.
11. Review the executive readout, hypothesis queue, stack scorecard, and wrong-lane restraint rules before any translator experiment.
12. Backfill Stage 2 and Stage 2B onto older ready windows before treating any March-only stack as durable.
13. Run the cross-window stack rollup and separate candidates, support gates, VTRAC watch rows, negative controls, and low-denominator fixtures.
14. Use Stage 2 and Stage 2B decisions as experiment gates, not live scoring changes.

## 5. Interpretation Rules

- `CAPTURED_AND_USED` means evidence reached final conversion.
- `CAPTURED_BUT_UNDERUSED` means evidence existed but old final selection did not fully use it.
- `CAPTURED_BUT_WRONG_LANE` means territory/VTRAC support existed but boxed/straight conversion failed.
- `DECAY_VALIDATED` means same-day grading under-credits a signal that resolved inside the configured horizon.
- `BROAD_CONTEXT_ONLY` means a signal may be useful context but is not sharp enough alone.
- `NOT_CAPTURED` means no strong machine-readable evidence was found by current parser coverage.
- Audit interpretation counts are teaching-cohort labels. They do not replace raw performance totals.
- Stage 2 `false_positive_proxy` means an exposed value did not match a same-day winner in the completed window. It is a denominator, not final proof of uselessness.
- Stage 2B stack rows measure agreement between sources on the same state-day. They are translator hypotheses, not final master-score weights.
- Stage 2B pairing ledgers are exported as Git-safe drill-down rows; the full pair/state-day denominator count is retained in stack JSON metadata.
- Old candidate/play-card dominated stacks are useful controls and fixture material, but they are not proof that new Analysis Arena translation logic is already solved.
- Cross-window boxed translator candidates are replay candidates only. Low-denominator repeats must stay fixture/watch material even when their rate looks high.

## 6. Guardrails

- Do not redesign prediction/budget logic directly from winner-only attribution.
- Add false-positive exposure denominators before building a new master score.
- Keep bonus/fireball metrics separate from standard exact/box/VTRAC metrics.
- Keep Brain2 rank-static diagnostics active.
- Treat the interpretation pass as design guidance; scoring changes still require Stage-2 exposure/false-positive measurement.
- Treat Stage 2 promotion labels as candidate experiment gates until confirmed across more than one window.
- Treat Stage 2B hypothesis labels as replay targets until they pass bounded fixture tests and at least one cross-window confirmation.
- Do not promote broad VTRAC/context stacks without a bounded boxed or exact confirmation source.
- Do not rank by hit rate alone; require denominator size, event support, lane correctness, and cross-window behavior.
"""


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    final_docs_dir = _resolve_path(args.final_docs_dir)
    if not window_root.exists():
        raise SystemExit(f"Window root not found: {window_root}")
    paths = _default_paths(window_root, final_docs_dir)
    dates = iter_window_dates(window_root)
    if not dates:
        raise SystemExit(f"No per-day Analysis Arena scoreboards found in {window_root}")

    perf_rows = _read_csv_rows(paths["perf"])
    util_rows = _read_csv_rows(paths["util"])
    attribution_rows = _read_csv_rows(paths["attribution"])
    priority_rows = _read_csv_rows(paths["priority_cases"])
    pro_files = [_resolve_path(path) for path in args.pro_feedback] if args.pro_feedback else list(DEFAULT_PRO_FILES)

    exposure_rows, warnings, metadata = _build_exposure_rows(
        window_root=window_root,
        dates=dates,
        perf_rows=perf_rows,
        include_control_pack_combos=bool(args.include_control_pack_combos),
    )
    metadata["exposure_rows"] = len(exposure_rows)

    score_rows = _scorecard_rows(exposure_rows)
    lane_panels = _lane_panels(score_rows)
    decision_rows = _decision_matrix_rows(score_rows)
    fixture_rows = _fixture_candidates(priority_rows, attribution_rows, score_rows)

    ssot_md, ssot_json = _build_baseline_ssot(
        window_root=window_root,
        paths=paths,
        util_rows=util_rows,
        attribution_rows=attribution_rows,
        exposure_rows=exposure_rows,
        score_rows=score_rows,
        decision_rows=decision_rows,
        fixture_rows=fixture_rows,
        pro_files=pro_files,
    )
    scorecard_payload = {
        "schema_version": "analysis_arena_stage2_signal_exposure_scorecard/v1",
        "window_root": safe_rel(window_root),
        "metadata": metadata,
        "warnings": warnings,
        "scorecard": score_rows,
        "lane_panels": lane_panels,
        "decision_counts": dict(Counter(str(row.get("stage2_decision") or "") for row in score_rows).most_common()),
    }
    stage2_payload = {
        "schema_version": "analysis_arena_stage2_audit_interpretation/v1",
        "window_root": safe_rel(window_root),
        "metadata": metadata,
        "decision_counts": scorecard_payload["decision_counts"],
        "lane_panels": lane_panels,
        "recommended_next_actions": [
            "Review fixture candidates against the 23 gap teachers.",
            "Use supporting gates only in paired translator tests.",
            "Keep VTRAC broad territory in watch/decay mode until paired with box/exact evidence.",
            "Replicate Stage 2 on older windows before permanent scoring weights.",
        ],
        "warnings": warnings,
    }

    _write_csv(paths["exposure_csv"], exposure_rows, force=args.force)
    _write_json(paths["scorecard_json"], scorecard_payload, force=args.force)
    _write_text(paths["scorecard_md"], _render_scorecard_md(score_rows, metadata), force=args.force)
    _write_csv(paths["decision_csv"], decision_rows, force=args.force)
    _write_text(paths["lane_md"], _render_lane_md(lane_panels, score_rows), force=args.force)
    _write_csv(paths["fixture_csv"], fixture_rows, force=args.force)
    _write_json(paths["stage2_json"], stage2_payload, force=args.force)
    _write_text(
        paths["stage2_md"],
        _render_stage2_interpretation_md(
            metadata=metadata,
            score_rows=score_rows,
            lane_panels=lane_panels,
            fixture_rows=fixture_rows,
            warnings=warnings,
        ),
        force=args.force,
    )
    _write_json(paths["baseline_ssot_json"], ssot_json, force=args.force)
    _write_text(paths["baseline_ssot_md"], ssot_md, force=args.force)
    _write_text(paths["protocol_md"], _protocol_text(), force=True)

    print(f"wrote {safe_rel(paths['baseline_ssot_md'])}")
    print(f"wrote {safe_rel(paths['exposure_csv'])} rows={len(exposure_rows)}")
    print(f"wrote {safe_rel(paths['scorecard_md'])} sources={len(score_rows)}")
    print(f"wrote {safe_rel(paths['decision_csv'])} rows={len(decision_rows)}")
    print(f"wrote {safe_rel(paths['fixture_csv'])} rows={len(fixture_rows)}")
    print(f"wrote {safe_rel(paths['stage2_md'])}")
    if warnings:
        print(f"warnings={len(warnings)}")


if __name__ == "__main__":
    main()
