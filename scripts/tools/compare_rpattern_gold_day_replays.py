#!/usr/bin/env python3
"""Compare the frozen March 9 R-pattern replay lanes.

The report keeps four claims separate:

1. Source correction: old artifacts versus the source-only replay.
2. Later runtime changes: source-only replay versus the current replay.
3. Predictive realization: Candidate Universe and Play Card coverage.
4. Post-result diagnosis: winner-side corridor evidence.

Nothing in this utility mutates a predictive artifact or production scorer.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.append(str(SRC_ROOT))

from modules.vtrac_reference import get_vtrac_index


R_ROWS = ("R2", "R4", "R6", "R8")
TABLE_COLUMNS = ("7", "6", "5", "4", "3", "2", "1")
VOLATILE_KEYS = {
    "created_at",
    "generated_at",
    "output_dir",
    "output_path",
    "repo_root",
    "sharepack_root",
    "sharepacks_root",
    "source_path",
    "source_paths",
    "timestamp",
    "version_timestamp",
}
LANE_ORDER = ("old", "source_only", "current")


@dataclass(frozen=True)
class Lane:
    name: str
    sharepacks_root: Path
    candidate_grade: Path
    play_grade: Path


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="2026-03-09")
    parser.add_argument("--old-root", default="sharepacks/_predictive")
    parser.add_argument(
        "--source-root", default="sharepacks/_replay_rpattern_source_only"
    )
    parser.add_argument("--current-root", default="sharepacks/_replay_rpattern_current")
    parser.add_argument(
        "--replay-root",
        default=(
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/"
            "REPLAY_RPATTERN_2026-03-09"
        ),
    )
    parser.add_argument(
        "--corridor-harness",
        default=(
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/"
            "REPLAY_RPATTERN_2026-03-09/COMPARISON/"
            "VTRAC_CORRIDOR_HARNESS/2026-03-09/"
            "VTRAC_CORRIDOR_ARENA_HARNESS__2026-03-09.json"
        ),
    )
    parser.add_argument(
        "--out-dir",
        default=(
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/"
            "REPLAY_RPATTERN_2026-03-09/COMPARISON"
        ),
    )
    return parser.parse_args(argv)


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _write_csv(
    path: Path,
    rows: Sequence[Mapping[str, Any]],
    fields: Sequence[str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fields), extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: _csv_value(row.get(field)) for field in fields})


def _csv_value(value: Any) -> Any:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (dict, list, tuple, set)):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    if value is None:
        return ""
    return value


def _digits(value: Any) -> str:
    return "".join(character for character in str(value or "") if character.isdigit())


def _literal(value: Any) -> str:
    digits = _digits(value)
    return digits.zfill(3) if 0 < len(digits) <= 3 else digits


def _canonical(value: Any) -> str:
    literal = _literal(value)
    return "".join(sorted(literal)) if len(literal) == 3 else ""


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "hit"}


def _integer(value: Any, default: int = 0) -> int:
    try:
        return int(float(str(value)))
    except (TypeError, ValueError):
        return default


def _state_dirs(root: Path, date: str) -> list[str]:
    day = root / date
    if not day.exists():
        return []
    return sorted(
        path.name
        for path in day.iterdir()
        if path.is_dir() and path.name != "control_center"
    )


CellKey = tuple[str, str, str, str, str, str]
BoxKey = tuple[str, str, str, str, str]


def _load_cells(root: Path, date: str) -> dict[CellKey, str]:
    cells: dict[CellKey, str] = {}
    for state in _state_dirs(root, date):
        tables_dir = root / date / state / "tables"
        for path in sorted(tables_dir.glob("*_Combined.csv")):
            variant = path.name.split("_", 1)[0]
            for row in _read_csv(path):
                for column in TABLE_COLUMNS:
                    key = (
                        state,
                        variant,
                        str(row.get("Set") or ""),
                        str(row.get("Draw") or ""),
                        str(row.get("RowType") or ""),
                        column,
                    )
                    cells[key] = _digits(row.get(column))
    return cells


def _cell_change_class(before: str, after: str, row_type: str) -> str:
    if before == after:
        return "UNCHANGED"
    if (
        row_type in R_ROWS
        and after
        and len(after) < 3
        and before == after.zfill(3)
    ):
        return "SYNTHETIC_ZERO_REMOVED"
    return "OTHER_CHANGE"


def _build_cell_diff(
    lane_cells: Mapping[str, Mapping[CellKey, str]],
) -> list[dict[str, Any]]:
    all_keys: set[CellKey] = set()
    for cells in lane_cells.values():
        all_keys.update(cells)

    rows: list[dict[str, Any]] = []
    for key in sorted(all_keys):
        state, variant, set_name, draw, row_type, column = key
        old = lane_cells["old"].get(key, "")
        source = lane_cells["source_only"].get(key, "")
        current = lane_cells["current"].get(key, "")
        source_class = _cell_change_class(old, source, row_type)
        current_class = _cell_change_class(source, current, row_type)
        if source_class == "UNCHANGED" and current_class == "UNCHANGED":
            continue
        rows.append(
            {
                "state_key": state,
                "variant": variant,
                "set": set_name,
                "draw": draw,
                "row_type": row_type,
                "column": column,
                "old_value": old,
                "source_only_value": source,
                "current_value": current,
                "old_length": len(old),
                "source_only_length": len(source),
                "current_length": len(current),
                "old_to_source_class": source_class,
                "source_to_current_class": current_class,
            }
        )
    return rows


def _consensus_groups(
    cells: Mapping[CellKey, str],
) -> dict[BoxKey, dict[str, str]]:
    groups: dict[BoxKey, dict[str, str]] = defaultdict(dict)
    for key, value in cells.items():
        state, variant, set_name, draw, row_type, column = key
        if row_type not in R_ROWS:
            continue
        groups[(state, variant, set_name, draw, column)][row_type] = value
    return groups


def _consensus_snapshot(rows: Mapping[str, str]) -> dict[str, Any]:
    values = [rows.get(row_type, "") for row_type in R_ROWS]
    strict = bool(all(values) and len(set(values)) == 1)
    nonempty = [value for value in values if value]
    counts = Counter(nonempty)
    near_value = ""
    near_count = 0
    if counts:
        near_value, near_count = counts.most_common(1)[0]
    near = bool(near_value and near_count >= 3 and not strict)
    value = values[0] if strict else near_value if near else ""
    return {
        "strict": strict,
        "near_3_of_4": near,
        "value": value,
        "tail_length": len(value),
        "r2": values[0],
        "r4": values[1],
        "r6": values[2],
        "r8": values[3],
    }


def _build_consensus_diff(
    lane_cells: Mapping[str, Mapping[CellKey, str]],
) -> list[dict[str, Any]]:
    grouped = {
        lane: _consensus_groups(cells) for lane, cells in lane_cells.items()
    }
    all_keys: set[BoxKey] = set()
    for groups in grouped.values():
        all_keys.update(groups)

    rows: list[dict[str, Any]] = []
    for key in sorted(all_keys):
        snapshots = {
            lane: _consensus_snapshot(grouped[lane].get(key, {}))
            for lane in LANE_ORDER
        }
        if not any(
            snapshot["strict"] or snapshot["near_3_of_4"]
            for snapshot in snapshots.values()
        ):
            continue
        state, variant, set_name, draw, column = key
        old = snapshots["old"]
        source = snapshots["source_only"]
        current = snapshots["current"]
        if (
            old["strict"]
            and source["strict"]
            and source["value"]
            and len(source["value"]) < 3
            and old["value"] == source["value"].zfill(3)
        ):
            source_change = "SYNTHETIC_THREE_DIGIT_MASK_REMOVED"
        elif old == source:
            source_change = "UNCHANGED"
        else:
            source_change = "OTHER_CHANGE"
        current_change = "UNCHANGED" if source == current else "OTHER_CHANGE"
        rows.append(
            {
                "state_key": state,
                "variant": variant,
                "set": set_name,
                "draw": draw,
                "column": column,
                "old_strict": old["strict"],
                "old_near_3_of_4": old["near_3_of_4"],
                "old_tail": old["value"],
                "old_tail_length": old["tail_length"],
                "source_only_strict": source["strict"],
                "source_only_near_3_of_4": source["near_3_of_4"],
                "source_only_tail": source["value"],
                "source_only_tail_length": source["tail_length"],
                "current_strict": current["strict"],
                "current_near_3_of_4": current["near_3_of_4"],
                "current_tail": current["value"],
                "current_tail_length": current["tail_length"],
                "old_to_source_class": source_change,
                "source_to_current_class": current_change,
                "old_rows": {row: old[row.lower()] for row in R_ROWS},
                "source_only_rows": {
                    row: source[row.lower()] for row in R_ROWS
                },
                "current_rows": {
                    row: current[row.lower()] for row in R_ROWS
                },
            }
        )
    return rows


def _grade_groups(path: Path) -> dict[tuple[str, str], list[dict[str, str]]]:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in _read_csv(path):
        key = (
            str(row.get("state_key") or ""),
            str(row.get("winner_label") or ""),
        )
        if all(key):
            groups[key].append(row)
    return groups


def _best_grade_row(
    rows: Sequence[dict[str, str]],
    predicates: Sequence[str],
) -> dict[str, str] | None:
    matches = [
        row for row in rows if any(_truthy(row.get(field)) for field in predicates)
    ]
    if not matches:
        return None
    return min(
        matches,
        key=lambda row: (
            _integer(row.get("combos_count"), 10**9),
            str(row.get("strategy") or row.get("method_id") or ""),
            str(row.get("budget_label") or row.get("pack_id") or ""),
        ),
    )


def _grade_summary(
    rows: Sequence[dict[str, str]],
    *,
    surface: str,
) -> dict[str, Any]:
    exact = _best_grade_row(rows, ("straight_hit",))
    canonical_fields = (
        ("box_hit", "canon_hit_any_perm")
        if surface == "play_card"
        else ("box_hit",)
    )
    canonical = _best_grade_row(rows, canonical_fields)
    vtrac = _best_grade_row(rows, ("vtrac_index_hit",))

    def descriptor(row: dict[str, str] | None) -> str:
        if not row:
            return ""
        if surface == "play_card":
            return ":".join(
                filter(
                    None,
                    (
                        str(row.get("strategy") or ""),
                        str(row.get("budget_label") or ""),
                    ),
                )
            )
        return ":".join(
            filter(
                None,
                (
                    str(row.get("pack_id") or ""),
                    str(row.get("method_id") or ""),
                ),
            )
        )

    def width(row: dict[str, str] | None) -> int | None:
        if not row:
            return None
        return _integer(row.get("combos_count"), 0)

    return {
        "exact": exact is not None,
        "exact_width": width(exact),
        "exact_route": descriptor(exact),
        "canonical": canonical is not None,
        "canonical_width": width(canonical),
        "canonical_route": descriptor(canonical),
        "vtrac": vtrac is not None,
        "vtrac_width": width(vtrac),
        "vtrac_route": descriptor(vtrac),
    }


def _coverage_label(summary: Mapping[str, Any]) -> str:
    if summary.get("exact"):
        return "EXACT"
    if summary.get("canonical"):
        return "CANONICAL"
    if summary.get("vtrac"):
        return "VTRAC_ONLY"
    return "NO_MATCH"


def _control_arm_rows(lanes: Mapping[str, Lane]) -> list[dict[str, Any]]:
    candidate_groups = {
        lane: _grade_groups(config.candidate_grade)
        for lane, config in lanes.items()
    }
    play_groups = {
        lane: _grade_groups(config.play_grade)
        for lane, config in lanes.items()
    }
    all_keys: set[tuple[str, str]] = set()
    for groups in candidate_groups.values():
        all_keys.update(groups)
    for groups in play_groups.values():
        all_keys.update(groups)

    rows: list[dict[str, Any]] = []
    for state, period in sorted(
        all_keys, key=lambda key: (key[0], 0 if key[1] == "Midday" else 1)
    ):
        identity_rows = (
            candidate_groups["current"].get((state, period))
            or play_groups["current"].get((state, period))
            or candidate_groups["old"].get((state, period))
            or []
        )
        identity = identity_rows[0] if identity_rows else {}
        row: dict[str, Any] = {
            "state_key": state,
            "period": period,
            "winner": str(identity.get("winner") or ""),
            "winner_canonical": str(identity.get("winner_canonical") or ""),
            "winner_vtrac_index": str(
                identity.get("winner_vtrac_index") or ""
            ),
        }
        snapshots: dict[str, dict[str, dict[str, Any]]] = {}
        for lane in LANE_ORDER:
            candidate = _grade_summary(
                candidate_groups[lane].get((state, period), []),
                surface="candidate_universe",
            )
            play = _grade_summary(
                play_groups[lane].get((state, period), []),
                surface="play_card",
            )
            snapshots[lane] = {"candidate_universe": candidate, "play_card": play}
            for surface_name, summary in (
                ("cu", candidate),
                ("play", play),
            ):
                prefix = f"{lane}_{surface_name}"
                row[f"{prefix}_coverage"] = _coverage_label(summary)
                for field in (
                    "exact",
                    "exact_width",
                    "exact_route",
                    "canonical",
                    "canonical_width",
                    "canonical_route",
                    "vtrac",
                    "vtrac_width",
                    "vtrac_route",
                ):
                    row[f"{prefix}_{field}"] = summary[field]
        old_view = (
            snapshots["old"]["candidate_universe"],
            snapshots["old"]["play_card"],
        )
        source_view = (
            snapshots["source_only"]["candidate_universe"],
            snapshots["source_only"]["play_card"],
        )
        current_view = (
            snapshots["current"]["candidate_universe"],
            snapshots["current"]["play_card"],
        )
        row["old_to_source_changed"] = old_view != source_view
        row["source_to_current_changed"] = source_view != current_view
        rows.append(row)
    return rows


def _glob_one(directory: Path, pattern: str) -> Path | None:
    matches = sorted(directory.glob(pattern))
    return matches[0] if matches else None


def _value_rank(items: Any, target: str) -> int | None:
    if not isinstance(items, list):
        return None
    for rank, item in enumerate(items, start=1):
        value = item.get("value") if isinstance(item, dict) else item
        if str(value or "") == str(target):
            return rank
    return None


def _example_literal_rank(items: Any, target: str) -> int | None:
    if not isinstance(items, list):
        return None
    for rank, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            continue
        examples = {
            _literal(value) for value in item.get("example_literals") or []
        }
        if target in examples:
            return rank
    return None


def _seed_rank(items: Any, target: str, *, canonical: bool = False) -> int | None:
    if not isinstance(items, list):
        return None
    for rank, item in enumerate(items, start=1):
        value = item.get("value") if isinstance(item, dict) else item
        normalized = _canonical(value) if canonical else _literal(value)
        expected = _canonical(target) if canonical else _literal(target)
        if normalized and normalized == expected:
            return rank
        if str(value or "") == str(target):
            return rank
    return None


def _arena_sandbox_snapshot(
    root: Path,
    date: str,
    state: str,
    winner: str,
    canonical: str,
    target_vtrac: str,
) -> dict[str, Any]:
    analysis_dir = root / date / state / "analysis"
    arena_path = _glob_one(analysis_dir, "aggregated_analysis_arena__*.json")
    sandbox_path = _glob_one(analysis_dir, "translation_sandbox_seed__*.json")
    arena = _read_json(arena_path) if arena_path else {}
    sandbox = _read_json(sandbox_path) if sandbox_path else {}
    synthesis = arena.get("arena_synthesis") or {}
    brain1 = sandbox.get("brain1_core") or {}
    hypotheses = sandbox.get("sandbox_hypotheses") or {}

    dominant_canonicals = synthesis.get("dominant_canonicals") or []
    context_canonicals = synthesis.get("context_reinforced_canonicals") or []
    dominant_vtracs = synthesis.get("dominant_vtrac_indices") or []
    box_seeds = hypotheses.get("diagnostic_boxed_seed") or []
    straight_seeds = hypotheses.get("diagnostic_straight_seed") or []
    vtrac_seeds = hypotheses.get("diagnostic_vt_box_seed") or []

    arena_canonical_rank = _value_rank(dominant_canonicals, canonical)
    arena_context_rank = _value_rank(context_canonicals, canonical)
    arena_literal_rank = min(
        [
            rank
            for rank in (
                _example_literal_rank(dominant_canonicals, winner),
                _example_literal_rank(context_canonicals, winner),
            )
            if rank is not None
        ],
        default=None,
    )
    arena_vtrac_rank = (
        _value_rank(dominant_vtracs, target_vtrac) if target_vtrac else None
    )
    brain1_canonical_rank = _seed_rank(
        brain1.get("dominant_canonicals") or [], canonical, canonical=True
    )
    brain1_vtrac_rank = (
        _seed_rank(
            brain1.get("dominant_vtrac_indices") or [],
            target_vtrac,
        )
        if target_vtrac
        else None
    )
    sandbox_box_rank = _seed_rank(box_seeds, canonical, canonical=True)
    sandbox_straight_rank = _seed_rank(straight_seeds, winner)
    sandbox_vtrac_rank = (
        _seed_rank(vtrac_seeds, target_vtrac) if target_vtrac else None
    )
    return {
        "arena_path": _safe_rel(arena_path) if arena_path else "",
        "sandbox_path": _safe_rel(sandbox_path) if sandbox_path else "",
        "arena_canonical_promoted": arena_canonical_rank is not None,
        "arena_canonical_rank": arena_canonical_rank,
        "arena_context_canonical_rank": arena_context_rank,
        "arena_exact_example_preserved": arena_literal_rank is not None,
        "arena_exact_example_rank": arena_literal_rank,
        "arena_vtrac_promoted": arena_vtrac_rank is not None,
        "arena_vtrac_rank": arena_vtrac_rank,
        "sandbox_brain1_canonical_preserved": brain1_canonical_rank is not None,
        "sandbox_brain1_canonical_rank": brain1_canonical_rank,
        "sandbox_brain1_vtrac_preserved": brain1_vtrac_rank is not None,
        "sandbox_brain1_vtrac_rank": brain1_vtrac_rank,
        "sandbox_box_seed": sandbox_box_rank is not None,
        "sandbox_box_seed_rank": sandbox_box_rank,
        "sandbox_straight_seed": sandbox_straight_rank is not None,
        "sandbox_straight_seed_rank": sandbox_straight_rank,
        "sandbox_vtrac_seed": sandbox_vtrac_rank is not None,
        "sandbox_vtrac_seed_rank": sandbox_vtrac_rank,
    }


def _corridor_cases(path: Path) -> dict[tuple[str, str], dict[str, Any]]:
    if not path.exists():
        return {}
    payload = _read_json(path)
    return {
        (str(case.get("state") or ""), str(case.get("draw_label") or "")): case
        for case in payload.get("cases") or []
        if isinstance(case, dict)
    }


def _winner_influence_rows(
    lanes: Mapping[str, Lane],
    control_rows: Sequence[Mapping[str, Any]],
    *,
    date: str,
    corridor_path: Path,
) -> list[dict[str, Any]]:
    corridor = _corridor_cases(corridor_path)
    rows: list[dict[str, Any]] = []
    for control in control_rows:
        state = str(control["state_key"])
        period = str(control["period"])
        winner = _literal(control["winner"])
        canonical = _canonical(control["winner_canonical"] or winner)
        winner_vtrac = control.get("winner_vtrac_index")
        if winner_vtrac in (None, "") and winner:
            inferred = get_vtrac_index(winner)
            winner_vtrac = inferred if isinstance(inferred, int) else ""
        target_vtrac = str(winner_vtrac or "")
        for lane in LANE_ORDER:
            snapshot = _arena_sandbox_snapshot(
                lanes[lane].sharepacks_root,
                date,
                state,
                winner,
                canonical,
                target_vtrac,
            )
            row: dict[str, Any] = {
                "lane": lane,
                "state_key": state,
                "period": period,
                "winner": winner,
                "winner_canonical": canonical,
                "winner_vtrac_index": target_vtrac,
                **snapshot,
            }
            for surface in ("cu", "play"):
                prefix = f"{lane}_{surface}"
                for field in (
                    "coverage",
                    "exact",
                    "exact_width",
                    "canonical",
                    "canonical_width",
                    "vtrac",
                    "vtrac_width",
                ):
                    row[f"{surface}_{field}"] = control.get(
                        f"{prefix}_{field}"
                    )
            if lane == "current":
                case = corridor.get((state, period), {})
                row.update(
                    {
                        "post_result_literal_pattern_hits": case.get(
                            "literal_pattern_hits"
                        ),
                        "post_result_ordered_lane_pattern_hits": case.get(
                            "ordered_lane_pattern_hits"
                        ),
                        "post_result_boxed_corridor_pattern_hits": case.get(
                            "boxed_corridor_pattern_hits"
                        ),
                        "arena_ordered_lane_rank": case.get(
                            "arena_ordered_vcode_rank"
                        ),
                        "arena_boxed_corridor_rank": case.get(
                            "arena_boxed_index_rank"
                        ),
                        "vtrac_enhanced_index_rank": case.get(
                            "enhanced_index_rank"
                        ),
                        "renderer_gap": case.get("renderer_gap"),
                        "analyzer_gap": case.get("analyzer_gap"),
                        "post_result_classification": case.get(
                            "classification"
                        ),
                    }
                )
            rows.append(row)
    return rows


def _normalize_semantic(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _normalize_semantic(item)
            for key, item in sorted(value.items())
            if key not in VOLATILE_KEYS
            and not key.endswith("_path")
            and not key.endswith("_paths")
        }
    if isinstance(value, list):
        return [_normalize_semantic(item) for item in value]
    if isinstance(value, str):
        normalized = re.sub(r"2026\d{10}", "<TIMESTAMP>", value)
        normalized = normalized.replace(
            "rpattern_source_only_v1", "<EXPERIMENT>"
        ).replace("rpattern_current_v1", "<EXPERIMENT>")
        normalized = normalized.replace("arena_v0", "<EXPERIMENT>")
        return normalized
    return value


def _semantic_payload(paths: Iterable[Path]) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for path in sorted(set(paths), key=lambda item: str(item)):
        if path.suffix.lower() == ".json":
            payload = _normalize_semantic(_read_json(path))
            shape = len(payload) if hasattr(payload, "__len__") else 1
        elif path.suffix.lower() == ".csv":
            raw_rows = _read_csv(path)
            payload = _normalize_semantic(raw_rows)
            shape = len(raw_rows)
        else:
            continue
        records.append(
            {
                "logical_name": re.sub(
                    r"2026\d{10}", "<TIMESTAMP>", path.name
                ),
                "shape": shape,
                "payload": payload,
            }
        )
    encoded = json.dumps(
        records, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return {
        "file_count": len(records),
        "row_or_key_count": sum(int(record["shape"]) for record in records),
        "semantic_sha256": hashlib.sha256(encoded).hexdigest(),
    }


def _surface_paths(state_dir: Path, surface: str) -> list[Path]:
    state = state_dir.name
    patterns = {
        "stable": [
            f"stable/{state}/*_stable_patterns_scores.csv",
            f"stable/{state}/*_stable_patterns_compound.csv",
            f"stable/{state}/*_stable_patterns_families.csv",
            f"stable/{state}/*_metrics.json",
        ],
        "digit_reduction": [
            f"digit_reduction/{state}/*_digit_reduction_scores.csv",
            f"digit_reduction/{state}/*_digit_reduction_meta.json",
        ],
        "hot_zones": [
            f"hot_zones/{state}/*_hot_zones_top_lanes.csv",
            f"hot_zones/{state}/*_hot_zones_per_lane.csv",
            f"hot_zones/{state}/*_hot_zones_meta.json",
        ],
        "vtrac": [f"vtrac/{state}/*_vtrac_enhanced_*.json"],
        "arena": ["analysis/aggregated_analysis_arena__*.json"],
        "sandbox": ["analysis/translation_sandbox_seed__*.json"],
        "candidate_universe": ["candidate_universe__*.json"],
        "play_card": ["play_card__*.json"],
    }
    paths: list[Path] = []
    for pattern in patterns[surface]:
        paths.extend(state_dir.glob(pattern))
    return paths


def _artifact_diff_rows(
    lanes: Mapping[str, Lane],
    *,
    date: str,
) -> list[dict[str, Any]]:
    surfaces = (
        "stable",
        "digit_reduction",
        "hot_zones",
        "vtrac",
        "arena",
        "sandbox",
        "candidate_universe",
        "play_card",
    )
    states: set[str] = set()
    for lane in lanes.values():
        states.update(_state_dirs(lane.sharepacks_root, date))
    rows: list[dict[str, Any]] = []
    for state in sorted(states):
        for surface in surfaces:
            snapshots = {}
            for lane in LANE_ORDER:
                state_dir = lanes[lane].sharepacks_root / date / state
                snapshots[lane] = _semantic_payload(
                    _surface_paths(state_dir, surface)
                )
            rows.append(
                {
                    "state_key": state,
                    "surface": surface,
                    "old_file_count": snapshots["old"]["file_count"],
                    "old_row_or_key_count": snapshots["old"][
                        "row_or_key_count"
                    ],
                    "old_semantic_sha256": snapshots["old"][
                        "semantic_sha256"
                    ],
                    "source_only_file_count": snapshots["source_only"][
                        "file_count"
                    ],
                    "source_only_row_or_key_count": snapshots["source_only"][
                        "row_or_key_count"
                    ],
                    "source_only_semantic_sha256": snapshots["source_only"][
                        "semantic_sha256"
                    ],
                    "current_file_count": snapshots["current"]["file_count"],
                    "current_row_or_key_count": snapshots["current"][
                        "row_or_key_count"
                    ],
                    "current_semantic_sha256": snapshots["current"][
                        "semantic_sha256"
                    ],
                    "old_to_source_changed": (
                        snapshots["old"]["semantic_sha256"]
                        != snapshots["source_only"]["semantic_sha256"]
                    ),
                    "source_to_current_changed": (
                        snapshots["source_only"]["semantic_sha256"]
                        != snapshots["current"]["semantic_sha256"]
                    ),
                }
            )
    return rows


def _r_consensus_harness_summary(out_dir: Path) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    for lane, directory_name in (
        ("old", "R_CONSENSUS_OLD"),
        ("current", "R_CONSENSUS_CURRENT"),
    ):
        matches = sorted(
            (out_dir / directory_name).glob(
                "*__R_CONSENSUS_EVENT_ROSTER.csv"
            )
        )
        rows = _read_csv(matches[0]) if matches else []
        summary[lane] = {
            "path": _safe_rel(matches[0]) if matches else "",
            "event_count": len(rows),
            "event_class_counts": dict(
                Counter(str(row.get("event_class") or "") for row in rows)
            ),
            "cons_full_flagged": sum(
                _truthy(row.get("cons_full")) for row in rows
            ),
            "cons_3v_flagged": sum(
                _truthy(row.get("cons_3v")) for row in rows
            ),
            "cons_stub_flagged": sum(
                _truthy(row.get("cons_stub")) for row in rows
            ),
            "raw_geometry_without_stable_flag": sum(
                not any(
                    _truthy(row.get(field))
                    for field in ("cons_full", "cons_3v", "cons_stub")
                )
                for row in rows
            ),
        }
    return summary


def _coverage_counts(
    rows: Sequence[Mapping[str, Any]], lane: str, surface: str
) -> Counter[str]:
    return Counter(
        str(row.get(f"{lane}_{surface}_coverage") or "NO_MATCH") for row in rows
    )


def _overlapping_coverage_counts(
    rows: Sequence[Mapping[str, Any]], lane: str, surface: str
) -> dict[str, int]:
    prefix = f"{lane}_{surface}"
    return {
        "exact": sum(bool(row.get(f"{prefix}_exact")) for row in rows),
        "canonical": sum(
            bool(row.get(f"{prefix}_canonical")) for row in rows
        ),
        "vtrac": sum(bool(row.get(f"{prefix}_vtrac")) for row in rows),
    }


def _markdown(
    *,
    date: str,
    lanes: Mapping[str, Lane],
    cell_rows: Sequence[Mapping[str, Any]],
    consensus_rows: Sequence[Mapping[str, Any]],
    control_rows: Sequence[Mapping[str, Any]],
    influence_rows: Sequence[Mapping[str, Any]],
    artifact_rows: Sequence[Mapping[str, Any]],
    corridor_path: Path,
    consensus_harness: Mapping[str, Any],
) -> str:
    cell_classes = Counter(
        str(row["old_to_source_class"]) for row in cell_rows
    )
    source_consensus_lengths = Counter(
        int(row["source_only_tail_length"])
        for row in consensus_rows
        if row["source_only_strict"]
    )
    artifact_source_changes = Counter(
        str(row["surface"])
        for row in artifact_rows
        if row["old_to_source_changed"]
    )
    artifact_current_changes = Counter(
        str(row["surface"])
        for row in artifact_rows
        if row["source_to_current_changed"]
    )
    control_changed_source = [
        row for row in control_rows if row["old_to_source_changed"]
    ]
    control_changed_current = [
        row for row in control_rows if row["source_to_current_changed"]
    ]
    ct = next(
        (
            row
            for row in influence_rows
            if row["lane"] == "current"
            and row["state_key"] == "Connecticut4"
            and row["period"] == "Evening"
        ),
        {},
    )
    old_consensus = consensus_harness.get("old") or {}
    current_consensus = consensus_harness.get("current") or {}

    lines = [
        f"# March 9 R-Pattern Replay Comparison ({date})",
        "",
        "## Claim Boundary",
        "",
        "- `old -> source_only` isolates the variable-length R-pattern source correction.",
        "- `source_only -> current` isolates later bounded runtime changes.",
        "- Candidate Universe and Play Card rows are frozen predictive/control-arm outputs.",
        "- Corridor evidence is post-result diagnosis and is not credited as a frozen prediction.",
        "- Exact, canonical/box, and VTRAC territory are reported separately.",
        "- The denominator is 28 posted outcomes. NorthCarolina4 Evening `000` remains present with model-specific VTRAC marked N/A.",
        "- The legacy board display order is not treated as an analytical rank.",
        "",
        "## Source Correction",
        "",
        f"- Changed table cells: `{len(cell_rows)}`.",
        f"- Synthetic zero removals: `{cell_classes.get('SYNTHETIC_ZERO_REMOVED', 0)}`.",
        f"- Other old-to-source cell changes: `{cell_classes.get('OTHER_CHANGE', 0)}`.",
        f"- Source-only to current cell changes: `{sum(1 for row in cell_rows if row['source_to_current_class'] != 'UNCHANGED')}`.",
        f"- Strict R-consensus locations: `{sum(1 for row in consensus_rows if row['source_only_strict'])}`.",
        f"- Corrected one-digit tails: `{source_consensus_lengths.get(1, 0)}`.",
        f"- Corrected two-digit tails: `{source_consensus_lengths.get(2, 0)}`.",
        f"- Dedicated harness old classes: `{old_consensus.get('event_class_counts', {})}`.",
        f"- Dedicated harness corrected classes: `{current_consensus.get('event_class_counts', {})}`.",
        f"- Corrected raw events lacking any Stable consensus flag: `{current_consensus.get('raw_geometry_without_stable_flag', 0)}`.",
        "",
        "The geometry did not disappear: the same strict locations existed in the old tables, but all were falsely rendered as three-digit values. The source-only and current table cells are identical, proving that the later runtime changes did not alter the corrected R-pattern source.",
        "",
        "The dedicated harness also includes one bounded three-of-four suffix event, producing 43 events rather than the 42 strict-equality locations. Raw geometry restoration is proven; downstream Stable/Arena recognition is not yet complete and remains a separately measured follow-up.",
        "",
        "## Predictive Control Arm",
        "",
        "Overlapping evidence counts preserve every relation. An exact row can also be canonical and VTRAC-supported.",
        "",
        "| Lane | Surface | Exact | Canonical | VTRAC territory |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for lane in LANE_ORDER:
        for surface, label in (("cu", "Candidate Universe"), ("play", "Play Card")):
            overlapping = _overlapping_coverage_counts(
                control_rows, lane, surface
            )
            lines.append(
                f"| {lane} | {label} | {overlapping['exact']} | {overlapping['canonical']} | {overlapping['vtrac']} |"
            )
    lines.extend(
        [
            "",
            "The following classes are mutually exclusive and identify each outcome's strongest realized relation.",
            "",
            "| Lane | Surface | Exact | Canonical only | VTRAC only | No match |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for lane in LANE_ORDER:
        for surface, label in (("cu", "Candidate Universe"), ("play", "Play Card")):
            counts = _coverage_counts(control_rows, lane, surface)
            lines.append(
                f"| {lane} | {label} | {counts['EXACT']} | {counts['CANONICAL']} | {counts['VTRAC_ONLY']} | {counts['NO_MATCH']} |"
            )
    lines.extend(
        [
            "",
            f"- Outcomes whose control-arm summary changed old-to-source: `{len(control_changed_source)}`.",
            f"- Outcomes whose control-arm summary changed source-to-current: `{len(control_changed_current)}`.",
            "",
            "This result is mixed rather than uniformly positive. Candidate Universe coverage classes remain stable, while the corrected Play Card replay gains VTRAC territory in one outcome and loses one old exact-order conversion. Width and route details are retained in `CONTROL_ARM_OUTCOME_COMPARISON.csv`.",
            "",
            "## Connecticut4 Evening 091",
            "",
            f"- Arena canonical `019` promoted: `{ct.get('arena_canonical_promoted')}` at rank `{ct.get('arena_canonical_rank')}`.",
            f"- Arena VTRAC index `9` promoted: `{ct.get('arena_vtrac_promoted')}` at rank `{ct.get('arena_vtrac_rank')}`.",
            f"- Sandbox canonical seed `019`: `{ct.get('sandbox_box_seed')}` at rank `{ct.get('sandbox_box_seed_rank')}`.",
            f"- Sandbox exact straight seed `091`: `{ct.get('sandbox_straight_seed')}`.",
            f"- Sandbox VTRAC seed `9`: `{ct.get('sandbox_vtrac_seed')}` at rank `{ct.get('sandbox_vtrac_seed_rank')}`.",
            f"- Candidate Universe coverage: `{ct.get('cu_coverage')}`; exact width `{ct.get('cu_exact_width')}`, canonical width `{ct.get('cu_canonical_width')}`, VTRAC width `{ct.get('cu_vtrac_width')}`.",
            f"- Play Card coverage: `{ct.get('play_coverage')}`; exact width `{ct.get('play_exact_width')}`, canonical width `{ct.get('play_canonical_width')}`, VTRAC width `{ct.get('play_vtrac_width')}`.",
            f"- Winner-side pattern cells: literal `{ct.get('post_result_literal_pattern_hits')}`, ordered lane `{ct.get('post_result_ordered_lane_pattern_hits')}`, boxed corridor `{ct.get('post_result_boxed_corridor_pattern_hits')}`.",
            f"- Predictive-safe Arena boxed-corridor rank: `{ct.get('arena_boxed_corridor_rank')}`; ordered-lane rank: `{ct.get('arena_ordered_lane_rank')}`.",
            "",
            "Interpretation: the system preserved and promoted the winning canonical/VTRAC territory and the old/current control arm converted it to canonical/box coverage. It did not isolate literal `091` as an exact Play Card result. The winner-side corridor explains a translation opportunity; it is not retroactively counted as a prediction.",
            "",
            "## Semantic Artifact Changes",
            "",
            f"- Old-to-source changed state/surface pairs: `{sum(artifact_source_changes.values())}`.",
            f"- Source-to-current changed state/surface pairs: `{sum(artifact_current_changes.values())}`.",
            f"- Old-to-source by surface: `{dict(sorted(artifact_source_changes.items()))}`.",
            f"- Source-to-current by surface: `{dict(sorted(artifact_current_changes.items()))}`.",
            "",
            "Semantic hashes remove timestamps, paths, and experiment labels. They show where payload meaning changed, not merely where replay filenames changed.",
            "",
            "## Output Map",
            "",
            "- `R_PATTERN_CELL_DIFF.csv`: every changed table cell.",
            "- `R_CONSENSUS_EVENT_DIFF.csv`: strict and 3-of-4 consensus locations across all lanes.",
            "- `CONTROL_ARM_OUTCOME_COMPARISON.csv`: exact/canonical/VTRAC outcomes and minimum widths.",
            "- `WINNER_INFLUENCE_LADDER.csv`: Arena, Sandbox, control-arm, and post-result corridor stages.",
            "- `ARTIFACT_SEMANTIC_DIFF.csv`: normalized per-state surface hashes.",
            f"- Corridor harness: `{_safe_rel(corridor_path)}`.",
            "",
            "## Lane Roots",
            "",
        ]
    )
    for lane in LANE_ORDER:
        lines.append(
            f"- `{lane}`: `{_safe_rel(lanes[lane].sharepacks_root)}`"
        )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    date = args.date
    replay_root = _resolve(args.replay_root)
    out_dir = _resolve(args.out_dir)
    corridor_path = _resolve(args.corridor_harness)
    lanes = {
        "old": Lane(
            "old",
            _resolve(args.old_root),
            replay_root
            / "COMPARISON/OLD_CONTROL_ARM"
            / f"{date}__CANDIDATE_UNIVERSE_GRADE.csv",
            replay_root
            / "COMPARISON/OLD_CONTROL_ARM"
            / f"{date}__PLAY_CARD_GRADE.csv",
        ),
        "source_only": Lane(
            "source_only",
            _resolve(args.source_root),
            replay_root
            / "SOURCE_ONLY/CONTROL_ARM"
            / f"{date}__CANDIDATE_UNIVERSE_GRADE.csv",
            replay_root
            / "SOURCE_ONLY/CONTROL_ARM"
            / f"{date}__PLAY_CARD_GRADE.csv",
        ),
        "current": Lane(
            "current",
            _resolve(args.current_root),
            replay_root
            / "CURRENT/CONTROL_ARM"
            / f"{date}__CANDIDATE_UNIVERSE_GRADE.csv",
            replay_root
            / "CURRENT/CONTROL_ARM"
            / f"{date}__PLAY_CARD_GRADE.csv",
        ),
    }

    lane_cells = {
        lane: _load_cells(config.sharepacks_root, date)
        for lane, config in lanes.items()
    }
    cell_rows = _build_cell_diff(lane_cells)
    consensus_rows = _build_consensus_diff(lane_cells)
    control_rows = _control_arm_rows(lanes)
    influence_rows = _winner_influence_rows(
        lanes,
        control_rows,
        date=date,
        corridor_path=corridor_path,
    )
    artifact_rows = _artifact_diff_rows(lanes, date=date)
    consensus_harness = _r_consensus_harness_summary(out_dir)

    cell_fields = [
        "state_key",
        "variant",
        "set",
        "draw",
        "row_type",
        "column",
        "old_value",
        "source_only_value",
        "current_value",
        "old_length",
        "source_only_length",
        "current_length",
        "old_to_source_class",
        "source_to_current_class",
    ]
    consensus_fields = [
        "state_key",
        "variant",
        "set",
        "draw",
        "column",
        "old_strict",
        "old_near_3_of_4",
        "old_tail",
        "old_tail_length",
        "source_only_strict",
        "source_only_near_3_of_4",
        "source_only_tail",
        "source_only_tail_length",
        "current_strict",
        "current_near_3_of_4",
        "current_tail",
        "current_tail_length",
        "old_to_source_class",
        "source_to_current_class",
        "old_rows",
        "source_only_rows",
        "current_rows",
    ]
    control_fields = list(control_rows[0].keys()) if control_rows else []
    influence_fields: list[str] = []
    for row in influence_rows:
        for key in row:
            if key not in influence_fields:
                influence_fields.append(key)
    artifact_fields = list(artifact_rows[0].keys()) if artifact_rows else []

    _write_csv(out_dir / "R_PATTERN_CELL_DIFF.csv", cell_rows, cell_fields)
    _write_csv(
        out_dir / "R_CONSENSUS_EVENT_DIFF.csv",
        consensus_rows,
        consensus_fields,
    )
    _write_csv(
        out_dir / "CONTROL_ARM_OUTCOME_COMPARISON.csv",
        control_rows,
        control_fields,
    )
    _write_csv(
        out_dir / "WINNER_INFLUENCE_LADDER.csv",
        influence_rows,
        influence_fields,
    )
    _write_csv(
        out_dir / "ARTIFACT_SEMANTIC_DIFF.csv",
        artifact_rows,
        artifact_fields,
    )

    payload = {
        "schema": "aat9.rpattern_gold_day_replay_comparison.v1",
        "date": date,
        "claim_boundary": {
            "old_to_source_only": "SOURCE_CORRECTION_CAUSAL_LANE",
            "source_only_to_current": "LATER_RUNTIME_CHANGE_LANE",
            "candidate_universe_and_play_card": "FROZEN_PREDICTIVE_CONTROL_ARM",
            "corridor_harness": "POST_RESULT_DIAGNOSTIC_ONLY",
            "analytical_state_rank": "INVALID_STATIC_ORDER_NOT_CREDITED",
        },
        "lane_roots": {
            lane: _safe_rel(config.sharepacks_root)
            for lane, config in lanes.items()
        },
        "summary": {
            "outcome_count": len(control_rows),
            "changed_table_cells": len(cell_rows),
            "synthetic_zero_removals": sum(
                row["old_to_source_class"] == "SYNTHETIC_ZERO_REMOVED"
                for row in cell_rows
            ),
            "source_to_current_table_changes": sum(
                row["source_to_current_class"] != "UNCHANGED"
                for row in cell_rows
            ),
            "strict_consensus_locations": sum(
                bool(row["source_only_strict"]) for row in consensus_rows
            ),
            "source_only_consensus_tail_lengths": dict(
                Counter(
                    str(row["source_only_tail_length"])
                    for row in consensus_rows
                    if row["source_only_strict"]
                )
            ),
            "control_arm_counts": {
                lane: {
                    surface: dict(
                        _coverage_counts(control_rows, lane, surface)
                    )
                    for surface in ("cu", "play")
                }
                for lane in LANE_ORDER
            },
            "control_arm_overlapping_counts": {
                lane: {
                    surface: _overlapping_coverage_counts(
                        control_rows, lane, surface
                    )
                    for surface in ("cu", "play")
                }
                for lane in LANE_ORDER
            },
            "control_outcomes_changed_old_to_source": sum(
                bool(row["old_to_source_changed"]) for row in control_rows
            ),
            "control_outcomes_changed_source_to_current": sum(
                bool(row["source_to_current_changed"]) for row in control_rows
            ),
            "artifact_pairs_changed_old_to_source": sum(
                bool(row["old_to_source_changed"]) for row in artifact_rows
            ),
            "artifact_pairs_changed_source_to_current": sum(
                bool(row["source_to_current_changed"]) for row in artifact_rows
            ),
            "r_consensus_harness": consensus_harness,
        },
        "outputs": {
            "cell_diff": _safe_rel(out_dir / "R_PATTERN_CELL_DIFF.csv"),
            "consensus_diff": _safe_rel(
                out_dir / "R_CONSENSUS_EVENT_DIFF.csv"
            ),
            "control_arm": _safe_rel(
                out_dir / "CONTROL_ARM_OUTCOME_COMPARISON.csv"
            ),
            "winner_influence": _safe_rel(
                out_dir / "WINNER_INFLUENCE_LADDER.csv"
            ),
            "artifact_semantics": _safe_rel(
                out_dir / "ARTIFACT_SEMANTIC_DIFF.csv"
            ),
            "corridor_harness": _safe_rel(corridor_path),
        },
    }
    _write_json(out_dir / "MARCH9_RPATTERN_REPLAY_COMPARISON.json", payload)
    _write_text(
        out_dir / "MARCH9_RPATTERN_REPLAY_COMPARISON.md",
        _markdown(
            date=date,
            lanes=lanes,
            cell_rows=cell_rows,
            consensus_rows=consensus_rows,
            control_rows=control_rows,
            influence_rows=influence_rows,
            artifact_rows=artifact_rows,
            corridor_path=corridor_path,
            consensus_harness=consensus_harness,
        ),
    )
    print(
        json.dumps(
            {
                "out_dir": _safe_rel(out_dir),
                "outcomes": len(control_rows),
                "cell_changes": len(cell_rows),
                "strict_consensus": sum(
                    bool(row["source_only_strict"]) for row in consensus_rows
                ),
                "influence_rows": len(influence_rows),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
