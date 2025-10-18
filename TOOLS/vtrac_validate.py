#!/usr/bin/env python3
# tools/vtrac_validate.py

import argparse
import json
import re
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime, timezone

import pandas as pd

# -----------------------------
# Utilities: V-TRAC mapping and helpers
# -----------------------------

# V-TRAC digit groups from your training guide:
# VTrac 1: {0,5}; VTrac 2: {1,6}; VTrac 3: {2,7}; VTrac 4: {3,8}; VTrac 5: {4,9}
VTRAC_MAP = {
    "0": "1", "5": "1",
    "1": "2", "6": "2",
    "2": "3", "7": "3",
    "3": "4", "8": "4",
    "4": "5", "9": "5",
}

DIGIT_RE = re.compile(r"[0-9]+")

def only_digits(s: str) -> str:
    if not isinstance(s, str):
        s = "" if pd.isna(s) else str(s)
    return "".join(ch for ch in s if ch.isdigit())

def count_hot_symbols(s: str) -> tuple[int, int]:
    """Return (#hot, #superhot) counting '*' and '**' tokens in a cell string."""
    if not isinstance(s, str):
        s = "" if pd.isna(s) else str(s)
    # Count '**' first, then remaining '*'
    superhot = s.count("**")
    # Remove '**' pairs to avoid double counting as single *
    tmp = s.replace("**", "")
    hot = tmp.count("*")
    return hot, superhot

def vtrac_sequence(s: str) -> str:
    """
    Map a numeric string to a sequence of V-TRAC groups, preserving order.
    Example: '6411' -> 'V2442' (6->2,4->5,1->2,1->2) ; we prefix 'V' to make it explicit.
    """
    digits = only_digits(s)
    if not digits:
        return "V"
    mapped = "".join(VTRAC_MAP.get(ch, "") for ch in digits)
    return "V" + mapped

def vtrac_box_signature(s: str) -> str:
    """
    Unordered 3-value signature using V-TRAC classes.
    We reduce to at most three distinct classes, sorted, e.g. '6411' -> 'V{2,5}' -> 'V255' (multiset flavor).
    For stability we encode as sorted counts of classes seen (compressed to <=3 distinct).
    """
    digits = only_digits(s)
    if len(digits) < 3:
        return ""  # not enough material for a 3-value candidate
    classes = [VTRAC_MAP.get(ch, "") for ch in digits]
    classes = [c for c in classes if c]  # drop unknown
    if not classes:
        return ""
    ctr = Counter(classes)
    # keep up to three most common classes (ties by class id for determinism)
    top = sorted(ctr.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
    # Encode as "V" + class+count pairs, e.g. [('2',3),('5',2)] -> 'V2x3_5x2'
    return "V" + "_".join(f"{cls}x{cnt}" for cls, cnt in top)

def is_three_value_candidate(s: str) -> bool:
    """
    Decide if a string qualifies as a 3-value candidate per your rule:
    - >=3 total digits AND
      (<=3 unique raw digits OR <=3 unique V-TRAC classes).
    """
    digits = only_digits(s)
    if len(digits) < 3:
        return False
    uniq_raw = set(digits)
    if len(uniq_raw) <= 3:
        return True
    classes = {VTRAC_MAP.get(ch, "") for ch in digits}
    classes.discard("")  # remove unknown just in case
    return len(classes) <= 3

# -----------------------------
# HTML discovery and parsing
# -----------------------------

def parse_tables_with_stdlib(html_path: Path) -> list[pd.DataFrame]:
    """
    Fallback HTML table parser that relies only on the standard library.
    It walks <table>/<tr>/<th>/<td> tags and produces pandas DataFrames.
    """
    class _TableParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.tables: list[list[list[str]]] = []
            self._current_table: list[list[str]] | None = None
            self._current_row: list[str] | None = None
            self._current_cell: list[str] | None = None

        def handle_starttag(self, tag, attrs):
            tag = tag.lower()
            if tag == "table":
                self._current_table = []
                self.tables.append(self._current_table)
            elif tag == "tr" and self._current_table is not None:
                self._current_row = []
                self._current_table.append(self._current_row)
            elif tag in {"td", "th"} and self._current_row is not None:
                self._current_cell = []
            elif self._current_cell is not None:
                self._current_cell.append(" ")

        def handle_endtag(self, tag):
            tag = tag.lower()
            if tag == "table":
                self._current_table = None
            elif tag == "tr":
                self._current_row = None
            elif tag in {"td", "th"} and self._current_row is not None and self._current_cell is not None:
                text = "".join(self._current_cell).strip()
                self._current_row.append(text)
                self._current_cell = None
            elif self._current_cell is not None:
                self._current_cell.append(" ")

        def handle_data(self, data):
            if self._current_cell is not None:
                self._current_cell.append(data)

    parser = _TableParser()
    parser.feed(html_path.read_text(encoding="utf-8", errors="ignore"))
    dfs: list[pd.DataFrame] = []
    for table in parser.tables:
        rows = [[cell.strip() for cell in row] for row in table if row]
        if not rows:
            continue
        header = rows[0]
        lower_header = [h.lower() for h in header]
        header_has_labels = any("set" in h or "draw" in h or "row" in h for h in lower_header)
        data_rows = rows[1:] if header_has_labels else rows
        if header_has_labels:
            col_names = header[:]
        else:
            width = max(len(row) for row in rows)
            col_names = [f"col_{idx+1}" for idx in range(width)]
        width = max(len(col_names), max((len(row) for row in data_rows), default=len(col_names)))
        if len(col_names) < width:
            extra = [f"col_{idx+1}" for idx in range(len(col_names), width)]
            col_names = col_names + extra
        padded = [row + [""] * (len(col_names) - len(row)) for row in data_rows]
        df = pd.DataFrame(padded, columns=col_names)
        if not df.empty:
            dfs.append(df)
    return dfs

def find_winners_html(state: str, winners_dir: Path | None) -> list[Path]:
    """
    Locate Winners Logger HTML files for a state.
    Default search:
      - data/outputs/analysis/winners/<STATE>/**/*.html
      - data/outputs/winners/*/vtrac_reports/<STATE>/**/*.html
    """
    roots: list[Path] = []
    if winners_dir:
        roots.append(Path(winners_dir))
    else:
        roots.append(Path("data/outputs/analysis/winners") / state)
        roots.append(Path("data/outputs/winners"))
    htmls: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        if "vtrac_reports" in str(root):
            # Compact path layout
            htmls.extend(root.rglob("*.html"))
        else:
            # Analysis winners layout
            htmls.extend((root).rglob("*.html"))
    # De-duplicate and prefer newest first
    htmls = sorted(set(htmls), key=lambda p: p.stat().st_mtime, reverse=True)
    return htmls

def read_three_tables_from_html(html_path: Path) -> tuple[list[pd.DataFrame], list[pd.DataFrame]]:
    """
    Attempt to read the Winners Logger's 3 big tables (Midday, Evening, Combined).
    pandas.read_html returns a list; we heuristically keep the 3 widest tables.
    """
    try:
        tables = pd.read_html(html_path, flavor="lxml")
    except Exception:
        try:
            tables = pd.read_html(html_path)
        except Exception:
            tables = parse_tables_with_stdlib(html_path)
    # Keep tables that have the expected R2/R4/R6/R8 vocabulary in a 'RowType' column (or similar)
    scored = []
    for df in tables:
        cols = [str(c).strip().lower() for c in df.columns]
        if any("rowtype" in c for c in cols) or any("draw" == c for c in cols) or any(c in {"7","6","5","4","3","2","1"} for c in cols):
            scored.append((df.shape[1], df))
    # pick up to 3 widest
    top = [df for _, df in sorted(scored, key=lambda kv: -kv[0])[:3]]
    return top, tables


def extract_straight_occurrences(all_tables: list[pd.DataFrame]) -> dict[str, int]:
    """
    Locate the 'Straight Combination Occurrences' table and return {pattern: count}.
    """
    for df in all_tables:
        columns = [str(c).strip().lower() for c in df.columns]
        if len(columns) != 2:
            continue
        if columns[0] == "pattern" and "straight" in columns[1]:
            occurrences: dict[str, int] = {}
            for _, row in df.iterrows():
                pattern = str(row[df.columns[0]]).strip()
                try:
                    count = int(str(row[df.columns[1]]).strip())
                except ValueError:
                    continue
                occurrences[pattern] = count
            return occurrences
    return {}

# -----------------------------
# Winners-table signal extraction
# -----------------------------

R_ROWS = {"R2", "R4", "R6", "R8"}
COL_LABELS = ["7","6","5","4","3","2","1"]

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Make column labels consistent
    df2 = df.copy()
    df2.columns = [str(c).strip() for c in df2.columns]
    # Ensure presence of key columns
    # We try common spellings seen in screenshots: 'Set','Draw','RowType'
    # If missing, attempt to infer from first columns
    if "Set" not in df2.columns:
        # Heuristic: first column
        df2.rename(columns={df2.columns[0]: "Set"}, inplace=True)
    if "Draw" not in df2.columns:
        df2.rename(columns={df2.columns[1]: "Draw"}, inplace=True)
    if "RowType" not in df2.columns:
        df2.rename(columns={df2.columns[2]: "RowType"}, inplace=True)
    return df2

def extract_signals_from_table(df_raw: pd.DataFrame) -> dict:
    """
    Compute hot/superhot, consensus, and top V-TRAC signatures for Set1/Draw1.
    """
    df = normalize_columns(df_raw)
    # Filter Set1 / Draw1 and the four R2,R4,R6,R8 rows
    mask = (df["Set"].astype(str).str.contains("Set1", case=False, na=False)) & \
           (df["Draw"].astype(str).str.contains("Draw1", case=False, na=False)) & \
           (df["RowType"].astype(str).isin(R_ROWS))
    block = df.loc[mask, ["RowType"] + [c for c in COL_LABELS if c in df.columns]].copy()
    signals: dict = {
        "hot": 0,
        "superhot": 0,
        "consensus_col1": False,
        "consensus_col2": False,
        "stable_columns": [],  # columns where a 3-value V-TRAC signature is common in >=3 of 4 rows
        "top_vtrac_box_signatures": [],  # frequency across all cells
    }
    if block.empty:
        return signals

    # Hot/superhot
    hot = superhot = 0
    for col in block.columns:
        if col in {"RowType"}:
            continue
        for val in block[col].astype(str).tolist():
            h, sh = count_hot_symbols(val)
            hot += h
            superhot += sh
    signals["hot"], signals["superhot"] = hot, superhot

    # Consensus: in col '1' or '2', if present, check if ALL four R* rows are <3 digits
    for target_col, key in (("1", "consensus_col1"), ("2", "consensus_col2")):
        if target_col in block.columns:
            vals = [only_digits(v) for v in block[target_col].astype(str).tolist()]
            if len(vals) == 4 and all(0 < len(v) < 3 for v in vals):
                signals[key] = True

    # Column-wise stability: if >=3 of the 4 rows share the same 3-value V-TRAC box signature
    stable_cols: list[str] = []
    for col in [c for c in COL_LABELS if c in block.columns]:
        sigs = []
        for v in block[col].astype(str).tolist():
            if is_three_value_candidate(v):
                sigs.append(vtrac_box_signature(v))
        # retain non-empty
        sigs = [s for s in sigs if s]
        if not sigs:
            continue
        top, cnt = Counter(sigs).most_common(1)[0]
        if cnt >= 3:
            stable_cols.append(col)
    signals["stable_columns"] = stable_cols

    # Global top V-TRAC box signatures across all Set1/Draw1 cells
    all_sigs: Counter = Counter()
    for col in [c for c in COL_LABELS if c in block.columns]:
        for v in block[col].astype(str).tolist():
            if is_three_value_candidate(v):
                all_sigs.update([vtrac_box_signature(v)])
    top_box = [sig for sig, _ in all_sigs.most_common(12) if sig]
    signals["top_vtrac_box_signatures"] = top_box
    return signals

# -----------------------------
# Analyzer JSON ingestion (optional)
# -----------------------------

def find_latest_json(analysis_dir: Path) -> Path | None:
    if not analysis_dir.exists():
        return None
    cands = sorted(analysis_dir.rglob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return cands[0] if cands else None

def load_analyzer_json(path: Path | None) -> dict:
    if not path or not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def extract_analyzer_details(blob: dict) -> dict:
    """
    Pull section-level signatures, metrics, and straight rankings from analyzer JSON.
    """
    details = {
        "signatures": {},
        "metrics": {},
        "section_straights": {},
        "global_top_straights": [],
    }
    if not isinstance(blob, dict):
        return details

    section_payload = blob.get("section_summaries")
    if isinstance(section_payload, dict):
        for section, data in section_payload.items():
            if not isinstance(data, dict):
                continue
            sigs = data.get("top_box_signatures")
            if isinstance(sigs, list):
                details["signatures"][section] = sorted(
                    s for s in sigs if isinstance(s, str)
                )
            metrics = data.get("analyzer_metrics")
            if isinstance(metrics, dict):
                details["metrics"][section] = metrics
                straights = metrics.get("top_straights")
                if isinstance(straights, list):
                    details["section_straights"][section] = straights

    generic: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
        elif isinstance(node, str):
            if re.match(r"^V[1-5](x\\d+)(_([1-5]x\\d+))*$", node):
                generic.add(node)

    walk(blob)
    if generic:
        details.setdefault("signatures", {}).setdefault("__global__", [])
        # Merge and deduplicate
        merged = set(details["signatures"].get("__global__", []))
        merged.update(generic)
        details["signatures"]["__global__"] = sorted(merged)

    global_top = blob.get("top_straights")
    if isinstance(global_top, list):
        details["global_top_straights"] = [
            straight for straight in global_top if isinstance(straight, str)
        ]
    return details

# -----------------------------
# Report writing
# -----------------------------

def write_json(out_path: Path, obj: dict):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(obj, indent=2), encoding="utf-8")

def write_markdown(out_path: Path, summary: dict):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append(f"# V-TRAC Validation Report -- {summary['state']}")
    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    lines.append(f"_Generated: {generated}_")
    lines.append("")

    winners_html = summary.get("winners_html") or []
    if winners_html:
        lines.append("**Winners HTML files considered (newest first):**")
        for p in winners_html[:5]:
            lines.append(f"- {p}")
        if len(winners_html) > 5:
            lines.append(f"- ... (+{len(winners_html) - 5} more)")
        lines.append("")

    straight_occurrences: dict[str, int] = summary.get("straight_occurrences") or {}
    if straight_occurrences:
        non_zero = [
            pattern for pattern, count in straight_occurrences.items() if count
        ]
        lines.append("**Straight Combination Occurrences (HTML):**")
        lines.append(
            "- Non-zero straights: {}".format(
                ", ".join(sorted(non_zero)) if non_zero else "--"
            )
        )
        lines.append("")

    analyzer_global_top = summary.get("analyzer_global_top_straights") or {}
    if analyzer_global_top:
        lines.append("**Analyzer global top straights (per source):**")
        for label in sorted(analyzer_global_top):
            straights = analyzer_global_top[label]
            preview = ", ".join(straights[:8]) if straights else "--"
            lines.append(f"- {label}: {preview}")
        lines.append("")

    html_straight_hits = {
        pattern for pattern, count in straight_occurrences.items() if count
    }

    for section in ("Midday", "Evening", "Combined"):
        sec = summary["sections"].get(section, {})
        lines.append(f"## {section}")
        if not sec:
            lines.append("_No table parsed._")
            lines.append("")
            continue
        sigs = sec["signals"]
        lines.append(f"- Hot cells: **{sigs['hot']}**, Super-hot: **{sigs['superhot']}**")
        lines.append(f"- Consensus col1: **{sigs['consensus_col1']}**, col2: **{sigs['consensus_col2']}**")
        lines.append(f"- Stable columns (>=3/4 rows share a 3-value V-TRAC signature): `{','.join(sigs['stable_columns']) or 'none'}`")
        lines.append(f"- Top V-TRAC box signatures in Set1/Draw1 cells: `{', '.join(sigs['top_vtrac_box_signatures']) or 'none'}`")
        # Overlap if analyzer signatures present
        w_sigs = set(sec['signals']['top_vtrac_box_signatures'])
        analyzer_sig_map = sec.get("analyzer_signatures", {})
        if isinstance(analyzer_sig_map, dict) and analyzer_sig_map:
            lines.append("- Analyzer <-> Winners overlaps by source:")
            for label in sorted(analyzer_sig_map):
                a_sigs = set(analyzer_sig_map[label])
                inter = sorted(a_sigs & w_sigs)
                lines.append(f"  - {label}: **{len(inter)}** -> {', '.join(inter) if inter else '--'}")
        analyzer_metrics_map = sec.get("analyzer_metrics", {})
        analyzer_straights_map = sec.get("analyzer_straights", {})
        if isinstance(analyzer_metrics_map, dict) and analyzer_metrics_map:
            lines.append("- Analyzer metrics:")
            for label in sorted(analyzer_metrics_map):
                metrics = analyzer_metrics_map.get(label, {})
                lines.append(
                    "  - {}: indices={} mask_drop={} reduction_hits={} mirror_supported={} double_hits={}".format(
                        label,
                        metrics.get("indices_considered", 0),
                        metrics.get("mask_drop_count", 0),
                        metrics.get("reduction_hits", 0),
                        metrics.get("mirror_supported", 0),
                        metrics.get("double_hits", 0),
                    )
                )
                straights = analyzer_straights_map.get(label, [])
                if straights:
                    straight_preview = ", ".join(
                        f"{item.get('straight')}({item.get('score', 0):.2f})"
                        for item in straights[:6]
                        if item.get("straight")
                    )
                    matches = [
                        item.get("straight")
                        for item in straights
                        if item.get("straight") in html_straight_hits
                    ]
                    lines.append(f"    straights: {straight_preview or '--'}")
                    lines.append(
                        f"    straight overlap: **{len(matches)}** -> {', '.join(matches) if matches else '--'}"
                    )
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")

# -----------------------------
# Main
# -----------------------------

def main():
    ap = argparse.ArgumentParser(description="Validate V-TRAC analyzer evidence against Winners Logger HTML.")
    ap.add_argument("--state", required=True, help="State folder, e.g., Delaware4")
    ap.add_argument("--winners-dir", default=None, help="Override winners HTML root directory")
    ap.add_argument("--analysis-dir", default=None, help="Override analyzer JSON root directory (search newest JSON)")
    ap.add_argument("--analysis-json", default=None, help="Explicit analyzer JSON file to compare")
    ap.add_argument("--analysis-json-a", default=None, help="Analyzer JSON A for A/B comparison")
    ap.add_argument("--analysis-json-b", default=None, help="Analyzer JSON B for A/B comparison")
    ap.add_argument("--label-a", default="A", help="Label for analyzer JSON A (default: A)")
    ap.add_argument("--label-b", default="B", help="Label for analyzer JSON B (default: B)")
    args = ap.parse_args()

    state = args.state
    winners_htmls = find_winners_html(state, Path(args.winners_dir) if args.winners_dir else None)

    # Discover analyzer JSON entries
    analyzer_paths: dict[str, Path] = {}
    if args.analysis_json_a or args.analysis_json_b:
        if args.analysis_json_a:
            p = Path(args.analysis_json_a)
            if p.exists():
                analyzer_paths[args.label_a] = p
        if args.analysis_json_b:
            p = Path(args.analysis_json_b)
            if p.exists():
                analyzer_paths[args.label_b] = p
    elif args.analysis_json:
        p = Path(args.analysis_json)
        if p.exists():
            analyzer_paths["primary"] = p
    else:
        root = Path(args.analysis_dir) if args.analysis_dir else Path("data/outputs/analysis/vtrac") / state
        auto = find_latest_json(root)
        if auto:
            analyzer_paths["primary"] = auto

    analyzer_details_map: dict[str, dict] = {}
    for label, path in list(analyzer_paths.items()):
        blob = load_analyzer_json(path)
        analyzer_details_map[label] = extract_analyzer_details(blob)

    # Parse up to newest HTML file that yields 3 tables
    sections = ["Midday", "Evening", "Combined"]
    parsed = {}
    picked_html = None
    all_tables: list[pd.DataFrame] = []
    for html in winners_htmls:
        tables, all_tables = read_three_tables_from_html(html)
        if len(tables) >= 3:
            picked_html = html
            for i, section in enumerate(sections):
                sigs = extract_signals_from_table(tables[i])
                # Section-specific analyzer signatures (currently global view)
                section_signature_view: dict[str, list[str]] = {}
                section_metrics_view: dict[str, dict] = {}
                section_straights_view: dict[str, list[dict]] = {}
                for label, detail in analyzer_details_map.items():
                    signatures_map = detail.get("signatures", {})
                    metrics_map = detail.get("metrics", {})
                    straights_map = detail.get("section_straights", {})
                    if section in signatures_map:
                        section_signature_view[label] = signatures_map[section]
                    elif "__global__" in signatures_map:
                        section_signature_view[label] = signatures_map["__global__"]
                    else:
                        section_signature_view[label] = []
                    if section in metrics_map:
                        section_metrics_view[label] = metrics_map[section]
                    if section in straights_map:
                        section_straights_view[label] = straights_map[section]
                parsed[section] = {
                    "signals": sigs,
                    "analyzer_signatures": section_signature_view,
                    "analyzer_metrics": section_metrics_view,
                    "analyzer_straights": section_straights_view,
                }
            break
    straight_occurrences = extract_straight_occurrences(all_tables) if picked_html else {}

    out_root = Path("data/outputs/analysis/vtrac_validation") / state
    summary = {
        "state": state,
        "winners_html": [str(p) for p in winners_htmls],
        "picked_html": str(picked_html) if picked_html else None,
        "analyzer_jsons": {label: str(path) for label, path in analyzer_paths.items()},
        "sections": parsed,
        "straight_occurrences": straight_occurrences,
        "analyzer_global_top_straights": {
            label: detail.get("global_top_straights", [])
            for label, detail in analyzer_details_map.items()
        },
    }
    write_json(out_root / "validation_report.json", summary)
    write_markdown(out_root / "validation_report.md", summary)

    # Console summary
    console_summary = {
        "state": state,
        "picked_html": summary["picked_html"],
        "analyzer_jsons": summary["analyzer_jsons"],
        "midday_top": parsed.get("Midday", {}).get("signals", {}).get("top_vtrac_box_signatures", [])[:6],
        "evening_top": parsed.get("Evening", {}).get("signals", {}).get("top_vtrac_box_signatures", [])[:6],
        "combined_top": parsed.get("Combined", {}).get("signals", {}).get("top_vtrac_box_signatures", [])[:6],
    }
    if analyzer_details_map:
        console_summary["analyzer_labels"] = list(analyzer_details_map.keys())
    print(json.dumps(console_summary, indent=2))
    print(f"\nWrote: {out_root/'validation_report.json'}")
    print(f"Wrote: {out_root/'validation_report.md'}")

if __name__ == "__main__":
    main()
