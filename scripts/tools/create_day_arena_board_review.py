#!/usr/bin/env python3
"""Create a day-level Brain 1 -> Brain 2 review flow.

This script exists to harden the operational path between:
1. per-state aggregated analysis arenas (Brain 1)
2. board-level review bundle artifacts (Brain 2)

It intentionally stays orchestration-only. It does not redesign analyzers,
change selection policy, or replace the existing per-tool/runtime builders.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.build_aggregated_analysis_arena import (
    _default_out_name as _arena_default_out_name,
    _infer_history_date,
    _load_day_meta,
    _resolve_states,
    _safe_rel,
    build_aggregated_analysis_arena_payload,
    write_aggregated_analysis_arena_files,
)
from scripts.tools.create_board_review_bundle import (
    _bundle_out_name,
    build_board_review_bundle_payload,
    write_board_review_bundle_files,
)
from scripts.tools.build_board_spillover_overlay import (
    _default_out_name as _overlay_default_out_name,
    build_board_spillover_overlay_payload,
    write_board_spillover_overlay_files,
)
from scripts.tools.create_board_scoreboard import (
    _default_out_name as _scoreboard_default_out_name,
    build_board_scoreboard_payload,
    write_board_scoreboard_files,
)


def run_day_arena_board_review(
    *,
    sharepacks_root: Path,
    results_date: str,
    states: Sequence[str],
    profile: str,
    experiment_tag: str,
    history_date: Optional[str],
    board_name: str,
    midday_results_path: Optional[Path],
    arena_top_items: int,
    board_top_items: int,
    out_dir: Path,
    rebuild_arenas: bool = True,
) -> Dict[str, Any]:
    day_dir = sharepacks_root / results_date
    if not day_dir.exists():
        raise FileNotFoundError(f"Day directory not found: {day_dir}")

    day_meta = _load_day_meta(day_dir)
    resolved_history_date = _infer_history_date(day_dir, history_date)
    resolved_states = _resolve_states(day_dir, states, day_meta)
    if not resolved_states:
        raise ValueError(f"No states found under {day_dir}")

    built_arena_paths: List[Path] = []
    if rebuild_arenas:
        for state_key in resolved_states:
            state_dir = day_dir / state_key
            if not state_dir.exists():
                raise FileNotFoundError(f"State dir not found: {state_dir}")
            payload = build_aggregated_analysis_arena_payload(
                day_dir=day_dir,
                state_key=state_key,
                results_date=results_date,
                history_date=resolved_history_date,
                profile=profile,
                experiment_tag=experiment_tag,
                sharepacks_root=sharepacks_root,
                repo_root=REPO_ROOT,
                top_items=int(arena_top_items),
            )
            out_json = state_dir / "analysis" / _arena_default_out_name(profile, experiment_tag)
            arena_json, _ = write_aggregated_analysis_arena_files(
                out_json_path=out_json,
                payload=payload,
                write_md=True,
            )
            built_arena_paths.append(arena_json)

    overlay_payload = build_board_spillover_overlay_payload(
        day_dir=day_dir,
        results_date=results_date,
        states=resolved_states,
        profile=profile,
        experiment_tag=experiment_tag,
        board_name=board_name,
        sharepacks_root=sharepacks_root,
        repo_root=REPO_ROOT,
        midday_results_path=midday_results_path,
        top_items=int(board_top_items),
    )
    overlay_json = out_dir / _overlay_default_out_name(results_date, board_name)
    overlay_json_path, overlay_md_path = write_board_spillover_overlay_files(
        out_json_path=overlay_json,
        payload=overlay_payload,
        write_md=True,
    )

    scoreboard_payload = build_board_scoreboard_payload(overlay_payload)
    scoreboard_payload.setdefault("metadata", {})
    scoreboard_payload["metadata"]["overlay_json"] = _safe_rel(overlay_json_path)
    scoreboard_md = out_dir / _scoreboard_default_out_name(scoreboard_payload.get("metadata") or {})
    scoreboard_md_path, scoreboard_csv_path, scoreboard_json_path = write_board_scoreboard_files(
        out_md_path=scoreboard_md,
        payload=scoreboard_payload,
        write_csv=True,
        write_json=True,
    )

    bundle_payload = build_board_review_bundle_payload(
        results_date=results_date,
        board_name=board_name,
        overlay_payload=overlay_payload,
        scoreboard_payload=scoreboard_payload,
        overlay_json_path=overlay_json_path,
        overlay_md_path=overlay_md_path,
        scoreboard_md_path=scoreboard_md_path,
        scoreboard_csv_path=scoreboard_csv_path,
        scoreboard_json_path=scoreboard_json_path,
    )
    bundle_md = out_dir / _bundle_out_name(results_date, board_name)
    bundle_md_path, bundle_json_path = write_board_review_bundle_files(
        out_md_path=bundle_md,
        payload=bundle_payload,
        write_json=True,
    )

    return {
        "results_date": results_date,
        "states": resolved_states,
        "history_date": resolved_history_date,
        "rebuilt_arenas": rebuild_arenas,
        "arena_paths": [_safe_rel(path) for path in built_arena_paths],
        "overlay_json": _safe_rel(overlay_json_path),
        "overlay_md": _safe_rel(overlay_md_path) if overlay_md_path is not None else None,
        "scoreboard_md": _safe_rel(scoreboard_md_path),
        "scoreboard_csv": _safe_rel(scoreboard_csv_path) if scoreboard_csv_path is not None else None,
        "scoreboard_json": _safe_rel(scoreboard_json_path) if scoreboard_json_path is not None else None,
        "bundle_md": _safe_rel(bundle_md_path),
        "bundle_json": _safe_rel(bundle_json_path) if bundle_json_path is not None else None,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Create a day-level Brain 1 -> Brain 2 arena board review flow.")
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--date", required=True)
    ap.add_argument("--states", nargs="*", default=[])
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--history-date")
    ap.add_argument("--board-name", default="board")
    ap.add_argument("--midday-results")
    ap.add_argument("--arena-top-items", type=int, default=12)
    ap.add_argument("--board-top-items", type=int, default=8)
    ap.add_argument("--out-dir", default="docs/AAT9_KIT/FINAL VALIDATION/RUNS")
    ap.add_argument("--skip-arena-build", action="store_true")
    args = ap.parse_args(argv)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    midday_results_path = Path(args.midday_results).resolve() if args.midday_results else None
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = (REPO_ROOT / out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    receipt = run_day_arena_board_review(
        sharepacks_root=sharepacks_root,
        results_date=args.date,
        states=args.states,
        profile=args.profile,
        experiment_tag=args.experiment_tag,
        history_date=args.history_date,
        board_name=args.board_name,
        midday_results_path=midday_results_path,
        arena_top_items=int(args.arena_top_items),
        board_top_items=int(args.board_top_items),
        out_dir=out_dir,
        rebuild_arenas=not bool(args.skip_arena_build),
    )

    print(f"[ok] day board review -> {receipt['bundle_md']}")
    if receipt.get("rebuilt_arenas"):
        print(f"     rebuilt arenas: {len(receipt.get('arena_paths') or [])}")
    print(f"     overlay: {receipt['overlay_json']}")
    print(f"     scoreboard: {receipt['scoreboard_md']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
