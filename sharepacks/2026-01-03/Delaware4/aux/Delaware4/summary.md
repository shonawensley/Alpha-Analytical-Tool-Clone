# Aux Summary — Delaware4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=076, 126, 937, 149, 337
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=126, 149, 082, 706, 357
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2026-01-03/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=076, 937, 337, 563, 386

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=17 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=21), P2:9 (gap=22), P3:1 (gap=40)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 414: score=42.74377785714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 494: score=42.285470714285715 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 454: score=42.26352071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 411: score=40.15885 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 491: score=39.700542857142864 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 451: score=39.67859285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=38.29580642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 474: score=38.00917785714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 444: score=36.140606428571424 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 431: score=35.71087857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=969 sev=B
- 447: ds=961 sev=B
- 033: ds=894 sev=B
- 288: ds=834 sev=B
- 579: ds=811 sev=B
- 088: ds=797 sev=B
- 155: ds=768 sev=B
- 079: ds=765 sev=B
- 269: ds=746 sev=B
- 555: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=60 sev=purple
  - 11: ds=52 sev=purple
  - 88: ds=34 sev=purple
  - 00: ds=31 sev=purple
  - 77: ds=28 sev=purple
  - 55: ds=13 sev=-
  - 22: ds=12 sev=-
  - 99: ds=11 sev=-
  - 66: ds=10 sev=-
  - 33: ds=4 sev=-
- non_repeating:
  - 24: ds=84 sev=red
  - 48: ds=61 sev=red
  - 13: ds=53 sev=blue
  - 47: ds=45 sev=blue
  - 78: ds=39 sev=blue
  - 17: ds=33 sev=purple
  - 27: ds=33 sev=purple
  - 01: ds=32 sev=purple
  - 18: ds=32 sev=purple
  - 69: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:232, 2:161, 32:126, 28:118, 19:92, 1:91, 31:87, 16:66, 26:64, 22:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=232 fs=5 fl=2 hz=0.010767160161507403, 2:ds=161 fs=13 fl=3 hz=0.01932367149758454, 32:ds=126 fs=2 fl=4 hz=0.008073817762399077, 28:ds=118 fs=14 fl=4 hz=0.02112676056338028, 19:ds=92 fs=30 fl=2 hz=0.03535911602209945, 1:ds=91 fs=1 fl=2 hz=0.008746355685131196, 31:ds=87 fs=16 fl=4 hz=0.022321428571428572, 16:ds=66 fs=2 fl=6 hz=0.009876543209876543, 26:ds=64 fs=8 fl=4 hz=0.014888337468982629, 22:ds=58 fs=46 fl=0 hz=0.0500544069640914

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S5: ds=54 flags=blue+purple
- S11: ds=53 flags=purple
- S2: ds=50 flags=blue+purple
- S8: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=2 last_repeat_gap=42 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=19), P2:3 (gap=25), P3:0 (gap=28)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 414: score=42.74377785714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 494: score=42.285470714285715 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 454: score=42.26352071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 411: score=40.15885 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 491: score=39.700542857142864 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 451: score=39.67859285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=38.29580642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 474: score=38.00917785714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 444: score=36.140606428571424 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 431: score=35.71087857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 122: ds=953 sev=B
- 778: ds=949 sev=B
- 118: ds=887 sev=B
- 066: ds=799 sev=B
- 155: ds=786 sev=B
- 033: ds=785 sev=B
- 444: ds=757 sev=B
- 269: ds=699 sev=B
- 005: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=73 sev=blue
  - 33: ds=69 sev=purple
  - 44: ds=55 sev=purple
  - 66: ds=47 sev=purple
  - 11: ds=27 sev=purple
  - 00: ds=15 sev=-
  - 77: ds=14 sev=-
  - 22: ds=9 sev=-
  - 55: ds=6 sev=-
  - 99: ds=5 sev=-
- non_repeating:
  - 09: ds=63 sev=red
  - 25: ds=62 sev=red
  - 79: ds=58 sev=red
  - 23: ds=52 sev=blue
  - 24: ds=43 sev=blue
  - 29: ds=43 sev=blue
  - 58: ds=42 sev=blue
  - 59: ds=42 sev=blue
  - 18: ds=35 sev=purple
  - 05: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:267, 32:202, 3:177, 15:124, 12:119, 26:111, 16:87, 28:86, 2:80, 29:75

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=267 fs=2 fl=1 hz=0.013636363636363637, 32:ds=202 fs=3 fl=1 hz=0.008077544426494346, 3:ds=177 fs=18 fl=0 hz=0.023899371069182388, 15:ds=124 fs=14 fl=3 hz=0.019744483159117306, 12:ds=119 fs=43 fl=0 hz=0.048919226393629126, 26:ds=111 fs=6 fl=0 hz=0.012750455373406192, 16:ds=87 fs=1 fl=1 hz=0.0053475935828877, 28:ds=86 fs=21 fl=1 hz=0.024309392265193373, 2:ds=80 fs=17 fl=3 hz=0.022123893805309734, 29:ds=75 fs=21 fl=2 hz=0.02519167579408543

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=80 flags=red+purple
- S25: ds=68 flags=purple
- S20: ds=58 flags=purple
- S22: ds=42 flags=purple
- S8: ds=36 flags=purple

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
- current_index=7 streak=1 max=3 last_repeat_gap=69 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=23), P2:5 (gap=22), P3:4 (gap=27)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 414: score=42.74377785714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 494: score=42.285470714285715 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 454: score=42.26352071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 411: score=40.15885 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 491: score=39.700542857142864 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 451: score=39.67859285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=38.29580642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 474: score=38.00917785714285 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 444: score=36.140606428571424 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 431: score=35.71087857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 229: ds=950 sev=B
- 055: ds=918 sev=B
- 000: ds=874 sev=B
- 279: ds=831 sev=B
- 222: ds=819 sev=B
- 006: ds=773 sev=B
- 778: ds=752 sev=B
- 189: ds=717 sev=B
- 255: ds=715 sev=B
- 004: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=156 sev=red
  - 99: ds=61 sev=purple
  - 44: ds=30 sev=purple
  - 11: ds=26 sev=purple
  - 00: ds=25 sev=purple
  - 88: ds=17 sev=-
  - 77: ds=14 sev=-
  - 22: ds=6 sev=-
  - 66: ds=5 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 69: ds=46 sev=blue
  - 03: ds=44 sev=blue
  - 24: ds=42 sev=blue
  - 48: ds=42 sev=blue
  - 89: ds=41 sev=blue
  - 13: ds=39 sev=blue
  - 19: ds=38 sev=blue
  - 16: ds=33 sev=purple
  - 47: ds=29 sev=purple
  - 34: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 5:176, 1:129, 35:116, 17:106, 31:88, 2:85, 32:63, 28:59, 21:51, 11:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 5:ds=176 fs=11 fl=2 hz=0.01643489254108723, 1:ds=129 fs=3 fl=1 hz=0.0063371356147021544, 35:ds=116 fs=3 fl=1 hz=0.007042253521126761, 17:ds=106 fs=20 fl=2 hz=0.02466367713004484, 31:ds=88 fs=20 fl=2 hz=0.025669642857142856, 2:ds=85 fs=15 fl=3 hz=0.02238805970149254, 32:ds=63 fs=2 fl=3 hz=0.007308160779537149, 28:ds=59 fs=15 fl=3 hz=0.020202020202020204, 21:ds=51 fs=49 fl=0 hz=0.05190677966101695, 11:ds=49 fs=54 fl=0 hz=0.05953693495038588

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=77 flags=blue+purple
- S23: ds=67 flags=purple
- S22: ds=65 flags=purple
- S18: ds=53 flags=red+purple

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
- 033 -> combined:894(B); midday:785(B)
- 155 -> combined:768(B); midday:786(B)
- 269 -> combined:746(B); midday:699(B)
- 778 -> evening:752(B); midday:949(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:31(purple); evening:25(purple)
- 11 -> combined:52(purple); evening:26(purple); midday:27(purple)
- 13 -> combined:53(blue); evening:39(blue); midday:26(purple)
- 18 -> combined:32(purple); midday:35(purple)
- 23 -> combined:26(purple); midday:52(blue)
- 24 -> combined:84(red); evening:42(blue); midday:43(blue)
- 44 -> combined:60(purple); evening:30(purple); midday:55(purple)
- 47 -> combined:45(blue); evening:29(purple)
- 48 -> combined:61(red); evening:42(blue); midday:30(purple)
- 69 -> combined:27(purple); evening:46(blue)
- 88 -> combined:34(purple); midday:73(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(5.71215)[R1,XVAR-Cons(CEM)], 2(3.3297)[R2,XVAR-Cons(CE)], 8(2.7352857142857143)[R3,XVAR-Cons(CM)], 1(1.3867142857142856)[R1,Double-Pressure], 5(0.9299)[R2,Double-Pressure]
- P2: 1(3.3644)[R2,XVAR-Cons(CE)], 9(2.9060928571428573)[R1,XVAR-Cons(CM)], 5(2.884142857142857)[R3,XVAR-Cons(CE)], 3(1.4164285714285714)[R1,Double-Pressure], 7(1.1298)[R2,Double-Pressure]
- P3: 1(8.0823)[R1,XVAR-Cons(CEM)], 4(6.887371428571428)[R2,XVAR-Cons(CEM)], 8(1.9236857142857144)[R3,XVAR-Cons(CE)], 0(1.506)[R1,Double-Pressure]
