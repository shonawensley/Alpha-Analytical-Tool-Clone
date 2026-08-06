#!/usr/bin/env python3
"""Lossless, read-only Positional Tracker adapter for AUX CORE review.

The existing Aux sharepack projection intentionally emits a compact Positional
summary. This module reruns the native analyzer against frozen draw snapshots and
serializes the complete review surface without changing native scoring or any
runtime consumer.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from core.aux_config import POSITIONAL_WINDOW, POS_SHORTLIST_CONFIG  # type: ignore
from modules.aux_loaders import load_state_draws  # type: ignore
from modules.module_d_auxiliary_tools.refactored.positional_tool import (  # type: ignore
    StatePositionalReport,
    WeightsConfig,
    analyze_state_variants,
)
from modules.vtrac_reference import get_vtrac_index  # type: ignore


VARIANTS: tuple[str, ...] = ("combined", "midday", "evening")
WIDTHS: tuple[int, ...] = (3, 6, 8, 10, 12, 16)
MIRROR_MAP: Dict[int, int] = {
    0: 5,
    5: 0,
    1: 6,
    6: 1,
    2: 7,
    7: 2,
    3: 8,
    8: 3,
    4: 9,
    9: 4,
}


def canonical(combo: str) -> str:
    value = str(combo or "").strip()
    if len(value) != 3 or not value.isdigit():
        return ""
    return "".join(sorted(value))


def normalize_winner(value: Any) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    return digits[-3:].zfill(3) if digits else ""


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


def load_frozen_draws(
    state_key: str,
    draws_dir: Path,
    *,
    max_n: int = 1000,
) -> tuple[Dict[str, list[str]], Dict[str, Dict[str, Any]]]:
    """Load M/E/C newest-first snapshots and return explicit provenance."""
    draws_by_variant: Dict[str, list[str]] = {}
    provenance: Dict[str, Dict[str, Any]] = {}
    for variant in VARIANTS:
        draws, resolved = load_state_draws(
            state_key,
            variant=variant,
            base=draws_dir,
            max_n=max_n,
        )
        if not draws or not resolved:
            continue
        path = Path(resolved)
        draws_by_variant[variant] = list(draws)
        provenance[variant] = {
            "resolved_path": safe_rel(path),
            "sha256": sha256_file(path),
            "draw_count": len(draws),
            "draws_head": list(draws[:5]),
            "newest_first": True,
        }
    return draws_by_variant, provenance


def _serialize_top_digit(item: Any, *, hard_due: bool) -> Dict[str, Any]:
    return {
        "digit": int(item.digit),
        "rank": int(item.rank),
        "gap": int(item.gap),
        "gap_percentile": float(item.gap_percentile),
        "lag_weight": float(item.lag_weight),
        "occurrence_count": int(item.occurrence_count),
        "last_seen_index": item.last_seen_index,
        "score": float(item.score),
        "score_components": {
            str(key): float(value)
            for key, value in sorted(item.score_components.items())
        },
        "tags": list(item.tags),
        "hard_due": bool(hard_due),
    }


def serialize_report(
    report: StatePositionalReport,
    *,
    state_key: str,
    results_date: str,
    profile: str,
    source_provenance: Mapping[str, Mapping[str, Any]],
    analysis_scope: str = "all_variants",
    target_variant: Optional[str] = None,
    context_receipt: Optional[Mapping[str, Any]] = None,
    window: int = POSITIONAL_WINDOW,
    topk: int = 3,
) -> Dict[str, Any]:
    """Serialize every native Positional field needed for review and grading."""
    variants: Dict[str, Any] = {}
    for variant, result in report.variant_results.items():
        positions: Dict[str, Any] = {}
        for position in (0, 1, 2):
            summary = result.position_summaries.get(position)
            hard_due_by_digit = {
                int(cell.digit): bool(cell.hard_due)
                for cell in result.tracker_grid.get(position, [])
            }
            positions[str(position)] = {
                "position": position,
                "population": int(summary.population) if summary else 0,
                "window": int(summary.window) if summary else int(window),
                "top_digits": [
                    _serialize_top_digit(
                        item,
                        hard_due=hard_due_by_digit.get(int(item.digit), False),
                    )
                    for item in (summary.top_digits if summary else [])
                ],
            }
        variants[variant] = {
            "draws_used": int(result.draws_used),
            "window": int(result.window),
            "positions": positions,
        }

    aggregated_digits: Dict[str, Any] = {}
    for position, items in report.aggregated_digits.items():
        aggregated_digits[str(position)] = [
            {
                "rank": rank,
                "digit": int(item.digit),
                "score": float(item.score),
                "occurrences": [
                    {"variant": str(variant), "rank": int(native_rank)}
                    for variant, native_rank in item.occurrences
                ],
                "tags": list(item.tags),
            }
            for rank, item in enumerate(items, start=1)
        ]

    candidates = []
    for rank, candidate in enumerate(report.candidates, start=1):
        combo = str(candidate.combo)
        candidates.append(
            {
                "rank": rank,
                "combo": combo,
                "canonical": canonical(combo),
                "score": float(candidate.score),
                "native_ranks": [int(value) for value in candidate.ranks],
                "digital_root": int(candidate.digital_root),
                "vtrac_index": candidate.vtrac_index,
                "tags": list(candidate.tags),
                "evidence": list(candidate.evidence),
                "source": str(candidate.source),
            }
        )

    return {
        "schema_version": "positional_aux_core_v1",
        "metadata": {
            "state_key": state_key,
            "results_date": results_date,
            "profile": profile,
            "analysis_scope": analysis_scope,
            "target_variant": target_variant,
            "window": int(window),
            "topk_per_position": int(topk),
            "source_is_frozen_pre_result": True,
            "winner_fields_present": False,
        },
        "source_provenance": {
            key: dict(value) for key, value in sorted(source_provenance.items())
        },
        "context_receipt": dict(context_receipt or {}),
        "variants": variants,
        "aggregated_digits": aggregated_digits,
        "consensus_notes": list(report.consensus_notes),
        "double_pressure_notes": list(report.double_pressure_notes),
        "candidates": candidates,
    }


def build_lossless_report(
    *,
    state_key: str,
    results_date: str,
    draws_dir: Path,
    profile: str = "native_all_variant",
    target_variant: Optional[str] = None,
    weights: Optional[WeightsConfig] = None,
    shortlist_cfg: Optional[Mapping[str, Any]] = None,
    due_doubles_active: bool = False,
    vtrac_hot_indices: Optional[Iterable[int]] = None,
    vtrac_hot_families: Optional[Mapping[str, str]] = None,
    max_n: int = 1000,
    window: int = POSITIONAL_WINDOW,
    topk: int = 3,
) -> Dict[str, Any]:
    draws_by_variant, provenance = load_frozen_draws(
        state_key,
        draws_dir,
        max_n=max_n,
    )
    if target_variant:
        target_variant = target_variant.lower()
        draws_by_variant = {
            target_variant: draws_by_variant[target_variant]
        } if target_variant in draws_by_variant else {}
        provenance = {
            target_variant: provenance[target_variant]
        } if target_variant in provenance else {}
    if not draws_by_variant:
        raise ValueError(f"No frozen Positional draws found for {state_key}: {draws_dir}")

    config = dict(POS_SHORTLIST_CONFIG or {})
    if shortlist_cfg:
        config.update(shortlist_cfg)
    hot_indices = sorted({int(value) for value in (vtrac_hot_indices or [])})
    hot_families = dict(vtrac_hot_families or {})
    report = analyze_state_variants(
        draws_by_variant,
        window=window,
        topk=topk,
        weights=weights,
        due_doubles_active=due_doubles_active,
        shortlist_cfg=config,
        vtrac_hot_indices=hot_indices,
        vtrac_hot_families=hot_families,
    )
    return serialize_report(
        report,
        state_key=state_key,
        results_date=results_date,
        profile=profile,
        source_provenance=provenance,
        analysis_scope="target_variant_only" if target_variant else "all_variants",
        target_variant=target_variant,
        context_receipt={
            "due_doubles_active": bool(due_doubles_active),
            "vtrac_hot_indices": hot_indices,
            "vtrac_hot_families": hot_families,
        },
        window=window,
        topk=topk,
    )


def _position_entries(
    payload: Mapping[str, Any],
    *,
    variant: str,
    position: int,
) -> list[Mapping[str, Any]]:
    variants = payload.get("variants") if isinstance(payload.get("variants"), dict) else {}
    variant_payload = variants.get(variant) if isinstance(variants.get(variant), dict) else {}
    positions = (
        variant_payload.get("positions")
        if isinstance(variant_payload.get("positions"), dict)
        else {}
    )
    position_payload = (
        positions.get(str(position))
        if isinstance(positions.get(str(position)), dict)
        else {}
    )
    rows = position_payload.get("top_digits")
    return [row for row in rows if isinstance(row, dict)] if isinstance(rows, list) else []


def _rank_in_entries(entries: Sequence[Mapping[str, Any]], digit: int) -> Optional[int]:
    for row in entries:
        if int(row.get("digit", -1)) == digit:
            return int(row.get("rank", 0)) or None
    return None


def _first_candidate_rank(
    candidates: Sequence[Mapping[str, Any]],
    *,
    field: str,
    expected: Any,
) -> Optional[int]:
    for row in candidates:
        if row.get(field) == expected:
            return int(row.get("rank", 0)) or None
    return None


def _winner_kind(winner: str) -> tuple[str, Optional[int]]:
    counts = Counter(int(ch) for ch in winner)
    if len(counts) == 1:
        return "triple", next(iter(counts))
    repeated = [digit for digit, count in counts.items() if count == 2]
    if repeated:
        return "double", repeated[0]
    return "single", None


def grade_winner(
    payload: Mapping[str, Any],
    *,
    period: str,
    winner: str,
) -> Dict[str, Any]:
    """Join a result after report generation and grade distinct evidence modes."""
    normalized = normalize_winner(winner)
    if len(normalized) != 3:
        raise ValueError(f"Invalid Pick-3 winner: {winner!r}")
    target_variant = period.strip().lower()
    if target_variant not in {"midday", "evening"}:
        raise ValueError(f"Unsupported result period for Positional grading: {period!r}")

    winner_digits = [int(ch) for ch in normalized]
    winner_canonical = canonical(normalized)
    winner_vtrac = get_vtrac_index(normalized)
    variants = [
        value
        for value in VARIANTS
        if value in (payload.get("variants") or {})
    ]

    position_receipts = []
    target_exact_count = 0
    all_variant_exact_count = 0
    all_variant_mirror_count = 0
    loose_exact_count = 0
    loose_mirror_count = 0
    for position, digit in enumerate(winner_digits):
        target_rows = _position_entries(
            payload,
            variant=target_variant,
            position=position,
        )
        target_rank = _rank_in_entries(target_rows, digit)
        if target_rank is not None:
            target_exact_count += 1

        exact_occurrences = []
        mirror_occurrences = []
        loose_exact_occurrences = []
        loose_mirror_occurrences = []
        mirror_digit = MIRROR_MAP[digit]
        for variant in variants:
            same_position_rows = _position_entries(
                payload,
                variant=variant,
                position=position,
            )
            exact_rank = _rank_in_entries(same_position_rows, digit)
            mirror_rank = _rank_in_entries(same_position_rows, mirror_digit)
            if exact_rank is not None:
                exact_occurrences.append({"variant": variant, "rank": exact_rank})
            if mirror_rank is not None:
                mirror_occurrences.append({"variant": variant, "rank": mirror_rank})
            for source_position in (0, 1, 2):
                rows = _position_entries(
                    payload,
                    variant=variant,
                    position=source_position,
                )
                rank = _rank_in_entries(rows, digit)
                if rank is not None:
                    loose_exact_occurrences.append(
                        {
                            "variant": variant,
                            "position": source_position,
                            "rank": rank,
                        }
                    )
                mirror_rank = _rank_in_entries(rows, mirror_digit)
                if mirror_rank is not None:
                    loose_mirror_occurrences.append(
                        {
                            "variant": variant,
                            "position": source_position,
                            "rank": mirror_rank,
                        }
                    )
        if exact_occurrences:
            all_variant_exact_count += 1
        if mirror_occurrences:
            all_variant_mirror_count += 1
        if loose_exact_occurrences:
            loose_exact_count += 1
        if loose_mirror_occurrences:
            loose_mirror_count += 1
        position_receipts.append(
            {
                "position": position,
                "winner_digit": digit,
                "target_variant_rank": target_rank,
                "same_position_exact": exact_occurrences,
                "same_position_mirror": mirror_occurrences,
                "loose_cross_position_exact": loose_exact_occurrences,
                "loose_cross_position_mirror": loose_mirror_occurrences,
            }
        )

    pair_receipts: Dict[str, Any] = {}
    pair_specs = {
        "front": (0, 1),
        "back": (1, 2),
        "endcap": (0, 2),
    }
    for name, (left, right) in pair_specs.items():
        supported_variants = []
        mirror_supported_variants = []
        for variant in variants:
            left_rows = _position_entries(payload, variant=variant, position=left)
            right_rows = _position_entries(payload, variant=variant, position=right)
            if (
                _rank_in_entries(left_rows, winner_digits[left]) is not None
                and _rank_in_entries(right_rows, winner_digits[right]) is not None
            ):
                supported_variants.append(variant)
            if (
                _rank_in_entries(left_rows, MIRROR_MAP[winner_digits[left]]) is not None
                and _rank_in_entries(right_rows, MIRROR_MAP[winner_digits[right]]) is not None
            ):
                mirror_supported_variants.append(variant)
        pair_receipts[name] = {
            "winner_pair": f"{winner_digits[left]}{winner_digits[right]}",
            "same_variant_exact_support": supported_variants,
            "same_variant_mirror_support": mirror_supported_variants,
            "cross_variant_position_support": bool(
                position_receipts[left]["same_position_exact"]
                and position_receipts[right]["same_position_exact"]
            ),
        }

    candidates = [
        row for row in (payload.get("candidates") or []) if isinstance(row, dict)
    ]
    exact_rank = _first_candidate_rank(
        candidates,
        field="combo",
        expected=normalized,
    )
    box_rank = _first_candidate_rank(
        candidates,
        field="canonical",
        expected=winner_canonical,
    )
    vtrac_rank = _first_candidate_rank(
        candidates,
        field="vtrac_index",
        expected=winner_vtrac,
    )

    winner_kind, repeated_digit = _winner_kind(normalized)
    double_anchor_occurrences = []
    if repeated_digit is not None:
        for variant in variants:
            for position in (0, 1, 2):
                rank = _rank_in_entries(
                    _position_entries(payload, variant=variant, position=position),
                    repeated_digit,
                )
                if rank is not None and rank <= 2:
                    double_anchor_occurrences.append(
                        {
                            "variant": variant,
                            "position": position,
                            "rank": rank,
                        }
                    )

    width_receipts = {
        str(width): {
            "exact": bool(exact_rank is not None and exact_rank <= width),
            "canonical_box": bool(box_rank is not None and box_rank <= width),
            "vtrac_box": bool(vtrac_rank is not None and vtrac_rank <= width),
        }
        for width in WIDTHS
    }

    roles = []
    if exact_rank is not None:
        roles.append("DIRECT_ORDERED")
    if box_rank is not None:
        roles.append("BOXED_CANONICAL")
    if vtrac_rank is not None:
        roles.append("VTRAC_TERRITORY")
    if all_variant_exact_count >= 2 or target_exact_count >= 2:
        roles.append("POSITIONAL_REINFORCEMENT")
    if not roles and (loose_exact_count or all_variant_mirror_count):
        roles.append("BACKGROUND_CONTEXT")
    if not roles:
        roles.append("NO_WINNER_ALIGNMENT")

    return {
        "winner_join_phase": "post_result_grading",
        "predictive_credit_boundary": (
            "Only the frozen report receives predictive credit; this result join "
            "grades pre-existing evidence."
        ),
        "period": period.title(),
        "winner": normalized,
        "winner_canonical": winner_canonical,
        "winner_vtrac_index": winner_vtrac,
        "winner_kind": winner_kind,
        "repeated_digit": repeated_digit,
        "target_variant_exact_position_count": target_exact_count,
        "all_variant_same_position_exact_count": all_variant_exact_count,
        "all_variant_same_position_mirror_count": all_variant_mirror_count,
        "loose_cross_position_exact_count": loose_exact_count,
        "loose_cross_position_mirror_count": loose_mirror_count,
        "position_receipts": position_receipts,
        "pair_receipts": pair_receipts,
        "double_anchor_top2": bool(double_anchor_occurrences),
        "double_anchor_occurrences": double_anchor_occurrences,
        "candidate_count": len(candidates),
        "shortlist_exact_rank": exact_rank,
        "shortlist_canonical_rank": box_rank,
        "shortlist_vtrac_rank": vtrac_rank,
        "width_receipts": width_receipts,
        "role_labels": roles,
    }


def render_report_markdown(
    payload: Mapping[str, Any],
    *,
    grading: Optional[Mapping[str, Any]] = None,
) -> str:
    meta = payload.get("metadata") or {}
    lines = [
        "# Positional AUX CORE Receipt",
        "",
        f"- State: `{meta.get('state_key')}`",
        f"- Results date: `{meta.get('results_date')}`",
        f"- Profile: `{meta.get('profile')}`",
        f"- Scope: `{meta.get('analysis_scope')}`",
        f"- Frozen pre-result source: `{meta.get('source_is_frozen_pre_result')}`",
        "",
        "## Variant Position Grids",
        "",
    ]
    for variant in VARIANTS:
        variant_payload = (payload.get("variants") or {}).get(variant)
        if not isinstance(variant_payload, dict):
            continue
        lines.extend([f"### {variant.title()}", ""])
        for position in (0, 1, 2):
            rows = _position_entries(payload, variant=variant, position=position)
            rendered = ", ".join(
                (
                    f"{row.get('digit')} (R{row.get('rank')}, gap={row.get('gap')}, "
                    f"score={float(row.get('score') or 0.0):.3f}"
                    f"{', HARD_DUE' if row.get('hard_due') else ''})"
                )
                for row in rows
            )
            lines.append(f"- P{position + 1}: {rendered or 'N/A'}")
        lines.append("")

    lines.extend(["## State-Level Ordered Shortlist", ""])
    for row in payload.get("candidates") or []:
        lines.append(
            f"- #{row.get('rank')} `{row.get('combo')}` / `{row.get('canonical')}` / "
            f"VT `{row.get('vtrac_index')}` / score `{float(row.get('score') or 0.0):.4f}` / "
            f"source `{row.get('source')}` / tags `{', '.join(row.get('tags') or []) or '-'}`"
        )
    lines.append("")

    if grading:
        lines.extend(
            [
                "## Post-Result Winner Alignment",
                "",
                f"- Winner: `{grading.get('winner')}` ({grading.get('period')})",
                f"- Target-variant exact-position support: `{grading.get('target_variant_exact_position_count')}/3`",
                f"- All-variant same-position exact support: `{grading.get('all_variant_same_position_exact_count')}/3`",
                f"- All-variant same-position mirror support: `{grading.get('all_variant_same_position_mirror_count')}/3`",
                f"- Shortlist exact rank: `{grading.get('shortlist_exact_rank')}`",
                f"- Shortlist canonical rank: `{grading.get('shortlist_canonical_rank')}`",
                f"- Shortlist VTRAC rank: `{grading.get('shortlist_vtrac_rank')}`",
                f"- Roles: `{', '.join(grading.get('role_labels') or [])}`",
                "",
                "Winner fields were joined after the frozen report was generated.",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


__all__ = [
    "MIRROR_MAP",
    "VARIANTS",
    "WIDTHS",
    "build_lossless_report",
    "canonical",
    "grade_winner",
    "load_frozen_draws",
    "normalize_winner",
    "render_report_markdown",
    "safe_rel",
    "serialize_report",
    "sha256_file",
    "write_json",
]
