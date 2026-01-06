# Aux Summary — Michigan4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2026-01-02/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=204, 032, 477, 583, 214
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2026-01-02/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=032, 583, 250, 731, 587
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2026-01-02/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=204, 477, 214, 896, 089

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=42 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=29), P2:6 (gap=24), P3:5 (gap=50)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 165: score=45.5821 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 168: score=44.891242857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 365: score=41.60923571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 368: score=40.91837857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 125: score=40.85539285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 128: score=40.16453571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 565: score=39.89008571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 868: score=37.768191428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 325: score=36.882528571428566 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 328: score=36.191671428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=969 sev=B
- 111: ds=923 sev=B
- 077: ds=922 sev=B
- 556: ds=917 sev=B
- 144: ds=905 sev=B
- 599: ds=866 sev=B
- 099: ds=826 sev=B
- 247: ds=749 sev=B
- 135: ds=733 sev=B
- 399: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=72 sev=blue
  - 55: ds=58 sev=purple
  - 88: ds=54 sev=purple
  - 33: ds=29 sev=purple
  - 11: ds=25 sev=purple
  - 66: ds=24 sev=-
  - 99: ds=13 sev=-
  - 00: ds=12 sev=-
  - 44: ds=11 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 01: ds=78 sev=red
  - 45: ds=65 sev=red
  - 19: ds=60 sev=red
  - 59: ds=50 sev=blue
  - 28: ds=40 sev=blue
  - 39: ds=39 sev=blue
  - 26: ds=36 sev=purple
  - 67: ds=34 sev=purple
  - 15: ds=31 sev=purple
  - 18: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:462, 32:321, 1:108, 6:106, 23:92, 10:84, 5:80, 30:76, 15:74, 20:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=462 fs=2 fl=3 hz=0.010660980810234541, 32:ds=321 fs=1 fl=0 hz=0.003125, 1:ds=108 fs=5 fl=1 hz=0.009060022650056626, 6:ds=106 fs=14 fl=2 hz=0.019079685746352413, 23:ds=92 fs=12 fl=3 hz=0.018203883495145633, 10:ds=84 fs=15 fl=3 hz=0.02011173184357542, 5:ds=80 fs=22 fl=1 hz=0.026345933562428404, 30:ds=76 fs=58 fl=0 hz=0.06775700934579439, 15:ds=74 fs=21 fl=2 hz=0.02547065337763012, 20:ds=68 fs=22 fl=1 hz=0.025081788440567066

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=62 flags=red+purple
- S2: ds=57 flags=purple
- S25: ds=54 flags=blue+purple
- S26: ds=51 flags=blue+purple
- S21: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=6 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=19), P2:2 (gap=31), P3:5 (gap=32)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 165: score=45.5821 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 168: score=44.891242857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 365: score=41.60923571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 368: score=40.91837857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 125: score=40.85539285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 128: score=40.16453571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 565: score=39.89008571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 868: score=37.768191428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 325: score=36.882528571428566 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 328: score=36.191671428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 339: ds=997 sev=B
- 266: ds=969 sev=B
- 667: ds=866 sev=B
- 188: ds=826 sev=B
- 345: ds=819 sev=B
- 499: ds=814 sev=B
- 114: ds=805 sev=B
- 777: ds=785 sev=B
- 099: ds=774 sev=B
- 566: ds=752 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=126 sev=red
  - 88: ds=76 sev=blue
  - 55: ds=35 sev=purple
  - 66: ds=27 sev=purple
  - 33: ds=14 sev=-
  - 11: ds=12 sev=-
  - 00: ds=10 sev=-
  - 77: ds=7 sev=-
  - 99: ds=6 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 69: ds=63 sev=red
  - 67: ds=59 sev=red
  - 07: ds=51 sev=blue
  - 19: ds=50 sev=blue
  - 04: ds=49 sev=blue
  - 01: ds=47 sev=blue
  - 12: ds=47 sev=blue
  - 59: ds=43 sev=blue
  - 26: ds=33 sev=purple
  - 45: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:465, 26:321, 16:180, 27:178, 32:160, 23:144, 6:121, 5:120, 24:87, 1:85

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=465 fs=2 fl=2 hz=0.01078167115902965, 26:ds=321 fs=0 fl=1 hz=0.005249343832020997, 16:ds=180 fs=1 fl=0 hz=0.008032128514056224, 27:ds=178 fs=23 fl=0 hz=0.03054448871181939, 32:ds=160 fs=4 fl=2 hz=0.008739076154806492, 23:ds=144 fs=12 fl=2 hz=0.017412935323383085, 6:ds=121 fs=19 fl=1 hz=0.02551020408163265, 5:ds=120 fs=10 fl=2 hz=0.01892744479495268, 24:ds=87 fs=60 fl=0 hz=0.06734006734006734, 1:ds=85 fs=2 fl=1 hz=0.0067226890756302525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S1: ds=92 flags=blue+purple
- S19: ds=77 flags=purple
- S25: ds=76 flags=purple
- S27: ds=72 flags=blue+purple
- S24: ds=71 flags=blue+purple
- S21: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=19 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=42), P2:5 (gap=29), P3:3 (gap=26)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 165: score=45.5821 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 168: score=44.891242857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 365: score=41.60923571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 368: score=40.91837857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 125: score=40.85539285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 128: score=40.16453571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 565: score=39.89008571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 868: score=37.768191428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 325: score=36.882528571428566 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 328: score=36.191671428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 017: ds=976 sev=B
- 146: ds=902 sev=B
- 135: ds=823 sev=B
- 557: ds=802 sev=B
- 258: ds=790 sev=B
- 144: ds=766 sev=B
- 228: ds=757 sev=B
- 009: ds=749 sev=B
- 399: ds=728 sev=B
- 288: ds=711 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=112 sev=red
  - 22: ds=36 sev=purple
  - 33: ds=31 sev=purple
  - 55: ds=29 sev=purple
  - 99: ds=28 sev=purple
  - 88: ds=27 sev=purple
  - 11: ds=15 sev=-
  - 66: ds=12 sev=-
  - 00: ds=6 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 34: ds=69 sev=red
  - 56: ds=67 sev=red
  - 48: ds=66 sev=red
  - 25: ds=62 sev=red
  - 03: ds=51 sev=blue
  - 38: ds=50 sev=blue
  - 01: ds=39 sev=blue
  - 05: ds=39 sev=blue
  - 15: ds=39 sev=blue
  - 39: ds=38 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:231, 32:167, 17:101, 7:80, 9:63, 34:61, 1:54, 6:53, 23:46, 10:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=231 fs=4 fl=0 hz=0.0091324200913242, 32:ds=167 fs=2 fl=0 hz=0.005859375, 17:ds=101 fs=16 fl=3 hz=0.021252796420581654, 7:ds=80 fs=36 fl=0 hz=0.040178571428571425, 9:ds=63 fs=35 fl=1 hz=0.03854389721627409, 34:ds=61 fs=9 fl=2 hz=0.01649175412293853, 1:ds=54 fs=2 fl=5 hz=0.008130081300813009, 6:ds=53 fs=18 fl=3 hz=0.022850924918389557, 23:ds=46 fs=22 fl=3 hz=0.026399155227032733, 10:ds=42 fs=19 fl=3 hz=0.02301255230125523

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=61 flags=blue+purple
- S2: ds=53 flags=purple
- S9: ds=52 flags=red+purple
- S3: ds=51 flags=purple
- S20: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 099 -> combined:826(B); midday:774(B)
- 135 -> combined:733(B); evening:823(B)
- 144 -> combined:905(B); evening:766(B)
- 399 -> combined:679(B); evening:728(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:78(red); evening:39(blue); midday:47(blue)
- 06 -> combined:26(purple); midday:30(purple)
- 15 -> combined:31(purple); evening:39(blue)
- 19 -> combined:60(red); evening:30(purple); midday:50(blue)
- 22 -> combined:72(blue); evening:36(purple); midday:126(red)
- 26 -> combined:36(purple); midday:33(purple)
- 33 -> combined:29(purple); evening:31(purple)
- 34 -> combined:27(purple); evening:69(red)
- 39 -> combined:39(blue); evening:38(blue)
- 45 -> combined:65(red); evening:37(blue); midday:32(purple)
- 55 -> combined:58(purple); evening:29(purple); midday:35(purple)
- 59 -> combined:50(blue); evening:25(purple); midday:43(blue)
- 67 -> combined:34(purple); midday:59(red)
- 88 -> combined:54(purple); evening:27(purple); midday:76(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(5.485892857142857)[R2,XVAR-Cons(CEM)], 3(4.013028571428571)[R1,XVAR-Cons(CE)], 9(2.1918571428571427)[R3,XVAR-Cons(CM)], 5(1.7149999999999999)[R1,Double-Pressure], 8(1.0044)[R2,Double-Pressure]
- P2: 6(6.048278571428572)[R1,XVAR-Cons(CEM)], 2(3.821571428571428)[R2,XVAR-Cons(CM)], 5(1.5658571428571428)[R1,Double-Pressure], 0(1.2551999999999999)[R2,Double-Pressure], 3(0.9925999999999999)[R2,Double-Pressure]
- P3: 5(8.54792857142857)[R1,XVAR-Cons(CEM)], 8(6.8570714285714285)[R2,XVAR-Cons(CEM)], 3(1.4984285714285714)[R1,Mirror-Echo], 6(0.24779285714285712)[R3,Swap], 9(0.11314285714285714)[R3]
