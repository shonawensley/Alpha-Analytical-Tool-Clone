from __future__ import annotations

import csv
import datetime as dt
import itertools
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from . import io

_MIRROR = {
    "0": "5",
    "1": "6",
    "2": "7",
    "3": "8",
    "4": "9",
    "5": "0",
    "6": "1",
    "7": "2",
    "8": "3",
    "9": "4",
}


def _digits(value: str) -> List[str]:
    return [c for c in value if c.isdigit()]


def _canon3(value: str) -> str:
    digits = _digits(value)
    if len(digits) < 3:
        return ""
    return "".join(sorted(digits[:3]))


def _canon_permutations(value: str) -> List[str]:
    canon = _canon3(value)
    if len(canon) != 3:
        return []
    return list({"".join(p) for p in itertools.permutations(canon)})


def _vtrac_local_key(value: str) -> Tuple[int, int, int]:
    digits = _digits(value)
    if len(digits) < 3:
        return (-1, -1, -1)
    raw = []
    for ch in digits[:3]:
        d = int(ch)
        m = int(_MIRROR[ch])
        raw.append(min(d, m))
    raw.sort()
    return tuple(raw)


def _vtrac_local_index(value: str) -> int:
    a, b, c = _vtrac_local_key(value)
    if a < 0:
        return -1
    return a * 25 + b * 5 + c


@dataclass
class WinnerSpec:
    combo: str
    variant: str = "Combined"
    when: Optional[str] = None

    @property
    def canon(self) -> str:
        return _canon3(self.combo)

    @property
    def permutations(self) -> List[str]:
        return _canon_permutations(self.combo)

    @property
    def vtrac_index(self) -> int:
        return _vtrac_local_index(self.combo)


def _analysis_digit_reduction_root(state: str, analysis_root: Path) -> Path:
    return analysis_root / "digit_reduction" / state


def _stacked_html_path(state: str, analysis_root: Path) -> Path:
    return _analysis_digit_reduction_root(state, analysis_root) / f"{state}_digit_reduction_report_stacked.html"


def _training_json_latest(state: str, analysis_root: Path) -> Optional[Path]:
    training_dir = _analysis_digit_reduction_root(state, analysis_root) / "training"
    if not training_dir.exists():
        return None
    candidates = sorted(training_dir.glob("*_digit_reduction_logs.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def _iter_items(training_json: Path) -> Iterable[Dict[str, Any]]:
    payload = json.loads(training_json.read_text(encoding="utf-8"))
    for item in payload.get("items", []):
        yield item


def _winner_item(view: Dict[str, Any], spec: WinnerSpec) -> Dict[str, Any]:
    steps = view.get("steps", [])
    final = view.get("final", {})

    steps_coerced = []
    for step in steps:
        val = step.get("value", "")
        steps_coerced.append(
            {
                "step": step.get("step"),
                "value": val,
                "canon": _canon3(val),
                "vtrac_local_index": _vtrac_local_index(val),
            }
        )

    def _earliest(field: str) -> int:
        best = None
        for step in steps_coerced:
            step_no = step.get("step")
            if not isinstance(step_no, int):
                continue
            if field == "canon" and step.get("canon") == spec.canon:
                best = step_no if best is None else min(best, step_no)
            elif field == "vtrac" and step.get("vtrac_local_index") == spec.vtrac_index:
                best = step_no if best is None else min(best, step_no)
        return best if best is not None else -1

    final_value = final.get("value", "")
    final_canon = _canon3(final_value)
    final_local_index = _vtrac_local_index(final_value)

    return {
        "state": view.get("state"),
        "area": view.get("area"),
        "section": view.get("section"),
        "set": view.get("set"),
        "draw": view.get("draw"),
        "col": view.get("col"),
        "method": view.get("method"),
        "mode": view.get("mode"),
        "earliest_exact_step": _earliest("canon"),
        "earliest_vtrac_step": _earliest("vtrac"),
        "final_value": final_value,
        "final_exact_match": final_canon == spec.canon,
        "final_vtrac_match": final_local_index == spec.vtrac_index and spec.vtrac_index >= 0,
        "final_vtrac_local_index": final_local_index,
    }


def build_winner_map(training_json: Path, spec: WinnerSpec, *, variant: str) -> Dict[str, Any]:
    items = []
    for view in _iter_items(training_json):
        if variant != "Combined" and view.get("section") != variant:
            continue
        row = _winner_item(view, spec)
        if (
            row.get("earliest_exact_step", -1) >= 0
            or row.get("earliest_vtrac_step", -1) >= 0
            or row.get("final_exact_match")
            or row.get("final_vtrac_match")
        ):
            items.append(row)
    return {
        "winner": spec.combo,
        "winner_canon": spec.canon,
        "winner_permutations": spec.permutations,
        "vtrac_local_index": spec.vtrac_index,
        "variant": variant,
        "generated_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "items": items,
    }


def _highlight_html(html: str, spec: WinnerSpec) -> str:
    perms = set(spec.permutations)
    if not perms:
        return html
    v_index = spec.vtrac_index

    def repl(match: re.Match[str]) -> str:
        token = match.group(0)
        canon = _canon3(token)
        if canon in perms:
            return f'<span class="dr-winner-exact">{token}</span>'
        if v_index >= 0 and _vtrac_local_index(token) == v_index:
            return f'<span class="dr-winner-vtrac">{token}</span>'
        return token

    return re.sub(r"\b\d{3}\b", repl, html)


def annotate_stacked_html(state: str, spec: WinnerSpec, *, variant: str, analysis_root: Path, stamp: str) -> Optional[Path]:
    stacked = _stacked_html_path(state, analysis_root)
    if not stacked.exists():
        return None
    html = stacked.read_text(encoding="utf-8")
    annotated = _highlight_html(html, spec)

    banner = (
        f"<!-- Digit Reduction winner overlay: state={state} variant={variant} winner={spec.combo} vtrac={spec.vtrac_index} -->\n"
        "<style>\n"
        ".dr-winner-exact { background: rgba(255, 215, 0, 0.85); color: #111; padding: 0 2px; border-radius: 2px; }\n"
        ".dr-winner-vtrac { background: rgba(255, 140, 0, 0.5); color: #111; padding: 0 2px; border-radius: 2px; }\n"
        "</style>\n"
        f"<div style='border:1px solid #666;padding:8px;margin:12px 0;background:#1b1b1b;color:#eee;'>\n"
        f"<strong>Digit Reduction — Winner Overlay</strong><br/>"
        f"state: {state} | variant: {variant} | winner: {spec.combo} | vtrac local index: {spec.vtrac_index} | generated: {dt.datetime.utcnow().isoformat(timespec='seconds')}Z"
        "</div>\n"
    )

    outdir = _analysis_digit_reduction_root(state, analysis_root) / "analyzer_v2" / "winners"
    outdir.mkdir(parents=True, exist_ok=True)
    overlay_path = outdir / f"{stamp}_{variant}_winner_overlay.html"
    overlay_path.write_text(banner + annotated, encoding="utf-8")
    return overlay_path


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _write_hits_csv(path: Path, wmap: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = [
        "state",
        "area",
        "section",
        "set",
        "draw",
        "col",
        "method",
        "mode",
        "earliest_exact_step",
        "earliest_vtrac_step",
        "final_value",
        "final_exact_match",
        "final_vtrac_match",
        "final_vtrac_local_index",
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        for item in wmap.get("items", []):
            writer.writerow([item.get(col, "") for col in header])


def run_winner_overlay(
    state: str,
    winner_combo: str,
    *,
    variant: str = "Combined",
    analysis_root: Optional[Path] = None,
    when: Optional[str] = None,
) -> Dict[str, Any]:
    analysis_root = Path(analysis_root) if analysis_root is not None else Path("data/outputs/analysis")
    training_json = _training_json_latest(state, analysis_root)
    if training_json is None:
        raise FileNotFoundError(f"No training JSON found for state {state}")

    spec = WinnerSpec(combo=winner_combo, variant=variant, when=when)
    stamp = when or dt.datetime.utcnow().strftime("%Y%m%d")

    wmap = build_winner_map(training_json, spec, variant=variant)

    outdir = _analysis_digit_reduction_root(state, analysis_root) / "analyzer_v2" / "winners"
    outdir.mkdir(parents=True, exist_ok=True)

    map_path = outdir / f"{stamp}_{variant}_winner_map.json"
    hits_path = outdir / f"{stamp}_{variant}_winner_hits.csv"
    _write_json(map_path, wmap)
    _write_hits_csv(hits_path, wmap)

    overlay_path = annotate_stacked_html(state, spec, variant=variant, analysis_root=analysis_root, stamp=stamp)

    return {
        "state": state,
        "variant": variant,
        "winner": winner_combo,
        "winner_map_json": str(map_path),
        "winner_hits_csv": str(hits_path),
        "overlay_html": str(overlay_path) if overlay_path else None,
        "hit_count": len(wmap.get("items", [])),
    }
# ---------------------------------------------------------------------------
# Part 2 extensions: batch overlays, flags, and winners stamps
# ---------------------------------------------------------------------------

from typing import Literal

Variant = Literal["Combined", "Midday", "Evening"]


def _ensure(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _counts_from_map(wmap: Dict[str, Any]) -> Dict[str, int]:
    items = wmap.get("items", [])
    return {
        "items_total": len(items),
        "items_exact_any": sum(1 for r in items if (r.get("earliest_exact_step", -1) >= 0 or r.get("final_exact_match"))),
        "items_vtrac_any": sum(1 for r in items if (r.get("earliest_vtrac_step", -1) >= 0 or r.get("final_vtrac_match"))),
        "final_exact": sum(1 for r in items if r.get("final_exact_match")),
        "final_vtrac": sum(1 for r in items if r.get("final_vtrac_match")),
    }


def _earliest_from_items(items: List[Dict[str, Any]], key: str) -> int:
    candidates = [int(r.get(key, -1)) for r in items if int(r.get(key, -1)) >= 0]
    return min(candidates) if candidates else -1


def _write_flags_csv(outdir: Path, stamp: str, variant: Variant, wmap: Dict[str, Any]) -> Path:
    path = _ensure(outdir / f"{stamp}_{variant}_winner_flags.csv")
    header = [
        "area",
        "section",
        "set",
        "draw",
        "col",
        "method",
        "mode",
        "dr_win_exact",
        "dr_win_vtrac",
        "dr_win_step_exact",
        "dr_win_step_vtrac",
        "dr_win_final_value",
        "dr_win_vtrac_local_index",
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        for row in wmap.get("items", []):
            writer.writerow([
                row.get("area", ""),
                row.get("section", ""),
                row.get("set", ""),
                row.get("draw", ""),
                row.get("col", ""),
                row.get("method", ""),
                row.get("mode", ""),
                1 if (row.get("earliest_exact_step", -1) >= 0 or row.get("final_exact_match")) else 0,
                1 if (row.get("earliest_vtrac_step", -1) >= 0 or row.get("final_vtrac_match")) else 0,
                int(row.get("earliest_exact_step", -1)),
                int(row.get("earliest_vtrac_step", -1)),
                row.get("final_value", ""),
                int(row.get("final_vtrac_local_index", -1)),
            ])
    return path


def _write_stamp_json(
    state: str,
    variant: Variant,
    spec: WinnerSpec,
    wmap: Dict[str, Any],
    *,
    analysis_root: Path,
    stamp: str,
    overlay_html: Optional[Path],
    map_path: Path,
    hits_path: Path,
    flags_path: Path,
    mirror_to_winners: bool,
) -> Dict[str, Any]:
    items = wmap.get("items", [])
    payload = {
        "tool": "digit_reduction",
        "state": state,
        "variant": variant,
        "winner": spec.combo,
        "winner_canon": spec.canon,
        "vtrac_local_index": spec.vtrac_index,
        "generated_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "counts": _counts_from_map(wmap),
        "earliest": {
            "exact_step_min": _earliest_from_items(items, "earliest_exact_step"),
            "vtrac_step_min": _earliest_from_items(items, "earliest_vtrac_step"),
        },
        "paths": {
            "overlay_html": str(overlay_html) if overlay_html else None,
            "winner_map_json": str(map_path),
            "winner_hits_csv": str(hits_path),
            "winner_flags_csv": str(flags_path),
        },
        "sample": [
            {
                "loc": {key: row.get(key, "") for key in ["area", "section", "set", "draw", "col", "method", "mode"]},
                "earliest_exact_step": int(row.get("earliest_exact_step", -1)),
                "final_exact_match": bool(row.get("final_exact_match")),
                "earliest_vtrac_step": int(row.get("earliest_vtrac_step", -1)),
                "final_vtrac_match": bool(row.get("final_vtrac_match")),
                "final_value": row.get("final_value", ""),
            }
            for row in items[:12]
        ],
    }

    stamps_dir = _analysis_digit_reduction_root(state, analysis_root) / "analyzer_v2" / "winners"
    stamp_path = _ensure(stamps_dir / f"{stamp}_{variant}_winner_stamp.json")
    stamp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    winners_stamp_path = None
    if mirror_to_winners:
        winners_dir = analysis_root / "winners" / state / "stamps" / "digit_reduction"
        winners_stamp_path = _ensure(winners_dir / f"{stamp}_{variant}_winner_stamp.json")
        winners_stamp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    payload["stamp_json_analyzer"] = str(stamp_path)
    payload["stamp_json_winners"] = str(winners_stamp_path) if winners_stamp_path else None
    return payload


def run_winner_overlay_batch(
    state: str,
    winners: Dict[Variant, str],
    *,
    analysis_root: Optional[Path] = None,
    when: Optional[str] = None,
    mirror_to_winners: bool = True,
) -> Dict[str, Any]:
    analysis_root = Path(analysis_root) if analysis_root is not None else Path("data/outputs/analysis")
    stamp = when or dt.datetime.utcnow().strftime("%Y%m%d")

    results: Dict[str, Dict[str, Any]] = {}
    for variant, combo in winners.items():
        combo = combo.strip()
        if not combo:
            continue
        single = run_winner_overlay(
            state,
            combo,
            variant=variant,
            analysis_root=analysis_root,
            when=stamp,
        )

        spec = WinnerSpec(combo=combo, variant=variant, when=stamp)
        training_json = _training_json_latest(state, analysis_root)
        if training_json is None:
            raise FileNotFoundError(f"No training JSON found for state {state}")
        wmap = build_winner_map(training_json, spec, variant=variant)

        winners_dir = _analysis_digit_reduction_root(state, analysis_root) / "analyzer_v2" / "winners"
        flags_path = _write_flags_csv(winners_dir, stamp, variant, wmap)
        stamp_payload = _write_stamp_json(
            state,
            variant,
            spec,
            wmap,
            analysis_root=analysis_root,
            stamp=stamp,
            overlay_html=Path(single["overlay_html"]) if single.get("overlay_html") else None,
            map_path=Path(single["winner_map_json"]),
            hits_path=Path(single["winner_hits_csv"]),
            flags_path=flags_path,
            mirror_to_winners=mirror_to_winners,
        )

        results[variant] = {
            "winner": combo,
            "overlay_html": single.get("overlay_html"),
            "map_json": single.get("winner_map_json"),
            "hits_csv": single.get("winner_hits_csv"),
            "flags_csv": str(flags_path),
            "stamp_json_analyzer": stamp_payload.get("stamp_json_analyzer"),
            "stamp_json_winners": stamp_payload.get("stamp_json_winners"),
            "hits": single.get("hit_count", 0),
        }

    return {
        "state": state,
        "stamp": stamp,
        "results": results,
    }
