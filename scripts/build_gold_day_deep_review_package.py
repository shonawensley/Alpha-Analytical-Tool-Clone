#!/usr/bin/env python3
"""Build a deterministic external-review package for one extraction-zone Gold Day.

The builder is deliberately read-only with respect to its source artifacts. It
consolidates frozen predictive analysis, result-aware autopsies, corrected winner
HTML, and AUX CORE evidence into a new package that can be reviewed externally.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATE = "2026-03-09"
DEFAULT_CORE_ROOT = Path("tasks/CORE_EXTRACTION_ZONE_EXAMPLES/2026-03-09")
DEFAULT_EXTERNAL_ROOT = Path(
    "tasks/PRIMARY_EXTRACTION_ZONE_REVIEW__2026-03-09/EXTERNAL_REVIEW_READY_V2"
)
DEFAULT_AUX_ROOT = Path("docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/AUX_CORE_V1/states")
DEFAULT_OUTPUT_DIR = DEFAULT_CORE_ROOT / "CHATGPT_PRO_DEEP_REVIEW_PACKAGE_V1"
PERIOD_ORDER = {"Midday": 0, "Evening": 1}
RELATION_ORDER = {
    "NO_MATCH": 0,
    "BOXED_VTRAC": 1,
    "ORDERED_VTRAC": 2,
    "CANONICAL_BOX": 3,
    "EXACT_LITERAL": 4,
}
STATE_DRAW_STEMS = {
    "Connecticut4": "Connecticut",
    "Delaware4": "Delaware",
    "Florida4": "Florida",
    "Indiana4": "Indiana",
    "Michigan4": "Michigan",
    "NewJersey4": "New_Jersey",
    "NewYork4": "New_York",
    "NorthCarolina4": "North_Carolina",
    "Ohio4": "Ohio",
    "OntarioCanada4": "Ontario",
    "Pennsylvania4": "Pennsylvania",
    "PuertoRico4": "Puerto_Rico",
    "SouthCarolina4": "South_Carolina",
    "Virginia4": "Virginia",
}


@dataclass(frozen=True)
class CaseSource:
    state: str
    period: str
    result: str
    immediate: dict[str, Any]
    predictive_md: Path
    predictive_json: Path
    post_md: Path
    post_json: Path
    winner_html: Path
    aux_post_md: Path
    aux_post_json: Path

    @property
    def case_id(self) -> str:
        return f"{self.state}__{self.period}__{self.result}"


@dataclass(frozen=True)
class StateSource:
    state: str
    predictive_md: Path
    predictive_json: Path
    aux_pre_md: Path
    aux_pre_json: Path
    cases: tuple[CaseSource, CaseSource]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument("--core-root", type=Path, default=DEFAULT_CORE_ROOT)
    parser.add_argument("--external-root", type=Path, default=DEFAULT_EXTERNAL_ROOT)
    parser.add_argument("--aux-root", type=Path, default=DEFAULT_AUX_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate source discovery without writing a package.",
    )
    parser.add_argument(
        "--verify-output",
        action="store_true",
        help="Verify an existing package against its manifest without rebuilding it.",
    )
    parser.add_argument(
        "--replace-output",
        action="store_true",
        help="Atomically replace a previously generated, manifest-valid package.",
    )
    return parser.parse_args()


def absolute(path: Path) -> Path:
    return path if path.is_absolute() else REPO_ROOT / path


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def ensure_repo_root() -> None:
    if Path.cwd().resolve() != REPO_ROOT:
        raise RuntimeError(
            f"Run from repository root {REPO_ROOT}; current directory is {Path.cwd().resolve()}"
        )


def require_file(path: Path, description: str) -> Path:
    if not path.is_file():
        raise FileNotFoundError(f"Missing {description}: {repo_relative(path)}")
    return path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, content: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(content, handle, indent=2, sort_keys=True, ensure_ascii=True)
        handle.write("\n")


def md_escape(value: Any) -> str:
    if value is None or value == "":
        return "-"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple, set)):
        value = ", ".join(str(item) for item in value) if value else "-"
    if isinstance(value, dict):
        value = json.dumps(value, sort_keys=True, ensure_ascii=True)
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def md_code(value: Any) -> str:
    rendered = md_escape(value)
    return rendered if rendered == "-" else f"`{rendered.replace('`', '')}`"


def md_table(headers: Sequence[str], rows: Iterable[Sequence[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_escape(item) for item in row) + " |")
    return "\n".join(lines)


def demote_markdown(text: str, amount: int = 2) -> str:
    def replace(match: re.Match[str]) -> str:
        level = min(6, len(match.group(1)) + amount)
        return "#" * level + match.group(2)

    return re.sub(r"^(#{1,6})(\s+)", replace, text, flags=re.MULTILINE).strip()


def source_marker(role: str, path: Path) -> str:
    return (
        f"<!-- SOURCE role={role} path={repo_relative(path)} "
        f"sha256={sha256(path)} -->"
    )


def embedded_markdown(role: str, path: Path, heading_demote: int = 2) -> str:
    return "\n".join(
        [
            source_marker(role, path),
            demote_markdown(read_text(path), heading_demote),
            f"<!-- SOURCE_END role={role} -->",
        ]
    )


def section_from_heading(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Heading not found: {heading}")
    return text[match.start() :].strip()


def rows_from_payload(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("rows"), list):
        return payload["rows"]
    raise TypeError("Expected a list or an object containing a rows list")


def register_source(
    registry: dict[str, dict[str, Any]],
    path: Path,
    role: str,
    state: str = "",
    period: str = "",
    result: str = "",
) -> None:
    require_file(path, role)
    relative = repo_relative(path)
    entry = {
        "path": relative,
        "role": role,
        "state": state,
        "period": period,
        "result": result,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }
    existing = registry.get(relative)
    if existing and existing != entry:
        raise ValueError(f"Conflicting source registration for {relative}")
    registry[relative] = entry


def external_artifact_map(external_manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(item["output_path"]): item
        for item in external_manifest.get("artifacts", [])
        if isinstance(item, dict) and item.get("output_path")
    }


def discover_sources(
    date: str,
    core_root: Path,
    external_root: Path,
    aux_root: Path,
) -> tuple[
    list[StateSource],
    dict[str, dict[str, Any]],
    dict[str, Any],
    dict[str, Any],
]:
    table1_path = require_file(
        core_root / "POST_RESULT/TABLE_1_IMMEDIATE_EXTRACTION_EVIDENCE.json",
        "immediate evidence ledger",
    )
    table1 = rows_from_payload(read_json(table1_path))
    if len(table1) != 28:
        raise ValueError(f"Expected 28 immediate evidence rows, found {len(table1)}")

    external_manifest_path = require_file(external_root / "MANIFEST.json", "external bundle manifest")
    external_manifest = read_json(external_manifest_path)
    artifact_map = external_artifact_map(external_manifest)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in table1:
        grouped[str(row["state"])].append(row)

    if len(grouped) != 14:
        raise ValueError(f"Expected 14 states, found {len(grouped)}")

    source_registry: dict[str, dict[str, Any]] = {}
    global_sources = {
        "predictive_synthesis_md": core_root / "PREDICTIVE/GOLD_DAY_PREDICTIVE_SYNTHESIS.md",
        "predictive_synthesis_json": core_root / "PREDICTIVE/GOLD_DAY_PREDICTIVE_SYNTHESIS.json",
        "post_result_synthesis_md": core_root / "POST_RESULT/GOLD_DAY_POST_RESULT_SYNTHESIS.md",
        "post_result_synthesis_json": core_root / "POST_RESULT/GOLD_DAY_POST_RESULT_SYNTHESIS.json",
        "immediate_ledger_json": table1_path,
        "decay_ledger_json": core_root / "POST_RESULT/TABLE_2_DECAY_AND_BONUS_BALL.json",
        "doubles_ledger_json": core_root / "POST_RESULT/TABLE_3_DOUBLES_RANKING_VS_OUTCOMES.json",
        "straight_ledger_json": core_root / "POST_RESULT/STRAIGHT_PATHWAY_LEDGER.json",
        "assessment_contract_md": core_root / "POST_RESULT_ASSESSMENT_CONTRACT.md",
        "external_bundle_manifest": external_manifest_path,
    }
    for role, path in global_sources.items():
        register_source(source_registry, require_file(path, role), role)

    states: list[StateSource] = []
    case_matrix: list[dict[str, Any]] = []
    for state in sorted(grouped):
        rows = sorted(grouped[state], key=lambda item: PERIOD_ORDER.get(str(item["target_period"]), 99))
        periods = [str(item["target_period"]) for item in rows]
        if periods != ["Midday", "Evening"]:
            raise ValueError(f"{state} must have Midday and Evening rows; found {periods}")

        predictive_md = require_file(
            core_root / "PREDICTIVE" / state / "PREDICTIVE_ANALYSIS.md",
            f"{state} predictive Markdown",
        )
        predictive_json = require_file(
            core_root / "PREDICTIVE" / state / "PREDICTIVE_ANALYSIS.json",
            f"{state} predictive JSON",
        )
        aux_state_root = aux_root / state
        aux_pre_md = require_file(
            aux_state_root / "AUX_CORE__FULL_PRE_RESULT.md",
            f"{state} AUX CORE pre-result Markdown",
        )
        aux_pre_json = require_file(
            aux_state_root / "AUX_CORE__PRE_RESULT.json",
            f"{state} AUX CORE pre-result JSON",
        )
        register_source(source_registry, predictive_md, "state_predictive_md", state)
        register_source(source_registry, predictive_json, "state_predictive_json", state)
        register_source(source_registry, aux_pre_md, "aux_core_pre_result_md", state)
        register_source(source_registry, aux_pre_json, "aux_core_pre_result_json", state)

        cases: list[CaseSource] = []
        for row in rows:
            period = str(row["target_period"])
            result = str(row["result"]).zfill(3)
            case_dir = core_root / "POST_RESULT/cases" / state / f"{period}__{result}"
            post_md = require_file(case_dir / "POST_RESULT_AUTOPSY.md", "post-result autopsy Markdown")
            post_json = require_file(case_dir / "POST_RESULT_AUTOPSY.json", "post-result autopsy JSON")
            external_rel = Path(state) / "POST_RESULT" / (
                f"{period}__{result}__01_STRING_TABLE_WINNER_FORENSIC.html"
            )
            winner_html = require_file(
                external_root / external_rel,
                f"{state} {period} corrected winner HTML",
            )
            artifact = artifact_map.get(external_rel.as_posix())
            if not artifact:
                raise ValueError(f"Winner HTML is absent from external manifest: {external_rel}")
            if artifact.get("output_sha256") != sha256(winner_html):
                raise ValueError(f"Winner HTML hash does not match external manifest: {external_rel}")
            aux_post_md = require_file(
                aux_state_root / f"AUX_CORE__{period}__{result}.md",
                f"{state} {period} AUX CORE post-result Markdown",
            )
            aux_post_json = require_file(
                aux_state_root / f"AUX_CORE__{period}__{result}__POST_RESULT.json",
                f"{state} {period} AUX CORE post-result JSON",
            )

            register_source(source_registry, post_md, "state_post_result_md", state, period, result)
            register_source(source_registry, post_json, "state_post_result_json", state, period, result)
            register_source(source_registry, winner_html, "corrected_winner_html", state, period, result)
            register_source(source_registry, aux_post_md, "aux_core_post_result_md", state, period, result)
            register_source(source_registry, aux_post_json, "aux_core_post_result_json", state, period, result)
            cases.append(
                CaseSource(
                    state=state,
                    period=period,
                    result=result,
                    immediate=row,
                    predictive_md=predictive_md,
                    predictive_json=predictive_json,
                    post_md=post_md,
                    post_json=post_json,
                    winner_html=winner_html,
                    aux_post_md=aux_post_md,
                    aux_post_json=aux_post_json,
                )
            )
            case_matrix.append(
                {
                    "case_id": f"{date}__{state}__{period}__{result}",
                    "state": state,
                    "period": period,
                    "result": result,
                    "winner_html_source": repo_relative(winner_html),
                }
            )
        states.append(
            StateSource(
                state=state,
                predictive_md=predictive_md,
                predictive_json=predictive_json,
                aux_pre_md=aux_pre_md,
                aux_pre_json=aux_pre_json,
                cases=(cases[0], cases[1]),
            )
        )

    if len({item["case_id"] for item in case_matrix}) != 28:
        raise ValueError("Case IDs are not unique")
    global_payloads = {
        "predictive_synthesis": read_json(global_sources["predictive_synthesis_json"]),
        "post_result_synthesis": read_json(global_sources["post_result_synthesis_json"]),
        "immediate": table1,
        "decay": rows_from_payload(read_json(global_sources["decay_ledger_json"])),
        "doubles": rows_from_payload(read_json(global_sources["doubles_ledger_json"])),
        "straight": rows_from_payload(read_json(global_sources["straight_ledger_json"])),
    }
    metadata = {
        "case_matrix": case_matrix,
        "external_manifest": external_manifest,
        "global_sources": global_sources,
    }
    return states, source_registry, global_payloads, metadata


def validate_draw_sources(states: Sequence[StateSource]) -> list[dict[str, Any]]:
    receipts: list[dict[str, Any]] = []
    draw_root = REPO_ROOT / "data/cleaned/draws"
    for state_source in states:
        stem = STATE_DRAW_STEMS.get(state_source.state)
        if not stem:
            raise ValueError(f"No cleaned-draw stem configured for {state_source.state}")
        for variant, suffix in (
            ("Midday", "_Midday_draws.csv"),
            ("Evening", "_Evening_draws.csv"),
            ("Combined", "_draws.csv"),
        ):
            path = require_file(draw_root / f"{stem}{suffix}", "cleaned draw validation source")
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                row_count = sum(1 for _ in csv.DictReader(handle))
            if row_count < 1:
                raise ValueError(f"Cleaned draw file is empty: {repo_relative(path)}")
            receipts.append(
                {
                    "state": state_source.state,
                    "variant": variant,
                    "path": repo_relative(path),
                    "row_count": row_count,
                    "sha256": sha256(path),
                    "role": "VALIDATION_REFERENCE_ONLY__NOT_REREAD_FOR_PACKAGE_ANALYTICS",
                }
            )
    return receipts


def zone_coverage(states: Sequence[StateSource]) -> dict[str, dict[str, int]]:
    relations = ("BOXED_VTRAC", "CANONICAL_BOX", "ORDERED_VTRAC", "EXACT_LITERAL")
    any_variant = Counter()
    target_or_combined = Counter()
    for state in states:
        for case in state.cases:
            payload = read_json(case.post_json)
            relation_payload = payload["secondary_raw_table_scan"]["relations"]
            for relation in relations:
                occurrences = relation_payload.get(relation, {}).get("occurrences", [])
                zone_occurrences = [
                    item for item in occurrences if item.get("zone1") or item.get("zone2")
                ]
                if zone_occurrences:
                    any_variant[relation] += 1
                if any(
                    item.get("target_context_role") in {"TARGET_VARIANT", "COMBINED_VARIANT"}
                    for item in zone_occurrences
                ):
                    target_or_combined[relation] += 1
    return {
        "any_variant": {relation: any_variant[relation] for relation in relations},
        "target_or_combined": {relation: target_or_combined[relation] for relation in relations},
    }


def case_summary_rows(state: StateSource) -> list[list[Any]]:
    rows: list[list[Any]] = []
    for case in state.cases:
        immediate = case.immediate
        aux = read_json(case.aux_post_json)["conversion_read"]
        rows.append(
            [
                case.period,
                md_code(case.result),
                md_code(immediate.get("result_canonical")),
                immediate.get("result_boxed_vtrac_index"),
                md_code(immediate.get("result_ordered_vcode")),
                md_code(immediate.get("frozen_opportunity_classification")),
                immediate.get("frozen_cumulative_width"),
                md_code(immediate.get("predictive_credit_label")),
                md_code(immediate.get("strongest_structural_relation")),
                "/".join(
                    str(immediate.get(key, 0))
                    for key in (
                        "raw_exact_literal_occurrences",
                        "raw_canonical_occurrences",
                        "raw_ordered_vtrac_occurrences",
                        "raw_boxed_vtrac_occurrences",
                    )
                ),
                md_code(immediate.get("first_material_success_or_loss_stage")),
                md_code(aux.get("highest_specificity_reached")),
                md_code(aux.get("translation_gap")),
            ]
        )
    return rows


def build_integrated_state_read(state: StateSource) -> str:
    immediate_rows = [case.immediate for case in state.cases]
    predictive_captures = sum(
        row.get("predictive_credit_label") != "PREDICTIVE_MISS" for row in immediate_rows
    )
    relation_presence = {
        "boxed VTRAC territory": sum(row.get("raw_boxed_vtrac_occurrences", 0) > 0 for row in immediate_rows),
        "canonical boxed winner": sum(row.get("raw_canonical_occurrences", 0) > 0 for row in immediate_rows),
        "ordered VTRAC lane": sum(row.get("raw_ordered_vtrac_occurrences", 0) > 0 for row in immediate_rows),
        "exact literal winner": sum(row.get("raw_exact_literal_occurrences", 0) > 0 for row in immediate_rows),
    }
    first_losses = Counter(row.get("first_material_success_or_loss_stage") for row in immediate_rows)
    aux_specificity = Counter(
        read_json(case.aux_post_json)["conversion_read"].get("highest_specificity_reached")
        for case in state.cases
    )
    return "\n".join(
        [
            f"- Frozen predictive capture occurred in **{predictive_captures}/2** outcomes. This is the only predictive-credit count.",
            "- Corrected result-aware table availability: "
            + "; ".join(f"{label} **{count}/2**" for label, count in relation_presence.items())
            + ". These are reverse-engineering availability observations, not predictive wins.",
            "- First material conversion stages: "
            + ", ".join(f"`{key}`={value}" for key, value in sorted(first_losses.items()))
            + ".",
            "- AUX CORE highest expressed specificity: "
            + ", ".join(f"`{key}`={value}" for key, value in sorted(aux_specificity.items()))
            + ". AUX evidence is reinforcement or translation evidence; it does not overwrite the string-first record.",
        ]
    )


def immediate_table_for_state(state: StateSource) -> str:
    return md_table(
        [
            "Period",
            "Result",
            "Canonical",
            "VT index",
            "Ordered VT",
            "Frozen opportunity",
            "Width",
            "Predictive credit",
            "Strongest raw relation",
            "Raw E/C/O/VT",
            "First material stage",
            "AUX highest",
            "AUX gap",
        ],
        case_summary_rows(state),
    )


def straight_section(state: StateSource, straight_rows: Sequence[dict[str, Any]]) -> str:
    selected = sorted(
        (row for row in straight_rows if row.get("state") == state.state),
        key=lambda row: PERIOD_ORDER.get(str(row.get("target")), 99),
    )
    parts: list[str] = []
    for row in selected:
        parts.extend(
            [
                f"### {row['target']} {row['winner']}",
                "",
                f"- Conclusion: {md_code(row.get('conclusion'))}; strength: {md_code(row.get('strength_class'))}.",
                f"- Canonical family ({row.get('canonical_family_width', 0)}): "
                + ", ".join(md_code(item) for item in row.get("canonical_family_members", []))
                + ".",
                f"- Ordered lane {md_code(row.get('official_ordered_vcode'))} "
                f"({row.get('ordered_lane_width', 0)}): "
                + ", ".join(md_code(item) for item in row.get("ordered_lane_members", []))
                + ".",
                "- Canonical x ordered-lane product: "
                + (
                    ", ".join(md_code(item) for item in row.get("canonical_x_ordered_lane_members", []))
                    if row.get("canonical_x_ordered_lane_members")
                    else "`NONE`"
                )
                + f" (width {row.get('canonical_x_ordered_lane_width', 0)}).",
                "- Conclusion-eligible routes: "
                + (
                    ", ".join(md_code(item) for item in row.get("conclusion_eligible_route_ids", []))
                    if row.get("conclusion_eligible_route_ids")
                    else "`NONE`"
                )
                + ".",
                "",
                md_table(
                    [
                        "Route",
                        "Trigger",
                        "Transformation",
                        "Product",
                        "Members",
                        "Width",
                        "Evidence",
                        "Merit",
                        "Eligible",
                        "Target-conditioned",
                        "Winner in product",
                    ],
                    [
                        [
                            md_code(route.get("route_id")),
                            md_code(route.get("trigger")),
                            md_code(route.get("transformation")),
                            md_code(route.get("product_type")),
                            ", ".join(str(item) for item in route.get("members", [])) or "-",
                            route.get("width", 0),
                            md_code(route.get("evidence_class")),
                            md_code(route.get("merit_class")),
                            route.get("conclusion_eligible", False),
                            route.get("target_conditioned_selector", False),
                            route.get("winner_in_members", False),
                        ]
                        for route in row.get("routes", [])
                    ],
                ),
                "",
                "Decision rationale:",
                "",
                *[f"- {item}" for item in row.get("decision_rationale", [])],
                "",
            ]
        )
    return "\n".join(parts).strip()


def aux_conversion_section(state: StateSource) -> str:
    rows: list[list[Any]] = []
    for case in state.cases:
        payload = read_json(case.aux_post_json)
        conversion = payload["conversion_read"]
        rows.append(
            [
                case.period,
                md_code(case.result),
                md_code(conversion.get("highest_specificity_reached")),
                md_code(conversion.get("highest_specificity_tier")),
                md_code(conversion.get("highest_narrowed_specificity")),
                f"{conversion.get('vtrac_territory_expressed', False)}/{conversion.get('vtrac_territory_narrowed', False)}",
                f"{conversion.get('canonical_box_expressed', False)}/{conversion.get('canonical_box_narrowed', False)}",
                f"{conversion.get('ordered_lane_expressed', False)}/{conversion.get('ordered_lane_narrowed', False)}",
                f"{conversion.get('exact_literal_expressed', False)}/{conversion.get('exact_literal_narrowed', False)}",
                md_code(conversion.get("translation_gap")),
                md_code(conversion.get("narrowed_translation_gap")),
            ]
        )
    return md_table(
        [
            "Period",
            "Result",
            "Highest expressed",
            "Tier",
            "Highest narrowed",
            "VT expressed/narrowed",
            "Canonical expressed/narrowed",
            "Order expressed/narrowed",
            "Exact expressed/narrowed",
            "Expression gap",
            "Narrowing gap",
        ],
        rows,
    )


def best_relation(rows: Sequence[dict[str, Any]]) -> str:
    return max(
        (str(row.get("best_relation") or "NO_MATCH") for row in rows),
        key=lambda item: RELATION_ORDER.get(item, -1),
        default="NO_MATCH",
    )


def decay_section(state: StateSource, decay_rows: Sequence[dict[str, Any]]) -> str:
    selected = [row for row in decay_rows if row.get("source_state") == state.state]
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in selected:
        key = (
            row.get("source_period"),
            row.get("cohort"),
            row.get("route_id"),
            row.get("identity_type"),
            row.get("original_burden"),
            row.get("qualifying_level"),
        )
        grouped[key].append(row)

    summaries: list[list[Any]] = []
    for key in sorted(grouped, key=lambda item: (PERIOD_ORDER.get(str(item[0]), 99), str(item[2]), str(item[1]))):
        rows = grouped[key]
        qualifying = [row for row in rows if row.get("qualifies")]
        offsets = [int(row["offset_index"]) for row in qualifying if row.get("offset_index") is not None]
        summaries.append(
            [
                key[0],
                md_code(key[1]),
                md_code(key[2]),
                md_code(key[3]),
                key[4],
                md_code(key[5]),
                len(rows),
                len({row.get("event_id") for row in rows if row.get("event_id")}),
                len(qualifying),
                min(offsets) if offsets else "-",
                md_code(best_relation(rows)),
            ]
        )

    qualifying_rows = sorted(
        (row for row in selected if row.get("qualifies")),
        key=lambda row: (
            PERIOD_ORDER.get(str(row.get("source_period")), 99),
            int(row.get("offset_index", 999)),
            str(row.get("channel")),
            str(row.get("route_id")),
        ),
    )
    parts = [
        f"The state ledger contains **{len(selected)}** channel observations. Negative rows remain in the machine-readable source ledger; the report preserves every route denominator and every qualifying convey event without reproducing repetitive open-window rows.",
        "",
        md_table(
            [
                "Source",
                "Cohort",
                "Route",
                "Identity",
                "Burden",
                "Credit level",
                "Channel rows",
                "Unique event IDs",
                "Convey rows",
                "First offset",
                "Best relation",
            ],
            summaries,
        ),
        "",
        "### Qualifying Decay/Convey Events",
        "",
    ]
    if qualifying_rows:
        parts.append(
            md_table(
                [
                    "Source",
                    "Route",
                    "Cohort",
                    "Channel",
                    "Offset",
                    "Event",
                    "Result",
                    "Relation",
                    "Credit level",
                    "Burden",
                ],
                [
                    [
                        row.get("source_period"),
                        md_code(row.get("route_id")),
                        md_code(row.get("cohort")),
                        md_code(row.get("channel")),
                        row.get("offset"),
                        md_code(row.get("event_id")),
                        md_code(row.get("result")),
                        md_code(row.get("best_relation")),
                        md_code(row.get("qualifying_level")),
                        row.get("original_burden"),
                    ]
                    for row in qualifying_rows
                ],
            )
        )
    else:
        parts.append("No qualifying convey event occurred inside the bounded decay window.")
    parts.extend(
        [
            "",
            "Bonus-ball rows are descriptive inventory only and receive no credit because substitution and payout rules remain unresolved.",
        ]
    )
    return "\n".join(parts)


def doubles_section(state: StateSource, doubles_rows: Sequence[dict[str, Any]]) -> str:
    selected = sorted(
        (row for row in doubles_rows if row.get("state") == state.state),
        key=lambda row: PERIOD_ORDER.get(str(row.get("target_period")), 99),
    )
    return md_table(
        [
            "Period",
            "Result",
            "Subtype",
            "Due rank",
            "Dense rank",
            "Bucket",
            "Days since double",
            "Emitted double families",
            "Route width",
            "Immediate exact/canonical/VT",
            "Decay",
            "First decay offset",
        ],
        [
            [
                row.get("target_period"),
                md_code(row.get("result")),
                md_code(row.get("result_subtype")),
                row.get("state_rank"),
                row.get("dense_rank"),
                md_code(row.get("rank_bucket")),
                row.get("draws_since_double"),
                ", ".join(row.get("emitted_double_families", [])) or "-",
                row.get("route_width"),
                f"{int(bool(row.get('immediate_exact_capture')))}/{int(bool(row.get('immediate_canonical_capture')))}/{int(bool(row.get('immediate_boxed_vtrac_capture')))}",
                row.get("decay_capture"),
                row.get("first_decay_offset"),
            ]
            for row in selected
        ],
    )


def renderer_gap_section(state: StateSource, post_synthesis: dict[str, Any]) -> str:
    gaps = [
        item
        for item in post_synthesis.get("renderer_recognition_gap_cases", [])
        if f"__{state.state}__" in str(item.get("case_id"))
    ]
    if not gaps:
        return "No renderer-versus-secondary-scan recognition gap was recorded for this state."
    return "\n".join(
        f"- {md_code(item.get('case_id'))}: "
        + ", ".join(md_code(gap) for gap in item.get("gaps", []))
        for item in gaps
    )


def state_source_inventory(
    state: StateSource, source_registry: dict[str, dict[str, Any]]
) -> str:
    selected = sorted(
        (entry for entry in source_registry.values() if entry.get("state") == state.state),
        key=lambda item: (
            PERIOD_ORDER.get(str(item.get("period")), -1),
            str(item.get("role")),
            str(item.get("path")),
        ),
    )
    return md_table(
        ["Role", "Period", "Result", "Path", "Bytes", "SHA-256"],
        [
            [
                md_code(item["role"]),
                item.get("period") or "-",
                md_code(item.get("result")) if item.get("result") else "-",
                md_code(item["path"]),
                item["bytes"],
                md_code(item["sha256"]),
            ]
            for item in selected
        ],
    )


def build_state_report(
    date: str,
    state: StateSource,
    payloads: dict[str, Any],
    source_registry: dict[str, dict[str, Any]],
) -> str:
    post_synthesis = payloads["post_result_synthesis"]
    sections = [
        f"# {state.state} - {date} Comprehensive Extraction-Zone Review",
        "",
        "> Consolidated external-review report. The frozen predictive analysis is shown first and remains distinct from the two result-aware autopsies. Post-result discoveries receive zero predictive credit.",
        "",
        "## Scope And Evidence Boundary",
        "",
        "- `PREDICTIVE`: frozen, result-blind replay analysis. Only its emitted products can receive predictive credit.",
        "- `POST_RESULT`: winner-aware reverse engineering of availability, extraction zones, maturity, straight pathways, conversion loss, and testable hypotheses.",
        "- `AUX CORE`: string-first reinforcement/translation evidence. It is not an independent override and is not silently counted as predictive selection.",
        "- Corrected winner HTML is a post-result research renderer. Candidate-symmetric raw-table scans remain the structural authority.",
        "- This report changes no runtime, template, scoring, ranking, or combination-forming behavior.",
        "",
        "## Outcome And Conversion Overview",
        "",
        immediate_table_for_state(state),
        "",
        "## Integrated Reviewer Read",
        "",
        build_integrated_state_read(state),
        "",
        "## Frozen Predictive Analysis",
        "",
        embedded_markdown("STATE_PREDICTIVE_ANALYSIS", state.predictive_md, 2),
    ]
    for case in state.cases:
        sections.extend(
            [
                "",
                f"## {case.period} {case.result} Result-Aware Autopsy",
                "",
                embedded_markdown("STATE_POST_RESULT_AUTOPSY", case.post_md, 2),
            ]
        )
    sections.extend(
        [
            "",
            "## Integrated Immediate Evidence Ledger",
            "",
            immediate_table_for_state(state),
            "",
            "The `Raw E/C/O/VT` column means exact literal / canonical boxed winner / ordered VTRAC / boxed-VTRAC occurrences. It measures result-aware availability in the corrected scan, not independent votes and not predictive success.",
            "",
            "## Straight Pathway Ledger",
            "",
            straight_section(state, payloads["straight"]),
            "",
            "## AUX CORE Conversion Read",
            "",
            aux_conversion_section(state),
            "",
            "The complete ten-block pre-result AUX report and both post-result joins are preserved in the separate AUX CORE state report and AUX stack. The table above is the compact bridge needed for this state-level conversion review.",
            "",
            "## Bounded Decay And Convey Review",
            "",
            decay_section(state, payloads["decay"]),
            "",
            "## Due-Doubles Ranking Versus Outcomes",
            "",
            doubles_section(state, payloads["doubles"]),
            "",
            "The state due rank is contextual tracker evidence, not combination containment. A route receives credit only at its declared identity and width.",
            "",
            "## Renderer Recognition Gaps",
            "",
            renderer_gap_section(state, post_synthesis),
            "",
            "## Source Provenance",
            "",
            state_source_inventory(state, source_registry),
            "",
            "Machine-readable analytical payloads remain at their source paths and are hash-pinned in `05_PACKAGE_MANIFEST.json`. This narrative report intentionally preserves full analyst prose while summarizing large negative-row ledgers through explicit denominators.",
        ]
    )
    return "\n".join(sections)


def build_aux_state_report(date: str, state: StateSource) -> str:
    sections = [
        f"# {state.state} - {date} AUX CORE State Report",
        "",
        "> Full frozen pre-result AUX CORE evidence appears once. Each winner-aware join then appears as a separate, explicitly retrospective section.",
        "",
        "## Evidence Boundary",
        "",
        "- The full ten-block object is frozen pre-result evidence.",
        "- Winner joins are post-result diagnostics and receive zero predictive credit.",
        "- Cross-block convergence is evidence organization, not a calibrated final-ranking policy.",
        "- Positional evidence is role-aware reinforcement, ordering, pair, contradiction, or VTRAC-territory context; it is not automatically a finalist engine.",
        "",
        "## Full Frozen Pre-Result AUX CORE",
        "",
        embedded_markdown("AUX_CORE_FULL_PRE_RESULT", state.aux_pre_md, 2),
        "",
        "## Result-Aware Conversion Joins",
    ]
    for case in state.cases:
        payload = read_json(case.aux_post_json)
        conversion = payload["conversion_read"]
        post_section = section_from_heading(
            read_text(case.aux_post_md), "Post-Result Reverse-Engineering Join"
        )
        sections.extend(
            [
                "",
                f"### {case.period} {case.result}",
                "",
                f"- Highest expressed specificity: {md_code(conversion.get('highest_specificity_reached'))}; highest narrowed specificity: {md_code(conversion.get('highest_narrowed_specificity'))}.",
                f"- Expression gap: {md_code(conversion.get('translation_gap'))}; narrowing gap: {md_code(conversion.get('narrowed_translation_gap'))}.",
                "",
                source_marker("AUX_CORE_POST_RESULT_JOIN", case.aux_post_md),
                demote_markdown(post_section, 2),
                "<!-- SOURCE_END role=AUX_CORE_POST_RESULT_JOIN -->",
            ]
        )
    return "\n".join(sections)


def build_state_stack(
    date: str,
    states: Sequence[StateSource],
    state_reports: dict[str, str],
    payloads: dict[str, Any],
    metadata: dict[str, Any],
    coverage: dict[str, dict[str, int]],
) -> str:
    predictive_md = metadata["global_sources"]["predictive_synthesis_md"]
    post_md = metadata["global_sources"]["post_result_synthesis_md"]
    toc = "\n".join(f"- [{state.state}](#state-{state.state.lower()})" for state in states)
    zone_rows = []
    labels = {
        "BOXED_VTRAC": "Winning boxed-VTRAC territory",
        "CANONICAL_BOX": "Actual winning digits in any order",
        "ORDERED_VTRAC": "Correct VTRAC positional lane",
        "EXACT_LITERAL": "Exact literal winner",
    }
    for relation in ("BOXED_VTRAC", "CANONICAL_BOX", "ORDERED_VTRAC", "EXACT_LITERAL"):
        zone_rows.append(
            [
                labels[relation],
                f"{coverage['any_variant'][relation]}/28",
                f"{coverage['target_or_combined'][relation]}/28",
            ]
        )
    sections = [
        f"# {date} Gold Day - Comprehensive Extraction-Zone State Reports",
        "",
        "> This is a stacked external-review artifact. It contains all 14 complete state reports: frozen predictive analysis first, followed by Midday and Evening winner-aware autopsies and integrated evidence ledgers.",
        "",
        "## Critical Reading Boundary",
        "",
        "- Do not treat post-result winner availability as a predictive hit rate.",
        "- Frozen predictive emission and post-result discovery are deliberately separated inside every state report.",
        "- Relations share source windows. Exact, canonical, ordered-VTRAC, and boxed-VTRAC counts are nested analytical views, not independent votes.",
        "- The purpose of the result-aware layer is to identify repeating extraction pathways, ranking losses, translation losses, combination-product gaps, and bounded hypotheses for later shadow testing.",
        "",
        "## Core Extraction-Zone Availability",
        "",
        md_table(["Result-aware relation in Zone 1 or 2", "Any variant", "Target or Combined"], zone_rows),
        "",
        "These overlapping counts establish that winning territory was often present in the corrected extraction zones. They do not establish that a pre-result selector chose that territory, that the route was affordable, or that its order was resolved.",
        "",
        "## State Index",
        "",
        toc,
        "",
        "## Gold Day Frozen Predictive Synthesis",
        "",
        embedded_markdown("GOLD_DAY_PREDICTIVE_SYNTHESIS", predictive_md, 2),
        "",
        "## Gold Day Result-Aware Synthesis",
        "",
        embedded_markdown("GOLD_DAY_POST_RESULT_SYNTHESIS", post_md, 2),
        "",
        "## State Reports",
    ]
    for state in states:
        sections.extend(
            [
                "",
                "---",
                "",
                f'<a id="state-{state.state.lower()}"></a>',
                f"<!-- STATE_REPORT_START state={state.state} -->",
                demote_markdown(state_reports[state.state], 1),
                f"<!-- STATE_REPORT_END state={state.state} -->",
            ]
        )
    return "\n".join(sections)


def build_aux_stack(
    date: str, states: Sequence[StateSource], aux_reports: dict[str, str]
) -> str:
    sections = [
        f"# {date} Gold Day - AUX CORE State Reports",
        "",
        "> Stacked 14-state AUX CORE evidence package. Each state contains one full frozen pre-result ten-block report followed by the Midday and Evening post-result conversion joins.",
        "",
        "## Reading Boundary",
        "",
        "AUX CORE is reviewed only after string-table extraction evidence. Its pre-result blocks can reinforce, contradict, narrow, or expose a translation gap. Winner joins are retrospective and receive zero predictive credit.",
        "",
        "## State Index",
        "",
        *[f"- [{state.state}](#aux-state-{state.state.lower()})" for state in states],
    ]
    for state in states:
        sections.extend(
            [
                "",
                "---",
                "",
                f'<a id="aux-state-{state.state.lower()}"></a>',
                f"<!-- AUX_STATE_REPORT_START state={state.state} -->",
                demote_markdown(aux_reports[state.state], 1),
                f"<!-- AUX_STATE_REPORT_END state={state.state} -->",
            ]
        )
    return "\n".join(sections)


def extract_html_parts(document: str) -> tuple[list[str], str, str]:
    styles = re.findall(r"<style\b[^>]*>(.*?)</style>", document, flags=re.IGNORECASE | re.DOTALL)
    title_match = re.search(r"<title\b[^>]*>(.*?)</title>", document, flags=re.IGNORECASE | re.DOTALL)
    body_match = re.search(r"<body\b[^>]*>(.*?)</body>", document, flags=re.IGNORECASE | re.DOTALL)
    if not body_match:
        raise ValueError("Winner HTML has no body element")
    title = re.sub(r"\s+", " ", title_match.group(1)).strip() if title_match else "Winner forensic"
    return styles, title, body_match.group(1).strip()


def build_stacked_winner_html(
    date: str,
    states: Sequence[StateSource],
    external_manifest: dict[str, Any],
    external_root: Path,
) -> tuple[str, dict[str, Any]]:
    artifact_map = external_artifact_map(external_manifest)
    unique_styles: list[str] = []
    style_seen: set[str] = set()
    articles: list[str] = []
    toc: list[str] = []
    source_table_count = 0
    source_body_hashes: list[dict[str, Any]] = []
    for state in states:
        for case in state.cases:
            document = read_text(case.winner_html)
            styles, title, body = extract_html_parts(document)
            for style in styles:
                normalized = style.strip()
                if normalized not in style_seen:
                    style_seen.add(normalized)
                    unique_styles.append(normalized)
            table_count = len(re.findall(r"<table\b", body, flags=re.IGNORECASE))
            source_table_count += table_count
            anchor = f"winner-{state.state.lower()}-{case.period.lower()}-{case.result}"
            toc.append(
                f'<li><a href="#{anchor}">{html.escape(state.state)} {html.escape(case.period)} {html.escape(case.result)}</a></li>'
            )
            rel = repo_relative(case.winner_html)
            external_rel = case.winner_html.relative_to(external_root).as_posix()
            artifact = artifact_map.get(external_rel, {})
            source_paths = artifact.get("source_paths", [])
            if isinstance(source_paths, dict):
                source_paths = list(source_paths.values())
            provenance = ", ".join(str(item) for item in source_paths) or "See external bundle manifest"
            articles.append(
                "\n".join(
                    [
                        f'<article class="stacked-winner-report" id="{anchor}" data-state="{html.escape(state.state)}" data-period="{html.escape(case.period)}" data-result="{html.escape(case.result)}">',
                        '<header class="outcome-banner">',
                        f"<h1>{html.escape(state.state)} - {html.escape(case.period)} {html.escape(case.result)}</h1>",
                        f"<p><strong>Original title:</strong> {html.escape(title)}</p>",
                        f"<p><strong>Claim class:</strong> {html.escape(str(artifact.get('claim_class', 'POST_RESULT_STRING_TABLE_FORENSIC')))}</p>",
                        f"<p><strong>Packaged source:</strong> <code>{html.escape(rel)}</code></p>",
                        f"<p><strong>Source SHA-256:</strong> <code>{sha256(case.winner_html)}</code></p>",
                        f"<p><strong>Corrected-table provenance:</strong> <code>{html.escape(provenance)}</code></p>",
                        f"<p><strong>Source table count:</strong> {table_count}</p>",
                        '<p class="boundary">Post-result research artifact. This winner overlay receives zero predictive credit.</p>',
                        '<p><a href="#package-top">Return to package index</a></p>',
                        "</header>",
                        '<div class="source-body">',
                        body,
                        "</div>",
                        "</article>",
                    ]
                )
            )
            source_body_hashes.append(
                {
                    "state": state.state,
                    "period": case.period,
                    "result": case.result,
                    "source_path": rel,
                    "source_sha256": sha256(case.winner_html),
                    "source_table_count": table_count,
                }
            )

    package_css = """
html { scroll-behavior: smooth; }
*, *::before, *::after { box-sizing: border-box; }
body { background: #f3f0e8; color: #17211d; }
.package-header { width: 100%; max-width: none; margin: 0 0 28px; padding: 24px; background: #fffdf6; border: 3px solid #203b35; }
.package-header h1 { margin-top: 0; color: #203b35; }
.package-header ul { columns: 2; column-gap: 32px; }
.package-header .boundary { background: #f9e3b7; border-left: 6px solid #a65f16; padding: 12px; font-weight: 700; }
.stacked-winner-report { width: 100%; max-width: none; margin: 34px 0; padding: 18px; background: white; border: 3px solid #203b35; box-shadow: 0 6px 20px rgba(0,0,0,.12); }
.outcome-banner { margin: -18px -18px 22px; padding: 18px 24px; color: #fdfcf7; background: #203b35; }
.outcome-banner h1 { margin: 0 0 8px; color: #fff; }
.outcome-banner p { margin: 4px 0; }
.outcome-banner code { color: #fff7ce; overflow-wrap: anywhere; }
.outcome-banner a { color: #fff7ce; }
.outcome-banner .boundary { margin-top: 10px; padding: 8px; color: #271d05; background: #f9e3b7; }
.source-body { width: 100%; max-width: none; overflow: visible; }
@media print { .stacked-winner-report { break-before: page; box-shadow: none; } }
@media (max-width: 900px) { .package-header ul { columns: 1; } .stacked-winner-report { margin: 18px 0; border-left: 0; border-right: 0; } }
""".strip()
    all_styles = "\n\n".join(f"<style>\n{style}\n</style>" for style in unique_styles)
    document = "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="en">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f"<title>{html.escape(date)} Gold Day - Stacked Corrected Winner Outputs</title>",
            all_styles,
            f"<style>\n{package_css}\n</style>",
            "</head>",
            "<body>",
            '<header class="package-header" id="package-top">',
            f"<h1>{html.escape(date)} Gold Day - Stacked Corrected Winner Outputs</h1>",
            "<p>Twenty-eight source winner-forensic bodies are preserved in state, Midday, Evening order with hash-pinned provenance.</p>",
            '<p class="boundary">Every section is result-aware research evidence. These overlays do not receive predictive credit and must not be used to inflate the frozen predictive record.</p>',
            "<ul>",
            *toc,
            "</ul>",
            "</header>",
            *articles,
            "</body>",
            "</html>",
        ]
    )
    receipt = {
        "article_count": len(articles),
        "deduplicated_source_style_block_count": len(unique_styles),
        "source_table_count": source_table_count,
        "source_bodies": source_body_hashes,
    }
    return document, receipt


def frozen_backlog(date: str) -> str:
    items = [
        (
            "EZV2-001",
            "Preserve V1 As The Matched Baseline",
            "Freeze the current 28-case predictive and result-aware artifacts. Every V2 experiment must report matched width, burden, and case coverage against this exact baseline.",
            "Prevents retrospective edits from being mistaken for predictive improvement.",
        ),
        (
            "EZV2-002",
            "Separate The Four Conversion Stages",
            "Maintain distinct ledgers for string availability, territory selection, AUX reinforcement, and final combination-product formation before outcome evaluation.",
            "Makes the first real loss visible instead of collapsing recognition, ranking, translation, and emission into one miss.",
        ),
        (
            "EZV2-003",
            "Complete Zone 1, Zone 2, And Zone 3 Candidate Ledgers",
            "Preserve all identity-bearing candidates and coordinates in Zones 1 and 2. Formalize Zone 3 survivor, bridge, maturity, and frontier thresholds without target-conditioned stopping.",
            "The Gold Day shows high territory availability but current top-N compression loses most outcomes.",
        ),
        (
            "EZV2-004",
            "Use Identity-Specific Ledgers",
            "Keep literal, canonical box, ordered VTRAC lane, boxed-VTRAC index, pair orientation, double family, and positional evidence separate until an explicit typed join.",
            "These relations overlap and cannot be treated as independent votes.",
        ),
        (
            "EZV2-005",
            "Rank Boxed-VTRAC Territories Explicitly",
            "Produce a complete candidate-symmetric VTRAC index ranking with competitors, support vectors, prevalence, candidate burden, and optional full-index fallback products.",
            "A trapped winning VTRAC neighborhood is a valuable bounded product even when canonical or order resolution remains incomplete.",
        ),
        (
            "EZV2-006",
            "Add A Pathway-State Tracker",
            "Track each candidate through PRESENT, MATURE, SELECTED, AUX_REINFORCED, TRANSLATED, EMITTED, WITHHELD, DECAY_OPEN, and CONVEYED states with lineage receipts.",
            "Prevents strong available routes from disappearing silently between extraction and final products.",
        ),
        (
            "EZV2-007",
            "Replace Opaque Score Compression With Merit Vectors",
            "Expose locked verticals, frontier persistence, bridge behavior, cross-variant support, consensus context, reduction survival, AUX roles, prevalence burden, and contradiction flags as separate fields.",
            "Supports rank-depth curves and auditable filters without pretending heterogeneous evidence is calibrated.",
        ),
        (
            "EZV2-008",
            "Build Typed Translation Bundles",
            "Generate explicit products for VTRAC-to-canonical, canonical-to-order, canonical x ordered-lane, pair-oriented family filtering, and abstention when a bridge is unsupported.",
            "The dominant issue is not raw availability alone; it is loss while translating territory into affordable box and straight products.",
        ),
        (
            "EZV2-009",
            "Correct Related-VTRAC Pair Orientation",
            "Enumerate every declared front, back, and end-cap orientation and every legal VTRAC-relative alternative before ranking. Never retain only the target-revealed orientation.",
            "Makes advanced straight-pathway analysis candidate-symmetric and testable.",
        ),
        (
            "EZV2-010",
            "Preserve Three-Permutation Double Products",
            "When a repeated digit plus key digit is selected, retain all three legal straight permutations unless a frozen order selector narrows them.",
            "Avoids discarding the system's strongest repeated-digit advantage during combination formation.",
        ),
        (
            "EZV2-011",
            "Preserve Qualified Non-Emitted Routes",
            "Create a shadow portfolio for high-merit routes that current gates withhold, including the Florida 383 and Virginia 188 regression cases.",
            "Distinguishes route discovery quality from a faulty emission gate.",
        ),
        (
            "EZV2-012",
            "Test AUX CORE With Controlled Shadow Arms",
            "Compare string-only, AUX-only, joined, and shuffled-AUX arms at matched width. Keep Positional role-aware for ordering, pair, mirror, contradiction, and VTRAC-territory support.",
            "Measures whether AUX adds real narrowing value instead of post-hoc narrative support.",
        ),
        (
            "EZV2-013",
            "Apply Board-Prevalence Controls",
            "Measure state-period specificity and down-weight ubiquitous candidates such as 688 and 668 unless independent local evidence exceeds the baseline prevalence burden.",
            "Prevents common candidates from appearing to be state-specific discoveries.",
        ),
        (
            "EZV2-014",
            "Use Candidate-Qualified Opportunity Labels",
            "Require explicit candidate sets, widths, and evidence thresholds before labels such as HIGH_STRAIGHT_OPPORTUNITY or HIGH_BOX_OPPORTUNITY are actionable.",
            "Opportunity labels must describe a reproducible product, not a broad qualitative environment.",
        ),
        (
            "EZV2-015",
            "Add Plain-Language Product Labels",
            "Report winning VTRAC territory trapped, actual winning digits in any order, correct VTRAC positional lane, and exact literal straight alongside technical terms.",
            "Keeps analytical meaning clear without changing canonical machine identities.",
        ),
        (
            "EZV2-016",
            "Instrument The First-Loss Funnel",
            "Count candidate survival and burden at recognition, maturity, territory rank, canonical translation, ordered-lane intersection, AUX join, emission, and decay stages.",
            "Turns the current 1/28 frozen capture result into an actionable conversion diagnosis.",
        ),
        (
            "EZV2-017",
            "Enforce Renderer And Secondary-Scan Parity",
            "Run candidate-symmetric literal and ordered-VTRAC recognition checks and classify unsupported identities such as 000 explicitly rather than silently coercing them.",
            "Thirteen Gold Day cases contain renderer-versus-secondary-recognition gaps.",
        ),
        (
            "EZV2-018",
            "Refresh Evening Evidence After Midday",
            "Create a separately labeled post-Midday snapshot before Evening selection and compare it with the current no-refresh control arm.",
            "The current Evening analysis intentionally uses a pre-day snapshot and may omit same-day progression information.",
        ),
        (
            "EZV2-019",
            "Keep Decay And Carryover Experimental",
            "Rebuild future structural evidence at each offset, cap persistence, preserve physical-event de-duplication, and keep bonus-ball inventory non-crediting until jurisdiction rules are verified.",
            "A bounded carry window is promising but cannot reuse a static winner-aware pathway as if it remained predictive.",
        ),
        (
            "EZV2-020",
            "Require Holdouts And Negative Controls",
            "Test every selector on additional complete Gold Days with matched-width random controls, shuffled joins, candidate burden, rank-depth efficiency, and untouched holdouts.",
            "March 9 is an in-sample reverse-engineering cohort, not proof of live lift or profitability.",
        ),
        (
            "EZV2-021",
            "Defer Runtime And Template Promotion",
            "Do not modify Analysis Arena synthesis, template execution, state allocation, scoreboard, bankroll, Profit Horns, or production combination forming until a shadow arm passes acceptance criteria.",
            "Keeps this extraction-zone study separate from the checkpointed template workflow and prevents another broad development detour.",
        ),
    ]
    return "\n".join(
        [
            f"# {date} Frozen Extraction V2 Optimization Backlog",
            "",
            "Status for every item: `FROZEN_PENDING_EXTERNAL_REVIEW`.",
            "",
            "This document preserves the complete proposed improvement set before ChatGPT Pro review. It is a backlog, not an implementation claim. No runtime, template, Analysis Arena, scoring, ranking, or combination-forming behavior was changed while creating it.",
            "",
            "## Acceptance Rule",
            "",
            "An item may move from frozen backlog to a shadow experiment only when it has a deterministic selector, complete candidate denominator, explicit identity and width, matched V1 baseline, negative control, and holdout plan. Promotion into runtime requires evidence from more than this in-sample Gold Day.",
            "",
            "## Frozen Items",
            "",
            md_table(
                ["ID", "Title", "Proposed change", "Why it matters", "Status"],
                [
                    [md_code(item_id), title, change, reason, md_code("FROZEN_PENDING_EXTERNAL_REVIEW")]
                    for item_id, title, change, reason in items
                ],
            ),
            "",
            "## Explicitly Out Of Scope",
            "",
            "- Retrofitting post-result discoveries into the frozen predictive record.",
            "- Claiming that the 92.9% result-aware zone territory rate is a predictive hit rate.",
            "- Treating raw relation rows, variants, or tools as independent votes.",
            "- Rebuilding the template workflow during extraction-zone V2 design.",
            "- Implementing profitability, bankroll, state allocation, or live-play policy from one in-sample day.",
        ]
    )


def start_here(
    date: str,
    states: Sequence[StateSource],
    payloads: dict[str, Any],
    coverage: dict[str, dict[str, int]],
) -> str:
    post = payloads["post_result_synthesis"]
    return "\n".join(
        [
            f"# {date} ChatGPT Pro Deep Review Package",
            "",
            "This package consolidates the complete first Gold Day extraction-zone review into three primary scrollable artifacts plus a frozen optimization backlog. It was built from existing analyses and corrected outputs without changing any source, runtime, template, score, rank, or combination-forming behavior.",
            "",
            "## Recommended Attachment Order",
            "",
            "1. `01_GOLD_DAY_STATE_REPORTS_STACKED.md`: all 14 state reports, each containing full frozen predictive analysis, both full winner-aware autopsies, straight routes, AUX conversion summaries, decay, doubles, renderer gaps, and source provenance.",
            "2. `02_GOLD_DAY_WINNER_OUTPUTS_STACKED.html`: all 28 corrected winner/VTRAC HTML bodies in one scrollable file, with source hashes and state/draw banners.",
            "3. `03_AUX_CORE_GOLD_DAY_STACKED.md`: all 14 full frozen ten-block AUX CORE reports plus all 28 post-result conversion joins.",
            "4. `04_FROZEN_EXTRACTION_V2_OPTIMIZATION_BACKLOG.md`: the locked proposed V2 repair/test set for critique before implementation.",
            "",
            "Individual state reports are also available under `states/`; individual AUX reports are under `aux_core_states/`.",
            "",
            "## Non-Negotiable Evidence Boundary",
            "",
            "- Frozen predictive analysis is the only layer eligible for predictive credit.",
            "- Winner HTML, winner-origin scans, straight autopsies, conversion diagnoses, and AUX winner joins are result-aware reverse engineering.",
            "- Post-result analysis is intentionally valuable for discovering repeating pathways and designing harness tests, but its availability counts cannot be reported as predictive hit rates.",
            "- Exact, canonical, ordered-VTRAC, and boxed-VTRAC relations overlap and often share the same root cell/window. They are not independent votes.",
            "",
            "## Gold Day Inventory",
            "",
            md_table(
                ["Item", "Count"],
                [
                    ["States", len(states)],
                    ["Outcomes", sum(len(state.cases) for state in states)],
                    ["Frozen predictive captures", sum(1 for row in payloads["immediate"] if row.get("predictive_credit_label") != "PREDICTIVE_MISS")],
                    ["Corrected whole-table boxed-VTRAC availability", post["raw_relation_case_coverage"]["BOXED_VTRAC"]],
                    ["Corrected whole-table canonical-box availability", post["raw_relation_case_coverage"]["CANONICAL_BOX"]],
                    ["Corrected whole-table ordered-VTRAC availability", post["raw_relation_case_coverage"]["ORDERED_VTRAC"]],
                    ["Corrected whole-table exact-literal availability", post["raw_relation_case_coverage"]["EXACT_LITERAL"]],
                    ["Zone 1/2 boxed-VTRAC availability, any variant", coverage["any_variant"]["BOXED_VTRAC"]],
                    ["Zone 1/2 canonical-box availability, any variant", coverage["any_variant"]["CANONICAL_BOX"]],
                    ["Zone 1/2 ordered-VTRAC availability, any variant", coverage["any_variant"]["ORDERED_VTRAC"]],
                    ["Zone 1/2 exact-literal availability, any variant", coverage["any_variant"]["EXACT_LITERAL"]],
                    ["Renderer/secondary recognition gap cases", len(post.get("renderer_recognition_gap_cases", []))],
                    ["Doubles, mirror doubles, or triples", post["doubles_summary"]["doubles_mirror_or_triple_events"]],
                    ["Decay channel observations", post["decay_summary"]["channel_observations"]],
                    ["Qualifying core convey rows", post["decay_summary"]["core_convey_rows"]],
                ],
            ),
            "",
            "The central finding is a conversion gap: corrected result-aware scans frequently contain winning VTRAC territory and often the canonical boxed winner, while the frozen emitted portfolios captured only one outcome. External review should therefore focus on candidate-symmetric selection, territory ranking, identity translation, order resolution, product width, and emission gates rather than dismissing the underlying string evidence or inflating it into predictive success.",
            "",
            "## Requested ChatGPT Pro Review",
            "",
            "1. Verify that the predictive/post-result boundary is maintained consistently in every state.",
            "2. Identify which repeated extraction-zone structures are genuinely candidate-symmetric and which are target-conditioned observations.",
            "3. Diagnose the dominant loss stage: recognition, top-N compression, VTRAC territory selection, canonical translation, order resolution, AUX narrowing, or final emission.",
            "4. Review whether boxed-VTRAC fallback, canonical x ordered-lane products, pair orientation, double three-permutation products, and qualified non-emitted routes deserve controlled shadow arms.",
            "5. Audit AUX CORE for real incremental narrowing value using string-only, AUX-only, joined, and shuffled controls at matched width.",
            "6. Critique the frozen V2 backlog: mark items `ACCEPT`, `REVISE`, `DEFER`, or `REJECT`, and name any missing acceptance test.",
            "7. Return a prioritized plan containing accepted findings, corrections, missing analyses, exact V2 experiments, required denominators, and holdout criteria. Do not recommend runtime promotion directly from this in-sample day.",
            "",
            "## Integrity Files",
            "",
            "- `05_PACKAGE_MANIFEST.json`: machine-readable input/output paths, SHA-256 hashes, result matrix, draw-source receipts, and validation metrics.",
            "- `05_PACKAGE_MANIFEST.csv`: compact artifact inventory.",
            "- `VALIDATION_RECEIPT.md`: human-readable build and verification checks.",
        ]
    )


def validate_source_immutability(source_registry: dict[str, dict[str, Any]]) -> None:
    changed: list[str] = []
    for entry in source_registry.values():
        path = REPO_ROOT / entry["path"]
        if not path.is_file() or path.stat().st_size != entry["bytes"] or sha256(path) != entry["sha256"]:
            changed.append(entry["path"])
    if changed:
        raise RuntimeError("Source artifacts changed during build: " + ", ".join(changed))


def validate_generated_package(
    package_root: Path,
    states: Sequence[StateSource],
    html_receipt: dict[str, Any],
    source_registry: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    state_files = sorted((package_root / "states").glob("*/COMPREHENSIVE_STATE_REPORT.md"))
    aux_files = sorted((package_root / "aux_core_states").glob("*/AUX_CORE_STATE_REPORT.md"))
    expected_states = [state.state for state in states]
    if [path.parent.name for path in state_files] != expected_states:
        raise ValueError("Generated state-report inventory does not match source states")
    if [path.parent.name for path in aux_files] != expected_states:
        raise ValueError("Generated AUX state-report inventory does not match source states")

    for state, path in zip(states, state_files):
        text = read_text(path)
        if text.count("STATE_POST_RESULT_AUTOPSY") != 4:
            # Each of two sections has SOURCE and SOURCE_END markers.
            raise ValueError(f"{state.state} report does not contain two complete autopsies")
        if "STATE_PREDICTIVE_ANALYSIS" not in text:
            raise ValueError(f"{state.state} report is missing predictive analysis")
        if demote_markdown(read_text(state.predictive_md), 2) not in text:
            raise ValueError(f"{state.state} predictive narrative was not preserved in full")
        for case in state.cases:
            if demote_markdown(read_text(case.post_md), 2) not in text:
                raise ValueError(
                    f"{state.state} {case.period} post-result narrative was not preserved in full"
                )

    for state, path in zip(states, aux_files):
        text = read_text(path)
        if demote_markdown(read_text(state.aux_pre_md), 2) not in text:
            raise ValueError(f"{state.state} AUX pre-result narrative was not preserved in full")
        for case in state.cases:
            join = section_from_heading(
                read_text(case.aux_post_md), "Post-Result Reverse-Engineering Join"
            )
            if demote_markdown(join, 2) not in text:
                raise ValueError(
                    f"{state.state} {case.period} AUX result join was not preserved in full"
                )

    stacked = read_text(package_root / "01_GOLD_DAY_STATE_REPORTS_STACKED.md")
    if stacked.count("<!-- STATE_REPORT_START") != 14:
        raise ValueError("Stacked state report does not contain 14 state sections")
    aux_stack = read_text(package_root / "03_AUX_CORE_GOLD_DAY_STACKED.md")
    if aux_stack.count("<!-- AUX_STATE_REPORT_START") != 14:
        raise ValueError("Stacked AUX report does not contain 14 state sections")
    winner_html = read_text(package_root / "02_GOLD_DAY_WINNER_OUTPUTS_STACKED.html")
    article_count = len(re.findall(r'<article class="stacked-winner-report"', winner_html))
    table_count = len(re.findall(r"<table\b", winner_html, flags=re.IGNORECASE))
    if article_count != 28:
        raise ValueError(f"Stacked winner HTML has {article_count} articles, expected 28")
    if table_count != html_receipt["source_table_count"]:
        raise ValueError(
            f"Stacked winner HTML table count {table_count} != source total {html_receipt['source_table_count']}"
        )
    ids = re.findall(r'\bid="([^"]+)"', winner_html, flags=re.IGNORECASE)
    if len(ids) != len(set(ids)):
        raise ValueError("Stacked winner HTML contains duplicate IDs")
    if re.search(r"<script\b|<link\b", winner_html, flags=re.IGNORECASE):
        raise ValueError("Stacked winner HTML unexpectedly contains script or link dependencies")
    verbatim_body_count = 0
    for state in states:
        for case in state.cases:
            _, _, body = extract_html_parts(read_text(case.winner_html))
            if body not in winner_html:
                raise ValueError(
                    f"Stacked winner HTML does not preserve {case.case_id} body verbatim"
                )
            verbatim_body_count += 1

    backlog = read_text(package_root / "04_FROZEN_EXTRACTION_V2_OPTIMIZATION_BACKLOG.md")
    backlog_ids = set(re.findall(r"EZV2-\d{3}", backlog))
    if len(backlog_ids) != 21:
        raise ValueError(f"Frozen backlog has {len(backlog_ids)} unique IDs, expected 21")
    validate_source_immutability(source_registry)
    return {
        "state_report_count": len(state_files),
        "aux_state_report_count": len(aux_files),
        "predictive_report_count": len(states),
        "post_result_autopsy_count": sum(len(state.cases) for state in states),
        "winner_html_article_count": article_count,
        "winner_html_table_count": table_count,
        "winner_html_unique_id_count": len(ids),
        "winner_html_external_dependency_count": 0,
        "winner_html_verbatim_body_count": verbatim_body_count,
        "full_predictive_narrative_count": len(states),
        "full_post_result_narrative_count": sum(len(state.cases) for state in states),
        "full_aux_pre_result_narrative_count": len(states),
        "full_aux_post_result_join_count": sum(len(state.cases) for state in states),
        "frozen_backlog_item_count": len(backlog_ids),
        "source_artifact_count": len(source_registry),
        "source_immutability_verified": True,
    }


def validation_receipt(
    date: str,
    validation: dict[str, Any],
    draw_receipts: Sequence[dict[str, Any]],
    coverage: dict[str, dict[str, int]],
    html_receipt: dict[str, Any],
) -> str:
    draw_summary = Counter(item["row_count"] for item in draw_receipts)
    return "\n".join(
        [
            f"# {date} Deep Review Package Validation Receipt",
            "",
            "## Result",
            "",
            "`PASS`",
            "",
            "## Structural Checks",
            "",
            md_table(
                ["Check", "Observed", "Expected", "Status"],
                [
                    ["State reports", validation["state_report_count"], 14, "PASS"],
                    ["AUX state reports", validation["aux_state_report_count"], 14, "PASS"],
                    ["Frozen predictive reports embedded", validation["predictive_report_count"], 14, "PASS"],
                    ["Result-aware autopsies embedded", validation["post_result_autopsy_count"], 28, "PASS"],
                    ["Full predictive narratives preserved", validation["full_predictive_narrative_count"], 14, "PASS"],
                    ["Full post-result narratives preserved", validation["full_post_result_narrative_count"], 28, "PASS"],
                    ["Full AUX pre-result narratives preserved", validation["full_aux_pre_result_narrative_count"], 14, "PASS"],
                    ["Full AUX post-result joins preserved", validation["full_aux_post_result_join_count"], 28, "PASS"],
                    ["Winner HTML articles", validation["winner_html_article_count"], 28, "PASS"],
                    ["Winner HTML bodies preserved verbatim", validation["winner_html_verbatim_body_count"], 28, "PASS"],
                    ["Winner HTML tables", validation["winner_html_table_count"], html_receipt["source_table_count"], "PASS"],
                    ["External script/link dependencies", validation["winner_html_external_dependency_count"], 0, "PASS"],
                    ["Frozen V2 backlog items", validation["frozen_backlog_item_count"], 21, "PASS"],
                    ["Source artifacts unchanged", validation["source_immutability_verified"], True, "PASS"],
                ],
            ),
            "",
            "## Zone-Coverage Recalculation",
            "",
            md_table(
                ["Relation inside Zone 1 or 2", "Any variant", "Target or Combined"],
                [
                    [relation, coverage["any_variant"][relation], coverage["target_or_combined"][relation]]
                    for relation in ("BOXED_VTRAC", "CANONICAL_BOX", "ORDERED_VTRAC", "EXACT_LITERAL")
                ],
            ),
            "",
            "The calculation reads every post-result autopsy's candidate-symmetric secondary scan and requires an occurrence explicitly tagged Zone 1 or Zone 2. It is retrospective availability, not predictive credit.",
            "",
            "## Cleaned Draw Source Gate",
            "",
            f"Validated **{len(draw_receipts)}** `data/cleaned/draws/*_draws.csv` files across 14 states and three variants. Row-count distribution: "
            + ", ".join(f"{rows} rows={count} files" for rows, count in sorted(draw_summary.items()))
            + ". These files are validation references only; the package does not recompute analytics from them.",
            "",
            "## HTML Preservation",
            "",
            f"The stacked HTML contains **{html_receipt['article_count']}** source bodies, **{html_receipt['source_table_count']}** source tables, and **{html_receipt['deduplicated_source_style_block_count']}** deduplicated source style blocks. Every article records its original source path and SHA-256.",
            "",
            "## Boundary Checks",
            "",
            "- Predictive and post-result sections remain visibly separated.",
            "- Full state narratives are preserved rather than replaced by short summaries.",
            "- AUX full pre-result evidence appears once per state; winner joins remain explicitly post-result.",
            "- Large decay negatives are preserved in the source JSON while reports retain route denominators and every qualifying convey row.",
            "- No existing analytical artifact was modified during generation.",
            "- No runtime, template, Analysis Arena, scoring, ranking, or combination-forming code was changed.",
        ]
    )


def output_entry(package_root: Path, path: Path, role: str) -> dict[str, Any]:
    return {
        "path": path.relative_to(package_root).as_posix(),
        "role": role,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def write_manifest_csv(
    path: Path,
    sources: Sequence[dict[str, Any]],
    outputs: Sequence[dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["kind", "role", "state", "period", "result", "path", "bytes", "sha256"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in sources:
            writer.writerow(
                {
                    "kind": "SOURCE",
                    "role": item.get("role", ""),
                    "state": item.get("state", ""),
                    "period": item.get("period", ""),
                    "result": item.get("result", ""),
                    "path": item["path"],
                    "bytes": item["bytes"],
                    "sha256": item["sha256"],
                }
            )
        for item in outputs:
            writer.writerow(
                {
                    "kind": "OUTPUT",
                    "role": item.get("role", ""),
                    "state": "",
                    "period": "",
                    "result": "",
                    "path": item["path"],
                    "bytes": item["bytes"],
                    "sha256": item["sha256"],
                }
            )


def build_package(
    date: str,
    core_root: Path,
    external_root: Path,
    aux_root: Path,
    output_dir: Path,
    replace_output: bool = False,
) -> dict[str, Any]:
    states, source_registry, payloads, metadata = discover_sources(
        date, core_root, external_root, aux_root
    )
    draw_receipts = validate_draw_sources(states)
    coverage = zone_coverage(states)
    if output_dir.exists() and not replace_output:
        raise FileExistsError(
            f"Refusing to replace existing output: {repo_relative(output_dir)}"
        )
    if output_dir.exists():
        verify_existing_package(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = output_dir.parent / f".{output_dir.name}.tmp"
    if temp_dir.exists():
        raise FileExistsError(f"Temporary output already exists: {repo_relative(temp_dir)}")
    temp_dir.mkdir()
    try:
        state_reports: dict[str, str] = {}
        aux_reports: dict[str, str] = {}
        for state in states:
            state_report = build_state_report(date, state, payloads, source_registry)
            aux_report = build_aux_state_report(date, state)
            state_reports[state.state] = state_report
            aux_reports[state.state] = aux_report
            write_text(
                temp_dir / "states" / state.state / "COMPREHENSIVE_STATE_REPORT.md",
                state_report,
            )
            write_text(
                temp_dir / "aux_core_states" / state.state / "AUX_CORE_STATE_REPORT.md",
                aux_report,
            )

        write_text(
            temp_dir / "01_GOLD_DAY_STATE_REPORTS_STACKED.md",
            build_state_stack(date, states, state_reports, payloads, metadata, coverage),
        )
        stacked_html, html_receipt = build_stacked_winner_html(
            date, states, metadata["external_manifest"], external_root
        )
        write_text(temp_dir / "02_GOLD_DAY_WINNER_OUTPUTS_STACKED.html", stacked_html)
        write_text(
            temp_dir / "03_AUX_CORE_GOLD_DAY_STACKED.md",
            build_aux_stack(date, states, aux_reports),
        )
        write_text(
            temp_dir / "04_FROZEN_EXTRACTION_V2_OPTIMIZATION_BACKLOG.md",
            frozen_backlog(date),
        )
        write_text(temp_dir / "00_START_HERE.md", start_here(date, states, payloads, coverage))

        validation = validate_generated_package(
            temp_dir, states, html_receipt, source_registry
        )
        write_text(
            temp_dir / "VALIDATION_RECEIPT.md",
            validation_receipt(date, validation, draw_receipts, coverage, html_receipt),
        )
        validate_source_immutability(source_registry)

        role_by_name = {
            "00_START_HERE.md": "review_guide",
            "01_GOLD_DAY_STATE_REPORTS_STACKED.md": "stacked_state_analysis",
            "02_GOLD_DAY_WINNER_OUTPUTS_STACKED.html": "stacked_corrected_winner_html",
            "03_AUX_CORE_GOLD_DAY_STACKED.md": "stacked_aux_core",
            "04_FROZEN_EXTRACTION_V2_OPTIMIZATION_BACKLOG.md": "frozen_v2_backlog",
            "VALIDATION_RECEIPT.md": "validation_receipt",
        }
        generated: list[dict[str, Any]] = []
        for path in sorted(temp_dir.rglob("*")):
            if not path.is_file() or path.name.startswith("05_PACKAGE_MANIFEST"):
                continue
            role = role_by_name.get(path.name)
            if not role and path.name == "COMPREHENSIVE_STATE_REPORT.md":
                role = "individual_state_analysis"
            elif not role and path.name == "AUX_CORE_STATE_REPORT.md":
                role = "individual_aux_core_state_report"
            generated.append(output_entry(temp_dir, path, role or "generated_artifact"))

        source_entries = sorted(source_registry.values(), key=lambda item: item["path"])
        manifest_csv = temp_dir / "05_PACKAGE_MANIFEST.csv"
        write_manifest_csv(manifest_csv, source_entries, generated)
        generated_with_csv = [
            *generated,
            output_entry(temp_dir, manifest_csv, "package_manifest_csv"),
        ]
        manifest = {
            "schema_version": "gold_day_chatgpt_pro_deep_review_package_v1",
            "analysis_date": date,
            "package_role": "EXTERNAL_DEEP_REVIEW__NO_RUNTIME_CHANGE",
            "claim_boundary": (
                "Frozen predictive sections are the only predictive-credit source. Winner HTML, "
                "post-result autopsies, AUX winner joins, decay diagnoses, and V2 proposals are "
                "retrospective research evidence and receive zero predictive credit."
            ),
            "source_roots": {
                "core_extraction_review": repo_relative(core_root),
                "external_review_bundle": repo_relative(external_root),
                "aux_core": repo_relative(aux_root),
            },
            "counts": {
                **validation,
                "state_count": len(states),
                "case_count": sum(len(state.cases) for state in states),
                "cleaned_draw_validation_receipt_count": len(draw_receipts),
                "generated_artifact_count_excluding_json_manifest": len(generated_with_csv),
            },
            "zone_1_or_2_result_aware_coverage": coverage,
            "case_matrix": metadata["case_matrix"],
            "draw_source_validation": draw_receipts,
            "winner_html_receipt": html_receipt,
            "source_immutability": {
                "verified": True,
                "method": "SHA-256 and byte-size captured before build and rechecked before manifest write",
            },
            "source_artifacts": source_entries,
            "generated_artifacts": generated_with_csv,
            "manifest_integrity_policy": (
                "The JSON manifest does not hash itself. Every other package file, including the "
                "CSV manifest, is hash-pinned here."
            ),
        }
        write_json(temp_dir / "05_PACKAGE_MANIFEST.json", manifest)
        validate_source_immutability(source_registry)
        if replace_output:
            backup_dir = output_dir.parent / f".{output_dir.name}.previous"
            if backup_dir.exists():
                raise FileExistsError(
                    f"Controlled replacement backup already exists: {repo_relative(backup_dir)}"
                )
            os.replace(output_dir, backup_dir)
            try:
                os.replace(temp_dir, output_dir)
                verify_existing_package(output_dir)
            except Exception:
                if output_dir.exists():
                    failed_dir = output_dir.parent / f".{output_dir.name}.failed"
                    os.replace(output_dir, failed_dir)
                os.replace(backup_dir, output_dir)
                raise
            shutil.rmtree(backup_dir)
        else:
            os.replace(temp_dir, output_dir)
        verify_existing_package(output_dir)
        return manifest
    except Exception:
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        raise


def verify_existing_package(output_dir: Path) -> dict[str, Any]:
    manifest_path = require_file(output_dir / "05_PACKAGE_MANIFEST.json", "package manifest")
    manifest = read_json(manifest_path)
    errors: list[str] = []
    for item in manifest.get("source_artifacts", []):
        path = REPO_ROOT / item["path"]
        if not path.is_file():
            errors.append(f"missing source {item['path']}")
        elif path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            errors.append(f"source hash/size mismatch {item['path']}")
    for item in manifest.get("generated_artifacts", []):
        path = output_dir / item["path"]
        if not path.is_file():
            errors.append(f"missing output {item['path']}")
        elif path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            errors.append(f"output hash/size mismatch {item['path']}")

    stacked_path = output_dir / "01_GOLD_DAY_STATE_REPORTS_STACKED.md"
    aux_path = output_dir / "03_AUX_CORE_GOLD_DAY_STACKED.md"
    html_path = output_dir / "02_GOLD_DAY_WINNER_OUTPUTS_STACKED.html"
    if stacked_path.is_file() and read_text(stacked_path).count("<!-- STATE_REPORT_START") != 14:
        errors.append("stacked state report marker count is not 14")
    if aux_path.is_file() and read_text(aux_path).count("<!-- AUX_STATE_REPORT_START") != 14:
        errors.append("stacked AUX report marker count is not 14")
    if html_path.is_file():
        html_text = read_text(html_path)
        if len(re.findall(r'<article class="stacked-winner-report"', html_text)) != 28:
            errors.append("stacked winner HTML article count is not 28")
        expected_tables = manifest.get("winner_html_receipt", {}).get("source_table_count")
        actual_tables = len(re.findall(r"<table\b", html_text, flags=re.IGNORECASE))
        if expected_tables != actual_tables:
            errors.append(
                f"stacked winner HTML table count {actual_tables} != manifest {expected_tables}"
            )
        ids = re.findall(r'\bid="([^"]+)"', html_text, flags=re.IGNORECASE)
        if len(ids) != len(set(ids)):
            errors.append("stacked winner HTML contains duplicate IDs")
    if errors:
        raise RuntimeError("Package verification failed:\n- " + "\n- ".join(errors))
    return {
        "status": "PASS",
        "source_artifacts_verified": len(manifest.get("source_artifacts", [])),
        "generated_artifacts_verified": len(manifest.get("generated_artifacts", [])),
        "state_count": manifest.get("counts", {}).get("state_count"),
        "case_count": manifest.get("counts", {}).get("case_count"),
        "output_dir": repo_relative(output_dir),
    }


def validate_only(
    date: str, core_root: Path, external_root: Path, aux_root: Path
) -> dict[str, Any]:
    states, source_registry, payloads, _ = discover_sources(
        date, core_root, external_root, aux_root
    )
    draw_receipts = validate_draw_sources(states)
    coverage = zone_coverage(states)
    return {
        "status": "PASS",
        "state_count": len(states),
        "case_count": sum(len(state.cases) for state in states),
        "source_artifact_count": len(source_registry),
        "cleaned_draw_file_count": len(draw_receipts),
        "cleaned_draw_files": [
            {
                "state": item["state"],
                "variant": item["variant"],
                "path": item["path"],
                "row_count": item["row_count"],
            }
            for item in draw_receipts
        ],
        "zone_1_or_2_result_aware_coverage": coverage,
        "predictive_credit_counts": payloads["post_result_synthesis"].get(
            "predictive_credit_counts", {}
        ),
    }


def main() -> int:
    args = parse_args()
    ensure_repo_root()
    core_root = absolute(args.core_root)
    external_root = absolute(args.external_root)
    aux_root = absolute(args.aux_root)
    output_dir = absolute(args.output_dir)
    if args.validate_only and args.verify_output:
        raise ValueError("Choose either --validate-only or --verify-output")
    if args.replace_output and (args.validate_only or args.verify_output):
        raise ValueError("--replace-output is valid only when building")
    if args.verify_output:
        result = verify_existing_package(output_dir)
    elif args.validate_only:
        result = validate_only(args.date, core_root, external_root, aux_root)
    else:
        manifest = build_package(
            args.date,
            core_root,
            external_root,
            aux_root,
            output_dir,
            replace_output=args.replace_output,
        )
        result = {
            "status": "PASS",
            "output_dir": repo_relative(output_dir),
            "state_count": manifest["counts"]["state_count"],
            "case_count": manifest["counts"]["case_count"],
            "generated_artifact_count_excluding_json_manifest": manifest["counts"][
                "generated_artifact_count_excluding_json_manifest"
            ],
        }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - CLI boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
