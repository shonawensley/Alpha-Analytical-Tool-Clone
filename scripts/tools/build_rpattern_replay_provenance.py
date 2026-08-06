#!/usr/bin/env python3
"""Freeze provenance for the March 9 R-pattern repair replay."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SOURCE_ONLY_FILES = (
    "src/utils/extract_data.py",
    "src/utils/table_generator.py",
    "utils/extract_data.py",
    "utils/table_generator.py",
)

CURRENT_RUNTIME_FILES = (
    "modules/vtrac_straight_map.py",
    "scripts/tools/build_aggregated_analysis_arena.py",
    "scripts/tools/build_runs2_window_review_package.py",
    "scripts/tools/create_candidate_universe.py",
    "scripts/tools/export_control_center_sharepack.py",
    "scripts/tools/validate_profit_alerts_contract.py",
    *SOURCE_ONLY_FILES,
)

QUARANTINED_FILES = (
    "scripts/tools/cc_sanity_snapshot.py",
)

QUARANTINE_REASONS = {
    "scripts/tools/cc_sanity_snapshot.py": (
        "Excluded from accepted runtime provenance: the proposed vt_straight_hit "
        "check is self-referential and has not passed semantic acceptance."
    ),
}

CURRENT_ADDITIVE_FILES = (
    "scripts/tools/build_runs2_day_custom_hit_report.py",
    "scripts/tools/build_runs2_day_training_kits.py",
    "scripts/tools/compact_candidate_slates.py",
    "scripts/tools/create_analysis_arena_contract_audit.py",
    "scripts/tools/create_bounded_vtrac_closure_slate.py",
    "scripts/tools/create_merit_allocated_vtrac_cluster_slate.py",
    "scripts/tools/create_structural_convergence_anchor_slate.py",
    "scripts/tools/create_vtrac_corridor_arena_harness.py",
    "scripts/tools/create_vtrac_corridor_summary.py",
    "scripts/tools/grade_compact_candidate_slates.py",
    "scripts/tools/grade_merit_allocated_vtrac_cluster_slate.py",
    "scripts/tools/merit_allocated_vtrac_cluster_slates.py",
    "scripts/tools/rebuild_fixed_winner_reports.py",
)


def run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_record(path: Path, base: Path) -> dict[str, object]:
    return {
        "path": path.relative_to(base).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def tree_records(
    root: Path,
    relative_root: str,
    *,
    name_contains: str | None = None,
) -> list[dict[str, object]]:
    target = root / relative_root
    if not target.exists():
        return []
    records = []
    for path in sorted(p for p in target.rglob("*") if p.is_file()):
        if name_contains and name_contains not in path.name:
            continue
        records.append(file_record(path, root))
    return records


def aggregate_digest(records: Iterable[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for record in records:
        digest.update(str(record["path"]).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(record["sha256"]).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def snapshot_files(source_root: Path, files: Iterable[str], destination: Path) -> None:
    for relative in files:
        source = source_root / relative
        if not source.is_file():
            raise FileNotFoundError(f"Required snapshot file is missing: {source}")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def write_patch(root: Path, files: Iterable[str], destination: Path) -> None:
    patch = run_git(root, "diff", "--binary", "--", *files)
    destination.write_text(patch, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--source-worktree", type=Path, required=True)
    parser.add_argument("--current-worktree", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.repo_root.resolve()
    source_worktree = args.source_worktree.resolve()
    current_worktree = args.current_worktree.resolve()
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    inputs = [
        file_record(root / "data/history/Pick3StatsC4_2026-03-08.xlsm", root),
        file_record(root / "data/results/2026-03-09.txt", root),
    ]

    surfaces = {
        "old_predictive_sharepack": tree_records(
            root, "sharepacks/_predictive/2026-03-09"
        ),
        "old_winner_reports": tree_records(
            root, "reports/stable/winners_by_date/2026-03-09"
        ),
        "fixed_winner_reports": tree_records(
            root, "reports/stable/winners_by_date_fixed/2026-03-09"
        ),
        "old_analysis_arena_day_files": tree_records(
            root,
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/"
            "WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA",
            name_contains="2026-03-09",
        ),
    }

    lane_files = {
        "source_only": [
            file_record(source_worktree / relative, source_worktree)
            for relative in SOURCE_ONLY_FILES
        ],
        "current_runtime": [
            file_record(current_worktree / relative, current_worktree)
            for relative in CURRENT_RUNTIME_FILES
        ],
        "current_additive": [
            file_record(current_worktree / relative, current_worktree)
            for relative in CURRENT_ADDITIVE_FILES
        ],
        "excluded_quarantine": [
            {
                **file_record(current_worktree / relative, current_worktree),
                "status": "EXCLUDED_FROM_ACCEPTED_RUNTIME",
                "reason": QUARANTINE_REASONS[relative],
            }
            for relative in QUARANTINED_FILES
        ],
    }

    manifest = {
        "schema_version": "rpattern-replay-provenance-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": {
            "history_date": "2026-03-08",
            "results_date": "2026-03-09",
            "states": 14,
            "result_rows": 28,
            "repair": "Preserve variable-length R2/R4/R6/R8 strings.",
        },
        "main_worktree": {
            "head": run_git(root, "rev-parse", "HEAD").strip(),
            "branch": run_git(root, "branch", "--show-current").strip(),
        },
        "lanes": {
            "source_only": {
                "base_head": run_git(source_worktree, "rev-parse", "HEAD").strip(),
                "contract": "Original March 9 code plus only the four source-value fixes.",
            },
            "current": {
                "base_head": run_git(current_worktree, "rev-parse", "HEAD").strip(),
                "contract": (
                    "Current committed code plus the bounded runtime snapshot; additive "
                    "slate scripts remain separately identified."
                ),
            },
        },
        "inputs": inputs,
        "lane_files": lane_files,
        "surfaces": {
            name: {
                "file_count": len(records),
                "aggregate_sha256": aggregate_digest(records),
                "files": records,
            }
            for name, records in surfaces.items()
        },
    }

    (out_dir / "PROVENANCE_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "MAIN_WORKTREE_STATUS.txt").write_text(
        run_git(root, "status", "--short", "--branch", "--untracked-files=all"),
        encoding="utf-8",
    )
    write_patch(
        source_worktree,
        SOURCE_ONLY_FILES,
        out_dir / "SOURCE_ONLY_RUNTIME.patch",
    )
    write_patch(
        current_worktree,
        CURRENT_RUNTIME_FILES,
        out_dir / "CURRENT_RUNTIME.patch",
    )
    snapshot_files(
        source_worktree,
        SOURCE_ONLY_FILES,
        out_dir / "runtime_snapshot/source_only",
    )
    snapshot_files(
        current_worktree,
        (*CURRENT_RUNTIME_FILES, *CURRENT_ADDITIVE_FILES),
        out_dir / "runtime_snapshot/current",
    )

    summary_lines = [
        "# March 9 R-pattern Replay Provenance",
        "",
        "## Scope",
        "- History cutoff: `2026-03-08`",
        "- Result day: `2026-03-09`",
        "- Source-only base: "
        f"`{manifest['lanes']['source_only']['base_head']}`",
        f"- Current base: `{manifest['lanes']['current']['base_head']}`",
        "- Existing outputs are frozen inputs; replay outputs use new roots.",
        "",
        "## Input Hashes",
    ]
    summary_lines.extend(
        f"- `{record['path']}`: `{record['sha256']}`" for record in inputs
    )
    summary_lines.extend(["", "## Frozen Surfaces"])
    for name, surface in manifest["surfaces"].items():
        summary_lines.append(
            f"- `{name}`: {surface['file_count']} files, "
            f"aggregate `{surface['aggregate_sha256']}`"
        )
    summary_lines.extend(
        [
            "",
            "## Lane Boundary",
            "- `source_only`: exactly four modified source/table files.",
            "- `current_runtime`: bounded current runtime changes.",
            "- `current_additive`: optional analysis/slate utilities, not standard cadence.",
            "- `excluded_quarantine`: hashed for traceability only; not snapshotted, patched, or accepted as runtime.",
            "",
            "See `PROVENANCE_MANIFEST.json` for every file hash.",
        ]
    )
    (out_dir / "PROVENANCE_SUMMARY.md").write_text(
        "\n".join(summary_lines) + "\n",
        encoding="utf-8",
    )
    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
