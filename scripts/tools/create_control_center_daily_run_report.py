"""
Create a per-date Control Center (Brain-2) daily run report Markdown file.

Goal
----
Provide a single cross-state artifact per results date D that:

- Links to the frozen sharepack Control Center bundle under sharepacks/<D>/control_center/
- Summarizes what fired (BA, Due Doubles, VTRAC Repeat Watch, Profit Alerts A01-A12)
- Includes a small, unitless "episode economics" section (no wagering engine)
- Provides fill-in prompts for human synthesis + fix-later capture

This script does not run analyzers and does not rebuild tables. It only reads
sharepack outputs and writes a report into docs/AAT9_KIT/FINAL VALIDATION/RUNS/.

Usage
-----
python3 scripts/tools/create_control_center_daily_run_report.py --date 2025-06-21
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from dataclasses import dataclass
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Iterable, List, Mapping, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> object:
    return json.loads(read_text(path))


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        return [{k: (v or "") for k, v in row.items()} for row in reader]


def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except Exception:
        return None


def safe_float(value: str) -> float | None:
    try:
        return float(value)
    except Exception:
        return None


@dataclass(frozen=True)
class Meta:
    results_date: str
    history_date: str
    history_excel_path: str
    results_file: str
    states_count: int


def load_meta(control_center_dir: Path, *, results_date: str) -> Meta:
    meta_path = control_center_dir / "meta.json"
    if meta_path.exists():
        raw = read_json(meta_path)
        if isinstance(raw, dict):
            history_date = str(raw.get("history_date") or "")
            history_excel_path = str(raw.get("history_excel_path") or "")
            results_file = str(raw.get("results_file") or f"data/results/{results_date}.txt")
            states = raw.get("states")
            states_count = len(states) if isinstance(states, list) else 0
            if history_date and history_excel_path:
                return Meta(
                    results_date=results_date,
                    history_date=history_date,
                    history_excel_path=history_excel_path,
                    results_file=results_file,
                    states_count=states_count,
                )

    d = parse_iso_date(results_date)
    h = (d - timedelta(days=1)).isoformat()
    return Meta(
        results_date=results_date,
        history_date=h,
        history_excel_path=f"data/history/Pick3StatsC4_{h.replace('-', '_')}.xlsm",
        results_file=f"data/results/{results_date}.txt",
        states_count=0,
    )


def count_truthy(rows: Iterable[Mapping[str, str]], key: str, truth: str = "True") -> int:
    return sum(1 for r in rows if r.get(key, "").strip() == truth)


def uniq_values(rows: Iterable[Mapping[str, str]], key: str, *, skip: set[str] | None = None) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for r in rows:
        v = (r.get(key) or "").strip()
        if not v:
            continue
        if skip and v in skip:
            continue
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def summarize_blackapple(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return ["- (missing) `blackapple_alerts.csv`"]

    status_counts: dict[str, int] = {}
    for r in rows:
        status = (r.get("Status") or "").strip() or "?"
        status_counts[status] = status_counts.get(status, 0) + 1

    alert_states = {r.get("StateKey", "").strip() for r in rows if (r.get("Status") or "").strip() == "ALERT"}
    watch_states = {r.get("StateKey", "").strip() for r in rows if (r.get("Status") or "").strip() == "WATCH"}
    alert_states.discard("")
    watch_states.discard("")

    midday_hit_rows = sum(
        1
        for r in rows
        if (r.get("Midday Hits") or "").strip() not in ("", "-", "N/A")
    )
    evening_hit_rows = sum(
        1
        for r in rows
        if (r.get("Evening Hits") or "").strip() not in ("", "-", "N/A")
    )

    lines: list[str] = []
    lines.append(f"- Rows: `{len(rows)}`")
    lines.append(f"- Status counts: `{', '.join([f'{k}={v}' for k, v in sorted(status_counts.items())])}`")
    lines.append(f"- States in ALERT: `{len(alert_states)}`")
    lines.append(f"- States in WATCH: `{len(watch_states)}`")
    lines.append(f"- Rows with Midday hits (D-only diagnostic): `{midday_hit_rows}`")
    lines.append(f"- Rows with Evening hits (D-only diagnostic): `{evening_hit_rows}`")
    return lines


def summarize_due_doubles(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return ["- (missing) `due_doubles.csv`"]

    top: list[tuple[int, str, str, str]] = []
    for r in rows:
        ds = safe_int((r.get("Draws Since Double") or "").strip())
        if ds is None:
            continue
        top.append((ds, (r.get("StateKey") or "").strip(), (r.get("Variant") or "").strip(), (r.get("State") or "").strip()))
    top_sorted = sorted(top, key=lambda t: (-t[0], t[1].lower(), t[2].lower()))[:5]

    midday_in_family = count_truthy(rows, "Midday Winner In Family")
    evening_in_family = count_truthy(rows, "Evening Winner In Family")

    lines: list[str] = []
    lines.append(f"- Rows: `{len(rows)}`")
    lines.append(f"- Midday winner-in-family True rows: `{midday_in_family}`")
    lines.append(f"- Evening winner-in-family True rows: `{evening_in_family}`")
    if top_sorted:
        lines.append("- Top due rows by Draws Since Double:")
        for ds, state_key, variant, _state in top_sorted:
            lines.append(f"  - `{state_key}` `{variant}`: `{ds}`")
    return lines


def summarize_vtrac_repeat_watch(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return ["- (missing) `vtrac_repeat_watch.csv`"]

    hits = [
        r for r in rows if (r.get("Current==WinnerVTRAC") or "").strip() == "True"
    ]
    lines: list[str] = []
    lines.append(f"- Rows: `{len(rows)}`")
    lines.append(f"- Rows where Current==WinnerVTRAC: `{len(hits)}`")
    if hits:
        lines.append("- Hit rows:")
        for r in hits[:10]:
            lines.append(
                f"  - `{r.get('StateKey','').strip()}` `{r.get('Variant','').strip()}`: "
                f"idx `{r.get('Current Index','').strip()}` == winnerVT `{r.get('Winner VTRAC','').strip()}`"
            )
    return lines


def summarize_profit_eval(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return ["- (missing) `profit_alerts_eval.csv` (run: `python3 scripts/tools/evaluate_profit_alerts.py --date <D>`)"]

    def is_y(r: Mapping[str, str], key: str) -> bool:
        return (r.get(key) or "").strip() == "Y"

    has_hit_7 = bool(rows) and "hit_within_7" in rows[0]
    has_hit_14 = bool(rows) and "hit_within_14" in rows[0]
    has_hit_any_7 = bool(rows) and "hit_any_within_7" in rows[0]
    has_hit_any_14 = bool(rows) and "hit_any_within_14" in rows[0]

    fired = len(rows)
    hit_decay = sum(1 for r in rows if is_y(r, "hit_within_decay"))
    hit_any_decay = sum(1 for r in rows if is_y(r, "hit_any_within_decay"))
    hit_7 = count_truthy(rows, "hit_within_7", truth="Y") if has_hit_7 else None
    hit_14 = count_truthy(rows, "hit_within_14", truth="Y") if has_hit_14 else None
    hit_any_7 = count_truthy(rows, "hit_any_within_7", truth="Y") if has_hit_any_7 else None
    hit_any_14 = count_truthy(rows, "hit_any_within_14", truth="Y") if has_hit_any_14 else None
    censored = sum(1 for r in rows if (r.get("status") or "").strip() == "CENSORED")

    by_alert: dict[str, dict[str, int]] = {}
    for r in rows:
        aid = (r.get("alert_id") or "").strip() or "?"
        by_alert.setdefault(aid, {"fired": 0, "hit_decay": 0, "hit_any_decay": 0, "hit_14": 0, "hit_any_14": 0})
        by_alert[aid]["fired"] += 1
        if is_y(r, "hit_within_decay"):
            by_alert[aid]["hit_decay"] += 1
        if is_y(r, "hit_any_within_decay"):
            by_alert[aid]["hit_any_decay"] += 1
        if has_hit_14 and is_y(r, "hit_within_14"):
            by_alert[aid]["hit_14"] += 1
        if has_hit_any_14 and is_y(r, "hit_any_within_14"):
            by_alert[aid]["hit_any_14"] += 1

    lines: list[str] = []
    lines.append(f"- Rows fired: `{fired}`")
    lines.append(f"- HIT(decay) rows (variant-faithful): `{hit_decay}`")
    lines.append(f"- HIT_any(decay) rows (any-outcome diagnostic): `{hit_any_decay}`")
    if hit_7 is not None:
        lines.append(f"- HIT<=7 rows (variant-faithful diagnostic): `{hit_7}`")
    if hit_14 is not None:
        lines.append(f"- HIT<=14 rows (variant-faithful diagnostic): `{hit_14}`")
    if hit_any_7 is not None:
        lines.append(f"- HIT_any<=7 rows (any-outcome diagnostic): `{hit_any_7}`")
    if hit_any_14 is not None:
        lines.append(f"- HIT_any<=14 rows (any-outcome diagnostic): `{hit_any_14}`")
    lines.append(f"- CENSORED rows (insufficient future results files): `{censored}`")
    lines.append("- By AlertId (fired / hit_decay / hit_any_decay):")
    for aid in sorted(by_alert.keys()):
        d = by_alert[aid]
        lines.append(f"  - `{aid}`: `{d['fired']}` / `{d['hit_decay']}` / `{d['hit_any_decay']}`")

    if hit_14 is not None or hit_any_14 is not None:
        lines.append("- By AlertId (hit_14 / hit_any_14):")
        for aid in sorted(by_alert.keys()):
            d = by_alert[aid]
            lines.append(f"  - `{aid}`: `{d['hit_14']}` / `{d['hit_any_14']}`")
    return lines


def summarize_profit_merged(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return ["- (missing) `profit_alerts_eval_merged.csv`"]

    def is_hit(r: Mapping[str, str]) -> bool:
        return (r.get("status") or "").strip() == "HIT"

    merged_total = len(rows)
    hit_total = sum(1 for r in rows if is_hit(r))
    hit_any_total = sum(1 for r in rows if (r.get("hit_any_within_decay") or "").strip() == "Y")
    hit_7_total = count_truthy(rows, "hit_within_7", truth="Y") if rows and "hit_within_7" in rows[0] else None
    hit_14_total = count_truthy(rows, "hit_within_14", truth="Y") if rows and "hit_within_14" in rows[0] else None
    hit_any_7_total = count_truthy(rows, "hit_any_within_7", truth="Y") if rows and "hit_any_within_7" in rows[0] else None
    hit_any_14_total = count_truthy(rows, "hit_any_within_14", truth="Y") if rows and "hit_any_within_14" in rows[0] else None

    cost_units_all: list[int] = []
    cost_units_hit: list[int] = []
    for r in rows:
        s = safe_int((r.get("implied_set_size") or "").strip())
        w = safe_int((r.get("decay_max") or "").strip())
        if s is None or w is None:
            continue
        cost = s * w
        cost_units_all.append(cost)
        if is_hit(r):
            cost_units_hit.append(cost)

    lines: list[str] = []
    lines.append(f"- Merged rows (deduped play-sets): `{merged_total}`")
    lines.append(f"- HIT(decay) merged episodes: `{hit_total}`")
    lines.append(f"- HIT_any(decay) merged episodes: `{hit_any_total}`")
    if hit_7_total is not None:
        lines.append(f"- HIT<=7 merged episodes (diagnostic): `{hit_7_total}`")
    if hit_14_total is not None:
        lines.append(f"- HIT<=14 merged episodes (diagnostic): `{hit_14_total}`")
    if hit_any_7_total is not None:
        lines.append(f"- HIT_any<=7 merged episodes (diagnostic): `{hit_any_7_total}`")
    if hit_any_14_total is not None:
        lines.append(f"- HIT_any<=14 merged episodes (diagnostic): `{hit_any_14_total}`")
    if cost_units_all:
        lines.append(f"- Episode cost units (implied_set_size * decay_max): min/median/max = `{min(cost_units_all)}` / `{int(statistics.median(cost_units_all))}` / `{max(cost_units_all)}`")
    if cost_units_hit:
        lines.append(f"- HIT episode cost units: min/median/max = `{min(cost_units_hit)}` / `{int(statistics.median(cost_units_hit))}` / `{max(cost_units_hit)}`")
    return lines


def list_top_merged_hits(rows: list[dict[str, str]], limit: int = 10) -> list[str]:
    hits = [r for r in rows if (r.get("status") or "").strip() == "HIT"]
    mode = "HIT(decay)"
    if not hits:
        hits = [
            r
            for r in rows
            if (r.get("hit_within_14") or "").strip() == "Y"
            or (r.get("hit_any_within_14") or "").strip() == "Y"
        ]
        mode = "HIT<=14 (diagnostic)"
    if not hits:
        return ["- (none on this day in merged view)"]

    def key(r: Mapping[str, str]) -> tuple[int, int]:
        strength = safe_int((r.get("strength_max") or "").strip()) or 0
        t_hit = safe_int((r.get("time_to_hit_steps") or "").strip())
        return (-strength, t_hit if t_hit is not None else 999999)

    out: list[str] = []
    if mode != "HIT(decay)":
        out.append(f"- (no HIT(decay) merged episodes; showing `{mode}` rows instead)")
    for r in sorted(hits, key=key)[:limit]:
        hit_flags: list[str] = []
        if (r.get("hit_within_14") or "").strip() == "Y":
            hit_flags.append("hit<=14")
        if (r.get("hit_any_within_14") or "").strip() == "Y":
            hit_flags.append("hit_any<=14")
        hit_when = (r.get("hit_when") or "").strip() or (r.get("hit_any_when") or "").strip()
        hit_type = (r.get("hit_type") or "").strip() or (r.get("hit_any_type") or "").strip()
        hit_suffix = (
            f"hit `{hit_when}` ({hit_type})"
            if hit_when and hit_type
            else f"{','.join(hit_flags) or mode} (timing not recorded in merged CSV)"
        )
        out.append(
            f"- `{r.get('state_key','').strip()}` `{r.get('variant','').strip()}` "
            f"(S={r.get('strength_max','').strip()}, set={r.get('implied_set_size','').strip()}, decay={r.get('decay_max','').strip()}): "
            f"`{r.get('alert_ids','').strip()}` + promoters `{r.get('promoters','').strip()}` "
            f"{hit_suffix}"
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md)",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing report (default: refuse to overwrite).",
    )
    args = ap.parse_args()

    d = parse_iso_date(args.date)
    results_date = d.isoformat()

    sharepack_dir = REPO_ROOT / "sharepacks" / results_date
    cc_dir = sharepack_dir / "control_center"
    if not cc_dir.exists():
        raise SystemExit(f"Missing Control Center sharepack folder: {cc_dir}")

    default_out = (
        REPO_ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "RUNS"
        / f"{results_date}__CONTROL_CENTER.md"
    )
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(
            f"Control Center run report already exists: {out_path}. Refusing to overwrite. "
            "Use --force to overwrite or --out to write a new file."
        )

    meta = load_meta(cc_dir, results_date=results_date)

    ba_csv = cc_dir / "blackapple_alerts.csv"
    dd_csv = cc_dir / "due_doubles.csv"
    vt_csv = cc_dir / "vtrac_repeat_watch.csv"
    pa_eval_csv = cc_dir / "profit_alerts_eval.csv"
    pa_merged_csv = cc_dir / "profit_alerts_eval_merged.csv"

    ba_rows = load_csv_rows(ba_csv)
    dd_rows = load_csv_rows(dd_csv)
    vt_rows = load_csv_rows(vt_csv)
    pa_rows = load_csv_rows(pa_eval_csv)
    merged_rows = load_csv_rows(pa_merged_csv)

    day_synth = (
        REPO_ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "RUNS"
        / f"{results_date}__DAY_SYNTHESIS.md"
    )

    lines: list[str] = []
    lines.append(f"# Control Center Daily Run Report — results {results_date} (history workbook ~ {meta.history_date})")
    lines.append("")
    lines.append("Reference template:")
    lines.append("- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`")
    lines.append("")
    lines.append("Sharepack pointers:")
    lines.append(f"- Sharepack root: `{sharepack_dir.relative_to(REPO_ROOT)}/`")
    lines.append(f"- Control Center bundle: `{cc_dir.relative_to(REPO_ROOT)}/`")
    lines.append(f"- Control Center report: `{(cc_dir / 'control_center_report.md').relative_to(REPO_ROOT)}`")
    lines.append(f"- Meta (provenance): `{(cc_dir / 'meta.json').relative_to(REPO_ROOT)}`")
    lines.append("")

    if day_synth.exists():
        lines.append("Cross-state Brain-1 synthesis (same day):")
        lines.append(f"- `{day_synth.relative_to(REPO_ROOT)}`")
        lines.append("")

    lines.append("## 0) Provenance")
    lines.append(f"- Results date (D): `{meta.results_date}`")
    lines.append(f"- History date (H): `{meta.history_date}`")
    lines.append(f"- History workbook: `{meta.history_excel_path}`")
    lines.append(f"- Results file: `{meta.results_file}`")
    lines.append(f"- States in scope: `{meta.states_count or 'unknown'}`")
    lines.append("")

    lines.append("## 1) Boards snapshot")
    lines.append("")
    lines.append("### 1.1 Blackapple")
    lines.append(f"- Artifacts: `{ba_csv.relative_to(REPO_ROOT)}`, `{(cc_dir / 'blackapple_alerts.md').relative_to(REPO_ROOT)}`")
    lines.extend(summarize_blackapple(ba_rows))
    lines.append("")

    lines.append("### 1.2 Due Doubles")
    lines.append(f"- Artifacts: `{dd_csv.relative_to(REPO_ROOT)}`, `{(cc_dir / 'due_doubles.md').relative_to(REPO_ROOT)}`")
    lines.extend(summarize_due_doubles(dd_rows))
    lines.append("")

    lines.append("### 1.3 VTRAC Repeat Watch")
    lines.append(f"- Artifacts: `{vt_csv.relative_to(REPO_ROOT)}`, `{(cc_dir / 'vtrac_repeat_watch.md').relative_to(REPO_ROOT)}`")
    lines.extend(summarize_vtrac_repeat_watch(vt_rows))
    lines.append("")

    lines.append("## 2) Profit Alerts (A01-A12) daily evaluation")
    lines.append("")
    lines.append("Artifacts:")
    lines.append(f"- Board: `{(cc_dir / 'profit_alerts.csv').relative_to(REPO_ROOT)}`, `{(cc_dir / 'profit_alerts.md').relative_to(REPO_ROOT)}`")
    lines.append(f"- Eval: `{pa_eval_csv.relative_to(REPO_ROOT)}`, `{(cc_dir / 'profit_alerts_eval.md').relative_to(REPO_ROOT)}`")
    lines.append(f"- Merged: `{pa_merged_csv.relative_to(REPO_ROOT)}`")
    lines.append("")
    lines.append("Auto-summary (from eval CSV):")
    lines.extend(summarize_profit_eval(pa_rows))
    lines.append("")
    lines.append("Merged-episode summary:")
    lines.extend(summarize_profit_merged(merged_rows))
    lines.append("")
    lines.append("Top HIT merged episodes:")
    lines.extend(list_top_merged_hits(merged_rows))
    lines.append("")

    lines.append("## 3) Profitability framing (unitless, evaluation-only)")
    lines.append("")
    lines.append("Working definitions (v0):")
    lines.append("- `1 unit = 1 line played for 1 draw-step`")
    lines.append("- `episode_cost_units = implied_set_size * decay_max` (merged view)")
    lines.append("")
    lines.append("Notes:")
    lines.append("- Do not interpret this as ROI until you attach payout assumptions per venue/state.")
    lines.append("- Use it to compare relative cost pressure across alert types and windows.")
    lines.append("")

    lines.append("## 4) Cross-state synthesis (Brain-2 vs Brain-1)")
    lines.append("")
    lines.append("Fill:")
    lines.append("- Day environment class (short label): `...`")
    lines.append("- What Control Center signaled that Brain-1 agreed with: `...`")
    lines.append("- What Control Center signaled that Brain-1 contradicted: `...`")
    lines.append("")

    lines.append("## 5) Fix-now vs fix-later")
    lines.append("")
    lines.append("- Fix-now (pipeline correctness / drift / missing artifacts): `...`")
    lines.append("- Fix-later (tuning / hypothesis tests / evaluation lens changes): `...`")
    lines.append("- Next run: `...`")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
