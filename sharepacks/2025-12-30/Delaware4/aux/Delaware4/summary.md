# Aux Summary — Delaware4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2025-12-30/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=386, 357, 660, 989, 022
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2025-12-30/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=357, 989, 355, 612, 603
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2025-12-30/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=386, 660, 022, 866, 865

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=9 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=17), P2:3 (gap=22), P3:1 (gap=32)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=45.47553500000001 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 141: score=38.943599285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=37.766999999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 171: score=37.35115642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 151: score=34.93674214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 111: score=34.65011357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 134: score=34.56832142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 138: score=31.564407142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 941: score=31.235064285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 434: score=30.94695 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=961 sev=B
- 447: ds=953 sev=B
- 033: ds=886 sev=B
- 337: ds=841 sev=B
- 288: ds=826 sev=B
- 579: ds=803 sev=B
- 088: ds=789 sev=B
- 155: ds=760 sev=B
- 079: ds=757 sev=B
- 269: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=52 sev=purple
  - 11: ds=44 sev=purple
  - 88: ds=26 sev=purple
  - 00: ds=23 sev=-
  - 33: ds=22 sev=-
  - 77: ds=20 sev=-
  - 55: ds=5 sev=-
  - 22: ds=4 sev=-
  - 99: ds=3 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 79: ds=106 sev=red
  - 24: ds=76 sev=red
  - 19: ds=68 sev=red
  - 48: ds=53 sev=blue
  - 13: ds=45 sev=blue
  - 47: ds=37 sev=blue
  - 78: ds=31 sev=purple
  - 17: ds=25 sev=purple
  - 27: ds=25 sev=purple
  - 01: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:224, 2:153, 32:118, 28:110, 19:84, 1:83, 31:79, 16:58, 26:56, 22:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=224 fs=5 fl=2 hz=0.010767160161507403, 2:ds=153 fs=13 fl=3 hz=0.01932367149758454, 32:ds=118 fs=3 fl=4 hz=0.009111617312072893, 28:ds=110 fs=14 fl=4 hz=0.02112676056338028, 19:ds=84 fs=30 fl=2 hz=0.03535911602209945, 1:ds=83 fs=1 fl=2 hz=0.008746355685131196, 31:ds=79 fs=16 fl=4 hz=0.022321428571428572, 16:ds=58 fs=2 fl=6 hz=0.009876543209876543, 26:ds=56 fs=8 fl=4 hz=0.014888337468982629, 22:ds=50 fs=46 fl=0 hz=0.0500544069640914

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=77 flags=purple
- S5: ds=46 flags=blue+purple
- S11: ds=45 flags=purple
- S2: ds=42 flags=blue+purple
- S8: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=38 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=15), P2:3 (gap=21), P3:0 (gap=24)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=45.47553500000001 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 141: score=38.943599285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=37.766999999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 171: score=37.35115642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 151: score=34.93674214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 111: score=34.65011357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 134: score=34.56832142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 138: score=31.564407142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 941: score=31.235064285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 434: score=30.94695 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 122: ds=949 sev=B
- 778: ds=945 sev=B
- 118: ds=883 sev=B
- 066: ds=795 sev=B
- 155: ds=782 sev=B
- 033: ds=781 sev=B
- 444: ds=753 sev=B
- 269: ds=695 sev=B
- 005: ds=688 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=69 sev=purple
  - 33: ds=65 sev=purple
  - 44: ds=51 sev=purple
  - 66: ds=43 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=11 sev=-
  - 77: ds=10 sev=-
  - 22: ds=5 sev=-
  - 55: ds=2 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 19: ds=72 sev=red
  - 09: ds=59 sev=red
  - 25: ds=58 sev=red
  - 79: ds=54 sev=blue
  - 23: ds=48 sev=blue
  - 24: ds=39 sev=blue
  - 29: ds=39 sev=blue
  - 58: ds=38 sev=blue
  - 59: ds=38 sev=blue
  - 08: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:263, 32:198, 3:173, 15:120, 12:115, 26:107, 16:83, 28:82, 2:76, 29:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=263 fs=2 fl=1 hz=0.013636363636363637, 32:ds=198 fs=3 fl=1 hz=0.008077544426494346, 3:ds=173 fs=18 fl=0 hz=0.023899371069182388, 15:ds=120 fs=14 fl=3 hz=0.019744483159117306, 12:ds=115 fs=43 fl=0 hz=0.048919226393629126, 26:ds=107 fs=6 fl=0 hz=0.012750455373406192, 16:ds=83 fs=1 fl=1 hz=0.0053475935828877, 28:ds=82 fs=21 fl=1 hz=0.024309392265193373, 2:ds=76 fs=17 fl=3 hz=0.022123893805309734, 29:ds=71 fs=21 fl=2 hz=0.02519167579408543

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=76 flags=red+purple
- S25: ds=64 flags=purple
- S20: ds=54 flags=purple
- S22: ds=38 flags=purple
- S8: ds=32 flags=purple

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
- current_index=23 streak=1 max=3 last_repeat_gap=65 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=41), P2:5 (gap=18), P3:4 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:9 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=45.47553500000001 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 141: score=38.943599285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=37.766999999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 171: score=37.35115642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 151: score=34.93674214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 111: score=34.65011357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 134: score=34.56832142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 138: score=31.564407142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 941: score=31.235064285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 434: score=30.94695 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 229: ds=946 sev=B
- 055: ds=914 sev=B
- 000: ds=870 sev=B
- 279: ds=827 sev=B
- 222: ds=815 sev=B
- 006: ds=769 sev=B
- 778: ds=748 sev=B
- 189: ds=713 sev=B
- 255: ds=711 sev=B
- 004: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=152 sev=red
  - 99: ds=57 sev=purple
  - 44: ds=26 sev=purple
  - 11: ds=22 sev=-
  - 00: ds=21 sev=-
  - 88: ds=13 sev=-
  - 33: ds=11 sev=-
  - 77: ds=10 sev=-
  - 22: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 79: ds=53 sev=blue
  - 37: ds=47 sev=blue
  - 69: ds=42 sev=blue
  - 03: ds=40 sev=blue
  - 24: ds=38 sev=blue
  - 48: ds=38 sev=blue
  - 89: ds=37 sev=blue
  - 13: ds=35 sev=purple
  - 19: ds=34 sev=purple
  - 35: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 5:172, 1:125, 35:112, 17:102, 31:84, 2:81, 32:59, 28:55, 21:47, 11:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 5:ds=172 fs=11 fl=2 hz=0.01643489254108723, 1:ds=125 fs=3 fl=1 hz=0.0063371356147021544, 35:ds=112 fs=3 fl=1 hz=0.007042253521126761, 17:ds=102 fs=20 fl=2 hz=0.02466367713004484, 31:ds=84 fs=20 fl=2 hz=0.025669642857142856, 2:ds=81 fs=15 fl=3 hz=0.02238805970149254, 32:ds=59 fs=2 fl=3 hz=0.007308160779537149, 28:ds=55 fs=16 fl=3 hz=0.02014846235418876, 21:ds=47 fs=50 fl=0 hz=0.052521008403361345, 11:ds=45 fs=54 fl=0 hz=0.05953693495038588

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=73 flags=blue+purple
- S23: ds=63 flags=purple
- S22: ds=61 flags=purple
- S18: ds=49 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '7', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 033 -> combined:886(B); midday:781(B)
- 155 -> combined:760(B); midday:782(B)
- 269 -> combined:738(B); midday:695(B)
- 778 -> evening:748(B); midday:945(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 13 -> combined:45(blue); evening:35(purple)
- 19 -> combined:68(red); evening:34(purple); midday:72(red)
- 24 -> combined:76(red); evening:38(blue); midday:39(blue)
- 44 -> combined:52(purple); evening:26(purple); midday:51(purple)
- 47 -> combined:37(blue); evening:25(purple)
- 48 -> combined:53(blue); evening:38(blue); midday:26(purple)
- 79 -> combined:106(red); evening:53(blue); midday:54(blue)
- 88 -> combined:26(purple); midday:69(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.5313857142857144)[R1,XVAR-Cons(CE)], 9(1.7149999999999999)[R1,Double-Pressure], 8(1.1178571428571429)[R1,Double-Pressure], 4(0.986)[R2,Double-Pressure], 0(0.8998999999999999)[R2,Double-Pressure]
- P2: 3(6.776221428571429)[R1,XVAR-Cons(CEM)], 4(2.744285714285714)[R3,XVAR-Cons(CM)], 7(2.151842857142857)[R2,XVAR-Cons(CM)], 5(1.2374285714285713)[R1,Double-Pressure], 1(0.9508)[R2,Double-Pressure]
- P3: 1(7.775778571428572)[R1,XVAR-Cons(CEM)], 4(3.7607142857142852)[R2,XVAR-Cons(CE)], 8(1.7568000000000001)[R3,XVAR-Cons(CE)], 0(1.3865714285714286)[R1,Double-Pressure], 6(0.40942142857142855)[R3,Mirror-Echo]
