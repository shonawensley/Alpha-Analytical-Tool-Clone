#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Results:
    midday: str | None
    evening: str | None


@dataclass(frozen=True)
class RunReportFacts:
    date: str
    state: str
    source_path: Path
    env_verdict: str | None
    drivers_midday: str | None
    drivers_evening: str | None
    drivers_overall: str | None
    pack_midday: str | None
    pack_evening: str | None
    pack_overall: str | None
    fix_later: str | None
    cross_variant_mentioned: bool


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _runs_dir(root: Path) -> Path:
    return root / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def _is_master_validation_run_report(path: Path) -> bool:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            first_line = f.readline()
    except Exception:
        return False
    return "Master Validation Run Report" in first_line


def _iter_run_reports(*, runs_dir: Path, dates: set[str] | None) -> Iterable[Path]:
    for path in sorted(runs_dir.glob("*.md")):
        name = path.name
        if not re.match(r"^\d{4}-\d{2}-\d{2}__.+\.md$", name):
            continue
        if name.endswith("__generated.md"):
            continue
        date, state_md = name.split("__", 1)
        state = state_md.removesuffix(".md")
        if state == "DAY_SYNTHESIS":
            continue
        if not _is_master_validation_run_report(path):
            continue
        if dates is not None and date not in dates:
            continue
        yield path


def _results_state_name(state: str) -> str:
    base = re.sub(r"\d+$", "", state)
    specials = {
        "NewYork": "New York",
        "NewJersey": "New Jersey",
        "NorthCarolina": "North Carolina",
        "SouthCarolina": "South Carolina",
        "PuertoRico": "Puerto Rico",
        "OntarioCanada": "Ontario",
        "WashingtonDC": "Washington, D.C.",
    }
    return specials.get(base, base)


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _parse_results_file(*, root: Path, date: str, states: set[str]) -> dict[str, Results]:
    path = root / "data" / "results" / f"{date}.txt"
    if not path.exists():
        return {s: Results(None, None) for s in states}

    lines = _read_text(path).splitlines()

    out: dict[str, Results] = {}
    for state in states:
        state_name = _results_state_name(state)
        midday = None
        evening = None
        for line in lines:
            if not re.match(rf"^\s*{re.escape(state_name)}(?:\s|\t)", line):
                continue

            if "\t" in line:
                parts = line.split("\t")
                midday_raw = parts[1].strip() if len(parts) > 1 else ""
                evening_raw = parts[2].strip() if len(parts) > 2 else ""
                midday_norm = _normalize_pick3_literal(midday_raw)
                evening_norm = _normalize_pick3_literal(evening_raw)
                if len(midday_norm) == 3 and midday_norm.isdigit():
                    midday = midday_norm
                if len(evening_norm) == 3 and evening_norm.isdigit():
                    evening = evening_norm
            else:
                nums = []
                for part in line.replace(",", " ").split():
                    literal = _normalize_pick3_literal(part)
                    if len(literal) == 3 and literal.isdigit():
                        nums.append(literal)
                if len(nums) >= 2:
                    midday, evening = nums[0], nums[1]
                elif len(nums) == 1:
                    midday, evening = nums[0], None
            break

        out[state] = Results(midday, evening)

    return out


def _extract_block(lines: list[str], start_idx: int, end_patterns: list[re.Pattern[str]], max_lines: int = 160) -> list[str]:
    out: list[str] = []
    for j in range(start_idx + 1, min(start_idx + 1 + max_lines, len(lines))):
        if any(p.search(lines[j]) for p in end_patterns):
            break
        out.append(lines[j])
    return out


def _find_first_index(lines: list[str], patterns: list[re.Pattern[str]]) -> int | None:
    for i, line in enumerate(lines):
        if any(p.search(line) for p in patterns):
            return i
    return None


def _extract_env_verdict(text: str) -> str | None:
    lines = text.splitlines()

    idx = _find_first_index(
        lines,
        [
            re.compile(r"Environment verdict", re.IGNORECASE),
            re.compile(r"Overall verdict", re.IGNORECASE),
        ],
    )
    if idx is None:
        return None

    line = lines[idx]
    bold = re.search(
        r"(?:Environment verdict[^:]*|Overall verdict)\s*:\s*\*\*([^*]+)\*\*",
        line,
        re.IGNORECASE,
    )
    if bold:
        return bold.group(1).strip()

    inline = re.search(r"(?:Environment verdict[^:]*|Overall verdict)\s*:\s*(.+)$", line, re.IGNORECASE)
    if inline:
        tail = inline.group(1).strip()
        if tail:
            return tail

    for j in range(idx + 1, min(idx + 9, len(lines))):
        m = re.search(r"\bOverall:\s*(.+)$", lines[j])
        if m:
            return m.group(1).strip()

    return None


def _extract_pack(lines: list[str]) -> tuple[str | None, str | None, str | None]:
    start_patterns = [
        re.compile(r"^- Pack vs winners:", re.IGNORECASE),
        re.compile(r"^###\s*5\.1\s+Pack vs winners", re.IGNORECASE),
    ]
    end_patterns = [
        re.compile(r"^- Key tags:", re.IGNORECASE),
        re.compile(r"^- Drivers:", re.IGNORECASE),
        re.compile(r"^- Conflicts:", re.IGNORECASE),
        re.compile(r"^###\s*5\.2\s+Key", re.IGNORECASE),
        re.compile(r"^###\s*5\.3\s+What drove", re.IGNORECASE),
        re.compile(r"^###\s*5\.4\s+Biggest", re.IGNORECASE),
        re.compile(r"^###\s*5\.5\s+Fix", re.IGNORECASE),
        re.compile(r"^- Fix-now", re.IGNORECASE),
    ]
    idx = _find_first_index(lines, start_patterns)
    if idx is None:
        return None, None, None

    block = _extract_block(lines, idx, end_patterns)
    cleaned = [b.strip().lstrip("-").strip() for b in block if b.strip()]

    midday = None
    evening = None
    for s in cleaned:
        if midday is None and re.search(r"\bMidday\b", s, re.IGNORECASE):
            midday = s
        if evening is None and re.search(r"\bEvening\b", s, re.IGNORECASE):
            evening = s
        if midday and evening:
            break

    overall = " | ".join([s for s in cleaned if len(s) <= 300]) if cleaned else None
    return midday, evening, overall


def _extract_drivers(lines: list[str]) -> tuple[str | None, str | None, str | None]:
    start_patterns = [
        re.compile(r"^- Drivers:", re.IGNORECASE),
        re.compile(r"^###\s*5\.3\s+What drove", re.IGNORECASE),
    ]
    end_patterns = [
        re.compile(r"^- Conflicts:", re.IGNORECASE),
        re.compile(r"^- Fix-now", re.IGNORECASE),
        re.compile(r"^###\s*5\.4\s+Biggest", re.IGNORECASE),
        re.compile(r"^###\s*5\.5\s+Fix", re.IGNORECASE),
    ]
    idx = _find_first_index(lines, start_patterns)
    if idx is None:
        return None, None, None

    block = _extract_block(lines, idx, end_patterns)

    cleaned = [b.strip().lstrip("-").strip() for b in block if b.strip().startswith("-")]
    if not cleaned:
        cleaned = [b.strip() for b in block if b.strip()]

    midday_lines: list[str] = []
    evening_lines: list[str] = []
    neutral_lines: list[str] = []

    for s in cleaned:
        if re.match(r"(?i)^midday\b", s):
            midday_lines.append(s)
        elif re.match(r"(?i)^evening\b", s):
            evening_lines.append(s)
        else:
            neutral_lines.append(s)

    overall = "; ".join(neutral_lines) if neutral_lines else None
    midday = "; ".join(midday_lines) if midday_lines else overall
    evening = "; ".join(evening_lines) if evening_lines else overall
    return midday, evening, overall


def _extract_fix_later(lines: list[str]) -> str | None:
    start_patterns = [
        re.compile(r"^- Fix-now vs fix-later:", re.IGNORECASE),
        re.compile(r"^###\s*5\.5\s+Fix-now", re.IGNORECASE),
    ]
    end_patterns = [
        re.compile(r"^- Next run:", re.IGNORECASE),
        re.compile(r"^###\s*5\.6", re.IGNORECASE),
    ]
    idx = _find_first_index(lines, start_patterns)
    if idx is None:
        return None

    block = _extract_block(lines, idx, end_patterns)
    cleaned = [b.strip().lstrip("-").strip() for b in block if b.strip()]

    fix_lines: list[str] = []
    capture = False
    for s in cleaned:
        if re.match(r"(?i)^fix-later", s):
            capture = True
            fix_lines.append(s)
            continue
        if capture:
            if re.match(r"(?i)^fix-now", s):
                continue
            if re.match(r"(?i)^next run", s):
                break
            if re.match(r"(?i)^fix-", s) and not s.lower().startswith("fix-later"):
                break
            if len(s) <= 240:
                fix_lines.append(s)

    if not fix_lines:
        return None

    if re.fullmatch(r"(?i)fix-later:\s*none\.?\s*", fix_lines[0]):
        return None

    return " | ".join(fix_lines)


def _parse_run_report(path: Path) -> RunReportFacts:
    name = path.name
    date, state_md = name.split("__", 1)
    state = state_md.removesuffix(".md")
    text = _read_text(path)
    lines = text.splitlines()

    env_verdict = _extract_env_verdict(text)
    drivers_midday, drivers_evening, drivers_overall = _extract_drivers(lines)
    pack_midday, pack_evening, pack_overall = _extract_pack(lines)
    fix_later = _extract_fix_later(lines)
    cross_variant = bool(re.search(r"cross-variant", text, re.IGNORECASE))

    return RunReportFacts(
        date=date,
        state=state,
        source_path=path,
        env_verdict=env_verdict,
        drivers_midday=drivers_midday,
        drivers_evening=drivers_evening,
        drivers_overall=drivers_overall,
        pack_midday=pack_midday,
        pack_evening=pack_evening,
        pack_overall=pack_overall,
        fix_later=fix_later,
        cross_variant_mentioned=cross_variant,
    )


def _write_csv(*, out_path: Path, rows: list[dict[str, str]]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out_path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def _write_fix_later_index(*, out_path: Path, items: list[tuple[str, str, str, str]]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Fix-Later Index (from Run Reports)")
    lines.append("")
    lines.append("This is an auto-extracted index of `Fix-later` notes from filled run reports.")
    lines.append("")
    lines.append("Source folder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`")
    lines.append("")

    by_date: dict[str, list[tuple[str, str, str]]] = {}
    for date, state, relpath, note in items:
        by_date.setdefault(date, []).append((state, relpath, note))

    for date in sorted(by_date.keys()):
        lines.append(f"## D={date}")
        lines.append("")
        for state, relpath, note in sorted(by_date[date], key=lambda t: t[0].lower()):
            lines.append(f"- `{state}`: {note}")
            lines.append(f"  - Source: `{relpath}`")
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    root = _repo_root()
    runs_dir = _runs_dir(root)

    parser = argparse.ArgumentParser(
        description="Export a machine-readable corpus summary from Master Validation run reports",
    )
    parser.add_argument(
        "--date",
        action="append",
        dest="dates",
        help="Results date D to include (repeatable). If omitted, includes all dates present in RUNS.",
    )
    parser.add_argument(
        "--out-csv",
        default=str(runs_dir / "corpus_summary.csv"),
        help="Output CSV path (default: RUNS/corpus_summary.csv)",
    )
    parser.add_argument(
        "--out-fix-later",
        default=str(runs_dir / "FIX_LATER_INDEX.md"),
        help="Output Fix-Later index path (default: RUNS/FIX_LATER_INDEX.md)",
    )
    args = parser.parse_args()

    dates: set[str] | None = set(args.dates) if args.dates else None

    report_paths = list(_iter_run_reports(runs_dir=runs_dir, dates=dates))
    if not report_paths:
        print("No run reports found.")
        return 1

    facts: list[RunReportFacts] = []
    for path in report_paths:
        facts.append(_parse_run_report(path))

    dates_in_scope = sorted({f.date for f in facts})
    states_in_scope = sorted({f.state for f in facts})

    results_by_date: dict[str, dict[str, Results]] = {
        d: _parse_results_file(root=root, date=d, states=set(states_in_scope)) for d in dates_in_scope
    }

    csv_rows: list[dict[str, str]] = []
    fix_later_items: list[tuple[str, str, str, str]] = []

    for f in sorted(facts, key=lambda x: (x.date, x.state.lower())):
        results = results_by_date.get(f.date, {}).get(f.state, Results(None, None))

        def add_period(period: str, winner: str | None, pack: str | None, drivers: str | None) -> None:
            csv_rows.append(
                {
                    "date": f.date,
                    "state": f.state,
                    "period": period,
                    "winner": winner or "",
                    "winner_missing": "1" if winner is None else "0",
                    "env_verdict": f.env_verdict or "",
                    "pack": pack or f.pack_overall or "",
                    "drivers": drivers or f.drivers_overall or "",
                    "cross_variant_mentioned": "1" if f.cross_variant_mentioned else "0",
                    "fix_later": f.fix_later or "",
                    "source_run_report": str(f.source_path.relative_to(root)),
                }
            )

        add_period("Midday", results.midday, f.pack_midday, f.drivers_midday)
        add_period("Evening", results.evening, f.pack_evening, f.drivers_evening)

        if f.fix_later:
            fix_later_items.append((f.date, f.state, str(f.source_path.relative_to(root)), f.fix_later))

    _write_csv(out_path=Path(args.out_csv), rows=csv_rows)
    _write_fix_later_index(out_path=Path(args.out_fix_later), items=fix_later_items)

    print(f"Wrote CSV: {args.out_csv}")
    print(f"Wrote Fix-Later index: {args.out_fix_later}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
