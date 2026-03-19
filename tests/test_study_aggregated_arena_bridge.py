from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.study_aggregated_arena_bridge import build_bridge_rows, write_bridge_outputs


def _write_csv(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
            for row in rows:
                writer.writerow(row)


def test_bridge_study_measures_same_day_and_future_hits(tmp_path: Path) -> None:
    sharepacks_root = tmp_path / "sharepacks"
    day1 = sharepacks_root / "2026-01-01"
    state_dir = day1 / "StateA"
    analysis_dir = state_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)
    (day1 / "control_center").mkdir(parents=True, exist_ok=True)
    (day1 / "control_center" / "meta.json").write_text(
        json.dumps(
            {
                "states": [{"state_key": "StateA", "winners": {"Midday": "366", "Evening": "111"}}],
            }
        ),
        encoding="utf-8",
    )

    arena_path = analysis_dir / "aggregated_analysis_arena__tool_only__arena_v0.json"
    arena_path.write_text(
        json.dumps(
            {
                "arena_synthesis": {
                    "vtrac_literal_watchlist": [
                        {
                            "rank": 1,
                            "candidate_canonicals": ["447"],
                            "example_literals": ["474"],
                            "context_source_count": 1,
                        },
                        {
                            "rank": 2,
                            "candidate_canonicals": ["366"],
                            "example_literals": ["636"],
                            "context_source_count": 1,
                        },
                        {
                            "rank": 3,
                            "candidate_canonicals": ["447"],
                            "example_literals": ["474"],
                            "context_source_count": 1,
                        },
                    ]
                }
            }
        ),
        encoding="utf-8",
    )

    day2 = sharepacks_root / "2026-01-02"
    (day2 / "control_center").mkdir(parents=True, exist_ok=True)
    (day2 / "control_center" / "meta.json").write_text(
        json.dumps(
            {
                "states": [{"state_key": "StateA", "winners": {"Midday": "474", "Evening": "999"}}],
            }
        ),
        encoding="utf-8",
    )

    front_rows_csv = tmp_path / "front_rows.csv"
    _write_csv(
        front_rows_csv,
        [
            {
                "date": "2026-01-01",
                "state_key": "StateA",
                "outcome": "Midday",
                "winner": "366",
                "winner_canonical": "366",
                "gap_detail": "lane_alive_literal_missing_front3",
                "source_mix": "aux_overdue+aux_badge",
                "arena_vtrac_rank": "2",
                "arena_path": str(arena_path.relative_to(tmp_path)),
                "candidate_universe_box_present": "0",
                "candidate_universe_straight_present": "0",
                "play_card_box_present": "0",
                "play_card_straight_present": "0",
            }
        ],
    )

    rows = build_bridge_rows(
        front_rows_csv=front_rows_csv,
        sharepacks_root=sharepacks_root,
        cohort_mixes=["aux_overdue+aux_badge"],
        rules=["top1_perm", "top2_perm"],
        decay_days=3,
    )

    assert len(rows) == 2
    by_rule = {row["rule_name"]: row for row in rows}
    assert by_rule["top1_perm"]["same_day_box_hit"] == "0"
    assert by_rule["top1_perm"]["within_3d_box_hit"] == "1"
    assert by_rule["top1_perm"]["first_box_event"] == "2026-01-02 Midday 474"
    assert by_rule["top2_perm"]["same_day_box_hit"] == "1"
    assert by_rule["top2_perm"]["same_day_exact_hit"] == "1"

    out_rows = tmp_path / "bridge_rows.csv"
    out_summary = tmp_path / "bridge_summary.csv"
    out_md = tmp_path / "bridge.md"
    write_bridge_outputs(
        rows=rows,
        out_rows_csv=out_rows,
        out_summary_csv=out_summary,
        out_md=out_md,
        cohort_mixes=["aux_overdue+aux_badge"],
        rules=["top1_perm", "top2_perm"],
    )

    assert out_rows.exists()
    assert out_summary.exists()
    assert out_md.exists()
