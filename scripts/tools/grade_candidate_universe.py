#!/usr/bin/env python3
"""
Grade per-state Candidate Universe artifacts against posted results.

This is an "analysis layer" tool:
- Reads ONLY existing artifacts:
    - sharepacks/<root>/<D>/<STATE>/candidate_universe.json
    - data/results/<D>.txt (or an explicit --results-file)
- Writes grading outputs ONLY into RUNS (never into predictive sharepacks).

Usage
-----
python3 scripts/tools/grade_candidate_universe.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive
python3 scripts/tools/grade_candidate_universe.py --date 2026-01-07 --states NewJersey4
python3 scripts/tools/grade_candidate_universe.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive --profile tool_only
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(draw: str) -> str:
    draw = _normalize_pick3_literal(draw)
    return "".join(sorted(draw)) if draw else ""


@dataclass(frozen=True)
class Winner:
    midday: Optional[str]
    evening: Optional[str]


def _load_results_winners(results_file: Path) -> Dict[str, Winner]:
    """
    Returns a mapping of project state key -> winners (Midday/Evening).

    Uses the same winner parsing logic as the Control Center batch runner so it
    matches the real pipeline expectations for LotteryPost-style tabbed files.
    """
    if not results_file.exists():
        return {}

    # Import from the pipeline's canonical parser (robust to tabbed + continuation lines).
    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        parse_winner_sheet,
        _PROJECT_STATE_CANDIDATES,
    )

    text = _read_text(results_file)
    entries = parse_winner_sheet(text)

    winners: Dict[str, Winner] = {}
    for entry in entries:
        canonical = getattr(entry, "canonical", None)
        midday = getattr(entry, "midday", None)
        evening = getattr(entry, "evening", None)
        if not canonical:
            continue
        candidates = _PROJECT_STATE_CANDIDATES.get(canonical)
        if not candidates:
            project_state = getattr(entry, "project_state", None)
            candidates = (project_state,) if project_state else ()
        for state_key in candidates:
            if not state_key:
                continue
            winners[state_key] = Winner(
                midday=_normalize_pick3_literal(midday or ""),
                evening=_normalize_pick3_literal(evening or ""),
            )
    return winners


def _iter_state_dirs(day_dir: Path, *, states: Sequence[str] | None) -> List[Path]:
    if states:
        return [day_dir / s for s in states]
    out: List[Path] = []
    for p in sorted(day_dir.iterdir(), key=lambda q: q.name):
        if not p.is_dir():
            continue
        if p.name == "control_center":
            continue
        out.append(p)
    return out


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _truth(v: bool) -> str:
    return "1" if v else "0"


def _pack_hit_any(*, play_mode: str, straight_hit: bool, box_hit: bool) -> bool:
    if play_mode == "BOX":
        return box_hit
    if play_mode == "MIXED":
        return straight_hit or box_hit
    return straight_hit


def _pack_vtrac_indices(combos: Iterable[str]) -> set[int]:
    import modules.vtrac_reference as vr

    indices: set[int] = set()
    for combo in combos:
        c = _normalize_pick3_literal(combo)
        if not c:
            continue
        idx = vr.get_vtrac_index(c)
        if isinstance(idx, int):
            indices.add(idx)
    return indices


def _winner_vtrac_index(winner: str) -> Optional[int]:
    import modules.vtrac_reference as vr

    w = _normalize_pick3_literal(winner)
    if not w:
        return None
    idx = vr.get_vtrac_index(w)
    return idx if isinstance(idx, int) else None


def _evaluate_pack(
    *,
    pack: dict,
    winner: str,
    winner_canon: str,
    winner_vt: Optional[int],
    vtrac_indices: set[int],
    box_canonicals: set[str],
) -> Dict[str, bool]:
    play_mode = str(pack.get("play_mode") or "STRAIGHT")

    straight_hit = winner in set(_normalize_pick3_literal(x) for x in (pack.get("combos") or []))
    box_hit = play_mode in {"BOX", "MIXED"} and winner_canon in box_canonicals
    hit_any = _pack_hit_any(play_mode=play_mode, straight_hit=straight_hit, box_hit=box_hit)
    vtrac_hit = bool(winner_vt is not None and winner_vt in vtrac_indices)
    return {
        "straight_hit": straight_hit,
        "box_hit": box_hit,
        "hit_any": hit_any,
        "vtrac_index_hit": vtrac_hit,
        "vtrac_index_hit_only": bool(vtrac_hit and not hit_any),
    }


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Grade sharepack candidate_universe.json artifacts against results.")
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile (default: tool_only). Selects candidate_universe filename and grade output suffix.",
    )
    ap.add_argument("--states", nargs="*", help="Optional subset of state keys to grade.")
    ap.add_argument(
        "--results-file",
        default=None,
        help="Override results file (default: data/results/<D>.txt)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs (default: refuse).")
    ap.add_argument("--out-csv", default=None, help="Override CSV output path (default: RUNS/<D>__CANDIDATE_UNIVERSE_GRADE.csv)")
    ap.add_argument("--out-md", default=None, help="Override Markdown output path (default: RUNS/<D>__CANDIDATE_UNIVERSE_GRADE.md)")
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {_safe_rel(day_dir)}")

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)

    profile = str(args.profile or "mixed").strip()
    out_suffix = "" if profile == "mixed" else f"__{profile}"

    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"{args.date}__CANDIDATE_UNIVERSE_GRADE{out_suffix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"{args.date}__CANDIDATE_UNIVERSE_GRADE{out_suffix}.md"
    if (out_csv.exists() or out_md.exists()) and not args.force:
        raise SystemExit(f"Refusing to overwrite existing outputs (use --force): {_safe_rel(out_csv)} / {_safe_rel(out_md)}")

    results_file = Path(args.results_file) if args.results_file else (REPO_ROOT / "data" / "results" / f"{args.date}.txt")
    winners_by_state = _load_results_winners(results_file)

    state_dirs = _iter_state_dirs(day_dir, states=args.states)
    if not state_dirs:
        raise SystemExit(f"No state dirs found under: {_safe_rel(day_dir)}")

    fieldnames = [
        "results_date",
        "sharepacks_root",
        "profile",
        "candidate_universe_path",
        "state_key",
        "history_date",
        "winner_label",
        "winner",
        "winner_canonical",
        "winner_vtrac_index",
        "winner_missing",
        "pack_id",
        "method_id",
        "pack_variant",
        "play_mode",
        "combos_count",
        "cost_units",
        "contains_winners_artifacts",
        "hit_any",
        "straight_hit",
        "box_hit",
        "vtrac_index_hit",
        "vtrac_index_hit_only",
    ]

    rows: List[Dict[str, str]] = []
    per_state_union: Dict[Tuple[str, str], Dict[str, str]] = {}

    for state_dir in state_dirs:
        state_key = state_dir.name
        cu_path = state_dir / f"candidate_universe{out_suffix}.json"
        if not cu_path.exists():
            continue

        raw = _read_json(cu_path)
        if not isinstance(raw, dict):
            continue
        packs = raw.get("packs")
        if not isinstance(packs, list):
            packs = []

        history_date = str(raw.get("history_date") or "") or ""
        contains_winners_artifacts = bool(raw.get("contains_winners_artifacts"))
        profile_in_payload = str(raw.get("profile") or profile or "mixed").strip()

        # Union pack (convenience): best-case across all packs.
        union_combos = raw.get("union_combos") if isinstance(raw.get("union_combos"), list) else []
        union_combos_norm = sorted({_normalize_pick3_literal(x) for x in union_combos if _normalize_pick3_literal(x)})

        # Cache per-pack VTRAC indices and box canonicals.
        pack_cache: Dict[str, Tuple[set[int], set[str]]] = {}
        for pack in packs:
            if not isinstance(pack, dict):
                continue
            pack_id = str(pack.get("pack_id") or "")
            combos = pack.get("combos") or []
            if not isinstance(combos, list):
                combos = []
            canonicals = pack.get("canonicals") or []
            if not isinstance(canonicals, list):
                canonicals = []
            box_canonicals = {c for c in (_canon(x) for x in canonicals) if c}
            vtrac_indices = _pack_vtrac_indices(combos)
            pack_cache[pack_id] = (vtrac_indices, box_canonicals)

        union_box_canonicals: set[str] = set()
        union_vtrac_indices: set[int] = set()
        for pack_id, (idxs, box_canonicals) in pack_cache.items():
            union_vtrac_indices.update(idxs)
            union_box_canonicals.update(box_canonicals)

        winners = winners_by_state.get(state_key) or Winner(None, None)
        for winner_label, winner in (("Midday", winners.midday), ("Evening", winners.evening)):
            winner = _normalize_pick3_literal(winner or "")
            winner_missing = not bool(winner)
            winner_canon = _canon(winner) if winner else ""
            winner_vt = _winner_vtrac_index(winner) if winner else None

            # Union metrics (best-case)
            union_pack = {
                "pack_id": "__UNION__",
                "method_id": "union",
                "variant": "Unknown",
                "play_mode": "MIXED",
                "combos": union_combos_norm,
                "canonicals": sorted(union_box_canonicals),
                "combos_count": len(union_combos_norm),
                "cost_units": len(union_combos_norm),
            }
            union_hits = _evaluate_pack(
                pack=union_pack,
                winner=winner,
                winner_canon=winner_canon,
                winner_vt=winner_vt,
                vtrac_indices=union_vtrac_indices,
                box_canonicals=union_box_canonicals,
            )

            per_state_union[(state_key, winner_label)] = {
                "winner": winner,
                "winner_missing": _truth(winner_missing),
                "hit_any": _truth(union_hits["hit_any"]) if not winner_missing else "0",
                "vtrac_index_hit": _truth(union_hits["vtrac_index_hit"]) if not winner_missing else "0",
            }

            # Emit per-pack rows
            for pack in packs:
                if not isinstance(pack, dict):
                    continue
                pack_id = str(pack.get("pack_id") or "")
                method_id = str(pack.get("method_id") or "")
                variant = str(pack.get("variant") or "Unknown")
                play_mode = str(pack.get("play_mode") or "STRAIGHT")
                combos = pack.get("combos") or []
                if not isinstance(combos, list):
                    combos = []
                combos_norm = sorted({_normalize_pick3_literal(x) for x in combos if _normalize_pick3_literal(x)})
                combos_count = int(pack.get("combos_count") or len(combos_norm))
                cost_units = int(pack.get("cost_units") or combos_count)

                vtrac_indices, box_canonicals = pack_cache.get(pack_id, (set(), set()))
                hits = _evaluate_pack(
                    pack=pack,
                    winner=winner,
                    winner_canon=winner_canon,
                    winner_vt=winner_vt,
                    vtrac_indices=vtrac_indices,
                    box_canonicals=box_canonicals,
                )

                rows.append(
                    {
                        "results_date": args.date,
                        "sharepacks_root": _safe_rel(sharepacks_root),
                        "profile": profile_in_payload,
                        "candidate_universe_path": _safe_rel(cu_path),
                        "state_key": state_key,
                        "history_date": history_date,
                        "winner_label": winner_label,
                        "winner": winner,
                        "winner_canonical": winner_canon,
                        "winner_vtrac_index": str(winner_vt) if winner_vt is not None else "",
                        "winner_missing": _truth(winner_missing),
                        "pack_id": pack_id,
                        "method_id": method_id,
                        "pack_variant": variant,
                        "play_mode": play_mode,
                        "combos_count": str(combos_count),
                        "cost_units": str(cost_units),
                        "contains_winners_artifacts": _truth(contains_winners_artifacts),
                        "hit_any": _truth(hits["hit_any"]) if not winner_missing else "0",
                        "straight_hit": _truth(hits["straight_hit"]) if not winner_missing else "0",
                        "box_hit": _truth(hits["box_hit"]) if not winner_missing else "0",
                        "vtrac_index_hit": _truth(hits["vtrac_index_hit"]) if not winner_missing else "0",
                        "vtrac_index_hit_only": _truth(hits["vtrac_index_hit_only"]) if not winner_missing else "0",
                    }
                )

            # Emit union row last (stable pack_id sorting keeps it last)
            rows.append(
                {
                    "results_date": args.date,
                    "sharepacks_root": _safe_rel(sharepacks_root),
                    "profile": profile_in_payload,
                    "candidate_universe_path": _safe_rel(cu_path),
                    "state_key": state_key,
                    "history_date": history_date,
                    "winner_label": winner_label,
                    "winner": winner,
                    "winner_canonical": winner_canon,
                    "winner_vtrac_index": str(winner_vt) if winner_vt is not None else "",
                    "winner_missing": _truth(winner_missing),
                    "pack_id": "__UNION__",
                    "method_id": "union",
                    "pack_variant": "Unknown",
                    "play_mode": "MIXED",
                    "combos_count": str(len(union_combos_norm)),
                    "cost_units": str(len(union_combos_norm)),
                    "contains_winners_artifacts": _truth(contains_winners_artifacts),
                    "hit_any": _truth(union_hits["hit_any"]) if not winner_missing else "0",
                    "straight_hit": _truth(union_hits["straight_hit"]) if not winner_missing else "0",
                    "box_hit": _truth(union_hits["box_hit"]) if not winner_missing else "0",
                    "vtrac_index_hit": _truth(union_hits["vtrac_index_hit"]) if not winner_missing else "0",
                    "vtrac_index_hit_only": _truth(union_hits["vtrac_index_hit_only"]) if not winner_missing else "0",
                }
            )

    rows.sort(key=lambda r: (r["state_key"], r["winner_label"], r["pack_id"]))

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    # Markdown summary: state-level union hits
    states = sorted({r["state_key"] for r in rows})
    def _union_flag(state: str, label: str, key: str) -> str:
        v = per_state_union.get((state, label), {}).get(key, "0")
        if per_state_union.get((state, label), {}).get("winner_missing") == "1":
            return "-"
        return "Y" if v == "1" else "N"

    lines: List[str] = []
    lines.append(f"# Candidate Universe Grade — D={args.date}")
    lines.append("")
    lines.append("Provenance")
    lines.append(f"- Generated: `{_now_iso()}`")
    lines.append(f"- Candidate Universe root: `{_safe_rel(day_dir)}`")
    lines.append(f"- Results file: `{_safe_rel(results_file)}` ({'present' if results_file.exists() else 'missing'})")
    lines.append("")
    lines.append("## Union summary (best-case across all packs)")
    lines.append("")
    lines.append("| StateKey | Midday | Midday Hit | Midday VTRAC | Evening | Evening Hit | Evening VTRAC |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for state in states:
        mid = per_state_union.get((state, "Midday"), {}).get("winner", "") or ""
        eve = per_state_union.get((state, "Evening"), {}).get("winner", "") or ""
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{state}`",
                    mid or "—",
                    _union_flag(state, "Midday", "hit_any"),
                    _union_flag(state, "Midday", "vtrac_index_hit"),
                    eve or "—",
                    _union_flag(state, "Evening", "hit_any"),
                    _union_flag(state, "Evening", "vtrac_index_hit"),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("Notes")
    lines.append("- This grades the Candidate Universe as a **pre-results** prediction substrate.")
    lines.append("- `VTRAC` here means boxed-family `vtrac_index` (not V-straights/vcode).")
    lines.append("- Outputs are written to RUNS to keep predictive sharepacks immutable.")
    lines.append("")

    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
