#!/usr/bin/env python3
"""
Create a cross-state Predictive Portfolio Markdown summary for a day D.

This is a reporting-only tool:
- Reads ONLY existing predictive sharepack artifacts (no analyzer runs).
- Summarizes the per-state Candidate Universe + Play Card closures so you can
  triage states quickly.
- Profit Alerts are available as an optional column-set (controlled by
  `--profile` / `--rank-by`), but are not required for the tool-first posture.

Usage
-----
python3 scripts/tools/create_predictive_portfolio_report.py --date 2026-01-07
python3 scripts/tools/create_predictive_portfolio_report.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _normalize_pick3(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(value: str) -> str:
    v = _normalize_pick3(value)
    return "".join(sorted(v)) if v else ""


def _profile_suffix(profile: str) -> str:
    p = (profile or "mixed").strip()
    return "" if p == "mixed" else f"__{p}"


@dataclass(frozen=True)
class ProfitAlertRow:
    variant: str
    alert_id: str
    strength: int
    suggested: str
    canonical: str
    combos: List[str]
    badges: str

    @property
    def cost_units(self) -> int:
        return len(self.combos)


def _parse_profit_alerts_for_state(rows: Sequence[Dict[str, str]], *, state_key: str) -> List[ProfitAlertRow]:
    out: List[ProfitAlertRow] = []
    for r in rows:
        if (r.get("StateKey") or "").strip() != state_key:
            continue
        suggested = (r.get("Suggested") or "").strip()
        if not suggested or suggested == "OVERLAY":
            continue
        implied_raw = (r.get("ImpliedSet") or "").strip()
        if not implied_raw.startswith("["):
            continue
        try:
            implied = json.loads(implied_raw)
        except Exception:
            continue
        if not isinstance(implied, list):
            continue
        combos = sorted({_normalize_pick3(x) for x in implied if _normalize_pick3(x)})
        if not combos:
            continue

        variant = (r.get("Variant") or "").strip() or "Unknown"
        alert_id = (r.get("AlertId") or "").strip() or "?"
        try:
            strength = int((r.get("Strength") or "0").strip() or "0")
        except Exception:
            strength = 0
        canonical = _canon((r.get("Canonical") or "").strip())
        badges = (r.get("Badges") or "").strip()

        out.append(
            ProfitAlertRow(
                variant=variant,
                alert_id=alert_id,
                strength=strength,
                suggested=suggested,
                canonical=canonical,
                combos=combos,
                badges=badges,
            )
        )
    # Highest strength first, then cheaper, then stable ordering.
    out.sort(key=lambda x: (-x.strength, x.cost_units, x.variant, x.alert_id, x.suggested, x.canonical))
    return out


def _load_candidate_universe_summary(state_dir: Path, *, profile: str) -> Tuple[int, int, List[str], int, List[str]]:
    """
    Returns:
      - packs_count
      - union_count
      - due_doubles_canonicals_union
      - top_support_count (how many packs support the top canonical)
      - top_support_canonicals (up to 3 canonicals tied for top support)

    Notes:
    - "Support" is computed as a per-pack vote over that pack's `canonicals` list.
    - This is intended as a lightweight convergence proxy for tool-first ranking.
    """
    cu = state_dir / f"candidate_universe{_profile_suffix(profile)}.json"
    if not cu.exists():
        return 0, 0, [], 0, []
    raw = _read_json(cu)
    if not isinstance(raw, dict):
        return 0, 0, [], 0, []
    packs = raw.get("packs")
    packs_list = packs if isinstance(packs, list) else []
    union_count = raw.get("union_combos_count")
    try:
        union_count_int = int(union_count)
    except Exception:
        union = raw.get("union_combos")
        union_count_int = len(union) if isinstance(union, list) else 0

    dd_canon: set[str] = set()
    support: Dict[str, int] = {}
    for p in packs_list:
        if not isinstance(p, dict):
            continue
        method_id = str(p.get("method_id") or "")
        canonicals = p.get("canonicals") or []
        if isinstance(canonicals, list):
            uniq: set[str] = set()
            for c in canonicals:
                cc = _canon(str(c))
                if cc:
                    uniq.add(cc)
            for cc in uniq:
                support[cc] = support.get(cc, 0) + 1

        if method_id != "due_doubles":
            continue
        for c in canonicals or []:
            cc = _canon(str(c))
            if cc:
                dd_canon.add(cc)

    top_support_count = max(support.values(), default=0)
    top_support = [c for c, n in sorted(support.items(), key=lambda x: (-x[1], x[0])) if n == top_support_count][:3]

    return len(packs_list), union_count_int, sorted(dd_canon), top_support_count, top_support


def _play_card_path(state_dir: Path, *, profile: str, experiment_tag: str) -> Path:
    out_suffix = _profile_suffix(profile)
    tag_suffix = f"__{experiment_tag.strip()}" if (experiment_tag or "").strip() else ""
    return state_dir / f"play_card{out_suffix}{tag_suffix}.json"


def _load_play_card_cut(
    state_dir: Path,
    *,
    profile: str,
    strategy: str,
    budget: int,
    prefer_experiment_tags: Sequence[str] = ("", "vtracpack_v1"),
) -> Tuple[int, List[str], List[str], Optional[int], List[str], Optional[Path]]:
    """
    Returns:
      (boxed_canonicals_count, boxed_canonicals, combos, vtrac_pack_index, vtrac_pack_combos, source_path)
    """
    bkey = f"B{int(budget)}"
    for tag in prefer_experiment_tags:
        pc = _play_card_path(state_dir, profile=profile, experiment_tag=tag)
        if not pc.exists():
            continue
        raw = _read_json(pc)
        if not isinstance(raw, dict):
            continue
        strategies = raw.get("strategies")
        if not isinstance(strategies, dict):
            continue
        strat = strategies.get(strategy)
        if not isinstance(strat, dict):
            continue
        card = strat.get(bkey)
        if not isinstance(card, dict):
            continue

        combos_raw = card.get("combos") or []
        combos: List[str] = []
        combos_seen: set[str] = set()
        for x in combos_raw:
            n = _normalize_pick3(x)
            if not n or n in combos_seen:
                continue
            combos.append(n)
            combos_seen.add(n)

        boxed_raw = card.get("boxed_canonicals") or []
        boxed = sorted({_canon(x) for x in boxed_raw if _canon(x)})
        try:
            boxed_count = int(card.get("boxed_canonicals_count"))
        except Exception:
            boxed_count = len(boxed)

        vtrac_pack_index: Optional[int] = None
        vtrac_pack_combos: List[str] = []
        vtrac_pack = card.get("vtrac_pack")
        if isinstance(vtrac_pack, dict):
            try:
                vtrac_pack_index = int(vtrac_pack.get("index"))
            except Exception:
                vtrac_pack_index = None
            pack_raw = vtrac_pack.get("pack_combos") or []
            if isinstance(pack_raw, list):
                vtrac_pack_combos = [_normalize_pick3(x) for x in pack_raw if _normalize_pick3(x)]

        return boxed_count, boxed, combos, vtrac_pack_index, vtrac_pack_combos, pc

    return 0, [], [], None, [], None


def _pack_label(pack_index: Optional[int], pack_combos: Sequence[str]) -> str:
    if pack_index is None:
        return "-"
    size = len(list(pack_combos or []))
    return f"{pack_index}({size})" if size else str(pack_index)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create a cross-state predictive portfolio report for a day D.")
    ap.add_argument("--date", required=True, help="Predictive results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile to summarize (default: tool_only). Uses candidate_universe*.json and play_card*.json for that profile.",
    )
    ap.add_argument(
        "--rank-by",
        choices=["profit_alerts", "tool_first"],
        default=None,
        help="Ranking mode (default: profit_alerts for mixed; tool_first for tool_only/profit_only).",
    )
    ap.add_argument("--out", default=None, help="Override output path (default: RUNS/<D>__PREDICTIVE_PORTFOLIO.md)")
    ap.add_argument("--force", action="store_true", help="Overwrite an existing report (default: refuse).")
    ap.add_argument("--top-n-alerts", type=int, default=3, help="Top N Profit Alerts rows to list per state (default: 3)")
    ap.add_argument("--top-n-due-doubles", type=int, default=6, help="Top N Due Doubles canonicals to show per state (default: 6)")
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {_safe_rel(day_dir)}")

    cc_dir = day_dir / "control_center"
    pa_path = cc_dir / "profit_alerts.csv"
    pa_rows = _load_csv_rows(pa_path)

    states = sorted(p.name for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center")
    if not states:
        raise SystemExit(f"No states found under: {_safe_rel(day_dir)}")

    profile = str(args.profile or "mixed").strip()
    rank_by = str(args.rank_by or ("profit_alerts" if profile in {"mixed", "profit_only"} else "tool_first")).strip()
    show_profit_alerts = profile in {"mixed", "profit_only"}

    out_suffix = "" if profile == "mixed" else f"__{profile}"

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else (runs_dir / f"{args.date}__PREDICTIVE_PORTFOLIO{out_suffix}.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Predictive portfolio already exists: {_safe_rel(out_path)} (use --force to overwrite).")

    # Build state rows.
    table_rows: List[Dict[str, Any]] = []
    for state_key in states:
        state_dir = day_dir / state_key
        alerts = _parse_profit_alerts_for_state(pa_rows, state_key=state_key) if show_profit_alerts else []
        packs_count, union_count, dd_canon, top_support_count, top_support = _load_candidate_universe_summary(
            state_dir, profile=profile
        )
        b12_boxed_count, b12_boxed, b12_combos, _, _, _ = _load_play_card_cut(
            state_dir, profile=profile, strategy="analysis_prefix", budget=12
        )
        b24_boxed_count, b24_boxed, b24_combos, b24_pack_index, b24_pack_combos, b24_src = _load_play_card_cut(
            state_dir, profile=profile, strategy="vtrac_pack_boxed_first", budget=24
        )
        b36_boxed_count, b36_boxed, b36_combos, b36_pack_index, b36_pack_combos, b36_src = _load_play_card_cut(
            state_dir, profile=profile, strategy="vtrac_pack_boxed_first", budget=36
        )

        top_alerts = alerts[: max(0, int(args.top_n_alerts))]
        top_strs: List[str] = []
        strength_sum = 0
        for a in top_alerts:
            strength_sum += int(a.strength)
            canon_label = a.canonical or (a.combos[0] if a.combos else "-")
            top_strs.append(f"{a.variant}:{a.alert_id}:{a.suggested}:{canon_label}({a.cost_units})")

        dd_show = dd_canon[: max(0, int(args.top_n_due_doubles))]
        b12_boxed_show = b12_boxed[:3]
        top_support_label = (
            f"{top_support_count}:{' '.join(top_support)}" if top_support_count and top_support else ("0" if packs_count else "-")
        )

        table_rows.append(
            {
                "StateKey": state_key,
                "alerts_count": len(alerts),
                "alerts_strength_sum_top": strength_sum,
                "alerts_top": "; ".join(top_strs) if top_strs else "-",
                "candidate_union": union_count,
                "candidate_packs": packs_count,
                "candidate_top_support": int(top_support_count),
                "candidate_top_support_label": top_support_label,
                "due_doubles_canon": " ".join(dd_show) if dd_show else "-",
                "due_doubles_count": len(dd_canon),
                "play_b12_boxed_count": int(b12_boxed_count),
                "play_b12_boxed": (
                    f"{b12_boxed_count}:{' '.join(b12_boxed_show)}" if b12_boxed_count else ("0" if b12_combos else "-")
                ),
                "play_b12_combos": " ".join(b12_combos),
                "play_b24_pack": _pack_label(b24_pack_index, b24_pack_combos),
                "play_b36_pack": _pack_label(b36_pack_index, b36_pack_combos),
                "play_b24_pack_combos": " ".join(b24_pack_combos) if b24_pack_combos else "-",
                "play_b36_pack_combos": " ".join(b36_pack_combos) if b36_pack_combos else "-",
                "play_b24_combos": " ".join(b24_combos),
                "play_b36_combos": " ".join(b36_combos),
                "play_b24_src": _safe_rel(b24_src) if b24_src else "-",
                "play_b36_src": _safe_rel(b36_src) if b36_src else "-",
                "play_b24_boxed_count": int(b24_boxed_count),
                "play_b36_boxed_count": int(b36_boxed_count),
            }
        )

    if rank_by == "profit_alerts":
        # Rank: more alerts + higher strength, then smaller candidate universe.
        table_rows.sort(
            key=lambda r: (
                -int(r["alerts_count"]),
                -int(r["alerts_strength_sum_top"]),
                int(r["candidate_union"]),
                str(r["StateKey"]),
            )
        )
    else:
        # Tool-first triage: prefer stronger low-cost closures and narrower universes.
        table_rows.sort(
            key=lambda r: (
                -int(r.get("candidate_top_support") or 0),
                int(r["candidate_union"]),
                -int(r.get("due_doubles_count") or 0),
                -int(r["candidate_packs"]),
                str(r["StateKey"]),
            )
        )

    # Render markdown.
    lines: List[str] = []
    lines.append(f"# Predictive Portfolio — D={args.date}")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Cross-state triage for a predictive day (pre-results).")
    lines.append(f"- Profile: `{profile}` | rank_by: `{rank_by}`")
    lines.append("- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.")
    lines.append("")
    lines.append("Evidence roots")
    lines.append(f"- Predictive sharepacks root: `{_safe_rel(sharepacks_root)}`")
    if show_profit_alerts:
        lines.append(f"- Control Center Profit Alerts: `{_safe_rel(pa_path)}`")
    else:
        lines.append(f"- Control Center Profit Alerts (excluded by profile): `{_safe_rel(pa_path)}`")
    lines.append(f"- Candidate Universe file: `candidate_universe{_profile_suffix(profile)}.json`")
    lines.append(f"- Play Card file(s): `play_card{_profile_suffix(profile)}*.json`")
    lines.append("")
    lines.append("## Portfolio table (ranked)")
    lines.append("")
    if show_profit_alerts:
        lines.append(
            "| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |"
        )
        lines.append("|---|---:|---:|---|---:|---:|---|---|---|---|---|")
    else:
        lines.append(
            "| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |"
        )
        lines.append("|---|---:|---:|---|---|---|---|---|")
    for r in table_rows:
        if show_profit_alerts:
            lines.append(
                "| {StateKey} | {alerts_count} | {alerts_strength_sum_top} | {alerts_top} | {candidate_packs} | {candidate_union} | {candidate_top_support_label} | {due_doubles_canon} | {play_b12_boxed} | {play_b24_pack} | {play_b36_pack} |".format(
                    **r
                )
            )
        else:
            lines.append(
                "| {StateKey} | {candidate_packs} | {candidate_union} | {candidate_top_support_label} | {due_doubles_canon} | {play_b12_boxed} | {play_b24_pack} | {play_b36_pack} |".format(
                    **r
                )
            )
    lines.append("")
    lines.append("## Play cards (defaults)")
    lines.append("")
    lines.append("These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).")
    lines.append("")
    lines.append("v0.2 posture (budget-split):")
    lines.append("- B12 uses `analysis_prefix` (conservative / diagnostic-first).")
    lines.append("- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).")
    lines.append("")
    lines.append("### B12 (analysis_prefix)")
    for r in table_rows:
        combos = str(r.get("play_b12_combos") or "").strip()
        if not combos:
            continue
        lines.append(f"- **{r['StateKey']}**: `{combos}`")
    lines.append("")
    lines.append("### B24/B36 VTRAC pack picks")
    lines.append("")
    lines.append("Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.")
    lines.append("")
    for r in table_rows:
        b24_pack = str(r.get("play_b24_pack") or "").strip()
        b36_pack = str(r.get("play_b36_pack") or "").strip()
        b24_pack_combos = str(r.get("play_b24_pack_combos") or "").strip()
        b36_pack_combos = str(r.get("play_b36_pack_combos") or "").strip()
        b24_src = str(r.get("play_b24_src") or "").strip()
        b36_src = str(r.get("play_b36_src") or "").strip()
        if b24_pack == "-" and b36_pack == "-":
            continue
        if b24_pack == b36_pack and b24_pack_combos == b36_pack_combos:
            src = b24_src if b24_src and b24_src != "-" else b36_src
            lines.append(f"- **{r['StateKey']}**: `idx(size)={b24_pack}` pack=`{b24_pack_combos or '-'}` (src: `{src}`)")
        else:
            lines.append(
                f"- **{r['StateKey']}**: B24 `idx(size)={b24_pack}` pack=`{b24_pack_combos or '-'}` (src: `{b24_src}`) | "
                f"B36 `idx(size)={b36_pack}` pack=`{b36_pack_combos or '-'}` (src: `{b36_src}`)"
            )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.")
    lines.append("- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:")
    lines.append(f"  - `{_safe_rel(cc_dir / 'profit_alerts.csv')}` (bet-ready implied sets; included only for mixed/profit_only)")
    lines.append(f"  - `sharepacks/_predictive/{args.date}/<STATE>/candidate_universe{_profile_suffix(profile)}.json` (gradeable playset)")
    lines.append(f"  - `sharepacks/_predictive/{args.date}/<STATE>/play_card{_profile_suffix(profile)}*.json` (budgeted cuts)")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {_safe_rel(out_path)}")


if __name__ == "__main__":
    main()
