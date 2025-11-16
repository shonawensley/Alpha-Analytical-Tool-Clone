#!/usr/bin/env python3
"""
V-TRAC validator → compact scorer/exporter.

Reads one or more folders of `validation_report.json` files (emitted by the
enhanced validator), computes per-section confidence scores using overlap,
right-column stability, consensus rescue, section/state priors, and light
token-ledger promotion, then exports a compact CSV/JSON suitable for sharing
or downstream aggregation.

Examples
--------
    python TOOLS/vtrac_score_and_export.py
    python TOOLS/vtrac_score_and_export.py data/outputs/analysis/vtrac_validation \
        --config configs/vtrac_score_config.json \
        --out-dir data/outputs/analysis/vtrac_validation \
        --verbose
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple, Optional

DEFAULT_INPUTS = [
    "data/outputs/analysis/vtrac_validation",
    "data/outputs/analysis/vtrac",
]

SCORER_VERSION = "0.4.0"

DEFAULT_WEIGHTS: Dict[str, float] = {
    "overlap": 1.0,
    "stable": 1.9,
    "consensus": 1.0,
    "token_echo": 2.0,
    "hot": 0.4,
    "super": 0.6,
    "mask": 0.8,
    "mirror": 0.6,
    "doubles": 0.4,
    "combined_prior": 1.15,
    "rescue_multiplier": 0.45,
    "recency_lane": 1.5,
    "vt_only": 1.0,
    "vt_only_lane": 1.2,
    "straight_lane": 0.8,
    "winner_lane_rescue": 2.5,
    "winner_lane_floor": 6.0,
}

DEFAULT_COL_WEIGHTS: Dict[int, float] = {
    7: 0.5,
    6: 0.7,
    5: 0.9,
    4: 1.1,
    3: 1.6,
    2: 2.0,
    1: 2.4,
}

DEFAULT_SECTION_PRIORS: Dict[str, float] = {
    "Combined": DEFAULT_WEIGHTS["combined_prior"],
    "Midday": 1.0,
    "Evening": 1.0,
}


def parse_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value > 0
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "t", "yes", "y"}
    return False


def to_int(value) -> int:
    if isinstance(value, bool):
        return int(value)
    try:
        return int(value)
    except Exception:
        return 0


def to_float(value) -> float:
    if isinstance(value, bool):
        return float(int(value))
    try:
        return float(value)
    except Exception:
        return 0.0


def norm01(value: float, lo: float, hi: float) -> float:
    if hi <= lo:
        return 0.0
    scaled = (value - lo) / float(hi - lo)
    return max(0.0, min(1.0, scaled))


def discover_reports(paths: Sequence[str]) -> List[Path]:
    reports: Set[Path] = set()
    for raw in paths:
        candidate = Path(raw)
        if candidate.is_file() and candidate.name == "validation_report.json":
            reports.add(candidate.resolve())
        elif candidate.is_dir():
            for report in candidate.rglob("validation_report.json"):
                reports.add(report.resolve())
    return sorted(reports)


def load_config(path: str | None) -> Dict[str, Dict]:
    if not path:
        return {
            "weights": {},
            "col_weights": {},
            "section_priors": {},
            "state_priors": {},
        }
    config_path = Path(path)
    try:
        data = json.loads(config_path.read_text())
        return {
            "weights": data.get("weights", {}),
            "col_weights": data.get("col_weights", {}),
            "section_priors": data.get("section_priors", {}),
            "state_priors": data.get("state_priors", {}),
        }
    except Exception as exc:  # pragma: no cover - defensive
        logging.warning("Could not load config %s (%s)", config_path, exc)
        return {
            "weights": {},
            "col_weights": {},
            "section_priors": {},
            "state_priors": {},
        }


def stable_score(stable_cols: Iterable[int], col_weights: Dict[int, float]) -> float:
    return sum(col_weights.get(int(col), 0.0) for col in stable_cols)


def build_global_token_ledger(staged_docs: List[dict]) -> Tuple[Dict[str, Set[str]], Dict[str, Dict[str, int]]]:
    token_states: Dict[str, Set[str]] = defaultdict(set)
    token_sections_by_state: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for entry in staged_docs:
        state = entry["__state__"]
        winners_map = entry["__sections__"]["winners_tokens"]
        analyzer_map = entry["__sections__"]["analyzer_tokens"]
        for section in winners_map:
            union_tokens = winners_map[section] | analyzer_map.get(section, set())
            for token in union_tokens:
                token_states[token].add(state)
                token_sections_by_state[state][token] += 1
    return token_states, token_sections_by_state


def tokens_for_section(payload: dict, section: str) -> Tuple[List[str], List[str]]:
    section_payload = (payload.get("sections") or {}).get(section, {})
    signals = section_payload.get("signals") or {}
    analyzer = section_payload.get("analyzer_signatures") or {}
    winners_tokens = signals.get("top_vtrac_box_signatures") or []
    analyzer_tokens = analyzer.get("primary") or []
    return winners_tokens, analyzer_tokens


def straight_list_for_section(payload: dict, section: str) -> List[str]:
    section_payload = (payload.get("sections") or {}).get(section, {})
    metrics = (section_payload.get("analyzer_metrics") or {}).get("primary") or {}
    straights = metrics.get("top_straights") or []
    if straights and isinstance(straights[0], dict):
        straights = [
            str(entry.get("straight"))
            for entry in sorted(straights, key=lambda e: e.get("score", 0), reverse=True)
            if entry.get("straight") is not None
        ]
    return straights[:3]


def metrics_for_section(payload: dict, section: str) -> Dict[str, object]:
    section_payload = (payload.get("sections") or {}).get(section, {})
    signals = section_payload.get("signals") or {}
    metrics = (section_payload.get("analyzer_metrics") or {}).get("primary") or {}
    summaries = (payload.get("section_summaries") or {}).get(section, {})

    mask_drop = metrics.get("mask_drop_count")
    doubles = metrics.get("double_hits")
    if doubles is None:
        doubles = metrics.get("doubles_hit_count", 0)

    return {
        "hot": signals.get("hot"),
        "superhot": signals.get("superhot"),
        "hot_count": summaries.get("hot_count"),
        "superhot_count": summaries.get("superhot_count"),
        "stable_cols": [to_int(c) for c in signals.get("stable_columns") or []],
        "consensus_col1": parse_bool(signals.get("consensus_col1")),
        "consensus_col2": parse_bool(signals.get("consensus_col2")),
        "mask_drop": mask_drop if mask_drop is not None else 0,
        "mirror": parse_bool(metrics.get("mirror_supported")),
        "doubles": doubles if doubles is not None else 0,
    }


def compute_cross_section_echo(tokens_map: Dict[str, Set[str]]) -> Dict[str, int]:
    echo: Dict[str, int] = {}
    sections = list(tokens_map.keys())
    for name in sections:
        mine = tokens_map[name]
        others = set().union(*(tokens_map[other] for other in sections if other != name)) if len(sections) > 1 else set()
        echo[name] = len(mine & others)
    return echo


def tier_from_overlap(overlap: int) -> str:
    if overlap >= 4:
        return "A"
    if overlap == 3:
        return "B+"
    if overlap == 2:
        return "B"
    if overlap == 1:
        return "C"
    return "Z"


def resolve_analyzer_path(path_str: Optional[str], report_path: Path) -> Optional[Path]:
    if not path_str:
        return None
    candidate = Path(path_str).expanduser()
    if candidate.exists():
        return candidate
    alt = report_path.parent / Path(path_str).name
    if alt.exists():
        return alt
    return None


def describe_section(row: dict) -> str:
    parts = [f"{row['section']} overlap={row['overlap']}"]
    cols = row.get("stable_cols") or []
    if cols:
        parts.append(f"cols {cols}")
    echo = row.get("cross_section_echo")
    if echo:
        parts.append(f"echo={echo}")
    if row.get("mirror_supported"):
        parts.append("mirror")
    doubles = row.get("double_hits")
    if doubles:
        parts.append(f"doubles={doubles}")
    rec = row.get("recency_lane_score")
    if rec:
        parts.append(f"recency_lane={rec:.2f}")
    return "; ".join(parts)


def compute_top_indices(analyzer_path: Optional[Path], section_map: Dict[str, dict]) -> List[dict]:
    if not analyzer_path or not analyzer_path.exists():
        return []
    try:
        payload = json.loads(analyzer_path.read_text())
    except Exception:
        return []

    # Map each section to the highest-scoring index from analyzer evidence
    section_best_index: Dict[str, int] = {}
    for entry in payload.get("indices_ranked", []):
        idx = entry.get("index")
        sections = entry.get("evidence", {}).get("raw", {}).get("sections", [])
        for section_name in sections:
            if section_name not in section_best_index:
                section_best_index[section_name] = idx
            # attach index to section cache if present
            if section_name in section_map:
                section_map[section_name]["index_hint"] = idx

    def lane_strength(row: dict) -> float:
        # Combine recency/echo/hot + straight signals to identify a strong lane
        rec = float(row.get("recency_lane_score") or 0.0)
        echo = float(row.get("cross_section_echo") or 0.0)
        hot_val = 0.0
        hot_count = row.get("hot_count")
        superhot_count = row.get("superhot_count")
        if hot_count is not None:
            hot_val += max(0.0, min(float(hot_count) / 8.0, 1.0))
        if superhot_count is not None:
            hot_val += max(0.0, min(float(superhot_count) / 12.0, 1.0))
        straight = 1.0 if row.get("straight_lane_score") else 0.0
        return rec + 0.5 * echo + 0.3 * hot_val + 0.5 * straight

    picks: List[dict] = []
    seen_indices: Set[int] = set()
    lane_candidates: List[tuple[float, dict]] = []

    for entry in payload.get("indices_ranked", []):
        idx = entry.get("index")
        if idx is None or idx in seen_indices:
            continue
        sections = entry.get("evidence", {}).get("raw", {}).get("sections", [])
        best_row = None
        for section_name in sections:
            candidate = section_map.get(section_name)
            if not candidate:
                continue
            if best_row is None or candidate["confidence_score"] > best_row["confidence_score"]:
                best_row = candidate
        if not best_row:
            continue
        seen_indices.add(idx)
        # attach index hint for promotion
        best_row["index_hint"] = idx
        picks.append(
            {
                "index": idx,
                "score": best_row["confidence_score"],
                "source_section": best_row["section"],
                "explain": describe_section(best_row),
            }
        )
        if best_row.get("overlap", 0) <= 1:
            lane_candidates.append((lane_strength(best_row), best_row))

    # Promote the strongest low-overlap lane if present
    lane_candidates.sort(key=lambda item: (-item[0], item[1].get("section", "")))
    if lane_candidates:
        _, lane_row = lane_candidates[0]
        forced = {
            "index": lane_row.get("index_hint") or lane_row.get("source_index") or section_best_index.get(lane_row.get("section", ""), -1),
            "score": lane_row["confidence_score"],
            "source_section": lane_row["section"],
            "explain": "lane_promotion: " + describe_section(lane_row),
        }
        # Only add if index is known and not already in picks
        if forced["index"] != -1 and all(p["index"] != forced["index"] for p in picks):
            picks.append(forced)

    picks.sort(key=lambda item: (-item["score"], item["index"]))
    return picks[:3]


def main() -> int:
    parser = argparse.ArgumentParser(description="V-TRAC validator → compact scorer/exporter")
    parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_INPUTS,
        help="Files/directories containing validation_report.json (searches recursively).",
    )
    parser.add_argument(
        "--config",
        help="Optional JSON overriding weights/priors (see configs/vtrac_score_config.json).",
    )
    parser.add_argument(
        "--out",
        dest="out_dir",
        help="Directory for vtrac_compact_report.{json,csv}. Defaults to first resolved input directory.",
    )
    parser.add_argument(
        "--out-dir",
        dest="out_dir",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose (DEBUG) logging output.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")

    reports = discover_reports(args.paths)
    if not reports:
        logging.error("No validation_report.json files found under %s", ", ".join(args.paths))
        return 1

    config = load_config(args.config)

    weights = {**DEFAULT_WEIGHTS, **{k: float(v) for k, v in config["weights"].items()}}
    col_weights = {**DEFAULT_COL_WEIGHTS, **{int(k): float(v) for k, v in config["col_weights"].items()}}
    section_priors = {**DEFAULT_SECTION_PRIORS, **{str(k): float(v) for k, v in config["section_priors"].items()}}
    state_priors = {str(k): float(v) for k, v in config["state_priors"].items()}

    output_dir = Path(args.out_dir) if args.out_dir else reports[0].parent
    output_dir.mkdir(parents=True, exist_ok=True)

    staged: List[dict] = []
    for report_path in reports:
        payload = json.loads(report_path.read_text())
        state = payload.get("state") or report_path.parent.name
        date = payload.get("generated_at", "")
        section_names = list((payload.get("sections") or {}).keys())

        winners_tokens_by_section: Dict[str, Set[str]] = {}
        analyzer_tokens_by_section: Dict[str, Set[str]] = {}

        for section in section_names:
            winners_tokens, analyzer_tokens = tokens_for_section(payload, section)
            winners_tokens_by_section[section] = set(winners_tokens)
            analyzer_tokens_by_section[section] = set(analyzer_tokens)

        analyzer_path = resolve_analyzer_path((payload.get("analyzer_jsons") or {}).get("primary"), report_path)

        staged.append(
            {
                "__path__": report_path,
                "__state__": state,
                "__date__": date,
                "__sections__": {
                    "winners_tokens": winners_tokens_by_section,
                    "analyzer_tokens": analyzer_tokens_by_section,
                },
                "__analyzer_json__": analyzer_path,
                "__source_index__": None,
                "doc": payload,
            }
        )

    token_states, token_sections_by_state = build_global_token_ledger(staged)

    rows: List[dict] = []
    state_sections: Dict[Tuple[str, str], List[dict]] = defaultdict(list)
    analyzer_lookup: Dict[Tuple[str, str], Optional[Path]] = {}
    for entry in staged:
        report_path = entry["__path__"]
        payload = entry["doc"]
        state = entry["__state__"]
        date = entry["__date__"]
        section_names = list((payload.get("sections") or {}).keys())

        raw_mask_values: List[float] = []
        raw_doubles_values: List[float] = []
        tokens_map: Dict[str, Set[str]] = {}
        section_cache: Dict[str, dict] = {}

        for section in section_names:
            winners_tokens, analyzer_tokens = tokens_for_section(payload, section)
            metrics = metrics_for_section(payload, section)
            tokens_map[section] = set(winners_tokens) | set(analyzer_tokens)
            section_cache[section] = {
                "winners_tokens": winners_tokens,
                "analyzer_tokens": analyzer_tokens,
                "metrics": metrics,
                "index_hint": None,  # filled later when we map analyzer indices to sections
            }
            raw_mask_values.append(to_float(metrics["mask_drop"]))
            raw_doubles_values.append(to_float(metrics["doubles"]))

        mask_min, mask_max = (min(raw_mask_values), max(raw_mask_values)) if raw_mask_values else (0.0, 0.0)
        doubles_min, doubles_max = (min(raw_doubles_values), max(raw_doubles_values)) if raw_doubles_values else (0.0, 0.0)
        echo_by_section = compute_cross_section_echo(tokens_map)

        state_prior = state_priors.get(state, 1.0)

        for section in section_names:
            cache_entry = section_cache[section]
            winners_tokens = cache_entry["winners_tokens"]
            analyzer_tokens = cache_entry["analyzer_tokens"]
            metrics = cache_entry["metrics"]

            overlap = len(set(winners_tokens) & set(analyzer_tokens))
            stable_cols = metrics["stable_cols"]
            stability_value = stable_score(stable_cols, col_weights)
            consensus_count = int(metrics["consensus_col1"]) + int(metrics["consensus_col2"])

            hot_count = metrics["hot_count"]
            superhot_count = metrics["superhot_count"]
            hot_value = to_int(hot_count) if hot_count is not None else to_int(metrics["hot"])
            superhot_value = to_int(superhot_count) if superhot_count is not None else to_int(metrics["superhot"])
            hot_norm = min(hot_value / 8.0, 1.0) if hot_value else 0.0
            super_norm = min(superhot_value / 12.0, 1.0) if superhot_value else 0.0

            mask_norm = norm01(to_float(metrics["mask_drop"]), mask_min, mask_max)
            mirror_value = 1.0 if metrics["mirror"] else 0.0
            doubles_norm = norm01(to_float(metrics["doubles"]), doubles_min, doubles_max)
            echo_value = echo_by_section.get(section, 0)

            recency_lane_score = 0.0
            latest_cols = {1, 2}
            if set(stable_cols) & latest_cols:
                recency_lane_score = 1.0
                # extra credit if both col2 and col1 present
                if 1 in stable_cols and 2 in stable_cols:
                    recency_lane_score = 1.2

            vt_only_signal = 0.0
            if overlap == 0:
                vt_only_signal = 0.0
                if stable_cols:
                    vt_only_signal += 1.0 + 0.2 * len(stable_cols)
                if echo_value:
                    vt_only_signal += 0.5 * echo_value
                vt_only_signal += recency_lane_score
                vt_only_signal += hot_norm + super_norm

            vt_lane_bonus = 0.0
            if overlap == 0 and echo_value >= 1 and recency_lane_score > 0:
                # reward VT-only lanes that echo across variants and land in Set1 col1/2 (recency)
                vt_lane_bonus = 1.0 + 0.3 * echo_value + 0.5 * recency_lane_score

            vt_lane_rescue = 0.0
            if overlap <= 1 and (recency_lane_score > 0 or echo_value > 0):
                vt_lane_rescue = 0.5 * recency_lane_score + 0.25 * echo_value + 0.1 * (hot_norm + super_norm)

            overlap_score = math.log1p(overlap)
            winner_lane_rescue = 0.0
            winner_lane_floor = 0.0
            if overlap <= 1 and (recency_lane_score > 0 or echo_value > 0):
                winner_lane_rescue = recency_lane_score + 0.5 * echo_value + 0.2 * (hot_norm + super_norm)
                winner_lane_floor = (
                    weights.get("winner_lane_floor", 0.0)
                    * (1.0 + 0.2 * recency_lane_score + 0.1 * echo_value)
                )

            straights = straight_list_for_section(payload, section)
            straight_lane_score = 0.0
            if straights:
                straight_lane_score = 1.0 + 0.1 * len(straights)
                if recency_lane_score > 0:
                    straight_lane_score += 0.3
                if echo_value > 0:
                    straight_lane_score += 0.2
                if hot_norm or super_norm:
                    straight_lane_score += 0.2

            components: List[Tuple[str, float, float]] = [
                ("overlap", weights["overlap"], overlap_score),
                ("stable", weights["stable"], stability_value),
                ("consensus", weights["consensus"], float(consensus_count) if stable_cols else 0.0),
                ("echo", weights["token_echo"], float(echo_value)),
                ("hot", weights["hot"], hot_norm),
                ("superhot", weights["super"], super_norm),
                ("mask_drop", weights["mask"], mask_norm),
                ("mirror", weights["mirror"], mirror_value),
                ("doubles", weights["doubles"], doubles_norm),
                ("recency_lane", weights.get("recency_lane", 0.0), recency_lane_score),
                ("vt_only", weights.get("vt_only", 0.0), vt_only_signal),
                ("vt_only_lane", weights.get("vt_only_lane", 0.0), vt_lane_bonus),
                ("vt_lane_rescue", weights.get("vt_only_lane", 0.0), vt_lane_rescue),
                ("winner_lane_rescue", weights.get("winner_lane_rescue", 0.0), winner_lane_rescue),
                ("straight_lane", weights.get("straight_lane", 0.0), straight_lane_score),
            ]

            base_score = sum(weight * value for _, weight, value in components)
            if winner_lane_floor:
                base_score = max(base_score, winner_lane_floor)
            section_prior = section_priors.get(section, 1.0)
            score = base_score * section_prior * state_prior

            flags: List[str] = []
            rescue_multiplier = 1.0
            if overlap == 0 and consensus_count >= 1 and stable_cols:
                rescue_multiplier = weights["rescue_multiplier"]
                score *= rescue_multiplier
                flags.append("weak_positive_rescue")
            if overlap == 0:
                flags.append("zero_overlap")

            tier = tier_from_overlap(overlap)

            union_tokens = set(winners_tokens) | set(analyzer_tokens)
            token_scores: List[Tuple[float, str]] = []
            for token in union_tokens:
                base = 1.0
                if token in analyzer_tokens:
                    base += 0.5
                local_rep = token_sections_by_state[state].get(token, 0)
                if local_rep > 1:
                    base += 0.2 * (local_rep - 1)
                if len(token_states[token]) >= 3:
                    base += 0.3
                token_scores.append((round(base, 3), token))
            token_scores.sort(key=lambda item: (-item[0], item[1]))
            recommended_tokens = [token for _, token in token_scores][:3]

            straights = straight_list_for_section(payload, section)

            why_parts: List[str] = [
                f"{label}={value:.3f}*{weight:.2f}->{weight * value:.2f}"
                for (label, weight, value) in components
                if value > 0.0
            ]
            why_parts.append(f"section_prior={section_prior:.2f}")
            if not math.isclose(state_prior, 1.0):
                why_parts.append(f"state_prior={state_prior:.2f}")
            if not math.isclose(rescue_multiplier, 1.0):
                why_parts.append(f"rescue_multiplier={rescue_multiplier:.2f}")
            row = {
                "date": date,
                "state": state,
                "section": section,
                "index_hint": payload.get("state_index") or None,
                "overlap": overlap,
                "stable_cols_count": len(stable_cols),
                "stable_cols": stable_cols,
                "consensus_col1": metrics["consensus_col1"],
                "consensus_col2": metrics["consensus_col2"],
                "cross_section_echo": echo_value,
                "hot_count": hot_value,
                "superhot_count": superhot_value,
                "mask_drop": metrics["mask_drop"],
                "mirror_supported": metrics["mirror"],
                "double_hits": metrics["doubles"],
                "confidence_score": round(score, 3),
                "tier": tier,
                "flags": flags,
                "top_tokens": winners_tokens,
                "recommended_tokens": recommended_tokens,
                "top_straights": straights,
                "section_prior": section_prior,
                "state_prior": state_prior,
                "recency_lane_score": recency_lane_score,
                "vt_lane_rescue": vt_lane_rescue,
                "winner_lane_rescue": winner_lane_rescue,
                "why": "; ".join(why_parts),
                "source": report_path.name,
            }
            rows.append(row)
            key = (state, date)
            state_sections[key].append(row)
            if key not in analyzer_lookup:
                analyzer_lookup[key] = entry.get("__analyzer_json__")

    run_date_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    weights_fingerprint = json.dumps(
        {
            "weights": weights,
            "col_weights": col_weights,
            "section_priors": section_priors,
            "state_priors": state_priors,
        },
        sort_keys=True,
    )
    weights_hash = hashlib.sha1(weights_fingerprint.encode("utf-8")).hexdigest()[:8]

    states_output: List[dict] = []
    for key in sorted(state_sections.keys()):
        state, date = key
        sections = sorted(state_sections[key], key=lambda r: r["section"])
        section_map = {row["section"]: row for row in sections}
        analyzer_path = analyzer_lookup.get(key)
        top_indices = compute_top_indices(analyzer_path, section_map)
        states_output.append(
            {
                "state": state,
                "date": date,
                "sections": sections,
                "top_indices_by_state": top_indices,
            }
        )

    out_json = output_dir / "vtrac_compact_report.json"
    out_csv = output_dir / "vtrac_compact_report.csv"

    out_json.write_text(
        json.dumps(
            {
                "scorer_version": SCORER_VERSION,
                "run_date_utc": run_date_utc,
                "weights_hash": weights_hash,
                "sections": rows,
                "states": states_output,
            },
            indent=2,
        )
    )

    headers = [
        "date",
        "state",
        "section",
        "overlap",
        "stable_cols_count",
        "stable_cols",
        "consensus_col1",
        "consensus_col2",
        "cross_section_echo",
        "hot_count",
        "superhot_count",
        "mask_drop",
        "mirror_supported",
        "double_hits",
        "confidence_score",
        "tier",
        "flags",
        "top_tokens",
        "recommended_tokens",
        "top_straights",
        "section_prior",
        "state_prior",
        "why",
        "source",
    ]

    def csv_escape(value) -> str:
        text = value if isinstance(value, str) else json.dumps(value, separators=(",", ":"))
        if any(ch in text for ch in {",", '"', "\n"}):
            text = '"' + text.replace('"', '""') + '"'
        return text

    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        handle.write(",".join(headers) + "\n")
        for row in rows:
            handle.write(",".join(csv_escape(row[column]) for column in headers) + "\n")

    logging.info("Wrote %d section rows", len(rows))
    logging.info(" - JSON: %s", out_json)
    logging.info(" - CSV : %s", out_csv)
    if states_output:
        logging.info("State summary:")
        for entry in states_output:
            logging.info(
                "   %s (%s): %d sections, %d top indices",
                entry["state"],
                entry["date"],
                len(entry["sections"]),
                len(entry["top_indices_by_state"]),
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
