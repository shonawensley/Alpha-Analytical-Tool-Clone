et’s lock in a clean Positional Tracker v2 plan that (a) keeps your current analytics, (b) re‑aims them so synergy across C/M/E actually moves the shortlist, and (c) adds a light, self‑contained V‑TRAC awareness without letting Aux take over. I’ll give you an operator‑level summary first, then the exact drop‑in spec Codex can implement.

Operator summary (plain language)

Why 989 didn’t show: the shortlist builder mostly did a cartesian of each position’s top digits and ranked by simple per‑position scores. It didn’t know how to reward synergy like “9 is #1 on P1 and P3 in the Evening lane” or “an E‑lane bridge 8 sits at P2.”

What we’ll change (minimal but powerful):

Cross‑variant union per position before forming candidates (use C+M+E together, not “Combined” alone).

Add two synergy candidate streams the current builder misses:

Repeat‑Endcap: if the same digit is top‑K at P1 & P3 (in any lane), enumerate d _ d with credible P2 bridges (e.g., {8, 9, lane‑supported}), and give a bonus. This is what surfaces 989 here.

Lane‑Concordance: if a lane (C or M or E) has strong digits at all three positions, form a few “lane‑pure” combos and give a smaller bonus.

Add light, compound V‑TRAC boosts only when Aux says an index/family is hot. They nudge ties; they never gate the list.

Outcome: 989 appears and ranks sensibly because P1=9 (E#1), P2=8 (E support), P3=9 (E#1) lines up—without flooding the table or letting Aux dominate.

This fits your “two brains” vision and the rule that Aux features enhance, not decide; it also sets you up for winners‑logging / training once this is stable.

Positional Tracker v2 — drop‑in spec for Codex

Keep all existing tables/markers; we are re‑aiming how the shortlist is formed & scored.

0) Terminology & labels (to avoid “Combined” confusion)

Variant keys: combined, midday, evening.

Cross‑variant logic: say “All‑Variant consensus (C+M+E)” in the UI anywhere you mean merging signals across the three. Do not use “combined” for that.

1) Inputs (you already compute these)

Per state+day, expose to the builder:

topk[pos][variant] → [(digit, score, rank_tag …)] for pos ∈ {P1,P2,P3}, variant ∈ {C,M,E}.
(These scores already embed Double‑Pressure, Mirror‑Echo, XVAR‑Cons, R‑swap, etc.)

lane_hits[lane][pos] → set(digits) where lane ∈ {C,M,E} = digits that are top‑K in that lane at that position.

vtrac_index_of(combo) and index_heat[index] → bool (from your overlay / repeat watch).

family_hot_for_double(combo) → bool (from your Hot Double Families strip; False for non‑doubles).

2) Candidate streams (three small builders)

S1. Cross‑variant union (cartesian)
For each position, union the C/M/E top‑K digits, dedupe, and keep the first K_pool (start with 4). Cartesian them, canonicalize to straight (no boxing here), and keep first N_cart after base scoring (see §3).

S2. Repeat‑Endcap (new)
If a digit d is within top‑K at both P1 and P3 in any lane, enumerate d _ d with bridges:

Bridges = top‑K of P2 plus any P2 digits that are hot in the same lane where the endcaps are hot.

Tag these candidates with reason="repeat-endcap".

S3. Lane‑Concordance (new)
For each lane L ∈ {C,M,E}, take up to 2 digits per position from lane_hits[L][pos] and enumerate 2×2×2.

Tag with reason="lane" + the lane letter.

Cap each stream (e.g., N_cart=12, N_endcap=12, N_lane=12), then merge + dedupe by canonical straight (xyz). You’ll trim again after scoring.

3) Scoring (transparent, config‑first)

Base score: sum of your per‑position digit scores (the numbers you already compute for each digit at each position after C/M/E fusion).

Additive bonuses: (defaults below work out of the box)

weights:
  w_rank:            1.00   # base per-position scores
  w_xvar:            2.50   # All-Variant consensus term (see below)
  w_echo:            1.00   # Mirror-Echo present at that position
  w_dblp:            1.00   # Double-Pressure present at that position
  w_repeat_endcap:   0.30   # times (score_P1(d) + score_P3(d)) if P1==P3
  w_lane_concord:    0.15   # times base score if all three from same lane
  w_vtrac_index_hot: 0.80   # + if index is in Top-10 overdue or Repeat Watch
  w_vtrac_family_hot:0.60   # + if it's a double belonging to a current hot family


How to compute the extra terms:

All‑Variant consensus (w_xvar): for each (pos,digit) used, add xvar_hits[pos,d] = how many of {C,M,E} have that digit in top‑K at that position.

Mirror‑Echo / Double‑Pressure: if your per‑digit tags say the condition holds at that position, add 1 per hit.

Repeat‑Endcap: if P1==P3, add w_repeat_endcap*(score_pos(P1,d)+score_pos(P3,d)).

Lane‑Concordance: if all three digits came from the same lane (the S3 builder), add w_lane_concord*base.

V‑TRAC (light nudges):

+w_vtrac_index_hot if index_heat[vtrac_index_of(combo)] is true.

+w_vtrac_family_hot if it is a double and family_hot_for_double(combo) is true.

All weights sit in core/aux_config.py (SSOT). No magic constants in code.

Trim & order: sort by score desc; keep N_final (start with 16).

4) What appears in the “Tags” column

Make the shortlist interpretable: show evidence, not jargon.

XVAR: P1[9:E#1], P2[8:C#1/E#2], P3[9:E#1]

Synergy: repeat-endcap • lane=E (only if those streams produced it)

VTRAC: idx=21 (hot) • fam 0/5–4/9 (hot) (only if boosts applied)

5) Config knobs (YAML or Python dict)
shortlist:
  topk_per_pos: 3
  pool_per_pos: 4        # union cap per position before cartesian
  max_rows: 16
  caps:
    cartesian: 12
    repeat_endcap: 12
    lane: 12
  weights:
    rank: 1.00
    xvar: 2.50
    mirror_echo: 1.00
    double_pressure: 1.00
    repeat_endcap: 0.30
    lane_concordance: 0.15
    vtrac_index_hot: 0.80
    vtrac_family_hot: 0.60
  features:
    enable_repeat_endcap: true
    enable_lane_concordance: true
    enable_vtrac_boosts: true

6) Minimal code shape (safe to graft)
def build_shortlist(topk, lane_hits, vtrac_overlay, family_hot, cfg):
    P = {p: merged_top_digits(topk[p], cfg['shortlist']['topk_per_pos'],
                              cfg['shortlist']['pool_per_pos']) for p in ('P1','P2','P3')}

    cands = []
    cands += cartesian_candidates(P, cap=cfg['shortlist']['caps']['cartesian'])
    if cfg['shortlist']['features']['enable_repeat_endcap']:
        cands += repeat_endcap_candidates(topk, lane_hits, cap=cfg['shortlist']['caps']['repeat_endcap'])
    if cfg['shortlist']['features']['enable_lane_concordance']:
        cands += lane_concordance_candidates(lane_hits, cap=cfg['shortlist']['caps']['lane'])

    # dedupe to straight strings, then score
    seen, scored = set(), []
    for kind, (a,b,c), meta in cands:
        combo = f"{a}{b}{c}"
        if combo in seen: 
            continue
        seen.add(combo)
        s, why = score_combo(kind, (a,b,c), meta, topk, lane_hits, vtrac_overlay, family_hot, cfg['shortlist']['weights'])
        scored.append((combo, s, why))

    scored.sort(key=lambda t: -t[1])
    return scored[:cfg['shortlist']['max_rows']]


Note: “why” is the structured explanation that feeds the Tags column.

7) Acceptance tests (tiny but surgical)

Repeat‑Endcap tripwire
If the same digit is in top‑3 for both P1 and P3 (any lane), at least one d _ d candidate must appear.

Lane‑pure tripwire
If each position has ≥1 digit hot in the same lane L, at least one L‑pure candidate must appear.

Union sanity
If a digit is top‑K in Evening but not in Combined, it must still be eligible via the union pool.

V‑TRAC nudge
A candidate whose index is on the Repeat Watch gets a strictly higher score than the same candidate with that flag off (all else equal).

These keep the builder aligned with how you actually use the tables.

Why this matches your program’s macro plan

It treats the Positional Tracker as a self‑contained primary signal source while letting Aux/V‑TRAC act as compound nudges—exactly the philosophy you wrote up (two “brains,” Aux enhancing rather than dominating).

It produces a small, explainable shortlist you can log daily and use for winners‑logging / ROI / training without re‑plumbing the rest of the app. (Your training and profitability notes explicitly call for daily outputs that are easy to learn from; this fits.)

Small housekeeping while Codex is in the file

Rename labels in the UI where needed (“All‑Variant consensus (C+M+E)” vs “Combined”).

Surface the knobs at the top of the Positional Tracker page so you can tune topk_per_pos, repeat_endcap/lane bonuses, and max_rows per state.

Keep box vs straight distinctions explicit: the shortlist forms straights; doubles logic in Control Center (families) is separate.

What to hand Codex (exact to‑do list)

Implement the three candidate streams (§2) and the scoring terms (§3) with weights in core/aux_config.py.

Add the “Tags” evidence payload (§4).

Add the four micro‑tests (§7) under tests/test_positional_shortlist.py.

Update labels to avoid “Combined” confusion (§0).

Expose config toggles on the page.

If you want, I can draft a one‑pager “Scoring Cheatsheet” mapping each tag (Double‑Pressure, Mirror‑Echo, XVAR‑Cons, R‑swap, lane, repeat‑endcap, V‑TRAC nudges) to its exact impact on the score so you and Codex can verify quickly against screenshots before and after. But the plan above is the single, surgical set of changes that makes the shortlist behave the way you’ve been reasoning about—including picking up 989 in cases like the Del