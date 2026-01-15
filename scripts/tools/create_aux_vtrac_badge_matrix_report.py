#!/usr/bin/env python3
"""
Create an Aux "boxed VTRAC badge matrix" export for a sharepack day.

This is a reporting-only tool:
- Reads ONLY sharepack-local Aux draw snapshots + Aux summary.json.
- Computes the per-index boxed VTRAC table badges (pair colors + combo DS badges)
  using the existing Aux logic (`modules.analyze_pairs.get_vtrac_statuses`).
- Writes outputs ONLY to RUNS (or explicit output paths), never into sharepacks.

Why this exists
--------------
Older Aux UX relied on the "boxed VTRAC matrix" (index rows with per-combo badges)
to spot dense pressure inside a vtrac_index and to compound across variants (C/M/E).

Sharepacks already capture:
- pair overdue buckets,
- vtrac overlay/heatboard,
- due_doubles board (by VTRAC double-family),
but they do not export the full per-index combo badge matrix.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from modules.analyze_pairs import get_vtrac_statuses  # noqa: E402
from modules.vtrac_reference import VTRAC_DISPLAY  # noqa: E402

VARIANTS: Tuple[str, ...] = ("combined", "midday", "evening")


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


def _normalize_pick3(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _read_draws_csv(path: Path, *, max_n: int = 1000) -> List[str]:
    if not path.exists():
        return []
    out: List[str] = []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        for row in csv.reader(f):
            if not row:
                continue
            val = _normalize_pick3(row[0])
            if val:
                out.append(val)
            if max_n and len(out) >= max_n:
                break
    return out


def _vtrac_display_entries() -> List[dict]:
    out = []
    for entry in VTRAC_DISPLAY:
        try:
            idx = int(entry.get("Index"))
        except Exception:
            continue
        singles = str(entry.get("Singles") or "").strip()
        doubles = str(entry.get("Doubles") or "").strip()
        out.append(
            {
                "index": idx,
                "singles": [c for c in singles.split() if _normalize_pick3(c)],
                "doubles": [c for c in doubles.split() if _normalize_pick3(c)],
            }
        )
    return out


def _badge_letter(color: str) -> str:
    c = (color or "").strip().lower()
    if c == "red":
        return "R"
    if c == "blue":
        return "B"
    if c == "purple":
        return "P"
    return ""


def _combo_token(*, combo: str, color: str, shape: str, draws_since: Optional[int]) -> str:
    badge = _badge_letter(color)
    parts: List[str] = []
    if badge:
        parts.append(badge)
    if shape:
        parts.append(shape)
    if draws_since is not None and shape:
        parts.append(str(int(draws_since)))
    if not parts:
        return combo
    return f"{combo}({','.join(parts)})"


def _shape_from_status(status: dict) -> str:
    if status.get("shape_red_circle"):
        return "RC"
    if status.get("shape_blue_square"):
        return "BS"
    return ""


def _index_style_label(style: dict) -> str:
    bg = (style.get("bg") or "").strip()
    rank = style.get("rank")
    if bg == "green" and rank:
        return f"recent#{int(rank)}"
    if bg == "red" and rank:
        return f"overdue#{int(rank)}"
    return ""


def _variant_title(v: str) -> str:
    return v.title() if v else "?"


def _load_states_from_meta(day_dir: Path) -> List[str]:
    meta = day_dir / "control_center" / "meta.json"
    if not meta.exists():
        return []
    try:
        payload = _read_json(meta)
    except Exception:
        return []
    if not isinstance(payload, dict):
        return []
    states = payload.get("states")
    if not isinstance(states, list):
        return []
    out = []
    for s in states:
        if isinstance(s, dict):
            key = str(s.get("state_key") or "").strip()
            if key:
                out.append(key)
    return out


def _overlay_map(aux_summary: dict, variant: str) -> Dict[int, int]:
    vtrac = aux_summary.get("vtrac") if isinstance(aux_summary, dict) else {}
    overlay_top = (vtrac or {}).get("overlay_top") if isinstance(vtrac, dict) else {}
    rows = overlay_top.get(variant) if isinstance(overlay_top, dict) else None
    out: Dict[int, int] = {}
    if isinstance(rows, list):
        for r in rows:
            if not isinstance(r, dict):
                continue
            try:
                idx = int(r.get("index"))
                ds = int(r.get("draws_since"))
            except Exception:
                continue
            out[idx] = ds
    return out


def _resolved_draw_path(aux_summary: dict, variant: str) -> Optional[Path]:
    draw_sources = aux_summary.get("draw_sources") if isinstance(aux_summary, dict) else {}
    snapshot = (draw_sources or {}).get("snapshot") if isinstance(draw_sources, dict) else {}
    payload = snapshot.get(variant) if isinstance(snapshot, dict) else None
    if not isinstance(payload, dict):
        return None
    resolved = str(payload.get("resolved_path") or "").strip()
    if not resolved:
        return None
    return Path(resolved)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export the Aux boxed VTRAC badge matrix for a sharepack day.")
    p.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    p.add_argument(
        "--sharepacks-root",
        default=str(REPO_ROOT / "sharepacks"),
        help="Sharepacks root directory (default: sharepacks/)",
    )
    p.add_argument("--states", nargs="*", help="Optional subset of states (default: day meta tracked list)")
    p.add_argument(
        "--top-indices",
        type=int,
        default=10,
        help="How many overdue indices (per variant) to include in the Markdown report per state (default: 10)",
    )
    p.add_argument("--out-md", default=None, help="Override Markdown output path (default: RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.md)")
    p.add_argument("--out-csv", default=None, help="Override CSV output path (default: RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.csv)")
    p.add_argument("--force", action="store_true", help="Overwrite outputs if they already exist.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    day_dir = sharepacks_root / str(args.date).strip()
    if not day_dir.exists():
        raise SystemExit(f"Sharepack day not found: {day_dir}")

    states = list(args.states) if args.states else _load_states_from_meta(day_dir)
    if not states:
        raise SystemExit("No states provided and could not infer from control_center/meta.json")

    out_md = Path(args.out_md) if args.out_md else (_runs_dir() / f"{args.date}__AUX_VTRAC_BADGE_MATRIX.md")
    out_csv = Path(args.out_csv) if args.out_csv else (_runs_dir() / f"{args.date}__AUX_VTRAC_BADGE_MATRIX.csv")
    if not args.force:
        for pth in (out_md, out_csv):
            if pth.exists():
                raise SystemExit(f"Refusing to overwrite existing output: {pth} (use --force)")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    vtrac_entries = _vtrac_display_entries()

    csv_rows: List[Dict[str, str]] = []
    md_lines: List[str] = []

    md_lines.append(f"# Aux — Boxed VTRAC Badge Matrix — D={args.date}")
    md_lines.append("")
    md_lines.append("This is a reporting-only export built from sharepack-local Aux draw snapshots.")
    md_lines.append("")
    md_lines.append(f"- Sharepacks root: `{_safe_rel(sharepacks_root)}`")
    md_lines.append(f"- Day dir: `{_safe_rel(day_dir)}`")
    md_lines.append("")
    md_lines.append("Legend:")
    md_lines.append("- Pair color badges (from overdue-pair logic): `R`=very late, `B`=late, `P`=pending")
    md_lines.append("- Combo DS badges (from combo draws-since thresholds): `RC`=red circle, `BS`=blue square")
    md_lines.append("- Token format: `COMBO(R,RC,816)` means pair-color=R, shape=RC, combo draws-since=816 (ds printed only when shape exists)")
    md_lines.append("")

    for state_key in states:
        aux_path = day_dir / state_key / "aux" / state_key / "summary.json"
        if not aux_path.exists():
            md_lines.append(f"## {state_key}")
            md_lines.append("")
            md_lines.append(f"- Missing Aux summary: `{_safe_rel(aux_path)}`")
            md_lines.append("")
            continue

        aux_summary = _read_json(aux_path)
        if not isinstance(aux_summary, dict):
            md_lines.append(f"## {state_key}")
            md_lines.append("")
            md_lines.append(f"- Invalid Aux summary JSON: `{_safe_rel(aux_path)}`")
            md_lines.append("")
            continue

        md_lines.append(f"## {state_key}")
        md_lines.append("")
        md_lines.append(f"- Aux summary: `{_safe_rel(aux_path)}`")
        md_lines.append("")

        for variant in VARIANTS:
            draw_path = _resolved_draw_path(aux_summary, variant)
            if not draw_path or not draw_path.exists():
                md_lines.append(f"### {_variant_title(variant)}")
                md_lines.append("")
                md_lines.append(f"- Missing draw snapshot path for `{variant}`")
                md_lines.append("")
                continue

            draws = _read_draws_csv(draw_path, max_n=1000)
            if not draws:
                md_lines.append(f"### {_variant_title(variant)}")
                md_lines.append("")
                md_lines.append(f"- No draws found in: `{_safe_rel(draw_path)}`")
                md_lines.append("")
                continue

            with redirect_stdout(StringIO()):
                vstat = get_vtrac_statuses(draws[:100], draws[:1000])

            meta = vstat.get(0, {}) if isinstance(vstat, dict) else {}
            singles_ds = meta.get("singles_ds", {}) if isinstance(meta, dict) else {}
            doubles_ds = meta.get("doubles_ds", {}) if isinstance(meta, dict) else {}

            overlay = _overlay_map(aux_summary, variant)
            overlay_sorted = sorted(overlay.items(), key=lambda kv: kv[1], reverse=True)
            top_idx = [idx for idx, _ in overlay_sorted[: max(0, int(args.top_indices))]]

            md_lines.append(f"### {_variant_title(variant)}")
            md_lines.append("")
            md_lines.append(f"- Draw snapshot: `{_safe_rel(draw_path)}` (n={len(draws)})")
            if overlay_sorted:
                md_lines.append(
                    "- Aux overlay top: "
                    + ", ".join(f"{idx}:{ds}" for idx, ds in overlay_sorted[: min(10, len(overlay_sorted))])
                )
            md_lines.append("")
            md_lines.append("| idx | overlay_ds | row_style | singles (boxed) | doubles (boxed) |")
            md_lines.append("|---:|---:|---|---|---|")

            for entry in vtrac_entries:
                idx = int(entry["index"])
                show_in_md = (not top_idx) or (idx in top_idx)

                idx_payload = vstat.get(idx, {}) if isinstance(vstat, dict) else {}
                idx_style = _index_style_label(idx_payload.get("index_style", {}) if isinstance(idx_payload, dict) else {})
                overlay_ds = overlay.get(idx)

                singles_tokens: List[str] = []
                doubles_tokens: List[str] = []

                singles_status = idx_payload.get("singles_status", {}) if isinstance(idx_payload, dict) else {}
                doubles_status = idx_payload.get("doubles_status", {}) if isinstance(idx_payload, dict) else {}

                for combo in entry["singles"]:
                    base = "".join(sorted(combo))
                    ds = singles_ds.get(base)
                    status = singles_status.get(combo, {}) if isinstance(singles_status, dict) else {}
                    color = str(status.get("color") or "")
                    shape = _shape_from_status(status) if isinstance(status, dict) else ""
                    singles_tokens.append(_combo_token(combo=combo, color=color, shape=shape, draws_since=ds))

                    csv_rows.append(
                        {
                            "date": str(args.date),
                            "sharepacks_root": _safe_rel(sharepacks_root),
                            "state_key": state_key,
                            "variant": variant,
                            "vtrac_index": str(idx),
                            "combo_type": "single",
                            "combo": combo,
                            "combo_base": base,
                            "overlay_draws_since": str(overlay_ds) if overlay_ds is not None else "",
                            "pair_color": color,
                            "shape": shape,
                            "combo_draws_since": str(ds) if ds is not None else "",
                            "row_style": idx_style,
                        }
                    )

                for combo in entry["doubles"]:
                    base = "".join(sorted(combo))
                    ds = doubles_ds.get(base)
                    status = doubles_status.get(combo, {}) if isinstance(doubles_status, dict) else {}
                    color = str(status.get("color") or "")
                    shape = _shape_from_status(status) if isinstance(status, dict) else ""
                    doubles_tokens.append(_combo_token(combo=combo, color=color, shape=shape, draws_since=ds))

                    csv_rows.append(
                        {
                            "date": str(args.date),
                            "sharepacks_root": _safe_rel(sharepacks_root),
                            "state_key": state_key,
                            "variant": variant,
                            "vtrac_index": str(idx),
                            "combo_type": "double",
                            "combo": combo,
                            "combo_base": base,
                            "overlay_draws_since": str(overlay_ds) if overlay_ds is not None else "",
                            "pair_color": color,
                            "shape": shape,
                            "combo_draws_since": str(ds) if ds is not None else "",
                            "row_style": idx_style,
                        }
                    )

                if show_in_md:
                    md_lines.append(
                        "| {idx} | {ods} | {sty} | {sing} | {dbl} |".format(
                            idx=idx,
                            ods=str(overlay_ds) if overlay_ds is not None else "",
                            sty=idx_style,
                            sing=" ".join(singles_tokens) if singles_tokens else "·",
                            dbl=" ".join(doubles_tokens) if doubles_tokens else "·",
                        )
                    )

            md_lines.append("")

    out_md.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")

    if csv_rows:
        fieldnames = list(csv_rows[0].keys())
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(csv_rows)
    else:
        out_csv.write_text("", encoding="utf-8")

    print(f"[OK] Wrote: {_safe_rel(out_md)}")
    print(f"[OK] Wrote: {_safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
