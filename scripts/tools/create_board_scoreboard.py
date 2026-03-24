#!/usr/bin/env python3
"""Create a compact Brain 2 board scoreboard from a board spillover overlay.

This is a reporting/consumer layer on top of the spillover overlay runtime
object. It does not re-score analyzers or recompute relationships. Its job is
to turn the overlay into a compact board table and handoff artifact.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _slugify(value: str) -> str:
    lowered = re.sub(r"[^a-zA-Z0-9]+", "_", str(value or "").strip()).strip("_").lower()
    return lowered or "board"


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _safe_rel(path: Path, repo_root: Path = REPO_ROOT) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _top_slice(values: Sequence[str], limit: int) -> List[str]:
    return [str(value) for value in list(values)[: max(0, int(limit))] if str(value).strip()]


def _tracker_posture(summary: Dict[str, Any]) -> str:
    ba_rows = summary.get("blackapple_statuses") if isinstance(summary.get("blackapple_statuses"), list) else []
    profit_rows = summary.get("top_profit_alerts") if isinstance(summary.get("top_profit_alerts"), list) else []
    due_rows = summary.get("due_double_families") if isinstance(summary.get("due_double_families"), list) else []
    compound_rows = summary.get("compound_events_top") if isinstance(summary.get("compound_events_top"), list) else []
    positional_notes = summary.get("positional_signal_notes") if isinstance(summary.get("positional_signal_notes"), list) else []

    ba_alert = any(str(row.get("status") or "").upper() == "ALERT" for row in ba_rows if isinstance(row, dict))
    ba_watch = any(str(row.get("status") or "").upper() == "WATCH" for row in ba_rows if isinstance(row, dict))
    profit_strong = any(_to_int(row.get("strength"), 0) >= 4 for row in profit_rows if isinstance(row, dict))
    due_active = any(_to_int(row.get("draws_since_double"), 0) > 0 for row in due_rows if isinstance(row, dict))
    compound_strong = any(
        _to_int(row.get("priority"), 0) >= 2 or _to_int(row.get("strength_max"), 0) >= 4
        for row in compound_rows
        if isinstance(row, dict)
    )
    positional_active = bool(positional_notes) or bool(summary.get("positional_shortlist_top"))

    if ba_alert and (profit_strong or compound_strong):
        return "tracker-rich"
    if ba_alert or compound_strong or (ba_watch and profit_strong):
        return "tracker-strong"
    if profit_strong or due_active or ba_watch or positional_active:
        return "tracker-support"
    return "tracker-light"


def _best_ba(summary: Dict[str, Any]) -> str:
    rows = summary.get("blackapple_statuses") if isinstance(summary.get("blackapple_statuses"), list) else []
    if not rows:
        return "-"
    ordered = sorted(
        [row for row in rows if isinstance(row, dict)],
        key=lambda row: (
            0 if str(row.get("status") or "").upper() == "ALERT" else 1 if str(row.get("status") or "").upper() == "WATCH" else 2,
            -_to_int(row.get("ba_score"), 0),
            str(row.get("variant") or ""),
        ),
    )
    top = ordered[0]
    return f"{top.get('variant')}:{top.get('status')}/{top.get('ba_score')}"


def _profit_alert_hint(summary: Dict[str, Any]) -> str:
    rows = summary.get("top_profit_alerts") if isinstance(summary.get("top_profit_alerts"), list) else []
    if not rows:
        return "-"
    top = next((row for row in rows if isinstance(row, dict)), None)
    if not isinstance(top, dict):
        return "-"
    canonical = str(top.get("canonical") or "")
    alert_id = str(top.get("alert_id") or "")
    badges = ",".join(str(badge) for badge in (top.get("badges") or [])[:2]) if isinstance(top.get("badges"), list) else ""
    decay_draws = _to_int(top.get("decay_draws"), 0)
    base = f"{alert_id}:{canonical}:{badges}".strip(":")
    return f"{base}:D{decay_draws}".strip(":") if decay_draws > 0 else base


def _due_double_hint(summary: Dict[str, Any]) -> str:
    rows = summary.get("due_double_families") if isinstance(summary.get("due_double_families"), list) else []
    if not rows:
        return "-"
    combined = next((row for row in rows if isinstance(row, dict) and str(row.get("variant") or "") == "Combined"), None)
    target = combined if isinstance(combined, dict) else next((row for row in rows if isinstance(row, dict)), None)
    if not isinstance(target, dict):
        return "-"
    families = target.get("families") if isinstance(target.get("families"), list) else []
    top_family = next((row for row in families if isinstance(row, dict)), None)
    if not isinstance(top_family, dict):
        return "-"
    return f"{target.get('variant')}:{top_family.get('family')}"


def _compound_event_hint(summary: Dict[str, Any]) -> str:
    rows = summary.get("compound_events_top") if isinstance(summary.get("compound_events_top"), list) else []
    top = next((row for row in rows if isinstance(row, dict)), None)
    if not isinstance(top, dict):
        return "-"
    return f"{top.get('variant')}:{top.get('top_event')}:P{_to_int(top.get('priority'), 0)}".strip(":")


def _positional_hint(summary: Dict[str, Any]) -> str:
    notes = summary.get("positional_signal_notes") if isinstance(summary.get("positional_signal_notes"), list) else []
    if notes:
        return str(notes[0])
    rows = summary.get("positional_shortlist_top") if isinstance(summary.get("positional_shortlist_top"), list) else []
    top = next((row for row in rows if isinstance(row, dict)), None)
    if not isinstance(top, dict):
        return "-"
    tags = ",".join(str(tag) for tag in (top.get("tags") or [])[:2] if str(tag))
    return f"{top.get('combo')}:{tags}".strip(":")


def _blackapple_reco_hint(summary: Dict[str, Any]) -> str:
    values = summary.get("blackapple_recommended_canonicals") if isinstance(summary.get("blackapple_recommended_canonicals"), list) else []
    return ",".join(str(value) for value in values[:3] if str(value).strip()) or "-"


def _survivor_hint(summary: Dict[str, Any]) -> str:
    regime = summary.get("state_regime") if isinstance(summary.get("state_regime"), dict) else {}
    if not regime:
        return "-"
    if not (
        bool(regime.get("survivor_pressure"))
        or bool(regime.get("last_remaining"))
        or bool(regime.get("hidden_terminal_support"))
    ):
        return "-"
    parts: List[str] = []
    if bool(regime.get("last_remaining")):
        parts.append(f"LR:{_to_int(regime.get('last_remaining_rows'), 0)}")
    if bool(regime.get("survivor_progression")):
        parts.append(f"Prog:{_to_int(regime.get('survivor_progression_count'), 0)}")
    if bool(regime.get("hidden_terminal_support")):
        parts.append("Hidden")
    profiles = summary.get("survivor_terminal_profiles") if isinstance(summary.get("survivor_terminal_profiles"), list) else []
    if profiles:
        parts.append(str(profiles[0]))
    return "|".join(parts) if parts else "Frontier"


def _context_signal_score(row: Dict[str, Any]) -> int:
    score = {"tracker-rich": 4, "tracker-strong": 3, "tracker-support": 2, "tracker-light": 0}.get(
        str(row.get("tracker_posture") or ""),
        0,
    )
    for key in ("profit_alert_hint", "compound_event_hint", "positional_hint", "due_double_hint"):
        if str(row.get(key) or "-") != "-":
            score += 1
    return score


def _targeting_bucket(row: Dict[str, Any]) -> str:
    role = str(row.get("role") or "")
    spent = str(row.get("spent_status") or "")
    if role == "clean_host":
        return "tight_core"
    if role == "shared_host" and spent == "mostly_unspent":
        return "tight_core"
    if role == "shared_host":
        return "small_shoulder"
    if role == "echo":
        return "echo_only"
    if role == "composite_interest":
        return "watch_only"
    return "deprioritize"


def build_board_scoreboard_payload(overlay: Dict[str, Any]) -> Dict[str, Any]:
    metadata = overlay.get("metadata") if isinstance(overlay.get("metadata"), dict) else {}
    board_summary = overlay.get("board_summary") if isinstance(overlay.get("board_summary"), dict) else {}
    summaries = overlay.get("state_summaries") if isinstance(overlay.get("state_summaries"), list) else []
    relationships = overlay.get("relationships") if isinstance(overlay.get("relationships"), list) else []

    summary_by_state = {
        str(row.get("state_key") or ""): row
        for row in summaries
        if isinstance(row, dict) and str(row.get("state_key") or "").strip()
    }

    scoreboard_rows = board_summary.get("board_scoreboard") if isinstance(board_summary.get("board_scoreboard"), list) else []
    compact_rows: List[Dict[str, Any]] = []
    for score_rank, row in enumerate(scoreboard_rows, start=1):
        if not isinstance(row, dict):
            continue
        state_key = str(row.get("state_key") or "")
        summary = summary_by_state.get(state_key, {})
        compact_rows.append(
            {
                "score_rank": score_rank,
                "state_key": state_key,
                "input_rank": _to_int(row.get("input_rank"), 0),
                "priority_score": _to_int(row.get("priority_score"), 0),
                "role": str(row.get("role") or ""),
                "spent_status": str(row.get("spent_status") or ""),
                "evening_bias": str(row.get("evening_bias") or ""),
                "targeting_bucket": _targeting_bucket(row),
                "tracker_posture": _tracker_posture(summary),
                "best_blackapple": _best_ba(summary),
                "blackapple_reco_hint": _blackapple_reco_hint(summary),
                "survivor_hint": _survivor_hint(summary),
                "profit_alert_hint": _profit_alert_hint(summary),
                "compound_event_hint": _compound_event_hint(summary),
                "positional_hint": _positional_hint(summary),
                "due_double_hint": _due_double_hint(summary),
                "top_canonicals": _top_slice(summary.get("dominant_canonicals") or [], 4),
                "top_vtrac_indices": _top_slice(summary.get("dominant_vtrac_indices") or [], 4),
                "overlap_score": _to_int(row.get("overlap_score"), 0),
                "primary_overlap_hits": _to_int(row.get("primary_overlap_hits"), 0),
                "direct_cross_hits": _to_int(row.get("direct_cross_hits"), 0),
            }
        )

    duplicate_pairs = board_summary.get("likely_duplicated_pairs") if isinstance(board_summary.get("likely_duplicated_pairs"), list) else []
    strongest_pairs = board_summary.get("strongest_overlap_pairs") if isinstance(board_summary.get("strongest_overlap_pairs"), list) else []
    direct_cross_rows = [
        row for row in relationships if isinstance(row, dict) and str(row.get("directness") or "") == "direct-cross-state"
    ]
    primary_targets = [row["state_key"] for row in compact_rows if row.get("targeting_bucket") == "tight_core"][:3]
    shoulder_states = [row["state_key"] for row in compact_rows if row.get("targeting_bucket") == "small_shoulder"][:3]
    watch_states = [row["state_key"] for row in compact_rows if row.get("targeting_bucket") in {"watch_only", "echo_only"}][:4]
    highest_priority_state = compact_rows[0]["state_key"] if compact_rows else None
    secondary_priority_state = compact_rows[1]["state_key"] if len(compact_rows) > 1 else None
    best_clean_host = primary_targets[0] if primary_targets else (shoulder_states[0] if shoulder_states else None)
    best_relationship_source = watch_states[0] if watch_states else None
    context_rich_rows = sorted(
        compact_rows,
        key=lambda row: (-_context_signal_score(row), -_to_int(row.get("priority_score"), 0), str(row.get("state_key") or "")),
    )
    highest_context_support_state = (
        context_rich_rows[0]["state_key"] if context_rich_rows and _context_signal_score(context_rich_rows[0]) > 0 else None
    )

    board_verdict = {
        "top_primary_target": highest_priority_state,
        "secondary_target": secondary_priority_state,
        "best_clean_host": best_clean_host,
        "best_relationship_source": best_relationship_source,
        "highest_context_support_state": highest_context_support_state,
        "tight_core_states": primary_targets,
        "small_shoulder_states": shoulder_states,
        "watch_only_states": watch_states,
        "highest_duplicate_pair": strongest_pairs[0] if strongest_pairs else None,
        "direct_cross_state_receipts": direct_cross_rows[:5],
    }

    return {
        "schema_version": "board_scoreboard_v0",
        "metadata": {
            "generated_from_overlay": metadata.get("board_name"),
            "results_date": metadata.get("results_date"),
            "profile": metadata.get("profile"),
            "experiment_tag": metadata.get("experiment_tag"),
            "overlay_results_path": metadata.get("midday_results_path"),
        },
        "scoreboard_rows": compact_rows,
        "duplicate_pairs": duplicate_pairs[:10],
        "strongest_overlap_pairs": strongest_pairs[:10],
        "board_verdict": board_verdict,
    }


def build_board_scoreboard_markdown(payload: Dict[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    rows = payload.get("scoreboard_rows") if isinstance(payload.get("scoreboard_rows"), list) else []
    board_verdict = payload.get("board_verdict") if isinstance(payload.get("board_verdict"), dict) else {}
    duplicate_pairs = payload.get("duplicate_pairs") if isinstance(payload.get("duplicate_pairs"), list) else []
    direct_cross_rows = board_verdict.get("direct_cross_state_receipts") if isinstance(board_verdict.get("direct_cross_state_receipts"), list) else []

    lines: List[str] = []
    lines.append(f"# Board Scoreboard — {metadata.get('generated_from_overlay') or 'Board'}")
    lines.append("")
    lines.append("Purpose: condense the spillover overlay into a compact Brain 2 targeting table and handoff view.")
    lines.append("")
    lines.append("## Scoreboard")
    lines.append("")
    lines.append("| Score Rank | State | Priority | Role | Targeting | Spent | Bias | Tracker | BA | BA Recos | Survivor | Profit Hint | Compound | Positional | Due-Doubles | Top Canonicals | Top VTRAC |")
    lines.append("|---:|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for row in rows:
        if not isinstance(row, dict):
            continue
        lines.append(
            f"| {row.get('score_rank')} | {row.get('state_key')} | {row.get('priority_score')} | {row.get('role')} | {row.get('targeting_bucket')} | {row.get('spent_status')} | {row.get('evening_bias')} | {row.get('tracker_posture')} | {row.get('best_blackapple')} | {row.get('blackapple_reco_hint')} | {row.get('survivor_hint')} | {row.get('profit_alert_hint')} | {row.get('compound_event_hint')} | {row.get('positional_hint')} | {row.get('due_double_hint')} | {', '.join(row.get('top_canonicals') or []) or '-'} | {', '.join(row.get('top_vtrac_indices') or []) or '-'} |"
        )

    if duplicate_pairs:
        lines.append("")
        lines.append("## Duplicate / Overlap Pressure")
        lines.append("")
        for row in duplicate_pairs[:8]:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"- `{row.get('state_a')} ↔ {row.get('state_b')}` score=`{row.get('pair_score')}` types=`{', '.join(row.get('relationship_types') or []) or '-'}`"
            )

    if direct_cross_rows:
        lines.append("")
        lines.append("## Direct Cross-State Receipts")
        lines.append("")
        for row in direct_cross_rows[:5]:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"- `{row.get('state_a')} -> {row.get('state_b')}` families=`{', '.join(row.get('canonical_families') or []) or '-'}` explanation=`{row.get('explanation') or ''}`"
            )

    lines.append("")
    lines.append("## Board Verdict")
    lines.append("")
    lines.append(f"- top_primary_target: `{board_verdict.get('top_primary_target') or '-'}`")
    lines.append(f"- secondary_target: `{board_verdict.get('secondary_target') or '-'}`")
    lines.append(f"- best_clean_host: `{board_verdict.get('best_clean_host') or '-'}`")
    lines.append(f"- best_relationship_source: `{board_verdict.get('best_relationship_source') or '-'}`")
    lines.append(f"- highest_context_support_state: `{board_verdict.get('highest_context_support_state') or '-'}`")
    lines.append(f"- tight_core_states: `{', '.join(board_verdict.get('tight_core_states') or []) or '-'}`")
    lines.append(f"- small_shoulder_states: `{', '.join(board_verdict.get('small_shoulder_states') or []) or '-'}`")
    lines.append(f"- watch_only_states: `{', '.join(board_verdict.get('watch_only_states') or []) or '-'}`")
    return "\n".join(lines).rstrip() + "\n"


def _write_csv(path: Path, rows: List[Dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "score_rank",
        "state_key",
        "input_rank",
        "priority_score",
        "role",
        "targeting_bucket",
        "spent_status",
        "evening_bias",
        "tracker_posture",
        "best_blackapple",
        "blackapple_reco_hint",
        "survivor_hint",
        "profit_alert_hint",
        "compound_event_hint",
        "positional_hint",
        "due_double_hint",
        "top_canonicals",
        "top_vtrac_indices",
        "overlap_score",
        "primary_overlap_hits",
        "direct_cross_hits",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            flat = dict(row)
            flat["top_canonicals"] = ",".join(flat.get("top_canonicals") or [])
            flat["top_vtrac_indices"] = ",".join(flat.get("top_vtrac_indices") or [])
            writer.writerow({key: flat.get(key, "") for key in fieldnames})
    return path


def write_board_scoreboard_files(
    *,
    out_md_path: Path,
    payload: Dict[str, Any],
    write_csv: bool = True,
    write_json: bool = True,
) -> Tuple[Path, Optional[Path], Optional[Path]]:
    out_md_path.parent.mkdir(parents=True, exist_ok=True)
    out_md_path.write_text(build_board_scoreboard_markdown(payload), encoding="utf-8")
    csv_path: Optional[Path] = None
    json_path: Optional[Path] = None
    if write_csv:
        csv_path = _write_csv(out_md_path.with_suffix(".csv"), payload.get("scoreboard_rows") or [])
    if write_json:
        json_path = out_md_path.with_suffix(".json")
        json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out_md_path, csv_path, json_path


def _default_out_name(overlay_metadata: Dict[str, Any]) -> str:
    date = str(overlay_metadata.get("results_date") or "unknown-date")
    board_name = str(overlay_metadata.get("generated_from_overlay") or overlay_metadata.get("board_name") or "board")
    return f"{date}__BOARD_SCOREBOARD__{_slugify(board_name)}.md"


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Create a compact board scoreboard from a board spillover overlay.")
    ap.add_argument("--overlay-json", required=True)
    ap.add_argument("--out-dir", default="docs/AAT9_KIT/FINAL VALIDATION/RUNS")
    args = ap.parse_args(argv)

    overlay_path = Path(args.overlay_json)
    if not overlay_path.is_absolute():
        overlay_path = (REPO_ROOT / overlay_path).resolve()
    if not overlay_path.exists():
        raise SystemExit(f"Overlay JSON not found: {overlay_path}")

    overlay = _read_json(overlay_path)
    if not isinstance(overlay, dict):
        raise SystemExit(f"Overlay payload is not a dict: {overlay_path}")

    payload = build_board_scoreboard_payload(overlay)
    payload["metadata"]["overlay_json"] = _safe_rel(overlay_path)

    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = (REPO_ROOT / out_dir).resolve()
    out_md = out_dir / _default_out_name(payload.get("metadata") or {})
    md_path, csv_path, json_path = write_board_scoreboard_files(out_md_path=out_md, payload=payload, write_csv=True, write_json=True)
    print(f"[ok] scoreboard -> {_safe_rel(md_path)}")
    if csv_path is not None:
        print(f"     csv -> {_safe_rel(csv_path)}")
    if json_path is not None:
        print(f"     json -> {_safe_rel(json_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
