#!/usr/bin/env python3
"""
DR-004 alignment report (10-case queue).

Goal: for a curated set of high-signal “buried-but-present” cases, verify that
DR-004 signals (digit pools / canonicals / index) surface the winner in a bounded
top-K list.

Reporting-only:
- Reads: sharepacks/<D>/<STATE>/... (steps CSV + winners/overlays for evaluation)
- Writes: docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_004__ALIGNMENT_REPORT.md

No analyzer writes, no sharepack mutation.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _canon(draw: str) -> str:
    d = "".join(ch for ch in str(draw or "") if ch.isdigit())
    if not d:
        return ""
    d = d.zfill(3) if len(d) <= 3 else d
    if len(d) != 3:
        return ""
    return "".join(sorted(d))


def _winner_type(winner: str) -> str:
    w = "".join(ch for ch in str(winner or "") if ch.isdigit()).zfill(3)
    if len(w) != 3 or not w.isdigit():
        return "unknown"
    a, b, c = w[0], w[1], w[2]
    if a == b == c:
        return "triple"
    if a == b or a == c or b == c:
        return "double"
    return "unique"


def _winner_pool_digits(winner: str) -> str:
    w = "".join(ch for ch in str(winner or "") if ch.isdigit()).zfill(3)
    uniq = sorted(set(w))
    return "".join(uniq)


def _expand_pool_to_canonicals(pool_digits: str) -> List[str]:
    uniq = "".join(sorted(set(pool_digits or "")))
    if not uniq:
        return []
    if len(uniq) == 1:
        d = uniq
        return [d + d + d]
    if len(uniq) == 2:
        a, b = uniq[0], uniq[1]
        return sorted({_canon(a + a + b), _canon(a + b + b)})
    if len(uniq) >= 3:
        a, b, c = uniq[0], uniq[1], uniq[2]
        doubles = {
            _canon(a + a + b),
            _canon(a + b + b),
            _canon(a + a + c),
            _canon(a + c + c),
            _canon(b + b + c),
            _canon(b + c + c),
        }
        singles = {_canon(a + b + c)}
        return sorted({*doubles, *singles} - {""})
    return []


def _find_first(path: Path, patterns: Sequence[str]) -> Optional[Path]:
    if not path.exists():
        return None
    for pat in patterns:
        matches = sorted(path.glob(pat))
        if matches:
            return matches[0]
    return None


def _find_winner_html(evidence_state_dir: Path, state_key: str, winner: str) -> Optional[Path]:
    winners_dir = evidence_state_dir / "winners" / state_key
    if not winners_dir.exists():
        return None
    w = "".join(ch for ch in str(winner or "") if ch.isdigit()).zfill(3)
    return _find_first(
        winners_dir,
        patterns=[
            f"*winner_{w}_*.html",
            f"*winner_{w}_*.htm",
            f"*{w}*.html",
        ],
    )


def _find_dr_overlay_html(evidence_state_dir: Path, state_key: str, results_date: str, outcome: str) -> Optional[Path]:
    dr_dir = evidence_state_dir / "digit_reduction" / state_key / "analyzer_v2" / "winners"
    if not dr_dir.exists():
        return None
    stamp = str(results_date or "").replace("-", "")
    out = str(outcome or "").strip()
    return _find_first(
        dr_dir,
        patterns=[
            f"{stamp}_{out}_winner_overlay.html",
            f"*_{out}_winner_overlay.html",
        ],
    )


def _vtrac_index(canon: str) -> Optional[int]:
    try:
        from modules.vtrac_reference import get_vtrac_index  # type: ignore
    except Exception:
        return None
    try:
        idx = get_vtrac_index(canon)
    except Exception:
        return None
    return int(idx) if isinstance(idx, int) else None


def _load_dr004_signals(
    *,
    sharepack_state_dir: Path,
    state_key: str,
    recent_draws: int,
    min_unique_digits: int,
    max_unique_digits: int,
    top_pools: int,
    top_canon: int,
    top_idx: int,
) -> Dict[str, Any]:
    # Import the already-implemented DR-004 scorer from Candidate Universe.
    from scripts.tools.create_candidate_universe import _parse_dr004_steps  # type: ignore

    signals: Dict[str, Any] = {}
    _parse_dr004_steps(
        state_dir=sharepack_state_dir,
        state_key=state_key,
        boxed_canonicals=0,
        index_boxed_canonicals=0,
        recent_draws=int(recent_draws),
        max_cost_units=0,
        min_unique_digits=int(min_unique_digits),
        max_unique_digits=int(max_unique_digits),
        signals_out=signals,
        signals_top_pools=int(top_pools),
        signals_top_canonicals=int(top_canon),
        signals_top_indices=int(top_idx),
    )
    return signals


@dataclass(frozen=True)
class Case:
    results_date: str
    state_key: str
    outcome: str
    winner: str


def _default_cases() -> List[Case]:
    # Seed queue from DR_004__SPEC.md (top 10).
    return [
        Case("2026-01-09", "OntarioCanada4", "Evening", "104"),
        Case("2026-01-08", "Florida4", "Midday", "429"),
        Case("2026-01-07", "Michigan4", "Evening", "616"),
        Case("2026-01-02", "NorthCarolina4", "Midday", "033"),
        Case("2025-12-31", "Delaware4", "Evening", "337"),
        Case("2025-06-21", "Pennsylvania4", "Midday", "667"),
        Case("2026-01-07", "Delaware4", "Evening", "922"),
        Case("2025-06-23", "Indiana4", "Midday", "110"),
        Case("2025-12-31", "Virginia4", "Midday", "686"),
        Case("2025-06-21", "OntarioCanada4", "Midday", "678"),
    ]


def _render_hit(rank: Optional[int]) -> str:
    return "—" if rank is None else f"YES (#{rank})"


def main() -> None:
    ap = argparse.ArgumentParser(description="DR-004 10-case alignment report (reporting-only).")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks",
        help="Post-results sharepacks root (for winners HTML + DR overlays) (default: sharepacks).",
    )
    ap.add_argument(
        "--predictive-sharepacks-root",
        default="sharepacks/_predictive",
        help="Predictive sharepacks root (preferred for signals inputs; fallback to sharepacks if missing) (default: sharepacks/_predictive).",
    )
    ap.add_argument(
        "--recent-draws",
        type=int,
        default=2,
        help="DR-004 recency digit overlap window (default: 2; 0 disables).",
    )
    ap.add_argument(
        "--min-unique-digits",
        type=int,
        default=1,
        help="DR-004 pool filter: minimum unique digits per segment (default: 1).",
    )
    ap.add_argument(
        "--max-unique-digits",
        type=int,
        default=3,
        help="DR-004 pool filter: maximum unique digits per segment (default: 3; set to 4 to enable envelope4).",
    )
    ap.add_argument("--top-pools", type=int, default=12, help="Top pools per section to check (default: 12).")
    ap.add_argument("--top-canonicals", type=int, default=25, help="Top canonicals per section to check (default: 25).")
    ap.add_argument("--top-indices", type=int, default=12, help="Top indices per section to check (default: 12).")
    ap.add_argument(
        "--out-md",
        default=str(
            REPO_ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS"
            / "DR_004__ALIGNMENT_REPORT.md"
        ),
        help="Output Markdown path (default: RUNS/DR_004__ALIGNMENT_REPORT.md).",
    )
    args = ap.parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    predictive_root = Path(args.predictive_sharepacks_root)
    if not predictive_root.is_absolute():
        predictive_root = (REPO_ROOT / predictive_root).resolve()

    cases = _default_cases()

    md: List[str] = []
    md.append("# DR-004 — 10-Case Alignment Report\n")
    md.append("Purpose: validate (case-first) whether DR-004 signals surface the winner as:\n")
    md.append("- a top digit pool (envelope),\n- a top canonical,\n- and/or a top VTRAC index gateway.\n")
    md.append("## Config\n")
    md.append(f"- recent_draws: `{int(args.recent_draws)}`")
    md.append(f"- unique_digits: `{int(args.min_unique_digits)}` → `{int(args.max_unique_digits)}`")
    md.append(f"- top_pools: `{int(args.top_pools)}`")
    md.append(f"- top_canonicals: `{int(args.top_canonicals)}`")
    md.append(f"- top_indices: `{int(args.top_indices)}`")
    md.append(f"- predictive root (preferred): `{_safe_rel(predictive_root)}`")
    md.append(f"- evidence root (winners/overlays): `{_safe_rel(sharepacks_root)}`\n")

    md.append("## Summary (winner presence in DR-004 signals)\n")
    md.append(
        "| # | Date | State | Outcome | Winner | Type | Canon | VTRAC idx | pool_contains | canonical_top | index_top |"
    )
    md.append("|---:|---|---|---|---:|---|---:|---:|---|---|---|")

    details_blocks: List[str] = []
    for i, c in enumerate(cases, start=1):
        evidence_state_dir = sharepacks_root / c.results_date / c.state_key
        pred_state_dir = predictive_root / c.results_date / c.state_key
        signals_state_dir = pred_state_dir if pred_state_dir.exists() else evidence_state_dir

        winner = "".join(ch for ch in c.winner if ch.isdigit()).zfill(3)
        winner_canon = _canon(winner)
        winner_type = _winner_type(winner)
        winner_pool = _winner_pool_digits(winner)
        winner_idx = _vtrac_index(winner_canon)

        signals = _load_dr004_signals(
            sharepack_state_dir=signals_state_dir,
            state_key=c.state_key,
            recent_draws=int(args.recent_draws),
            min_unique_digits=int(args.min_unique_digits),
            max_unique_digits=int(args.max_unique_digits),
            top_pools=int(args.top_pools),
            top_canon=int(args.top_canonicals),
            top_idx=int(args.top_indices),
        )
        section = str(c.outcome).strip()
        sec = (signals.get("sections") or {}).get(section) if isinstance(signals.get("sections"), dict) else None
        sec = sec if isinstance(sec, dict) else {}

        # Canonical rank.
        canon_rank: Optional[int] = None
        canon_list = sec.get("top_canonicals") if isinstance(sec.get("top_canonicals"), list) else []
        for j, row in enumerate(canon_list, start=1):
            if isinstance(row, dict) and str(row.get("canonical") or "") == winner_canon:
                canon_rank = j
                break

        # Index rank.
        idx_rank: Optional[int] = None
        if winner_idx is not None:
            idx_list = sec.get("top_indices") if isinstance(sec.get("top_indices"), list) else []
            for j, row in enumerate(idx_list, start=1):
                if isinstance(row, dict) and row.get("vtrac_index") == winner_idx:
                    idx_rank = j
                    break

        # Pool containment (winner canonical present in any top pool expansion).
        pool_rank: Optional[int] = None
        pools_list = sec.get("top_pools") if isinstance(sec.get("top_pools"), list) else []
        for j, row in enumerate(pools_list, start=1):
            if not isinstance(row, dict):
                continue
            pool_digits = str(row.get("digits") or "")
            if winner_canon in _expand_pool_to_canonicals(pool_digits):
                pool_rank = j
                break

        md.append(
            f"| {i} | {c.results_date} | {c.state_key} | {c.outcome} | {winner} | {winner_type} | {winner_canon} | "
            f"{'' if winner_idx is None else str(winner_idx)}"
            f" | {_render_hit(pool_rank)} | {_render_hit(canon_rank)} | {_render_hit(idx_rank)} |"
        )

        winner_html = _find_winner_html(evidence_state_dir, c.state_key, winner)
        dr_overlay = _find_dr_overlay_html(evidence_state_dir, c.state_key, c.results_date, c.outcome)

        # Small per-case block with direct links and minimal signal excerpt.
        block: List[str] = []
        block.append(f"### {i}) {c.results_date} {c.state_key} {c.outcome} — winner {winner}\n")
        block.append(f"- Evidence dir: `{_safe_rel(evidence_state_dir)}`")
        block.append(f"- Signals input dir: `{_safe_rel(signals_state_dir)}`")
        if winner_html:
            block.append(f"- Winners HTML: `{_safe_rel(winner_html)}`")
        else:
            block.append("- Winners HTML: (missing)")
        if dr_overlay:
            block.append(f"- DR overlay: `{_safe_rel(dr_overlay)}`")
        else:
            block.append("- DR overlay: (missing)")
        block.append(
            f"- Winner canonical/index: `{winner_canon}` / `{'' if winner_idx is None else str(winner_idx)}` "
            f"(type={winner_type}; pool=`{winner_pool}`)"
        )
        block.append(
            f"- pool_contains: {_render_hit(pool_rank)}; canonical_top: {_render_hit(canon_rank)}; index_top: {_render_hit(idx_rank)}"
        )

        # Show the first few pool/canonical digits so humans can sanity-check quickly.
        top_pool_digits = [str(r.get("digits") or "") for r in pools_list[:6] if isinstance(r, dict)]
        top_pool_digits = [d for d in top_pool_digits if d]
        top_canon_digits = [str(r.get("canonical") or "") for r in canon_list[:6] if isinstance(r, dict)]
        top_canon_digits = [d for d in top_canon_digits if d]
        if top_pool_digits:
            block.append(f"- Top pools (first 6): `{', '.join(top_pool_digits)}`")
        if top_canon_digits:
            block.append(f"- Top canonicals (first 6): `{', '.join(top_canon_digits)}`")

        details_blocks.append("\n".join(block))

    md.append("\n## Case Details\n")
    md.extend(details_blocks)

    out_md = Path(args.out_md)
    if not out_md.is_absolute():
        out_md = (REPO_ROOT / out_md).resolve()
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
