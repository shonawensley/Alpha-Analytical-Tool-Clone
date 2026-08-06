#!/usr/bin/env python3
"""Build the lossless, read-only AUX CORE review object.

AUX CORE is a Deep Review surface. It reorganizes frozen Auxiliary and Control
Center evidence, preserves source lineage, and builds a cross-block convergence
lattice. It does not alter native analyzers, runtime scoring, Candidate
Universe, Play Cards, or Analysis Arena behavior.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from contextlib import redirect_stdout
from dataclasses import asdict
from io import StringIO
from itertools import permutations
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, MutableMapping, Optional, Sequence


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from modules.analyze_pairs import compute_combo_draws_since, get_vtrac_statuses  # noqa: E402
from modules.vtrac_reference import DIGIT2V, VTRAC_DISPLAY, get_vtrac_index  # noqa: E402
from modules.vtrac_straight_map import (  # noqa: E402
    ordered_vcode_for_combo,
    vstraight_lane_for_vcode,
    vstraight_lanes_for_index,
)
from scripts.tools.positional_aux_core import (  # noqa: E402
    build_lossless_report,
    grade_winner as grade_positional_winner,
    load_frozen_draws,
)
from core.classic_due_doubles import build_classic_due_doubles_review  # noqa: E402


SCHEMA_VERSION = "aux_core_v1"
VARIANTS: tuple[str, ...] = ("midday", "evening", "combined")
DISPLAY_VARIANTS: tuple[str, ...] = ("midday", "evening", "combined")
PERIOD_VARIANTS = {"Midday": "midday", "Evening": "evening"}
WIDTHS: tuple[int, ...] = (3, 6, 8, 10, 12, 16)

PAIR_TRACKER = "PAIR_TRACKER"
BOXED_COMBO_TRACKER = "BOXED_COMBO_TRACKER"
VTRAC_DUE_TRACKER = "VTRAC_DUE_TRACKER"
SUM_TRACKER = "SUM_TRACKER"
BLACKAPPLE = "BLACKAPPLE"
VTRAC_REPEAT = "VTRAC_REPEAT"
POSITIONAL = "POSITIONAL"
PROFIT_ALERTS = "PROFIT_ALERTS"

BASE_SOURCE_FAMILIES: tuple[str, ...] = (
    PAIR_TRACKER,
    BOXED_COMBO_TRACKER,
    VTRAC_DUE_TRACKER,
    SUM_TRACKER,
    BLACKAPPLE,
    VTRAC_REPEAT,
    POSITIONAL,
    PROFIT_ALERTS,
)
CANDIDATE_SOURCE_FAMILIES = {
    BOXED_COMBO_TRACKER,
    BLACKAPPLE,
    POSITIONAL,
    PROFIT_ALERTS,
}
ORDER_AWARE_SOURCE_FAMILIES = {POSITIONAL, PROFIT_ALERTS}
DERIVED_RECEIPTS = {
    "BLOCK_7_BADGE_CONCENTRATION",
    "BLOCK_8_SHORTLIST_CONVERGENCE",
    "BLOCK_10_CROSS_BLOCK_CONVERGENCE",
}

STATUS_SEVERITY = {"red": 3, "blue": 2, "purple": 1}
SHAPE_SEVERITY = {"RC": 2, "BS": 1}
IDENTITY_SPECIFICITY = {
    "exact_literal": 4,
    "ordered_lane": 3,
    "canonical_box": 2,
    "vtrac_index": 1,
}
REVIEW_TIER_PRIORITY = {
    "TIER_A_INDEPENDENT_IDENTITY": 3,
    "TIER_B_SOURCE_PLUS_STRUCTURE": 2,
    "TIER_C_UNTRANSLATED_STRUCTURE": 1,
    "NOT_QUALIFIED": 0,
}
NARROWED_REVIEW_TIERS = {
    "TIER_A_INDEPENDENT_IDENTITY",
    "TIER_B_SOURCE_PLUS_STRUCTURE",
}


def safe_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except Exception:
        return str(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_sha256(payload: Any) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def normalize_pick3(value: Any) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    digits = digits[-3:].zfill(3)
    return digits if len(digits) == 3 else ""


def normalize_playable_pick3(value: Any) -> str:
    """Accept only an exact playable Pick-3 literal from candidate arrays."""
    text = str(value or "").strip()
    return text if len(text) == 3 and text.isdigit() else ""


def canonical(value: Any) -> str:
    literal = normalize_pick3(value)
    return "".join(sorted(literal)) if literal else ""


def digital_root(value: Any) -> int:
    literal = normalize_pick3(value)
    if not literal:
        return 0
    total = sum(int(ch) for ch in literal)
    return 0 if total == 0 else 1 + ((total - 1) % 9)


def combo_sum(value: Any) -> int:
    literal = normalize_pick3(value)
    return sum(int(ch) for ch in literal) if literal else 0


def combo_kind(value: Any) -> str:
    literal = normalize_pick3(value)
    if not literal:
        return "invalid"
    unique = len(set(literal))
    if unique == 1:
        return "triple"
    if unique == 2:
        return "double"
    return "single"


def combo_pairs(value: Any) -> list[str]:
    literal = normalize_pick3(value)
    if not literal:
        return []
    pairs = {
        "".join(sorted((literal[0], literal[1]))),
        "".join(sorted((literal[1], literal[2]))),
        "".join(sorted((literal[0], literal[2]))),
    }
    return sorted(pairs)


def pair_vtrac_family(pair: str) -> str:
    if len(pair) != 2 or not pair.isdigit():
        return ""
    return "".join(sorted((str(DIGIT2V[pair[0]]), str(DIGIT2V[pair[1]]))))


def canonical_permutations(value: Any) -> list[str]:
    box = canonical(value)
    if not box:
        return []
    return sorted({"".join(chars) for chars in permutations(box)})


def _read_json(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected object JSON: {safe_rel(path)}")
    return payload


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _json_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [
            normalize_playable_pick3(item)
            for item in value
            if normalize_playable_pick3(item)
        ]
    text = str(value or "").strip()
    if not text:
        return []
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = text.replace(",", " ").split()
    if not isinstance(parsed, list):
        return []
    return [
        normalize_playable_pick3(item)
        for item in parsed
        if normalize_playable_pick3(item)
    ]


def _provenance(path: Path, *, required: bool) -> Dict[str, Any]:
    return {
        "path": safe_rel(path),
        "required": required,
        "present": path.exists(),
        "sha256": sha256_file(path) if path.exists() else None,
        "size_bytes": path.stat().st_size if path.exists() else None,
    }


def _forbidden_result_paths(payload: Any) -> list[str]:
    forbidden = {
        "winner",
        "result",
        "winning_number",
        "winner_canonical",
        "winner_vtrac_index",
        "winner_ordered_vcode",
    }
    paths: list[str] = []

    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                child_path = f"{path}/{key}"
                if str(key).lower() in forbidden:
                    paths.append(child_path)
                walk(child, child_path)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}/{index}")

    walk(payload, "")
    return paths


def _rank_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def _active_flags(metrics: Mapping[str, Any]) -> list[str]:
    flags = metrics.get("flags")
    if not isinstance(flags, dict):
        return []
    return [
        color
        for color in ("red", "blue", "purple")
        if bool(flags.get(color))
    ]


def _variant_tag(variant: str) -> str:
    return {"midday": "M", "evening": "E", "combined": "C"}.get(
        variant,
        variant.upper(),
    )


def _vtrac_members() -> Dict[int, Dict[str, list[str]]]:
    members: Dict[int, Dict[str, list[str]]] = {}
    for entry in VTRAC_DISPLAY:
        idx = int(entry["Index"])
        members[idx] = {
            "singles": [
                canonical(item)
                for item in str(entry.get("Singles") or "").split()
                if canonical(item)
            ],
            "doubles": [
                canonical(item)
                for item in str(entry.get("Doubles") or "").split()
                if canonical(item)
            ],
        }
    return members


VTRAC_MEMBERS = _vtrac_members()


def _burden(identity_level: str, identity: str) -> Dict[str, Any]:
    if identity_level == "exact_literal":
        return {
            "boxed_vtrac_indices": 1 if get_vtrac_index(identity) else 0,
            "canonical_boxes": 1,
            "ordered_lanes": 1 if ordered_vcode_for_combo(identity) else 0,
            "exact_literals": 1,
        }
    if identity_level == "ordered_lane":
        lane = vstraight_lane_for_vcode(identity)
        return {
            "boxed_vtrac_indices": 1 if lane else 0,
            "canonical_boxes": len({canonical(item) for item in lane}),
            "ordered_lanes": 1 if lane else 0,
            "exact_literals": len(lane),
        }
    if identity_level == "canonical_box":
        literals = canonical_permutations(identity)
        return {
            "boxed_vtrac_indices": 1 if get_vtrac_index(identity) else 0,
            "canonical_boxes": 1,
            "ordered_lanes": len(
                {
                    ordered_vcode_for_combo(item)
                    for item in literals
                    if ordered_vcode_for_combo(item)
                }
            ),
            "exact_literals": len(literals),
        }
    if identity_level == "vtrac_index":
        idx = int(identity)
        members = VTRAC_MEMBERS.get(idx, {})
        canonicals = set(members.get("singles", [])) | set(
            members.get("doubles", [])
        )
        lanes = vstraight_lanes_for_index(idx)
        literals = {
            literal
            for values in lanes.values()
            for literal in values
            if normalize_pick3(literal)
        }
        return {
            "boxed_vtrac_indices": 1,
            "canonical_boxes": len(canonicals),
            "ordered_lanes": len(lanes),
            "exact_literals": len(literals),
        }
    return {
        "boxed_vtrac_indices": 0,
        "canonical_boxes": 0,
        "ordered_lanes": 0,
        "exact_literals": 0,
    }


def build_due_pairs_block(summary: Mapping[str, Any]) -> Dict[str, Any]:
    source = ((summary.get("pairs") or {}).get("by_variant") or {})
    by_variant: Dict[str, Any] = {}
    exact_receipts: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)
    family_receipts: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)

    for variant in VARIANTS:
        variant_data = source.get(variant) if isinstance(source, dict) else {}
        variant_data = variant_data if isinstance(variant_data, dict) else {}
        statuses = variant_data.get("status")
        statuses = statuses if isinstance(statuses, dict) else {}
        variant_payload: Dict[str, Any] = {}
        for kind_key, source_key in (
            ("repeating_pairs", "repeating"),
            ("non_repeating_pairs", "non_repeating"),
        ):
            values = variant_data.get(source_key)
            values = values if isinstance(values, dict) else {}
            rows = []
            for pair, raw_ds in values.items():
                status = str(statuses.get(pair) or "").lower()
                if status not in {"red", "blue"}:
                    continue
                row = {
                    "pair": str(pair),
                    "draws_since": int(raw_ds),
                    "status": status,
                    "vtrac_pair_family": pair_vtrac_family(str(pair)),
                    "source_lineage": PAIR_TRACKER,
                    "variant": variant,
                }
                rows.append(row)
                exact_receipts[str(pair)].append(dict(row))
                family_receipts[row["vtrac_pair_family"]].append(dict(row))
            rows.sort(
                key=lambda row: (
                    -STATUS_SEVERITY[row["status"]],
                    -row["draws_since"],
                    row["pair"],
                )
            )
            variant_payload[kind_key] = _rank_rows(rows)
        by_variant[variant] = variant_payload

    exact_duplicates = []
    for pair, receipts in exact_receipts.items():
        variants = sorted({row["variant"] for row in receipts})
        if len(variants) < 2:
            continue
        exact_duplicates.append(
            {
                "pair": pair,
                "variant_coverage": variants,
                "receipts": sorted(receipts, key=lambda row: VARIANTS.index(row["variant"])),
            }
        )
    exact_duplicates.sort(
        key=lambda row: (
            -len(row["variant_coverage"]),
            -sum(STATUS_SEVERITY[item["status"]] for item in row["receipts"]),
            row["pair"],
        )
    )
    _rank_rows(exact_duplicates)

    family_relations = []
    for family, receipts in family_receipts.items():
        variants = sorted({row["variant"] for row in receipts})
        literals = sorted({row["pair"] for row in receipts})
        if len(variants) < 2 or len(literals) < 2:
            continue
        family_relations.append(
            {
                "vtrac_pair_family": family,
                "variant_coverage": variants,
                "pairs": literals,
                "receipts": sorted(
                    receipts,
                    key=lambda row: (VARIANTS.index(row["variant"]), row["pair"]),
                ),
            }
        )
    family_relations.sort(
        key=lambda row: (
            -len(row["variant_coverage"]),
            -len(row["pairs"]),
            row["vtrac_pair_family"],
        )
    )
    _rank_rows(family_relations)

    return {
        "block_id": 1,
        "name": "Due Pairs",
        "source_lineages": [PAIR_TRACKER],
        "derived": False,
        "selection": "red_and_blue_only",
        "by_variant": by_variant,
        "cross_variant": {
            "exact_duplicates": exact_duplicates,
            "vtrac_pair_relations": family_relations,
        },
    }


def _pair_badges(
    canonical_combo: str,
    *,
    summary: Mapping[str, Any],
    variant: str,
) -> list[dict[str, str]]:
    pair_payload = ((summary.get("pairs") or {}).get("by_variant") or {}).get(
        variant,
        {},
    )
    statuses = pair_payload.get("status") if isinstance(pair_payload, dict) else {}
    statuses = statuses if isinstance(statuses, dict) else {}
    return [
        {"pair": pair, "status": str(statuses[pair])}
        for pair in combo_pairs(canonical_combo)
        if pair in statuses
    ]


def build_boxed_combinations_block(
    summary: Mapping[str, Any],
    draws_by_variant: Mapping[str, Sequence[str]],
) -> tuple[Dict[str, Any], Dict[str, Dict[str, Dict[str, int]]]]:
    by_variant: Dict[str, Any] = {}
    combo_ds: Dict[str, Dict[str, Dict[str, int]]] = {}
    selected_by_kind: Dict[str, MutableMapping[str, list[dict[str, Any]]]] = {
        "singles": defaultdict(list),
        "doubles": defaultdict(list),
    }

    for variant in VARIANTS:
        draws = list(draws_by_variant.get(variant) or [])[:1000]
        singles_ds, doubles_ds = compute_combo_draws_since(draws)
        combo_ds[variant] = {
            "singles": singles_ds,
            "doubles": doubles_ds,
        }
        singles = []
        for box, ds in singles_ds.items():
            shape = "RC" if ds >= 501 else "BS" if ds >= 334 else ""
            if not shape:
                continue
            row = {
                "canonical": box,
                "draws_since": int(ds),
                "shape": shape,
                "vtrac_index": get_vtrac_index(box),
                "pair_badges": _pair_badges(
                    box,
                    summary=summary,
                    variant=variant,
                ),
                "sum": combo_sum(box),
                "root_sum": digital_root(box),
                "variant": variant,
                "source_lineage": BOXED_COMBO_TRACKER,
            }
            singles.append(row)
            selected_by_kind["singles"][box].append(dict(row))
        singles.sort(
            key=lambda row: (
                -SHAPE_SEVERITY[row["shape"]],
                -row["draws_since"],
                row["canonical"],
            )
        )
        _rank_rows(singles)

        doubles = []
        for box, ds in doubles_ds.items():
            if ds < 1000:
                continue
            row = {
                "canonical": box,
                "draws_since": int(ds),
                "shape": "RC",
                "vtrac_index": get_vtrac_index(box),
                "pair_badges": _pair_badges(
                    box,
                    summary=summary,
                    variant=variant,
                ),
                "sum": combo_sum(box),
                "root_sum": digital_root(box),
                "variant": variant,
                "source_lineage": BOXED_COMBO_TRACKER,
            }
            doubles.append(row)
            selected_by_kind["doubles"][box].append(dict(row))
        doubles.sort(key=lambda row: (-row["draws_since"], row["canonical"]))
        _rank_rows(doubles)
        by_variant[variant] = {
            "singles_red_blue": singles,
            "doubles_red_only": doubles,
        }

    cross_variant: Dict[str, Any] = {}
    for kind in ("singles", "doubles"):
        exact = []
        family_map: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
        for box, receipts in selected_by_kind[kind].items():
            variants = sorted({row["variant"] for row in receipts})
            if len(variants) >= 2:
                exact.append(
                    {
                        "canonical": box,
                        "vtrac_index": get_vtrac_index(box),
                        "variant_coverage": variants,
                        "receipts": sorted(
                            receipts,
                            key=lambda row: (
                                VARIANTS.index(row["variant"]),
                                row["canonical"],
                            ),
                        ),
                    }
                )
            idx = get_vtrac_index(box)
            if idx:
                family_map[int(idx)].extend(receipts)
        exact.sort(
            key=lambda row: (
                -len(row["variant_coverage"]),
                -sum(item["draws_since"] for item in row["receipts"]),
                row["canonical"],
            )
        )
        _rank_rows(exact)

        families = []
        for idx, receipts in family_map.items():
            variants = sorted({row["variant"] for row in receipts})
            boxes = sorted({row["canonical"] for row in receipts})
            if len(variants) < 2 or len(boxes) < 2:
                continue
            families.append(
                {
                    "vtrac_index": idx,
                    "variant_coverage": variants,
                    "canonicals": boxes,
                    "receipts": sorted(
                        receipts,
                        key=lambda row: (
                            VARIANTS.index(row["variant"]),
                            row["canonical"],
                        ),
                    ),
                }
            )
        families.sort(
            key=lambda row: (
                -len(row["variant_coverage"]),
                -len(row["canonicals"]),
                row["vtrac_index"],
            )
        )
        _rank_rows(families)
        cross_variant[kind] = {
            "exact_duplicates": exact,
            "vtrac_relations": families,
        }

    classic_due_doubles = asdict(
        build_classic_due_doubles_review(
            str(summary.get("state") or summary.get("state_key") or ""),
            draws_by_variant,
        )
    )
    classic_due_doubles["derived"] = True
    classic_due_doubles["source_lineages"] = [
        PAIR_TRACKER,
        BOXED_COMBO_TRACKER,
    ]
    classic_due_doubles["credit_boundary"] = (
        "Doubles Table 2 reorganizes existing pair and boxed-combination "
        "evidence. It is display-only and cannot create an additional source vote."
    )

    return (
        {
            "block_id": 2,
            "name": "Boxed Combinations",
            "source_lineages": [BOXED_COMBO_TRACKER],
            "derived": False,
            "thresholds": {
                "single_red": 501,
                "single_blue": 334,
                "double_red": 1000,
                "double_blue_excluded": [667, 999],
            },
            "by_variant": by_variant,
            "cross_variant": cross_variant,
            "classic_due_doubles_table_2": classic_due_doubles,
        },
        combo_ds,
    )


def build_vtrac_due_block(summary: Mapping[str, Any]) -> Dict[str, Any]:
    vtrac = summary.get("vtrac")
    vtrac = vtrac if isinstance(vtrac, dict) else {}
    top = vtrac.get("overlay_top")
    top = top if isinstance(top, dict) else {}
    heatboard = vtrac.get("heatboard_by_variant")
    heatboard = heatboard if isinstance(heatboard, dict) else {}
    by_variant: Dict[str, Any] = {}
    index_receipts: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)

    for variant in VARIANTS:
        rows = []
        variant_heat = heatboard.get(variant)
        variant_heat = variant_heat if isinstance(variant_heat, dict) else {}
        for raw in top.get(variant, []) if isinstance(top.get(variant), list) else []:
            if not isinstance(raw, dict):
                continue
            idx = int(raw.get("index") or 0)
            metrics = variant_heat.get(str(idx), variant_heat.get(idx, {}))
            metrics = metrics if isinstance(metrics, dict) else {}
            row = {
                "vtrac_index": idx,
                "draws_since": int(raw.get("draws_since") or metrics.get("ds") or 0),
                "avg_gap": metrics.get("avg_gap"),
                "q80_gap": metrics.get("q80_gap"),
                "hazard": metrics.get("hazard"),
                "freq_short": metrics.get("freq_short"),
                "freq_long": metrics.get("freq_long"),
                "trend": metrics.get("trend"),
                "sample_size": metrics.get("sample_size"),
                "variant": variant,
                "source_lineage": VTRAC_DUE_TRACKER,
            }
            rows.append(row)
        _rank_rows(rows)
        for row in rows:
            index_receipts[row["vtrac_index"]].append(dict(row))
        by_variant[variant] = rows

    shared = []
    for idx, receipts in index_receipts.items():
        variants = sorted({row["variant"] for row in receipts})
        if len(variants) < 2:
            continue
        shared.append(
            {
                "vtrac_index": idx,
                "variant_coverage": variants,
                "receipts": receipts,
            }
        )
    shared.sort(
        key=lambda row: (
            -len(row["variant_coverage"]),
            sum(item["rank"] for item in row["receipts"]),
            row["vtrac_index"],
        )
    )
    _rank_rows(shared)
    return {
        "block_id": 3,
        "name": "VTRAC Index Due Ranking",
        "source_lineages": [VTRAC_DUE_TRACKER],
        "derived": False,
        "by_variant": by_variant,
        "cross_variant": {"shared_due_indices": shared},
    }


def build_sums_block(summary: Mapping[str, Any]) -> Dict[str, Any]:
    sums = summary.get("sums")
    sums = sums if isinstance(sums, dict) else {}
    source = sums.get("by_variant")
    source = source if isinstance(source, dict) else {}
    by_variant: Dict[str, Any] = {}

    for variant in VARIANTS:
        payload = source.get(variant)
        payload = payload if isinstance(payload, dict) else {}
        variant_rows: Dict[str, Any] = {}
        for label, key, identity_key in (
            ("ordinary_sums", "by_sum", "sum"),
            ("root_sums", "by_root_sum", "root_sum"),
        ):
            raw_values = payload.get(key)
            raw_values = raw_values if isinstance(raw_values, dict) else {}
            rows = []
            for raw_identity, metrics in raw_values.items():
                if not isinstance(metrics, dict):
                    continue
                flags = _active_flags(metrics)
                if not flags:
                    continue
                row = {
                    identity_key: int(raw_identity),
                    "draws_since": int(metrics.get("draws_since") or 0),
                    "count": int(metrics.get("count") or 0),
                    "expected": float(metrics.get("expected") or 0.0),
                    "z": float(metrics.get("z") or 0.0),
                    "flags": flags,
                    "variant": variant,
                    "source_lineage": SUM_TRACKER,
                }
                rows.append(row)
            rows.sort(
                key=lambda row: (
                    -row["draws_since"],
                    -max((STATUS_SEVERITY[item] for item in row["flags"]), default=0),
                    row[identity_key],
                )
            )
            variant_rows[label] = _rank_rows(rows)
        variant_rows["window"] = int(payload.get("window") or 0)
        by_variant[variant] = variant_rows

    cross_variant: Dict[str, Any] = {}
    for label, identity_key in (
        ("ordinary_sums", "sum"),
        ("root_sums", "root_sum"),
    ):
        grouped: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
        for variant in VARIANTS:
            for row in by_variant[variant][label]:
                grouped[int(row[identity_key])].append(row)
        duplicates = []
        for identity, receipts in grouped.items():
            variants = sorted({row["variant"] for row in receipts})
            if len(variants) < 2:
                continue
            duplicates.append(
                {
                    identity_key: identity,
                    "variant_coverage": variants,
                    "receipts": receipts,
                }
            )
        duplicates.sort(
            key=lambda row: (
                -len(row["variant_coverage"]),
                -sum(item["draws_since"] for item in row["receipts"]),
                row[identity_key],
            )
        )
        _rank_rows(duplicates)
        cross_variant[label] = duplicates

    return {
        "block_id": 4,
        "name": "Sums and Root-Sums Tracking",
        "source_lineages": [SUM_TRACKER],
        "derived": False,
        "by_variant": by_variant,
        "cross_variant": cross_variant,
    }


def _blackapple_status(score: int) -> str:
    if score >= 3:
        return "ALERT"
    if score == 2:
        return "WATCH"
    return "OFF"


def build_blackapple_block(summary: Mapping[str, Any]) -> Dict[str, Any]:
    blackapple = summary.get("blackapple")
    blackapple = blackapple if isinstance(blackapple, dict) else {}
    source = blackapple.get("by_variant")
    source = source if isinstance(source, dict) else {}
    by_variant: Dict[str, Any] = {}

    for variant in VARIANTS:
        payload = source.get(variant)
        payload = payload if isinstance(payload, dict) else {}
        score = int(payload.get("score") or 0)
        candidates = []
        for rank, raw in enumerate(payload.get("candidates") or [], start=1):
            if not isinstance(raw, dict):
                continue
            box = canonical(raw.get("combo"))
            if not box:
                continue
            candidates.append(
                {
                    "rank": rank,
                    "canonical": box,
                    "score": int(raw.get("score") or 0),
                    "tags": sorted(str(item) for item in raw.get("tags") or []),
                    "vtrac_index": get_vtrac_index(box),
                    "variant": variant,
                    "source_lineage": BLACKAPPLE,
                }
            )
        by_variant[variant] = {
            "score": score,
            "status": _blackapple_status(score),
            "active_for_shortlist_convergence": score >= 2,
            "triggers": payload.get("triggers") if isinstance(payload.get("triggers"), dict) else {},
            "candidates": candidates,
        }

    grouped: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)
    for variant, payload in by_variant.items():
        if not payload["active_for_shortlist_convergence"]:
            continue
        for row in payload["candidates"]:
            grouped[row["canonical"]].append(row)
    duplicates = []
    for box, receipts in grouped.items():
        variants = sorted({row["variant"] for row in receipts})
        if len(variants) < 2:
            continue
        duplicates.append(
            {
                "canonical": box,
                "variant_coverage": variants,
                "receipts": receipts,
            }
        )
    duplicates.sort(
        key=lambda row: (
            -len(row["variant_coverage"]),
            min(item["rank"] for item in row["receipts"]),
            row["canonical"],
        )
    )
    _rank_rows(duplicates)
    return {
        "block_id": 5,
        "name": "Blackapple",
        "source_lineages": [BLACKAPPLE],
        "derived": False,
        "by_variant": by_variant,
        "cross_variant": {"active_candidate_duplicates": duplicates},
    }


def build_repeat_watch_block(summary: Mapping[str, Any]) -> Dict[str, Any]:
    source = summary.get("repeat_watch")
    source = source if isinstance(source, dict) else {}
    by_variant: Dict[str, Any] = {}
    current_grouped: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
    last_grouped: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
    for variant in VARIANTS:
        raw = source.get(variant)
        raw = raw if isinstance(raw, dict) else {}
        row = {
            "current_index": int(raw.get("current_index") or 0),
            "current_streak": int(raw.get("current_streak") or 0),
            "active_repeat": int(raw.get("current_streak") or 0) >= 2,
            "last_repeat_gap": int(raw.get("last_repeat_gap") or 0),
            "last_repeat_index": int(raw.get("last_repeat_index") or 0),
            "max_streak": int(raw.get("max_streak") or 0),
            "window": int(raw.get("window") or 0),
            "variant": variant,
            "source_lineage": VTRAC_REPEAT,
        }
        by_variant[variant] = row
        if row["current_index"]:
            current_grouped[row["current_index"]].append(row)
        if row["last_repeat_index"]:
            last_grouped[row["last_repeat_index"]].append(row)

    def shared_rows(
        grouped: Mapping[int, Sequence[Mapping[str, Any]]],
        identity_key: str,
    ) -> list[dict[str, Any]]:
        rows = []
        for idx, receipts in grouped.items():
            variants = sorted({str(row["variant"]) for row in receipts})
            if len(variants) < 2:
                continue
            rows.append(
                {
                    identity_key: idx,
                    "variant_coverage": variants,
                    "receipts": [dict(row) for row in receipts],
                }
            )
        rows.sort(key=lambda row: (-len(row["variant_coverage"]), row[identity_key]))
        return _rank_rows(rows)

    return {
        "block_id": 6,
        "name": "VTRAC Repeat Watch",
        "source_lineages": [VTRAC_REPEAT],
        "derived": False,
        "by_variant": by_variant,
        "cross_variant": {
            "shared_current_indices": shared_rows(current_grouped, "current_index"),
            "shared_last_repeat_indices": shared_rows(
                last_grouped,
                "last_repeat_index",
            ),
        },
    }


def _shape_from_status(status: Mapping[str, Any]) -> str:
    if status.get("shape_red_circle"):
        return "RC"
    if status.get("shape_blue_square"):
        return "BS"
    return ""


def _sum_context(
    summary: Mapping[str, Any],
    *,
    variant: str,
    box: str,
) -> Dict[str, Any]:
    payload = ((summary.get("sums") or {}).get("by_variant") or {}).get(
        variant,
        {},
    )
    payload = payload if isinstance(payload, dict) else {}
    by_sum = payload.get("by_sum")
    by_sum = by_sum if isinstance(by_sum, dict) else {}
    by_root = payload.get("by_root_sum")
    by_root = by_root if isinstance(by_root, dict) else {}
    sum_value = combo_sum(box)
    root_value = digital_root(box)
    sum_metrics = by_sum.get(str(sum_value), by_sum.get(sum_value, {}))
    root_metrics = by_root.get(str(root_value), by_root.get(root_value, {}))
    sum_metrics = sum_metrics if isinstance(sum_metrics, dict) else {}
    root_metrics = root_metrics if isinstance(root_metrics, dict) else {}
    return {
        "sum": sum_value,
        "sum_flags": _active_flags(sum_metrics),
        "root_sum": root_value,
        "root_sum_flags": _active_flags(root_metrics),
    }


def build_badge_concentration_block(
    summary: Mapping[str, Any],
    draws_by_variant: Mapping[str, Sequence[str]],
) -> tuple[Dict[str, Any], Dict[str, Any]]:
    by_variant: Dict[str, list[dict[str, Any]]] = {}
    validation = {
        "selected_rows": 0,
        "qualification_failures": [],
    }

    for variant in VARIANTS:
        draws = list(draws_by_variant.get(variant) or [])[:1000]
        with redirect_stdout(StringIO()):
            statuses = get_vtrac_statuses(draws[:100], draws)
        pair_statuses = (
            ((summary.get("pairs") or {}).get("by_variant") or {})
            .get(variant, {})
            .get("status", {})
        )
        pair_statuses = pair_statuses if isinstance(pair_statuses, dict) else {}
        heatboard = (
            ((summary.get("vtrac") or {}).get("heatboard_by_variant") or {})
            .get(variant, {})
        )
        heatboard = heatboard if isinstance(heatboard, dict) else {}
        rows = []
        for idx in range(1, 36):
            entry = VTRAC_MEMBERS[idx]
            all_members = [
                ("single", box) for box in entry["singles"]
            ] + [("double", box) for box in entry["doubles"]]
            native = statuses.get(idx, {})
            member_rows = []
            pressure_raw = 0
            exact_events = 0
            badge_classes: set[str] = set()
            core_badged_count = 0
            opportunity_mass = 0
            for kind, box in all_members:
                native_group = (
                    native.get("singles_status", {})
                    if kind == "single"
                    else native.get("doubles_status", {})
                )
                native_status = native_group.get(box, {})
                native_status = (
                    native_status if isinstance(native_status, dict) else {}
                )
                pair_badges = [
                    {
                        "pair": pair,
                        "status": str(pair_statuses[pair]),
                    }
                    for pair in combo_pairs(box)
                    if pair in pair_statuses
                ]
                shape = _shape_from_status(native_status)
                core_events = len(pair_badges) + (1 if shape else 0)
                core_badged = core_events > 0
                if core_badged:
                    core_badged_count += 1
                exact_events += core_events
                badge_classes.update(
                    item["status"].upper()[0] for item in pair_badges
                )
                if shape:
                    badge_classes.add(shape)
                color = str(native_status.get("color") or "").lower()
                pressure_raw += STATUS_SEVERITY.get(color, 0)
                pressure_raw += SHAPE_SEVERITY.get(shape, 0)
                opportunity_mass += len(canonical_permutations(box))
                member_rows.append(
                    {
                        "canonical": box,
                        "combo_kind": kind,
                        "core_badged": core_badged,
                        "pair_badges": pair_badges,
                        "shape": shape or None,
                        "draws_since": int(
                            statuses.get(0, {})
                            .get(
                                "singles_ds" if kind == "single" else "doubles_ds",
                                {},
                            )
                            .get(box, len(draws))
                        ),
                        **_sum_context(summary, variant=variant, box=box),
                    }
                )
            total_members = len(member_rows)
            if total_members < 6 or core_badged_count < 4:
                continue
            metrics = heatboard.get(str(idx), heatboard.get(idx, {}))
            metrics = metrics if isinstance(metrics, dict) else {}
            style = native.get("index_style")
            style = style if isinstance(style, dict) else {}
            posture = (
                f"RECENT#{style.get('rank')}"
                if style.get("bg") == "green"
                else f"OVERDUE#{style.get('rank')}"
                if style.get("bg") == "red"
                else "NEUTRAL"
            )
            avg_gap = metrics.get("avg_gap")
            rows.append(
                {
                    "vtrac_index": idx,
                    "member_count": total_members,
                    "core_badged_member_count": core_badged_count,
                    "core_badge_event_count": exact_events,
                    "badge_classes": sorted(badge_classes),
                    "pressure_raw": pressure_raw,
                    "pressure_density": (
                        round(pressure_raw / total_members, 6)
                        if total_members
                        else 0.0
                    ),
                    "opportunity_mass": opportunity_mass,
                    "draws_since": int(metrics.get("ds") or 0),
                    "avg_gap": avg_gap,
                    "q80_gap": metrics.get("q80_gap"),
                    "age_ratio": (
                        round(float(metrics.get("ds") or 0) / float(avg_gap), 6)
                        if avg_gap
                        else None
                    ),
                    "index_posture": posture,
                    "variant": variant,
                    "members": member_rows,
                    "derived_receipt": "BLOCK_7_BADGE_CONCENTRATION",
                    "underlying_source_lineages": [
                        PAIR_TRACKER,
                        BOXED_COMBO_TRACKER,
                    ],
                }
            )
        rows.sort(
            key=lambda row: (
                -row["core_badged_member_count"],
                -row["core_badge_event_count"],
                -row["pressure_raw"],
                -row["pressure_density"],
                -(row["age_ratio"] or 0.0),
                row["vtrac_index"],
            )
        )
        by_variant[variant] = _rank_rows(rows[:8])
        validation["selected_rows"] += len(by_variant[variant])
        for row in by_variant[variant]:
            if row["member_count"] < 6 or row["core_badged_member_count"] < 4:
                validation["qualification_failures"].append(
                    {
                        "variant": variant,
                        "vtrac_index": row["vtrac_index"],
                    }
                )

    grouped: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
    member_grouped: MutableMapping[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for variant, rows in by_variant.items():
        for row in rows:
            grouped[row["vtrac_index"]].append(row)
            for member in row["members"]:
                if member["core_badged"]:
                    member_grouped[(row["vtrac_index"], member["canonical"])].append(
                        {
                            "variant": variant,
                            "rank": row["rank"],
                            "member": member,
                        }
                    )

    shared_indices = []
    for idx, receipts in grouped.items():
        variants = sorted({row["variant"] for row in receipts})
        if len(variants) < 2:
            continue
        shared_indices.append(
            {
                "vtrac_index": idx,
                "variant_coverage": variants,
                "receipts": [
                    {
                        "variant": row["variant"],
                        "rank": row["rank"],
                        "core_badged_member_count": row[
                            "core_badged_member_count"
                        ],
                        "member_count": row["member_count"],
                        "core_badge_event_count": row[
                            "core_badge_event_count"
                        ],
                        "pressure_raw": row["pressure_raw"],
                    }
                    for row in receipts
                ],
            }
        )
    shared_indices.sort(
        key=lambda row: (
            -len(row["variant_coverage"]),
            sum(item["rank"] for item in row["receipts"]),
            row["vtrac_index"],
        )
    )
    _rank_rows(shared_indices)

    duplicate_members = []
    for (idx, box), receipts in member_grouped.items():
        variants = sorted({row["variant"] for row in receipts})
        if len(variants) < 2:
            continue
        duplicate_members.append(
            {
                "vtrac_index": idx,
                "canonical": box,
                "variant_coverage": variants,
                "receipts": receipts,
            }
        )
    duplicate_members.sort(
        key=lambda row: (
            -len(row["variant_coverage"]),
            row["vtrac_index"],
            row["canonical"],
        )
    )
    _rank_rows(duplicate_members)

    return (
        {
            "block_id": 7,
            "name": "VTRAC Badge-Concentration Index",
            "source_lineages": [PAIR_TRACKER, BOXED_COMBO_TRACKER],
            "derived": True,
            "derived_receipt": "BLOCK_7_BADGE_CONCENTRATION",
            "anti_inflation_rule": (
                "Block 7 reorganizes pair and combination badges; it is not an "
                "additional independent source vote."
            ),
            "qualification": {
                "minimum_members": 6,
                "minimum_core_badged_members": 4,
                "display_cap_per_variant": 8,
                "sum_and_root_are_context_only": True,
            },
            "by_variant": by_variant,
            "cross_variant": {
                "shared_selected_indices": shared_indices,
                "duplicate_core_badged_members": duplicate_members,
            },
        },
        validation,
    )


def _profit_rows(
    control_dir: Path,
    *,
    state_key: str,
) -> list[dict[str, Any]]:
    rows = []
    for raw in _read_csv(control_dir / "profit_alerts.csv"):
        if raw.get("StateKey") != state_key:
            continue
        implied = _json_list(raw.get("ImpliedSet"))
        suggested = str(raw.get("Suggested") or "").upper()
        canonical_value = canonical(raw.get("Canonical"))
        candidate_producing = bool(implied) and suggested != "OVERLAY"
        rows.append(
            {
                "variant": str(raw.get("Variant") or "").lower(),
                "alert_id": str(raw.get("AlertId") or ""),
                "strength": int(raw.get("Strength") or 0),
                "suggested": suggested,
                "cap_lines": int(raw.get("CapLines") or 0),
                "decay_draws": int(raw.get("DecayDraws") or 0),
                "badges": [
                    item
                    for item in str(raw.get("Badges") or "").split("/")
                    if item
                ],
                "canonical": canonical_value or None,
                "implied_set": implied,
                "candidate_producing": candidate_producing,
                "order_aware": suggested.startswith("STR8"),
                "promoter_only": suggested == "OVERLAY",
                "source_lineage": PROFIT_ALERTS,
            }
        )
    return rows


def build_shortlist_block(
    block5: Mapping[str, Any],
    positional: Mapping[str, Any],
    *,
    control_dir: Path,
    state_key: str,
) -> tuple[Dict[str, Any], list[dict[str, Any]]]:
    profit_path = control_dir / "profit_alerts.csv"
    compound_path = control_dir / "profit_compound_events.csv"
    source_rows: list[dict[str, Any]] = []
    positional_candidates = []
    for raw in positional.get("candidates") or []:
        if not isinstance(raw, dict):
            continue
        row = {
            "source_family": POSITIONAL,
            "scope": "state",
            "variant": "state",
            "rank": int(raw.get("rank") or 0),
            "literal": normalize_pick3(raw.get("combo")),
            "canonical": canonical(raw.get("canonical") or raw.get("combo")),
            "vtrac_index": raw.get("vtrac_index")
            or get_vtrac_index(raw.get("combo")),
            "order_aware": True,
            "native_score": float(raw.get("score") or 0.0),
            "tags": list(raw.get("tags") or []),
        }
        positional_candidates.append(row)
        source_rows.append(row)

    blackapple_lists: Dict[str, Any] = {}
    for variant in VARIANTS:
        payload = (block5.get("by_variant") or {}).get(variant, {})
        active = bool(payload.get("active_for_shortlist_convergence"))
        rows = []
        if active:
            for raw in payload.get("candidates") or []:
                row = {
                    "source_family": BLACKAPPLE,
                    "scope": "variant",
                    "variant": variant,
                    "rank": int(raw.get("rank") or 0),
                    "literal": None,
                    "canonical": raw.get("canonical"),
                    "vtrac_index": raw.get("vtrac_index"),
                    "order_aware": False,
                    "native_score": int(raw.get("score") or 0),
                    "tags": list(raw.get("tags") or []),
                }
                rows.append(row)
                source_rows.append(row)
        blackapple_lists[variant] = {
            "availability": "LIST" if active else str(payload.get("status") or "OFF"),
            "status": payload.get("status"),
            "candidates": rows,
        }

    profits = _profit_rows(control_dir, state_key=state_key)
    for profit in profits:
        if not profit["candidate_producing"]:
            continue
        if profit["order_aware"]:
            for rank, literal in enumerate(profit["implied_set"], start=1):
                source_rows.append(
                    {
                        "source_family": PROFIT_ALERTS,
                        "scope": "variant",
                        "variant": profit["variant"],
                        "rank": rank,
                        "literal": literal,
                        "canonical": canonical(literal),
                        "vtrac_index": get_vtrac_index(literal),
                        "order_aware": True,
                        "alert_id": profit["alert_id"],
                        "mode": profit["suggested"],
                    }
                )
        else:
            source_rows.append(
                {
                    "source_family": PROFIT_ALERTS,
                    "scope": "variant",
                    "variant": profit["variant"],
                    "rank": 1,
                    "literal": None,
                    "canonical": profit["canonical"],
                    "vtrac_index": get_vtrac_index(profit["canonical"]),
                    "order_aware": False,
                    "alert_id": profit["alert_id"],
                    "mode": profit["suggested"],
                    "implied_set": profit["implied_set"],
                }
            )

    compound_rows = [
        row
        for row in _read_csv(compound_path)
        if row.get("state_key") == state_key or row.get("StateKey") == state_key
    ]

    ordered_grouped: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)
    canonical_grouped: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)
    vtrac_grouped: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
    for row in source_rows:
        if row.get("order_aware") and row.get("literal"):
            ordered_grouped[str(row["literal"])].append(row)
        if row.get("canonical"):
            canonical_grouped[str(row["canonical"])].append(row)
        if row.get("vtrac_index"):
            vtrac_grouped[int(row["vtrac_index"])].append(row)

    def independent_families(
        receipts: Sequence[Mapping[str, Any]],
    ) -> list[str]:
        return sorted({str(row["source_family"]) for row in receipts})

    ordered = []
    for literal, receipts in ordered_grouped.items():
        families = independent_families(receipts)
        if len(families) < 2:
            continue
        ordered.append(
            {
                "literal": literal,
                "source_families": families,
                "receipts": receipts,
            }
        )
    ordered.sort(key=lambda row: (-len(row["source_families"]), row["literal"]))
    _rank_rows(ordered)

    canonical_rows = []
    for box, receipts in canonical_grouped.items():
        families = independent_families(receipts)
        if len(families) < 2:
            continue
        canonical_rows.append(
            {
                "canonical": box,
                "vtrac_index": get_vtrac_index(box),
                "source_families": families,
                "variant_coverage": sorted(
                    {
                        row["variant"]
                        for row in receipts
                        if row.get("variant") in VARIANTS
                    }
                ),
                "receipts": receipts,
            }
        )
    canonical_rows.sort(
        key=lambda row: (
            -len(row["source_families"]),
            -len(row["variant_coverage"]),
            row["canonical"],
        )
    )
    _rank_rows(canonical_rows)

    vtrac_rows = []
    for idx, receipts in vtrac_grouped.items():
        families = independent_families(receipts)
        if len(families) < 2:
            continue
        vtrac_rows.append(
            {
                "vtrac_index": idx,
                "source_families": families,
                "variant_coverage": sorted(
                    {
                        row["variant"]
                        for row in receipts
                        if row.get("variant") in VARIANTS
                    }
                ),
                "receipts": receipts,
            }
        )
    vtrac_rows.sort(
        key=lambda row: (
            -len(row["source_families"]),
            -len(row["variant_coverage"]),
            row["vtrac_index"],
        )
    )
    _rank_rows(vtrac_rows)

    def profit_availability(variant: str) -> str:
        if not profit_path.exists():
            return "SOURCE_MISSING"
        if any(
            row["variant"] == variant and row["candidate_producing"]
            for row in profits
        ):
            return "LIST"
        if any(
            row["variant"] == variant and row["promoter_only"]
            for row in profits
        ):
            return "OVERLAY_ONLY"
        return "NO_EVENT"

    return (
        {
            "block_id": 8,
            "name": "Aux and Control Center Shortlist Convergence",
            "source_lineages": [POSITIONAL, BLACKAPPLE, PROFIT_ALERTS],
            "derived": True,
            "derived_receipt": "BLOCK_8_SHORTLIST_CONVERGENCE",
            "anti_inflation_rule": (
                "One vote per source family per identity. Active variants remain "
                "coverage receipts, not additional independent tools."
            ),
            "availability": {
                "positional": {
                    "midday": "NOT_EMITTED_BY_DESIGN",
                    "evening": "NOT_EMITTED_BY_DESIGN",
                    "combined": "NOT_EMITTED_BY_DESIGN",
                    "state": "LIST" if positional_candidates else "NO_LIST",
                },
                "blackapple": {
                    variant: blackapple_lists[variant]["availability"]
                    for variant in VARIANTS
                },
                "profit_alerts": {
                    variant: profit_availability(variant)
                    for variant in VARIANTS
                },
                "profit_compound_events": (
                    "SOURCE_MISSING"
                    if not compound_path.exists()
                    else "CONTEXT_EVENT"
                    if compound_rows
                    else "NO_EVENT"
                ),
            },
            "positional_state_shortlist": positional_candidates,
            "blackapple_active_shortlists": blackapple_lists,
            "profit_alerts": profits,
            "profit_compound_events": compound_rows,
            "within_block_convergence": {
                "ordered_support": ordered,
                "canonical_support": canonical_rows,
                "vtrac_support": vtrac_rows,
            },
        },
        source_rows,
    )


def _receipt(
    *,
    source_family: str,
    support_level: str,
    variant: str,
    dimension: str,
    block_id: int,
    source_identity: Any,
    rank: Optional[int] = None,
    derived_receipt: Optional[str] = None,
    detail: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    return {
        "source_family": source_family,
        "support_level": support_level,
        "variant": variant,
        "dimension": dimension,
        "block_id": block_id,
        "source_identity": source_identity,
        "rank": rank,
        "derived_receipt": derived_receipt,
        "detail": dict(detail or {}),
    }


def _candidate_canonicals(
    blocks: Mapping[str, Any],
    shortlist_rows: Sequence[Mapping[str, Any]],
) -> set[str]:
    boxes: set[str] = set()
    for variant in VARIANTS:
        combo_payload = blocks["block_2_boxed_combinations"]["by_variant"][variant]
        for row in combo_payload["singles_red_blue"] + combo_payload["doubles_red_only"]:
            boxes.add(row["canonical"])
        for row in blocks["block_7_badge_concentration"]["by_variant"][variant]:
            boxes.update(member["canonical"] for member in row["members"])
    boxes.update(
        str(row["canonical"])
        for row in shortlist_rows
        if row.get("canonical")
    )
    return boxes


def _source_rows_by_canonical(
    blocks: Mapping[str, Any],
    shortlist_rows: Sequence[Mapping[str, Any]],
) -> Dict[str, list[dict[str, Any]]]:
    receipts: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)
    block2 = blocks["block_2_boxed_combinations"]
    for variant in VARIANTS:
        payload = block2["by_variant"][variant]
        for row in payload["singles_red_blue"] + payload["doubles_red_only"]:
            receipts[row["canonical"]].append(
                _receipt(
                    source_family=BOXED_COMBO_TRACKER,
                    support_level="canonical_box",
                    variant=variant,
                    dimension="due_combo",
                    block_id=2,
                    source_identity=row["canonical"],
                    rank=row["rank"],
                    detail={
                        "draws_since": row["draws_since"],
                        "shape": row["shape"],
                    },
                )
            )
    for row in shortlist_rows:
        box = row.get("canonical")
        if not box:
            continue
        source = str(row["source_family"])
        support_level = (
            "exact_literal"
            if row.get("order_aware") and row.get("literal")
            else "canonical_box"
        )
        dimension = {
            BLACKAPPLE: "blackapple_candidate",
            PROFIT_ALERTS: "profit_alert_candidate",
            POSITIONAL: "positional_candidate",
        }.get(source, "candidate")
        receipts[str(box)].append(
            _receipt(
                source_family=source,
                support_level=support_level,
                variant=str(row.get("variant") or "state"),
                dimension=dimension,
                block_id=8 if source != POSITIONAL else 9,
                source_identity=row.get("literal") or box,
                rank=int(row.get("rank") or 0) or None,
                detail={
                    key: row[key]
                    for key in ("alert_id", "mode", "native_score")
                    if key in row
                },
            )
        )
    return dict(receipts)


def _context_receipts_for_canonical(
    box: str,
    blocks: Mapping[str, Any],
) -> list[dict[str, Any]]:
    receipts: list[dict[str, Any]] = []
    pairs = set(combo_pairs(box))
    target_sum = combo_sum(box)
    target_root = digital_root(box)
    target_idx = get_vtrac_index(box)

    block1 = blocks["block_1_due_pairs"]
    for variant in VARIANTS:
        payload = block1["by_variant"][variant]
        for row in payload["repeating_pairs"] + payload["non_repeating_pairs"]:
            if row["pair"] not in pairs:
                continue
            receipts.append(
                _receipt(
                    source_family=PAIR_TRACKER,
                    support_level="pair_facet",
                    variant=variant,
                    dimension="due_pair",
                    block_id=1,
                    source_identity=row["pair"],
                    rank=row["rank"],
                    detail={
                        "status": row["status"],
                        "draws_since": row["draws_since"],
                    },
                )
            )

    block3 = blocks["block_3_vtrac_due"]
    if target_idx:
        for variant in VARIANTS:
            for row in block3["by_variant"][variant]:
                if row["vtrac_index"] != target_idx:
                    continue
                receipts.append(
                    _receipt(
                        source_family=VTRAC_DUE_TRACKER,
                        support_level="vtrac_index",
                        variant=variant,
                        dimension="vtrac_due",
                        block_id=3,
                        source_identity=target_idx,
                        rank=row["rank"],
                        detail={
                            "draws_since": row["draws_since"],
                            "age_ratio": (
                                row["draws_since"] / row["avg_gap"]
                                if row.get("avg_gap")
                                else None
                            ),
                        },
                    )
                )

    block4 = blocks["block_4_sums"]
    for variant in VARIANTS:
        payload = block4["by_variant"][variant]
        for row in payload["ordinary_sums"]:
            if row["sum"] == target_sum:
                receipts.append(
                    _receipt(
                        source_family=SUM_TRACKER,
                        support_level="sum_facet",
                        variant=variant,
                        dimension="sum_posture",
                        block_id=4,
                        source_identity=target_sum,
                        rank=row["rank"],
                        detail={
                            "flags": row["flags"],
                            "draws_since": row["draws_since"],
                            "z": row["z"],
                        },
                    )
                )
        for row in payload["root_sums"]:
            if row["root_sum"] == target_root:
                receipts.append(
                    _receipt(
                        source_family=SUM_TRACKER,
                        support_level="root_sum_facet",
                        variant=variant,
                        dimension="root_sum_posture",
                        block_id=4,
                        source_identity=target_root,
                        rank=row["rank"],
                        detail={
                            "flags": row["flags"],
                            "draws_since": row["draws_since"],
                            "z": row["z"],
                        },
                    )
                )

    block6 = blocks["block_6_repeat_watch"]
    if target_idx:
        for variant in VARIANTS:
            row = block6["by_variant"][variant]
            if row["active_repeat"] and row["current_index"] == target_idx:
                receipts.append(
                    _receipt(
                        source_family=VTRAC_REPEAT,
                        support_level="vtrac_index",
                        variant=variant,
                        dimension="active_vtrac_repeat",
                        block_id=6,
                        source_identity=target_idx,
                        detail={"current_streak": row["current_streak"]},
                    )
                )

    block7 = blocks["block_7_badge_concentration"]
    if target_idx:
        for variant in VARIANTS:
            for row in block7["by_variant"][variant]:
                if row["vtrac_index"] != target_idx:
                    continue
                member = next(
                    (
                        item
                        for item in row["members"]
                        if item["canonical"] == box
                    ),
                    None,
                )
                if not member or not member["core_badged"]:
                    continue
                receipts.append(
                    _receipt(
                        source_family=PAIR_TRACKER,
                        support_level="canonical_facet",
                        variant=variant,
                        dimension="badge_concentration_member",
                        block_id=7,
                        source_identity=box,
                        rank=row["rank"],
                        derived_receipt="BLOCK_7_BADGE_CONCENTRATION",
                        detail={
                            "vtrac_index": target_idx,
                            "pair_badges": member["pair_badges"],
                            "shape": member["shape"],
                        },
                    )
                )
                if member["shape"]:
                    receipts.append(
                        _receipt(
                            source_family=BOXED_COMBO_TRACKER,
                            support_level="canonical_facet",
                            variant=variant,
                            dimension="badge_concentration_member",
                            block_id=7,
                            source_identity=box,
                            rank=row["rank"],
                            derived_receipt="BLOCK_7_BADGE_CONCENTRATION",
                            detail={
                                "vtrac_index": target_idx,
                                "shape": member["shape"],
                            },
                        )
                    )
    return receipts


def _dedupe_receipts(
    receipts: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    seen: set[str] = set()
    result = []
    normalized = sorted(
        (dict(raw) for raw in receipts),
        key=lambda row: json.dumps(
            row,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ),
    )
    for row in normalized:
        key = stable_sha256(
            {
                "source_family": row.get("source_family"),
                "support_level": row.get("support_level"),
                "variant": row.get("variant"),
                "dimension": row.get("dimension"),
                "block_id": row.get("block_id"),
                "source_identity": row.get("source_identity"),
                "derived_receipt": row.get("derived_receipt"),
            }
        )
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result


def _same_variant_coherence(
    receipts: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    by_variant: Dict[str, set[str]] = {variant: set() for variant in VARIANTS}
    state_lineages: set[str] = set()
    for row in receipts:
        source = str(row.get("source_family") or "")
        variant = str(row.get("variant") or "")
        if variant in VARIANTS:
            by_variant[variant].add(source)
        elif variant == "state":
            state_lineages.add(source)
    coherent = [
        variant
        for variant, lineages in by_variant.items()
        if len(lineages) >= 2
    ]
    return {
        "variants": {
            variant: sorted(lineages)
            for variant, lineages in by_variant.items()
            if lineages
        },
        "coherent_variants": coherent,
        "maximum_independent_lineages_in_one_variant": max(
            (len(lineages) for lineages in by_variant.values()),
            default=0,
        ),
        "state_scope_lineages": sorted(state_lineages),
    }


def _build_identity_row(
    *,
    identity_level: str,
    identity: str,
    receipts: Sequence[Mapping[str, Any]],
    derived_receipts: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    unique = _dedupe_receipts(receipts)
    all_lineages = sorted(
        {
            str(row["source_family"])
            for row in unique
            if row.get("source_family") in BASE_SOURCE_FAMILIES
        }
    )
    identity_levels = {
        "exact_literal": {"exact_literal"},
        "ordered_lane": {"exact_literal", "ordered_lane"},
        "canonical_box": {
            "exact_literal",
            "ordered_lane",
            "canonical_box",
            "canonical_facet",
        },
        "vtrac_index": {
            "exact_literal",
            "ordered_lane",
            "canonical_box",
            "canonical_facet",
            "vtrac_index",
        },
    }[identity_level]
    identity_lineages = sorted(
        {
            str(row["source_family"])
            for row in unique
            if row.get("source_family") in CANDIDATE_SOURCE_FAMILIES
            and row.get("support_level") in identity_levels
        }
    )
    order_lineages = sorted(
        {
            str(row["source_family"])
            for row in unique
            if row.get("source_family") in ORDER_AWARE_SOURCE_FAMILIES
            and row.get("support_level") == "exact_literal"
        }
    )
    dimensions = sorted(
        {str(row["dimension"]) for row in unique if row.get("dimension")}
    )
    variants = sorted(
        {
            str(row["variant"])
            for row in unique
            if row.get("variant") in VARIANTS
        }
    )
    coherence = _same_variant_coherence(unique)
    derived = sorted(
        {
            str(value)
            for value in (
                list(derived_receipts or [])
                + [
                    row.get("derived_receipt")
                    for row in unique
                    if row.get("derived_receipt")
                ]
            )
            if value
        }
    )
    burden = _burden(identity_level, identity)
    narrowed_lineages = sorted(
        set(identity_lineages).intersection(
            {BLACKAPPLE, POSITIONAL, PROFIT_ALERTS}
        )
    )
    has_badge_concentration = "BLOCK_7_BADGE_CONCENTRATION" in derived
    has_vtrac_due = "vtrac_due" in dimensions
    has_boxed_combo = BOXED_COMBO_TRACKER in identity_lineages
    has_pair = PAIR_TRACKER in all_lineages
    has_sum = SUM_TRACKER in all_lineages

    if identity_level in {"exact_literal", "ordered_lane"}:
        if len(order_lineages) >= 2:
            review_tier = "TIER_A_INDEPENDENT_IDENTITY"
        elif order_lineages and len(all_lineages) >= 3:
            review_tier = "TIER_B_SOURCE_PLUS_STRUCTURE"
        else:
            review_tier = "NOT_QUALIFIED"
    elif identity_level == "canonical_box":
        if len(identity_lineages) >= 2:
            review_tier = "TIER_A_INDEPENDENT_IDENTITY"
        elif narrowed_lineages and len(all_lineages) >= 3:
            review_tier = "TIER_B_SOURCE_PLUS_STRUCTURE"
        elif has_badge_concentration and has_pair and (has_sum or has_boxed_combo):
            review_tier = "TIER_C_UNTRANSLATED_STRUCTURE"
        else:
            review_tier = "NOT_QUALIFIED"
    else:
        if len(narrowed_lineages) >= 2:
            review_tier = "TIER_A_INDEPENDENT_IDENTITY"
        elif (
            narrowed_lineages
            and (has_badge_concentration or has_vtrac_due)
            and len(all_lineages) >= 3
        ):
            review_tier = "TIER_B_SOURCE_PLUS_STRUCTURE"
        elif (
            not narrowed_lineages
            and has_badge_concentration
            and has_vtrac_due
            and has_boxed_combo
            and len(all_lineages) >= 3
        ):
            review_tier = "TIER_C_UNTRANSLATED_STRUCTURE"
        else:
            review_tier = "NOT_QUALIFIED"

    roles = []
    if identity_level in {"exact_literal", "ordered_lane"} and len(order_lineages) >= 2:
        roles.append("ORDERED_MULTI_SOURCE")
    if identity_level == "canonical_box" and len(identity_lineages) >= 2:
        roles.append("CANONICAL_MULTI_SOURCE")
    if identity_level == "vtrac_index" and len(identity_lineages) >= 2:
        roles.append("VTRAC_TERRITORY_MULTI_SOURCE")
    if PAIR_TRACKER in all_lineages and identity_lineages:
        roles.append("PAIR_ANCHORED_COMPOUND")
    if len(dimensions) >= 3 and identity_lineages:
        roles.append("STRUCTURAL_REINFORCEMENT")
    if burden["exact_literals"] > 36:
        roles.append("BROAD_HIGH_BURDEN")
    if not narrowed_lineages and has_badge_concentration:
        roles.append("UNTRANSLATED_OPPORTUNITY")
    if not roles:
        roles.append("CONTEXT_ONLY")
    return {
        "identity_level": identity_level,
        "identity": identity,
        "vtrac_index": (
            int(identity)
            if identity_level == "vtrac_index"
            else get_vtrac_index(identity)
            if identity_level in {"exact_literal", "canonical_box"}
            else get_vtrac_index(vstraight_lane_for_vcode(identity)[0])
            if identity_level == "ordered_lane"
            and vstraight_lane_for_vcode(identity)
            else None
        ),
        "canonical": (
            canonical(identity)
            if identity_level in {"exact_literal", "canonical_box"}
            else None
        ),
        "ordered_vcode": (
            ordered_vcode_for_combo(identity)
            if identity_level == "exact_literal"
            else identity
            if identity_level == "ordered_lane"
            else None
        ),
        "base_source_lineages": all_lineages,
        "identity_source_lineages": identity_lineages,
        "narrowed_source_lineages": narrowed_lineages,
        "order_aware_source_lineages": order_lineages,
        "derived_receipts": derived,
        "evidence_dimensions": dimensions,
        "variant_coverage": variants,
        "cross_variant_breadth": len(variants),
        "same_variant_coherence": coherence,
        "burden": burden,
        "review_tier": review_tier,
        "review_qualified": review_tier != "NOT_QUALIFIED",
        "merit_gate_receipts": {
            "has_badge_concentration": has_badge_concentration,
            "has_vtrac_due": has_vtrac_due,
            "has_boxed_combo": has_boxed_combo,
            "has_pair": has_pair,
            "has_sum": has_sum,
        },
        "role_labels": roles,
        "receipts": unique,
    }


def build_cross_block_convergence(
    blocks: Mapping[str, Any],
    *,
    shortlist_rows: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    boxes = _candidate_canonicals(blocks, shortlist_rows)
    direct_by_box = _source_rows_by_canonical(blocks, shortlist_rows)
    canonical_rows = []
    exact_receipts: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)
    lane_receipts: MutableMapping[str, list[dict[str, Any]]] = defaultdict(list)

    for box in sorted(boxes):
        receipts = list(direct_by_box.get(box, []))
        receipts.extend(_context_receipts_for_canonical(box, blocks))
        derived = [
            "BLOCK_7_BADGE_CONCENTRATION"
            for row in receipts
            if row.get("derived_receipt") == "BLOCK_7_BADGE_CONCENTRATION"
        ]
        canonical_rows.append(
            _build_identity_row(
                identity_level="canonical_box",
                identity=box,
                receipts=receipts,
                derived_receipts=derived,
            )
        )
        for row in receipts:
            if row.get("support_level") != "exact_literal":
                continue
            literal = normalize_pick3(row.get("source_identity"))
            if not literal:
                continue
            exact_receipts[literal].append(dict(row))
            vcode = ordered_vcode_for_combo(literal)
            if vcode:
                lane_receipts[vcode].append(dict(row))

    exact_rows = [
        _build_identity_row(
            identity_level="exact_literal",
            identity=literal,
            receipts=receipts
            + _context_receipts_for_canonical(canonical(literal), blocks),
        )
        for literal, receipts in sorted(exact_receipts.items())
    ]
    lane_rows = [
        _build_identity_row(
            identity_level="ordered_lane",
            identity=vcode,
            receipts=receipts
            + [
                context
                for box in sorted(
                    {
                        canonical(literal)
                        for literal in vstraight_lane_for_vcode(vcode)
                    }
                )
                for context in _context_receipts_for_canonical(box, blocks)
            ],
        )
        for vcode, receipts in sorted(lane_receipts.items())
    ]

    index_receipts: MutableMapping[int, list[dict[str, Any]]] = defaultdict(list)
    index_derived: MutableMapping[int, set[str]] = defaultdict(set)
    for row in canonical_rows:
        idx = row.get("vtrac_index")
        if not idx:
            continue
        index_receipts[int(idx)].extend(row["receipts"])
        index_derived[int(idx)].update(row["derived_receipts"])
    block3 = blocks["block_3_vtrac_due"]
    for variant in VARIANTS:
        for row in block3["by_variant"][variant]:
            index_receipts[row["vtrac_index"]].append(
                _receipt(
                    source_family=VTRAC_DUE_TRACKER,
                    support_level="vtrac_index",
                    variant=variant,
                    dimension="vtrac_due",
                    block_id=3,
                    source_identity=row["vtrac_index"],
                    rank=row["rank"],
                    detail={"draws_since": row["draws_since"]},
                )
            )
    block6 = blocks["block_6_repeat_watch"]
    for variant in VARIANTS:
        row = block6["by_variant"][variant]
        if not row["active_repeat"]:
            continue
        index_receipts[row["current_index"]].append(
            _receipt(
                source_family=VTRAC_REPEAT,
                support_level="vtrac_index",
                variant=variant,
                dimension="active_vtrac_repeat",
                block_id=6,
                source_identity=row["current_index"],
                detail={"current_streak": row["current_streak"]},
            )
        )
    block7 = blocks["block_7_badge_concentration"]
    for variant in VARIANTS:
        for row in block7["by_variant"][variant]:
            index_derived[row["vtrac_index"]].add(
                "BLOCK_7_BADGE_CONCENTRATION"
            )

    index_rows = [
        _build_identity_row(
            identity_level="vtrac_index",
            identity=str(idx),
            receipts=receipts,
            derived_receipts=index_derived.get(idx, set()),
        )
        for idx, receipts in sorted(index_receipts.items())
    ]

    def include(row: Mapping[str, Any]) -> bool:
        return bool(row["review_qualified"])

    all_rows = [
        row
        for row in exact_rows + lane_rows + canonical_rows + index_rows
        if include(row)
    ]
    all_rows.sort(
        key=lambda row: (
            -IDENTITY_SPECIFICITY[row["identity_level"]],
            -REVIEW_TIER_PRIORITY[row["review_tier"]],
            -len(row["identity_source_lineages"]),
            -len(row["base_source_lineages"]),
            -len(row["evidence_dimensions"]),
            -row["same_variant_coherence"][
                "maximum_independent_lineages_in_one_variant"
            ],
            -row["cross_variant_breadth"],
            row["burden"]["exact_literals"],
            str(row["identity"]),
        )
    )
    _rank_rows(all_rows)

    by_level = {
        level: [row for row in all_rows if row["identity_level"] == level]
        for level in (
            "exact_literal",
            "ordered_lane",
            "canonical_box",
            "vtrac_index",
        )
    }
    by_tier = {
        tier: [row for row in all_rows if row["review_tier"] == tier]
        for tier in (
            "TIER_A_INDEPENDENT_IDENTITY",
            "TIER_B_SOURCE_PLUS_STRUCTURE",
            "TIER_C_UNTRANSLATED_STRUCTURE",
        )
    }

    def row_reference(row: Mapping[str, Any]) -> Dict[str, Any]:
        return {
            "rank": row["rank"],
            "identity_level": row["identity_level"],
            "identity": row["identity"],
            "review_tier": row["review_tier"],
            "exact_literal_burden": row["burden"]["exact_literals"],
        }

    return {
        "block_id": 10,
        "name": "AUX CORE Cross-Block Compound Convergence",
        "source_lineages": list(BASE_SOURCE_FAMILIES),
        "derived": True,
        "derived_receipt": "BLOCK_10_CROSS_BLOCK_CONVERGENCE",
        "contract": {
            "identity_ladder": [
                "vtrac_index",
                "canonical_box",
                "ordered_lane",
                "exact_literal",
            ],
            "report_order": "REVIEW_ORDER_NOT_CALIBRATED",
            "raw_scores_combined": False,
            "winner_fields_allowed": False,
            "anti_inflation_rules": [
                "Each base source family counts once per identity.",
                "Midday, Evening, and Combined are breadth receipts, not tools.",
                "Combined overlaps Midday and Evening and is never independent credit.",
                "Block 7 and Block 8 are derived receipts, not source votes.",
                "Pairs and sums annotate established identities; they do not manufacture candidates.",
                "BOX alert permutations receive canonical, not straight-order, credit.",
            ],
            "merit_tiers": {
                "TIER_A_INDEPENDENT_IDENTITY": (
                    "Multiple independent identity-producing sources agree at "
                    "the row's specificity."
                ),
                "TIER_B_SOURCE_PLUS_STRUCTURE": (
                    "A narrowed source is reinforced by independent structural "
                    "lineage and either badge concentration or VTRAC-due posture "
                    "at index level."
                ),
                "TIER_C_UNTRANSLATED_STRUCTURE": (
                    "No narrowed source completed the identity, but bounded "
                    "badge concentration and compatible structural receipts "
                    "preserved an explicit extraction opportunity."
                ),
            },
            "review_surfaces": {
                "independent_identity_convergence": (
                    "Tier A identities supported independently at the reported "
                    "specificity."
                ),
                "narrowed_source_plus_structure": (
                    "Tier B identities emitted by a narrowed source and "
                    "reinforced by separate structural evidence."
                ),
                "untranslated_structure": (
                    "Tier C structural extraction opportunities that were not "
                    "emitted by a narrowed source at the reported specificity."
                ),
                "complete_qualified_lattice": (
                    "All Tier A, B, and C rows retained for audit and "
                    "reverse-engineering."
                ),
            },
        },
        "rows": all_rows,
        "by_identity_level": by_level,
        "review_views": {
            "independent_identity_convergence": [
                row_reference(row)
                for row in by_tier["TIER_A_INDEPENDENT_IDENTITY"]
            ],
            "narrowed_source_plus_structure": [
                row_reference(row)
                for row in by_tier["TIER_B_SOURCE_PLUS_STRUCTURE"]
            ],
            "untranslated_structure": [
                row_reference(row)
                for row in by_tier["TIER_C_UNTRANSLATED_STRUCTURE"]
            ],
        },
        "inventory": {
            "candidate_canonicals_considered": len(boxes),
            "exact_literals_considered": len(exact_rows),
            "ordered_lanes_considered": len(lane_rows),
            "vtrac_indices_considered": len(index_rows),
            "qualifying_rows": len(all_rows),
            "narrowed_rows": sum(
                1
                for row in all_rows
                if row["review_tier"] in NARROWED_REVIEW_TIERS
            ),
            "untranslated_structure_rows": len(
                by_tier["TIER_C_UNTRANSLATED_STRUCTURE"]
            ),
            "rows_by_tier": {
                tier: len(rows) for tier, rows in by_tier.items()
            },
            "rows_by_identity_level": {
                level: len(rows) for level, rows in by_level.items()
            },
        },
    }


def build_aux_core(
    *,
    state_key: str,
    results_date: str,
    day_dir: Path,
    profile: str = "frozen_native_aux",
) -> Dict[str, Any]:
    day_dir = day_dir.resolve()
    state_dir = day_dir / state_key
    summary_path = state_dir / "aux" / state_key / "summary.json"
    draws_dir = state_dir / "aux" / "draws"
    control_dir = day_dir / "control_center"
    if not summary_path.exists():
        raise FileNotFoundError(f"Missing Aux summary: {safe_rel(summary_path)}")
    if not draws_dir.exists():
        raise FileNotFoundError(f"Missing Aux draw snapshots: {safe_rel(draws_dir)}")

    summary = _read_json(summary_path)
    draws_by_variant, draw_provenance = load_frozen_draws(
        state_key,
        draws_dir,
        max_n=1000,
    )
    missing_variants = [
        variant for variant in VARIANTS if variant not in draws_by_variant
    ]
    if missing_variants:
        raise ValueError(
            f"Missing frozen draw variants for {state_key}: {missing_variants}"
        )

    positional = build_lossless_report(
        state_key=state_key,
        results_date=results_date,
        draws_dir=draws_dir,
        profile="native_all_variant",
        max_n=1000,
        window=int((summary.get("config") or {}).get("POSITIONAL_WINDOW") or 360),
        topk=3,
    )

    block1 = build_due_pairs_block(summary)
    block2, _combo_ds = build_boxed_combinations_block(summary, draws_by_variant)
    block3 = build_vtrac_due_block(summary)
    block4 = build_sums_block(summary)
    block5 = build_blackapple_block(summary)
    block6 = build_repeat_watch_block(summary)
    block7, block7_validation = build_badge_concentration_block(
        summary,
        draws_by_variant,
    )
    block9 = {
        "block_id": 9,
        "name": "Full Positional Tracker Evidence",
        "source_lineages": [POSITIONAL],
        "derived": False,
        "payload": positional,
    }
    partial_blocks = {
        "block_1_due_pairs": block1,
        "block_2_boxed_combinations": block2,
        "block_3_vtrac_due": block3,
        "block_4_sums": block4,
        "block_5_blackapple": block5,
        "block_6_repeat_watch": block6,
        "block_7_badge_concentration": block7,
    }
    block8, shortlist_rows = build_shortlist_block(
        block5,
        positional,
        control_dir=control_dir,
        state_key=state_key,
    )
    blocks = {
        **partial_blocks,
        "block_8_shortlist_convergence": block8,
        "block_9_positional": block9,
    }
    block10 = build_cross_block_convergence(
        blocks,
        shortlist_rows=shortlist_rows,
    )
    blocks["block_10_cross_block_convergence"] = block10

    control_requirements = {
        "blackapple_alerts.csv": True,
        "profit_alerts.csv": True,
        "profit_compound_events.csv": False,
        "vtrac_repeat_watch.csv": True,
    }
    payload: Dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "metadata": {
            "state_key": state_key,
            "results_date": results_date,
            "profile": profile,
            "source_is_frozen_pre_result": True,
            "winner_fields_present": False,
            "runtime_behavior_changed": False,
            "review_order": "REVIEW_ORDER_NOT_CALIBRATED",
        },
        "contract": {
            "purpose": (
                "Lossless Aux evidence inventory plus lineage-aware Deep Review "
                "convergence; not a production score or final prediction slate."
            ),
            "base_source_families": list(BASE_SOURCE_FAMILIES),
            "derived_receipts": sorted(DERIVED_RECEIPTS),
            "variant_semantics": {
                "midday": "native draw variant",
                "evening": "native draw variant",
                "combined": "overlapping analytical lens",
                "state": "state-level synthesis scope, not a fourth variant",
            },
            "identity_ladder": [
                "vtrac_index",
                "canonical_box",
                "ordered_lane",
                "exact_literal",
            ],
        },
        "source_provenance": {
            "aux_summary": _provenance(summary_path, required=True),
            "draw_snapshots": draw_provenance,
            "control_center": {
                name: _provenance(control_dir / name, required=required)
                for name, required in control_requirements.items()
            },
        },
        "blocks": blocks,
        "validation": {
            "required_blocks_present": list(range(1, 11)),
            "missing_draw_variants": missing_variants,
            "block_7": block7_validation,
            "forbidden_result_key_paths": [],
        },
    }
    forbidden_paths = _forbidden_result_paths(payload)
    if forbidden_paths:
        raise ValueError(
            "Pre-result AUX CORE payload contains result fields: "
            + ", ".join(forbidden_paths[:10])
        )
    payload["validation"]["forbidden_result_key_paths"] = forbidden_paths
    payload["frozen_object_sha256"] = stable_sha256(payload)
    return payload


def _winner_pair_alignment(
    block1: Mapping[str, Any],
    *,
    winner: str,
) -> Dict[str, Any]:
    target_pairs = set(combo_pairs(winner))
    receipts = []
    for variant in VARIANTS:
        payload = block1["by_variant"][variant]
        for row in payload["repeating_pairs"] + payload["non_repeating_pairs"]:
            if row["pair"] in target_pairs:
                receipts.append(row)
    return {
        "winner_pairs": sorted(target_pairs),
        "aligned": bool(receipts),
        "receipts": receipts,
    }


def grade_winner(
    payload: Mapping[str, Any],
    *,
    period: str,
    winner: str,
) -> Dict[str, Any]:
    literal = normalize_pick3(winner)
    if not literal:
        raise ValueError(f"Invalid Pick-3 winner: {winner!r}")
    period_title = period.title()
    if period_title not in PERIOD_VARIANTS:
        raise ValueError(f"Unsupported period: {period!r}")
    target_variant = PERIOD_VARIANTS[period_title]
    box = canonical(literal)
    idx = get_vtrac_index(literal)
    vcode = ordered_vcode_for_combo(literal)
    blocks = payload["blocks"]

    block2_rows = (
        blocks["block_2_boxed_combinations"]["by_variant"][target_variant][
            "singles_red_blue"
        ]
        + blocks["block_2_boxed_combinations"]["by_variant"][target_variant][
            "doubles_red_only"
        ]
    )
    block3_rows = blocks["block_3_vtrac_due"]["by_variant"][target_variant]
    block4_rows = blocks["block_4_sums"]["by_variant"][target_variant]
    block5 = blocks["block_5_blackapple"]["by_variant"][target_variant]
    block6 = blocks["block_6_repeat_watch"]["by_variant"][target_variant]
    block7_rows = blocks["block_7_badge_concentration"]["by_variant"][
        target_variant
    ]
    block8 = blocks["block_8_shortlist_convergence"]
    positional_payload = blocks["block_9_positional"]["payload"]
    block10 = blocks["block_10_cross_block_convergence"]

    exact_row = next(
        (
            row
            for row in block10["by_identity_level"]["exact_literal"]
            if row["identity"] == literal
        ),
        None,
    )
    lane_row = next(
        (
            row
            for row in block10["by_identity_level"]["ordered_lane"]
            if row["identity"] == vcode
        ),
        None,
    )
    canonical_row = next(
        (
            row
            for row in block10["by_identity_level"]["canonical_box"]
            if row["identity"] == box
        ),
        None,
    )
    index_row = next(
        (
            row
            for row in block10["by_identity_level"]["vtrac_index"]
            if int(row["identity"]) == idx
        ),
        None,
    )

    sum_value = combo_sum(literal)
    root_value = digital_root(literal)
    sum_receipts = [
        row for row in block4_rows["ordinary_sums"] if row["sum"] == sum_value
    ]
    root_receipts = [
        row for row in block4_rows["root_sums"] if row["root_sum"] == root_value
    ]
    ba_candidates = [
        row for row in block5["candidates"] if row["canonical"] == box
    ]
    block7_index = [
        row for row in block7_rows if row["vtrac_index"] == idx
    ]
    block7_member = [
        {
            "index_rank": row["rank"],
            "member": member,
        }
        for row in block7_index
        for member in row["members"]
        if member["canonical"] == box
    ]
    shortlist_exact = [
        row
        for row in block8["positional_state_shortlist"]
        if row.get("literal") == literal
    ]
    shortlist_canonical = [
        row
        for source in (
            block8["positional_state_shortlist"],
            *[
                block8["blackapple_active_shortlists"][variant]["candidates"]
                for variant in VARIANTS
            ],
        )
        for row in source
        if row.get("canonical") == box
    ]
    profit_rows = [
        row
        for row in block8["profit_alerts"]
        if row.get("candidate_producing")
        and (
            row.get("canonical") == box
            or literal in row.get("implied_set", [])
        )
    ]
    positional_grade = grade_positional_winner(
        positional_payload,
        period=period_title,
        winner=literal,
    )

    if exact_row:
        highest_level = "exact_literal"
    elif lane_row:
        highest_level = "ordered_lane"
    elif canonical_row:
        highest_level = "canonical_box"
    elif index_row:
        highest_level = "vtrac_index"
    else:
        highest_level = "no_cross_block_identity"

    matched_rows = {
        "exact_literal": exact_row,
        "ordered_lane": lane_row,
        "canonical_box": canonical_row,
        "vtrac_index": index_row,
    }
    narrowed_rows = {
        level: row
        for level, row in matched_rows.items()
        if row and row["review_tier"] in NARROWED_REVIEW_TIERS
    }
    untranslated_rows = {
        level: row
        for level, row in matched_rows.items()
        if row and row["review_tier"] == "TIER_C_UNTRANSLATED_STRUCTURE"
    }

    def highest_matched_level(rows: Mapping[str, Any], *, empty: str) -> str:
        return next(
            (
                level
                for level in (
                    "exact_literal",
                    "ordered_lane",
                    "canonical_box",
                    "vtrac_index",
                )
                if rows.get(level)
            ),
            empty,
        )

    highest_narrowed_level = highest_matched_level(
        narrowed_rows,
        empty="no_narrowed_identity",
    )
    highest_untranslated_level = highest_matched_level(
        untranslated_rows,
        empty="no_untranslated_structure",
    )

    def translation_gap(
        rows: Mapping[str, Any],
        *,
        empty: str,
    ) -> str:
        if rows.get("exact_literal"):
            return "NONE"
        if rows.get("ordered_lane"):
            return "ORDERED_LANE_TO_LITERAL"
        if rows.get("canonical_box"):
            return "CANONICAL_TO_ORDER"
        if rows.get("vtrac_index"):
            return "VTRAC_TO_CANONICAL"
        return empty

    return {
        "winner_join_phase": "post_result_reverse_engineering",
        "frozen_object_sha256": payload.get("frozen_object_sha256"),
        "credit_boundary": (
            "The frozen object proves what evidence existed before the result. "
            "This post-result join evaluates how that evidence related to the "
            "winner and cannot alter the frozen object."
        ),
        "state_key": payload["metadata"]["state_key"],
        "results_date": payload["metadata"]["results_date"],
        "period": period_title,
        "target_variant": target_variant,
        "winner": literal,
        "winner_canonical": box,
        "winner_vtrac_index": idx,
        "winner_ordered_vcode": vcode,
        "winner_sum": sum_value,
        "winner_root_sum": root_value,
        "block_alignment": {
            "block_1_due_pairs": _winner_pair_alignment(
                blocks["block_1_due_pairs"],
                winner=literal,
            ),
            "block_2_boxed_combinations": {
                "target_variant_canonical_match": [
                    row for row in block2_rows if row["canonical"] == box
                ]
            },
            "block_3_vtrac_due": {
                "target_variant_index_match": [
                    row for row in block3_rows if row["vtrac_index"] == idx
                ]
            },
            "block_4_sums": {
                "target_variant_sum_match": sum_receipts,
                "target_variant_root_sum_match": root_receipts,
            },
            "block_5_blackapple": {
                "status": block5["status"],
                "active": block5["active_for_shortlist_convergence"],
                "canonical_match": ba_candidates,
            },
            "block_6_repeat_watch": {
                "active_current_index_match": bool(
                    block6["active_repeat"] and block6["current_index"] == idx
                ),
                "last_repeat_index_match": block6["last_repeat_index"] == idx,
                "receipt": block6,
            },
            "block_7_badge_concentration": {
                "selected_index_match": block7_index,
                "canonical_member_match": block7_member,
            },
            "block_8_shortlist_convergence": {
                "positional_exact_match": shortlist_exact,
                "canonical_matches": shortlist_canonical,
                "profit_alert_matches": profit_rows,
            },
            "block_9_positional": positional_grade,
            "block_10_cross_block_convergence": {
                "highest_specificity_reached": highest_level,
                "highest_narrowed_specificity": highest_narrowed_level,
                "highest_untranslated_specificity": highest_untranslated_level,
                "exact_literal": exact_row,
                "ordered_lane": lane_row,
                "canonical_box": canonical_row,
                "vtrac_index": index_row,
            },
        },
        "conversion_read": {
            "exact_literal_expressed": bool(exact_row),
            "ordered_lane_expressed": bool(lane_row),
            "canonical_box_expressed": bool(canonical_row),
            "vtrac_territory_expressed": bool(index_row),
            "highest_specificity_reached": highest_level,
            "highest_specificity_tier": (
                matched_rows[highest_level]["review_tier"]
                if highest_level in matched_rows
                else "NO_MATCH"
            ),
            "translation_gap": translation_gap(
                matched_rows,
                empty="NO_COMPOUND_ALIGNMENT",
            ),
            "highest_narrowed_specificity": highest_narrowed_level,
            "narrowed_translation_gap": translation_gap(
                narrowed_rows,
                empty="NO_NARROWED_ALIGNMENT",
            ),
            "highest_untranslated_specificity": highest_untranslated_level,
            "exact_literal_narrowed": "exact_literal" in narrowed_rows,
            "ordered_lane_narrowed": "ordered_lane" in narrowed_rows,
            "canonical_box_narrowed": "canonical_box" in narrowed_rows,
            "vtrac_territory_narrowed": "vtrac_index" in narrowed_rows,
            "canonical_untranslated_structure": (
                "canonical_box" in untranslated_rows
            ),
            "vtrac_untranslated_structure": "vtrac_index" in untranslated_rows,
        },
    }


def _short_receipt(row: Mapping[str, Any]) -> str:
    return (
        f"{row.get('source_family')}:{row.get('variant')}:"
        f"{row.get('dimension')}"
    )


def _md_cell(value: Any) -> str:
    text = str(value if value is not None else "-")
    return text.replace("|", "\\|").replace("\n", " ").strip() or "-"


def _append_variant_grid(
    lines: list[str],
    *,
    title: str,
    rows_by_variant: Mapping[str, Sequence[Mapping[str, Any]]],
    formatter: Any,
) -> None:
    lines.extend(
        [
            f"### {title}",
            "",
            "| Rank | Midday | Evening | Combined |",
            "|---:|---|---|---|",
        ]
    )
    maximum = max(
        (len(rows_by_variant.get(variant) or []) for variant in DISPLAY_VARIANTS),
        default=0,
    )
    if maximum == 0:
        lines.extend(["| - | - | - | - |", ""])
        return
    for index in range(maximum):
        cells = []
        for variant in DISPLAY_VARIANTS:
            rows = rows_by_variant.get(variant) or []
            cells.append(
                _md_cell(formatter(rows[index])) if index < len(rows) else "-"
            )
        lines.append(f"| {index + 1} | {' | '.join(cells)} |")
    lines.append("")


def _pair_text(row: Mapping[str, Any]) -> str:
    return (
        f"`{row.get('pair')}` - {row.get('draws_since')} DS "
        f"[{str(row.get('status') or '').upper()}] "
        f"[VP{row.get('vtrac_pair_family')}]"
    )


def _combo_text(row: Mapping[str, Any]) -> str:
    pair_badges = row.get("pair_badges") or []
    pair_text = ",".join(
        f"{item.get('pair')}:{str(item.get('status') or '').upper()[0:1]}"
        for item in pair_badges
    )
    suffix = f" [{pair_text}]" if pair_text else ""
    return (
        f"`{row.get('canonical')}` - {row.get('draws_since')} DS "
        f"[{row.get('shape')}] [VT{row.get('vtrac_index')}]{suffix}"
    )


def _due_vtrac_text(row: Mapping[str, Any]) -> str:
    return (
        f"`VT{row.get('vtrac_index')}` - {row.get('draws_since')} DS; "
        f"AVG={row.get('avg_gap')}; Q80={row.get('q80_gap')}; "
        f"HZ={row.get('hazard')}; T={row.get('trend')}; "
        f"N={row.get('sample_size')}"
    )


def _sum_text(row: Mapping[str, Any], *, root: bool = False) -> str:
    identity = row.get("root_sum") if root else row.get("sum")
    flags = ",".join(str(flag).upper() for flag in row.get("flags") or [])
    return (
        f"`{identity}` - {row.get('draws_since')} DS; "
        f"H={row.get('count')}/{row.get('expected')}; "
        f"Z={row.get('z')}; [{flags or 'NEUTRAL'}]"
    )


def _classic_due_boxes(slot: Mapping[str, Any]) -> str:
    grouped: MutableMapping[str, list[str]] = defaultdict(list)
    for row in slot.get("red_boxes") or []:
        grouped[str(row.get("combo"))].append(str(row.get("badge")))
    if not grouped:
        return "-"
    return ", ".join(
        f"`{combo}`[{'+'.join(sorted(set(badges), key='CME'.index))}]"
        for combo, badges in sorted(grouped.items())
    )


def _badge_member_text(member: Mapping[str, Any]) -> str:
    pair_badges = ",".join(
        f"{item.get('pair')}:{str(item.get('status') or '').upper()[0:1]}"
        for item in member.get("pair_badges") or []
    )
    badges = [str(member.get("shape") or "")]
    if pair_badges:
        badges.append(pair_badges)
    badges = [badge for badge in badges if badge]
    return (
        f"{member.get('canonical')}:{member.get('draws_since')}DS"
        f"[{';'.join(badges) or '-'}]"
    )


def _badge_index_text(row: Mapping[str, Any]) -> str:
    members = ", ".join(
        _badge_member_text(member) for member in row.get("members") or []
    )
    return (
        f"`VT{row.get('vtrac_index')}` B="
        f"{row.get('core_badged_member_count')}/{row.get('member_count')} "
        f"E={row.get('core_badge_event_count')} "
        f"V={','.join(row.get('badge_classes') or [])} "
        f"DS={row.get('draws_since')} [{row.get('index_posture')}] "
        f"{{{members}}}"
    )


def render_external_markdown(payload: Mapping[str, Any]) -> str:
    """Render a bounded, human-readable pre-result AUX CORE report."""
    meta = payload["metadata"]
    blocks = payload["blocks"]
    lines = [
        f"# AUX CORE Full Pre-Result Report - {meta['state_key']}",
        "",
        "## Scope and provenance",
        "",
        f"- Results date: `{meta['results_date']}`",
        f"- Profile: `{meta['profile']}`",
        f"- Frozen pre-result object: `{meta['source_is_frozen_pre_result']}`",
        f"- Winner fields present: `{meta['winner_fields_present']}`",
        f"- Frozen SHA-256: `{payload.get('frozen_object_sha256')}`",
        f"- Review ordering: `{meta['review_order']}`",
        "",
        "This document is a readable projection of frozen AUX CORE evidence. It "
        "does not alter Aux, Analysis Arena, Candidate Universe, Play Cards, or "
        "runtime scoring.",
        "",
        "## Complete legend",
        "",
        "- `M / E / C`: Midday, Evening, and Combined. Combined is an "
        "overlapping analytical lens, not an independent fourth source.",
        "- `R / B / P`: Red, Blue, and Purple due/status bands.",
        "- `RC / BS`: Red-circle and blue-square boxed-combination bands.",
        "- `DS`: draws since last observed.",
        "- `VT#`: boxed VTRAC index. `VP#` is a two-digit VTRAC pair family.",
        "- `AVG / Q80 / HZ / T / N`: average gap, 80th-percentile gap, "
        "hazard, short-minus-long trend, and sample size.",
        "- `H observed/expected / Z`: sum frequency receipt and z-score.",
        "- `XVAR-DUP`: the same literal independently qualifies in multiple "
        "variants. `XVAR-VT` is a shared boxed VTRAC family relation.",
        "- `LIST / OFF / NO_EVENT / OVERLAY_ONLY / NOT_EMITTED_BY_DESIGN`: "
        "explicit shortlist availability states.",
        "- `POSITIONAL_REINFORCEMENT / ORDERING_SUPPORT / VTRAC_TERRITORY / "
        "BOUNDED_CANDIDATE / CONTRADICTION / NO_ALIGNMENT`: Positional roles.",
        "- `Tier A`: independent identity convergence. `Tier B`: a narrowed "
        "source plus structural support. `Tier C`: untranslated structure only.",
        "- Doubles Table 2 uses Combined to rank the top four repeated pairs; "
        "C/M/E badges identify where a boxed double independently met the "
        "1,000-draw red threshold. Its closure is generated structure.",
        "- Blocks 7, 8, 10, and Doubles Table 2 reorganize base evidence and "
        "cannot create extra independent-source votes.",
        "",
    ]

    block1 = blocks["block_1_due_pairs"]
    lines.extend(["## Block 1: Due Pairs", ""])
    for key, title in (
        ("repeating_pairs", "Repeating pairs"),
        ("non_repeating_pairs", "Non-repeating pairs"),
    ):
        _append_variant_grid(
            lines,
            title=title,
            rows_by_variant={
                variant: block1["by_variant"][variant][key]
                for variant in DISPLAY_VARIANTS
            },
            formatter=_pair_text,
        )
    duplicate_pairs = block1["cross_variant"]["exact_duplicates"]
    lines.extend(
        [
            "### Cross-variant duplicate pairs",
            "",
            "| Rank | Pair | Variants | Receipts |",
            "|---:|---|---|---|",
        ]
    )
    for row in duplicate_pairs:
        receipts = ", ".join(
            f"{_variant_tag(item['variant'])}:{str(item['status']).upper()}"
            f"/{item['draws_since']}"
            for item in row.get("receipts") or []
        )
        lines.append(
            f"| {row['rank']} | `{row['pair']}` | "
            f"{'+'.join(_variant_tag(v) for v in row['variant_coverage'])} | "
            f"{_md_cell(receipts)} |"
        )
    if not duplicate_pairs:
        lines.append("| - | - | - | - |")
    lines.append("")

    block2 = blocks["block_2_boxed_combinations"]
    lines.extend(["## Block 2: Boxed Combinations", ""])
    for key, title in (
        ("singles_red_blue", "Singles: Red and Blue"),
        ("doubles_red_only", "Doubles: Red only"),
    ):
        _append_variant_grid(
            lines,
            title=title,
            rows_by_variant={
                variant: block2["by_variant"][variant][key]
                for variant in DISPLAY_VARIANTS
            },
            formatter=_combo_text,
        )
    classic = block2["classic_due_doubles_table_2"]
    lines.extend(
        [
            "### Doubles Table 2: Top-four due pairs and red boxed combinations",
            "",
            "| Rank | Combined due pair | Red boxed combinations by source |",
            "|---:|---|---|",
        ]
    )
    for slot in classic.get("pair_slots") or []:
        lines.append(
            f"| {slot['rank']} | `{slot['pair']}` - "
            f"{slot['draws_since']} DS [{slot['band']}] | "
            f"{_md_cell(_classic_due_boxes(slot))} |"
        )
    coverage_text = ", ".join(
        f"{item['badge']}={item['draws_used']}"
        for item in classic.get("coverage") or []
    )
    lines.extend(
        [
            "",
            f"- Generated top-four closure: "
            f"`{', '.join(classic.get('closure') or []) or 'none'}`",
            f"- Coverage: `{coverage_text or 'none'}`",
            f"- Credit boundary: {classic['credit_boundary']}",
            "",
        ]
    )

    block3 = blocks["block_3_vtrac_due"]
    lines.extend(["## Block 3: VTRAC Index Due Ranking", ""])
    _append_variant_grid(
        lines,
        title="Due VTRAC indices",
        rows_by_variant=block3["by_variant"],
        formatter=_due_vtrac_text,
    )

    block4 = blocks["block_4_sums"]
    lines.extend(["## Block 4: Sums and Root Sums", ""])
    _append_variant_grid(
        lines,
        title="Ordinary sums",
        rows_by_variant={
            variant: block4["by_variant"][variant]["ordinary_sums"]
            for variant in DISPLAY_VARIANTS
        },
        formatter=_sum_text,
    )
    _append_variant_grid(
        lines,
        title="Root sums",
        rows_by_variant={
            variant: block4["by_variant"][variant]["root_sums"]
            for variant in DISPLAY_VARIANTS
        },
        formatter=lambda row: _sum_text(row, root=True),
    )

    block5 = blocks["block_5_blackapple"]
    lines.extend(
        [
            "## Block 5: Blackapple",
            "",
            "| Variant | Status | Active for shortlist | Score | Candidates |",
            "|---|---|---|---:|---|",
        ]
    )
    for variant in DISPLAY_VARIANTS:
        row = block5["by_variant"][variant]
        candidates = ", ".join(
            f"{item['canonical']}(VT{item['vtrac_index']},S{item['score']})"
            for item in row.get("candidates") or []
        )
        lines.append(
            f"| {_variant_tag(variant)} | `{row.get('status')}` | "
            f"`{row.get('active_for_shortlist_convergence')}` | "
            f"{row.get('score')} | {_md_cell(candidates)} |"
        )
    lines.append("")

    block6 = blocks["block_6_repeat_watch"]
    lines.extend(
        [
            "## Block 6: VTRAC Repeat Watch",
            "",
            "| Variant | Current VT | Streak | Active | Last repeat VT | "
            "Last gap | Max streak |",
            "|---|---:|---:|---|---:|---:|---:|",
        ]
    )
    for variant in DISPLAY_VARIANTS:
        row = block6["by_variant"][variant]
        lines.append(
            f"| {_variant_tag(variant)} | {row.get('current_index')} | "
            f"{row.get('current_streak')} | `{row.get('active_repeat')}` | "
            f"{row.get('last_repeat_index')} | {row.get('last_repeat_gap')} | "
            f"{row.get('max_streak')} |"
        )
    lines.append("")

    block7 = blocks["block_7_badge_concentration"]
    lines.extend(["## Block 7: VTRAC Badge-Concentration Index", ""])
    _append_variant_grid(
        lines,
        title="Selected badge neighborhoods",
        rows_by_variant=block7["by_variant"],
        formatter=_badge_index_text,
    )
    shared_indices = block7["cross_variant"]["shared_selected_indices"]
    lines.extend(
        [
            "### Shared selected indices",
            "",
            "| Rank | VTRAC index | Variants |",
            "|---:|---:|---|",
        ]
    )
    for row in shared_indices:
        lines.append(
            f"| {row['rank']} | VT{row['vtrac_index']} | "
            f"{'+'.join(_variant_tag(v) for v in row['variant_coverage'])} |"
        )
    if not shared_indices:
        lines.append("| - | - | - |")
    lines.extend(["", block7["anti_inflation_rule"], ""])

    block8 = blocks["block_8_shortlist_convergence"]
    lines.extend(
        [
            "## Block 8: Aux and Control Center Shortlists",
            "",
            "### Availability",
            "",
            "| Source | Midday | Evening | Combined | State |",
            "|---|---|---|---|---|",
        ]
    )
    availability = block8["availability"]
    for source in ("blackapple", "positional", "profit_alerts"):
        row = availability.get(source) or {}
        lines.append(
            f"| `{source}` | `{row.get('midday', '-')}` | "
            f"`{row.get('evening', '-')}` | `{row.get('combined', '-')}` | "
            f"`{row.get('state', '-')}` |"
        )
    lines.extend(
        [
            f"| `profit_compound_events` | "
            f"`{availability.get('profit_compound_events', '-')}` | - | - | - |",
            "",
            "### Positional state shortlist",
            "",
            "| Rank | Literal | Canonical | VT | Native score | Tags |",
            "|---:|---|---|---:|---:|---|",
        ]
    )
    for row in block8["positional_state_shortlist"]:
        lines.append(
            f"| {row['rank']} | `{row['literal']}` | `{row['canonical']}` | "
            f"{row['vtrac_index']} | {float(row['native_score']):.4f} | "
            f"{_md_cell(', '.join(row.get('tags') or []))} |"
        )
    lines.extend(
        [
            "",
            "### Profit Alerts",
            "",
            "| Alert | Variant | Canonical | Suggested | Strength | "
            "Candidate-producing | Implied set |",
            "|---|---|---|---|---:|---|---|",
        ]
    )
    for row in block8["profit_alerts"]:
        lines.append(
            f"| `{row.get('alert_id')}` | {_variant_tag(row.get('variant'))} | "
            f"`{row.get('canonical') or '-'}` | `{row.get('suggested')}` | "
            f"{row.get('strength')} | `{row.get('candidate_producing')}` | "
            f"{_md_cell(', '.join(row.get('implied_set') or []))} |"
        )
    if not block8["profit_alerts"]:
        lines.append("| - | - | - | - | - | - | - |")
    lines.extend(["", block8["anti_inflation_rule"], ""])

    block9 = blocks["block_9_positional"]["payload"]
    lines.extend(
        [
            "## Block 9: Full Positional Tracker Evidence",
            "",
            "| Variant | Position | Top three digits |",
            "|---|---:|---|",
        ]
    )
    for variant in DISPLAY_VARIANTS:
        variant_row = block9["variants"][variant]
        for position in ("0", "1", "2"):
            top_digits = variant_row["positions"][position]["top_digits"]
            rendered = ", ".join(
                f"#{item['rank']}={item['digit']} "
                f"(gap {item['gap']}, score {float(item['score']):.4f})"
                for item in top_digits
            )
            lines.append(
                f"| {_variant_tag(variant)} | {int(position) + 1} | "
                f"{_md_cell(rendered)} |"
            )
    lines.extend(
        [
            "",
            "### Positional candidates",
            "",
            "| Rank | Literal | Canonical | VT | Score | Evidence |",
            "|---:|---|---|---:|---:|---|",
        ]
    )
    for row in block9["candidates"]:
        lines.append(
            f"| {row['rank']} | `{row['combo']}` | `{row['canonical']}` | "
            f"{row['vtrac_index']} | {float(row['score']):.4f} | "
            f"{_md_cell('; '.join(row.get('evidence') or []))} |"
        )
    lines.extend(
        [
            "",
            "### Positional consensus notes",
            "",
        ]
    )
    lines.extend(f"- {note}" for note in block9.get("consensus_notes") or [])
    lines.append("")

    compact = render_markdown(payload)
    marker = "## Block 10: Cross-Block Compound Convergence"
    if marker not in compact:
        raise ValueError("Compact AUX CORE report is missing Block 10")
    lines.extend(compact[compact.index(marker) :].rstrip().splitlines())
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_markdown(
    payload: Mapping[str, Any],
    *,
    grading: Optional[Mapping[str, Any]] = None,
) -> str:
    meta = payload["metadata"]
    blocks = payload["blocks"]
    block10 = blocks["block_10_cross_block_convergence"]
    lines = [
        "# AUX CORE Deep Review Receipt",
        "",
        f"- State: `{meta['state_key']}`",
        f"- Results date: `{meta['results_date']}`",
        f"- Profile: `{meta['profile']}`",
        f"- Frozen pre-result object: `{meta['source_is_frozen_pre_result']}`",
        f"- Frozen SHA-256: `{payload.get('frozen_object_sha256')}`",
        f"- Review ordering: `{meta['review_order']}`",
        "",
        "This is a review surface, not a calibrated production score or final "
        "prediction slate. Midday, Evening, and Combined show breadth; they are "
        "not independent tools.",
        "",
        "## Block Inventory",
        "",
    ]
    for key, block in blocks.items():
        lines.append(
            f"- `{block['block_id']}` {block['name']} "
            f"({'derived' if block.get('derived') else 'base'}) - `{key}`"
        )
    lines.extend(
        [
            "",
            "## Block 10: Cross-Block Compound Convergence",
            "",
            f"- Tier A independent identities: `{block10['inventory']['rows_by_tier']['TIER_A_INDEPENDENT_IDENTITY']}`",
            f"- Tier B narrowed-source-plus-structure identities: `{block10['inventory']['rows_by_tier']['TIER_B_SOURCE_PLUS_STRUCTURE']}`",
            f"- Tier C untranslated structural opportunities: `{block10['inventory']['rows_by_tier']['TIER_C_UNTRANSLATED_STRUCTURE']}`",
            f"- Complete qualified lattice: `{block10['inventory']['qualifying_rows']}` rows",
            "",
            "Tier A and B rows are narrowed convergence. Tier C rows remain "
            "valuable reverse-engineering opportunities, but they are not "
            "credited as candidates emitted by a narrowed source.",
            "",
            "| Review rank | Tier | Level | Identity | Identity sources | All base lineages | Dimensions | Variants | Burden | Roles |",
            "|---:|---|---|---|---|---|---|---|---|---|",
        ]
    )
    narrowed_display = [
        row
        for row in block10["rows"]
        if row["review_tier"] in NARROWED_REVIEW_TIERS
    ]
    untranslated_display = [
        row
        for row in block10["rows"]
        if row["review_tier"] == "TIER_C_UNTRANSLATED_STRUCTURE"
    ]
    for row in narrowed_display[:40]:
        burden = row["burden"]
        lines.append(
            "| {rank} | `{tier}` | `{level}` | `{identity}` | {identity_sources} | "
            "{lineages} | {dimensions} | {variants} | "
            "VT={vt}, Box={box}, Lane={lane}, Exact={exact} | {roles} |".format(
                rank=row["rank"],
                tier=row["review_tier"],
                level=row["identity_level"],
                identity=row["identity"],
                identity_sources=", ".join(row["identity_source_lineages"]) or "-",
                lineages=", ".join(row["base_source_lineages"]) or "-",
                dimensions=", ".join(row["evidence_dimensions"]) or "-",
                variants=", ".join(_variant_tag(v) for v in row["variant_coverage"])
                or "-",
                vt=burden["boxed_vtrac_indices"],
                box=burden["canonical_boxes"],
                lane=burden["ordered_lanes"],
                exact=burden["exact_literals"],
                roles=", ".join(row["role_labels"]),
            )
        )
    lines.extend(
        [
            "",
            f"The table shows the first `{min(40, len(narrowed_display))}` of "
            f"`{len(narrowed_display)}` narrowed rows. The complete narrowed "
            "inventory remains in the JSON receipt.",
            "",
            "### Untranslated Structural Opportunities",
            "",
            "| Review rank | Level | Identity | Base lineages | Dimensions | Variants | Burden |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for row in untranslated_display[:20]:
        burden = row["burden"]
        lines.append(
            "| {rank} | `{level}` | `{identity}` | {lineages} | "
            "{dimensions} | {variants} | "
            "VT={vt}, Box={box}, Lane={lane}, Exact={exact} |".format(
                rank=row["rank"],
                level=row["identity_level"],
                identity=row["identity"],
                lineages=", ".join(row["base_source_lineages"]) or "-",
                dimensions=", ".join(row["evidence_dimensions"]) or "-",
                variants=", ".join(_variant_tag(v) for v in row["variant_coverage"])
                or "-",
                vt=burden["boxed_vtrac_indices"],
                box=burden["canonical_boxes"],
                lane=burden["ordered_lanes"],
                exact=burden["exact_literals"],
            )
        )
    lines.extend(
        [
            "",
            f"The table shows the first `{min(20, len(untranslated_display))}` "
            f"of `{len(untranslated_display)}` Tier C opportunities. These rows "
            "identify missing translation work; they are not final candidate "
            "credit.",
            "",
            "Block 7 and Block 8 remain derived receipts. Their evidence is "
            "attributed to the underlying base source family rather than counted "
            "again.",
            "",
        ]
    )

    if grading:
        conversion = grading["conversion_read"]
        lines.extend(
            [
                "## Post-Result Reverse-Engineering Join",
                "",
                f"- Winner: `{grading['winner']}` ({grading['period']})",
                f"- Canonical: `{grading['winner_canonical']}`",
                f"- Boxed VTRAC index: `VT{grading['winner_vtrac_index']}`",
                f"- Ordered VSTRAIGHTS lane: `{grading['winner_ordered_vcode']}`",
                f"- Highest pre-existing compound identity: `{conversion['highest_specificity_reached']}`",
                f"- Highest narrowed identity: `{conversion['highest_narrowed_specificity']}`",
                f"- Highest untranslated structural opportunity: `{conversion['highest_untranslated_specificity']}`",
                f"- Translation gap: `{conversion['translation_gap']}`",
                f"- Narrowed-source translation gap: `{conversion['narrowed_translation_gap']}`",
                "",
                grading["credit_boundary"],
                "",
            ]
        )
        block10_grade = grading["block_alignment"][
            "block_10_cross_block_convergence"
        ]
        for level in (
            "exact_literal",
            "ordered_lane",
            "canonical_box",
            "vtrac_index",
        ):
            row = block10_grade.get(level)
            if not row:
                lines.append(f"- `{level}`: no qualifying Block 10 row")
                continue
            lines.append(
                f"- `{level}`: `{row['identity']}` / "
                f"tier `{row['review_tier']}` / "
                f"lineages `{', '.join(row['base_source_lineages'])}` / "
                f"roles `{', '.join(row['role_labels'])}` / receipts "
                f"`{'; '.join(_short_receipt(item) for item in row['receipts'])}`"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True, help="Project state key.")
    parser.add_argument("--date", required=True, help="Results date YYYY-MM-DD.")
    parser.add_argument(
        "--day-dir",
        required=True,
        help="Frozen sharepack day directory.",
    )
    parser.add_argument("--period", choices=("Midday", "Evening"))
    parser.add_argument("--winner", help="Optional post-result winner.")
    parser.add_argument("--out-dir", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if bool(args.period) != bool(args.winner):
        raise SystemExit("--period and --winner must be supplied together")
    payload = build_aux_core(
        state_key=args.state,
        results_date=args.date,
        day_dir=Path(args.day_dir),
    )
    grading = (
        grade_winner(payload, period=args.period, winner=args.winner)
        if args.period and args.winner
        else None
    )
    out_dir = Path(args.out_dir).resolve()
    stem = f"{args.date}__{args.state}__AUX_CORE"
    write_json(out_dir / f"{stem}__PRE_RESULT.json", payload)
    if grading:
        write_json(
            out_dir / f"{stem}__{args.period}__{args.winner}__GRADING.json",
            grading,
        )
    (out_dir / f"{stem}.md").write_text(
        render_markdown(payload, grading=grading),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "BASE_SOURCE_FAMILIES",
    "SCHEMA_VERSION",
    "VARIANTS",
    "build_aux_core",
    "build_cross_block_convergence",
    "canonical",
    "grade_winner",
    "normalize_pick3",
    "normalize_playable_pick3",
    "render_external_markdown",
    "render_markdown",
    "stable_sha256",
    "write_json",
]
