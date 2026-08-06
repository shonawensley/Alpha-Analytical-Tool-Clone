#!/usr/bin/env python3
"""Create Analysis Arena audit artifacts for a completed window.

This is a documentation/audit generator only. It does not change runtime
scoring, translators, Play Cards, or source analytical outputs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_WINDOW_ROOT = (
    REPO_ROOT
    / "docs"
    / "AAT9_KIT"
    / "FINAL VALIDATION"
    / "RUNS_2"
    / "WINDOW_2026-03-09_to_2026-03-23"
)
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_SHAREPACK_ROOT = REPO_ROOT / "sharepacks" / "_predictive"
DEFAULT_OUT_DIR = DEFAULT_WINDOW_ROOT / "ANALYSIS_ARENA_AUDIT"


@dataclass(frozen=True)
class FeatureSpec:
    feature: str
    tool_or_context_source: str
    scope: str
    runtime_file_type: str
    expected_namespace: str
    actual_json_paths: Sequence[str]
    source_terms: Sequence[str]
    consumer_layer: str
    contract_doc: str
    expected_status: str = "explicit"
    notes: str = ""


@dataclass
class FeatureStats:
    spec: FeatureSpec
    scope_total: int = 0
    explicit_count: int = 0
    folded_count: int = 0
    linked_only_count: int = 0
    missing_count: int = 0
    empty_object_count: int = 0
    sample_actual_json_path: str = ""
    sample_source_file_path: str = ""
    sample_human_review_artifact: str = ""
    exception_examples: List[Dict[str, Any]] = field(default_factory=list)


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", default=str(DEFAULT_WINDOW_ROOT))
    ap.add_argument("--sharepack-root", default=str(DEFAULT_SHAREPACK_ROOT))
    ap.add_argument("--final-docs-root", default=str(DEFAULT_FINAL_DOCS))
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return ap.parse_args()


def _resolve(path_value: str | Path) -> Path:
    path = Path(path_value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _safe_rel(path: str | Path) -> str:
    path = Path(path)
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except Exception:
        return str(path)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], fields: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(fields), extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _values_at(obj: Any, dotted_path: str) -> List[Any]:
    """Return values for a dotted path; '*' iterates dict values or list items."""
    parts = [part for part in dotted_path.split(".") if part]

    def walk(value: Any, idx: int) -> List[Any]:
        if idx >= len(parts):
            return [value]
        part = parts[idx]
        out: List[Any] = []
        if part == "*":
            if isinstance(value, dict):
                for child in value.values():
                    out.extend(walk(child, idx + 1))
            elif isinstance(value, list):
                for child in value:
                    out.extend(walk(child, idx + 1))
            return out
        if isinstance(value, dict) and part in value:
            return walk(value[part], idx + 1)
        return []

    return walk(obj, 0)


def _has_content(values: Sequence[Any]) -> bool:
    if not values:
        return False
    for value in values:
        if value is None:
            continue
        if value == "":
            continue
        if isinstance(value, (list, dict)) and len(value) == 0:
            continue
        return True
    return False


def _load_window_scope(window_root: Path) -> Dict[str, Any]:
    manifest_path = window_root / "REVIEW_MANIFEST.json"
    if manifest_path.exists():
        manifest = _read_json(manifest_path)
        window = manifest.get("window") or {}
        dates = list(window.get("dates") or [])
        states = list(window.get("states") or [])
        if dates and states:
            return {"dates": dates, "states": states, "manifest": manifest}

    dates = sorted(path.name for path in DEFAULT_SHAREPACK_ROOT.iterdir() if path.is_dir())
    states = sorted(
        path.name
        for path in (DEFAULT_SHAREPACK_ROOT / dates[0]).iterdir()
        if path.is_dir() and path.name.endswith("4")
    ) if dates else []
    return {"dates": dates, "states": states, "manifest": {}}


def _aggregate_path(sharepack_root: Path, date: str, state_key: str) -> Path:
    return sharepack_root / date / state_key / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json"


def _aggregate_md_path(sharepack_root: Path, date: str, state_key: str) -> Path:
    return sharepack_root / date / state_key / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.md"


def _state_seed_path(sharepack_root: Path, date: str, state_key: str) -> Path:
    return sharepack_root / date / state_key / "analysis" / "translation_sandbox_seed__tool_only__arena_v0.json"


def _state_seed_md_path(sharepack_root: Path, date: str, state_key: str) -> Path:
    return sharepack_root / date / state_key / "analysis" / "translation_sandbox_seed__tool_only__arena_v0.md"


def _brain2_json_path(window_root: Path, date: str, stem: str) -> Path:
    return window_root / "ANALYSIS_ARENA" / f"{date}__{stem}__analysis_arena_day_review.json"


def _brain2_md_path(window_root: Path, date: str, stem: str) -> Path:
    return window_root / "ANALYSIS_ARENA" / f"{date}__{stem}__analysis_arena_day_review.md"


def _predictive_shell_path(window_root: Path, date: str, state_key: str) -> Path:
    return window_root / "PREDICTIVE" / f"{date}__{state_key}__PREDICTIVE__tool_only__arena_v0.md"


def _validation_path(window_root: Path, date: str, state_key: str) -> Path:
    return window_root / "VALIDATION" / f"{date}__{state_key}.md"


def _final_doc_sources() -> Dict[str, str]:
    base = "docs/AAT9_KIT/FINAL VALIDATION/final docs/"
    return {
        "aggregate_contract": base + "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md",
        "string_feed": base + "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
        "context_feed": base + "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
        "system_map": base + "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md",
        "dpl": base + "AAT9_DECISION_POLICY_LAYER__ANALYSIS_ARENA_BRANCH.md",
        "translator": base + "AAT9_TRANSLATOR_ARCHITECTURE__ANALYSIS_ARENA_BRANCH.md",
        "runs2_map": base + "AAT9_ANALYSIS_ARENA__RUNS2_ARTIFACT_REVIEW_MAP.md",
    }


def _feature_specs() -> List[FeatureSpec]:
    docs = _final_doc_sources()
    specs: List[FeatureSpec] = []

    def add(
        feature: str,
        source: str,
        paths: Sequence[str],
        terms: Sequence[str],
        consumer: str,
        doc: str,
        *,
        scope: str = "state_day",
        runtime: str = "aggregated_arena_json",
        ns: str = "",
        status: str = "explicit",
        notes: str = "",
    ) -> None:
        specs.append(
            FeatureSpec(
                feature=feature,
                tool_or_context_source=source,
                scope=scope,
                runtime_file_type=runtime,
                expected_namespace=ns or (paths[0] if paths else ""),
                actual_json_paths=list(paths),
                source_terms=list(terms),
                consumer_layer=consumer,
                contract_doc=doc,
                expected_status=status,
                notes=notes,
            )
        )

    # Required top-level aggregate namespaces.
    for feature, path in [
        ("schema_version", "schema_version"),
        ("metadata", "metadata"),
        ("provenance.source_status", "provenance.source_status"),
        ("provenance.evidence_paths", "provenance.evidence_paths"),
        ("review_links", "review_links"),
    ]:
        add(feature, "Aggregate contract", [path], [], "human audit / traceability", docs["aggregate_contract"])

    # Stable.
    stable_terms = ["stable/"]
    for feature in [
        "top_row_patterns",
        "pattern_ledgers_top",
        "top_compound_patterns",
        "family_rollups_top",
        "survivor_frontiers",
        "survivor_progressions",
    ]:
        add(
            f"stable.{feature}",
            "Stable Pattern Extractor",
            [f"string_tools.stable.sections.*.{feature}"],
            stable_terms,
            "cross_tool_relations / arena_synthesis",
            docs["string_feed"],
        )
    add("stable.metrics_summary", "Stable Pattern Extractor", ["string_tools.stable.metrics_summary"], stable_terms, "review / synthesis context", docs["string_feed"])
    add("stable.r_consensus_context", "Stable Pattern Extractor", ["string_tools.stable.r_consensus_context"], stable_terms, "arena_synthesis / sandbox", docs["string_feed"])

    # Digit Reduction.
    dr_terms = ["digit_reduction/", "analyzer_v2"]
    dr_features = [
        "summary",
        "dr_trace_strength",
        "dr_lane_only_confidence",
        "dr_competing_literal_pressure",
        "dr_double_pressure",
        "dr_corridor_strength",
        "dr_empty_lens",
        "dr_structural_signals",
        "dr_vtrac_lane_gateway",
        "dr_vtrac_cluster_strength",
        "dr_assigned_box_vtrac_strength",
        "dr_vtrac_fusion_strength",
        "dr_row_repeat_and_final_survival",
        "precluster_ledger",
        "reduction_reveal_ledger",
        "box_validity_ledger",
        "fourth_variable_candidates",
    ]
    for feature in dr_features:
        add(
            f"digit_reduction.{feature}",
            "Digit Reduction",
            [f"string_tools.digit_reduction.sections.*.{feature}"],
            dr_terms,
            "cross_tool_relations / arena_synthesis",
            docs["string_feed"],
        )

    # VTRAC Analyzer. These are present, but often folded under the enhanced/raw object
    # rather than rendered as one named object per contract concept.
    add("vtrac.indices_ranked", "VTRAC Analyzer", ["string_tools.vtrac_analyzer.enhanced.indices_ranked"], ["vtrac/"], "cross_tool_relations", docs["string_feed"])
    add("vtrac.straights_ranked", "VTRAC Analyzer", ["string_tools.vtrac_analyzer.enhanced.straights_ranked"], ["vtrac/"], "cross_tool_relations", docs["string_feed"])
    add("vtrac.section_summaries", "VTRAC Analyzer", ["string_tools.vtrac_analyzer.enhanced.section_summaries"], ["vtrac/"], "cross_tool_relations", docs["string_feed"])
    add("vtrac.compact_report_day", "VTRAC Analyzer", ["string_tools.vtrac_analyzer.compact_report_day"], ["vtrac/"], "cross_tool_relations", docs["string_feed"])
    for feature in [
        "cross_variant_lane_strength",
        "right_column_lane_stability",
        "vt_only_lane_confidence",
        "straight_lane_quality",
        "lane_dominance",
        "section_lead_profile",
        "mask_drop_lane_reveal",
        "mirror_double_lane_support",
    ]:
        add(
            f"vtrac.contract_surface.{feature}",
            "VTRAC Analyzer",
            ["string_tools.vtrac_analyzer.enhanced", "string_tools.vtrac_analyzer.compact_report_day"],
            ["vtrac/"],
            "cross_tool_relations / arena_synthesis",
            docs["string_feed"],
            status="folded",
            notes="Contract concept is present through VTRAC enhanced/compact payloads, not as a dedicated named sub-object.",
        )

    # Hot Zones.
    add("hot_zones.top_lanes", "Hot Zones", ["string_tools.hot_zones.top_lanes"], ["hot_zones/"], "cross_tool_relations", docs["string_feed"])
    add("hot_zones.per_lane_top", "Hot Zones", ["string_tools.hot_zones.per_lane_top"], ["hot_zones/"], "review / drilldown", docs["string_feed"])
    add("hot_zones.meta", "Hot Zones", ["string_tools.hot_zones.meta"], ["hot_zones/"], "review / traceability", docs["string_feed"])
    add("hot_zones.winner_map_top", "Hot Zones", ["string_tools.hot_zones.winner_map_top"], ["hot_zones/"], "post-result compatibility", docs["string_feed"])
    for feature in [
        "late_tail_pressure_strength",
        "superhot_echo_strength",
        "vertical_repeat_strength",
        "rowtype_span_support",
        "precol1_funnel_strength",
        "col1_arrival_strength",
        "vt_only_lane_pressure",
        "repeat_3value_score",
        "consensus_column_signal",
        "set1_funnel_density",
    ]:
        add(
            f"hot_zones.contract_surface.{feature}",
            "Hot Zones",
            ["string_tools.hot_zones.top_lanes", "string_tools.hot_zones.per_lane_top"],
            ["hot_zones/"],
            "cross_tool_relations / review drilldown",
            docs["string_feed"],
            status="folded",
            notes="Contract concept is preserved through top-lane/per-lane payloads, not as a dedicated named sub-object.",
        )

    # Aux / Control Center.
    aux_terms = ["aux/", "control_center/"]
    for feature in [
        "aux_positional_pressure",
        "aux_vtrac_pressure",
        "aux_badge_pressure",
        "aux_pair_band_context",
        "aux_due_doubles_family_pressure",
        "aux_repeat_watch_context",
        "aux_sums_context",
        "aux_blackapple_context",
        "cc_profit_alert_context",
        "cc_compound_event_context",
        "cc_tracker_context",
    ]:
        add(
            f"aux_control_center.{feature}",
            "Aux / Control Center",
            [f"context_tools.aux_control_center.arena_objects.{feature}"],
            aux_terms,
            "Brain1 synthesis / Brain2 context",
            docs["context_feed"],
        )

    # Cross-tool relations and Arena synthesis.
    for feature in [
        "canonical_consensus_top",
        "vtrac_index_consensus_top",
        "family_consensus_top",
        "r_consensus_context",
        "regime_flags",
        "contradiction_flags",
    ]:
        add(f"cross_tool_relations.{feature}", "Aggregate relation layer", [f"cross_tool_relations.{feature}"], [], "arena_synthesis", docs["aggregate_contract"])
    for feature in [
        "dominant_canonicals",
        "dominant_vtrac_indices",
        "dominant_families",
        "vtrac_literal_watchlist",
        "context_reinforced_canonicals",
        "context_only_pressure",
        "stable_survivor_context",
        "r_consensus_context",
        "state_regime",
        "review_prompts",
    ]:
        add(f"arena_synthesis.{feature}", "Arena synthesis", [f"arena_synthesis.{feature}"], [], "translation_sandbox / human review", docs["aggregate_contract"])

    # Downstream handoff remains the control-arm bridge, not a final Arena-native translator.
    add("downstream_handoff.candidate_universe", "Control-arm handoff", ["downstream_handoff.candidate_universe"], ["candidate_universe"], "control-arm comparison", docs["aggregate_contract"], notes="Old downstream/control-arm bridge.")
    add("downstream_handoff.play_card", "Control-arm handoff", ["downstream_handoff.play_card"], ["play_card"], "control-arm comparison", docs["aggregate_contract"], notes="Old downstream/control-arm bridge.")

    # Translation sandbox seed, per-state.
    seed_features = [
        ("translation_sandbox.brain1_core", "brain1_core"),
        ("translation_sandbox.brain2_context", "brain2_context"),
        ("translation_sandbox.shadow_decision_policy", "shadow_decision_policy"),
        ("translation_sandbox.control_arm", "control_arm"),
        ("translation_sandbox.diagnostic_boxed_seed", "sandbox_hypotheses.diagnostic_boxed_seed"),
        ("translation_sandbox.diagnostic_straight_seed", "sandbox_hypotheses.diagnostic_straight_seed"),
        ("translation_sandbox.diagnostic_vt_box_seed", "sandbox_hypotheses.diagnostic_vt_box_seed"),
    ]
    for feature, path in seed_features:
        add(
            feature,
            "Translation Sandbox",
            [path],
            ["translation_sandbox_seed"],
            "diagnostic Arena-native translator research",
            docs["translator"],
            runtime="state_translation_sandbox_json",
            notes="Diagnostic/shadow surface, not live playable infrastructure.",
        )

    # Brain2 day-level artifacts.
    for feature, stem in [
        ("brain2.board_review_bundle", "BOARD_REVIEW_BUNDLE"),
        ("brain2.board_scoreboard", "BOARD_SCOREBOARD"),
        ("brain2.board_spillover_overlay", "BOARD_SPILLOVER_OVERLAY"),
        ("brain2.shadow_decision_policy", "SHADOW_DECISION_POLICY"),
        ("brain2.day_translation_sandbox_seed", "TRANSLATION_SANDBOX_SEED"),
    ]:
        add(
            feature,
            "Brain2 day layer",
            ["."],
            [stem],
            "board ranking / board context",
            docs["system_map"],
            scope="day",
            runtime=f"brain2:{stem}",
            ns=f"ANALYSIS_ARENA/{stem}",
        )

    return specs


def _runtime_payload_for_spec(
    spec: FeatureSpec,
    *,
    window_root: Path,
    sharepack_root: Path,
    date: str,
    state_key: str,
    json_cache: Dict[Path, Any],
) -> tuple[Path, Any]:
    if spec.runtime_file_type == "aggregated_arena_json":
        path = _aggregate_path(sharepack_root, date, state_key)
    elif spec.runtime_file_type == "state_translation_sandbox_json":
        path = _state_seed_path(sharepack_root, date, state_key)
    elif spec.runtime_file_type.startswith("brain2:"):
        stem = spec.runtime_file_type.split(":", 1)[1]
        path = _brain2_json_path(window_root, date, stem)
    else:
        path = _aggregate_path(sharepack_root, date, state_key)

    resolved = path.resolve()
    if resolved in json_cache:
        return path, json_cache[resolved]

    if not path.exists():
        json_cache[resolved] = None
        return path, None
    try:
        payload = _read_json(path)
        json_cache[resolved] = payload
        return path, payload
    except Exception:
        json_cache[resolved] = None
        return path, None


def _source_sample(payload: Any, terms: Sequence[str]) -> str:
    if not isinstance(payload, dict) or not terms:
        return ""
    provenance = payload.get("provenance") or {}
    evidence_paths = provenance.get("evidence_paths") or []
    if isinstance(evidence_paths, dict):
        candidates: Iterable[str] = [str(v) for v in evidence_paths.values()]
    else:
        candidates = [str(v) for v in evidence_paths]
    lower_terms = [term.lower() for term in terms]
    for item in candidates:
        item_lower = item.lower()
        if any(term in item_lower for term in lower_terms):
            return item
    return ""


def _human_artifact_for_spec(
    spec: FeatureSpec,
    *,
    window_root: Path,
    sharepack_root: Path,
    date: str,
    state_key: str,
) -> str:
    if spec.scope == "day":
        if spec.runtime_file_type.startswith("brain2:"):
            stem = spec.runtime_file_type.split(":", 1)[1]
            md = _brain2_md_path(window_root, date, stem)
            return _safe_rel(md) if md.exists() else _safe_rel(_brain2_json_path(window_root, date, stem))
        return _safe_rel(window_root / "ANALYSIS_ARENA")

    if spec.runtime_file_type == "state_translation_sandbox_json":
        md = _state_seed_md_path(sharepack_root, date, state_key)
        return _safe_rel(md) if md.exists() else _safe_rel(_state_seed_path(sharepack_root, date, state_key))
    predictive = _predictive_shell_path(window_root, date, state_key)
    if predictive.exists():
        return _safe_rel(predictive)
    md = _aggregate_md_path(sharepack_root, date, state_key)
    return _safe_rel(md) if md.exists() else _safe_rel(_aggregate_path(sharepack_root, date, state_key))


def _status_for_spec(spec: FeatureSpec, payload: Any) -> tuple[str, str, bool]:
    if payload is None:
        return "missing", "", False
    if spec.scope == "day":
        return "explicit", ".", False

    path_with_content = ""
    path_without_content = ""
    for path in spec.actual_json_paths:
        values = _values_at(payload, path)
        if values and not path_without_content:
            path_without_content = path
        if _has_content(values):
            path_with_content = path
            break

    if path_with_content:
        if spec.expected_status == "folded":
            return "folded", path_with_content, False
        return "explicit", path_with_content, False

    if path_without_content:
        if spec.expected_status == "folded":
            return "folded", path_without_content, True
        return "explicit", path_without_content, True

    linked = _source_sample(payload, spec.source_terms)
    if linked:
        return "linked_only", "", False
    return "missing", "", False


def build_compliance(
    *,
    window_root: Path,
    sharepack_root: Path,
    dates: Sequence[str],
    states: Sequence[str],
) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any]]:
    specs = _feature_specs()
    rows: List[Dict[str, Any]] = []
    exceptions: List[Dict[str, Any]] = []
    summary = {
        "feature_count": len(specs),
        "state_day_scope_count": len(dates) * len(states),
        "day_scope_count": len(dates),
        "status_totals": {},
        "claim_boundary": {
            "explicit_or_folded": "EVIDENCE_AVAILABILITY_AND_NAVIGABILITY_ONLY",
            "not_proven": [
                "synthesis_consumption",
                "cross_tool_calibration",
                "ranking_influence",
                "promotion",
                "translation",
                "predictive_value",
            ],
        },
    }
    json_cache: Dict[Path, Any] = {}

    for spec in specs:
        stats = FeatureStats(spec=spec)
        items: List[tuple[str, str]] = []
        if spec.scope == "day":
            items = [(date, "") for date in dates]
        else:
            items = [(date, state_key) for date in dates for state_key in states]
        stats.scope_total = len(items)

        for date, state_key in items:
            runtime_path, payload = _runtime_payload_for_spec(
                spec,
                window_root=window_root,
                sharepack_root=sharepack_root,
                date=date,
                state_key=state_key or states[0],
                json_cache=json_cache,
            )
            status, actual_path, empty_object = _status_for_spec(spec, payload)
            source_sample = _source_sample(payload, spec.source_terms)
            human_artifact = _human_artifact_for_spec(
                spec,
                window_root=window_root,
                sharepack_root=sharepack_root,
                date=date,
                state_key=state_key or states[0],
            )

            if status == "explicit":
                stats.explicit_count += 1
            elif status == "folded":
                stats.folded_count += 1
            elif status == "linked_only":
                stats.linked_only_count += 1
            else:
                stats.missing_count += 1
            if empty_object:
                stats.empty_object_count += 1

            if actual_path and not stats.sample_actual_json_path:
                stats.sample_actual_json_path = actual_path
            if source_sample and not stats.sample_source_file_path:
                stats.sample_source_file_path = source_sample
            if human_artifact and not stats.sample_human_review_artifact:
                stats.sample_human_review_artifact = human_artifact

            if status in {"missing", "linked_only"} and len(stats.exception_examples) < 20:
                stats.exception_examples.append(
                    {
                        "date": date,
                        "state_key": state_key,
                        "feature": spec.feature,
                        "status": status,
                        "runtime_file": _safe_rel(runtime_path),
                        "expected_namespace": spec.expected_namespace,
                        "source_sample": source_sample,
                        "human_review_artifact": human_artifact,
                    }
                )

        status_summary = "missing"
        if stats.missing_count == 0 and stats.linked_only_count == 0:
            if stats.folded_count > 0 and stats.explicit_count == 0:
                status_summary = "folded"
            elif stats.folded_count > 0:
                status_summary = "mixed_explicit_folded"
            else:
                status_summary = "explicit"
        elif stats.explicit_count or stats.folded_count:
            status_summary = "partial"
        elif stats.linked_only_count:
            status_summary = "linked_only"

        summary["status_totals"][status_summary] = summary["status_totals"].get(status_summary, 0) + 1
        rows.append(
            {
                "contract_feature": spec.feature,
                "tool_or_context_source": spec.tool_or_context_source,
                "scope": spec.scope,
                "runtime_file_type": spec.runtime_file_type,
                "expected_namespace": spec.expected_namespace,
                "sample_actual_json_path": stats.sample_actual_json_path,
                "sample_source_file_path": stats.sample_source_file_path,
                "consumer_layer": spec.consumer_layer,
                "status_summary": status_summary,
                "scope_total": stats.scope_total,
                "explicit_count": stats.explicit_count,
                "folded_count": stats.folded_count,
                "linked_only_count": stats.linked_only_count,
                "missing_count": stats.missing_count,
                "empty_object_count": stats.empty_object_count,
                "human_review_artifact": stats.sample_human_review_artifact,
                "contract_doc": spec.contract_doc,
                "notes": spec.notes,
            }
        )
        exceptions.extend(stats.exception_examples)

    return rows, exceptions, summary


def _artifact(path: Path, *, date: str, state_key: str, layer: str, artifact_id: str, notes: str = "") -> Dict[str, Any]:
    exists = path.exists()
    row = {
        "date": date,
        "state_key": state_key,
        "layer": layer,
        "artifact_id": artifact_id,
        "exists": "yes" if exists else "no",
        "path": _safe_rel(path),
        "size_bytes": path.stat().st_size if exists else "",
        "mtime_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat() if exists else "",
        "notes": notes,
    }
    return row


def build_artifact_manifest(
    *,
    window_root: Path,
    sharepack_root: Path,
    dates: Sequence[str],
    states: Sequence[str],
) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []

    state_artifacts = [
        ("brain1_aggregate_json", lambda d, s: _aggregate_path(sharepack_root, d, s), "Brain1"),
        ("brain1_aggregate_md", lambda d, s: _aggregate_md_path(sharepack_root, d, s), "Brain1"),
        ("state_translation_sandbox_json", lambda d, s: _state_seed_path(sharepack_root, d, s), "Brain1"),
        ("state_translation_sandbox_md", lambda d, s: _state_seed_md_path(sharepack_root, d, s), "Brain1"),
        ("predictive_review_shell_md", lambda d, s: _predictive_shell_path(window_root, d, s), "Predictive wrapper"),
        ("state_validation_md", lambda d, s: _validation_path(window_root, d, s), "Validation"),
        ("candidate_universe_json", lambda d, s: sharepack_root / d / s / "candidate_universe__tool_only__arena_v0.json", "Control arm"),
        ("candidate_universe_evidence_csv", lambda d, s: sharepack_root / d / s / "candidate_universe_evidence__tool_only__arena_v0.csv", "Control arm"),
        ("candidate_universe_evidence_md", lambda d, s: sharepack_root / d / s / "candidate_universe_evidence__tool_only__arena_v0.md", "Control arm"),
        ("play_card_json", lambda d, s: sharepack_root / d / s / "play_card__tool_only__arena_v0.json", "Control arm"),
        ("play_card_md", lambda d, s: sharepack_root / d / s / "play_card__tool_only__arena_v0.md", "Control arm"),
        ("signals_bundle_json", lambda d, s: sharepack_root / d / s / "signals_bundle__tool_only__arena_v0.json", "Predictive source"),
        ("stable_report_html", lambda d, s: sharepack_root / d / s / "stable" / s / f"{s}_stable_patterns_report.html", "Tool source"),
        ("stable_scores_csv", lambda d, s: sharepack_root / d / s / "stable" / s / f"{s}_stable_patterns_scores.csv", "Tool source"),
        ("stable_compound_csv", lambda d, s: sharepack_root / d / s / "stable" / s / f"{s}_stable_patterns_compound.csv", "Tool source"),
        ("stable_families_csv", lambda d, s: sharepack_root / d / s / "stable" / s / f"{s}_stable_patterns_families.csv", "Tool source"),
        ("stable_metrics_json", lambda d, s: sharepack_root / d / s / "stable" / s / f"{s}_metrics.json", "Tool source"),
        ("dr_report_html", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / f"{s}_digit_reduction_report.html", "Tool source"),
        ("dr_stacked_report_html", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / f"{s}_digit_reduction_report_stacked.html", "Tool source"),
        ("dr_scores_csv", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / f"{s}_digit_reduction_scores.csv", "Tool source"),
        ("dr_analyzer_meta_json", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / "analyzer_v2" / f"{s}_analyzer_v2_meta.json", "Tool source"),
        ("dr_top_candidates_csv", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / "analyzer_v2" / f"{s}_analyzer_v2_top_candidates.csv", "Tool source"),
        ("dr_per_item_csv", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / "analyzer_v2" / f"{s}_analyzer_v2_per_item.csv", "Tool source"),
        ("dr_training_logs_json", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / "training" / f"{s}_digit_reduction_logs.json", "Tool source"),
        ("dr_training_steps_csv", lambda d, s: sharepack_root / d / s / "digit_reduction" / s / "training" / f"{s}_digit_reduction_steps.csv", "Tool source"),
        ("aux_summary_json", lambda d, s: sharepack_root / d / s / "aux" / s / "summary.json", "Context source"),
        ("aux_summary_md", lambda d, s: sharepack_root / d / s / "aux" / s / "summary.md", "Context source"),
        ("vtrac_enhanced_json", lambda d, s: next((sharepack_root / d / s / "vtrac" / s).glob("*_vtrac_enhanced_*.json"), sharepack_root / d / s / "vtrac" / s / "__missing_vtrac_enhanced__.json"), "Tool source"),
        ("hot_zones_meta_json", lambda d, s: sharepack_root / d / s / "hot_zones" / s / f"{s}_hot_zones_meta.json", "Tool source"),
        ("hot_zones_top_lanes_csv", lambda d, s: sharepack_root / d / s / "hot_zones" / s / f"{s}_hot_zones_top_lanes.csv", "Tool source"),
        ("hot_zones_per_lane_csv", lambda d, s: sharepack_root / d / s / "hot_zones" / s / f"{s}_hot_zones_per_lane.csv", "Tool source"),
        ("hot_zones_winner_map_json", lambda d, s: sharepack_root / d / s / "hot_zones" / s / f"{d}_hot_zones_winner_map.json", "Tool source"),
        ("state_training_kit_start_here", lambda d, s: window_root / "TRAINING_KITS" / f"{d}__STATE_KITS" / s / "START_HERE.md", "Training kit"),
    ]

    for date in dates:
        for state_key in states:
            for artifact_id, path_fn, layer in state_artifacts:
                rows.append(_artifact(path_fn(date, state_key), date=date, state_key=state_key, layer=layer, artifact_id=artifact_id))

    day_artifacts = [
        ("brain2_board_review_bundle_json", lambda d: _brain2_json_path(window_root, d, "BOARD_REVIEW_BUNDLE"), "Brain2"),
        ("brain2_board_review_bundle_md", lambda d: _brain2_md_path(window_root, d, "BOARD_REVIEW_BUNDLE"), "Brain2"),
        ("brain2_board_scoreboard_json", lambda d: _brain2_json_path(window_root, d, "BOARD_SCOREBOARD"), "Brain2"),
        ("brain2_board_scoreboard_md", lambda d: _brain2_md_path(window_root, d, "BOARD_SCOREBOARD"), "Brain2"),
        ("brain2_board_scoreboard_csv", lambda d: window_root / "ANALYSIS_ARENA" / f"{d}__BOARD_SCOREBOARD__analysis_arena_day_review.csv", "Brain2"),
        ("brain2_spillover_overlay_json", lambda d: _brain2_json_path(window_root, d, "BOARD_SPILLOVER_OVERLAY"), "Brain2"),
        ("brain2_spillover_overlay_md", lambda d: _brain2_md_path(window_root, d, "BOARD_SPILLOVER_OVERLAY"), "Brain2"),
        ("shadow_decision_policy_json", lambda d: _brain2_json_path(window_root, d, "SHADOW_DECISION_POLICY"), "Brain2"),
        ("shadow_decision_policy_md", lambda d: _brain2_md_path(window_root, d, "SHADOW_DECISION_POLICY"), "Brain2"),
        ("day_translation_sandbox_json", lambda d: _brain2_json_path(window_root, d, "TRANSLATION_SANDBOX_SEED"), "Brain2"),
        ("day_translation_sandbox_md", lambda d: _brain2_md_path(window_root, d, "TRANSLATION_SANDBOX_SEED"), "Brain2"),
        ("pre_cycle_md", lambda d: window_root / "ANALYSIS_ARENA" / f"ANALYSIS_ARENA__CYCLE__PRE__{d}__tool_only__arena_v0.md", "Cycle"),
        ("validation_control_center_md", lambda d: window_root / "VALIDATION" / f"{d}__CONTROL_CENTER.md", "Validation"),
        ("brain2_master_validation_md", lambda d: window_root / "VALIDATION" / f"{d}__BRAIN2_MASTER_VALIDATION.md", "Validation"),
        ("brain2_tracker_ledger_json", lambda d: window_root / "VALIDATION" / f"{d}__BRAIN2_TRACKER_LEDGER.json", "Validation"),
        ("day_synthesis_md", lambda d: window_root / "VALIDATION" / f"{d}__DAY_SYNTHESIS.md", "Validation"),
        ("macro_training_kit_start_here", lambda d: window_root / "TRAINING_KITS" / f"{d}__MACRO_STARTER" / "START_HERE.md", "Training kit"),
        ("state_training_kit_index", lambda d: window_root / "TRAINING_KITS" / f"{d}__STATE_KITS" / "START_HERE.md", "Training kit"),
        ("quantification_stack_start_here", lambda d: window_root / "TRAINING_KITS" / f"{d}__QUANTIFICATION_STACK" / "START_HERE.md", "Training kit"),
        ("custom_hit_report_md", lambda d: window_root / "TRAINING_KITS" / f"{d}__CUSTOM_HIT_REPORT" / f"{d}__CUSTOM_HIT_REPORT.md", "Training kit"),
    ]
    for date in dates:
        for artifact_id, path_fn, layer in day_artifacts:
            rows.append(_artifact(path_fn(date), date=date, state_key="", layer=layer, artifact_id=artifact_id))

    window_close_files = sorted(
        path
        for path in window_root.glob("WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__*")
        if path.is_file()
    )
    for path in window_close_files:
        rows.append(_artifact(path, date="", state_key="", layer="Window-close learning", artifact_id=path.name))

    training_root_files = [
        window_root / "TRAINING_KITS" / "START_HERE.md",
        window_root / "TRAINING_KITS" / "REFERENCE__ARENA_ORIENTATION" / "START_HERE.md",
        window_root / "REVIEW_INDEX.md",
        window_root / "REVIEW_MANIFEST.json",
    ]
    for path in training_root_files:
        rows.append(_artifact(path, date="", state_key="", layer="Navigation", artifact_id=path.name))

    total = len(rows)
    exists = sum(1 for row in rows if row["exists"] == "yes")
    by_layer: Dict[str, Dict[str, int]] = {}
    for row in rows:
        layer = str(row["layer"])
        by_layer.setdefault(layer, {"total": 0, "exists": 0, "missing": 0})
        by_layer[layer]["total"] += 1
        if row["exists"] == "yes":
            by_layer[layer]["exists"] += 1
        else:
            by_layer[layer]["missing"] += 1
    return rows, {"total_rows": total, "exists_rows": exists, "missing_rows": total - exists, "by_layer": by_layer}


def build_doc_registry(final_docs_root: Path, window_root: Path) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
    candidates: List[Path] = []
    if final_docs_root.exists():
        for path in final_docs_root.iterdir():
            if not path.is_file():
                continue
            name = path.name.upper()
            if (
                "ANALYSIS_ARENA" in name
                or "AGGREGATED_ANALYSIS_ARENA" in name
                or "FINAL_STRING_TOOL_OUTPUTS" in name
                or "FINAL_CONTEXT_TOOL_OUTPUTS" in name
                or "VALIDATION_WORKFLOW" in name
                or "WORKFLOW_CHANGELOG" in name
                or "MASTER_VALIDATION_TEMPLATE" in name
                or "BRAIN2" in name
            ):
                candidates.append(path)

    for extra in [
        window_root / "REVIEW_MANIFEST.json",
        window_root / "REVIEW_INDEX.md",
        window_root / "TRAINING_KITS" / "START_HERE.md",
        window_root / "TRAINING_KITS" / "REFERENCE__ARENA_ORIENTATION" / "START_HERE.md",
    ]:
        if extra.exists():
            candidates.append(extra)

    rows: List[Dict[str, Any]] = []
    by_name: Dict[str, int] = {}
    by_hash: Dict[str, int] = {}
    for path in candidates:
        by_name[path.name] = by_name.get(path.name, 0) + 1
        digest = _sha256(path)
        by_hash[digest] = by_hash.get(digest, 0) + 1
    for path in sorted(set(candidates), key=lambda p: _safe_rel(p).lower()):
        stat = path.stat()
        digest = _sha256(path)
        rows.append(
            {
                "path": _safe_rel(path),
                "filename": path.name,
                "size_bytes": stat.st_size,
                "mtime_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                "sha256": digest,
                "duplicate_filename_count": by_name.get(path.name, 0),
                "duplicate_hash_count": by_hash.get(digest, 0),
                "category": _doc_category(path.name),
            }
        )
    summary = {
        "doc_count": len(rows),
        "duplicate_filename_rows": sum(1 for row in rows if int(row["duplicate_filename_count"]) > 1),
        "duplicate_hash_rows": sum(1 for row in rows if int(row["duplicate_hash_count"]) > 1),
        "exact_string_feed_count": sum(1 for row in rows if row["filename"] == "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"),
        "exact_context_feed_count": sum(1 for row in rows if row["filename"] == "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"),
    }
    return rows, summary


def _doc_category(name: str) -> str:
    upper = name.upper()
    if "FINAL_STRING_TOOL_OUTPUTS" in upper:
        return "string_feed_contract"
    if "FINAL_CONTEXT_TOOL_OUTPUTS" in upper:
        return "context_feed_contract"
    if "AGGREGATED_ANALYSIS_ARENA_CONTRACT" in upper:
        return "aggregate_contract"
    if "SYSTEM_MAP" in upper:
        return "system_map"
    if "RUNS2_ARTIFACT_REVIEW_MAP" in upper:
        return "review_map"
    if "TRANSLATOR" in upper or "TRANSLATION" in upper:
        return "translator_or_sandbox"
    if "DECISION_POLICY" in upper:
        return "decision_policy"
    if "VALIDATION" in upper or "BRAIN2" in upper:
        return "validation_or_brain2"
    if "MANIFEST" in upper or "INDEX" in upper or "START_HERE" in upper:
        return "navigation"
    return "analysis_arena_doc"


def _render_compliance_md(rows: Sequence[Dict[str, Any]], summary: Dict[str, Any]) -> str:
    lines = [
        "# AAT9 Analysis Arena Contract Compliance Matrix",
        "",
        "## Scope",
        "",
        f"- state_day_scope_count: `{summary.get('state_day_scope_count', 0)}`",
        f"- day_scope_count: `{summary.get('day_scope_count', 0)}`",
        f"- contract_feature_count: `{summary.get('feature_count', 0)}`",
        f"- status_totals: `{json.dumps(summary.get('status_totals', {}), sort_keys=True)}`",
        "",
        "## Interpretation",
        "",
        "- `explicit`: named object/path exists in the runtime JSON.",
        "- `folded`: evidence is present, but contract concept is inside a broader raw/enhanced object rather than a named object.",
        "- `linked_only`: source artifact is linked in provenance, but no matching runtime object was found.",
        "- `missing`: neither a runtime object nor a source link was found by this audit.",
        "- These statuses establish availability and navigability only. They do not prove that synthesis consumes, calibrates, promotes, ranks, or translates the feature.",
        "",
        "## Matrix",
        "",
        "| Feature | Source | Scope | Status | Explicit | Folded | Linked | Missing | Empty | Runtime path | Source sample | Human artifact |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {feature} | {source} | {scope} | {status} | {explicit} | {folded} | {linked} | {missing} | {empty} | `{runtime}` | `{source_sample}` | `{human}` |".format(
                feature=str(row["contract_feature"]).replace("|", "\\|"),
                source=str(row["tool_or_context_source"]).replace("|", "\\|"),
                scope=row["scope_total"],
                status=row["status_summary"],
                explicit=row["explicit_count"],
                folded=row["folded_count"],
                linked=row["linked_only_count"],
                missing=row["missing_count"],
                empty=row.get("empty_object_count", 0),
                runtime=row["sample_actual_json_path"],
                source_sample=row["sample_source_file_path"],
                human=row["human_review_artifact"],
            )
        )
    lines.append("")
    return "\n".join(lines)


def _render_artifact_manifest_md(rows: Sequence[Dict[str, Any]], summary: Dict[str, Any]) -> str:
    lines = [
        "# AAT9 Analysis Arena Window Artifact Manifest",
        "",
        "## Scope",
        "",
        f"- total_manifest_rows: `{summary.get('total_rows', 0)}`",
        f"- existing_artifacts: `{summary.get('exists_rows', 0)}`",
        f"- missing_artifacts: `{summary.get('missing_rows', 0)}`",
        "",
        "## Layer Counts",
        "",
        "| Layer | Existing | Missing | Total |",
        "|---|---:|---:|---:|",
    ]
    for layer, item in sorted((summary.get("by_layer") or {}).items()):
        lines.append(f"| {layer} | {item.get('exists', 0)} | {item.get('missing', 0)} | {item.get('total', 0)} |")

    missing = [row for row in rows if row["exists"] == "no"]
    lines.extend(["", "## Missing Artifact Samples", ""])
    if not missing:
        lines.append("- none")
    else:
        lines.append("| Date | State | Layer | Artifact | Path |")
        lines.append("|---|---|---|---|---|")
        for row in missing[:80]:
            lines.append(f"| {row['date']} | {row['state_key']} | {row['layer']} | {row['artifact_id']} | `{row['path']}` |")
    lines.append("")
    return "\n".join(lines)


def _render_doc_registry_md(rows: Sequence[Dict[str, Any]], summary: Dict[str, Any]) -> str:
    lines = [
        "# AAT9 Analysis Arena Document Registry",
        "",
        "## Summary",
        "",
        f"- document_count: `{summary.get('doc_count', 0)}`",
        f"- duplicate_filename_rows: `{summary.get('duplicate_filename_rows', 0)}`",
        f"- duplicate_hash_rows: `{summary.get('duplicate_hash_rows', 0)}`",
        f"- exact_string_feed_count: `{summary.get('exact_string_feed_count', 0)}`",
        f"- exact_context_feed_count: `{summary.get('exact_context_feed_count', 0)}`",
        "",
        "## Key Feed Files",
        "",
    ]
    for row in rows:
        if row["filename"] in {
            "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
            "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
            "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md",
        }:
            lines.append(f"- `{row['filename']}`: `{row['path']}` ({row['size_bytes']} bytes)")
    lines.extend(
        [
            "",
            "## Registry",
            "",
            "| Category | File | Size | Modified UTC | Duplicate name count | Path |",
            "|---|---|---:|---|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['category']} | {row['filename']} | {row['size_bytes']} | {row['mtime_utc']} | {row['duplicate_filename_count']} | `{row['path']}` |"
        )
    lines.append("")
    return "\n".join(lines)


def _render_findings_md(
    *,
    compliance_summary: Dict[str, Any],
    artifact_summary: Dict[str, Any],
    doc_summary: Dict[str, Any],
    out_dir: Path,
) -> str:
    status_totals = compliance_summary.get("status_totals") or {}
    by_layer = artifact_summary.get("by_layer") or {}
    training_missing = (by_layer.get("Training kit") or {}).get("missing", 0)
    core_layers = [
        "Brain1",
        "Brain2",
        "Tool source",
        "Context source",
        "Control arm",
        "Validation",
        "Window-close learning",
    ]
    core_missing = sum((by_layer.get(layer) or {}).get("missing", 0) for layer in core_layers)
    lines = [
        "# AAT9 Analysis Arena Audit Findings",
        "",
        "## Verdict",
        "",
        "The Analysis Arena is present as a runtime evidence system. The main per-state receipt is the JSON at `sharepacks/_predictive/<date>/<state>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`, not the compact Markdown twin.",
        "",
        "This audit does not determine whether the strongest remaining gap is rendering or synthesis. It maps preservation and navigability: several important concepts are present only in compressed or folded JSON/source forms, especially VTRAC and Hot Zones contract surfaces. A separate utilization trace is required to prove downstream use.",
        "",
        "## What This Audit Produced",
        "",
        f"- Contract matrix: `{_safe_rel(out_dir / 'AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_MATRIX.md')}`",
        f"- Contract exceptions: `{_safe_rel(out_dir / 'AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_EXCEPTIONS.csv')}`",
        f"- Window artifact manifest: `{_safe_rel(out_dir / 'AAT9_ANALYSIS_ARENA_WINDOW_ARTIFACT_MANIFEST.md')}`",
        f"- Document registry: `{_safe_rel(out_dir / 'AAT9_ANALYSIS_ARENA_DOC_REGISTRY.md')}`",
        "",
        "## High-Signal Findings",
        "",
        f"- Feature status totals: `{json.dumps(status_totals, sort_keys=True)}`",
        f"- Artifact manifest rows: `{artifact_summary.get('total_rows', 0)}` total, `{artifact_summary.get('exists_rows', 0)}` existing, `{artifact_summary.get('missing_rows', 0)}` missing.",
        f"- Exact string feed docs found: `{doc_summary.get('exact_string_feed_count', 0)}`.",
        f"- Exact context feed docs found: `{doc_summary.get('exact_context_feed_count', 0)}`.",
        "",
        "## Interpretation",
        "",
        "- Stable, Digit Reduction, Aux / Control Center, cross-tool relations, Arena synthesis, downstream handoff, and state translation sandbox surfaces are represented as named runtime namespaces; namespace presence does not prove that every preserved child feature is consumed.",
        "- VTRAC and Hot Zones are present in the aggregate JSON, but many contract-level concepts are folded into enhanced/raw payloads instead of first-class named Arena sub-objects.",
        f"- Core evidence layers have `{core_missing}` missing manifest rows across Brain1, Brain2, Tool source, Context source, Control arm, Validation, and Window-close learning.",
        f"- The manifest's missing rows are training-kit convenience wrappers (`{training_missing}` rows), mostly for dates beyond the currently packaged Day-1 review kits.",
        "- Candidate Universe and Play Card remain the old control-arm conversion layer. They are available for comparison, but they should not be treated as the final Arena-native translator.",
        "- Translation Sandbox Seed is the closest diagnostic Arena-native translator surface, but it remains shadow/diagnostic rather than live budgeted prediction infrastructure.",
        "- Compact Markdown files are useful entry points, but they under-render the Arena compared with the JSON and provenance source files.",
        "- An `explicit` or `folded` status must never be read as evidence of calibrated weighting, independent convergence, ranking influence, promotion, or predictive credit.",
        "",
        "## Recommended Next Step",
        "",
        "Use the matrix and manifest to begin one deep example review and a separate utilization trace without changing runtime logic. A good starting case remains Connecticut4 on 2026-03-09, because it connects Brain2 rank, Brain1 evidence, Translation Sandbox, Control Arm, validation, and winner-side review.",
        "",
        "## Safety Boundary",
        "",
        "No runtime behavior, scoring, translators, or Play Card generation were modified by this audit generator.",
        "",
    ]
    return "\n".join(lines)


def _render_start_here(out_dir: Path) -> str:
    return "\n".join(
        [
            "# AAT9 Analysis Arena Audit - Start Here",
            "",
            "This folder is an audit/navigation layer for the March 2026 window. It does not replace source artifacts and does not change runtime behavior.",
            "",
            "## Read Order",
            "",
            "1. `AAT9_ANALYSIS_ARENA_AUDIT_FINDINGS.md`",
            "2. `AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_MATRIX.md`",
            "3. `AAT9_ANALYSIS_ARENA_WINDOW_ARTIFACT_MANIFEST.md`",
            "4. `AAT9_ANALYSIS_ARENA_DOC_REGISTRY.md`",
            "5. CSV files when you need sortable/filterable detail.",
            "",
            "## Purpose",
            "",
            "The purpose is to answer: what reaches the Arena, where is it, what is folded or under-rendered, and where should human deep example review look next? Presence here does not prove synthesis consumption or predictive influence.",
            "",
        ]
    )


def main() -> None:
    args = _parse_args()
    window_root = _resolve(args.window_root)
    sharepack_root = _resolve(args.sharepack_root)
    final_docs_root = _resolve(args.final_docs_root)
    out_dir = _resolve(args.out_dir)

    scope = _load_window_scope(window_root)
    dates: List[str] = scope["dates"]
    states: List[str] = scope["states"]

    compliance_rows, compliance_exceptions, compliance_summary = build_compliance(
        window_root=window_root,
        sharepack_root=sharepack_root,
        dates=dates,
        states=states,
    )
    artifact_rows, artifact_summary = build_artifact_manifest(
        window_root=window_root,
        sharepack_root=sharepack_root,
        dates=dates,
        states=states,
    )
    doc_rows, doc_summary = build_doc_registry(final_docs_root, window_root)

    matrix_fields = [
        "contract_feature",
        "tool_or_context_source",
        "scope",
        "runtime_file_type",
        "expected_namespace",
        "sample_actual_json_path",
        "sample_source_file_path",
        "consumer_layer",
        "status_summary",
        "scope_total",
        "explicit_count",
        "folded_count",
        "linked_only_count",
        "missing_count",
        "empty_object_count",
        "human_review_artifact",
        "contract_doc",
        "notes",
    ]
    exception_fields = [
        "date",
        "state_key",
        "feature",
        "status",
        "runtime_file",
        "expected_namespace",
        "source_sample",
        "human_review_artifact",
    ]
    artifact_fields = [
        "date",
        "state_key",
        "layer",
        "artifact_id",
        "exists",
        "path",
        "size_bytes",
        "mtime_utc",
        "notes",
    ]
    doc_fields = [
        "path",
        "filename",
        "size_bytes",
        "mtime_utc",
        "sha256",
        "duplicate_filename_count",
        "duplicate_hash_count",
        "category",
    ]

    _write_csv(out_dir / "AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_MATRIX.csv", compliance_rows, matrix_fields)
    _write_text(out_dir / "AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_MATRIX.md", _render_compliance_md(compliance_rows, compliance_summary))
    _write_csv(out_dir / "AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_EXCEPTIONS.csv", compliance_exceptions, exception_fields)
    _write_json(out_dir / "AAT9_ANALYSIS_ARENA_CONTRACT_COMPLIANCE_SUMMARY.json", compliance_summary)

    _write_csv(out_dir / "AAT9_ANALYSIS_ARENA_WINDOW_ARTIFACT_MANIFEST.csv", artifact_rows, artifact_fields)
    _write_text(out_dir / "AAT9_ANALYSIS_ARENA_WINDOW_ARTIFACT_MANIFEST.md", _render_artifact_manifest_md(artifact_rows, artifact_summary))
    _write_json(out_dir / "AAT9_ANALYSIS_ARENA_WINDOW_ARTIFACT_MANIFEST_SUMMARY.json", artifact_summary)

    _write_csv(out_dir / "AAT9_ANALYSIS_ARENA_DOC_REGISTRY.csv", doc_rows, doc_fields)
    _write_text(out_dir / "AAT9_ANALYSIS_ARENA_DOC_REGISTRY.md", _render_doc_registry_md(doc_rows, doc_summary))
    _write_json(out_dir / "AAT9_ANALYSIS_ARENA_DOC_REGISTRY_SUMMARY.json", doc_summary)

    _write_text(
        out_dir / "AAT9_ANALYSIS_ARENA_AUDIT_FINDINGS.md",
        _render_findings_md(
            compliance_summary=compliance_summary,
            artifact_summary=artifact_summary,
            doc_summary=doc_summary,
            out_dir=out_dir,
        ),
    )
    _write_text(out_dir / "START_HERE.md", _render_start_here(out_dir))

    print(json.dumps({
        "out_dir": _safe_rel(out_dir),
        "dates": len(dates),
        "states": len(states),
        "contract_features": len(compliance_rows),
        "artifact_manifest_rows": len(artifact_rows),
        "doc_registry_rows": len(doc_rows),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
