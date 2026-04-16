#!/usr/bin/env python3
"""Create normalized bonus-ball truth artifacts for one results date.

The core `data/results/<D>.txt` file remains authoritative for winners HTML and
all existing Pick 3 grading. This script reads the separate
`data/results_bonus/<D>.txt` sidecar, extracts only the supported active bonus
states, and accepts bonus digits only when the sidecar draw parity-matches the
core results draw for the same state and slot.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from alpha_analytical.control_center.bonus_ball_sidecar import (  # noqa: E402
    build_bonus_ball_truth_payload,
)


DEFAULT_RESULTS_ROOT = REPO_ROOT / "data" / "results"
DEFAULT_BONUS_RESULTS_ROOT = REPO_ROOT / "data" / "results_bonus"
DEFAULT_REPORTS_ROOT = REPO_ROOT / "reports" / "stable" / "bonus_ball_by_date"


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    rows = list(rows)
    fieldnames = [
        "results_date",
        "canonical",
        "project_state",
        "slot",
        "state_label_raw",
        "game_label_raw",
        "draw_date_raw",
        "core_draw",
        "sidecar_draw",
        "bonus_label_raw",
        "bonus_label_norm",
        "bonus_digit",
        "status",
        "reason",
        "accepted",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in fieldnames})


def _render_markdown(payload: dict[str, Any], *, json_path: Path, csv_path: Path) -> str:
    metadata = payload.get("metadata") or {}
    summary = payload.get("summary") or {}
    rows = list(payload.get("rows") or [])
    accepted = [row for row in rows if row.get("status") == "accepted"]
    rejected = [row for row in rows if row.get("status") == "rejected"]
    skipped = [row for row in rows if row.get("status") == "skipped"]

    lines: list[str] = [
        "# Bonus-Ball Parity Audit",
        "",
        "This companion lane does not modify or replace the authoritative Pick 3 results.",
        "A bonus row is accepted only when the structured sidecar draw parity-matches the core results draw.",
        "",
        "## Inputs",
        f"- Results date: `{metadata.get('results_date', '')}`",
        f"- Core results: `{metadata.get('core_results_path', '')}`",
        f"- Bonus results sidecar: `{metadata.get('bonus_results_path', '')}`",
        "",
        "## Summary",
        f"- Parsed rows: `{summary.get('rows_total', 0)}`",
        f"- Accepted rows: `{summary.get('accepted_rows', 0)}`",
        f"- Rejected rows: `{summary.get('rejected_rows', 0)}`",
        f"- Skipped rows: `{summary.get('skipped_rows', 0)}`",
        f"- Truth JSON: `{safe_rel(json_path)}`",
        f"- Truth CSV: `{safe_rel(csv_path)}`",
        "",
        "## Supported Bonus Labels Accepted",
    ]

    accepted_by_label = summary.get("accepted_by_bonus_label") or {}
    if accepted_by_label:
        for label, count in sorted(accepted_by_label.items()):
            lines.append(f"- `{label}`: `{count}`")
    else:
        lines.append("- none")

    lines += [
        "",
        "## State Coverage",
        "",
        "| State | Rows | Accepted | Rejected | Skipped |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in summary.get("rows_by_state") or []:
        lines.append(
            f"| `{row.get('project_state', '')}` | `{row.get('rows', 0)}` | `{row.get('accepted_rows', 0)}` | `{row.get('rejected_rows', 0)}` | `{row.get('skipped_rows', 0)}` |"
        )

    lines += [
        "",
        "## Accepted Rows",
        "",
        "| State | Slot | Draw | Bonus | Digit | Source Game |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    if accepted:
        for row in accepted:
            lines.append(
                f"| `{row.get('project_state', '')}` | `{row.get('slot', '')}` | `{row.get('core_draw', '')}` | `{row.get('bonus_label_raw', '')}` | `{row.get('bonus_digit', '')}` | `{row.get('game_label_raw', '')}` |"
            )
    else:
        lines.append("| none |  |  |  |  |  |")

    lines += [
        "",
        "## Rejected / Skipped Rows",
        "",
        "| State | Slot | Sidecar Draw | Core Draw | Status | Reason | Source Game |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    if rejected or skipped:
        for row in rejected + skipped:
            lines.append(
                f"| `{row.get('project_state', '')}` | `{row.get('slot', '') or ''}` | `{row.get('sidecar_draw', '') or ''}` | `{row.get('core_draw', '') or ''}` | `{row.get('status', '')}` | `{row.get('reason', '')}` | `{row.get('game_label_raw', '')}` |"
            )
    else:
        lines.append("| none |  |  |  |  |  |  |")

    lines += [
        "",
        "## Guardrails",
        "",
        "- Core `data/results` remains authoritative for winners HTML and all existing Pick 3 grading.",
        "- The sidecar only tracks supported active bonus-ball states.",
        "- The sidecar accepts bonus digits only when the underlying Pick 3 draw parity-matches the core results.",
        "- Bonus-ball truth is a separate research lane and is not yet mixed into standard straight / box metrics.",
        "",
    ]
    return "\n".join(lines)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create normalized bonus-ball truth artifacts for one results date.")
    parser.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD).")
    parser.add_argument("--results-root", default=str(DEFAULT_RESULTS_ROOT))
    parser.add_argument("--bonus-results-root", default=str(DEFAULT_BONUS_RESULTS_ROOT))
    parser.add_argument("--out-dir", default=None, help="Default: reports/stable/bonus_ball_by_date/<D>/")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    results_root = Path(args.results_root)
    bonus_results_root = Path(args.bonus_results_root)
    out_dir = Path(args.out_dir) if args.out_dir else DEFAULT_REPORTS_ROOT / args.date

    core_results_path = results_root / f"{args.date}.txt"
    bonus_results_path = bonus_results_root / f"{args.date}.txt"

    if not core_results_path.exists():
        raise SystemExit(f"Core results file not found: {core_results_path}")
    if not bonus_results_path.exists():
        raise SystemExit(f"Bonus results sidecar file not found: {bonus_results_path}")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / "bonus_ball_truth.json"
    out_csv = out_dir / "bonus_ball_truth.csv"
    out_md = out_dir / "bonus_ball_parity_audit.md"
    outputs = (out_json, out_csv, out_md)
    if not args.force and any(path.exists() for path in outputs):
        raise SystemExit("Output files already exist; pass --force to overwrite them.")

    payload = build_bonus_ball_truth_payload(
        results_date=args.date,
        core_results_text=_read_text(core_results_path),
        bonus_results_text=_read_text(bonus_results_path),
        core_results_path=safe_rel(core_results_path),
        bonus_results_path=safe_rel(bonus_results_path),
    )
    _write_json(out_json, payload)
    _write_csv(out_csv, payload.get("rows") or [])
    out_md.write_text(_render_markdown(payload, json_path=out_json, csv_path=out_csv), encoding="utf-8")


if __name__ == "__main__":
    main()
