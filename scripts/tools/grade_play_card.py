#!/usr/bin/env python3
"""
Grade play_card.json artifacts against posted results.

This is an "analysis layer" tool:
- Reads ONLY existing artifacts:
  - sharepacks/<root>/<D>/<STATE>/play_card*.json
  - data/results/<D>.txt (or an explicit --results-file)
- Writes grading outputs ONLY into RUNS (never into predictive sharepacks).
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


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
    d = _normalize_pick3_literal(draw)
    return "".join(sorted(d)) if d else ""


def _unique_perms(triad: str) -> set[str]:
    from itertools import permutations

    triad = _normalize_pick3_literal(triad)
    if not triad:
        return set()
    return {"".join(p) for p in permutations(triad, 3)}


def _boxed_canonicals(combos: Sequence[str]) -> set[str]:
    by_canon: Dict[str, set[str]] = {}
    for c in combos:
        c = _normalize_pick3_literal(c)
        if not c:
            continue
        by_canon.setdefault(_canon(c), set()).add(c)
    boxed: set[str] = set()
    for canon, members in by_canon.items():
        perms = _unique_perms(canon)
        if perms and perms.issubset(members):
            boxed.add(canon)
    return boxed


def _pack_vtrac_indices(combos: Sequence[str]) -> set[int]:
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


@dataclass(frozen=True)
class Winner:
    midday: Optional[str]
    evening: Optional[str]


def _load_results_winners(results_file: Path) -> Dict[str, Winner]:
    if not results_file.exists():
        return {}
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


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Grade sharepack play_card.json artifacts against results.")
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="mixed",
        help="Ablation profile (default: mixed). Selects play_card filename and grade output suffix.",
    )
    ap.add_argument("--states", nargs="*", help="Optional subset of state keys to grade.")
    ap.add_argument(
        "--results-file",
        default=None,
        help="Override results file (default: data/results/<D>.txt)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs (default: refuse).")
    ap.add_argument("--out-csv", default=None, help="Override CSV output path (default: RUNS/<D>__PLAY_CARD_GRADE.csv)")
    ap.add_argument("--out-md", default=None, help="Override Markdown output path (default: RUNS/<D>__PLAY_CARD_GRADE.md)")
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

    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"{args.date}__PLAY_CARD_GRADE{out_suffix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"{args.date}__PLAY_CARD_GRADE{out_suffix}.md"
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
        "play_card_path",
        "state_key",
        "winner_label",
        "winner",
        "winner_canonical",
        "winner_vtrac_index",
        "winner_missing",
        "strategy",
        "budget_label",
        "combos_count",
        "boxed_canonicals_count",
        "hit_any",
        "straight_hit",
        "box_hit",
        "vtrac_index_hit",
        "vtrac_index_hit_only",
    ]

    rows_out: List[Dict[str, str]] = []

    for state_dir in state_dirs:
        state_key = state_dir.name
        pc_path = state_dir / f"play_card{out_suffix}.json"
        if not pc_path.exists():
            continue
        raw = _read_json(pc_path)
        if not isinstance(raw, dict):
            continue
        profile_in_payload = str(raw.get("profile") or profile or "mixed").strip()

        strategies = raw.get("strategies") or {}
        if not isinstance(strategies, dict):
            continue

        winners = winners_by_state.get(state_key, Winner(midday=None, evening=None))

        for winner_label, winner in (("Midday", winners.midday), ("Evening", winners.evening)):
            w = _normalize_pick3_literal(winner or "")
            missing = not bool(w)
            wcanon = _canon(w) if w else ""
            wvt = _winner_vtrac_index(w) if w else None

            for strat_name, strat_payload in sorted(strategies.items(), key=lambda kv: kv[0]):
                if not isinstance(strat_payload, dict):
                    continue
                for budget_label, card in sorted(strat_payload.items(), key=lambda kv: kv[0]):
                    if not isinstance(card, dict):
                        continue
                    combos = [_normalize_pick3_literal(c) for c in (card.get("combos") or [])]
                    combos = [c for c in combos if c]
                    combos_set = set(combos)
                    boxed = _boxed_canonicals(combos)
                    indices = _pack_vtrac_indices(combos)

                    straight_hit = bool(w and w in combos_set)
                    box_hit = bool(wcanon and wcanon in boxed)
                    hit_any = bool((straight_hit or box_hit) and not missing)
                    vtrac_hit = bool(wvt is not None and wvt in indices)

                    rows_out.append(
                        {
                            "results_date": args.date,
                            "sharepacks_root": _safe_rel(sharepacks_root),
                            "profile": profile_in_payload,
                            "play_card_path": _safe_rel(pc_path),
                            "state_key": state_key,
                            "winner_label": winner_label,
                            "winner": w,
                            "winner_canonical": wcanon,
                            "winner_vtrac_index": str(wvt) if wvt is not None else "",
                            "winner_missing": "1" if missing else "0",
                            "strategy": strat_name,
                            "budget_label": budget_label,
                            "combos_count": str(len(combos)),
                            "boxed_canonicals_count": str(len(boxed)),
                            "hit_any": "1" if hit_any else "0",
                            "straight_hit": "1" if straight_hit else "0",
                            "box_hit": "1" if box_hit else "0",
                            "vtrac_index_hit": "1" if (vtrac_hit and not missing) else "0",
                            "vtrac_index_hit_only": "1" if (vtrac_hit and not hit_any and not missing) else "0",
                        }
                    )

    rows_out.sort(key=lambda r: (r["state_key"], r["winner_label"], r["strategy"], r["budget_label"]))

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    # Minimal Markdown summary (top-line counts).
    total = len(rows_out)
    hits = sum(1 for r in rows_out if r.get("hit_any") == "1")
    lines = [
        f"# Play Card Grade — {args.date}",
        "",
        f"- generated_at: `{_now_iso()}`",
        f"- results_file: `{_safe_rel(results_file)}`",
        f"- rows: `{total}`",
        f"- hit_any: `{hits}`",
        "",
        f"- CSV: `{_safe_rel(out_csv)}`",
    ]
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
