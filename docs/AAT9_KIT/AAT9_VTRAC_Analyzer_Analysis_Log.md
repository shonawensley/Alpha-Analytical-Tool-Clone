# AAT9 — VTRAC Analyzer Analysis Log

This log captures per-state insights for each VTRAC analyzer run, using the winners HTML (3-variant view), validator outputs, and compact report (`vtrac_compact_report.json`) as evidence.

## Analysis Criteria (run per state/date)
- **Winners HTML trace**: Follow the winner across Set3→Set2→Set1 and columns 7→…→1. Note repeats (survives reductions), hot/superhot boxes, and VT-box overlaps.
- **Cross-variant echoes**: Identify VTRAC families/straights appearing in multiple variants; highlight when they sit in superhot cells across variants.
- **Permutation/straight cues**: VT straight lanes from HTML/`top_straights`; ordered repeats in late columns (3/2/1); cross-variant straight echoes; superhot + straight co-location; single-lane dominance; mirror/double alignment with straights; order stability across columns (7→5→3→1); mask-drop revealing consistent lanes; note if only one variant shows strong ordered clues.
- **Recency / hot-zone recency**: Flag when the winner sits in Set1 column1/2 (freshest boxes) and whether it persisted from earlier columns (e.g., 4→2→1) and/or across sets.
- **Own-chart vs cross-variant factors**: Overlap, right-column stability, hot/superhot, cross-section echo, mirror/double pressure, mask drops; separate own-variant signals from cross-variant boosts.
- **Hit taxonomy**: Exact vs VT-boxed vs VT-straight; note hot/superhot context and whether presence is repeated or first appearance.
- **Scoring alignment**: Compare HTML evidence to compact report section scores and `top_indices_by_state`; record mis-ranks and tuning hypotheses.
- **Environment sketch & action hooks**: Summarize the winning environment (e.g., superhot repeats across variants, persistent R2/R4/R6 cluster in cols 3/2/1) and list follow-ups (boost cross-variant superhot repeats, VT-only lanes, straight-lane cues, etc.).

Checklist per entry:
1. Winners HTML trace + repeats/hot/superhot.
2. Cross-variant VTRAC relationships (box/straight echoes).
3. Permutation/straight cues (ordered repeats, VT straight lanes, superhot interactions, cross-variant straights).
4. Recency box check (Set1 col1/2; persisted vs first appearance).
5. Scoring alignment vs compact report / top_indices_by_state.
6. Action items / tuning hypotheses.

## Entries

> Add logs below in chronological order (state/date as headers).

### 2025-06-24 workbook → results 2025-06-25 (Connecticut4)
- Checklist: HTML traces done; cross-variant echoes captured; permutation/straight cues noted; recency checked; scoring aligned vs compact report; action items captured.
- Observations:
  - Midday winner 919 sits in superhot cells across Set3→Set2→Set1 and migrates into Set1 col2/col1. Persistent VT-box (V3x2_1x1) shows in all variants; strong right-column survival (cols 3→2→1).
  - Evening winner 864 shows VT straight lane overlap (V5x2_2x1) in Evening/Combined; sits in Set1 col1 superhot; repeats across Set3/Set2 before landing in Set1.
  - Permutation cues: straight candidates 683/386/836 dominate `top_straights`; lanes align with VT families present in HTML.
  - Compact report: Combined tier B, overlap low; `top_indices_by_state` favors #25/#34/#23; winner families not top-ranked → false-negative risk.
- Action items: Increase weight for cross-variant superhot repeats and right-column persistence; consider lane bump when repeats land in Set1 col1; check overlap gate to avoid suppressing strong stability runs.

### 2025-06-24 workbook → results 2025-06-25 (Delaware4)
- Checklist: ✓ HTML traces; ✓ cross-variant echoes; ✓ permutation cues; ✓ recency; ✓ scoring alignment; ✓ actions.
- Observations:
  - Midday 524: lives in Set3→Set2 superhot boxes (cols 7→5), reaches Set1 col3/2 superhot; VT box V2x2_4x2_1x1 repeated across variants. No strong straight lane in top_straights; order remains diffuse.
  - Evening 534: Set3/Set2 col5/4 superhot cluster; Set1 col4 (superhot) hit with V4x4_5x2 family; VT-straight lane weak but VT-box strong. Cross-variant family echo in Combined/Evening.
  - Recency: both winners occupy Set1 col2/col4 hot zones; persistence through earlier columns evident (7→5→4→2).
  - Compact report: `top_indices_by_state` (23/32/8) didn’t surface the winning families; tiers B/C with low overlap despite stability/hot repeats.
- Action items: Boost cross-variant superhot repeats and persistence; add VT-only lane credit when families recur across variants; consider mild consensus credit beyond overlap when repeats are dense in Set1 hot zones.

### 2025-06-24 workbook → results 2025-06-25 (Florida4)
- Checklist: ✓
- Observations:
  - Midday 310: Set3→Set2 col7→5 hot march; Set1 col3/2 hot; VT box V2x2_1x1_5x1 shows in Combined/Evening; no sharp straight lane dominance.
  - Evening 695: Strong VT box V1x1_3x1_4x1 spanning variants; sits in Set1 col1 superhot; repeats from Set3 col7 → Set1 col1. Cross-variant echo solid.
  - Recency: Evening winner lands in freshest col1 with prior-column persistence; Midday lands in col3/2 hot.
  - Compact report: `top_indices_by_state` (5/3/14) misses winner lane; sections tiered B/C with low overlap.
- Action items: Lane bump for families repeating into Set1 col1; increase weight for cross-variant echoes in superhot cells; review hot/superhot interaction weight.

### 2025-06-24 workbook → results 2025-06-25 (Indiana4)
- Checklist: ✓
- Observations:
  - Midday 147: VT box V2x1_4x1_5x1 appears in Combined/Midday; sits in Set1 col3 hot, with repeats from Set3 col6→5→3. Straight lane weak but ordered hints (147/741) present in top_straights.
  - Evening 138: Strong VT straight lane (V1x3_3x2) in Evening/Combined; winner lands Set1 col1 superhot after appearing Set3 col6→4→1; order stability clear.
  - Recency: Evening winner persists into col1; Midday into col3.
  - Compact report: top_indices (23/32/8) tilted to other families; overlap low, stability high; mis-rank for Evening winner lane.
- Action items: Increase lane credit when straight lane appears in multiple variants and ends in Set1 col1; modest boost for ordered repeats across columns.

### 2025-06-24 workbook → results 2025-06-25 (Michigan4)
- Checklist: ✓
- Observations:
  - Midday 783: VT box V3x2_1x1 repeats across variants; winner in Set1 col2 hot (not col1); path Set3 col6→5→2. Straight lane weak; order diffuse.
  - Evening 199: VT box V1x1_3x1_5x1 with mirror/double pressure; winner in Set1 col1 superhot, repeated from Set3 col7→5→1; strong persistence and hot interaction.
  - Recency: Evening winner best (col1 + persistence); Midday moderate (col2).
  - Compact report: top_indices (23/3/6) miss winner lane; tiers B/C; overlap absent.
- Action items: Boost persistence+hot in Set1 col1/2; consider mirror/double tie-break when aligned with straights.

### 2025-06-24 workbook → results 2025-06-25 (NewJersey4)
- Checklist: ✓
- Observations:
  - Midday 590: VT box V2x2_1x1_4x1 shows in Combined/Midday; winner in Set1 col3 hot; repeats from Set3 col6→4→3; straights lane weak.
  - Evening 756: VT box V1x1_3x1_4x1 appears across variants; winner in Set1 col4 superhot; repeats Set3 col6→4; some straight lane hints (567).
  - Recency: winners in col3/4, both with prior-column persistence.
  - Compact report: top_indices (5/6/9) do not surface winner families; low overlap; echo muted.
- Action items: Increase cross-variant echo + persistence weight even when overlap=0; lane credit for repeats in Set1 hot columns beyond col1.

### 2025-06-24 workbook → results 2025-06-25 (NewYork4)
- Checklist: ✓
- Observations:
  - Midday 662: VT box V1x2_2x1 appears Combined/Midday; winner in Set1 col2 superhot; repeats from Set3 col5→3→2; straight lane modest.
  - Evening 381: VT box V1x3_3x1 appears across variants; winner in Set1 col1 hot; repeats from Set3 col6→4→1; order stability visible.
  - Recency: Evening strongest (col1 + persistence); Midday good (col2 + persistence).
  - Compact report: top_indices (23/20/34) miss; low overlap coded; stability present.
- Action items: Similar: boost persistence into col1/2 + cross-variant repeats; lane bump on ordered repeats.

### 2025-06-24 workbook → results 2025-06-25 (NorthCarolina4)
- Checklist: ✓
- Observations:
  - Midday 262: VT box V1x2_2x1 strong; Set1 col2 hot; repeats from Set3 col6→3→2; order lane (2-6-2) weakly present.
  - Evening 410: VT box V1x1_2x1_4x1 shows across variants; winner in Set1 col3 hot; repeats Set3 col7→4→3.
  - Recency: Midday best (col2 with strong persistence); Evening moderate (col3).
  - Compact report: top_indices (8/14/23) off target; overlap low.
- Action items: persistence-in-hot weighting; VT-only lane bump for cross-variant repeats.

### 2025-06-24 workbook → results 2025-06-25 (Ohio4)
- Checklist: ✓
- Observations:
  - Midday 227: VT box V1x3_2x1 repeats; Set1 col2 hot; path Set3 col6→4→2; straight lane weak.
  - Evening 990: VT box V1x1_5x1 with mirror/double pressure; Set1 col1 superhot; strong repeats across variants and columns.
  - Recency: Evening strong (col1 + repeats + mirror/doubles); Midday good (col2).
  - Compact report: top_indices (23/20/31) miss; low overlap gate suppresses; stability present.
- Action items: mirror/double tie-break bump; persistence/hot weighting into col1/2.

### 2025-06-24 workbook → results 2025-06-25 (OntarioCanada4)
- Checklist: ✓
- Observations:
  - Midday 669: VT box V4x2_5x2 appears; Set1 col2 superhot; repeats Set3 col6→4→2; straight lane modest.
  - Evening 641: VT box V1x2_4x1_5x1; Set1 col3 hot; repeats; some straight lane presence.
  - Recency: Midday better (col2); Evening moderate (col3).
  - Compact report: top_indices (5/4/3) miss families; overlap low.
- Action items: persistence + hot weighting; VT-only lane bump when repeats across variants.

### 2025-06-24 workbook → results 2025-06-25 (Pennsylvania4)
- Checklist: ✓
- Observations:
  - Midday 065: VT box V3x2_4x1_5x1; Set1 col2 hot; repeats Set3 col6→3→2; straight lane weak.
  - Evening 073: VT box V4x2_2x1; Set1 col3 hot; repeats across variants; order hints weak.
  - Recency: Midday (col2) better; Evening (col3) moderate.
  - Compact report: top_indices (2/5/3) misaligned; overlap low; stability present.
- Action items: reinforce repeats/hot in col2/3; cross-variant echo bump.

### 2025-06-24 workbook → results 2025-06-25 (PuertoRico4)
- Checklist: ✓
- Observations:
  - Midday 828: VT box V1x1_2x1_4x1; Set1 col2 superhot; repeats across variants; mirror present.
  - Evening 449: VT box V5x3_1x2_3x2; Set1 col3 hot; repeats; straights diffuse.
  - Recency: Midday stronger (col2 + repeats); Evening moderate (col3).
  - Compact report: top_indices (29/22/14) off; overlap low.
- Action items: mirror bump; persistence/hot weighting; lane credit when cross-variant repeats.

### 2025-06-24 workbook → results 2025-06-25 (SouthCarolina4)
- Checklist: ✓
- Observations:
  - Midday 374: VT box V2x2_4x2_1x1; Set1 col2 superhot; repeats Set3→Set1; straights modest.
  - Evening 933: VT box V5x3_4x2_3x1; Set1 col1 superhot; cross-variant repeats into col1; mirror/double pressure present.
  - Recency: Evening strongest (col1 + repeats + mirror/doubles); Midday good (col2).
  - Compact report: top_indices (30/29/22) miss; overlap low; stability present.
- Action items: mirror/double tie-break; persistence into col1/2; VT-only lane bump.

### 2025-06-24 workbook → results 2025-06-25 (Virginia4)
- Checklist: ✓
- Observations:
  - Midday 175: VT box V1x3_3x2_5x2; Set1 col1 superhot; strong repeats Set3 col6→4→1; straight lane decent (571).
  - Evening 165: VT box V1x2_5x1; Set1 col2 hot; repeats; straights modest.
  - Recency: Midday strongest (col1 + repeats); Evening moderate (col2).
  - Compact report: top_indices (7/6/1) miss winner lane; overlap low.
- Action items: lane bump for repeats into col1; cross-variant echo weighting.

### 2025-06-25 workbook → results 2025-06-26 (Connecticut4)
- Checklist: ✓
- Observations:
  - Midday 928: VT box V3x2_1x1; Set1 col2 superhot; path Set3 col6→4→2; straight lane weak.
  - Evening 612: VT box V5x2_2x1; Set1 col1 superhot; repeats Set3 col7→4→1; strong lane presence.
  - Recency: Evening strongest (col1 + repeats); Midday good (col2).
  - Compact report: top_indices (25/34/23) miss winner; low overlap gate; stability high.
- Action items: same as prior (persistence/hot into col1/2; lane bump for repeats).

### 2025-06-25 workbook → results 2025-06-26 (Delaware4)
- Checklist: ✓
- Observations:
  - Midday 424: VT box V2x1_3x1_5x1; Set1 col3 hot; repeats Set3 col7→4→3.
  - Evening 771: VT box V4x4_5x2/3; Set1 col2 superhot; repeats across variants; straights diffuse.
  - Recency: Evening better (col2).
  - Compact report: top_indices (20/23/8) off; overlap low.
- Action items: persistence/hot weighting; cross-variant repeats bump.

### 2025-06-25 workbook → results 2025-06-26 (Florida4)
- Checklist: ✓
- Observations:
  - Midday 337: VT box V2x2_1x1_5x1; Set1 col3 hot; repeats Set3→Set1.
  - Evening 949: VT box V1x1_3x1_4x1; Set1 col1 superhot; strong repeats; lane modest.
  - Recency: Evening strong (col1); Midday moderate (col3).
  - Compact report: top_indices (5/24/14) off; overlap low.
- Action items: lane bump for col1 repeats; cross-variant echo boost.

### 2025-06-25 workbook → results 2025-06-26 (Indiana4)
- Checklist: ✓
- Observations:
  - Midday 913: VT box V2x1_4x1_5x1; Set1 col2 hot; repeats Set3 col6→3→2.
  - Evening 138: VT box V3x3_4x1_5x1; Set1 col1 superhot; strong repeats across variants; lane strong (138).
  - Recency: Evening strong (col1 + lane); Midday good (col2).
  - Compact report: top_indices (24/23/6) miss winner lane; overlap low.
- Action items: lane credit for repeats into col1; persistence/hot boost.

### 2025-06-25 workbook → results 2025-06-26 (Michigan4)
- Checklist: ✓
- Observations:
  - Midday 693: VT box V3x2_1x1; Set1 col2 superhot; repeats Set3 col6→4→2; straights modest.
  - Evening 693 (repeat): same cues; strong persistence; Set1 col2.
  - Recency: both in col2 with repeats.
  - Compact report: top_indices (24/23/3) miss; low overlap.
- Action items: persistence/hot weighting into col2; lane bump when repeats across variants.

### 2025-06-25 workbook → results 2025-06-26 (NewJersey4)
- Checklist: ✓
- Observations:
  - Midday 756: VT box V2x2_1x1_4x1; Set1 col3 superhot; repeats Set3→Set1.
  - Evening 617: VT box V1x1_2x1_3x1; Set1 col2 hot; repeats; straight lane modest.
  - Recency: Evening better (col2); Midday moderate (col3).
  - Compact report: top_indices (7/14/5) off; overlap low.
- Action items: cross-variant echo + persistence weighting; lane credit when repeats into col1/2.

### 2025-06-25 workbook → results 2025-06-26 (NewYork4)
- Checklist: ✓
- Observations:
  - Midday 093: VT box V1x2_4x1_5x1; Set1 col3 hot; repeats; straights weak.
  - Evening 580: VT box V1x1_3x1_4x1; Set1 col1 superhot; strong repeats across variants; lane modest.
  - Recency: Evening strong (col1 + repeats); Midday moderate (col3).
  - Compact report: top_indices (33/22/19) miss; overlap low.
- Action items: persistence/hot into col1/2; lane bump for repeats; cross-variant echoes boost.

### 2025-06-25 workbook → results 2025-06-26 (NorthCarolina4)
- Checklist: ✓
- Observations:
  - Midday 883: VT box V1x3_3x1_4x1; Set1 col2 hot; repeats Set3→Set1; straights modest.
  - Evening 482: VT box V1x1_2x1_4x1; Set1 col3 hot; repeats.
  - Recency: Midday better (col2); Evening moderate (col3).
  - Compact report: top_indices (25/24/23) miss; overlap low.
- Action items: persistence/hot weighting; echo/lane credit even when overlap=0.

### 2025-06-25 workbook → results 2025-06-26 (Ohio4)
- Checklist: ✓
- Observations:
  - Midday 694: VT box V1x2_4x1_5x1; Set1 col2 hot; repeats.
  - Evening 718: VT box V1x3_3x2; Set1 col1 superhot; strong repeats; lane decent.
  - Recency: Evening strong (col1); Midday good (col2).
  - Compact report: top_indices (22/21/20) off; overlap low.
- Action items: persistence/hot col1/2 bump; lane credit; echo weight.

### 2025-06-25 workbook → results 2025-06-26 (OntarioCanada4)
- Checklist: ✓
- Observations:
  - Midday 196: VT box V1x1_2x1_4x1; Set1 col2 hot; repeats.
  - Evening 653: VT box V5x2_2x1_3x1; Set1 col3 hot; repeats; straight lane modest.
  - Recency: Midday better (col2).
  - Compact report: top_indices (22/12/9) miss; overlap low.
- Action items: persistence/hot weighting; echo bump.

### 2025-06-25 workbook → results 2025-06-26 (Pennsylvania4)
- Checklist: ✓
- Observations:
  - Midday 773: VT box V3x2_4x1_5x1; Set1 col2 superhot; repeats.
  - Evening 544: VT box V4x2_2x1; Set1 col3 hot; repeats; double pressure.
  - Recency: Midday better (col2).
  - Compact report: top_indices (27/5/2) miss; overlap low.
- Action items: persist/hot boost; double/mirror tie-break bump.

### 2025-06-25 workbook → results 2025-06-26 (PuertoRico4)
- Checklist: ✓
- Observations:
  - Midday 467: VT box V1x1_2x1_4x1; Set1 col2 hot; repeats; mirror present.
  - Evening 828: VT box V5x3_1x2_3x2; Set1 col3 hot; repeats.
  - Recency: Midday better (col2).
  - Compact report: top_indices (22/19/17) miss; overlap low.
- Action items: mirror bump; persistence/hot weighting.

### 2025-06-25 workbook → results 2025-06-26 (SouthCarolina4)
- Checklist: ✓
- Observations:
  - Midday 774: VT box V2x2_4x2_1x1; Set1 col2 hot; repeats.
  - Evening 933: VT box V5x3_4x2_3x1; Set1 col1 superhot; strong repeats; mirror/double pressure.
  - Recency: Evening strong (col1); Midday good (col2).
  - Compact report: top_indices (33/30/22) miss; overlap low.
- Action items: mirror/double tie-break; persistence/hot into col1/2; echo bump.

### 2025-06-25 workbook → results 2025-06-26 (Virginia4)
- Checklist: ✓
- Observations:
  - Midday 165: VT box V1x3_3x2_5x2; Set1 col1 superhot; strong repeats; straight lane present.
  - Evening 165 (same): identical cues; strong lane.
  - Recency: col1 with repeats and lane dominance.
  - Compact report: top_indices (6/7/1) miss; overlap low gate.
- Action items: lane bump for repeats into col1; echo/hot weighting.

### Lane lift / scorer freeze (post-2025-11-16)
- Added scoring components: recency_lane, VT-only/VT-only lane, straight_lane, winner_lane_floor/rescue (no further engine/JSON changes). Overlap lowered/capped and lane promotion logic present, but analyzer JSON lacks per-section index mapping, so top_indices_by_state stays overlap/recency-driven.
- Current stance: freeze scorer as-is for Aggregator v1; treat top_indices_by_state as one signal alongside the richer per-section features (recency/hot/echo/straights, etc.). Further lane-aware ranking will happen in the Aggregator using the full feature set.
