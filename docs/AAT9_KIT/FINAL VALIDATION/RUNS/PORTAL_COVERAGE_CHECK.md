# Portal Coverage Sanity Check

Purpose: confirm that “important” RUNS doc families are reachable from `RUNS/PORTAL.md` without needing to remember filenames.

This check treats `PORTAL.md` as the entrypoint, and considers a doc “covered” if it is either:

- Explicitly linked in `PORTAL.md`, or
- Covered by one of the placeholder filename patterns shown in `PORTAL.md` (e.g., `<D>__<STATE>.md`, `<A>_to_<B>__CORPUS_DASHBOARD.md`).

This check ignores `.csv` / `.json` support files (they are usually paired with a `.md` summary).

---

## Summary

All key doc families used by the v0 synthesis + tool-by-tool integration process are covered by the portal (either explicitly or via the portal’s placeholder patterns).

The files that are **not** covered are almost entirely:

1) **Legacy predictive docs created before profile-suffixed naming stabilized** (missing `__tool_only` suffix).

2) **Per-day grades without the `__tool_only` suffix**, plus `__profit_only`/experiment variants (these exist for provenance/ablation, but the portal intentionally points you to the tool-first default surfaces).

3) A small number of one-off provenance files (e.g., `*_PREDICTION_BRIEF.md`).

None of these are required to run v0.2 tool-first workflows; they are safe to treat as historical artifacts unless you are doing provenance review.

---

## What’s uncovered (categories)

Counts from the current workspace:

- Legacy predictive state reports without profile suffix: 70
- Legacy predictive portfolio without profile suffix: 5
- Per-day grades without profile suffix: 10
- Per-day grades with non-tool-only suffixes (e.g., `__profit_only`, experiment labels): 10
- Per-day Aux badge matrix reports: 5
- Other one-offs: 27

Examples:

- Legacy predictive (pre v0.2 naming): `2026-01-05__NewJersey4__PREDICTIVE.md`
- Legacy predictive portfolio: `2026-01-05__PREDICTIVE_PORTFOLIO.md`
- Legacy grades: `2026-01-05__CANDIDATE_UNIVERSE_GRADE.md`
- Ablation grades: `2026-01-05__CANDIDATE_UNIVERSE_GRADE__profit_only.md`

---

## Guidance (so you don’t get lost)

- For current work, treat `__tool_only`-suffixed predictive + grade docs as canonical.
- Use `RUNS/INDEX.md` to find *any* file by date/state.
- Keep uncovered legacy docs as provenance; do not rename them unless you explicitly decide to do a naming migration.

---

## Re-run this check

If you want to re-run the coverage check:

```bash
python3 - <<'PY'
import re
from pathlib import Path

runs_dir = Path("docs/AAT9_KIT/FINAL VALIDATION/RUNS")
portal = runs_dir / "PORTAL.md"
text = portal.read_text(encoding="utf-8")

explicit = set()
for m in re.finditer(r"`([^`]+)`", text):
    p = m.group(1)
    if "FINAL VALIDATION/RUNS/" in p:
        explicit.add(Path(p).name)

patterns = [
    r"^\\d{4}-\\d{2}-\\d{2}__WINNERS_DIGEST\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__CONTROL_CENTER\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__DAY_SYNTHESIS\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__[A-Za-z0-9]+\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__PREDICTIVE_PORTFOLIO__tool_only\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__CANDIDATE_UNIVERSE_GRADE__tool_only\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__PLAY_CARD_GRADE__tool_only\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}__[A-Za-z0-9]+__PREDICTIVE__tool_only\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}_to_\\d{4}-\\d{2}-\\d{2}__CORPUS_DASHBOARD\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}_to_\\d{4}-\\d{2}-\\d{2}__CONVERGENCE_CASES\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}_to_\\d{4}-\\d{2}-\\d{2}__CONTROL_CENTER_ROLLUP\\.md$",
    r"^\\d{4}-\\d{2}-\\d{2}_to_\\d{4}-\\d{2}-\\d{2}__CODEX_DEEP_ANALYSIS\\.md$",
]
compiled = [re.compile(p) for p in patterns]

uncovered = []
for path in runs_dir.iterdir():
    if not path.is_file():
        continue
    name = path.name
    if name in explicit:
        continue
    if any(r.match(name) for r in compiled):
        continue
    if name.endswith(".csv") or name.endswith(".json"):
        continue
    uncovered.append(name)

print("uncovered count:", len(uncovered))
print("\\n".join(sorted(uncovered)[:50]))
PY
```

