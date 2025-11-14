#!/usr/bin/env python3
"""
Prototype winners log builder.

Reads Stable sharepacks (brain + winners lens) plus the packaged V-TRAC winner HTML
files for a given date and emits a consolidated CSV + JSON showing winner classes
and supporting evidence per state/variant.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass
class WinnerRecord:
    date: str
    state: str
    variant: str
    winner: str
    classes: dict[str, bool]
    stable_evidence: dict[str, Any]
    vtrac_evidence: dict[str, Any] | None

    def to_row(self) -> dict[str, Any]:
        flat = {
            "date": self.date,
            "state": self.state,
            "variant": self.variant,
            "winner": self.winner,
            "exact_straight": self.classes.get("exact_straight"),
            "exact_boxed": self.classes.get("exact_boxed"),
            "vt_boxed": self.classes.get("vt_boxed"),
            "vt_straight": self.classes.get("vt_straight"),
        }
        flat.update(
            {
                "best_compound_rank": self.stable_evidence.get("best_compound_rank"),
                "winner_family_rank": self.stable_evidence.get("winner_family_rank"),
                "vt_only_lane": self.stable_evidence.get("vt_only_lane"),
                "funnel_precol1": self.stable_evidence.get("funnel_precol1"),
            }
        )
        if self.vtrac_evidence:
            flat["vtrac_index"] = self.vtrac_evidence.get("vt_index")
            flat["vtrac_source"] = self.vtrac_evidence.get("source")
        else:
            flat["vtrac_index"] = None
            flat["vtrac_source"] = None
        return flat


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build consolidated winners log from sharepacks.")
    parser.add_argument("--date", required=True, help="Date folder under sharepacks/, e.g. 2025-06-24")
    parser.add_argument("--states", nargs="*", help="Optional subset of states to include.")
    parser.add_argument(
        "--sharepacks-root",
        default="sharepacks",
        help="Root directory containing dated sharepack folders (default: sharepacks)",
    )
    parser.add_argument(
        "--out-dir",
        default="winners",
        help="Directory to write consolidated outputs (default: winners)",
    )
    return parser.parse_args()


def read_vtrac_hits(winners_dir: Path) -> dict[str, dict[str, str]]:
    hits: dict[str, dict[str, str]] = {}
    if not winners_dir.exists():
        return hits
    for html_path in sorted(winners_dir.glob("*_winner_*.html")):
        parts = html_path.stem.split("_")
        if len(parts) < 4 or not parts[1].startswith("vtrac"):
            continue
        winner = parts[3]
        vt_index = parts[1].replace("vtrac", "")
        hits[winner] = {
            "vt_index": vt_index,
            "source": str(html_path),
        }
    return hits


def canonicalize(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return "".join(sorted(digits))


def build_records_for_state(date: str, state_dir: Path, state: str) -> list[WinnerRecord]:
    stable_dir = state_dir / "stable"
    metrics_path = stable_dir / f"{state}_metrics.json"
    compound_path = stable_dir / f"{state}_stable_patterns_compound.csv"
    spotlight_path = stable_dir / f"{state}_winner_family_spotlight_raw.csv"
    winners_dir = state_dir / "winners"

    if not metrics_path.exists() or not compound_path.exists():
        return []

    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    compound = pd.read_csv(compound_path)
    spotlight_mid = ""
    spotlight_eve = ""
    if spotlight_path.exists():
        spotlight = pd.read_csv(spotlight_path)
        if "winner_literal_midday" in spotlight:
            spotlight_mid = str(
                next((v for v in spotlight["winner_literal_midday"].tolist() if str(v).strip()), "")
            )
        if "winner_literal_evening" in spotlight:
            spotlight_eve = str(
                next((v for v in spotlight["winner_literal_evening"].tolist() if str(v).strip()), "")
            )

    variant_map = {
        "Midday": spotlight_mid,
        "Evening": spotlight_eve,
    }
    vtrac_hits = read_vtrac_hits(winners_dir)

    family_ranks = metrics.get("winner_family_best_rank") or {}
    best_comp = metrics.get("best_compound_rank") or {}
    hits = metrics.get("winner_hits") or {}

    combined = compound[compound["section"].astype(str).str.lower() == "combined"]
    records: list[WinnerRecord] = []

    for variant, winner in variant_map.items():
        winner = str(winner).strip()
        if not winner:
            continue
        canonical = canonicalize(winner)
        comp_row = combined.loc[combined["Canonical"].astype(str) == canonical]
        row = comp_row.iloc[0] if not comp_row.empty else None

        evidence = {
            "best_compound_rank": best_comp.get(winner),
            "winner_family_rank": family_ranks.get(winner),
            "vt_only_lane": bool(row["vt_only_lane"]) if row is not None and "vt_only_lane" in row else None,
            "funnel_precol1": int(row["funnel_precol1"])
            if row is not None and "funnel_precol1" in row and not pd.isna(row["funnel_precol1"])
            else None,
        }

        classes = {
            "exact_straight": bool(hits.get(winner, {}).get("exact_straight")),
            "exact_boxed": bool(hits.get(winner, {}).get("exact_boxed")),
            "vt_boxed": bool(hits.get(winner, {}).get("vtrac_boxed")),
            "vt_straight": bool(row["vtrac_straight_hits"]) if row is not None and "vtrac_straight_hits" in row else False,
        }

        record = WinnerRecord(
            date=date,
            state=state,
            variant=variant,
            winner=winner,
            classes=classes,
            stable_evidence=evidence,
            vtrac_evidence=vtrac_hits.get(winner),
        )
        records.append(record)

    return records


def main() -> None:
    args = parse_args()
    date = args.date
    sharepack_root = Path(args.sharepacks_root) / date
    if not sharepack_root.exists():
        raise SystemExit(f"Sharepack folder {sharepack_root} does not exist")

    target_states = set(args.states or [])
    records: list[WinnerRecord] = []
    for state_dir in sorted(p for p in sharepack_root.iterdir() if p.is_dir()):
        state = state_dir.name
        if target_states and state not in target_states:
            continue
        records.extend(build_records_for_state(date, state_dir, state))

    out_dir = Path(args.out_dir) / date
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{date}_winners_map.json"
    csv_path = out_dir / f"{date}_winners_map.csv"

    json_payload = [
        {
            "date": rec.date,
            "state": rec.state,
            "variant": rec.variant,
            "winner": rec.winner,
            "classes": rec.classes,
            "stable": rec.stable_evidence,
            "vtrac": rec.vtrac_evidence,
        }
        for rec in records
    ]
    json_path.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")

    df = pd.DataFrame([rec.to_row() for rec in records])
    df.to_csv(csv_path, index=False)

    print(f"Wrote {len(records)} winner rows to {json_path} and {csv_path}")


if __name__ == "__main__":
    main()
