#!/usr/bin/env python3
"""Build a single-day custom hit report from RUNS_2 review artifacts.

The report intentionally separates old control-arm coverage from Analysis Arena
diagnostic signals so review notes do not over-credit unfinished infrastructure.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    from modules.vtrac_reference import get_vtrac_index
except Exception:  # pragma: no cover - defensive fallback for doc generation.
    get_vtrac_index = None


PERIOD_ORDER = {"Midday": 0, "Evening": 1}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a per-day custom hit report for a RUNS_2 window."
    )
    parser.add_argument(
        "--window-root",
        type=Path,
        required=True,
        help="RUNS_2 window root, for example WINDOW_2026-03-09_to_2026-03-23.",
    )
    parser.add_argument("--date", default="2026-03-09")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional output markdown path. Defaults under TRAINING_KITS.",
    )
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8-sig"))


def safe_int(value: Any, default: int = 0) -> int:
    try:
        if value in (None, ""):
            return default
        return int(float(str(value)))
    except (TypeError, ValueError):
        return default


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, ""):
            return default
        return float(str(value))
    except (TypeError, ValueError):
        return default


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y", "hit"}


def clean(value: Any, default: str = "-") -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text if text else default


def md_escape(value: Any) -> str:
    text = clean(value)
    text = text.replace("\n", "; ")
    text = text.replace("|", r"\|")
    return text


def render_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "_No rows found._"
    lines = [
        "| " + " | ".join(md_escape(header) for header in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_escape(cell) for cell in row) + " |")
    return "\n".join(lines)


def details(summary: str, body: str) -> str:
    return f"<details>\n<summary>{md_escape(summary)}</summary>\n\n{body}\n\n</details>"


def event_id(row: dict[str, str]) -> str:
    return f"{row.get('date')}|{row.get('state_key')}|{row.get('period')}|{row.get('winner')}"


def period_hit_field(period: str) -> str:
    return f"{period} Hits"


def canonicalize(combo: Any) -> str:
    digits = "".join(ch for ch in str(combo or "") if ch.isdigit())
    if not digits:
        return ""
    return "".join(sorted(digits.zfill(3)[-3:]))


def normalize_combo(combo: Any) -> str:
    digits = "".join(ch for ch in str(combo or "") if ch.isdigit())
    return digits.zfill(3)[-3:] if digits else ""


def vtrac_value(combo_or_canonical: Any) -> str:
    if get_vtrac_index is None:
        return ""
    try:
        value = get_vtrac_index(str(combo_or_canonical).zfill(3)[-3:])
    except Exception:
        return ""
    return str(value) if value is not None else ""


def split_values(value: Any) -> list[str]:
    text = clean(value, "")
    if not text or text == "-":
        return []
    for sep in (";", ","):
        if sep in text:
            return [part.strip() for part in text.split(sep) if part.strip()]
    return [text]


def rel_link(from_file: Path, target: Path, label: str | None = None) -> str:
    if not target.exists():
        return clean(label or target.name)
    rel = (
        Path(os.path.relpath(target.resolve(), from_file.parent.resolve()))
        if target.is_absolute()
        else target
    )
    encoded = quote(str(rel).replace("\\", "/"), safe="/.-_~#")
    return f"[{md_escape(label or target.name)}]({encoded})"


def rel_path(from_file: Path, target: Path) -> Path:
    try:
        return target.resolve().relative_to(from_file.parent.resolve())
    except ValueError:
        return Path(target.name)


def sort_events(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(
        rows,
        key=lambda row: (
            safe_int(row.get("board_rank"), 999),
            PERIOD_ORDER.get(row.get("period", ""), 9),
            row.get("state_key", ""),
            row.get("winner", ""),
        ),
    )


def bool_badge(value: Any) -> str:
    return "yes" if truthy(value) else "no"


def source_paths(window_root: Path, date: str) -> dict[str, Path]:
    runs_root = window_root.parents[1] / "RUNS"
    share_root = REPO_ROOT / "sharepacks" / "_predictive" / date
    bonus_root = REPO_ROOT / "reports" / "stable" / "bonus_ball_by_date" / date
    return {
        "hit_roster": window_root / f"{window_root.name}__ANALYSIS_ARENA__HIT_ROSTER.csv",
        "performance_gap": window_root
        / f"{window_root.name}__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv",
        "evidence_ledger": window_root
        / f"{window_root.name}__ANALYSIS_ARENA__EVIDENCE_UTILIZATION_LEDGER.csv",
        "winner_signal_attribution": window_root
        / f"{window_root.name}__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv",
        "stage2b_pairs": window_root
        / f"{window_root.name}__ANALYSIS_ARENA__STAGE2B_SIGNAL_PAIRING_LEDGER.csv",
        "positive_conversions": window_root
        / f"{window_root.name}__ANALYSIS_ARENA__POSITIVE_CONVERSION_REGRESSION_SET.csv",
        "decay_teaching": window_root
        / f"{window_root.name}__ANALYSIS_ARENA__DECAY_CARRYFORWARD_TEACHING_SET.csv",
        "scoreboard": window_root
        / "ANALYSIS_ARENA"
        / f"{date}__BOARD_SCOREBOARD__analysis_arena_day_review.csv",
        "spillover": window_root
        / "ANALYSIS_ARENA"
        / f"{date}__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json",
        "play_card_grade": runs_root / f"{date}__PLAY_CARD_GRADE__tool_only__arena_v0.csv",
        "control_blackapple": share_root / "control_center" / "blackapple_alerts.csv",
        "control_due_doubles": share_root / "control_center" / "due_doubles.csv",
        "control_profit_alerts": share_root / "control_center" / "profit_alerts.csv",
        "control_compound_events": share_root / "control_center" / "profit_compound_events.csv",
        "control_vtrac_repeat": share_root / "control_center" / "vtrac_repeat_watch.csv",
        "bonus_truth": bonus_root / "bonus_ball_truth.csv",
        "bonus_audit": bonus_root / "bonus_ball_parity_audit.md",
    }


class DayReportBuilder:
    def __init__(self, window_root: Path, date: str, out_file: Path):
        self.window_root = window_root.resolve()
        self.date = date
        self.out_file = out_file.resolve()
        self.paths = source_paths(self.window_root, self.date)
        self.share_root = REPO_ROOT / "sharepacks" / "_predictive" / self.date

        self.hit_rows = [
            row for row in read_csv(self.paths["hit_roster"]) if row.get("date") == self.date
        ]
        self.performance_rows = [
            row
            for row in read_csv(self.paths["performance_gap"])
            if row.get("date") == self.date
        ]
        self.evidence_rows = [
            row
            for row in read_csv(self.paths["evidence_ledger"])
            if row.get("date") == self.date
        ]
        self.signal_rows = [
            row
            for row in read_csv(self.paths["winner_signal_attribution"])
            if row.get("date") == self.date
        ]
        self.stage2b_rows = [
            row for row in read_csv(self.paths["stage2b_pairs"]) if row.get("date") == self.date
        ]
        self.positive_rows = [
            row
            for row in read_csv(self.paths["positive_conversions"])
            if row.get("date") == self.date
        ]
        self.decay_rows = [
            row for row in read_csv(self.paths["decay_teaching"]) if row.get("date") == self.date
        ]
        self.play_grade_rows = [
            row
            for row in read_csv(self.paths["play_card_grade"])
            if row.get("results_date") == self.date
        ]
        self.scoreboard_rows = read_csv(self.paths["scoreboard"])
        self.blackapple_rows = read_csv(self.paths["control_blackapple"])
        self.due_double_rows = read_csv(self.paths["control_due_doubles"])
        self.profit_alert_rows = read_csv(self.paths["control_profit_alerts"])
        self.compound_rows = read_csv(self.paths["control_compound_events"])
        self.vtrac_repeat_rows = read_csv(self.paths["control_vtrac_repeat"])
        self.bonus_rows = [
            row
            for row in read_csv(self.paths["bonus_truth"])
            if row.get("results_date") == self.date and truthy(row.get("accepted"))
        ]
        spillover_json = read_json(self.paths["spillover"]) or {}
        self.spillover_rows = spillover_json.get("relationships", [])

        self.hit_by_event = {event_id(row): row for row in self.hit_rows}
        self.evidence_by_event = {event_id(row): row for row in self.evidence_rows}
        self.performance_by_event = {event_id(row): row for row in self.performance_rows}
        self.decay_by_event = {event_id(row): row for row in self.decay_rows}
        self.positive_by_event = {event_id(row): row for row in self.positive_rows}

        self.signal_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.signal_rows:
            self.signal_by_event[clean(row.get("event_id"), "")].append(row)

        self.stage2b_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.stage2b_rows:
            for match_event_id in split_values(row.get("matched_event_ids")):
                self.stage2b_by_event[match_event_id].append(row)

        self.play_grade_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.play_grade_rows:
            state_key = clean(row.get("state_key"), "")
            period = clean(row.get("winner_label"), "")
            winner = clean(row.get("winner"), "")
            self.play_grade_by_event[f"{self.date}|{state_key}|{period}|{winner}"].append(row)

        self.cu_cache: dict[str, dict[str, Any]] = {}
        self.play_card_cache: dict[str, dict[str, Any]] = {}
        self.sandbox_cache: dict[str, dict[str, Any]] = {}

    def build(self) -> str:
        all_events = sort_events(self.performance_rows)
        hit_events = sort_events(self.hit_rows)
        lines: list[str] = [
            f"# {self.date} Custom Hit Report",
            "",
            "This report is a single-day performance reading surface. It joins the board ranking, "
            "old control-arm predictions, Analysis Arena diagnostics, aggregated trackers, decay "
            "fixtures, grouped spillover evidence, and bonus/fireball sidecar data into one file.",
            "",
            "**Reading rule:** control-arm catches are live prediction-stack evidence. Arena diagnostic "
            "catches are translator-learning evidence unless the source also appears in the old control "
            "arm. VTRAC-only territory is not treated as equivalent to straight or boxed conversion. "
            "Bonus/fireball rows are sidecar context, not standard Pick 3 credit unless an explicit "
            "prediction source used the bonus digit.",
            "",
            self.render_source_map(),
            "",
            self.render_executive_summary(all_events, hit_events),
            "",
            self.render_all_results_matrix(all_events),
            "",
            self.render_hit_summary(hit_events),
            "",
            self.render_tracker_conversion_tables(),
            "",
            self.render_grouped_pending_summary(hit_events),
            "",
            self.render_bonus_sidecar(),
            "",
            "# Event Cards",
            "",
        ]
        for row in hit_events:
            lines.append(self.render_event_card(row))
            lines.append("")
        lines.extend(
            [
                "# Review Notes",
                "",
                "- Use `Control-arm catch` rows to evaluate what the current playable stack already "
                "captured.",
                "- Use `Arena diagnostic catch` and `Arena + control-arm overlap` rows to identify "
                "translator, final-candidate, and budgeting rebuild evidence.",
                "- Use `Tracker-supported catch` rows to decide which aggregated alerts deserve "
                "stronger upstream weighting or clearer budget lanes.",
                "- Use `No credited hit` rows in the all-results matrix as the negative baseline for "
                "false-positive and missed-opportunity review.",
            ]
        )
        return "\n".join(lines).rstrip() + "\n"

    def render_source_map(self) -> str:
        rows = []
        labels = [
            ("Hit roster", "hit_roster"),
            ("All-result performance ledger", "performance_gap"),
            ("Evidence utilization ledger", "evidence_ledger"),
            ("Winner signal attribution ledger", "winner_signal_attribution"),
            ("Stage 2B signal pairing ledger", "stage2b_pairs"),
            ("Positive conversion regression set", "positive_conversions"),
            ("Decay carryforward teaching set", "decay_teaching"),
            ("Board scoreboard", "scoreboard"),
            ("Board spillover overlay", "spillover"),
            ("Play Card grade", "play_card_grade"),
            ("Blackapple alerts", "control_blackapple"),
            ("Due doubles", "control_due_doubles"),
            ("Profit alerts", "control_profit_alerts"),
            ("Compound events", "control_compound_events"),
            ("VTRAC repeat watch", "control_vtrac_repeat"),
            ("Bonus/fireball truth", "bonus_truth"),
        ]
        for label, key in labels:
            path = self.paths[key]
            rows.append([label, rel_link(self.out_file, path, path.name), "found" if path.exists() else "missing"])
        return "# Source Map\n\n" + render_table(["Source", "Path", "Status"], rows)

    def render_executive_summary(
        self, all_events: list[dict[str, str]], hit_events: list[dict[str, str]]
    ) -> str:
        hit_class_counts = Counter(clean(row.get("hit_class")) for row in hit_events)
        outcome_counts = Counter(
            clean(self.evidence_by_event.get(event_id(row), {}).get("outcome_class"))
            for row in all_events
        )
        rank_counts = Counter(self.rank_bucket(row) for row in hit_events)
        control_counts = Counter(self.control_label(row) for row in hit_events)
        arena_counts = Counter(self.arena_label(row) for row in hit_events)
        tracker_supported = sum(1 for row in hit_events if self.has_tracker_support(row))
        cu_exact = sum(1 for row in hit_events if truthy(row.get("cu_exact")))
        cu_box = sum(1 for row in hit_events if truthy(row.get("cu_box")))
        play_exact = sum(1 for row in hit_events if truthy(row.get("play_card_any_exact")))
        play_box = sum(1 for row in hit_events if truthy(row.get("play_card_any_box")))
        arena_exact = sum(
            1
            for row in hit_events
            if truthy(row.get("arena_exact_signal")) or truthy(row.get("sandbox_exact_seed"))
        )
        arena_box = sum(
            1
            for row in hit_events
            if truthy(row.get("arena_box_signal"))
            or truthy(row.get("arena_primary_box"))
            or truthy(row.get("sandbox_box_seed"))
        )
        arena_vt = sum(
            1
            for row in hit_events
            if truthy(row.get("arena_primary_vt")) or truthy(row.get("sandbox_vt_seed"))
        )

        rows = [
            ["Result events", len(all_events)],
            ["Credited / diagnostic hit rows", len(hit_events)],
            ["No-conversion events", max(len(all_events) - len(hit_events), 0)],
            ["Control-arm CU exact hits", cu_exact],
            ["Control-arm CU box hits", cu_box],
            ["Play Card exact hits", play_exact],
            ["Play Card box hits", play_box],
            ["Arena exact diagnostic catches", arena_exact],
            ["Arena box diagnostic catches", arena_box],
            ["Arena VTRAC diagnostic catches", arena_vt],
            ["Tracker-supported credited rows", tracker_supported],
            ["Bonus/fireball accepted rows", len(self.bonus_rows)],
        ]
        sections = [
            "# Executive Summary",
            "",
            render_table(["Metric", "Value"], rows),
            "",
            "## Hit Class Mix",
            "",
            render_table(["Class", "Count"], [[key, value] for key, value in hit_class_counts.items()]),
            "",
            "## Outcome Mix From Evidence Ledger",
            "",
            render_table(["Outcome", "Count"], [[key, value] for key, value in outcome_counts.items()]),
            "",
            "## Rank Mix For Credited Rows",
            "",
            render_table(["Rank bucket", "Count"], [[key, value] for key, value in rank_counts.items()]),
            "",
            "## Control-Arm Versus Arena Diagnostic Labels",
            "",
            render_table(["Control-arm label", "Count"], [[key, value] for key, value in control_counts.items()]),
            "",
            render_table(["Arena diagnostic label", "Count"], [[key, value] for key, value in arena_counts.items()]),
        ]
        return "\n".join(sections)

    def render_all_results_matrix(self, rows: list[dict[str, str]]) -> str:
        table_rows = []
        for row in rows:
            eid = event_id(row)
            hit = self.hit_by_event.get(eid, {})
            evidence = self.evidence_by_event.get(eid, {})
            base = hit or evidence or row
            bonus = self.bonus_for_event(row)
            credited = bool(hit)
            table_rows.append(
                [
                    clean(row.get("state_key")),
                    clean(row.get("period")),
                    clean(row.get("winner")),
                    clean(row.get("winner_canonical")),
                    clean(row.get("winner_vtrac_index")),
                    clean(row.get("board_rank")),
                    clean(evidence.get("outcome_class"), clean(hit.get("hit_class"), "No credited hit")),
                    self.combined_credit_label(base) if credited else "No credited hit",
                    self.control_label(base) if credited else "No old control-arm conversion",
                    self.arena_label(base) if credited else self.arena_status_for_no_credit(base),
                    self.tracker_summary(base),
                    self.decay_summary(row),
                    self.bonus_summary(bonus),
                ]
            )
        return "\n".join(
            [
                "# All-Results Matrix",
                "",
                "Every draw result for the day is listed here so the positive rows can be read against "
                "the missed-opportunity baseline.",
                "",
                render_table(
                    [
                        "State",
                        "Period",
                        "Winner",
                        "Canon",
                        "VT",
                        "Board rank",
                        "Outcome",
                        "Credit label",
                        "Control arm",
                        "Arena diagnostic",
                        "Trackers",
                        "Decay",
                        "Bonus sidecar",
                    ],
                    table_rows,
                ),
            ]
        )

    def render_hit_summary(self, hit_events: list[dict[str, str]]) -> str:
        rows = []
        for row in hit_events:
            eid = event_id(row)
            cu_matches = self.matched_cu_packs(row)
            play_matches = self.matched_play_rows(row)
            rows.append(
                [
                    clean(row.get("board_rank")),
                    clean(row.get("state_key")),
                    clean(row.get("period")),
                    clean(row.get("winner")),
                    clean(row.get("winner_canonical")),
                    clean(row.get("winner_vtrac_index")),
                    clean(row.get("hit_class")),
                    self.combined_credit_label(row),
                    self.list_size_summary(row, cu_matches, play_matches),
                    self.tracker_summary(row),
                    "yes" if eid in self.positive_by_event else "no",
                ]
            )
        return "\n".join(
            [
                "# Credited Hit Summary",
                "",
                render_table(
                    [
                        "Rank",
                        "State",
                        "Period",
                        "Winner",
                        "Canon",
                        "VT",
                        "Hit class",
                        "Credit label",
                        "Prediction-list coverage",
                        "Tracker support",
                        "Positive regression row",
                    ],
                    rows,
                ),
            ]
        )

    def render_tracker_conversion_tables(self) -> str:
        return "\n".join(
            [
                "# Aggregated Tracker Conversion Tables",
                "",
                "These are day-level control-center tracker readings. They are included separately "
                "from the event cards so tracker conversion can be reviewed as a macro layer.",
                "",
                "## Blackapple Alerts",
                "",
                self.render_blackapple_table(),
                "",
                "## Due Doubles",
                "",
                self.render_due_double_table(),
                "",
                "## Profit Alerts",
                "",
                self.render_profit_alert_table(),
                "",
                "## Compound Events",
                "",
                self.render_compound_table(),
                "",
                "## VTRAC Repeat Watch",
                "",
                self.render_vtrac_repeat_table(),
            ]
        )

    def render_blackapple_table(self) -> str:
        rows = [
            [
                row.get("StateKey"),
                row.get("Variant"),
                row.get("BA-Score"),
                row.get("Status"),
                row.get("#Candidates"),
                row.get("Examples"),
                row.get("Midday Hits"),
                row.get("Evening Hits"),
            ]
            for row in self.blackapple_rows
            if clean(row.get("Status")) not in {"-", "NONE"} or clean(row.get("Midday Hits")) != "-" or clean(row.get("Evening Hits")) != "-"
        ]
        return render_table(
            ["State", "Variant", "Score", "Status", "#Candidates", "Examples", "Midday Hits", "Evening Hits"],
            rows,
        )

    def render_due_double_table(self) -> str:
        ranked = sorted(
            self.due_double_rows,
            key=lambda row: -safe_int(row.get("Draws Since Double")),
        )
        rows = [
            [
                row.get("StateKey"),
                row.get("Variant"),
                row.get("Draws Since Double"),
                row.get("Family 1"),
                row.get("Family 2"),
                row.get("Family 3"),
                row.get("Midday Winner In Family"),
                row.get("Evening Winner In Family"),
            ]
            for row in ranked[:30]
        ]
        return render_table(
            [
                "State",
                "Variant",
                "Draws since double",
                "Family 1",
                "Family 2",
                "Family 3",
                "Midday family hit",
                "Evening family hit",
            ],
            rows,
        )

    def render_profit_alert_table(self) -> str:
        filtered = sorted(
            self.profit_alert_rows,
            key=lambda row: (
                -safe_float(row.get("Strength")),
                clean(row.get("StateKey")),
                clean(row.get("Variant")),
                clean(row.get("AlertId")),
            ),
        )[:40]
        rows = [
            [
                row.get("StateKey"),
                row.get("Variant"),
                row.get("AlertId"),
                row.get("Strength"),
                row.get("Suggested"),
                row.get("Badges"),
                row.get("Canonical"),
                row.get("ImpliedSet"),
                row.get("Midday Hits"),
                row.get("Evening Hits"),
            ]
            for row in filtered
        ]
        return render_table(
            [
                "State",
                "Variant",
                "Alert ID",
                "Strength",
                "Suggested",
                "Badges",
                "Canonical",
                "Implied set",
                "Midday Hits",
                "Evening Hits",
            ],
            rows,
        )

    def render_compound_table(self) -> str:
        rows = [
            [
                row.get("state_key"),
                row.get("variant"),
                row.get("top_event"),
                row.get("priority"),
                row.get("watchlist_tags"),
                row.get("candidate_alert_ids"),
                row.get("promoter_alert_ids"),
                row.get("merged_hits"),
                row.get("merged_hit_types"),
            ]
            for row in self.compound_rows
            if clean(row.get("merged_hits")) != "-"
        ]
        return render_table(
            [
                "State",
                "Variant",
                "Top event",
                "Priority",
                "Tags",
                "Candidate alert IDs",
                "Promoter alert IDs",
                "Merged hits",
                "Hit types",
            ],
            rows,
        )

    def render_vtrac_repeat_table(self) -> str:
        rows = [
            [
                row.get("StateKey"),
                row.get("Variant"),
                row.get("Current Index"),
                row.get("Current Streak"),
                row.get("Heat Index"),
                row.get("Winner"),
                row.get("Winner VTRAC"),
                row.get("Current==WinnerVTRAC"),
            ]
            for row in self.vtrac_repeat_rows
            if truthy(row.get("Current==WinnerVTRAC"))
        ]
        return render_table(
            [
                "State",
                "Variant",
                "Current VT",
                "Streak",
                "Heat",
                "Winner",
                "Winner VT",
                "Current==Winner",
            ],
            rows,
        )

    def render_grouped_pending_summary(self, hit_events: list[dict[str, str]]) -> str:
        hit_states = {row.get("state_key") for row in hit_events}
        rows = []
        for rel in self.spillover_rows:
            if rel.get("state_a") not in hit_states and rel.get("state_b") not in hit_states:
                continue
            rows.append(
                [
                    rel.get("state_a"),
                    rel.get("state_b"),
                    rel.get("relationship_type"),
                    rel.get("source_surface"),
                    rel.get("support_count"),
                    rel.get("canonical_families"),
                    rel.get("vtrac_indices"),
                    rel.get("explanation"),
                ]
            )
        rows = sorted(rows, key=lambda row: -safe_int(row[4]))[:30]
        return "\n".join(
            [
                "# Grouped / Universal Pending Summary",
                "",
                "This section uses the board spillover overlay to surface cross-state shared families, "
                "VTRAC territory, or alert-implied echoes connected to hit states. It is a review "
                "surface, not a live final-combination engine.",
                "",
                render_table(
                    [
                        "State A",
                        "State B",
                        "Relationship",
                        "Surface",
                        "Support",
                        "Shared canonicals",
                        "Shared VT",
                        "Explanation",
                    ],
                    rows,
                ),
            ]
        )

    def render_bonus_sidecar(self) -> str:
        rows = [
            [
                row.get("project_state"),
                row.get("slot"),
                row.get("core_draw"),
                row.get("bonus_label_raw"),
                row.get("bonus_digit"),
                row.get("status"),
                row.get("reason"),
            ]
            for row in self.bonus_rows
        ]
        return "\n".join(
            [
                "# Bonus / Fireball Sidecar",
                "",
                "These rows confirm the extra variable was parsed for states that publish it. They are "
                "kept outside standard hit credit unless a prediction source explicitly used the bonus "
                "digit.",
                "",
                render_table(
                    ["State", "Period", "Winner", "Bonus label", "Bonus digit", "Status", "Reason"],
                    rows,
                ),
            ]
        )

    def render_event_card(self, row: dict[str, str]) -> str:
        eid = event_id(row)
        evidence = self.evidence_by_event.get(eid, {})
        cu_matches = self.matched_cu_packs(row)
        play_matches = self.matched_play_rows(row)
        sandbox = self.sandbox_for_state(row.get("state_key", ""))
        signal_rows = self.top_signal_rows(eid)
        stack_rows = self.top_stage2b_rows(eid)
        spillover_rows = self.spillover_for_event(row)
        bonus = self.bonus_for_event(row)
        sections = [
            f"## Rank {clean(row.get('board_rank'))}: {clean(row.get('state_key'))} "
            f"{clean(row.get('period'))} {clean(row.get('winner'))}",
            "",
            self.render_event_core_table(row, evidence),
            "",
            "### Credit Split",
            "",
            render_table(
                ["Layer", "Label", "Evidence"],
                [
                    ["Combined", self.combined_credit_label(row), clean(row.get("credit_signature"))],
                    ["Control arm", self.control_label(row), self.control_evidence_summary(row, cu_matches, play_matches)],
                    ["Arena diagnostic", self.arena_label(row), self.arena_evidence_summary(row, sandbox)],
                    ["Trackers", "Tracker-supported catch" if self.has_tracker_support(row) else "No direct tracker support", self.tracker_summary(row)],
                    ["Decay", self.decay_summary(row), self.decay_detail(row)],
                    ["Bonus sidecar", self.bonus_summary(bonus), self.bonus_detail(bonus)],
                ],
            ),
            "",
            "### Prediction List Coverage",
            "",
            self.render_candidate_universe_section(row, cu_matches),
            "",
            self.render_play_card_section(row, play_matches),
            "",
            "### Arena Diagnostic Details",
            "",
            self.render_arena_diagnostic_section(row, sandbox),
            "",
            "### Aggregated Tracker Details",
            "",
            self.render_tracker_details(row),
            "",
            "### Winner Signal Attribution",
            "",
            self.render_signal_rows(signal_rows),
            "",
            "### Stack / Convergence Evidence",
            "",
            self.render_stage2b_rows(stack_rows),
            "",
            "### Grouped Pending / Spillover Context",
            "",
            self.render_spillover_rows(spillover_rows),
            "",
            "### Interpretation",
            "",
            self.interpretation(row, cu_matches, play_matches, sandbox),
        ]
        return "\n".join(sections)

    def render_event_core_table(self, row: dict[str, str], evidence: dict[str, str]) -> str:
        return render_table(
            ["Field", "Value"],
            [
                ["Event ID", event_id(row)],
                ["Winner", row.get("winner")],
                ["Canonical", row.get("winner_canonical")],
                ["VTRAC index", row.get("winner_vtrac_index")],
                ["Board rank", row.get("board_rank")],
                ["Priority score", row.get("board_priority_score")],
                ["Board role", row.get("board_role")],
                ["Board bucket", row.get("board_bucket")],
                ["Board tracker posture", row.get("board_tracker_posture")],
                ["Shadow posture", row.get("shadow_posture")],
                ["Shadow mode", row.get("shadow_mode")],
                ["Translator route", row.get("translator_route")],
                ["Hit class", row.get("hit_class")],
                ["Hit primary class", row.get("hit_primary_class")],
                ["Outcome class", evidence.get("outcome_class")],
                ["Evidence status", evidence.get("evidence_status")],
                ["Budget floor", row.get("budget_floor")],
                ["High conviction budget floor", row.get("high_conviction_budget_floor")],
                ["Reason codes", row.get("reason_codes")],
            ],
        )

    def render_candidate_universe_section(
        self, row: dict[str, str], matches: list[dict[str, Any]]
    ) -> str:
        state = clean(row.get("state_key"), "")
        cu = self.candidate_universe_for_state(state)
        cu_path = self.state_artifact_path(state, "candidate_universe__tool_only__arena_v0.json")
        union_count = clean(cu.get("union_combos_count")) if cu else "-"
        visible = matches[:12]
        table = render_table(
            ["Pack", "Method", "Variant", "Mode", "Combos", "Cost", "Match", "Prediction list"],
            [
                [
                    match.get("pack_id"),
                    match.get("method_id"),
                    match.get("variant"),
                    match.get("play_mode"),
                    match.get("combos_count"),
                    match.get("cost_units"),
                    match.get("match_mode"),
                    ", ".join(match.get("combos", [])[:80]),
                ]
                for match in visible
            ],
        )
        note = (
            f"Candidate Universe source: {rel_link(self.out_file, cu_path, cu_path.name)}. "
            f"Union list size: {union_count}. Matched packs: {len(matches)}."
        )
        if len(matches) > len(visible):
            all_rows = render_table(
                ["Pack", "Method", "Variant", "Mode", "Combos", "Cost", "Match"],
                [
                    [
                        match.get("pack_id"),
                        match.get("method_id"),
                        match.get("variant"),
                        match.get("play_mode"),
                        match.get("combos_count"),
                        match.get("cost_units"),
                        match.get("match_mode"),
                    ]
                    for match in matches
                ],
            )
            table += "\n\n" + details(f"All {len(matches)} matched Candidate Universe packs", all_rows)
        return note + "\n\n" + table

    def render_play_card_section(
        self, row: dict[str, str], matches: list[dict[str, str]]
    ) -> str:
        state = clean(row.get("state_key"), "")
        play_path = self.state_artifact_path(state, "play_card__tool_only__arena_v0.json")
        sorted_matches = sorted(matches, key=self.play_match_sort_key)
        visible = sorted_matches[:16]
        rows = []
        for match in visible:
            combos = self.play_card_combos_for_grade_row(state, match)
            rows.append(
                [
                    match.get("strategy"),
                    match.get("budget_label"),
                    match.get("combos_count"),
                    match.get("boxed_canonicals_count"),
                    self.play_match_mode(match),
                    ", ".join(combos[:80]),
                ]
            )
        table = render_table(
            ["Strategy", "Budget", "Combos", "Boxed canonicals", "Match", "Prediction list"],
            rows,
        )
        note = (
            f"Play Card source: {rel_link(self.out_file, play_path, play_path.name)}. "
            f"Matched grade rows: {len(matches)}."
        )
        if len(sorted_matches) > len(visible):
            all_rows = render_table(
                ["Strategy", "Budget", "Combos", "Boxed canonicals", "Match"],
                [
                    [
                        match.get("strategy"),
                        match.get("budget_label"),
                        match.get("combos_count"),
                        match.get("boxed_canonicals_count"),
                        self.play_match_mode(match),
                    ]
                    for match in sorted_matches
                ],
            )
            table += "\n\n" + details(f"All {len(sorted_matches)} matched Play Card grade rows", all_rows)
        return note + "\n\n" + table

    def render_arena_diagnostic_section(self, row: dict[str, str], sandbox: dict[str, Any]) -> str:
        seeds = sandbox.get("sandbox_hypotheses", {})
        if isinstance(seeds, list):
            grouped: dict[str, list[Any]] = defaultdict(list)
            for item in seeds:
                grouped[clean(item.get("kind"), "unknown")].append(item.get("value"))
            seeds = grouped
        box_seed = self.seed_values(seeds, "diagnostic_boxed_seed")
        exact_seed = self.seed_values(seeds, "diagnostic_straight_seed")
        vt_seed = self.seed_values(seeds, "diagnostic_vt_box_seed")
        shadow_policy = sandbox.get("shadow_decision_policy", {})
        rows = [
            ["Arena box signal", bool_badge(row.get("arena_box_signal"))],
            ["Arena exact signal", bool_badge(row.get("arena_exact_signal"))],
            ["Arena primary box", bool_badge(row.get("arena_primary_box"))],
            ["Arena primary VTRAC", bool_badge(row.get("arena_primary_vt"))],
            ["Sandbox boxed seed", bool_badge(row.get("sandbox_box_seed"))],
            ["Sandbox exact seed", bool_badge(row.get("sandbox_exact_seed"))],
            ["Sandbox VTRAC seed", bool_badge(row.get("sandbox_vt_seed"))],
            ["Preserved not budgeted", bool_badge(row.get("preserved_not_budgeted"))],
            ["Arena final candidate signature score", row.get("arena_final_candidate_signature_score")],
            ["Arena final candidate signature", row.get("arena_final_candidate_signature")],
            ["Top primary target", row.get("top_primary_target")],
            ["Secondary target", row.get("secondary_target")],
            ["Best clean host", row.get("best_clean_host")],
            ["Highest context support state", row.get("highest_context_support_state")],
            ["Shadow policy", json.dumps(shadow_policy, ensure_ascii=True)[:600]],
            ["Diagnostic boxed seed list", ", ".join(box_seed)],
            ["Diagnostic straight seed list", ", ".join(exact_seed)],
            ["Diagnostic VTRAC seed list", ", ".join(vt_seed)],
        ]
        return render_table(["Diagnostic field", "Value"], rows)

    def render_tracker_details(self, row: dict[str, str]) -> str:
        state = clean(row.get("state_key"), "")
        period = clean(row.get("period"), "")
        sections = [
            "Blackapple",
            render_table(
                ["Variant", "Score", "Status", "Triggers", "#Candidates", "Examples", f"{period} Hits"],
                [
                    [
                        item.get("Variant"),
                        item.get("BA-Score"),
                        item.get("Status"),
                        item.get("Triggers"),
                        item.get("#Candidates"),
                        item.get("Examples"),
                        item.get(period_hit_field(period)),
                    ]
                    for item in self.blackapple_for_state(state)
                ],
            ),
            "",
            "Due doubles",
            render_table(
                ["Variant", "Draws since double", "Family 1", "Family 2", "Family 3", f"{period} winner in family"],
                [
                    [
                        item.get("Variant"),
                        item.get("Draws Since Double"),
                        item.get("Family 1"),
                        item.get("Family 2"),
                        item.get("Family 3"),
                        item.get(f"{period} Winner In Family"),
                    ]
                    for item in self.due_doubles_for_state(state)
                ],
            ),
            "",
            "Profit alerts",
            render_table(
                ["Variant", "Alert ID", "Strength", "Suggested", "Canonical", "Implied set", f"{period} Hits"],
                [
                    [
                        item.get("Variant"),
                        item.get("AlertId"),
                        item.get("Strength"),
                        item.get("Suggested"),
                        item.get("Canonical"),
                        item.get("ImpliedSet"),
                        item.get(period_hit_field(period)),
                    ]
                    for item in self.profit_alerts_for_state(state, row)
                ],
            ),
            "",
            "Compound events",
            render_table(
                ["Variant", "Top event", "Priority", "Tags", "Candidate alerts", "Promoter alerts", "Merged hits"],
                [
                    [
                        item.get("variant"),
                        item.get("top_event"),
                        item.get("priority"),
                        item.get("watchlist_tags"),
                        item.get("candidate_alert_ids"),
                        item.get("promoter_alert_ids"),
                        item.get("merged_hits"),
                    ]
                    for item in self.compound_for_state(state)
                ],
            ),
            "",
            "VTRAC repeat watch",
            render_table(
                ["Variant", "Current VT", "Streak", "Heat", "Winner", "Winner VT", "Current==Winner"],
                [
                    [
                        item.get("Variant"),
                        item.get("Current Index"),
                        item.get("Current Streak"),
                        item.get("Heat Index"),
                        item.get("Winner"),
                        item.get("Winner VTRAC"),
                        item.get("Current==WinnerVTRAC"),
                    ]
                    for item in self.vtrac_repeat_for_state(state)
                ],
            ),
        ]
        return "\n".join(sections)

    def render_signal_rows(self, rows: list[dict[str, str]]) -> str:
        return render_table(
            [
                "Family",
                "Tool",
                "Signal ID",
                "Value",
                "Kind",
                "Rank",
                "Match",
                "Lane",
                "Pre-draw",
                "Notes",
            ],
            [
                [
                    row.get("source_family"),
                    row.get("source_tool"),
                    row.get("signal_id"),
                    row.get("signal_value"),
                    row.get("signal_value_kind"),
                    row.get("signal_rank"),
                    row.get("match_best_mode"),
                    row.get("target_lane"),
                    row.get("pre_draw_available"),
                    row.get("notes"),
                ]
                for row in rows
            ],
        )

    def render_stage2b_rows(self, rows: list[dict[str, str]]) -> str:
        return render_table(
            [
                "Scope",
                "Source A",
                "Source B",
                "Matched values",
                "Matched events",
                "Positive events",
                "Outcome mix",
                "Status mix",
                "Role",
            ],
            [
                [
                    row.get("pair_scope"),
                    row.get("source_a"),
                    row.get("source_b"),
                    row.get("matched_values_sample"),
                    row.get("matched_event_count"),
                    row.get("positive_conversion_event_count"),
                    row.get("outcome_mix"),
                    row.get("status_mix"),
                    row.get("ledger_role"),
                ]
                for row in rows
            ],
        )

    def render_spillover_rows(self, rows: list[dict[str, Any]]) -> str:
        return render_table(
            [
                "State A",
                "State B",
                "Relationship",
                "Surface",
                "Support",
                "Canonicals",
                "VT",
                "Winner matched shared territory",
                "Explanation",
            ],
            [
                [
                    row.get("state_a"),
                    row.get("state_b"),
                    row.get("relationship_type"),
                    row.get("source_surface"),
                    row.get("support_count"),
                    row.get("canonical_families"),
                    row.get("vtrac_indices"),
                    row.get("_winner_shared_match"),
                    row.get("explanation"),
                ]
                for row in rows
            ],
        )

    def interpretation(
        self,
        row: dict[str, str],
        cu_matches: list[dict[str, Any]],
        play_matches: list[dict[str, str]],
        sandbox: dict[str, Any],
    ) -> str:
        labels = [self.combined_credit_label(row), self.control_label(row), self.arena_label(row)]
        if self.has_tracker_support(row):
            labels.append("Tracker-supported catch")
        phrases = [f"Primary labels: {', '.join(label for label in labels if label)}."]
        if truthy(row.get("play_card_any_exact")) or truthy(row.get("play_card_any_box")):
            phrases.append(
                "The Play Card layer contained the winner, so this is direct evidence for the "
                "current playable control arm."
            )
        elif cu_matches:
            phrases.append(
                "The Candidate Universe contained the winner but the Play Card did not fully carry "
                "it forward, which makes this a budgeting or selection-frontier review case."
            )
        if self.has_arena_signal(row):
            phrases.append(
                "The Arena diagnostic layer also surfaced the winner territory, so this event should "
                "be used as translator-learning evidence rather than only as old-stack performance."
            )
        if self.has_tracker_support(row):
            phrases.append(
                "At least one aggregated tracker supported the result, which makes it useful for "
                "reviewing alert weighting and cross-layer convergence."
            )
        if truthy(row.get("play_vtrac_only_hit")) or clean(row.get("hit_class")) == "VTRAC_ONLY":
            phrases.append(
                "The main conversion is VTRAC-only territory, so it should not be overcounted as "
                "straight or boxed precision."
            )
        if sandbox:
            phrases.append(
                "The linked sandbox seed lists show which Arena-preserved candidates existed before "
                "later translator and final-combination rebuilds."
            )
        return " ".join(phrases)

    def rank_bucket(self, row: dict[str, str]) -> str:
        rank = safe_int(row.get("board_rank"), 999)
        if rank <= 3:
            return "top 3"
        if rank <= 5:
            return "top 5"
        if rank <= 10:
            return "top 10"
        return "outside top 10"

    def combined_credit_label(self, row: dict[str, str]) -> str:
        control = self.has_control_catch(row)
        arena = self.has_arena_signal(row)
        tracker = self.has_tracker_support(row)
        vtrac_only = truthy(row.get("play_vtrac_only_hit")) or clean(row.get("hit_class")) == "VTRAC_ONLY"
        if vtrac_only and control and arena:
            return "Arena + control-arm VTRAC-only territory"
        if vtrac_only and control:
            return "Control-arm VTRAC-only territory"
        if vtrac_only and arena:
            return "Arena VTRAC-only territory"
        if vtrac_only:
            return "VTRAC-only territory"
        if control and arena:
            return "Arena + control-arm overlap"
        if control:
            return "Control-arm catch"
        if arena:
            return "Arena diagnostic catch"
        if tracker:
            return "Tracker-supported catch"
        return "No credited hit"

    def control_label(self, row: dict[str, str]) -> str:
        if truthy(row.get("play_card_any_exact")) or truthy(row.get("play_straight_hit")):
            return "Play Card exact/straight catch"
        if truthy(row.get("play_card_any_box")) or truthy(row.get("play_box_any_hit")):
            return "Play Card boxed catch"
        if truthy(row.get("cu_exact")):
            return "Candidate Universe exact catch"
        if truthy(row.get("cu_box")):
            return "Candidate Universe boxed catch"
        if truthy(row.get("play_vtrac_hit")) or truthy(row.get("candidate_vtrac_hit")):
            return "Control-arm VTRAC territory"
        return "No old control-arm conversion"

    def arena_label(self, row: dict[str, str]) -> str:
        if truthy(row.get("arena_exact_signal")) or truthy(row.get("sandbox_exact_seed")):
            return "Arena exact diagnostic catch"
        if (
            truthy(row.get("arena_box_signal"))
            or truthy(row.get("arena_primary_box"))
            or truthy(row.get("sandbox_box_seed"))
        ):
            return "Arena boxed diagnostic catch"
        if truthy(row.get("arena_primary_vt")) or truthy(row.get("sandbox_vt_seed")):
            return "Arena VTRAC diagnostic catch"
        signature = clean(row.get("arena_final_candidate_signature"), "")
        if signature == "CONTROL_ARM_ONLY_CATCH":
            return "No Arena diagnostic catch (control-arm-only signature)"
        if signature not in {"", "-"}:
            return f"Arena finalist diagnostic catch: {signature}"
        return "No Arena diagnostic catch"

    def arena_status_for_no_credit(self, row: dict[str, str]) -> str:
        label = self.arena_label(row)
        if label == "No Arena diagnostic catch":
            return label
        return label.replace(" catch", " present")

    def has_control_catch(self, row: dict[str, str]) -> bool:
        fields = [
            "cu_exact",
            "cu_box",
            "play_card_any_exact",
            "play_card_any_box",
            "play_straight_hit",
            "play_box_any_hit",
            "play_inclusive_hit",
        ]
        return any(truthy(row.get(field)) for field in fields)

    def has_arena_signal(self, row: dict[str, str]) -> bool:
        fields = [
            "arena_box_signal",
            "arena_exact_signal",
            "arena_primary_box",
            "arena_primary_vt",
            "sandbox_box_seed",
            "sandbox_exact_seed",
            "sandbox_vt_seed",
        ]
        return any(truthy(row.get(field)) for field in fields) or clean(
            row.get("arena_final_candidate_signature"), ""
        ) not in {"", "-", "CONTROL_ARM_ONLY_CATCH"}

    def has_tracker_support(self, row: dict[str, str]) -> bool:
        fields = [
            "profit_alert_support",
            "compound_event_support",
            "due_double_support",
            "blackapple_support",
            "positional_support",
            "r_consensus_support",
            "survivor_support",
        ]
        return any(truthy(row.get(field)) for field in fields)

    def tracker_summary(self, row: dict[str, str]) -> str:
        labels = []
        mapping = [
            ("blackapple_support", "Blackapple"),
            ("due_double_support", "Due doubles"),
            ("profit_alert_support", "Profit alerts"),
            ("compound_event_support", "Compound events"),
            ("positional_support", "Positional"),
            ("r_consensus_support", "R consensus"),
            ("survivor_support", "Survivor"),
        ]
        for field, label in mapping:
            if truthy(row.get(field)):
                labels.append(label)
        return ", ".join(labels) if labels else "-"

    def decay_summary(self, row: dict[str, str]) -> str:
        eid = event_id(row)
        if eid in self.decay_by_event:
            return clean(self.decay_by_event[eid].get("decay_profile"), "future_day_decay")
        evidence = self.evidence_by_event.get(eid, {})
        profile = clean(evidence.get("decay_any_profile"), "")
        return profile if profile not in {"", "-"} else "same-day/no decay fixture"

    def decay_detail(self, row: dict[str, str]) -> str:
        eid = event_id(row)
        decay = self.decay_by_event.get(eid)
        if decay:
            return (
                f"profile={clean(decay.get('decay_profile'))}; "
                f"event={clean(decay.get('decay_event'))}; "
                f"active_metric_count={clean(decay.get('active_metric_count'))}; "
                f"metrics={clean(decay.get('active_metrics'))}"
            )
        evidence = self.evidence_by_event.get(eid, {})
        return (
            f"profile={clean(evidence.get('decay_any_profile'))}; "
            f"event={clean(evidence.get('decay_any_event'))}; "
            f"active_metric_count={clean(evidence.get('active_decay_metric_count'))}"
        )

    def bonus_for_event(self, row: dict[str, str]) -> dict[str, str] | None:
        state = clean(row.get("state_key"), "")
        period = clean(row.get("period"), "")
        winner = clean(row.get("winner"), "")
        for bonus in self.bonus_rows:
            if (
                clean(bonus.get("project_state"), "") == state
                and clean(bonus.get("slot"), "") == period
                and clean(bonus.get("core_draw"), "") == winner
            ):
                return bonus
        return None

    def bonus_summary(self, bonus: dict[str, str] | None) -> str:
        if not bonus:
            return "-"
        return f"{clean(bonus.get('bonus_label_raw'))}={clean(bonus.get('bonus_digit'))}"

    def bonus_detail(self, bonus: dict[str, str] | None) -> str:
        if not bonus:
            return "No bonus/fireball row for this event."
        return (
            f"{clean(bonus.get('bonus_label_raw'))} digit {clean(bonus.get('bonus_digit'))}; "
            f"status={clean(bonus.get('status'))}; reason={clean(bonus.get('reason'))}."
        )

    def control_evidence_summary(
        self,
        row: dict[str, str],
        cu_matches: list[dict[str, Any]],
        play_matches: list[dict[str, str]],
    ) -> str:
        cu = self.candidate_universe_for_state(clean(row.get("state_key"), ""))
        union_count = clean(cu.get("union_combos_count")) if cu else "-"
        return (
            f"CU exact={bool_badge(row.get('cu_exact'))}; CU box={bool_badge(row.get('cu_box'))}; "
            f"CU union size={union_count}; matched CU packs={len(cu_matches)}; "
            f"Play exact={bool_badge(row.get('play_card_any_exact'))}; "
            f"Play box={bool_badge(row.get('play_card_any_box'))}; "
            f"matched Play Card rows={len(play_matches)}."
        )

    def arena_evidence_summary(self, row: dict[str, str], sandbox: dict[str, Any]) -> str:
        sandbox_path = self.state_artifact_path(
            clean(row.get("state_key"), ""), "translation_sandbox_seed__tool_only__arena_v0.json"
        )
        return (
            f"exact={bool_badge(row.get('arena_exact_signal'))}; "
            f"box={bool_badge(row.get('arena_box_signal'))}; "
            f"primary_box={bool_badge(row.get('arena_primary_box'))}; "
            f"primary_vt={bool_badge(row.get('arena_primary_vt'))}; "
            f"sandbox={rel_link(self.out_file, sandbox_path, sandbox_path.name)}; "
            f"signature={clean(row.get('arena_final_candidate_signature'))}."
        )

    def list_size_summary(
        self,
        row: dict[str, str],
        cu_matches: list[dict[str, Any]],
        play_matches: list[dict[str, str]],
    ) -> str:
        cu = self.candidate_universe_for_state(clean(row.get("state_key"), ""))
        union_count = clean(cu.get("union_combos_count")) if cu else "-"
        min_play = "-"
        if play_matches:
            min_play = str(min(safe_int(match.get("combos_count"), 9999) for match in play_matches))
        return f"CU union={union_count}; CU packs hit={len(cu_matches)}; Play rows hit={len(play_matches)}; tightest Play row={min_play}"

    def candidate_universe_for_state(self, state: str) -> dict[str, Any]:
        if state not in self.cu_cache:
            self.cu_cache[state] = read_json(
                self.state_artifact_path(state, "candidate_universe__tool_only__arena_v0.json")
            ) or {}
        return self.cu_cache[state]

    def play_card_for_state(self, state: str) -> dict[str, Any]:
        if state not in self.play_card_cache:
            self.play_card_cache[state] = read_json(
                self.state_artifact_path(state, "play_card__tool_only__arena_v0.json")
            ) or {}
        return self.play_card_cache[state]

    def sandbox_for_state(self, state: str) -> dict[str, Any]:
        if state not in self.sandbox_cache:
            self.sandbox_cache[state] = read_json(
                self.state_artifact_path(state, "translation_sandbox_seed__tool_only__arena_v0.json")
            ) or {}
        return self.sandbox_cache[state]

    def state_artifact_path(self, state: str, filename: str) -> Path:
        return self.share_root / state / filename

    def matched_cu_packs(self, row: dict[str, str]) -> list[dict[str, Any]]:
        state = clean(row.get("state_key"), "")
        winner = normalize_combo(row.get("winner"))
        canon = clean(row.get("winner_canonical"), canonicalize(winner))
        winner_vt = clean(row.get("winner_vtrac_index"), vtrac_value(winner))
        cu = self.candidate_universe_for_state(state)
        matches: list[dict[str, Any]] = []
        for pack in cu.get("packs", []):
            combos = [normalize_combo(combo) for combo in pack.get("combos", [])]
            canonicals = [canonicalize(combo) for combo in pack.get("canonicals", [])]
            modes = []
            if winner in combos:
                modes.append("exact")
            if canon in canonicals:
                modes.append("box/canonical")
            if winner_vt and any(vtrac_value(item) == winner_vt for item in canonicals):
                modes.append("vtrac")
            if modes:
                match = dict(pack)
                match["match_mode"] = ", ".join(modes)
                match["combos"] = combos
                matches.append(match)
        return sorted(matches, key=lambda item: (safe_int(item.get("combos_count"), 9999), clean(item.get("pack_id"))))

    def matched_play_rows(self, row: dict[str, str]) -> list[dict[str, str]]:
        eid = event_id(row)
        rows = []
        for grade in self.play_grade_by_event.get(eid, []):
            if any(
                truthy(grade.get(field))
                for field in [
                    "hit_any",
                    "hit_any_box",
                    "hit_any_inclusive",
                    "straight_hit",
                    "box_hit",
                    "canon_hit_any_perm",
                    "vtrac_index_hit",
                    "pack_any_correct",
                    "pack_hit_any_inclusive",
                    "filler_hit_any_inclusive",
                ]
            ):
                rows.append(grade)
        return rows

    def play_match_sort_key(self, row: dict[str, str]) -> tuple[int, int, str, str]:
        mode_rank = 9
        if truthy(row.get("straight_hit")):
            mode_rank = 0
        elif truthy(row.get("box_hit")):
            mode_rank = 1
        elif truthy(row.get("canon_hit_any_perm")):
            mode_rank = 2
        elif truthy(row.get("vtrac_index_hit")):
            mode_rank = 3
        elif truthy(row.get("hit_any_inclusive")):
            mode_rank = 4
        return (mode_rank, safe_int(row.get("combos_count"), 9999), clean(row.get("strategy")), clean(row.get("budget_label")))

    def play_match_mode(self, row: dict[str, str]) -> str:
        labels = []
        mapping = [
            ("straight_hit", "straight"),
            ("box_hit", "box"),
            ("canon_hit_any_perm", "canonical"),
            ("vtrac_index_hit", "vtrac"),
            ("vtrac_index_hit_only", "vtrac-only"),
            ("hit_any_inclusive", "inclusive"),
            ("pack_any_correct", "pack"),
            ("filler_hit_any_inclusive", "filler"),
        ]
        for field, label in mapping:
            if truthy(row.get(field)):
                labels.append(label)
        return ", ".join(labels) if labels else "-"

    def play_card_combos_for_grade_row(self, state: str, grade: dict[str, str]) -> list[str]:
        play_card = self.play_card_for_state(state)
        strategy = clean(grade.get("strategy"), "")
        budget = clean(grade.get("budget_label"), "")
        strategies = play_card.get("strategies", {})
        if not isinstance(strategies, dict):
            return []
        strategy_node = strategies.get(strategy, {})
        if not isinstance(strategy_node, dict):
            return []
        budget_node = strategy_node.get(budget, {})
        if not isinstance(budget_node, dict):
            return []
        combos = budget_node.get("combos", [])
        return [normalize_combo(combo) for combo in combos]

    def seed_values(self, seeds: Any, key: str) -> list[str]:
        if not isinstance(seeds, dict):
            return []
        value = seeds.get(key, [])
        if isinstance(value, list):
            results = []
            for item in value:
                if isinstance(item, dict):
                    results.append(clean(item.get("value"), ""))
                else:
                    results.append(clean(item, ""))
            return [item for item in results if item]
        return split_values(value)

    def blackapple_for_state(self, state: str) -> list[dict[str, str]]:
        return [row for row in self.blackapple_rows if clean(row.get("StateKey"), "") == state]

    def due_doubles_for_state(self, state: str) -> list[dict[str, str]]:
        return [row for row in self.due_double_rows if clean(row.get("StateKey"), "") == state]

    def profit_alerts_for_state(self, state: str, event_row: dict[str, str]) -> list[dict[str, str]]:
        period = clean(event_row.get("period"), "")
        rows = [
            row
            for row in self.profit_alert_rows
            if clean(row.get("StateKey"), "") == state
            and (
                clean(row.get(period_hit_field(period))) != "-"
                or clean(row.get("Variant")) in {"Combined", period}
            )
        ]
        return sorted(rows, key=lambda row: -safe_float(row.get("Strength")))[:25]

    def compound_for_state(self, state: str) -> list[dict[str, str]]:
        return [row for row in self.compound_rows if clean(row.get("state_key"), "") == state]

    def vtrac_repeat_for_state(self, state: str) -> list[dict[str, str]]:
        return [row for row in self.vtrac_repeat_rows if clean(row.get("StateKey"), "") == state]

    def top_signal_rows(self, eid: str) -> list[dict[str, str]]:
        rows = self.signal_by_event.get(eid, [])

        def key(row: dict[str, str]) -> tuple[int, int, float]:
            mode = clean(row.get("match_best_mode"), "")
            mode_rank = {"exact": 0, "box": 1, "vtrac": 2}.get(mode, 9)
            return (mode_rank, safe_int(row.get("signal_rank"), 9999), -safe_float(row.get("normalized_score")))

        return sorted(rows, key=key)[:20]

    def top_stage2b_rows(self, eid: str) -> list[dict[str, str]]:
        rows = self.stage2b_by_event.get(eid, [])
        return sorted(
            rows,
            key=lambda row: (
                -safe_int(row.get("positive_conversion_event_count")),
                -safe_int(row.get("matched_value_count")),
                safe_int(row.get("overlap_value_count"), 9999),
            ),
        )[:16]

    def spillover_for_event(self, row: dict[str, str]) -> list[dict[str, Any]]:
        state = clean(row.get("state_key"), "")
        canon = clean(row.get("winner_canonical"), canonicalize(row.get("winner")))
        vt = clean(row.get("winner_vtrac_index"), vtrac_value(row.get("winner")))
        results: list[dict[str, Any]] = []
        for rel in self.spillover_rows:
            if rel.get("state_a") != state and rel.get("state_b") != state:
                continue
            rel_copy = dict(rel)
            canonicals = split_values(rel.get("canonical_families")) + split_values(
                rel.get("secondary_canonical_families")
            )
            vts = split_values(rel.get("vtrac_indices"))
            matched = (canon and canon in canonicals) or (vt and vt in vts)
            rel_copy["_winner_shared_match"] = "yes" if matched else "no"
            results.append(rel_copy)
        return sorted(
            results,
            key=lambda rel: (
                0 if rel.get("_winner_shared_match") == "yes" else 1,
                -safe_int(rel.get("support_count")),
            ),
        )[:12]


def main() -> int:
    args = parse_args()
    window_root = args.window_root.resolve()
    if not window_root.exists():
        raise SystemExit(f"Window root not found: {window_root}")
    out_file = (
        args.out.resolve()
        if args.out
        else window_root
        / "TRAINING_KITS"
        / f"{args.date}__CUSTOM_HIT_REPORT"
        / f"{args.date}__CUSTOM_HIT_REPORT.md"
    )
    out_file.parent.mkdir(parents=True, exist_ok=True)
    builder = DayReportBuilder(window_root, args.date, out_file)
    out_file.write_text(builder.build(), encoding="utf-8")
    print(out_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
