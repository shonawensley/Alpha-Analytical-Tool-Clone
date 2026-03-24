#!/usr/bin/env python3
"""Create a one-step Brain 2 board review bundle.

This orchestrates the two current runtime Brain 2 artifacts:
1. board spillover overlay
2. board scoreboard

It then writes a compact manifest/summary so board review can run as a single
workflow instead of multiple manual script calls.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Dict, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.build_board_spillover_overlay import (
    _default_out_name as _overlay_default_out_name,
    _safe_rel,
    build_board_spillover_overlay_payload,
    write_board_spillover_overlay_files,
)
from scripts.tools.create_board_scoreboard import (
    _default_out_name as _scoreboard_default_out_name,
    build_board_scoreboard_payload,
    write_board_scoreboard_files,
)
from scripts.tools.build_shadow_decision_policy import (
    _default_out_name as _dpl_default_out_name,
    build_shadow_decision_policy_payload,
    write_shadow_decision_policy_files,
)


def _slugify(value: str) -> str:
    import re

    lowered = re.sub(r"[^a-zA-Z0-9]+", "_", str(value or "").strip()).strip("_").lower()
    return lowered or "board"


def build_board_review_bundle_payload(
    *,
    results_date: str,
    board_name: str,
    overlay_payload: Dict[str, Any],
    scoreboard_payload: Dict[str, Any],
    decision_policy_payload: Dict[str, Any],
    overlay_json_path: Path,
    overlay_md_path: Optional[Path],
    scoreboard_md_path: Path,
    scoreboard_csv_path: Optional[Path],
    scoreboard_json_path: Optional[Path],
    decision_policy_md_path: Path,
    decision_policy_json_path: Optional[Path],
) -> Dict[str, Any]:
    board_verdict = scoreboard_payload.get("board_verdict") if isinstance(scoreboard_payload.get("board_verdict"), dict) else {}
    scoreboard_rows = scoreboard_payload.get("scoreboard_rows") if isinstance(scoreboard_payload.get("scoreboard_rows"), list) else []
    duplicate_pairs = scoreboard_payload.get("duplicate_pairs") if isinstance(scoreboard_payload.get("duplicate_pairs"), list) else []
    direct_cross = board_verdict.get("direct_cross_state_receipts") if isinstance(board_verdict.get("direct_cross_state_receipts"), list) else []
    shadow_verdict = decision_policy_payload.get("shadow_verdict") if isinstance(decision_policy_payload.get("shadow_verdict"), dict) else {}
    state_decisions = decision_policy_payload.get("state_decisions") if isinstance(decision_policy_payload.get("state_decisions"), list) else []

    return {
        "schema_version": "board_review_bundle_v0",
        "metadata": {
            "results_date": results_date,
            "board_name": board_name,
        },
        "artifacts": {
            "overlay_json": _safe_rel(overlay_json_path),
            "overlay_md": _safe_rel(overlay_md_path) if overlay_md_path is not None else None,
            "scoreboard_md": _safe_rel(scoreboard_md_path),
            "scoreboard_csv": _safe_rel(scoreboard_csv_path) if scoreboard_csv_path is not None else None,
            "scoreboard_json": _safe_rel(scoreboard_json_path) if scoreboard_json_path is not None else None,
            "shadow_decision_policy_md": _safe_rel(decision_policy_md_path),
            "shadow_decision_policy_json": _safe_rel(decision_policy_json_path) if decision_policy_json_path is not None else None,
        },
        "board_verdict": board_verdict,
        "shadow_decision_policy": shadow_verdict,
        "highlights": {
            "top_scoreboard_rows": scoreboard_rows[:5],
            "duplicate_pairs": duplicate_pairs[:5],
            "direct_cross_state_receipts": direct_cross[:5],
            "top_decisions": state_decisions[:5],
        },
        "workflow_manifest": {
            "brain1_runtime_entrypoint": "scripts/tools/build_aggregated_analysis_arena.py",
            "brain2_runtime_entrypoint": "scripts/tools/create_board_review_bundle.py",
            "board_overlay_builder": "scripts/tools/build_board_spillover_overlay.py",
            "board_scoreboard_consumer": "scripts/tools/create_board_scoreboard.py",
            "shadow_decision_policy_builder": "scripts/tools/build_shadow_decision_policy.py",
            "next_step": "Use this bundle as the canonical board-level review receipt before any later combination-forming or UI display work.",
        },
        "source_refs": {
            "overlay_schema": overlay_payload.get("schema_version"),
            "scoreboard_schema": scoreboard_payload.get("schema_version"),
            "shadow_decision_policy_schema": decision_policy_payload.get("schema_version"),
        },
    }


def build_board_review_bundle_markdown(payload: Dict[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    artifacts = payload.get("artifacts") if isinstance(payload.get("artifacts"), dict) else {}
    board_verdict = payload.get("board_verdict") if isinstance(payload.get("board_verdict"), dict) else {}
    shadow_verdict = payload.get("shadow_decision_policy") if isinstance(payload.get("shadow_decision_policy"), dict) else {}
    highlights = payload.get("highlights") if isinstance(payload.get("highlights"), dict) else {}
    workflow_manifest = payload.get("workflow_manifest") if isinstance(payload.get("workflow_manifest"), dict) else {}

    lines = [
        f"# Board Review Bundle — {metadata.get('board_name') or 'Board'}",
        "",
        "Purpose: one-step Brain 2 board review bundle linking the runtime overlay and compact scoreboard.",
        "",
        "## Artifacts",
        "",
        f"- overlay_json: `{artifacts.get('overlay_json') or '-'}`",
        f"- overlay_md: `{artifacts.get('overlay_md') or '-'}`",
        f"- scoreboard_md: `{artifacts.get('scoreboard_md') or '-'}`",
        f"- scoreboard_csv: `{artifacts.get('scoreboard_csv') or '-'}`",
        f"- scoreboard_json: `{artifacts.get('scoreboard_json') or '-'}`",
        f"- shadow_decision_policy_md: `{artifacts.get('shadow_decision_policy_md') or '-'}`",
        f"- shadow_decision_policy_json: `{artifacts.get('shadow_decision_policy_json') or '-'}`",
        "",
        "## Workflow",
        "",
        f"- brain1_runtime_entrypoint: `{workflow_manifest.get('brain1_runtime_entrypoint') or '-'}`",
        f"- brain2_runtime_entrypoint: `{workflow_manifest.get('brain2_runtime_entrypoint') or '-'}`",
        f"- board_overlay_builder: `{workflow_manifest.get('board_overlay_builder') or '-'}`",
        f"- board_scoreboard_consumer: `{workflow_manifest.get('board_scoreboard_consumer') or '-'}`",
        f"- shadow_decision_policy_builder: `{workflow_manifest.get('shadow_decision_policy_builder') or '-'}`",
        f"- next_step: `{workflow_manifest.get('next_step') or '-'}`",
        "",
        "## Board Verdict",
        "",
        f"- top_primary_target: `{board_verdict.get('top_primary_target') or '-'}`",
        f"- secondary_target: `{board_verdict.get('secondary_target') or '-'}`",
        f"- best_clean_host: `{board_verdict.get('best_clean_host') or '-'}`",
        f"- best_relationship_source: `{board_verdict.get('best_relationship_source') or '-'}`",
        f"- highest_context_support_state: `{board_verdict.get('highest_context_support_state') or '-'}`",
        f"- tight_core_states: `{', '.join(board_verdict.get('tight_core_states') or []) or '-'}`",
        f"- small_shoulder_states: `{', '.join(board_verdict.get('small_shoulder_states') or []) or '-'}`",
        f"- watch_only_states: `{', '.join(board_verdict.get('watch_only_states') or []) or '-'}`",
        "",
        "## Shadow Decision Policy",
        "",
        f"- top_play_state: `{shadow_verdict.get('top_play_state') or '-'}`",
        f"- top_watch_state: `{shadow_verdict.get('top_watch_state') or '-'}`",
        f"- play_states: `{', '.join(shadow_verdict.get('play_states') or []) or '-'}`",
        f"- watch_states: `{', '.join(shadow_verdict.get('watch_states') or []) or '-'}`",
        f"- skip_states: `{', '.join(shadow_verdict.get('skip_states') or []) or '-'}`",
    ]

    top_rows = highlights.get("top_scoreboard_rows") if isinstance(highlights.get("top_scoreboard_rows"), list) else []
    if top_rows:
        lines.extend(["", "## Top Scoreboard Rows", "", "| Rank | State | Priority | Role | Targeting |", "|---:|---|---:|---|---|"])
        for row in top_rows:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"| {row.get('score_rank')} | {row.get('state_key')} | {row.get('priority_score')} | {row.get('role')} | {row.get('targeting_bucket')} |"
            )

    dupes = highlights.get("duplicate_pairs") if isinstance(highlights.get("duplicate_pairs"), list) else []
    if dupes:
        lines.extend(["", "## Duplicate Pairs", ""])
        for row in dupes:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"- `{row.get('state_a')} ↔ {row.get('state_b')}` score=`{row.get('pair_score')}` types=`{', '.join(row.get('relationship_types') or []) or '-'}`"
            )

    direct_cross = highlights.get("direct_cross_state_receipts") if isinstance(highlights.get("direct_cross_state_receipts"), list) else []
    if direct_cross:
        lines.extend(["", "## Direct Cross-State Receipts", ""])
        for row in direct_cross:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"- `{row.get('state_a')} -> {row.get('state_b')}` families=`{', '.join(row.get('canonical_families') or []) or '-'}`"
            )

    top_decisions = highlights.get("top_decisions") if isinstance(highlights.get("top_decisions"), list) else []
    if top_decisions:
        lines.extend(["", "## Top Shadow Decisions", "", "| Rank | State | Posture | Mode | Cap | Route |", "|---:|---|---|---|---|---|"])
        for row in top_decisions:
            if not isinstance(row, dict):
                continue
            lines.append(
                f"| {row.get('score_rank')} | {row.get('state_key')} | {row.get('posture')} | {row.get('mode')} | {row.get('cap_class')} | {row.get('translator_route')} |"
            )

    return "\n".join(lines).rstrip() + "\n"


def write_board_review_bundle_files(
    *,
    out_md_path: Path,
    payload: Dict[str, Any],
    write_json: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_md_path.parent.mkdir(parents=True, exist_ok=True)
    out_md_path.write_text(build_board_review_bundle_markdown(payload), encoding="utf-8")
    json_path: Optional[Path] = None
    if write_json:
        json_path = out_md_path.with_suffix(".json")
        json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out_md_path, json_path


def _bundle_out_name(results_date: str, board_name: str) -> str:
    return f"{results_date}__BOARD_REVIEW_BUNDLE__{_slugify(board_name)}.md"


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Create a one-step Brain 2 board review bundle.")
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--date", required=True)
    ap.add_argument("--states", nargs="+", required=True)
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--board-name", required=True)
    ap.add_argument("--midday-results")
    ap.add_argument("--top-items", type=int, default=8)
    ap.add_argument("--out-dir", default="docs/AAT9_KIT/FINAL VALIDATION/RUNS")
    args = ap.parse_args(argv)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Day directory not found: {day_dir}")

    midday_results_path = Path(args.midday_results).resolve() if args.midday_results else None
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = (REPO_ROOT / out_dir).resolve()

    overlay_payload = build_board_spillover_overlay_payload(
        day_dir=day_dir,
        results_date=args.date,
        states=args.states,
        profile=args.profile,
        experiment_tag=args.experiment_tag,
        board_name=args.board_name,
        sharepacks_root=sharepacks_root,
        repo_root=REPO_ROOT,
        midday_results_path=midday_results_path,
        top_items=int(args.top_items),
    )
    overlay_json = out_dir / _overlay_default_out_name(args.date, args.board_name)
    overlay_json_path, overlay_md_path = write_board_spillover_overlay_files(
        out_json_path=overlay_json,
        payload=overlay_payload,
        write_md=True,
    )

    scoreboard_payload = build_board_scoreboard_payload(overlay_payload)
    scoreboard_payload["metadata"]["overlay_json"] = _safe_rel(overlay_json_path)
    scoreboard_md = out_dir / _scoreboard_default_out_name(scoreboard_payload.get("metadata") or {})
    scoreboard_md_path, scoreboard_csv_path, scoreboard_json_path = write_board_scoreboard_files(
        out_md_path=scoreboard_md,
        payload=scoreboard_payload,
        write_csv=True,
        write_json=True,
    )

    decision_policy_payload = build_shadow_decision_policy_payload(
        overlay_payload=overlay_payload,
        scoreboard_payload=scoreboard_payload,
    )
    decision_md = out_dir / _dpl_default_out_name(args.date, args.board_name)
    decision_md_path, decision_json_path = write_shadow_decision_policy_files(
        out_md_path=decision_md,
        payload=decision_policy_payload,
        write_json=True,
    )

    bundle_payload = build_board_review_bundle_payload(
        results_date=args.date,
        board_name=args.board_name,
        overlay_payload=overlay_payload,
        scoreboard_payload=scoreboard_payload,
        decision_policy_payload=decision_policy_payload,
        overlay_json_path=overlay_json_path,
        overlay_md_path=overlay_md_path,
        scoreboard_md_path=scoreboard_md_path,
        scoreboard_csv_path=scoreboard_csv_path,
        scoreboard_json_path=scoreboard_json_path,
        decision_policy_md_path=decision_md_path,
        decision_policy_json_path=decision_json_path,
    )
    out_md = out_dir / _bundle_out_name(args.date, args.board_name)
    bundle_md_path, bundle_json_path = write_board_review_bundle_files(
        out_md_path=out_md,
        payload=bundle_payload,
        write_json=True,
    )

    print(f"[ok] bundle -> {_safe_rel(bundle_md_path)}")
    if bundle_json_path is not None:
        print(f"     json -> {_safe_rel(bundle_json_path)}")
    print(f"     overlay -> {_safe_rel(overlay_json_path)}")
    print(f"     scoreboard -> {_safe_rel(scoreboard_md_path)}")
    print(f"     shadow_dpl -> {_safe_rel(decision_md_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
