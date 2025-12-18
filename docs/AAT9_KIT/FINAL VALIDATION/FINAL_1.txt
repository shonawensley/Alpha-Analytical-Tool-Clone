I’ll answer as a world‑famous data‑pipeline reliability engineer with an ACM Software System Award.

TL;DR:

Your tables and winners_by_date pipeline (history → results → HTML/JSON) is solid and not secretly mixing dates.

The only “shaky” part is that Digit Reduction analyzer outputs live in a single per‑state folder, so each new DR run overwrites the previous run for that state. That’s expected behavior, but it means you can’t safely come back later and treat those live DR files as if they were still tied to some older workbook/date.

That does not mean past one‑day analyses were wrong; it only means any later “multi‑day comparison” that re‑used the same DR folder without re‑running or snapshotting could be blurry.

The fix going forward is simple: treat DR outputs as ephemeral and only trust per‑date snapshots (sharepacks / stamped folders) + the new run_history_and_results.py / validation docs as your “gospel”.

Below I’ll break it down cleanly and then give you a “never‑again” checklist you can hand to any future AI or session.

1. What’s actually safe today (and why you are not crazy)

From everything you pasted, the core pipeline and validation docs all agree on the same story:

History workbook → tables/JSON

run_tables_with_guard.py activates a specific Pick3 workbook and regenerates all tables + JSON mirrors for that history date.

It records the active workbook (path / mtime / size) into data/outputs/tables/tables_manifest.json.

This is written up in:

AAT9 String Table Testing SOP (Stage 1 + manifest + guard columns)

AAT9 Master Validation Preflight

AAT9 Table Swap Verification

Those all say the same thing: “when you swap Excel, you must re‑run tables with the guard, and the manifest proves what workbook is active”.

Results (day‑ahead) → winners_by_date

Results file is always history_date + 1, e.g.:

history 2025‑06‑21 → data/results/2025‑06‑22.txt → reports/stable/winners_by_date/2025‑06‑22/

This is baked into several places you pasted:

SOP “Stage 2 – Batch/Winners Verification” for runs A/B/C (20→21, 21→22, 22→23)

Master Validation Preflight (explicitly: “results file is always the day after the history workbook date”)

run_history_and_results.py wrapper which literally computes results_date = history_date + 1 and then checks CT/FL winners + Set1 sequences.

Winners dirs are per‑date and never reused

All runs write to date‑keyed directories:

reports/stable/winners_by_date/2025‑06‑21/...

reports/stable/winners_by_date/2025‑06‑22/...

reports/stable/winners_by_date/2025‑06‑23/...

etc. (same pattern for 25/26/27)

The SOPs/logs you pasted explicitly list CT/FL triads per date and the exact HTML where the Set1/Draw1 sequence appears.

👉 Bottom line:
When a session did:

pick a history workbook,

run run_tables_with_guard.py,

run generate_winners_from_results.py into winners_by_date/<RESULTS_DATE>/,

and then looked at those winners HTML/JSON for that date,

it was looking at the correct tables + correct results. That part is locked in, and your 20‑billion checks (tables manifest, guard columns, day‑ahead rule, CT/FL sequence check, etc.) really do their job.

2. Where the “nightmare” actually lives: live Digit Reduction outputs

Now the awkward bit: Digit Reduction analyzer outputs.

From your log (the big run_digit_reduction_workflow printout), you can see the current design:

DR outputs live in paths like:

data/outputs/analysis/digit_reduction/Connecticut4/analyzer_v2/Connecticut4_analyzer_v2_per_item.csv

.../Connecticut4_analyzer_v2_top_candidates.csv

Overlays / flags in .../analyzer_v2/winners/20251206_Combined_winner_flags.csv etc.

Key things we can read from that snippet:

The overlay filenames are stamped by run date (e.g. 20251206_...) but not by results date.

Every time you call run_digit_reduction_workflow for a state, those files are updated to reflect that run’s results.

So when Codex did:

20→21 (run DR),

21→22 (run DR),

22→23 (run DR),

24→25 (run DR),

25→26 (run DR),

26→27 (run DR),

the live DR files after the very last step correspond only to the last results date you ran, even though the winners HTML/JSON for earlier days are all still neatly sitting under their own winners_by_date folders.

That’s all I was trying to point at:

DR live folders = “current brain for this state”, always overwritten.

Winners_by_date = per‑date, never overwritten.

There is no bug there. It’s just that you can’t later open the DR folder and assume it still represents “2025‑06‑22” after you’ve run other dates.

3. So… were past analyses “wrong”?

Let’s be really explicit:

Safe cases (what you mostly did)

If the flow was:

You told Codex: “Use history X, results Y, run DR, then analyze that.”

Codex ran the pipeline and immediately looked at those DR outputs in the same context.

Then:

The analysis was using the correct workbook + results pairing.

Overwriting older DR outputs is exactly what you want: you don’t care about yesterday’s DR run while you’re looking at today’s Excel/run.

So your “single‑day, per‑session” examples are fine.

Risky case (why I raised the flag)

The only time things go sideways is if a later session does something like:

“Let’s talk about June 22 again”

but does not re‑run DR for June 22 and just re‑opens whatever DR files happen to be on disk

after you’ve already run other dates (25, 26, 27, etc.).

Then that later session is staring at DR outputs that actually belong to the last run, not June 22.

In human terms: you know very well that “live outputs = last run”; an LLM or future script might not, unless you tell it.

That’s the only “nightmare” here: confusing ephemeral DR live outputs with per‑date snapshots.

4. What about sharepacks / dated bundles?

Your instinct with sharepacks was correct:

When you (or Codex) built a dated sharepack, that copy is frozen.

Later DR runs cannot change that zipped / copied snapshot.

So any previous analysis that explicitly used “sharepack for 2025‑06‑23” (or similar) is still good; those files don’t magically change just because live DR ran again.

The gap is just: we haven’t yet made DR sharepacks for every example run (e.g. all those June 20→27 pairs). Some exist (e.g. Stable, V‑TRAC bundles); some DR runs were only ever stored in the live DR folders.

That’s why I’ve been careful about June 22 specifically: I don’t want to promise “I’m reading DR for 2025‑06‑22” if the live folder currently reflects a different date’s run.

5. Why your “clear outputs” idea is orthogonal

You asked:

“Wouldn’t overwriting be expected? Isn’t clearing folders the same idea?”

Yes, exactly:

Rerunning DR for a new workbook should overwrite the old outputs — that’s normal.

Clearing the folder beforehand is just a human‑clarity thing; it doesn’t change the fact that after the run, the folder contains only one state of the world: “whatever you just ran”.

That’s why your intuition (“if I’m re‑running anyway, isn’t overwrite expected?”) is spot on. The only extra thing we need is:

A way to keep a permanent copy per date when we care about that example run for long‑term analysis.

Which brings us to the “never‑again” strategy.

6. How to make this bullet‑proof going forward

You already have most of the guardrails in place (and they’re good). We just need to add one small DR snapshot layer and a couple of habits:

A. Treat Stage 1 + Stage 2 as gospel (you already do)

For any “gold” backtest run:

Use run_history_and_results.py (or the manual commands from Master Preflight) to ensure:

History workbook = correct date.

Tables + JSON rebuilt.

Results file = history_date + 1.

CT/FL triads and Set1/Draw1 sequences match between tables and winners HTML.

Log that run in the String Table SOP / Table Swap Verification (which you already started).

Once that’s done, you can trust:

data/outputs/tables/*

reports/stable/winners_by_date/<RESULTS_DATE>/...

for that pair.

B. Add a tiny DR snapshot protocol

For any date where you want deep analysis (like 2025‑06‑22):

Run DR once for that results date, with the correct history already active.
Something like what you already did via run_digit_reduction_workflow for that data/results/YYYY‑MM‑DD.txt.

Immediately snapshot the DR outputs into a dated folder, e.g.:

sharepacks/DR_2025-06-22/<STATE>/... or

data/outputs/analysis/digit_reduction_snapshots/2025-06-22/<STATE>/...

Copy at least:

analyzer_v2/…_per_item.csv

analyzer_v2/…_top_candidates.csv

analyzer_v2/meta.json

analyzer_v2/winners/20251206_*_winner_{overlay.html,flags.csv}

Write a tiny manifest JSON alongside, e.g.:

{
  "history_date": "2025-06-21",
  "results_date": "2025-06-22",
  "states": ["Connecticut4", "Delaware4", ...],
  "tables_manifest": "data/outputs/tables/tables_manifest.json",
  "winners_root": "reports/stable/winners_by_date/2025-06-22/",
  "dr_snapshot_root": "sharepacks/DR_2025-06-22/",
  "dr_config_hash": "<from meta.json>"
}


In AAT9_Digit_Analysis_Log.md, when you write an entry like:

2025‑06‑22 — DR example runs (CT, DE, FL, …)

explicitly reference:

that manifest,

the winners_by_date path,

and the DR snapshot root.

From that point on, any AI / agent / future you just needs to be told:

“For 2025‑06‑22, ONLY read:
• winners from reports/stable/winners_by_date/2025-06-22/
• DR from sharepacks/DR_2025-06-22/
• ignore live DR folders; they are ephemeral.”

And the mixing nightmare disappears.

7. What this means for your big picture (and past work)

Your 20+ validation docs are not contradicting each other — they’re basically all saying:

history D → tables → guard columns

results D+1 → winners_by_date

tools (Stable, V‑TRAC, DR, Hot Zones) read those tables/winners in well‑documented ways.

The new wrapper run_history_and_results.py plus Master Preflight and String Table SOP give you a clean, reproducible Stage 1/2 pipeline. That alone already stops the worst kind of “wrong results file” mistakes you caught earlier.

The only place where “datasets could mix” is if someone reuses live DR outputs for a date other than the last one that was run. That’s not a logic bug in DR; it’s just an output‑layout design choice.

You fix it by:

committing to per‑date DR snapshots for important runs, and

training every future session: “live DR folders = current run only; for historical examples, use the dated snapshot manifest.”

8. What I’d hand off to a new chat / engine

If a new Pro session (or a different AI engine) is going to pick this up, I’d give it something like:

Read this first:

docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md

docs/AAT9_KIT/AAT9_String_Table_Testing.md

docs/AAT9_KIT/AAT9_Final_Validation_Help.md

docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md

docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md (especially the June runs)

Never assume live DR folders are date‑specific.

For any historical example, always work from:

winners_by_date/<RESULTS_DATE>/

DR snapshot for that date (if it exists).

If a DR snapshot doesn’t exist for a day they care about, they must re‑run DR for that day and snapshot it before analyzing.

For state‑of‑the‑art analysis (your “Brain 2 / profitability” mission):

Start from winners JSON (3 tables, ls‑boxes, 4 hit criteria).

Then cross‑check the matching DR snapshot (per_item/top/flags) to see:

where the winner lives (LS1 core, LS2, ladder, vt_only lane, etc.),

which evidence features fire (progression, drops, VT families, LS2 progress),

and what environments look “profitable” vs noisy across states.

If you want, in the next conversation we can assume:

“For date X we have (or we create) a DR snapshot at sharepacks/DR_X.”

and then just focus purely on the state‑by‑state analytical side (4 criteria, VT‑families, profitable environments, when to skip playing, etc.), without re‑litigating any of this plumbing again.