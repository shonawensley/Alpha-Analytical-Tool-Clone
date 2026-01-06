# Aux Summary — Delaware4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2026-01-02/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=937, 149, 337, 082, 563
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2026-01-02/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=149, 082, 706, 357, 989
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2026-01-02/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=937, 337, 563, 386, 660

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=15 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=19), P2:7 (gap=26), P3:1 (gap=38)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 471: score=48.89517285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 474: score=48.23395714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 494: score=41.63447857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 414: score=41.590607142857145 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 271: score=41.04600714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=40.45835 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 274: score=39.74558571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 171: score=39.45727142857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 491: score=39.24415 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 411: score=39.20027857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=967 sev=B
- 447: ds=959 sev=B
- 033: ds=892 sev=B
- 288: ds=832 sev=B
- 579: ds=809 sev=B
- 088: ds=795 sev=B
- 155: ds=766 sev=B
- 079: ds=763 sev=B
- 269: ds=744 sev=B
- 555: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=58 sev=purple
  - 11: ds=50 sev=purple
  - 88: ds=32 sev=purple
  - 00: ds=29 sev=purple
  - 77: ds=26 sev=purple
  - 55: ds=11 sev=-
  - 22: ds=10 sev=-
  - 99: ds=9 sev=-
  - 66: ds=8 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 24: ds=82 sev=red
  - 48: ds=59 sev=red
  - 13: ds=51 sev=blue
  - 47: ds=43 sev=blue
  - 78: ds=37 sev=blue
  - 17: ds=31 sev=purple
  - 27: ds=31 sev=purple
  - 01: ds=30 sev=purple
  - 18: ds=30 sev=purple
  - 69: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:230, 2:159, 32:124, 28:116, 19:90, 1:89, 31:85, 16:64, 26:62, 22:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=230 fs=5 fl=2 hz=0.010767160161507403, 2:ds=159 fs=13 fl=3 hz=0.01932367149758454, 32:ds=124 fs=2 fl=4 hz=0.008073817762399077, 28:ds=116 fs=14 fl=4 hz=0.02112676056338028, 19:ds=90 fs=30 fl=2 hz=0.03535911602209945, 1:ds=89 fs=1 fl=2 hz=0.008746355685131196, 31:ds=85 fs=16 fl=4 hz=0.022321428571428572, 16:ds=64 fs=2 fl=6 hz=0.009876543209876543, 26:ds=62 fs=8 fl=4 hz=0.014888337468982629, 22:ds=56 fs=46 fl=0 hz=0.0500544069640914

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=83 flags=purple
- S5: ds=52 flags=blue+purple
- S11: ds=51 flags=purple
- S2: ds=48 flags=blue+purple
- S8: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=2 last_repeat_gap=41 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=18), P2:3 (gap=24), P3:0 (gap=27)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 471: score=48.89517285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 474: score=48.23395714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 494: score=41.63447857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 414: score=41.590607142857145 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 271: score=41.04600714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=40.45835 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 274: score=39.74558571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 171: score=39.45727142857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 491: score=39.24415 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 411: score=39.20027857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 122: ds=952 sev=B
- 778: ds=948 sev=B
- 118: ds=886 sev=B
- 066: ds=798 sev=B
- 155: ds=785 sev=B
- 033: ds=784 sev=B
- 444: ds=756 sev=B
- 269: ds=698 sev=B
- 005: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=72 sev=blue
  - 33: ds=68 sev=purple
  - 44: ds=54 sev=purple
  - 66: ds=46 sev=purple
  - 11: ds=26 sev=purple
  - 00: ds=14 sev=-
  - 77: ds=13 sev=-
  - 22: ds=8 sev=-
  - 55: ds=5 sev=-
  - 99: ds=4 sev=-
- non_repeating:
  - 09: ds=62 sev=red
  - 25: ds=61 sev=red
  - 79: ds=57 sev=red
  - 23: ds=51 sev=blue
  - 24: ds=42 sev=blue
  - 29: ds=42 sev=blue
  - 58: ds=41 sev=blue
  - 59: ds=41 sev=blue
  - 18: ds=34 sev=purple
  - 05: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:266, 32:201, 3:176, 15:123, 12:118, 26:110, 16:86, 28:85, 2:79, 29:74

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=266 fs=2 fl=1 hz=0.013636363636363637, 32:ds=201 fs=3 fl=1 hz=0.008077544426494346, 3:ds=176 fs=18 fl=0 hz=0.023899371069182388, 15:ds=123 fs=14 fl=3 hz=0.019744483159117306, 12:ds=118 fs=43 fl=0 hz=0.048919226393629126, 26:ds=110 fs=6 fl=0 hz=0.012750455373406192, 16:ds=86 fs=1 fl=1 hz=0.0053475935828877, 28:ds=85 fs=21 fl=1 hz=0.024309392265193373, 2:ds=79 fs=17 fl=3 hz=0.022123893805309734, 29:ds=74 fs=21 fl=2 hz=0.02519167579408543

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=79 flags=red+purple
- S25: ds=67 flags=purple
- S20: ds=57 flags=purple
- S22: ds=41 flags=purple
- S8: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=3 tags=MIR,RS
  - 056: score=3 tags=MIR,RS
  - 146: score=3 tags=MIR,RS
  - 389: score=3 tags=MIR,RS
  - 479: score=3 tags=MIR,RS
  - 029: score=2 tags=RS
  - 047: score=2 tags=RS
  - 128: score=2 tags=RS
  - 137: score=2 tags=RS
  - 236: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=68 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=22), P2:5 (gap=21), P3:4 (gap=26)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 471: score=48.89517285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 474: score=48.23395714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 494: score=41.63447857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 414: score=41.590607142857145 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 271: score=41.04600714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=40.45835 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 274: score=39.74558571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 171: score=39.45727142857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 491: score=39.24415 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 411: score=39.20027857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 229: ds=949 sev=B
- 055: ds=917 sev=B
- 000: ds=873 sev=B
- 279: ds=830 sev=B
- 222: ds=818 sev=B
- 006: ds=772 sev=B
- 778: ds=751 sev=B
- 189: ds=716 sev=B
- 255: ds=714 sev=B
- 004: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=155 sev=red
  - 99: ds=60 sev=purple
  - 44: ds=29 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=24 sev=-
  - 88: ds=16 sev=-
  - 77: ds=13 sev=-
  - 22: ds=5 sev=-
  - 66: ds=4 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 69: ds=45 sev=blue
  - 03: ds=43 sev=blue
  - 24: ds=41 sev=blue
  - 48: ds=41 sev=blue
  - 89: ds=40 sev=blue
  - 13: ds=38 sev=blue
  - 19: ds=37 sev=blue
  - 16: ds=32 sev=purple
  - 47: ds=28 sev=purple
  - 67: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 5:175, 1:128, 35:115, 17:105, 31:87, 2:84, 32:62, 28:58, 21:50, 11:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 5:ds=175 fs=11 fl=2 hz=0.01643489254108723, 1:ds=128 fs=3 fl=1 hz=0.0063371356147021544, 35:ds=115 fs=3 fl=1 hz=0.007042253521126761, 17:ds=105 fs=20 fl=2 hz=0.02466367713004484, 31:ds=87 fs=20 fl=2 hz=0.025669642857142856, 2:ds=84 fs=15 fl=3 hz=0.02238805970149254, 32:ds=62 fs=2 fl=3 hz=0.007308160779537149, 28:ds=58 fs=15 fl=3 hz=0.020202020202020204, 21:ds=50 fs=49 fl=0 hz=0.05190677966101695, 11:ds=48 fs=54 fl=0 hz=0.05953693495038588

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=76 flags=blue+purple
- S23: ds=66 flags=purple
- S22: ds=64 flags=purple
- S18: ds=52 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 033 -> combined:892(B); midday:784(B)
- 155 -> combined:766(B); midday:785(B)
- 269 -> combined:744(B); midday:698(B)
- 778 -> evening:751(B); midday:948(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 11 -> combined:50(purple); evening:25(purple); midday:26(purple)
- 13 -> combined:51(blue); evening:38(blue); midday:25(purple)
- 18 -> combined:30(purple); midday:34(purple)
- 24 -> combined:82(red); evening:41(blue); midday:42(blue)
- 44 -> combined:58(purple); evening:29(purple); midday:54(purple)
- 47 -> combined:43(blue); evening:28(purple)
- 48 -> combined:59(red); evening:41(blue); midday:29(purple)
- 69 -> combined:25(purple); evening:45(blue)
- 88 -> combined:32(purple); midday:72(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(5.562421428571429)[R1,XVAR-Cons(CEM)], 2(3.2648)[R2,XVAR-Cons(CE)], 8(2.677142857142857)[R3,XVAR-Cons(CM)], 1(1.3568571428571428)[R1,Double-Pressure], 5(0.9089999999999999)[R2,Double-Pressure]
- P2: 7(6.7407071428571435)[R1,XVAR-Cons(CEM)], 9(2.6412285714285715)[R2,XVAR-Cons(CM)], 1(2.5973571428571427)[R3,XVAR-Cons(CE)], 3(1.3865714285714286)[R1,Double-Pressure], 5(1.327)[R1,Double-Pressure]
- P3: 1(8.0405)[R1,XVAR-Cons(CEM)], 4(6.740078571428572)[R2,XVAR-Cons(CEM)], 8(1.8819642857142858)[R3,XVAR-Cons(CE)], 0(1.4761428571428572)[R1,Double-Pressure]
