# Aux Summary — Connecticut4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-06-23/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=835, 281, 155, 950, 763
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-06-23/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=281, 950, 913, 620, 221
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-06-23/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=835, 155, 763, 201, 070

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=2 last_repeat_gap=7 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=16), P2:4 (gap=21), P3:7 (gap=26)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.24317142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 547: score=42.4667 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=41.011025714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 346: score=35.46432857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 546: score=34.68785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 377: score=33.26833571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 577: score=32.491864285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 397: score=32.27627142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 317: score=31.570271428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 307: score=31.510414285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=940 sev=B
- 111: ds=924 sev=B
- 145: ds=899 sev=B
- 448: ds=841 sev=B
- 004: ds=832 sev=B
- 223: ds=813 sev=B
- 099: ds=804 sev=B
- 001: ds=787 sev=B
- 127: ds=786 sev=B
- 466: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=167 sev=red
  - 88: ds=33 sev=purple
  - 44: ds=32 sev=purple
  - 99: ds=25 sev=purple
  - 11: ds=18 sev=-
  - 66: ds=15 sev=-
  - 77: ds=12 sev=-
  - 22: ds=9 sev=-
  - 00: ds=8 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 14: ds=89 sev=red
  - 03: ds=47 sev=blue
  - 56: ds=43 sev=blue
  - 04: ds=42 sev=blue
  - 47: ds=39 sev=blue
  - 68: ds=31 sev=purple
  - 27: ds=30 sev=purple
  - 57: ds=29 sev=purple
  - 17: ds=26 sev=purple
  - 79: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 4:85, 23:76, 8:70, 14:65, 10:49, 15:45, 6:43, 9:42, 30:39, 29:36

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 4:ds=85 fs=25 fl=2 hz=0.029900332225913623, 23:ds=76 fs=17 fl=2 hz=0.021372328458942633, 8:ds=70 fs=43 fl=0 hz=0.04658721560130011, 14:ds=65 fs=31 fl=0 hz=0.033879781420765025, 10:ds=49 fs=17 fl=1 hz=0.022641509433962266, 15:ds=45 fs=17 fl=3 hz=0.02107481559536354, 6:ds=43 fs=31 fl=0 hz=0.03311965811965812, 9:ds=42 fs=35 fl=1 hz=0.03761755485893417, 30:ds=39 fs=55 fl=0 hz=0.05789473684210526, 29:ds=36 fs=26 fl=1 hz=0.02857142857142857

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=90 flags=red+purple
- S4: ds=70 flags=purple
- S12: ds=61 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 045: score=4 tags=FLT,MIR,RS
  - 459: score=4 tags=FLT,MIR,RS
  - 027: score=3 tags=MIR,RS
  - 126: score=3 tags=MIR,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=MIR,RS
  - 378: score=3 tags=MIR,RS
  - 468: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 036: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=33 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:0 (gap=27), P3:7 (gap=14)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.24317142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 547: score=42.4667 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=41.011025714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 346: score=35.46432857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 546: score=34.68785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 377: score=33.26833571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 577: score=32.491864285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 397: score=32.27627142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 317: score=31.570271428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 307: score=31.510414285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=893 sev=B
- 337: ds=856 sev=B
- 889: ds=826 sev=B
- 234: ds=777 sev=B
- 225: ds=753 sev=B
- 077: ds=734 sev=B
- 009: ds=727 sev=B
- 279: ds=700 sev=B
- 117: ds=686 sev=B
- 478: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=83 sev=blue
  - 11: ds=74 sev=blue
  - 00: ds=42 sev=purple
  - 44: ds=39 sev=purple
  - 77: ds=25 sev=purple
  - 88: ds=16 sev=-
  - 55: ds=13 sev=-
  - 99: ds=12 sev=-
  - 66: ds=7 sev=-
  - 22: ds=4 sev=-
- non_repeating:
  - 69: ds=69 sev=red
  - 14: ds=44 sev=blue
  - 04: ds=36 sev=purple
  - 45: ds=32 sev=purple
  - 58: ds=32 sev=purple
  - 67: ds=28 sev=purple
  - 01: ds=27 sev=purple
  - 29: ds=26 sev=purple
  - 79: ds=25 sev=purple
  - 27: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:144, 13:125, 19:106, 23:92, 17:74, 2:67, 8:59, 27:51, 31:48, 12:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=144 fs=2 fl=0 hz=0.006006006006006006, 13:ds=125 fs=16 fl=1 hz=0.021013597033374538, 19:ds=106 fs=21 fl=1 hz=0.026284348864994027, 23:ds=92 fs=22 fl=1 hz=0.02561247216035635, 17:ds=74 fs=32 fl=2 hz=0.037158469945355196, 2:ds=67 fs=22 fl=1 hz=0.026713124274099886, 8:ds=59 fs=53 fl=0 hz=0.05644302449414271, 27:ds=51 fs=16 fl=3 hz=0.020452099031216364, 31:ds=48 fs=20 fl=3 hz=0.024390243902439025, 12:ds=43 fs=50 fl=0 hz=0.052576235541535225

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=94 flags=purple
- S6: ds=67 flags=red+purple
- S9: ds=59 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 034: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 124: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 349: score=3 tags=FLT,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 016: score=2 tags=RS
  - 025: score=2 tags=RS
  - 169: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=25 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=18), P2:1 (gap=28), P3:6 (gap=14)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.24317142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 547: score=42.4667 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=41.011025714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 346: score=35.46432857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 546: score=34.68785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 377: score=33.26833571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 577: score=32.491864285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 397: score=32.27627142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 317: score=31.570271428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 307: score=31.510414285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 255: ds=935 sev=B
- 034: ds=912 sev=B
- 228: ds=890 sev=B
- 088: ds=888 sev=B
- 223: ds=849 sev=B
- 666: ds=837 sev=B
- 225: ds=812 sev=B
- 678: ds=713 sev=B
- 668: ds=710 sev=B
- 399: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=86 sev=blue
  - 88: ds=51 sev=purple
  - 99: ds=17 sev=-
  - 44: ds=16 sev=-
  - 66: ds=14 sev=-
  - 11: ds=9 sev=-
  - 22: ds=7 sev=-
  - 77: ds=6 sev=-
  - 00: ds=4 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 14: ds=79 sev=red
  - 56: ds=74 sev=red
  - 16: ds=45 sev=blue
  - 08: ds=37 sev=blue
  - 03: ds=35 sev=purple
  - 57: ds=33 sev=purple
  - 39: ds=32 sev=purple
  - 34: ds=31 sev=purple
  - 47: ds=31 sev=purple
  - 13: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 20:225, 15:146, 32:132, 16:119, 34:95, 4:57, 6:55, 33:51, 10:43, 14:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 20:ds=225 fs=18 fl=2 hz=0.0258732212160414, 15:ds=146 fs=14 fl=1 hz=0.025466893039049237, 32:ds=132 fs=2 fl=0 hz=0.004120879120879121, 16:ds=119 fs=2 fl=1 hz=0.005961251862891207, 34:ds=95 fs=20 fl=2 hz=0.025, 4:ds=57 fs=22 fl=1 hz=0.024918743228602384, 6:ds=55 fs=16 fl=1 hz=0.0196078431372549, 33:ds=51 fs=29 fl=0 hz=0.03176341730558598, 10:ds=43 fs=20 fl=3 hz=0.02561247216035635, 14:ds=42 fs=35 fl=0 hz=0.0384204909284952

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=95 flags=red+purple
- S8: ds=93 flags=red+purple
- S24: ds=72 flags=purple
- S20: ds=71 flags=purple
- S6: ds=59 flags=purple
- S2: ds=55 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 249: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR
  - 348: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 044 -> combined:699(B); evening:705(B)
- 145 -> combined:899(B); evening:674(B)
- 223 -> combined:813(B); evening:849(B)
- 225 -> evening:812(B); midday:753(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:47(blue); evening:35(purple)
- 04 -> combined:42(blue); midday:36(purple)
- 14 -> combined:89(red); evening:79(red); midday:44(blue)
- 33 -> combined:167(red); evening:86(blue); midday:83(blue)
- 44 -> combined:32(purple); midday:39(purple)
- 47 -> combined:39(blue); evening:31(purple)
- 56 -> combined:43(blue); evening:74(red)
- 57 -> combined:29(purple); evening:33(purple)
- 79 -> combined:26(purple); midday:25(purple)
- 88 -> combined:33(purple); evening:51(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(3.4374285714285713)[R2,XVAR-Cons(CE)], 5(2.660957142857143)[R1,XVAR-Cons(CM)], 4(2.618257142857143)[R3,XVAR-Cons(CE)], 1(1.5061428571428572)[R1,Double-Pressure], 7(1.0971)[R2,Double-Pressure]
- P2: 4(7.2089)[R1,Mirror-Echo], 7(1.7340642857142858)[R3,XVAR-Cons(CM)], 1(1.536)[R1,Double-Pressure], 0(1.4761428571428572)[R1,Double-Pressure], 9(1.242)[R2,Mirror-Echo]
- P3: 7(7.596842857142858)[R1,Mirror-Echo], 6(3.3179999999999996)[R2,XVAR-Cons(CE)], 9(0.9508)[R2,Double-Pressure], 2(0.6394285714285715)[R3,Mirror-Echo], 4(0.2612285714285714)[R3,Swap]
