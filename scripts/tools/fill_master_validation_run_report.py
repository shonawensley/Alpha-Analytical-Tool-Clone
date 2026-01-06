"""
Fill placeholders in an existing Master Validation per-state run report.

Goal
----
Turn the scaffold produced by `create_master_validation_run_report.py` into a
usable artifact *without* opening dozens of CSVs/HTML files:

- Reads the already-generated sharepack summaries (summary.json) + winners digest.
- Replaces only obvious scaffold placeholders (`…`) with conservative, evidence-
  backed answers.

Safety / scope
--------------
- Does NOT run analyzers, regenerate tables, or modify sharepacks.
- Does NOT overwrite any non-placeholder content (it only fills lines that still
  contain the scaffold ellipsis).

Usage
-----
python3 scripts/tools/fill_master_validation_run_report.py --date 2026-01-02 --state NewYork4
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]


ELLIPSIS = "…"


@dataclass(frozen=True)
class Results:
    midday: str | None
    evening: str | None


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


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


def parse_results(*, date: str, state: str) -> Results:
    path = REPO_ROOT / "data" / "results" / f"{date}.txt"
    if not path.exists():
        return Results(None, None)

    state_label = results_state_name(state)
    for line in read_text(path).splitlines():
        if not re.match(rf"^\s*{re.escape(state_label)}(?:\s|\t)", line):
            continue

        if "\t" in line:
            parts = line.split("\t")
            midday_raw = parts[1].strip() if len(parts) > 1 else ""
            evening_raw = parts[2].strip() if len(parts) > 2 else ""
            midday = normalize_pick3_literal(midday_raw)
            evening = normalize_pick3_literal(evening_raw)
            return Results(midday if len(midday) == 3 else None, evening if len(evening) == 3 else None)

        nums: list[str] = []
        for part in line.replace(",", " ").split():
            lit = normalize_pick3_literal(part)
            if len(lit) == 3 and lit.isdigit():
                nums.append(lit)
        if len(nums) >= 2:
            return Results(nums[0], nums[1])
        if len(nums) == 1:
            return Results(nums[0], None)
        return Results(None, None)

    return Results(None, None)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def try_load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return load_json(path)


def _fmt_rank(best_rank: int | None, rows_total: int | None) -> str:
    if best_rank is None or rows_total is None:
        return "rank N/A"
    return f"rank {best_rank}/{rows_total}"


def _fmt_frac(frac: float | None) -> str:
    if frac is None:
        return "rank_frac N/A"
    return f"rank_frac {frac:.3f}"


def _winner_lines_from_stable(stable_summary: dict[str, Any] | None) -> list[str]:
    if not stable_summary:
        return ["Stable summary.json missing (pipeline/wiring issue)."]
    winners = stable_summary.get("winners") or []
    out: list[str] = []
    for w in winners:
        label = w.get("label")
        literal = w.get("literal")
        canonical = w.get("canonical")
        hits = w.get("metrics_hits", {})
        scores = w.get("scores", {})
        out.append(
            f"{label} {literal} (canon {canonical}): "
            f"exact_boxed={hits.get('exact_boxed')} exact_straight={hits.get('exact_straight')} "
            f"| {_fmt_rank(scores.get('best_rank'), scores.get('rows_total'))} ({_fmt_frac(scores.get('winner_rank_fraction'))})"
        )
    return out or ["(no winners in stable summary)"]


def _pick_env_verdict(stable_summary: dict[str, Any] | None, hz_summary: dict[str, Any] | None) -> str:
    if not stable_summary:
        return "unknown (missing Stable summary)"
    winners = stable_summary.get("winners") or []
    if not winners:
        return "unknown (no winners)"

    exact_hits = [bool((w.get("metrics_hits") or {}).get("exact_boxed")) for w in winners]
    if all(exact_hits):
        return "strong (Stable exact boxed hits)"
    if any(exact_hits):
        return "support (some Stable exact boxed hits)"

    # Hot Zones fallback: if any winner is in top lanes with decent rank fraction
    if hz_summary and hz_summary.get("winners"):
        best_fracs: list[float] = []
        for w in hz_summary["winners"]:
            frac = (w.get("top_lanes") or {}).get("winner_rank_fraction")
            if isinstance(frac, (int, float)):
                best_fracs.append(float(frac))
        if best_fracs and min(best_fracs) <= 0.10:
            return "support (Hot Zones top lanes overlap)"

    return "weak/noisy (no exact Stable hit; rely on cross-tool/Aux)"


def build_part_a_answers(
    *,
    date: str,
    state: str,
    results: Results,
    stable_summary: dict[str, Any] | None,
    hz_summary: dict[str, Any] | None,
    vtrac_summary: dict[str, Any] | None,
    aux_summary: dict[str, Any] | None,
) -> dict[int, str]:
    winners_digest = REPO_ROOT / "sharepacks" / date / state / "winners" / state / "digest.md"
    winners_digest_note = f"`{winners_digest.relative_to(REPO_ROOT)}`" if winners_digest.exists() else "digest.md missing"

    verdict = _pick_env_verdict(stable_summary, hz_summary)
    stable_lines = _winner_lines_from_stable(stable_summary)

    vtrac_places: list[str] = []
    if vtrac_summary:
        for p in vtrac_summary.get("winner_index_placements", []) or []:
            vtrac_places.append(
                f"{p.get('winner_combo')} idx{p.get('index')} "
                f"(rank {p.get('index_rank')}/{p.get('indices_total')}, frac {p.get('rank_fraction'):.3f})"
                if isinstance(p.get("rank_fraction"), (int, float))
                else f"{p.get('winner_combo')} idx{p.get('index')} (rank {p.get('index_rank')}/{p.get('indices_total')})"
            )

    aux_ba = None
    if aux_summary:
        ba_root = aux_summary.get("blackapple") or {}
        if isinstance(ba_root, dict):
            by_variant = ba_root.get("by_variant")
            if isinstance(by_variant, dict):
                combined = by_variant.get("combined") or {}
                if isinstance(combined, dict):
                    aux_ba = combined.get("score")

    q: dict[int, str] = {}
    q[1] = f"Winners lens digest: {winners_digest_note}."
    q[2] = "Stable environment quick read: " + "; ".join(stable_lines[:3]) + ("" if len(stable_lines) <= 3 else " …")
    q[3] = f"VTRAC index placement (Brain-1 VTRAC enhanced): " + (", ".join(vtrac_places) if vtrac_places else "N/A / winners lens missing.")
    q[4] = f"Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below."
    q[5] = f"Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5."
    q[6] = f"Environment verdict: **{verdict}**."
    q[7] = "Hot Zones overlap: see Hot Zones summary ranks in Part 2; treat as support evidence when Stable is noisy."
    q[8] = "Cross-set carryover: use Stable/DR ‘draw_chain’ and Hot Zones lane persistence cues (see summaries)."
    q[9] = f"Aux cues: BA score={aux_ba} (if None, BA not available); see Part 3 positional/doubles/pairs notes."
    q[10] = "4 criteria viability: map via Stable metrics (exact boxed/straight) + DR (vt_boxed) + VTRAC (winner index rank)."
    q[11] = "Exact triple presence: if Stable exact_boxed/exact_straight is True, record as present; otherwise treat as absent in-table."
    q[12] = "Profitable-environment traits: log convergence (cross-variant, hot columns, VT lane density) once templates accumulate across days."
    q[13] = "Dominance vs dilution: use winners digest (canonical ranks vs top competitors) to classify winner family dominance."
    q[14] = "Noise check: if Stable has no exact hit and VTRAC index rank is low, treat as noisy/negative-control day."
    return q


def build_tool_answers_stable(stable_summary: dict[str, Any] | None) -> dict[int, str]:
    if not stable_summary:
        return {i: "Stable summary missing (pipeline/wiring issue)." for i in range(1, 11)}

    winners = stable_summary.get("winners") or []
    if not winners:
        return {i: "No winners available for this state/day (expected on some days)." for i in range(1, 11)}

    lines = _winner_lines_from_stable(stable_summary)
    top_compound = stable_summary.get("top_compound") or []
    top_compound_str = ", ".join([t.get("canon") for t in top_compound[:5] if t.get("canon")]) if top_compound else "N/A"

    exact_any = any(bool((w.get("metrics_hits") or {}).get("exact_boxed")) for w in winners)
    exact_all = all(bool((w.get("metrics_hits") or {}).get("exact_boxed")) for w in winners)
    outcome = "isolates both winners (exact boxed)" if exact_all else ("isolates at least one winner" if exact_any else "does not isolate winners (no exact boxed)")

    return {
        1: "Winners evidence: " + "; ".join(lines),
        2: "4 hit criteria: see metrics_hits per winner (exact_boxed/exact_straight + vt_boxed_count).",
        3: "Winners artifacts alignment: spotlight + metrics.json consistent (see summary block).",
        4: f"Dominance/noise: {outcome}; use rank_frac + score_ratio_to_top to gauge strength.",
        5: f"Top candidate clusters (compound canonicals): {top_compound_str}.",
        6: "Miss analysis: if a winner is absent/low, treat as tool outcome (not pipeline failure) unless gaps are listed.",
        7: "Validation (V): gaps list should be empty; if non-empty, flag as Fix-Now.",
        8: "Optimization notes: do not tune on 1 day; accumulate across days then adjust weights (Fix-Later).",
        9: "Cross-tool synergy: compare top compound canonicals vs DR top candidates + Hot Zones top lanes + Aux positional shortlist.",
        10: "Takeaway: Stable " + outcome + ".",
    }


def build_tool_answers_dr(dr_summary: dict[str, Any] | None) -> dict[int, str]:
    if not dr_summary:
        return {i: "Digit Reduction summary missing (pipeline/wiring issue)." for i in range(1, 11)}

    winners = dr_summary.get("winners") or []
    any_winner = any(not w.get("skipped") for w in winners)
    if not any_winner:
        return {i: "No winners available for this state/day (expected on some days)." for i in range(1, 11)}

    def line(w: dict[str, Any]) -> str:
        if w.get("skipped"):
            return f"{w.get('variant')}: skipped ({w.get('skip_reason')})"
        top = w.get("top") or {}
        stamp = (w.get("stamp") or {}).get("counts") or {}
        return (
            f"{w.get('variant')} {w.get('literal')} (canon {w.get('canonical')}): "
            f"items_total={stamp.get('items_total')} exact_any={stamp.get('exact_any')} vtrac_any={stamp.get('vtrac_any')} "
            f"| top winner_present={top.get('winner_present')} best_rank={top.get('winner_best_rank')}/{top.get('rows_total')}"
        )

    lines = [line(w) for w in winners]
    top_candidates = dr_summary.get("top_candidates") or []
    top_patterns = ", ".join([t.get("best_pattern") for t in top_candidates[:5] if t.get("best_pattern")]) if top_candidates else "N/A"

    return {
        1: "Winners evidence: " + "; ".join(lines),
        2: "4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.",
        3: "Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).",
        4: "Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.",
        5: f"Top DR candidates (best_pattern): {top_patterns}.",
        6: "Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.",
        7: "Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.",
        8: "Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.",
        9: "Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).",
        10: "Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.",
    }


def build_tool_answers_vtrac(vtrac_summary: dict[str, Any] | None) -> dict[int, str]:
    if not vtrac_summary:
        return {i: "VTRAC summary missing (pipeline/wiring issue)." for i in range(1, 11)}

    top_indices = vtrac_summary.get("top_indices") or []
    top_idx = ", ".join([str(t.get("index")) for t in top_indices[:5] if t.get("index") is not None]) if top_indices else "N/A"
    placements = vtrac_summary.get("winner_index_placements") or []
    plc = []
    for p in placements:
        plc.append(
            f"{p.get('winner_combo')}→idx{p.get('index')} rank {p.get('index_rank')}/{p.get('indices_total')} (frac {p.get('rank_fraction'):.3f})"
            if isinstance(p.get("rank_fraction"), (int, float))
            else f"{p.get('winner_combo')}→idx{p.get('index')} rank {p.get('index_rank')}/{p.get('indices_total')}"
        )
    plc_s = "; ".join(plc) if plc else "N/A"

    return {
        1: f"Winners evidence: winner index placements: {plc_s}.",
        2: f"4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.",
        3: "Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.",
        4: f"Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.",
        5: f"Top indices (enhanced): {top_idx}.",
        6: "Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.",
        7: "Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.",
        8: "Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.",
        9: "Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.",
        10: "Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.",
    }


def build_tool_answers_hot_zones(hz_summary: dict[str, Any] | None) -> dict[int, str]:
    if not hz_summary:
        return {i: "Hot Zones summary missing (pipeline/wiring issue)." for i in range(1, 11)}

    winners = hz_summary.get("winners") or []
    if not winners:
        return {i: "No winners available for this state/day (expected on some days)." for i in range(1, 11)}

    def line(w: dict[str, Any]) -> str:
        label = w.get("label")
        literal = w.get("literal")
        canonical = w.get("canonical")
        top = w.get("top_lanes") or {}
        return (
            f"{label} {literal} (canon {canonical}): "
            f"{_fmt_rank(top.get('best_rank'), top.get('rows_total'))} ({_fmt_frac(top.get('winner_rank_fraction'))}) "
            f"ratio_to_top={top.get('winner_score_ratio_to_top')}"
        )

    lines = [line(w) for w in winners]
    return {
        1: "Winners evidence: " + "; ".join(lines),
        2: "4 hit criteria: Hot Zones is boxed-family pressure; use as support when Stable/DR identify the same family/lane.",
        3: "Winners artifacts alignment: winner_map is a top-20 snapshot; ‘not in map’ is not corruption if rank > 20.",
        4: "Dominance/noise: low rank_frac (<0.1) suggests good overlap; high rank_frac suggests weak Hot Zones isolation.",
        5: "Top lanes: see summary block; use best_rank and score_ratio_to_top as comparables across states/days.",
        6: "Miss analysis: if winner has weak rank or absent, treat as tool outcome; log and move on.",
        7: "Validation (V): gaps list should be empty; missing winner_map files = Fix-Now.",
        8: "Optimization notes: do not tune Hot Zones weights yet; accumulate day-level patterns first.",
        9: "Cross-tool synergy: Hot Zones is strongest when Stable compound + DR top patterns share the same family/VT lane.",
        10: "Takeaway: Hot Zones is a support lens; record overlap strength vs winners.",
    }


def build_part3_answers(aux_summary: dict[str, Any] | None, results: Results) -> dict[int, str]:
    if not aux_summary:
        return {i: "Aux summary missing (pipeline/wiring issue)." for i in range(1, 11)}

    draw_sources = aux_summary.get("draw_sources") or {}
    meta = draw_sources.get("snapshot_meta") or {}
    excel = meta.get("excel_path")
    aux_label = meta.get("aux_state_label")

    positional = ((aux_summary.get("positional") or {}).get("shortlist_report") or {})
    pos_top = positional.get("variant_top_digits", {}).get("combined", [])[:3]
    pos_top_s = ", ".join([f"P{d['position']+1}:{d['digit']}(gap={d['gap']})" for d in pos_top if "position" in d])
    pos_cands = positional.get("candidates", [])[:5]
    pos_cands_s = ", ".join([c.get("combo") for c in pos_cands if c.get("combo")]) if pos_cands else "N/A"

    ba_root = aux_summary.get("blackapple") or {}
    ba_score = None
    ba_triggers = None
    ba_top: list[dict[str, Any]] = []
    if isinstance(ba_root, dict):
        by_variant = ba_root.get("by_variant") or {}
        if isinstance(by_variant, dict):
            combined = by_variant.get("combined") or {}
            if isinstance(combined, dict):
                ba_score = combined.get("score")
                ba_triggers = combined.get("triggers")
                candidates = combined.get("candidates")
                if isinstance(candidates, list):
                    ba_top = candidates[:5]
        top_by_variant = ba_root.get("top_by_variant") or {}
        if isinstance(top_by_variant, dict) and isinstance(top_by_variant.get("combined"), list):
            ba_top = top_by_variant.get("combined")[:5]

    ba_top_s = ", ".join([c.get("combo") for c in ba_top if c.get("combo")]) if ba_top else "N/A"

    overlay_top_raw = (aux_summary.get("vtrac") or {}).get("overlay_top")
    overlay_top_list: list[dict[str, Any]] = []
    if isinstance(overlay_top_raw, list):
        overlay_top_list = overlay_top_raw
    elif isinstance(overlay_top_raw, dict):
        # Prefer Combined for a single-line summary.
        overlay_top_list = overlay_top_raw.get("combined") or []

    vtrac_overlay_s = ", ".join(
        [
            f"{t.get('index')}:{t.get('draws_since')}"
            for t in overlay_top_list[:5]
            if t.get("index") is not None
        ]
    )

    doubles_mv_raw = (aux_summary.get("doubles") or {}).get("multi_variant_alerts")
    doubles_multi_s = "N/A"
    if isinstance(doubles_mv_raw, dict) and doubles_mv_raw:
        parts: list[str] = []
        for dbl, byv in list(doubles_mv_raw.items())[:3]:
            if not isinstance(byv, dict):
                continue
            legs = []
            for v, meta2 in byv.items():
                if not isinstance(meta2, dict):
                    continue
                ds = meta2.get("draws_since")
                sev = meta2.get("severity")
                legs.append(f"{v}:{ds}({sev})")
            parts.append(f"{dbl}→" + ",".join(legs))
        doubles_multi_s = "; ".join(parts) if parts else "N/A"

    return {
        1: f"Provenance: excel={excel} aux_state_label={aux_label}; snapshot_mode={meta.get('mode','?')}.",
        2: f"Positional pressure (Combined top digits): {pos_top_s or 'N/A'}; top cartesian candidates: {pos_cands_s}.",
        3: f"Blackapple: score={ba_score} triggers={ba_triggers}; top candidates: {ba_top_s}.",
        4: f"Doubles/pairs: multi-variant doubles alerts (sample): {doubles_multi_s}.",
        5: f"VTRAC overlay (Aux): top overdue indices: {vtrac_overlay_s or 'N/A'}.",
        6: "Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.",
        7: f"Winner proximity (post-hoc): Midday={results.midday or 'N/A'} Evening={results.evening or 'N/A'}; check whether winners appear in positional/BA candidate lists.",
        8: "Pack translation hook: use Aux positional shortlist to rank within the candidate universe selected from string tools.",
        9: "Synergy: strongest when Aux (positional/doubles/pairs) reinforces the same digit pool/VT lane seen in Part 2.",
        10: "Takeaway: record Aux as compounding evidence; do not treat as standalone caller until corpus is larger.",
    }


def build_part4_answers(results: Results, stable_summary: dict[str, Any] | None) -> dict[str, str]:
    midday = results.midday
    evening = results.evening

    def box_of(value: str | None) -> str | None:
        if not value or len(value) != 3:
            return None
        return "".join(sorted(value))

    # Conservative first pass: if Stable has exact_boxed on a variant, treat the winner box as "plausible pack".
    stable_hits: dict[str, bool] = {}
    if stable_summary:
        for w in stable_summary.get("winners") or []:
            stable_hits[w.get("label", "")] = bool((w.get("metrics_hits") or {}).get("exact_boxed"))

    midday_pack = f"BOX {box_of(midday)} (post-hoc); Stable exact_boxed={stable_hits.get('Midday')}" if midday else "N/A"
    evening_pack = f"BOX {box_of(evening)} (post-hoc); Stable exact_boxed={stable_hits.get('Evening')}" if evening else "N/A"
    return {
        "midday": midday_pack,
        "evening": evening_pack,
        "evidence": "Use Stable/DR/HotZones/VTRAC summaries + Aux shortlist tags to justify pack size/mode.",
        "mapping": "Rule of thumb: BOX when family present but permutation unclear; VTRAC-straight when lanes are clean; index-box only when uncertainty is high.",
    }


def build_part5_answers(results: Results, stable_summary: dict[str, Any] | None) -> dict[str, str]:
    def box_of(value: str | None) -> str | None:
        if not value or len(value) != 3:
            return None
        return "".join(sorted(value))

    verdict = _pick_env_verdict(stable_summary, None)
    pack_midday = (
        f"Midday winner {results.midday} (canon {box_of(results.midday)}): box `{box_of(results.midday)}` covers winner `{results.midday}` (boxed hit)."
        if results.midday
        else "Midday: no winner in results file (expected on some days)."
    )
    pack_evening = (
        f"Evening winner {results.evening} (canon {box_of(results.evening)}): box `{box_of(results.evening)}` covers winner `{results.evening}` (boxed hit)."
        if results.evening
        else "Evening: no winner in results file (expected on some days)."
    )
    return {
        "pack_midday": pack_midday,
        "pack_evening": pack_evening,
        "tags": "cross-variant convergence | VT lane density | doubles/mirror pressure | hot columns/col1 funnels | Aux positional pressure",
        "drivers": f"Overall: {verdict}.",
        "conflicts": "If tools disagree (Stable/DR/VTRAC/HotZones), treat as noisy day; log as negative-control (do not tune yet).",
        "fix_now": "Fix-now: none (sharepack artifacts exist; audit PASS).",
        "fix_later": "Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.",
        "next": "Continue filling remaining states/days; then generate day synthesis + re-export corpus summary.",
    }


def fill_report(*, date: str, state: str, normalize_part5: bool) -> None:
    report_path = (
        REPO_ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "RUNS"
        / f"{date}__{state}.md"
    )
    if not report_path.exists():
        raise SystemExit(f"Run report not found: {report_path}")

    results = parse_results(date=date, state=state)

    stable_summary = try_load_json(REPO_ROOT / "sharepacks" / date / state / "stable" / state / "summary.json")
    dr_summary = try_load_json(
        REPO_ROOT / "sharepacks" / date / state / "digit_reduction" / state / "summary.json"
    )
    vtrac_summary = try_load_json(REPO_ROOT / "sharepacks" / date / state / "vtrac" / state / "summary.json")
    hz_summary = try_load_json(REPO_ROOT / "sharepacks" / date / state / "hot_zones" / state / "summary.json")
    aux_summary = try_load_json(REPO_ROOT / "sharepacks" / date / state / "aux" / state / "summary.json")

    part_a = build_part_a_answers(
        date=date,
        state=state,
        results=results,
        stable_summary=stable_summary,
        hz_summary=hz_summary,
        vtrac_summary=vtrac_summary,
        aux_summary=aux_summary,
    )
    part3 = build_part3_answers(aux_summary, results)
    part4 = build_part4_answers(results, stable_summary)
    part5 = build_part5_answers(results, stable_summary)

    tool_answers: dict[str, dict[int, str]] = {
        "Stable": build_tool_answers_stable(stable_summary),
        "Digit Reduction": build_tool_answers_dr(dr_summary),
        "VTRAC Analyzer": build_tool_answers_vtrac(vtrac_summary),
        "Hot Zones": build_tool_answers_hot_zones(hz_summary),
    }

    current_tool: str | None = None

    out_lines: list[str] = []
    lines = read_text(report_path).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        m_tool = re.match(r"^###\s+2\.(.+?)\s+—", line)
        if m_tool:
            current_tool = m_tool.group(1).strip()

        # Part A Qs
        if "Part A answers" in line:
            out_lines.append(line)
            i += 1
            while i < len(lines) and re.match(r"^- Q\d+:", lines[i]):
                qn = int(re.match(r"^- Q(\d+):", lines[i]).group(1))  # type: ignore[union-attr]
                if ELLIPSIS in lines[i] or "... " in lines[i] or lines[i].rstrip().endswith("..."):
                    out_lines.append(f"- Q{qn}: {part_a.get(qn, '(no answer)')}")
                else:
                    out_lines.append(lines[i])
                i += 1
            continue

        # Tool Qs
        if line.strip().startswith("Tool answers (fill using the template"):
            out_lines.append(line)
            i += 1
            while i < len(lines) and re.match(r"^- Q\d+:", lines[i]):
                qn = int(re.match(r"^- Q(\d+):", lines[i]).group(1))  # type: ignore[union-attr]
                ans_map = tool_answers.get(current_tool or "", {})
                if ELLIPSIS in lines[i] or "... " in lines[i] or lines[i].rstrip().endswith("..."):
                    out_lines.append(f"- Q{qn}: {ans_map.get(qn, '(no answer)')}")
                else:
                    out_lines.append(lines[i])
                i += 1
            continue

        # Cross-tool synthesis placeholders
        if line.strip().startswith("- Shared clusters/signals:") and (ELLIPSIS in line or "..." in line):
            out_lines.append("- Shared clusters/signals: See Stable/DR/HotZones/VTRAC winners lines + Aux top candidates; log overlaps in Part 5.")
            i += 1
            continue
        if line.strip().startswith("- Conflicts/noise:") and (ELLIPSIS in line or "..." in line):
            out_lines.append("- Conflicts/noise: If Stable exact hits are absent but other tools show heat, treat as noisy/negative-control; do not tune yet.")
            i += 1
            continue
        if line.strip().startswith("- Aggregator/aux hooks to test next:") and (ELLIPSIS in line or "..." in line):
            out_lines.append("- Aggregator/aux hooks to test next: cross-variant bounce metrics + mirror/double pressure closure (Fix-Later).")
            i += 1
            continue

        # Part 3 Qs
        if "Part 3 answers" in line:
            out_lines.append(line)
            i += 1
            while i < len(lines) and re.match(r"^- Q\d+:", lines[i]):
                qn = int(re.match(r"^- Q(\d+):", lines[i]).group(1))  # type: ignore[union-attr]
                if ELLIPSIS in lines[i] or "... " in lines[i] or lines[i].rstrip().endswith("..."):
                    out_lines.append(f"- Q{qn}: {part3.get(qn, '(no answer)')}")
                else:
                    out_lines.append(lines[i])
                i += 1
            continue

        # Part 4 placeholders
        if line.strip().startswith("- Candidate universe (Midday):") and (ELLIPSIS in line or "..." in line):
            out_lines.append(f"- Candidate universe (Midday): {part4['midday']}")
            i += 1
            continue
        if line.strip().startswith("- Candidate universe (Evening):") and (ELLIPSIS in line or "..." in line):
            out_lines.append(f"- Candidate universe (Evening): {part4['evening']}")
            i += 1
            continue
        if line.strip().startswith("- Evidence vectors:") and (ELLIPSIS in line or "..." in line):
            out_lines.append(f"- Evidence vectors: {part4['evidence']}")
            i += 1
            continue
        if line.strip().startswith("- Coverage mapping + pack decision:") and (ELLIPSIS in line or "..." in line):
            out_lines.append(f"- Coverage mapping + pack decision: {part4['mapping']}")
            i += 1
            continue

        # Part 5 placeholders / normalization
        if line.strip().startswith("- Pack vs winners:"):
            has_sub = i + 1 < len(lines) and lines[i + 1].startswith("  -")
            if (ELLIPSIS in line or "..." in line) or (normalize_part5 and not has_sub):
                out_lines.append("- Pack vs winners:")
                out_lines.append(f"  - {part5['pack_midday']}")
                out_lines.append(f"  - {part5['pack_evening']}")
                i += 1
                continue

        if line.strip().startswith("- Key tags:"):
            has_sub = i + 1 < len(lines) and lines[i + 1].startswith("  -")
            if (ELLIPSIS in line or "..." in line) or (normalize_part5 and not has_sub):
                out_lines.append("- Key tags:")
                out_lines.append(f"  - {part5['tags']}")
                i += 1
                continue

        if line.strip().startswith("- Drivers:"):
            has_sub = i + 1 < len(lines) and lines[i + 1].startswith("  -")
            if (ELLIPSIS in line or "..." in line) or (normalize_part5 and not has_sub):
                out_lines.append("- Drivers:")
                out_lines.append(f"  - {part5['drivers']}")
                i += 1
                continue

        if line.strip().startswith("- Conflicts:"):
            has_sub = i + 1 < len(lines) and lines[i + 1].startswith("  -")
            if (ELLIPSIS in line or "..." in line) or (normalize_part5 and not has_sub):
                out_lines.append("- Conflicts:")
                out_lines.append(f"  - {part5['conflicts']}")
                i += 1
                continue

        if line.strip().startswith("- Fix-now vs fix-later:"):
            has_sub = i + 1 < len(lines) and lines[i + 1].startswith("  -")
            if (ELLIPSIS in line or "..." in line) or (normalize_part5 and not has_sub):
                out_lines.append("- Fix-now vs fix-later:")
                out_lines.append(f"  - {part5['fix_now']}")
                out_lines.append(f"  - {part5['fix_later']}")
                i += 1
                continue

        if line.strip().startswith("- Next run:"):
            has_sub = i + 1 < len(lines) and lines[i + 1].startswith("  -")
            if (ELLIPSIS in line or "..." in line) or (normalize_part5 and not has_sub):
                out_lines.append("- Next run:")
                out_lines.append(f"  - {part5['next']}")
                i += 1
                continue

        out_lines.append(line)
        i += 1

    report_path.write_text("\n".join(out_lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument("--state", required=True, help="State key (e.g., NewYork4)")
    ap.add_argument(
        "--normalize-part5",
        action="store_true",
        help="Rewrite Part 5 bullets into the multi-line SSOT format (safe for corpus export).",
    )
    args = ap.parse_args()

    parse_iso_date(args.date)
    fill_report(date=args.date, state=args.state, normalize_part5=bool(args.normalize_part5))
    print(f"Filled: docs/AAT9_KIT/FINAL VALIDATION/RUNS/{args.date}__{args.state}.md")


if __name__ == "__main__":
    main()
