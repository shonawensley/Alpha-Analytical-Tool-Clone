from __future__ import annotations

import csv
import datetime as dt
import itertools
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Literal, Set

from . import io
from modules.aux_loaders import load_state_draws

def _utc_iso(timespec: str = "seconds") -> str:
    stamp = dt.datetime.now(dt.UTC).isoformat(timespec=timespec)
    return stamp[:-6] + "Z" if stamp.endswith("+00:00") else stamp
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


Variant = Literal["Combined", "Midday", "Evening"]

RECENT_DRAW_VARIANTS = ("Combined", "Midday", "Evening")
VARIANT_TO_LOADER = {
    "Combined": "combined",
    "Midday": "midday",
    "Evening": "evening",
}
RECENT_DRAW_DEPTH = 4


def _collect_recent_draws(state: str, depth: int = RECENT_DRAW_DEPTH) -> Dict[str, Dict[str, Any]]:
    results: Dict[str, Dict[str, Any]] = {}
    mapping = [("Set1", "current"), ("Set2", "previous"), ("Set3", "two_prior")]
    for label in RECENT_DRAW_VARIANTS:
        loader_variant = VARIANT_TO_LOADER[label]
        draws, source = load_state_draws(state, loader_variant, max_n=depth)
        trimmed = draws[:depth] if depth else draws
        sets: Dict[str, str] = {}
        by_label: Dict[str, str] = {}
        for idx, (set_name, desc) in enumerate(mapping):
            if idx < len(trimmed):
                value = trimmed[idx]
                sets[set_name] = value
                by_label[desc] = value
        results[label] = {
            "draws": trimmed,
            "source": source,
            "sets": sets,
            "labels": by_label,
        }
    return results


def _winner_permutation_variants(spec: WinnerSpec) -> Dict[str, List[str]]:
    perms = spec.permutations
    digits = [ch for ch in spec.combo if ch.isdigit()]
    family: List[str] = []
    if len(digits) >= 3:
        pools: List[List[str]] = []
        for ch in digits[:3]:
            mirror = _MIRROR.get(ch)
            options = {ch}
            if mirror is not None:
                options.add(mirror)
            pools.append(sorted(options))
        family = sorted({''.join(p) for p in itertools.product(*pools)})
    return {
        'permutations': perms,
        'vtrac_family': family,
    }

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


MATCH_EXACT = "exact"
MATCH_VTRAC = "vtrac"
MATCH_DROP_EXACT = "drop_exact"
MATCH_DROP_VTRAC = "drop_vtrac"
MATCH_FAMILY_EXACT = "family_exact"
MATCH_FAMILY_VTRAC = "family_vtrac"

MATCH_ORDER = [
    MATCH_EXACT,
    MATCH_VTRAC,
    MATCH_DROP_EXACT,
    MATCH_DROP_VTRAC,
    MATCH_FAMILY_EXACT,
    MATCH_FAMILY_VTRAC,
]

MATCH_DISPLAY_NAME = {
    MATCH_EXACT: "Exact",
    MATCH_VTRAC: "V-TRAC",
    MATCH_DROP_EXACT: "Drop Exact",
    MATCH_DROP_VTRAC: "Drop V-TRAC",
    MATCH_FAMILY_EXACT: "3-Value Exact",
    MATCH_FAMILY_VTRAC: "3-Value V-TRAC",
}

MATCH_CSS_CLASS = {
    MATCH_EXACT: "dr-winner-exact",
    MATCH_VTRAC: "dr-winner-vtrac",
    MATCH_DROP_EXACT: "dr-winner-drop-exact",
    MATCH_DROP_VTRAC: "dr-winner-drop-vtrac",
    MATCH_FAMILY_EXACT: "dr-winner-family-exact",
    MATCH_FAMILY_VTRAC: "dr-winner-family-vtrac",
}

EARLIEST_FIELD_BY_KIND = {
    MATCH_EXACT: "earliest_exact_step",
    MATCH_VTRAC: "earliest_vtrac_step",
    MATCH_DROP_EXACT: "earliest_drop_exact_step",
    MATCH_DROP_VTRAC: "earliest_drop_vtrac_step",
    MATCH_FAMILY_EXACT: "earliest_family_exact_step",
    MATCH_FAMILY_VTRAC: "earliest_family_vtrac_step",
}

FINAL_FIELD_BY_KIND = {
    MATCH_EXACT: "final_exact_match",
    MATCH_VTRAC: "final_vtrac_match",
    MATCH_DROP_EXACT: "final_drop_exact_match",
    MATCH_DROP_VTRAC: "final_drop_vtrac_match",
    MATCH_FAMILY_EXACT: "final_family_exact_match",
    MATCH_FAMILY_VTRAC: "final_family_vtrac_match",
}


@dataclass
class WinnerContext:
    permutations: set[str]
    canon: str
    vtrac_index: int
    digit_set: set[str]
    vtrac_key: Tuple[int, int, int]


@dataclass
class RunAnalysis:
    kinds: set[str]
    drop_digit: Optional[str] = None
    drop_kind: Optional[str] = None


def _winner_context(spec: WinnerSpec) -> WinnerContext:
    permutations = set(spec.permutations)
    canon = spec.canon
    digits = [ch for ch in spec.combo if ch.isdigit()]
    digit_set = set(digits)
    vtrac_index = spec.vtrac_index
    vtrac_key = _vtrac_local_key(spec.combo) if vtrac_index >= 0 else (-1, -1, -1)
    return WinnerContext(
        permutations=permutations,
        canon=canon,
        vtrac_index=vtrac_index,
        digit_set=digit_set,
        vtrac_key=vtrac_key,
    )


def _iter_digit_runs(value: str) -> Iterable[Tuple[int, int, str]]:
    for match in re.finditer(r"\d+", value):
        yield match.start(), match.end(), match.group(0)


def _analyze_run(run: str, ctx: WinnerContext) -> RunAnalysis:
    digits = "".join(ch for ch in run if ch.isdigit())
    if len(digits) < 3:
        return RunAnalysis(set())

    kinds: set[str] = set()
    drop_digit: Optional[str] = None

    has_exact = False
    has_vtrac = False
    if ctx.canon or ctx.vtrac_index >= 0:
        for idx in range(len(digits) - 2):
            window = digits[idx : idx + 3]
            if ctx.canon and _canon3(window) == ctx.canon:
                has_exact = True
            if ctx.vtrac_index >= 0 and _vtrac_local_index(window) == ctx.vtrac_index:
                has_vtrac = True
    if has_exact:
        kinds.add(MATCH_EXACT)
    if has_vtrac:
        kinds.add(MATCH_VTRAC)

    if len(digits) > 3:
        for idx in range(len(digits)):
            trimmed = digits[:idx] + digits[idx + 1 :]
            if len(trimmed) < 3:
                continue
            trimmed_canon = _canon3(trimmed)
            matched = False
            if trimmed_canon and ctx.canon and trimmed_canon == ctx.canon:
                kinds.add(MATCH_DROP_EXACT)
                drop_digit = drop_digit or digits[idx]
                matched = True
            if ctx.vtrac_index >= 0 and _vtrac_local_index(trimmed) == ctx.vtrac_index:
                kinds.add(MATCH_DROP_VTRAC)
                drop_digit = drop_digit or digits[idx]
                matched = True
            if matched and MATCH_DROP_EXACT in kinds and MATCH_DROP_VTRAC in kinds:
                break

    if ctx.digit_set and len(ctx.digit_set) == 3 and set(digits) == ctx.digit_set:
        kinds.add(MATCH_FAMILY_EXACT)
    if ctx.vtrac_index >= 0:
        key = _vtrac_local_key(digits)
        if key == ctx.vtrac_key:
            kinds.add(MATCH_FAMILY_VTRAC)

    drop_kind = None
    if MATCH_DROP_EXACT in kinds:
        drop_kind = MATCH_DROP_EXACT
    elif MATCH_DROP_VTRAC in kinds:
        drop_kind = MATCH_DROP_VTRAC

    return RunAnalysis(kinds=kinds, drop_digit=drop_digit, drop_kind=drop_kind)




def _render_exact_run(run: str, ctx: WinnerContext, analysis: RunAnalysis) -> str:
    digits = "".join(ch for ch in run if ch.isdigit())
    if len(digits) < 3:
        return run
    pieces: list[str] = []
    i = 0
    while i <= len(digits) - 3:
        window = digits[i : i + 3]
        if ctx.canon and _canon3(window) == ctx.canon:
            class_attr = MATCH_CSS_CLASS[MATCH_EXACT]
            pieces.append(f'<span class="{class_attr}">{window}</span>')
            i += 3
        else:
            pieces.append(digits[i])
            i += 1
    if i < len(digits):
        pieces.append(digits[i:])
    return "".join(pieces)


def _render_run(run: str, analysis: RunAnalysis) -> str:
    if not analysis.kinds:
        return run
    classes = []
    for kind in MATCH_ORDER:
        if kind in analysis.kinds:
            classes.append(MATCH_CSS_CLASS[kind])
    class_attr = " ".join(dict.fromkeys(classes))
    attrs = [f'class="{class_attr}"']
    if analysis.drop_digit is not None:
        attrs.append(f'data-drop-digit="{analysis.drop_digit}"')
    return f"<span {' '.join(attrs)}>{run}</span>"


def _counts_from_map(wmap: Dict[str, Any]) -> Dict[str, int]:
    items = wmap.get("items", [])
    counts: Dict[str, int] = {"items_total": len(items)}
    for kind in MATCH_ORDER:
        earliest_field = EARLIEST_FIELD_BY_KIND[kind]
        final_field = FINAL_FIELD_BY_KIND[kind]
        any_hits = sum(
            1
            for row in items
            if int(row.get(earliest_field, -1)) >= 0 or bool(row.get(final_field))
        )
        final_hits = sum(1 for row in items if bool(row.get(final_field)))
        counts[f"{kind}_any"] = any_hits
        counts[f"{kind}_final"] = final_hits
    return counts


def _earliest_from_items(items: List[Dict[str, Any]], field: str) -> int:
    candidates = [int(row.get(field, -1)) for row in items if int(row.get(field, -1)) >= 0]
    return min(candidates) if candidates else -1


def _summarize_winner_map(wmap: Dict[str, Any]) -> Dict[str, Any]:
    items = wmap.get("items", [])
    counts = _counts_from_map(wmap)
    earliest_map = {
        kind: _earliest_from_items(items, EARLIEST_FIELD_BY_KIND[kind])
        for kind in MATCH_ORDER
    }
    summary: Dict[str, Any] = {
        "counts": counts,
        "earliest": earliest_map,
        "winner_variants": wmap.get("winner_variants", {}),
    }
    summary["winner_permutations"] = summary["winner_variants"].get("permutations", wmap.get("winner_permutations", []))
    summary["winner_vtrac_family"] = summary["winner_variants"].get("vtrac_family", wmap.get("winner_vtrac_family", []))
    for kind, value in earliest_map.items():
        summary[f"earliest_{kind}_step"] = value
    return summary


def _ensure(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


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
    ]
    for kind in MATCH_ORDER:
        header.append(f"dr_win_{kind}")
    for kind in MATCH_ORDER:
        header.append(f"dr_win_step_{kind}")
    header.extend([
        "dr_win_final_value",
        "dr_win_drop_digit",
        "dr_win_vtrac_local_index",
    ])
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        for row in wmap.get("items", []):
            record: List[Any] = [
                row.get("area", ""),
                row.get("section", ""),
                row.get("set", ""),
                row.get("draw", ""),
                row.get("col", ""),
                row.get("method", ""),
                row.get("mode", ""),
            ]
            for kind in MATCH_ORDER:
                earliest_field = EARLIEST_FIELD_BY_KIND[kind]
                final_field = FINAL_FIELD_BY_KIND[kind]
                any_flag = 1 if (
                    int(row.get(earliest_field, -1)) >= 0 or bool(row.get(final_field))
                ) else 0
                record.append(any_flag)
            for kind in MATCH_ORDER:
                record.append(int(row.get(EARLIEST_FIELD_BY_KIND[kind], -1)))
            record.extend([
                row.get("final_value", ""),
                row.get("final_drop_digit", ""),
                int(row.get("final_vtrac_local_index", -1)),
            ])
            writer.writerow(record)
    return path


def _analysis_digit_reduction_root(state: str, analysis_root: Path) -> Path:
    return analysis_root / "digit_reduction" / state

def _stacked_html_path(state: str, analysis_root: Path) -> Path:
    return _analysis_digit_reduction_root(state, analysis_root) / f"{state}_digit_reduction_report_stacked.html"

def _training_json_latest(state: str, analysis_root: Path) -> Optional[Path]:
    training_dir = _analysis_digit_reduction_root(state, analysis_root) / "training"
    if not training_dir.exists():
        return None
    patterns = ["*_digit_reduction_log.json", "*_digit_reduction_logs.json"]
    candidates: list[Path] = []
    for pattern in patterns:
        candidates.extend(training_dir.glob(pattern))
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    seen: set[Path] = set()
    unique: list[Path] = []
    for cand in candidates:
        resolved = cand.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(cand)
    return unique[0] if unique else None

def _iter_items(training_json: Path) -> Iterable[Dict[str, Any]]:
    payload = json.loads(training_json.read_text(encoding="utf-8"))
    for item in payload.get("items", []):
        yield item

def _analyze_value(value: str, ctx: WinnerContext) -> Dict[str, Any]:
    kinds: set[str] = set()
    drop_digit: Optional[str] = None
    for _, _, run in _iter_digit_runs(value):
        analysis = _analyze_run(run, ctx)
        if analysis.kinds:
            kinds.update(analysis.kinds)
            if analysis.drop_kind and analysis.drop_digit is not None and drop_digit is None:
                drop_digit = analysis.drop_digit
    return {"kinds": kinds, "drop_digit": drop_digit}


def _winner_item(view: Dict[str, Any], spec: WinnerSpec, ctx: WinnerContext) -> Optional[Dict[str, Any]]:
    earliest: Dict[str, Optional[int]] = {kind: None for kind in MATCH_ORDER}
    steps = view.get("steps", [])
    for step in steps:
        step_no = step.get("step")
        value = str(step.get("value", ""))
        analysis = _analyze_value(value, ctx)
        if not isinstance(step_no, int):
            continue
        for kind in analysis["kinds"]:
            if earliest.get(kind) is None:
                earliest[kind] = step_no

    final = view.get("final", {})
    final_value = str(final.get("value", ""))
    final_analysis = _analyze_value(final_value, ctx)
    final_kinds = final_analysis["kinds"]

    if not final_kinds and all(v is None for v in earliest.values()):
        return None

    row: Dict[str, Any] = {
        "state": view.get("state"),
        "area": view.get("area"),
        "section": view.get("section"),
        "set": view.get("set"),
        "draw": view.get("draw"),
        "col": view.get("col"),
        "method": view.get("method"),
        "mode": view.get("mode"),
        "final_value": final_value,
        "final_exact_match": MATCH_EXACT in final_kinds,
        "final_vtrac_match": MATCH_VTRAC in final_kinds,
        "final_drop_exact_match": MATCH_DROP_EXACT in final_kinds,
        "final_drop_vtrac_match": MATCH_DROP_VTRAC in final_kinds,
        "final_family_exact_match": MATCH_FAMILY_EXACT in final_kinds,
        "final_family_vtrac_match": MATCH_FAMILY_VTRAC in final_kinds,
        "final_drop_digit": final_analysis.get("drop_digit") or "",
        "final_vtrac_local_index": _vtrac_local_index(final_value),
        "match_types": ",".join(sorted(final_kinds | {kind for kind, val in earliest.items() if val is not None})),
    }

    for kind in MATCH_ORDER:
        key = f"earliest_{kind}_step"
        value = earliest.get(kind)
        row[key] = value if value is not None else -1

    return row


def build_winner_map(training_json: Path, spec: WinnerSpec, *, variant: str) -> Dict[str, Any]:
    ctx = _winner_context(spec)
    items = []
    variants_info = _winner_permutation_variants(spec)
    for view in _iter_items(training_json):
        if variant != "Combined" and view.get("section") != variant:
            continue
        row = _winner_item(view, spec, ctx)
        if row:
            items.append(row)
    return {
        "winner": spec.combo,
        "winner_canon": spec.canon,
        "winner_permutations": variants_info.get("permutations", spec.permutations),
        "winner_variants": variants_info,
        "winner_vtrac_family": variants_info.get("vtrac_family", []),
        "vtrac_local_index": spec.vtrac_index,
        "variant": variant,
        "generated_at": _utc_iso("seconds"),
        "items": items,
    }


def _highlight_text_segment(segment: str, ctx: WinnerContext | WinnerSpec) -> str:
    context = _winner_context(ctx) if isinstance(ctx, WinnerSpec) else ctx
    pieces: list[str] = []
    last = 0
    for start, end, run in _iter_digit_runs(segment):
        if start > last:
            pieces.append(segment[last:start])
        analysis = _analyze_run(run, context)
        if MATCH_EXACT in analysis.kinds:
            pieces.append(_render_exact_run(run, context, analysis))
        else:
            pieces.append(_render_run(run, analysis))
        last = end
    if last < len(segment):
        pieces.append(segment[last:])
    return "".join(pieces)



def _highlight_html(html: str, spec: WinnerSpec) -> str:
    ctx = _winner_context(spec)
    if not ctx.permutations and ctx.vtrac_index < 0:
        return html

    parts = re.split(r"(<[^>]+>)", html)
    for idx, part in enumerate(parts):
        if not part or part.startswith("<"):
            continue
        parts[idx] = _highlight_text_segment(part, ctx)
    return "".join(parts)



def _format_step(value: Optional[int]) -> str:
    try:
        if value is None:
            return "n/a"
        ivalue = int(value)
    except (TypeError, ValueError):
        return "n/a"
    return "n/a" if ivalue < 0 else str(ivalue)



def _render_banner(state: str, variant: str, spec: WinnerSpec, summary: Optional[Dict[str, Any]]) -> str:
    ts = _utc_iso("seconds")
    payload = summary or {}
    counts = payload.get("counts") or {}
    earliest_map = payload.get("earliest") or {}

    count_line = " | ".join(
        f"{MATCH_DISPLAY_NAME[kind]}: {counts.get(f'{kind}_any', 0)}"
        for kind in MATCH_ORDER
    )
    final_line = " | ".join(
        f"{MATCH_DISPLAY_NAME[kind]}: {counts.get(f'{kind}_final', 0)}"
        for kind in MATCH_ORDER
    )
    earliest_parts = []
    for kind in MATCH_ORDER:
        value = earliest_map.get(kind)
        if value is None:
            value = payload.get(f"earliest_{kind}_step")
        if value is not None and int(value) >= 0:
            earliest_parts.append(f"{MATCH_DISPLAY_NAME[kind]}: {value}")
    earliest_line = " | ".join(earliest_parts) if earliest_parts else "n/a"

    variants_info = payload.get("winner_variants") or {}
    permutations_line = ", ".join(variants_info.get("permutations", [])) or "n/a"
    family_line = ", ".join(variants_info.get("vtrac_family", [])) or "n/a"

    recent_map = payload.get("recent_draws") or {}
    depth = payload.get("recent_draw_depth")
    draw_entries: List[str] = []
    for label in RECENT_DRAW_VARIANTS:
        info = recent_map.get(label) or {}
        sets = info.get("sets") or {}
        formatted = ", ".join(f"{set_name}={sets.get(set_name, 'n/a') or 'n/a'}" for set_name in ("Set1", "Set2", "Set3"))
        draw_entries.append(f"{label}: {formatted or 'n/a'}")
    draws_line = " | ".join(draw_entries) if draw_entries else "n/a"
    draws_prefix = "Draw timeline (Set1 current, Set2 previous, Set3 two prior)"

    legend_html = " ".join(
        f'<span class="{MATCH_CSS_CLASS[kind]}">{MATCH_DISPLAY_NAME[kind]}</span>'
        for kind in MATCH_ORDER
    )
    return "".join([
        f"<!-- Digit Reduction winner overlay: state={state} variant={variant} winner={spec.combo} vtrac={spec.vtrac_index} -->\n",
        "<style>\n",
        ".dr-winner-exact { background: rgba(255, 215, 0, 0.85); color: #111; padding: 0 2px; border-radius: 2px; }\n",
        ".dr-winner-vtrac { background: rgba(255, 140, 0, 0.55); color: #111; padding: 0 2px; border-radius: 2px; }\n",
        ".dr-winner-drop-exact { border:1px solid rgba(229, 194, 0, 0.8); background: rgba(255, 215, 0, 0.28); color: #111; padding:0 2px; border-radius:2px; }\n",
        ".dr-winner-drop-vtrac { border:1px solid rgba(230, 138, 0, 0.8); background: rgba(255, 165, 0, 0.25); color:#111; padding:0 2px; border-radius:2px; }\n",
        ".dr-winner-family-exact { background: rgba(135, 206, 250, 0.3); color:#111; padding:0 2px; border-radius:2px; border:1px solid rgba(90, 162, 201, 0.6); }\n",
        ".dr-winner-family-vtrac { background: rgba(186, 85, 211, 0.3); color:#111; padding:0 2px; border-radius:2px; border:1px solid rgba(123, 47, 165, 0.6); }\n",
        ".dr-winner-banner { border:1px solid #666; padding: 10px; margin: 12px 0; background:#1b1b1b; color:#eee; font-size:0.95rem; }\n",
        ".dr-winner-banner__title { font-size: 1rem; margin-bottom: 4px; }\n",
        ".dr-winner-legend { margin-top: 6px; line-height: 1.4; font-size: 0.85rem; }\n",
        "</style>\n",
        '<div class="dr-winner-banner">\n',
        '  <div class="dr-winner-banner__title"><strong>Digit Reduction - Winner Overlay</strong></div>\n',
        f'  <div>state: {state} | variant: {variant} | winner: {spec.combo} | vtrac local index: {spec.vtrac_index} | generated: {ts}</div>\n',
        '  <div class="dr-winner-legend">',
        f'Legend: {legend_html}<br/>',
        f'Hits: {count_line}<br/>Finals: {final_line}<br/>Earliest steps: {earliest_line}',
        f'<br/>Permutations: {permutations_line}'
        f'<br/>V-TRAC family variants: {family_line}'
        f'<br/>{draws_prefix}: {draws_line}',
        '</div>\n',
        '</div>\n',
    ])



def annotate_stacked_html(state: str, spec: WinnerSpec, *, variant: str, analysis_root: Path, stamp: str, summary: Optional[Dict[str, Any]] = None) -> Optional[Path]:
    stacked = _stacked_html_path(state, analysis_root)
    if not stacked.exists():
        return None
    html = stacked.read_text(encoding="utf-8")
    annotated = _highlight_html(html, spec)
    banner = _render_banner(state, variant, spec, summary)
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
    ]
    for kind in MATCH_ORDER:
        header.append(f"earliest_{kind}_step")
    header.extend(
        [
            "final_value",
        ]
    )
    for kind in MATCH_ORDER:
        header.append(f"final_{kind}_match")
    header.extend([
        "final_drop_digit",
        "final_vtrac_local_index",
        "match_types",
    ])

    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        for row in wmap.get("items", []):
            record: List[Any] = [
                row.get("state", ""),
                row.get("area", ""),
                row.get("section", ""),
                row.get("set", ""),
                row.get("draw", ""),
                row.get("col", ""),
                row.get("method", ""),
                row.get("mode", ""),
            ]
            for kind in MATCH_ORDER:
                record.append(int(row.get(EARLIEST_FIELD_BY_KIND[kind], -1)))
            record.append(row.get("final_value", ""))
            for kind in MATCH_ORDER:
                record.append(1 if row.get(FINAL_FIELD_BY_KIND[kind]) else 0)
            record.extend([
                row.get("final_drop_digit", ""),
                int(row.get("final_vtrac_local_index", -1)),
                row.get("match_types", ""),
            ])
            writer.writerow(record)
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
    stamp = when or dt.datetime.now(dt.UTC).strftime("%Y%m%d")

    wmap = build_winner_map(training_json, spec, variant=variant)
    summary = _summarize_winner_map(wmap)
    summary = dict(summary or {})
    variants_info = _winner_permutation_variants(spec)
    summary.setdefault("winner_variants", variants_info)
    summary.setdefault("winner_permutations", variants_info.get("permutations", []))
    summary.setdefault("winner_vtrac_family", variants_info.get("vtrac_family", []))
    recent_draws = _collect_recent_draws(state, RECENT_DRAW_DEPTH)
    summary["recent_draws"] = recent_draws
    summary["recent_draw_depth"] = RECENT_DRAW_DEPTH

    outdir = _analysis_digit_reduction_root(state, analysis_root) / "analyzer_v2" / "winners"
    outdir.mkdir(parents=True, exist_ok=True)

    map_path = outdir / f"{stamp}_{variant}_winner_map.json"
    hits_path = outdir / f"{stamp}_{variant}_winner_hits.csv"

    _write_json(map_path, wmap)
    _write_hits_csv(hits_path, wmap)

    overlay_path = annotate_stacked_html(
        state,
        spec,
        variant=variant,
        analysis_root=analysis_root,
        stamp=stamp,
        summary=summary,
    )

    return {
        "state": state,
        "variant": variant,
        "winner": winner_combo,
        "winner_map_json": str(map_path),
        "winner_hits_csv": str(hits_path),
        "overlay_html": str(overlay_path) if overlay_path else None,
        "hit_count": len(wmap.get("items", [])),
        "summary": summary,
        "recent_draws": recent_draws,
    }


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
    recent_draws: Optional[Dict[str, Any]] = None,
    recent_draw_depth: Optional[int] = None,
) -> Dict[str, Any]:
    items = wmap.get("items", [])
    counts = _counts_from_map(wmap)
    earliest = {
        kind: _earliest_from_items(items, EARLIEST_FIELD_BY_KIND[kind])
        for kind in MATCH_ORDER
    }
    variants_info = wmap.get("winner_variants", {})
    payload = {
        "tool": "digit_reduction",
        "state": state,
        "variant": variant,
        "winner": spec.combo,
        "winner_canon": spec.canon,
        "winner_variants": variants_info,
        "winner_permutations": variants_info.get("permutations", wmap.get("winner_permutations", [])),
        "winner_vtrac_family": variants_info.get("vtrac_family", wmap.get("winner_vtrac_family", [])),
        "vtrac_local_index": spec.vtrac_index,
        "generated_at": _utc_iso("seconds"),
        "counts": counts,
        "earliest": earliest,
        "recent_draws": recent_draws or {},
        "recent_draw_depth": recent_draw_depth if recent_draw_depth is not None else RECENT_DRAW_DEPTH,
        "paths": {
            "overlay_html": str(overlay_html) if overlay_html else None,
            "winner_map_json": str(map_path),
            "winner_hits_csv": str(hits_path),
            "winner_flags_csv": str(flags_path),
        },
        "sample": [
            {
                "loc": {
                    key: row.get(key, "")
                    for key in ["area", "section", "set", "draw", "col", "method", "mode"]
                },
                **{
                    f"earliest_{kind}_step": int(row.get(EARLIEST_FIELD_BY_KIND[kind], -1))
                    for kind in MATCH_ORDER
                },
                **{
                    f"final_{kind}_match": bool(row.get(FINAL_FIELD_BY_KIND[kind]))
                    for kind in MATCH_ORDER
                },
                "final_value": row.get("final_value", ""),
                "final_drop_digit": row.get("final_drop_digit", ""),
                "match_types": row.get("match_types", ""),
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
    stamp = when or dt.datetime.now(dt.UTC).strftime("%Y%m%d")

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
        summary = single.get("summary") or {}
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
            recent_draws=summary.get("recent_draws"),
            recent_draw_depth=summary.get("recent_draw_depth"),
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
            "summary": summary,
            "counts": summary.get("counts"),
            "earliest_exact_step": summary.get("earliest_exact_step"),
            "earliest_vtrac_step": summary.get("earliest_vtrac_step"),
        }

    return {
        "state": state,
        "stamp": stamp,
        "results": results,
    }


@dataclass
class OverlayArtifacts:
    flag_map: Dict[Tuple[str, str, str, str, str, int, str, str], Dict[str, Any]]
    files: List[str]


def _parse_winner_flags_csv(path: Path, state: str) -> Dict[Tuple[str, str, str, str, str, int, str, str], Dict[str, Any]]:
    result: Dict[Tuple[str, str, str, str, str, int, str, str], Dict[str, Any]] = {}
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            key = (
                state,
                str(row.get("area", "")),
                str(row.get("section", "")),
                str(row.get("set", "")),
                str(row.get("draw", "")),
                int(row.get("col", 0)),
                str(row.get("method", "")),
                str(row.get("mode", "")),
            )
            payload: Dict[str, Any] = {}
            for kind in MATCH_ORDER:
                payload[f"dr.win_{kind}"] = int(row.get(f"dr_win_{kind}", 0))
            for kind in MATCH_ORDER:
                payload[f"dr.win_step_{kind}"] = int(row.get(f"dr_win_step_{kind}", -1))
            payload["dr.win_final_value"] = row.get("dr_win_final_value", "")
            payload["dr.win_drop_digit"] = row.get("dr_win_drop_digit", "")
            payload["dr.win_vtrac_local_index"] = int(row.get("dr_win_vtrac_local_index", -1))
            result[key] = payload
    return result


def build_winner_overlay(
    state: str,
    rows: List[Dict[str, Any]],
    _feature_entries: Iterable[Any],
    config: Dict[str, Any],
    analysis_root: Optional[Path],
    overlay_cfg: Dict[str, Any],
) -> OverlayArtifacts:
    winners_cfg = overlay_cfg.get("winners") or {}
    winners: Dict[Variant, str] = {}
    for variant in ("Combined", "Midday", "Evening"):
        value = winners_cfg.get(variant)
        if value:
            winners[variant] = str(value)

    if not winners:
        return OverlayArtifacts(flag_map={}, files=[])

    batch = run_winner_overlay_batch(
        state,
        winners,
        analysis_root=analysis_root,
        mirror_to_winners=overlay_cfg.get("mirror_to_winners", True),
    )

    files: List[str] = []
    flag_map: Dict[Tuple[str, str, str, str, str, int, str, str], Dict[str, Any]] = {}
    for variant, details in batch.get("results", {}).items():
        flags_csv = details.get("flags_csv")
        if not flags_csv:
            continue
        path = Path(flags_csv)
        files.append(str(Path("winners") / path.name))
        flag_map.update(_parse_winner_flags_csv(path, state))
        for extra in ("map_json", "hits_csv", "overlay_html", "stamp_json_analyzer", "stamp_json_winners"):
            extra_path = details.get(extra)
            if not extra_path:
                continue
            files.append(str(Path("winners") / Path(extra_path).name))
    unique_files = []
    seen: Set[str] = set()
    for entry in files:
        if entry in seen:
            continue
        seen.add(entry)
        unique_files.append(entry)
    return OverlayArtifacts(flag_map=flag_map, files=unique_files)


