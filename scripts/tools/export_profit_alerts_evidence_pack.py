#!/usr/bin/env python3
"""
Export a small, GitHub-visible evidence pack for Profit Alerts manual audits / Deep Research.

Why this exists:
- Root `sharepacks/` are intentionally gitignored (large, local).
- Deep Research agents (and collaborators) can't see your local filesystem sharepacks.
- This script copies only the minimal evidence needed for a bounded set of cases
  into `docs/.../PACKAGES/...`, preserving a sharepack-like folder layout.

Inputs:
- A `CASES.csv` produced by `scripts/tools/create_profit_alerts_casebook.py`.
- The local `sharepacks/<D>/...` corpus for the referenced dates/states.

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__<A>_to_<B>__<STAMP>__<LABEL>/...`
  containing:
  - a mirror of the minimal `sharepacks/<D>/...` files needed,
  - a casebook that points to the mirror (not the local sharepacks),
  - stable evidence excerpts for referenced stable locators.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import shutil
from dataclasses import dataclass
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]


def clean_label(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    out = []
    for ch in raw.replace(" ", "_"):
        if ch.isalnum() or ch in {"_", "-"}:
            out.append(ch)
    cleaned = "".join(out).strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --label: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def iter_files(dir_path: Path, *, suffixes: Sequence[str]) -> Iterable[Path]:
    if not dir_path.exists():
        return []
    for p in sorted(dir_path.iterdir()):
        if p.is_file() and any(p.name.endswith(s) for s in suffixes):
            yield p


@dataclass(frozen=True)
class CaseRow:
    case_num: str
    kind: str
    results_date: str
    state_key: str
    variant: str
    alert_id: str
    row_num: str
    status: str
    strength: str
    suggested: str
    canonical: str
    implied_set_size: str
    decay_draws: str
    badges: str
    strict_hit: str
    hit_within_decay: str
    hit_any_within_decay: str
    hit_within_7: str
    hit_within_14: str
    hit_type: str
    hit_any_type: str
    stable_scores_relpath: str
    stable_section: str
    stable_set: str
    stable_draw: str
    stable_column: str
    stable_family_id: str
    stable_why: str
    stub_section: str
    stub_set: str
    stub_draw: str
    stub_column: str
    stub_canonical: str
    vtrac_index: str

    @staticmethod
    def from_dict(row: Dict[str, str]) -> "CaseRow":
        def g(k: str) -> str:
            return (row.get(k) or "").strip()

        return CaseRow(
            case_num=g("case_num"),
            kind=g("kind"),
            results_date=g("results_date"),
            state_key=g("state_key"),
            variant=g("variant"),
            alert_id=g("alert_id"),
            row_num=g("row_num"),
            status=g("status"),
            strength=g("strength"),
            suggested=g("suggested"),
            canonical=g("canonical"),
            implied_set_size=g("implied_set_size"),
            decay_draws=g("decay_draws"),
            badges=g("badges"),
            strict_hit=g("strict_hit"),
            hit_within_decay=g("hit_within_decay"),
            hit_any_within_decay=g("hit_any_within_decay"),
            hit_within_7=g("hit_within_7"),
            hit_within_14=g("hit_within_14"),
            hit_type=g("hit_type"),
            hit_any_type=g("hit_any_type"),
            stable_scores_relpath=g("stable_scores_relpath"),
            stable_section=g("stable_section"),
            stable_set=g("stable_set"),
            stable_draw=g("stable_draw"),
            stable_column=g("stable_column"),
            stable_family_id=g("stable_family_id"),
            stable_why=g("stable_why"),
            stub_section=g("stub_section"),
            stub_set=g("stub_set"),
            stub_draw=g("stub_draw"),
            stub_column=g("stub_column"),
            stub_canonical=g("stub_canonical"),
            vtrac_index=g("vtrac_index"),
        )


def read_cases(path: Path) -> List[CaseRow]:
    if not path.exists():
        raise SystemExit(f"--cases-csv not found: {path}")
    out: List[CaseRow] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(CaseRow.from_dict(row))
    if not out:
        raise SystemExit(f"No rows in CASES.csv: {path}")
    return out


def stable_excerpt(
    *,
    src_scores: Path,
    dst_excerpt: Path,
    targets: List[Tuple[str, str, str, str, str]],
) -> bool:
    """
    Extract rows from stable_patterns_scores.csv matching any (section, Set, Draw, Column, Canonical).
    """
    if not src_scores.exists():
        return False
    if not targets:
        return False
    wanted = {(a, b, c, d, e) for a, b, c, d, e in targets}
    rows_out: List[Dict[str, str]] = []
    with src_scores.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        for row in reader:
            key = (
                (row.get("section") or "").strip(),
                (row.get("Set") or "").strip(),
                (row.get("Draw") or "").strip(),
                (row.get("Column") or "").strip(),
                (row.get("Canonical") or "").strip(),
            )
            if key in wanted:
                rows_out.append({k: (row.get(k) or "") for k in fieldnames})
    if not rows_out:
        return False
    dst_excerpt.parent.mkdir(parents=True, exist_ok=True)
    with dst_excerpt.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows_out[0].keys())
        writer.writeheader()
        writer.writerows(rows_out)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a minimal Profit Alerts evidence pack from a casebook CASES.csv.")
    parser.add_argument("--start", required=True, help="Window start date (YYYY-MM-DD) used for naming")
    parser.add_argument("--end", required=True, help="Window end date (YYYY-MM-DD) used for naming")
    parser.add_argument("--cases-csv", required=True, help="Path to CASES.csv produced by create_profit_alerts_casebook.py")
    parser.add_argument("--stamp", default=dt.date.today().isoformat(), help="Stamp used in output folder name")
    parser.add_argument("--label", default="", help="Optional label appended to output folder name (safe for reruns)")
    parser.add_argument("--sharepacks-dir", default=str(ROOT / "sharepacks"), help="Local sharepacks root directory")
    parser.add_argument(
        "--packages-dir",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "PACKAGES"),
        help="Packages output directory",
    )
    args = parser.parse_args()

    label = clean_label(args.label)
    stamp = (args.stamp or "").strip()
    if not stamp:
        raise SystemExit("--stamp must be non-empty")

    cases_csv = Path(args.cases_csv)
    cases = read_cases(cases_csv)

    sharepacks_root = Path(args.sharepacks_dir)
    packages_root = Path(args.packages_dir)
    packages_root.mkdir(parents=True, exist_ok=True)

    label_suffix = f"__{label}" if label else ""
    pack_dir = packages_root / f"profit_alerts_evidence_pack__{args.start}_to_{args.end}__{stamp}{label_suffix}"
    pack_dir.mkdir(parents=True, exist_ok=True)

    # Mirror base
    mirror_root = pack_dir / "sharepacks"

    # Copy CASES.csv in
    shutil.copy2(cases_csv, pack_dir / "CASES.csv")

    # Copy needed control_center + winners/json, and build stable excerpts.
    needed_dates = sorted({c.results_date for c in cases if c.results_date})
    needed_state_keys = sorted({(c.results_date, c.state_key) for c in cases if c.results_date and c.state_key})

    for d in needed_dates:
        src_cc = sharepacks_root / d / "control_center"
        dst_cc = mirror_root / d / "control_center"
        for name in [
            "profit_alerts.csv",
            "profit_alerts.md",
            "profit_alerts_eval.csv",
            "profit_alerts_eval.md",
            "profit_alerts_eval_merged.csv",
        ]:
            copy_if_exists(src_cc / name, dst_cc / name)

    # Stable excerpt targets by (date,state_key)
    targets_by_state: Dict[Tuple[str, str], List[Tuple[str, str, str, str, str]]] = defaultdict(list)
    for c in cases:
        if not (c.results_date and c.state_key and c.stable_section and c.stable_set and c.stable_draw and c.stable_column and c.canonical):
            continue
        targets_by_state[(c.results_date, c.state_key)].append((c.stable_section, c.stable_set, c.stable_draw, c.stable_column, c.canonical))

    for d, state_key in needed_state_keys:
        src_state = sharepacks_root / d / state_key
        dst_state = mirror_root / d / state_key

        # Winners (copy digest + all html/json in winners/<StateKey>/)
        src_winners_dir = src_state / "winners" / state_key
        dst_winners_dir = dst_state / "winners" / state_key
        copy_if_exists(src_winners_dir / "digest.md", dst_winners_dir / "digest.md")
        for p in iter_files(src_winners_dir, suffixes=(".html", ".json")):
            copy_if_exists(p, dst_winners_dir / p.name)

        # JSON tables snapshot
        src_json = src_state / "json" / f"{state_key}_tables.json"
        dst_json = dst_state / "json" / f"{state_key}_tables.json"
        copy_if_exists(src_json, dst_json)

        # Stable excerpt (if we have locators)
        src_scores = src_state / "stable" / state_key / f"{state_key}_stable_patterns_scores.csv"
        dst_scores_dir = dst_state / "stable" / state_key
        dst_excerpt = dst_scores_dir / f"{state_key}_stable_patterns_scores__profit_alerts_excerpt.csv"
        targets = targets_by_state.get((d, state_key), [])
        if stable_excerpt(src_scores=src_scores, dst_excerpt=dst_excerpt, targets=targets):
            write_text(
                dst_scores_dir / "README.md",
                "\n".join(
                    [
                        "# Stable excerpt",
                        "",
                        "This file contains only the Stable rows referenced by Profit Alerts cases in this evidence pack.",
                        "Match keys: (section, Set, Draw, Column, Canonical).",
                        "",
                        f"- Source: `{src_scores.as_posix()}`",
                        f"- Excerpt: `{dst_excerpt.relative_to(ROOT).as_posix()}`",
                    ]
                ),
            )

    # Write a pack-local casebook that points to the mirror paths.
    pack_rel = pack_dir.relative_to(ROOT).as_posix()
    lines: List[str] = []
    lines.append(f"# Profit Alerts Evidence Pack — {args.start} → {args.end}")
    lines.append("")
    lines.append("This pack is a GitHub-visible mirror of the minimal `sharepacks/<D>/...` files needed to inspect the selected Profit Alerts cases.")
    lines.append("")
    lines.append("Start here:")
    lines.append(f"- Cases: `{pack_rel}/CASES.csv`")
    lines.append("")
    lines.append("## Cases")
    lines.append("")
    for c in cases:
        d = c.results_date
        state_key = c.state_key
        lines.append(f"### Case {c.case_num} — {c.kind} — {c.alert_id} — {state_key} — {c.variant} — D=`{d}`")
        lines.append("")
        lines.append(f"- Status: `{c.status}` | Strength: `{c.strength}` | Suggested: `{c.suggested}` | Canonical: `{c.canonical or '-'}` | DecayDraws: `{c.decay_draws}` | Badges: `{c.badges}`")
        lines.append(f"- Eval: strict_hit=`{c.strict_hit}` hit_decay=`{c.hit_within_decay}` hit_any_decay=`{c.hit_any_within_decay}` hit_any<=7=`{c.hit_within_7}` hit_any<=14=`{c.hit_within_14}`")
        if c.hit_type or c.hit_any_type:
            lines.append(f"- Hit typing: hit_type=`{c.hit_type or '-'}` hit_any_type=`{c.hit_any_type or '-'}`")
        if c.stable_section or c.stable_set or c.stable_draw or c.stable_column:
            lines.append(
                f"- Stable locator: section=`{c.stable_section or '-'}` set=`{c.stable_set or '-'}` draw=`{c.stable_draw or '-'}` col=`{c.stable_column or '-'}` family_id=`{c.stable_family_id or '-'}`"
            )
        if c.stub_section or c.stub_set or c.stub_draw or c.stub_column:
            lines.append(
                f"- Consensus stub: section=`{c.stub_section or '-'}` set=`{c.stub_set or '-'}` draw=`{c.stub_draw or '-'}` col=`{c.stub_column or '-'}` canonical=`{c.stub_canonical or '-'}`"
            )
        lines.append("")
        lines.append("Files (mirrored inside this pack):")
        lines.append(f"- Eval row source: `{pack_rel}/sharepacks/{d}/control_center/profit_alerts_eval.csv` (row_num={c.row_num})")
        lines.append(f"- Profit board (md): `{pack_rel}/sharepacks/{d}/control_center/profit_alerts.md`")
        lines.append(f"- Profit board (csv): `{pack_rel}/sharepacks/{d}/control_center/profit_alerts.csv`")
        lines.append(f"- Eval merged sets: `{pack_rel}/sharepacks/{d}/control_center/profit_alerts_eval_merged.csv`")
        lines.append(f"- Winners digest: `{pack_rel}/sharepacks/{d}/{state_key}/winners/{state_key}/digest.md`")
        lines.append(f"- Winners HTML/JSON dir: `{pack_rel}/sharepacks/{d}/{state_key}/winners/{state_key}`")
        lines.append(f"- JSON tables: `{pack_rel}/sharepacks/{d}/{state_key}/json/{state_key}_tables.json`")
        if c.stable_section or c.stable_set or c.stable_draw or c.stable_column:
            lines.append(
                f"- Stable excerpt: `{pack_rel}/sharepacks/{d}/{state_key}/stable/{state_key}/{state_key}_stable_patterns_scores__profit_alerts_excerpt.csv`"
            )
        lines.append("")

    write_text(pack_dir / "CASEBOOK.md", "\n".join(lines))
    write_text(
        pack_dir / "README.md",
        "\n".join(
            [
                "# Profit Alerts Evidence Pack",
                "",
                "This package is generated by `scripts/tools/export_profit_alerts_evidence_pack.py`.",
                "It mirrors a small subset of sharepack evidence into a GitHub-visible folder so Deep Research can inspect it.",
                "",
                "Entry points:",
                f"- `CASEBOOK.md`",
                f"- `CASES.csv`",
                "",
            ]
        ),
    )

    print(f"Wrote: {pack_dir / 'README.md'}")
    print(f"Wrote: {pack_dir / 'CASEBOOK.md'}")
    print(f"Wrote: {pack_dir / 'CASES.csv'}")
    print(f"Wrote mirror under: {mirror_root}")


if __name__ == "__main__":
    main()
