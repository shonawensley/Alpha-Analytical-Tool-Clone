# Aux Summary — Delaware4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2025-12-31/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=563, 706, 386, 357, 660
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2025-12-31/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=706, 357, 989, 355, 612
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2025-12-31/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=563, 386, 660, 022, 866

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=11 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=19), P2:3 (gap=24), P3:1 (gap=34)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=50.92236785714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 134: score=45.47392857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 141: score=44.33346785714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 171: score=42.719274999999996 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 151: score=40.277282142857146 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 111: score=40.011696428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 144: score=38.88502857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 231: score=38.46605714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=37.373512142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 234: score=37.296078571428566 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=963 sev=B
- 447: ds=955 sev=B
- 033: ds=888 sev=B
- 337: ds=843 sev=B
- 288: ds=828 sev=B
- 579: ds=805 sev=B
- 088: ds=791 sev=B
- 155: ds=762 sev=B
- 079: ds=759 sev=B
- 269: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=54 sev=purple
  - 11: ds=46 sev=purple
  - 88: ds=28 sev=purple
  - 00: ds=25 sev=purple
  - 33: ds=24 sev=-
  - 77: ds=22 sev=-
  - 55: ds=7 sev=-
  - 22: ds=6 sev=-
  - 99: ds=5 sev=-
  - 66: ds=4 sev=-
- non_repeating:
  - 79: ds=108 sev=red
  - 24: ds=78 sev=red
  - 19: ds=70 sev=red
  - 48: ds=55 sev=blue
  - 13: ds=47 sev=blue
  - 47: ds=39 sev=blue
  - 78: ds=33 sev=purple
  - 17: ds=27 sev=purple
  - 27: ds=27 sev=purple
  - 01: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:226, 2:155, 32:120, 28:112, 19:86, 1:85, 31:81, 16:60, 26:58, 22:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=226 fs=5 fl=2 hz=0.010767160161507403, 2:ds=155 fs=13 fl=3 hz=0.01932367149758454, 32:ds=120 fs=3 fl=4 hz=0.009111617312072893, 28:ds=112 fs=14 fl=4 hz=0.02112676056338028, 19:ds=86 fs=30 fl=2 hz=0.03535911602209945, 1:ds=85 fs=1 fl=2 hz=0.008746355685131196, 31:ds=81 fs=16 fl=4 hz=0.022321428571428572, 16:ds=60 fs=2 fl=6 hz=0.009876543209876543, 26:ds=58 fs=8 fl=4 hz=0.014888337468982629, 22:ds=52 fs=46 fl=0 hz=0.0500544069640914

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=79 flags=purple
- S5: ds=48 flags=blue+purple
- S11: ds=47 flags=purple
- S2: ds=44 flags=blue+purple
- S8: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '4', '9'], 'pairs': {'remaining_count': 1}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=39 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=16), P2:3 (gap=22), P3:0 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=50.92236785714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 134: score=45.47392857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 141: score=44.33346785714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 171: score=42.719274999999996 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 151: score=40.277282142857146 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 111: score=40.011696428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 144: score=38.88502857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 231: score=38.46605714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=37.373512142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 234: score=37.296078571428566 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 122: ds=950 sev=B
- 778: ds=946 sev=B
- 118: ds=884 sev=B
- 066: ds=796 sev=B
- 155: ds=783 sev=B
- 033: ds=782 sev=B
- 444: ds=754 sev=B
- 269: ds=696 sev=B
- 005: ds=689 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=70 sev=purple
  - 33: ds=66 sev=purple
  - 44: ds=52 sev=purple
  - 66: ds=44 sev=purple
  - 11: ds=24 sev=-
  - 00: ds=12 sev=-
  - 77: ds=11 sev=-
  - 22: ds=6 sev=-
  - 55: ds=3 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 19: ds=73 sev=red
  - 09: ds=60 sev=red
  - 25: ds=59 sev=red
  - 79: ds=55 sev=blue
  - 23: ds=49 sev=blue
  - 24: ds=40 sev=blue
  - 29: ds=40 sev=blue
  - 58: ds=39 sev=blue
  - 59: ds=39 sev=blue
  - 08: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:264, 32:199, 3:174, 15:121, 12:116, 26:108, 16:84, 28:83, 2:77, 29:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=264 fs=2 fl=1 hz=0.013636363636363637, 32:ds=199 fs=3 fl=1 hz=0.008077544426494346, 3:ds=174 fs=18 fl=0 hz=0.023899371069182388, 15:ds=121 fs=14 fl=3 hz=0.019744483159117306, 12:ds=116 fs=43 fl=0 hz=0.048919226393629126, 26:ds=108 fs=6 fl=0 hz=0.012750455373406192, 16:ds=84 fs=1 fl=1 hz=0.0053475935828877, 28:ds=83 fs=21 fl=1 hz=0.024309392265193373, 2:ds=77 fs=17 fl=3 hz=0.022123893805309734, 29:ds=72 fs=21 fl=2 hz=0.02519167579408543

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=77 flags=red+purple
- S25: ds=65 flags=purple
- S20: ds=55 flags=purple
- S22: ds=39 flags=purple
- S8: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=66 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=42), P2:5 (gap=19), P3:4 (gap=24)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:9 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=50.92236785714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 134: score=45.47392857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 141: score=44.33346785714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 171: score=42.719274999999996 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 151: score=40.277282142857146 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 111: score=40.011696428571426 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 144: score=38.88502857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 231: score=38.46605714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=37.373512142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 234: score=37.296078571428566 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 229: ds=947 sev=B
- 055: ds=915 sev=B
- 000: ds=871 sev=B
- 279: ds=828 sev=B
- 222: ds=816 sev=B
- 006: ds=770 sev=B
- 778: ds=749 sev=B
- 189: ds=714 sev=B
- 255: ds=712 sev=B
- 004: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=153 sev=red
  - 99: ds=58 sev=purple
  - 44: ds=27 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=22 sev=-
  - 88: ds=14 sev=-
  - 33: ds=12 sev=-
  - 77: ds=11 sev=-
  - 22: ds=3 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 79: ds=54 sev=blue
  - 37: ds=48 sev=blue
  - 69: ds=43 sev=blue
  - 03: ds=41 sev=blue
  - 24: ds=39 sev=blue
  - 48: ds=39 sev=blue
  - 89: ds=38 sev=blue
  - 13: ds=36 sev=purple
  - 19: ds=35 sev=purple
  - 16: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 5:173, 1:126, 35:113, 17:103, 31:85, 2:82, 32:60, 28:56, 21:48, 11:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 5:ds=173 fs=11 fl=2 hz=0.01643489254108723, 1:ds=126 fs=3 fl=1 hz=0.0063371356147021544, 35:ds=113 fs=3 fl=1 hz=0.007042253521126761, 17:ds=103 fs=20 fl=2 hz=0.02466367713004484, 31:ds=85 fs=20 fl=2 hz=0.025669642857142856, 2:ds=82 fs=15 fl=3 hz=0.02238805970149254, 32:ds=60 fs=2 fl=3 hz=0.007308160779537149, 28:ds=56 fs=16 fl=3 hz=0.02014846235418876, 21:ds=48 fs=49 fl=0 hz=0.05190677966101695, 11:ds=46 fs=54 fl=0 hz=0.05953693495038588

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=74 flags=blue+purple
- S23: ds=64 flags=purple
- S22: ds=62 flags=purple
- S18: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '7', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 027: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 033 -> combined:888(B); midday:782(B)
- 155 -> combined:762(B); midday:783(B)
- 269 -> combined:740(B); midday:696(B)
- 778 -> evening:749(B); midday:946(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 08 -> combined:26(purple); midday:36(purple)
- 13 -> combined:47(blue); evening:36(purple)
- 18 -> combined:26(purple); midday:32(purple)
- 19 -> combined:70(red); evening:35(purple); midday:73(red)
- 24 -> combined:78(red); evening:39(blue); midday:40(blue)
- 44 -> combined:54(purple); evening:27(purple); midday:52(purple)
- 47 -> combined:39(blue); evening:26(purple)
- 48 -> combined:55(blue); evening:39(blue); midday:27(purple)
- 79 -> combined:108(red); evening:54(blue); midday:55(blue)
- 88 -> combined:28(purple); midday:70(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(6.436064285714286)[R1,XVAR-Cons(CEM)], 2(1.7582142857142857)[R3,XVAR-Cons(CE)], 9(1.7149999999999999)[R1,Double-Pressure], 8(1.1477142857142857)[R1,Double-Pressure], 4(1.03)[R2,Double-Pressure]
- P2: 3(6.882371428571429)[R1,XVAR-Cons(CEM)], 4(2.7934714285714284)[R3,XVAR-Cons(CM)], 7(2.179278571428571)[R2,XVAR-Cons(CM)], 5(1.2372857142857143)[R1,Double-Pressure], 1(0.9717)[R2,Double-Pressure]
- P3: 1(7.825471428571428)[R1,XVAR-Cons(CEM)], 4(6.655492857142857)[R2,XVAR-Cons(CEM)], 8(1.7985214285714286)[R3,XVAR-Cons(CE)], 0(1.4164285714285714)[R1,Double-Pressure]
