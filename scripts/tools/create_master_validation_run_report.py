#!/usr/bin/env python3
"""
Create an arena-native per-state Master Validation run report.

This report is the state-level post-results companion for the Analysis Arena
branch. It intentionally joins:

- frozen winners truth from `sharepacks/<D>/<STATE>/winners/...`
- predictive/runtime evidence from `sharepacks/_predictive/<D>/<STATE>/...`
- arena receipts such as aggregated analysis arena, translation sandbox, and
  downstream control-arm artifacts

It does NOT rebuild analyzers or regenerate sharepacks.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS2_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
STATE_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
ARENA_CONTRACT_PATH = FINAL_DOCS_DIR / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md"
CONTEXT_FEED_PATH = FINAL_DOCS_DIR / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"
STRING_FEED_PATH = FINAL_DOCS_DIR / "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"
SYSTEM_MAP_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md"
TRANSLATION_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
BRAIN2_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
BRAIN2_MV_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    return raw.replace(" ", "_")


def normalize_pick3_literal(value: Any) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else digits


def canonicalize(value: str) -> str:
    digits = normalize_pick3_literal(value)
    return "".join(sorted(digits)) if len(digits) == 3 else ""


def results_state_name(state: str) -> str:
    base = re.sub(r"\d+$", "", state)
    specials = {
        "NewYork": "New York",
        "NewJersey": "New Jersey",
        "NorthCarolina": "North Carolina",
        "SouthCarolina": "South Carolina",
        "PuertoRico": "Puerto Rico",
        "OntarioCanada": "Ontario",
        "WashingtonDC": "Washington, D.C.",
    }
    return specials.get(base, base)


def parse_results(*, date: str, state: str) -> dict[str, str]:
    path = REPO_ROOT / "data" / "results" / f"{date}.txt"
    if not path.exists():
        return {"midday": "", "evening": ""}

    state_label = results_state_name(state)
    for line in read_text(path).splitlines():
        if not re.match(rf"^\s*{re.escape(state_label)}(?:\s|\t)", line):
            continue
        if "\t" in line:
            parts = line.split("\t")
            midday = normalize_pick3_literal(parts[1].strip() if len(parts) > 1 else "")
            evening = normalize_pick3_literal(parts[2].strip() if len(parts) > 2 else "")
            return {"midday": midday, "evening": evening}

        nums: list[str] = []
        for part in line.replace(",", " ").split():
            lit = normalize_pick3_literal(part)
            if len(lit) == 3 and lit.isdigit():
                nums.append(lit)
        return {
            "midday": nums[0] if len(nums) >= 1 else "",
            "evening": nums[1] if len(nums) >= 2 else "",
        }

    return {"midday": "", "evening": ""}


def load_json(path: Path) -> Any:
    return json.loads(read_text(path))


def try_load_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    return load_json(path)


def list_artifacts(path: Path, pattern: str) -> list[Path]:
    if not path.exists():
        return []
    return sorted(path.glob(pattern))


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        value = str(value or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _fmt_items(values: Sequence[str], *, empty: str = "_none_") -> str:
    ordered = _ordered_unique(values)
    if not ordered:
        return empty
    return ", ".join(f"`{value}`" for value in ordered)


def _fmt_path(path: Path) -> str:
    suffix = "" if path.exists() else " (missing)"
    return f"`{safe_rel(path)}`{suffix}"


def _tagged_path(base_dir: Path, stem: str, ext: str, *, profile: str, experiment_tag: str) -> Path:
    out_suffix = "" if profile == "mixed" else f"__{profile}"
    tag_suffix = f"__{experiment_tag}" if experiment_tag else ""
    return base_dir / f"{stem}{out_suffix}{tag_suffix}.{ext}"


def _preferred_path(base_dir: Path, stem: str, ext: str, *, profile: str, experiment_tag: str) -> Path:
    tagged = _tagged_path(base_dir, stem, ext, profile=profile, experiment_tag=experiment_tag)
    if tagged.exists():
        return tagged
    untagged = _tagged_path(base_dir, stem, ext, profile=profile, experiment_tag="")
    return untagged


def _candidate_universe_summary(raw: Mapping[str, Any] | None) -> str:
    if not isinstance(raw, Mapping):
        return "Candidate Universe missing."
    packs = raw.get("packs")
    packs_count = len(packs) if isinstance(packs, list) else 0
    union_count = raw.get("union_combos_count")
    try:
        union_count = int(union_count)
    except Exception:
        union_count = len(raw.get("union_combos") or []) if isinstance(raw.get("union_combos"), list) else 0
    return f"`packs={packs_count}` | `union_combos={union_count}`"


def _play_card_summary(raw: Mapping[str, Any] | None) -> str:
    if not isinstance(raw, Mapping):
        return "Play Card missing."
    strategies = raw.get("strategies")
    if not isinstance(strategies, Mapping):
        return "Play Card has no `strategies` map."
    labels: list[str] = []
    for strategy_name, strat in list(strategies.items())[:4]:
        budgets: list[str] = []
        if isinstance(strat, Mapping):
            budgets = [key for key, value in strat.items() if isinstance(value, Mapping)]
        labels.append(f"`{strategy_name}`[{','.join(budgets[:4]) or '-'}]")
    return ", ".join(labels) if labels else "Play Card strategies unavailable."


def _ranked_values(items: Any, *, value_key: str = "value", limit: int = 6) -> list[str]:
    if not isinstance(items, list):
        return []
    out: list[str] = []
    for item in items[:limit]:
        if isinstance(item, Mapping):
            value = item.get(value_key)
        else:
            value = item
        value_s = str(value or "").strip()
        if value_s:
            out.append(value_s)
    return out


def _state_regime_summary(state_regime: Any) -> list[str]:
    if not isinstance(state_regime, Mapping):
        return []
    out: list[str] = []
    for key in [
        "dominant_canonical",
        "dominant_family",
        "dominant_vtrac_index",
        "tracker_posture",
        "survivor_pressure",
        "last_remaining",
        "hidden_terminal_support",
    ]:
        if key in state_regime:
            out.append(f"`{key}={state_regime.get(key)}`")
    return out


def _survivor_summary(data: Any) -> list[str]:
    if not isinstance(data, Mapping) or not data.get("available"):
        return ["`available=false`"]
    return [
        f"`frontier_rows={data.get('frontier_rows', 0)}`",
        f"`progressions={data.get('progression_count', 0)}`",
        f"`last_remaining_rows={data.get('last_remaining_rows', 0)}`",
        f"`hidden_terminal_frontiers={data.get('hidden_terminal_frontier_count', 0)}`",
        f"`top_frontier_canonicals={','.join((data.get('top_frontier_canonicals') or [])[:6]) or '-'}`",
    ]


def _r_consensus_summary(data: Any) -> list[str]:
    if not isinstance(data, Mapping) or not data.get("available"):
        return ["`available=false`"]
    return [
        f"`events={data.get('event_count', 0)}`",
        f"`signal_class={data.get('signal_strength_class', 'unknown')}`",
        f"`trial_eligible={data.get('trial_eligible', False)}`",
        f"`top_tails={','.join((data.get('top_tail_values') or [])[:6]) or '-'}`",
        f"`top_support={','.join((data.get('top_support_canonicals') or [])[:6]) or '-'}`",
    ]


def _watchlist_summary(items: Any, *, limit: int = 5) -> list[str]:
    if not isinstance(items, list):
        return []
    out: list[str] = []
    for item in items[:limit]:
        if not isinstance(item, Mapping):
            continue
        idx = str(item.get("vtrac_index") or "").strip()
        candidates = ",".join(item.get("candidate_canonicals") or [])
        if idx or candidates:
            out.append(f"`{idx}` -> `{candidates or '-'}`")
    return out


def _arena_objects_from_sources(
    arena: Mapping[str, Any] | None,
    signals_bundle: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {}
    signal_objects = (
        (((signals_bundle or {}).get("tools") or {}).get("aux_control_center_context") or {}).get("arena_objects") or {}
    )
    if isinstance(signal_objects, Mapping):
        out.update(signal_objects)
    arena_objects = (
        (((arena or {}).get("context_tools") or {}).get("aux_control_center") or {}).get("arena_objects") or {}
    )
    if isinstance(arena_objects, Mapping):
        out.update(arena_objects)
    return out


def _variant_label(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return "-"
    mapping = {
        "combined": "Combined",
        "midday": "Midday",
        "evening": "Evening",
        "Combined": "Combined",
        "Midday": "Midday",
        "Evening": "Evening",
    }
    return mapping.get(raw, raw.title())


def _fmt_badge_rows(rows: Any, *, literal_key: str, limit: int = 12) -> str:
    if not isinstance(rows, list):
        return "_none_"
    out: list[str] = []
    for row in rows[:limit]:
        if not isinstance(row, Mapping):
            continue
        literal = str(row.get(literal_key) or "").strip()
        if not literal:
            continue
        ds = row.get("draws_since")
        sev = str(row.get("severity") or "").strip()
        extras: list[str] = []
        if ds not in {None, ""}:
            extras.append(f"DS={ds}")
        if sev:
            extras.append(f"sev={sev}")
        out.append(f"`{literal}`[{'; '.join(extras) or '-'}]")
    return ", ".join(out) if out else "_none_"


def _fmt_multi_variant_alerts(alerts: Any, *, limit: int = 12) -> str:
    if not isinstance(alerts, Mapping):
        return "_none_"
    out: list[str] = []
    for literal, payload in list(alerts.items())[:limit]:
        if not isinstance(payload, Mapping):
            continue
        per_variant: list[str] = []
        for variant in ("combined", "midday", "evening"):
            details = payload.get(variant)
            if not isinstance(details, Mapping):
                continue
            sev = str(details.get("severity") or "").strip() or "-"
            ds = details.get("draws_since")
            part = f"{_variant_label(variant)}={sev}"
            if ds not in {None, ""}:
                part += f"/DS={ds}"
            per_variant.append(part)
        if per_variant:
            out.append(f"`{literal}`[{'; '.join(per_variant)}]")
    return ", ".join(out) if out else "_none_"


def _fmt_vtrac_overlay_rows(rows: Any, *, limit: int = 8) -> str:
    if not isinstance(rows, list):
        return "_none_"
    out: list[str] = []
    for row in rows[:limit]:
        if not isinstance(row, Mapping):
            continue
        idx = row.get("index")
        ds = row.get("draws_since")
        if idx in {None, ""}:
            continue
        extras = [f"DS={ds}"] if ds not in {None, ""} else []
        out.append(f"`{idx}`[{'; '.join(extras) or '-'}]")
    return ", ".join(out) if out else "_none_"


def _fmt_vtrac_heat_rows(rows: Any, *, limit: int = 8) -> str:
    if not isinstance(rows, list):
        return "_none_"
    out: list[str] = []
    for row in rows[:limit]:
        if not isinstance(row, Mapping):
            continue
        idx = row.get("index")
        if idx in {None, ""}:
            continue
        extras: list[str] = []
        for key, label in (("ds", "DS"), ("hazard", "HZ"), ("trend", "TR"), ("avg_gap", "AVG")):
            value = row.get(key)
            if value in {None, ""}:
                continue
            if isinstance(value, float):
                extras.append(f"{label}={value:.3f}")
            else:
                extras.append(f"{label}={value}")
        out.append(f"`{idx}`[{'; '.join(extras) or '-'}]")
    return ", ".join(out) if out else "_none_"


def _aux_inventory_sections(
    aux_summary: Mapping[str, Any] | None,
    arena: Mapping[str, Any] | None,
    signals_bundle: Mapping[str, Any] | None,
) -> dict[str, list[str]]:
    out = {
        "badge_pairs": [],
        "badge_combos": [],
        "badge_indices": [],
        "due_vtrac": [],
    }
    if not isinstance(aux_summary, Mapping):
        return out

    pairs_top = ((((aux_summary.get("pairs") or {}).get("top_by_variant")) or {}))
    pair_multi = ((((aux_summary.get("pairs") or {}).get("multi_variant_alerts")) or {}))
    for variant in ("combined", "midday", "evening"):
        payload = pairs_top.get(variant) if isinstance(pairs_top, Mapping) else None
        if not isinstance(payload, Mapping):
            continue
        repeating = payload.get("repeating") or []
        non_repeating = payload.get("non_repeating") or []
        combined_rows = [row for row in [*(repeating if isinstance(repeating, list) else []), *(non_repeating if isinstance(non_repeating, list) else [])] if isinstance(row, Mapping)]
        for severity in ("red", "blue", "purple"):
            sev_rows = [
                row
                for row in combined_rows
                if str(row.get("severity") or "").strip().lower() == severity
            ]
            if sev_rows:
                out["badge_pairs"].append(
                    f"{_variant_label(variant)} pair badges `{severity.upper()}`: {_fmt_badge_rows(sev_rows, literal_key='pair')}"
                )
    out["badge_pairs"].append(
        f"Cross-variant pair overlaps: {_fmt_multi_variant_alerts(pair_multi)}"
    )

    doubles_top = ((((aux_summary.get("doubles") or {}).get("top_by_variant")) or {}))
    doubles_multi = ((((aux_summary.get("doubles") or {}).get("multi_variant_alerts")) or {}))
    for variant in ("combined", "midday", "evening"):
        rows = doubles_top.get(variant) if isinstance(doubles_top, Mapping) else None
        if isinstance(rows, list) and rows:
            out["badge_combos"].append(
                f"{_variant_label(variant)} boxed combo badges: {_fmt_badge_rows(rows, literal_key='combo')}"
            )
    out["badge_combos"].append(
        f"Cross-variant boxed-combo overlaps: {_fmt_multi_variant_alerts(doubles_multi)}"
    )

    arena_objects = _arena_objects_from_sources(arena, signals_bundle)
    badge_pressure = arena_objects.get("aux_badge_pressure") or {}
    if isinstance(badge_pressure, Mapping):
        by_variant = (((badge_pressure.get("index_pressure") or {}).get("by_variant")) or {})
        for variant in ("combined", "midday", "evening"):
            payload = by_variant.get(variant) if isinstance(by_variant, Mapping) else None
            top_indices = (payload or {}).get("top_indices") if isinstance(payload, Mapping) else None
            if isinstance(top_indices, list) and top_indices:
                rendered: list[str] = []
                for row in top_indices[:8]:
                    if not isinstance(row, Mapping):
                        continue
                    idx = row.get("index")
                    if idx in {None, ""}:
                        continue
                    density = row.get("pressure_density")
                    raw = row.get("pressure_raw")
                    extras: list[str] = []
                    if density not in {None, ""}:
                        try:
                            extras.append(f"PD={float(density):.2f}")
                        except Exception:
                            extras.append(f"PD={density}")
                    if raw not in {None, ""}:
                        extras.append(f"RAW={raw}")
                    rendered.append(f"`{idx}`[{'; '.join(extras) or '-'}]")
                if rendered:
                    out["badge_indices"].append(
                        f"{_variant_label(variant)} badge-pressure top indices: {', '.join(rendered)}"
                    )
        intersection = badge_pressure.get("midday_evening_intersection") or []
        if isinstance(intersection, list):
            rendered = ", ".join(f"`{value}`" for value in intersection[:12] if str(value).strip())
            if rendered:
                out["badge_indices"].append(f"Midday/Evening badge-index intersection: {rendered}")

    aux_vtrac = arena_objects.get("aux_vtrac_pressure") or {}
    overlay_top = {}
    heatboard_top = {}
    if isinstance(aux_vtrac, Mapping):
        overlay_top = aux_vtrac.get("overlay_top") or {}
        heatboard_top = aux_vtrac.get("heatboard_top") or {}
    if not overlay_top and isinstance(aux_summary.get("vtrac"), Mapping):
        overlay_top = ((aux_summary.get("vtrac") or {}).get("overlay_top") or {})
    if not heatboard_top and isinstance(aux_summary.get("vtrac"), Mapping):
        heatboard_top = ((aux_summary.get("vtrac") or {}).get("heatboard_top") or {})
    for variant in ("Combined", "Midday", "Evening"):
        overlay_rows = overlay_top.get(variant) if isinstance(overlay_top, Mapping) else None
        heat_rows = heatboard_top.get(variant) if isinstance(heatboard_top, Mapping) else None
        if isinstance(overlay_top, Mapping) and overlay_rows is None:
            overlay_rows = overlay_top.get(variant.lower())
        if isinstance(heatboard_top, Mapping) and heat_rows is None:
            heat_rows = heatboard_top.get(variant.lower())
        out["due_vtrac"].append(
            f"{variant} due VTRAC overlay: {_fmt_vtrac_overlay_rows(overlay_rows)}"
        )
        out["due_vtrac"].append(
            f"{variant} due VTRAC heatboard: {_fmt_vtrac_heat_rows(heat_rows)}"
        )
    return out


def _context_summary(
    arena: Mapping[str, Any] | None,
    sandbox: Mapping[str, Any] | None,
    signals_bundle: Mapping[str, Any] | None = None,
) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {
        "positional": [],
        "due_doubles": [],
        "blackapple": [],
        "profit_alerts": [],
        "compound_events": [],
        "scoreboard": [],
    }
    arena_objects = _arena_objects_from_sources(arena, signals_bundle)
    if isinstance(arena_objects, Mapping):
        positional = arena_objects.get("aux_positional_pressure") or {}
        if isinstance(positional, Mapping):
            out["positional"] = [
                f"`shortlist_count={positional.get('shortlist_count', 0)}`",
                f"`shortlist_top={','.join([str((row or {}).get('canonical') or '') for row in (positional.get('shortlist_top') or [])[:6] if isinstance(row, Mapping)]) or '-'}`",
            ]
        due = arena_objects.get("aux_due_doubles_family_pressure") or {}
        if isinstance(due, Mapping):
            out["due_doubles"] = [
                f"`best_draws_since={due.get('best_draws_since_double', 0)}`",
                f"`families={','.join((due.get('top_families') or [])[:6]) or '-'}`",
            ]
        ba = arena_objects.get("aux_blackapple_context") or {}
        if isinstance(ba, Mapping):
            out["blackapple"] = [
                f"`best_status={ba.get('best_status', 'unknown')}`",
                f"`best_score={ba.get('best_score', 0)}`",
                f"`recommended={','.join((ba.get('recommended_canonicals_top') or [])[:8]) or '-'}`",
            ]
        pa = arena_objects.get("cc_profit_alert_context") or {}
        if isinstance(pa, Mapping):
            top_alerts = []
            for row in (pa.get("top_alerts") or [])[:6]:
                if not isinstance(row, Mapping):
                    continue
                label = ":".join(
                    part for part in [
                        str(row.get("variant") or "").strip(),
                        str(row.get("alert_id") or "").strip(),
                        str(row.get("canonical") or "").strip(),
                        str(row.get("suggested") or "").strip(),
                    ] if part
                )
                if label:
                    top_alerts.append(label)
            out["profit_alerts"] = [
                f"`alert_count={pa.get('alert_count', 0)}`",
                f"`top_alerts={','.join(top_alerts) or '-'}`",
            ]
        comp = arena_objects.get("cc_compound_event_context") or {}
        if isinstance(comp, Mapping):
            top_events = []
            for row in (comp.get("top_events") or [])[:4]:
                if not isinstance(row, Mapping):
                    continue
                label = ":".join(
                    part for part in [
                        str(row.get("variant") or "").strip(),
                        str(row.get("top_event") or "").strip(),
                        f"P{row.get('priority')}" if row.get("priority") is not None else "",
                    ] if part
                )
                if label:
                    top_events.append(label)
            out["compound_events"] = [
                f"`top_events={','.join(top_events) or '-'}`",
            ]
    brain2_context = (sandbox or {}).get("brain2_context") or {}
    if isinstance(brain2_context, Mapping):
        scoreboard_row = brain2_context.get("scoreboard_row") or {}
        if isinstance(scoreboard_row, Mapping):
            out["scoreboard"] = [
                f"`rank={scoreboard_row.get('score_rank', '-')}`",
                f"`role={scoreboard_row.get('role', '-')}`",
                f"`bucket={scoreboard_row.get('targeting_bucket', '-')}`",
                f"`tracker={scoreboard_row.get('tracker_posture', '-')}`",
            ]
    return out


def build_master_validation_run_report(
    *,
    results_date: str,
    state: str,
    profile: str,
    experiment_tag: str,
    predictive_sharepacks_root: Path,
    truth_sharepacks_root: Path,
) -> str:
    predictive_day_dir = predictive_sharepacks_root / results_date
    predictive_state_dir = predictive_day_dir / state
    truth_state_dir = truth_sharepacks_root / results_date / state
    truth_winners_dir = truth_state_dir / "winners" / state
    analysis_dir = predictive_state_dir / "analysis"
    history_date = (parse_iso_date(results_date) - timedelta(days=1)).isoformat()

    aggregated_json = _preferred_path(
        analysis_dir,
        "aggregated_analysis_arena",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    aggregated_md = aggregated_json.with_suffix(".md")
    sandbox_json = _preferred_path(
        analysis_dir,
        "translation_sandbox_seed",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    sandbox_md = sandbox_json.with_suffix(".md")
    candidate_universe_json = _preferred_path(
        predictive_state_dir,
        "candidate_universe",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    play_card_json = _preferred_path(
        predictive_state_dir,
        "play_card",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    play_card_md = play_card_json.with_suffix(".md")
    signals_bundle_json = _preferred_path(
        predictive_state_dir,
        "signals_bundle",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )

    aggregated = try_load_json(aggregated_json)
    sandbox = try_load_json(sandbox_json)
    candidate_universe = try_load_json(candidate_universe_json)
    play_card = try_load_json(play_card_json)
    signals_bundle = try_load_json(signals_bundle_json)
    aux_summary = try_load_json(predictive_state_dir / "aux" / state / "summary.json")

    results = parse_results(date=results_date, state=state)
    winners_html = list_artifacts(truth_winners_dir, "*.html")
    winners_json = list_artifacts(truth_winners_dir, "*.json")

    arena_synthesis = (aggregated or {}).get("arena_synthesis") or {}
    context_sections = _context_summary(aggregated, sandbox, signals_bundle)
    aux_inventory_sections = _aux_inventory_sections(
        aux_summary if isinstance(aux_summary, Mapping) else None,
        aggregated if isinstance(aggregated, Mapping) else None,
        signals_bundle if isinstance(signals_bundle, Mapping) else None,
    )

    dominant_canonicals = _ranked_values(arena_synthesis.get("dominant_canonicals"))
    dominant_families = _ranked_values(arena_synthesis.get("dominant_families"))
    dominant_vtrac = _ranked_values(arena_synthesis.get("dominant_vtrac_indices"))
    reinforced_canonicals = _ranked_values(arena_synthesis.get("context_reinforced_canonicals"))
    context_only_pressure = _ranked_values(arena_synthesis.get("context_only_pressure"))
    watchlist_summary = _watchlist_summary(arena_synthesis.get("vtrac_literal_watchlist"))
    state_regime = _state_regime_summary(arena_synthesis.get("state_regime"))
    survivor_summary = _survivor_summary(arena_synthesis.get("stable_survivor_context"))
    r_consensus_summary = _r_consensus_summary(arena_synthesis.get("r_consensus_context"))

    metadata = (aggregated or {}).get("metadata") or {}
    if isinstance(metadata, Mapping) and metadata.get("history_date"):
        history_date = str(metadata.get("history_date"))

    lines: list[str] = []
    lines.append(f"# Analysis Arena Master Validation Run Report — {state} — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- State-level post-results review packet for the Analysis Arena branch.")
    lines.append("- Locks Part A truth inputs, points Parts B-E at the predictive raw tool evidence, and auto-captures Parts F/G/H from the live arena/runtime objects.")
    lines.append("- This report is an arena-native working shell. It is not the old summary-driven validation scaffold.")
    lines.append("")
    lines.append("Template / SSOT anchors")
    lines.append(f"- Per-state Master Validation template: {_fmt_path(STATE_TEMPLATE_PATH)}")
    lines.append(f"- Aggregated arena contract: {_fmt_path(ARENA_CONTRACT_PATH)}")
    lines.append(f"- String-tool arena feed: {_fmt_path(STRING_FEED_PATH)}")
    lines.append(f"- Context-tool arena feed: {_fmt_path(CONTEXT_FEED_PATH)}")
    lines.append(f"- Translation Sandbox companion: {_fmt_path(TRANSLATION_TEMPLATE_PATH)}")
    lines.append(f"- Brain 2 operating template: {_fmt_path(BRAIN2_TEMPLATE_PATH)}")
    lines.append(f"- Brain 2 Master Validation template: {_fmt_path(BRAIN2_MV_TEMPLATE_PATH)}")
    lines.append(f"- Arena system map: {_fmt_path(SYSTEM_MAP_PATH)}")
    lines.append("")
    lines.append("Scope")
    lines.append(f"- Results date `D`: `{results_date}`")
    lines.append(f"- History date `H`: `{history_date}`")
    lines.append(f"- State: `{state}`")
    lines.append(f"- Predictive sharepack root: `{safe_rel(predictive_sharepacks_root)}`")
    lines.append(f"- Predictive state dir: `{safe_rel(predictive_state_dir)}`")
    lines.append(f"- Truth/frozen sharepack root: `{safe_rel(truth_sharepacks_root)}`")
    lines.append(f"- Truth state dir: `{safe_rel(truth_state_dir)}`")
    lines.append(f"- Profile: `{profile}`")
    lines.append(f"- Experiment tag: `{experiment_tag or 'untagged'}`")
    lines.append("")
    lines.append("## Part A — Winners Environment Lens")
    lines.append("")
    lines.append("### A0. File Lock And Truth Inputs")
    lines.append(f"- Results file: {_fmt_path(REPO_ROOT / 'data' / 'results' / f'{results_date}.txt')}")
    lines.append(f"- Midday winner: literal `{results.get('midday') or '-'}` | canonical `{canonicalize(results.get('midday') or '') or '-'}`")
    lines.append(f"- Evening winner: literal `{results.get('evening') or '-'}` | canonical `{canonicalize(results.get('evening') or '') or '-'}`")
    lines.append(f"- Truth winners dir: {_fmt_path(truth_winners_dir)}")
    lines.append(f"- Winners HTML: {_fmt_items([safe_rel(path) for path in winners_html], empty='_(none found)_')}")
    lines.append(f"- Winners JSON: {_fmt_items([safe_rel(path) for path in winners_json], empty='_(none found)_')}")
    lines.append("")
    lines.append("### A1-A7. Analyst Read")
    lines.append("- Winning pattern formation: `...`")
    lines.append("- Variant behavior / environment class: `...`")
    lines.append("- Winner structure class: `...`")
    lines.append("- Progression / survivor read: `...`")
    lines.append("- VTRAC winner read: `...`")
    lines.append("- Pre-system predictive thesis: `...`")
    lines.append("- Part A handoff: `a strong predictive system needed to preserve ...`")
    lines.append("")
    lines.append("## Parts B-E — Raw Tool Review Surfaces")
    lines.append("")
    lines.append("These sections remain governed by the arena-era template. This report locks the predictive-side files that should be reviewed for Parts B-E instead of trying to restage the old summary-only shell.")
    lines.append("")
    lines.append("### Stable")
    lines.append(f"- Scores CSV: {_fmt_path(predictive_state_dir / 'stable' / state / f'{state}_stable_patterns_scores.csv')}")
    lines.append(f"- Families CSV: {_fmt_path(predictive_state_dir / 'stable' / state / f'{state}_stable_patterns_families.csv')}")
    lines.append(f"- Compound CSV: {_fmt_path(predictive_state_dir / 'stable' / state / f'{state}_stable_patterns_compound.csv')}")
    lines.append(f"- Metrics JSON: {_fmt_path(predictive_state_dir / 'stable' / state / f'{state}_metrics.json')}")
    lines.append(f"- HTML report: {_fmt_path(predictive_state_dir / 'stable' / state / f'{state}_stable_patterns_report.html')}")
    lines.append("")
    lines.append("### Digit Reduction")
    lines.append(f"- Scores CSV: {_fmt_path(predictive_state_dir / 'digit_reduction' / state / f'{state}_digit_reduction_scores.csv')}")
    lines.append(f"- Report HTML: {_fmt_path(predictive_state_dir / 'digit_reduction' / state / f'{state}_digit_reduction_report.html')}")
    lines.append(f"- Stacked report HTML: {_fmt_path(predictive_state_dir / 'digit_reduction' / state / f'{state}_digit_reduction_report_stacked.html')}")
    lines.append("")
    lines.append("### VTRAC")
    lines.append(f"- Enhanced JSON: {_fmt_items([safe_rel(path) for path in list_artifacts(predictive_state_dir / 'vtrac' / state, f'{state}_vtrac_enhanced_*.json')], empty='_(none found)_')}")
    lines.append(f"- Validation report JSON: {_fmt_path(predictive_state_dir / 'vtrac' / state / 'validation_report.json')}")
    lines.append(f"- Validation report MD: {_fmt_path(predictive_state_dir / 'vtrac' / state / 'validation_report.md')}")
    lines.append("")
    lines.append("### Hot Zones")
    lines.append(f"- Top lanes CSV: {_fmt_path(predictive_state_dir / 'hot_zones' / state / f'{state}_hot_zones_top_lanes.csv')}")
    lines.append(f"- Per-lane CSV: {_fmt_path(predictive_state_dir / 'hot_zones' / state / f'{state}_hot_zones_per_lane.csv')}")
    lines.append(f"- Meta JSON: {_fmt_path(predictive_state_dir / 'hot_zones' / state / f'{state}_hot_zones_meta.json')}")
    lines.append(f"- Winner map JSON: {_fmt_items([safe_rel(path) for path in list_artifacts(predictive_state_dir / 'hot_zones' / state, '*hot_zones_winner_map.json')], empty='_(none found)_')}")
    lines.append("")
    lines.append("## Part F — Aggregated Analysis Arena")
    lines.append("")
    lines.append("### F0. Arena File Lock And Review Surface")
    lines.append(f"- Aggregated arena JSON: {_fmt_path(aggregated_json)}")
    lines.append(f"- Aggregated arena MD: {_fmt_path(aggregated_md)}")
    lines.append(f"- Signals bundle JSON: {_fmt_path(signals_bundle_json)}")
    lines.append(f"- Review links available: `{bool((aggregated or {}).get('review_links'))}`")
    lines.append("")
    lines.append("### F1-F9. Auto-captured arena snapshot")
    lines.append(f"- Dominant canonicals: {_fmt_items(dominant_canonicals)}")
    lines.append(f"- Dominant families: {_fmt_items(dominant_families)}")
    lines.append(f"- Dominant VTRAC indices: {_fmt_items(dominant_vtrac)}")
    lines.append(f"- Context-reinforced canonicals: {_fmt_items(reinforced_canonicals)}")
    lines.append(f"- Context-only pressure: {_fmt_items(context_only_pressure)}")
    lines.append(f"- State regime: {_fmt_items(state_regime)}")
    lines.append(f"- VTRAC literal watchlist: {_fmt_items(watchlist_summary)}")
    lines.append(f"- Stable survivor context: {_fmt_items(survivor_summary)}")
    lines.append(f"- R-Consensus context: {_fmt_items(r_consensus_summary)}")
    lines.append("- Arena truth alignment summary: `...`")
    lines.append("- Arena added value read: `...`")
    lines.append("- Arena judgment / handoff: `...`")
    lines.append("")
    lines.append("## Part G — Context / Aux / Control Center Audit")
    lines.append("")
    lines.append("### G0. Context file lock")
    lines.append(f"- Aux summary JSON: {_fmt_path(predictive_state_dir / 'aux' / state / 'summary.json')}")
    lines.append(f"- Aux summary MD: {_fmt_path(predictive_state_dir / 'aux' / state / 'summary.md')}")
    lines.append(f"- Control Center dir: {_fmt_path(predictive_day_dir / 'control_center')}")
    lines.append("")
    lines.append("### G1-G10. Auto-captured context snapshot")
    lines.append(f"- Positional pressure: {_fmt_items(context_sections['positional'])}")
    lines.append(f"- Due doubles / mirror-double family pressure: {_fmt_items(context_sections['due_doubles'])}")
    lines.append(f"- Blackapple context: {_fmt_items(context_sections['blackapple'])}")
    lines.append(f"- Profit alerts: {_fmt_items(context_sections['profit_alerts'])}")
    lines.append(f"- Compound events: {_fmt_items(context_sections['compound_events'])}")
    lines.append(f"- Scoreboard carry-through: {_fmt_items(context_sections['scoreboard'])}")
    if isinstance(aux_summary, Mapping):
        lines.append(f"- Aux draw sources present: `{bool((aux_summary.get('draw_sources') or {}))}`")
    lines.append("")
    lines.append("### G1a. Explicit Aux badge inventory")
    for bullet in aux_inventory_sections["badge_pairs"] or ["_none_"]:
        lines.append(f"- {bullet}")
    for bullet in aux_inventory_sections["badge_combos"] or ["_none_"]:
        lines.append(f"- {bullet}")
    for bullet in aux_inventory_sections["badge_indices"] or ["_none_"]:
        lines.append(f"- {bullet}")
    lines.append("")
    lines.append("### G1b. Explicit due VTRAC inventory")
    for bullet in aux_inventory_sections["due_vtrac"] or ["_none_"]:
        lines.append(f"- {bullet}")
    lines.append("- Context reinforcement vs context-only pressure: `...`")
    lines.append("- Policy relationship / handoff: `...`")
    lines.append("")
    lines.append("## Part H — Translation Sandbox / Downstream Control Arm")
    lines.append("")
    lines.append("### H0. File lock")
    lines.append(f"- Translation sandbox JSON: {_fmt_path(sandbox_json)}")
    lines.append(f"- Translation sandbox MD: {_fmt_path(sandbox_md)}")
    lines.append(f"- Candidate Universe JSON: {_fmt_path(candidate_universe_json)}")
    lines.append(f"- Play Card JSON: {_fmt_path(play_card_json)}")
    lines.append(f"- Play Card MD: {_fmt_path(play_card_md)}")
    lines.append("")
    lines.append("### H1. Auto-captured control-arm snapshot")
    lines.append(f"- Candidate Universe summary: {_candidate_universe_summary(candidate_universe if isinstance(candidate_universe, Mapping) else None)}")
    lines.append(f"- Play Card summary: {_play_card_summary(play_card if isinstance(play_card, Mapping) else None)}")
    if isinstance(sandbox, Mapping):
        brain2_context = sandbox.get("brain2_context") or {}
        sandbox_hyp = sandbox.get("sandbox_hypotheses") or {}
        lines.append(f"- Translation Sandbox positional shortlist top: {_fmt_items([str((row or {}).get('canonical') or '') for row in (brain2_context.get('positional_shortlist_top') or [])])}")
        lines.append(f"- Translation Sandbox BA canonicals: {_fmt_items(brain2_context.get('blackapple_recommended_canonicals') or [])}")
        lines.append(f"- Translation Sandbox profit canonicals: {_fmt_items(brain2_context.get('profit_alert_implied_canonicals') or [])}")
        boxed_seed = [str((row or {}).get('value') or '') for row in (sandbox_hyp.get('diagnostic_boxed_seed') or [])]
        straight_seed = [str((row or {}).get('value') or '') for row in (sandbox_hyp.get('diagnostic_straight_seed') or [])]
        vt_seed = [str((row or {}).get('value') or '') for row in (sandbox_hyp.get('diagnostic_vt_box_seed') or [])]
        lines.append(f"- Diagnostic boxed seed: {_fmt_items(boxed_seed)}")
        lines.append(f"- Diagnostic straight seed: {_fmt_items(straight_seed)}")
        lines.append(f"- Diagnostic VT-box seed: {_fmt_items(vt_seed)}")
    lines.append("- Translation-learning capture: `...`")
    lines.append("- Control-arm comparison / bounded handoff: `...`")
    lines.append("")
    lines.append("## Part I — Final State-Level Learning")
    lines.append("")
    lines.append("- Strongest truth-side clue: `...`")
    lines.append("- Strongest Brain 1 preservation win: `...`")
    lines.append("- Strongest context/Brain 2 handoff clue: `...`")
    lines.append("- Strongest conversion/control-arm gap: `...`")
    lines.append("- Fix-now vs fix-later: `...`")
    lines.append("- Translation Sandbox companion needed?: `yes/no`")
    lines.append("- Brain 2 handoff: `...`")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create an arena-native per-state Master Validation report.")
    ap.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD)")
    ap.add_argument("--state", required=True, help="State key (for example NewYork4)")
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument(
        "--predictive-sharepacks-root",
        default="sharepacks/_predictive",
        help="Predictive sharepacks root (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--truth-sharepacks-root",
        default="sharepacks",
        help="Frozen/results sharepacks root for winners truth (default: sharepacks)",
    )
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: RUNS_2/<D>__<STATE>.md)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite an existing report.")
    return ap.parse_args()


def main() -> None:
    args = _parse_args()
    results_date = parse_iso_date(args.date).isoformat()
    predictive_sharepacks_root = Path(args.predictive_sharepacks_root)
    if not predictive_sharepacks_root.is_absolute():
        predictive_sharepacks_root = (REPO_ROOT / predictive_sharepacks_root).resolve()
    truth_sharepacks_root = Path(args.truth_sharepacks_root)
    if not truth_sharepacks_root.is_absolute():
        truth_sharepacks_root = (REPO_ROOT / truth_sharepacks_root).resolve()

    default_out = RUNS2_DIR / f"{results_date}__{args.state}.md"
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Run report already exists: {safe_rel(out_path)} (use --force to overwrite).")

    report = build_master_validation_run_report(
        results_date=results_date,
        state=args.state,
        profile=str(args.profile or "tool_only").strip(),
        experiment_tag=normalize_tag(args.experiment_tag),
        predictive_sharepacks_root=predictive_sharepacks_root,
        truth_sharepacks_root=truth_sharepacks_root,
    )
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {safe_rel(out_path)}")


if __name__ == "__main__":
    main()
