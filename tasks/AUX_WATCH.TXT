thanks for lining up the evidence and the docs. Below is a crisp, decision‑oriented readout for A–D, grounded in what’s already shipped in AAT9 and what will give you the most leverage next.

A) “What (if anything) should we add that won’t already be picked up by string‑pattern analysis?”

Short answer: most of your Aux signals do complement the string tools, and only a couple are “must‑haves” that aren’t naturally visible to the string tables.

Must‑add (strongest ROI, low risk):

V‑TRAC repeat‑index streaks (per state & variant).
String tables don’t track index‑level recurrence across days; the Aux page already computes per‑index draws‑since (1,000‑draw scan). Elevate that into a small, persistent repeat‑streak feature (current streak, last repeat age, max 90‑day streak) and surface it in Control Center. This is orthogonal to strings and pays off immediately when an index repeats. The Aux wiring for V‑TRAC index hits is already in place (rank sets + 1,000‑draw scan), so you’re adding features, not inventing new math.

Pairs window SSOT + captions.
Not a “feature,” but a correctness guardrail that keeps pair thresholds trustworthy. Centralize the window (e.g., 360 draws for pairs) and show it in captions so operator expectations match the math. Your roadmap explicitly anticipates this kind of logging/discipline.

Nice‑to‑have (safe to defer):

Mirror‑double & “floater” clocks as compact Aux features. Many of these cues are already embedded in Blackapple scoring and tags; converting them to explicit, numeric features can wait until we start logging feature vectors with winners.

Already covered well enough today:

Overdue pairs & top‑5 (repeating/non‑repeating) are implemented and verified.

V‑TRAC index hits, rank tints, and sums badges already render on the Aux page; sums table appears when the package is available (see next section for how to use it as a scoring feature).

B) Sums — is the current tracking sufficient, and can we use it as an individual scoring feature now?

What you have now

Inline sums badges next to each combo; when the optional Sums package is importable, a full Sums Tracking table appears. Both are wired to the Aux page and degrade gracefully if the package is missing. The analysis window is currently a parameter (defaulted via analysis_draws), and the UI is already conditioned on availability.

My call: You’re good enough to use it right now as a low‑weight individual feature—no need to invent complexity:

Start with two scalar features per run:
(1) sum_is_due / root_sum_is_due (boolean), (2) days_since_root_sum (numeric).
These come straight from the Sums stats you already compute and align with how Blackapple frames “due” calls (root/short sum cycles). Keep weight small so strings remain the primary driver, and let logging teach us if these deserve more influence.

Tiny enhancement (optional now, easy later):

Move the sums window into the SSOT config alongside pairs and echo the active window in captions (“Sums window = N draws”). That keeps operators honest about scope and is consistent with your winners‑logging discipline.

C) Codex’s “AUX_RESEARCH / AUX_VALIDATE → checklist” plan — should we let it proceed?

Yes—with a tight, bounded slice that locks in correctness and keeps scoring simple until we start logging. Green‑light this exact scope:

Window SSOT & captions. Add a small aux_config.py (pairs=360, vtrac_index=1000, sums=N) and show the active window values inside the Aux captions.

V‑TRAC overlay reuse. Feed both the big V‑TRAC table and the mini‑table from the same overlay function; ensure Top‑10 Overdue and Top‑5 Recent align and the row count is 35.

Feature extractors (read‑only). Provide a unified aux_features helper that returns a dict per state/day with: pair color buckets, vtrac index status (overdue/recent + draws‑since), simple sums flags (as above). Persist nothing beyond the existing run logs.

No scoring aggregator yet. Compute additive scores later—for now, just log the feature vector with winners so we can learn stable weights before we influence string scoring. (This mirrors your “log first, learn weights later” plan.)

Definition of done for this slice:

SSOT windows in code + captions visible.

Mini‑table = big‑table overlay (unit check on 35 rows, Top‑10/Top‑5 parity).

Feature dict emitted to the run/winners logs next to BA and V‑TRAC outputs.

Changelog + checkpoint entries written.

D) Should you hand Codex an aggregated “big‑picture” doc now?

Yes—share a trimmed “executive read” before the feature work. It will cut ramp‑up time and keep the PRs scoped. Your Final Outlook already captures the “two brains” model (per‑state vs aggregate/Control Center) and the logging‑first philosophy—exactly what another agent needs to stay aligned. I’d drop a short brief (e.g., briefings/CODEX_READ_FIRST_AUX.md) with these bullets:

Two brains: per‑state analysis & aggregate Control Center for cross‑state profitability.

Data contracts: Aux consumes only data/cleaned/*_draws.csv; string tools consume combined tables under tables/....

Windows & thresholds: pairs=360, vtrac_index=1000, sums=N (SSOT), echo in UI.

What to build now: the four items in (C) and nothing else.

What not to change: string‑pattern scoring; keep Aux features compound‑only until we have logged evidence.

Where logs land & why: runs/YYYY‑MM‑DD/... and winners/... for reproducibility and future ML weighting.

This brief should reference your “In a nutshell” framing so future sessions keep the same north star.

Quick confirmations (so you feel safe moving forward)

Aux coverage today: V‑TRAC table + index hits, overdue pairs (NR/REP) + Top‑5, sums badges/table (when available), and cross‑state doubles in Control Center are already wired and working.

Winners logging: your MVP structure and run artifacts are already specified; the next step is appending Aux feature vectors to those JSONs—no architectural surprises.

Process guardrails: KIT, preflight, and the checkpoint log make this a reversible, low‑risk slice.

Bottom line

Add now: V‑TRAC repeat‑streak features + SSOT windows/captions; unify the mini‑table source; log a tiny sums feature (due flag + days‑since).

Defer: scoring weights/aggregator and any heavy feature expansion until we’ve logged real evidence.

Share: a short “read‑first” brief distilled from your Final Outlook so Codex stays laser‑aligned with your intent.

If you want, I can turn the above into a copy‑paste PR template and a 10‑item checklist for Codex to execute against.