[#] DO NOT DELETE ITEMS ONCE ADDED — APPEND / CHECK OFF IN NEW SECTIONS

# AAT9 — Final Validation Checklist

Purpose: Running list of important considerations, caveats, and “don’t forget this” items for the AAT9 master validation and final workflow wiring. Use this alongside `AAT9_Final_Validation_Help.md` when a new Codex session starts master validation.

---

## 1. Tables / Results / Winners Pipeline

- History → Tables/JSON:
  - Always use `run_tables_with_guard.py` with a specific `Pick3StatsC4_YYYY-MM-DD.xlsm` history workbook.
  - Confirm `data/outputs/tables/tables_manifest.json` matches the active workbook (path, mtime, size).
  - Guard: Set1/Draw1 in `Combined_Combined` must reflect the history file’s most recent draw; results will always be history+1 day.
- Results (day-ahead) → Winners:
  - Results date = history date + 1 (e.g., history 2025‑06‑21 → results `data/results/2025‑06‑22.txt` → `reports/stable/winners_by_date/2025‑06‑22/`).
  - Winners directories are per-date and never reused; winners_by_date is safe to treat as per-date truth when Stage 1/2 have been run.
- Stage‑1/2 pipeline is already well-documented in:
  - `AAT9_String_Table_Testing.md`
  - `AAT9_Master_Validation_Preflight.md`
  - `AAT9_Table_Swap_Verification.md`
  - `AAT9_Final_Validation_Help.md`

## 2. Digit Reduction — Live Outputs vs Snapshots

- Live DR outputs (`data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/...`) are **ephemeral**:
  - Each new `run_digit_reduction_workflow` call overwrites the analyzer outputs and winners overlays for that state with the **latest** results date.
  - It is safe to inspect them immediately after a run for that (history, results) pair within the same session.
  - It is **not** safe to assume that these live files still correspond to an older results date after running additional dates.
- Dated DR snapshots / sharepacks are the only safe long-term per-date bundles:
  - Use `sharepacks/DR_<RESULTS_DATE>/` or a similar `digit_reduction_snapshots/<RESULTS_DATE>/` layout.
  - For each date where deep analysis is needed:
    - Run DR once with the correct history/results active.
    - Immediately copy at least:
      - `<STATE>_analyzer_v2_per_item.csv`
      - `<STATE>_analyzer_v2_top_candidates.csv`
      - `<STATE>_analyzer_v2_meta.json`
      - `analyzer_v2/winners/<STAMP>_*_winner_{overlay.html,flags.csv,hits.csv,map.json,stamp.json}`
    - Write a small manifest alongside, e.g.:
      ```json
      {
        "history_date": "2025-06-21",
        "results_date": "2025-06-22",
        "states": ["Connecticut4", "Delaware4", "..."],
        "tables_manifest": "data/outputs/tables/tables_manifest.json",
        "winners_root": "reports/stable/winners_by_date/2025-06-22/",
        "dr_snapshot_root": "sharepacks/DR_2025-06-22/",
        "dr_config_hash": "<from meta.json>"
      }
      ```
  - When writing analysis entries (in `AAT9_Digit_Analysis_Log_Part2.md` or master validation docs), always reference:
    - the `history_date`,
    - the `results_date`,
    - the winners_by_date path,
    - and the DR snapshot root.
  - Rule of thumb: “If it’s not in a dated snapshot/sharepack, treat it as live and potentially overwritten; only treat dated folders as per-date DR evidence.”

## 3. Master Validation Kickoff — Doc Scan

- Before starting aggregator design or combining tools, always:
  - Read `AAT9_Final_Validation_Help.md` (ENTRY point) to recall Stage‑1/2 pipeline and tool batch commands.
  - Use the “Master Validation Docs — Quick Index” section in that file to find:
    - Core wiring docs (KIT README, Workflow Standard, Live Wiring, Macro Roadmap).
    - Tool analysis logs (DR/Stable/V‑TRAC/Hot Zones).
    - Roadmaps and checkpoints (Aux Roadmap, Checkpoint Log, Unified Changelog, Analysis Insights).
    - Winners/aggregator docs (Winners Module, Winners VTRAC Report).
    - Optional architecture docs (ARCHITECTURE_AAT9, module_A/B/C/D, AAT9_Roadmap_2025‑09‑03_Winners_Logging_and_Health).
  - Build an “Open hooks to consider in aggregator” list based on “Next / Follow-ups” sections in those docs.
    - Example hooks:
      - Aux V‑TRAC index “due” summary based on `cached_aux_analysis(state)["vstat"]` and thresholds in `core/aux_config.py` (can be a UI summary and an Aux feature via `aux_features.extract`).
      - Stable/V‑TRAC/Hot Zones cross-signals (shared VT families, late-column overlaps, common hot zones).
      - Any documented environment-quality metrics (primary/support/skip states) from the DR and Stable logs.

## 4. Brain vs Projector — Outputs vs Internal Logic

- “Brain” = code + configs + internal features:
  - Digit Reduction: reducer, Analyzer V2, ladder windows, V‑TRAC features, scoring_v2, lockscore, config.yml.
  - Stable Pattern: extractor, persistence logic, family/compound scoring.
  - V‑TRAC Analyzer: evidence grid, straight scoring, ring/column weights, compact report.
  - Hot Zones: JSON tables scanner, EB/ES/VB/VS lanes, lane scoring.
- “Projector” = HTML/CSVs/overlays used for human explanation and QA:
  - Winners HTML/JSON (3‑table view).
  - DR overlays + winner maps/hits/flags.
  - Stable spotlight reports.
  - V‑TRAC validation reports and compact summaries.
  - Hot Zones winner maps and lane reports.
- For master validation and aggregator design:
  - Prefer driving logic off the **lean outputs** (per_item/top/meta + compact reports) defined in `AAT9_Analyzer_Lean_Outputs.md`.
  - Use projector outputs mainly to explain and debug why a candidate scored as it did.
  - It’s acceptable (and expected) that some projector outputs are pruned or merged in the final workflow as long as the core “brain” features are preserved in the lean outputs.

## 5. Master Validation / Aggregator Design Notes

- Winners HTML/JSON as environment primer:
  - For deep example runs, always start with the winners HTML/JSON (or its JSON twin) as **Phase A**:
    - Describe how the winner walks through the 3 tables (Set3→Set2→Set1 across Midday/Evening/Combined).
    - Note LS1/LS2 positions, VT families, long-string boxes, and which hit criteria (exact, box, VT-boxed, VT-straight) fire where.
  - Only after that primer should tools’ analyzer outputs be reviewed (DR/Stable/V-TRAC/Hot Zones) to see if they “see” the same environment.

- Four hit criteria as the profit axis:
  - Treat the 4 hit criteria as the core lens for profitability:
    - Exact straight
    - Boxed (any order)
    - VT-boxed (family cluster)
    - VT-straight (value-track straight signatures)
  - For each state/day, ask:
    - “Which criteria are strongly lit in this environment?”
    - “If we only play when at least one criterion is strongly lit, what is our hit frequency / ROI in backtests?”
  - Tools should be evaluated partly on:
    - How well they surface environments where at least one criterion is promising.
    - How well they suppress environments where none of the criteria look favorable.

- Gold example days (“broad then lean” strategy):
  - Before compressing features, identify a small set of **gold days** spanning different regimes:
    - VT-straight heavy days
    - VT-boxed heavy days
    - Boxed-heavy but messy days
    - “Do not play” days (weak LS/VT structure)
  - For each gold day and a handful of states:
    - Freeze sharepacks (winners HTML/JSON + DR/Stable/V-TRAC/Hot Zones outputs).
    - Write short environment-focused notes (e.g., “LS1 spine + VT-family X dominated”, “LS2/VT-only lanes rescued patterns”, “should not have played”).
  - Use these gold days as the seed dataset for aggregator feature design and gating rules.

- Aggregator Contract v0 (per-tool feature list):
  - Before coding the aggregator, draft a short “Aggregator Contract v0” listing, for each tool (DR, Stable, V-TRAC, Aux), a minimal set (~5–7) of:
    - Per-candidate features (e.g., DR primary score, LS zone, VT signal strength, progression flag).
    - Per-environment features (e.g., environment quality flags, cluster intensity, convergence/consensus).
  - This contract should be based on:
    - What actually correlated with hits in the gold example days.
    - The tool-specific analysis logs and roadmaps (see Section 3 for where to read).
  - The aggregator should consume these compressed features rather than raw tool outputs; projector files remain for explanation, not for core scoring.

## 6. Hot Zones as Environment Radar (Aggregator View)

- Hot Zones is a first-class AAT9 tool, wired via:
  - Inputs: `data/outputs/json_tables/<STATE>_tables.json`
  - Outputs: per-lane (`<STATE>_hot_zones_per_lane.csv`), top lanes (`<STATE>_hot_zones_top_lanes.csv`), meta (`<STATE>_hot_zones_meta.json`), and winners maps (`YYYYMMDD_hot_zones_winner_map.{json,csv}`).
- For the aggregator, treat Hot Zones primarily as **environment radar**, not another heavy per-candidate scorer:
  - Lane-level primitives to consider:
    - `HZ_LANE_ID`: natural lane identifier (index/band/mask).
    - `HZ_SCORE` / `HZ_RANK`: how hot that lane is today.
    - `HZ_VARIANT_COVERAGE`: in how many variants (Combined/Midday/Evening) the lane is hot.
    - `HZ_WINNER_HIT_FLAG`: whether today’s winner fell inside this lane (from the Hot Zones winner map).
  - Cross-tool overlap flags (per lane or candidate):
    - `HZ_OVERLAP_DR`: lane overlaps DR LS1/LS2/ladder boxes that scored well.
    - `HZ_OVERLAP_VTRAC`: lane overlaps V-TRAC hot/super-hot families or straights.
    - `HZ_OVERLAP_STABLE`: lane overlaps Stable high-persistence/score patterns.
    - (Optional) `HZ_OVERLAP_AUX`: lane aligns with Aux positional/doubles pressure across variants.
  - Day-level environment descriptors:
    - `HZ_TOP_LANE_SCORE` / `HZ_TOP_LANE_RANK`: extremity of the hottest lane.
    - `HZ_CONSENSUS_LANE_COUNT`: count of lanes that are both hot and overlapping DR/V-TRAC/Stable.
    - `HZ_ENVIRONMENT_CLASS`: coarse label like “Calm” (no strong consensus), “Focused” (few strong consensus lanes), “Noisy” (many hot lanes, little agreement).
- In master validation, use these to:
  - Identify “consensus environments” where DR + V-TRAC + Stable + Hot Zones all like the same lane (prime play candidates).
  - Flag days where Hot Zones is noisy or flat so the aggregator demands more consensus or stands down.

## 7. Aggregator Wiring Docs (Tool Index & Inbox)

- AAT9 already has strong wiring and lean-output docs; before or during master validation it can help to make the aggregator wiring explicit:
  - **Tool Index in Live Wiring** (optional but helpful):
    - In `AAT9_Live_Wiring_and_Data_Paths.md`, keep or add a small table listing, for each wired tool:
      - Entry point (module / Streamlit tab).
      - Inputs (tables/JSON/draws).
      - Primary outputs (lean bundles under `data/outputs/analysis/...`).
      - Example aggregator-facing fields (score, VT/LS flags, lane IDs, aux pressure flags).
  - **Aggregator Inbox mini-spec** (can live in `AAT9_Analyzer_Lean_Outputs.md` or a short `AAT9_Aggregator_Inbox.md`):
    - For each module (DR, Stable, V-TRAC, Hot Zones, Aux), name the small set of fields the aggregator is allowed to use (matching the “Aggregator Contract v0” in Section 5).
    - Ensure names/keys line up with what per-tool logs/log specs already describe (e.g., pattern_key, vt_only_lane, recency_lane, hot_level, pos.double_pressure, etc.).
- This wiring layer is not a new architecture; it just centralizes what the existing AAT9 docs already imply so future sessions don’t have to rediscover the same connections.
