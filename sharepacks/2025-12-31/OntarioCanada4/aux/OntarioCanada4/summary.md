# Aux Summary — OntarioCanada4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-12-31/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=372, 409, 043, 006, 297
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-12-31/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=409, 006, 313, 909, 497
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-12-31/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=372, 043, 297, 606, 056

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=46 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=20), P2:8 (gap=18), P3:4 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 888: score=37.57125857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 184: score=36.058014285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 188: score=35.888778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.550442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=32.1356 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 181: score=31.893148571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=31.62802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.46078 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 484: score=31.128658571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 180: score=30.282907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=997 sev=B
- 128: ds=917 sev=B
- 555: ds=882 sev=B
- 039: ds=773 sev=B
- 333: ds=744 sev=B
- 188: ds=717 sev=B
- 266: ds=703 sev=B
- 477: ds=701 sev=B
- 126: ds=693 sev=B
- 669: ds=688 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=119 sev=red
  - 55: ds=75 sev=blue
  - 11: ds=34 sev=purple
  - 88: ds=28 sev=purple
  - 44: ds=19 sev=-
  - 77: ds=10 sev=-
  - 99: ds=7 sev=-
  - 66: ds=6 sev=-
  - 33: ds=5 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 89: ds=79 sev=red
  - 01: ds=54 sev=blue
  - 68: ds=52 sev=blue
  - 15: ds=51 sev=blue
  - 17: ds=45 sev=blue
  - 18: ds=45 sev=blue
  - 12: ds=31 sev=purple
  - 69: ds=30 sev=purple
  - 24: ds=29 sev=purple
  - 26: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:329, 16:283, 17:155, 20:133, 33:79, 12:78, 26:73, 30:63, 34:60, 8:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=329 fs=1 fl=0 hz=0.005698005698005698, 16:ds=283 fs=2 fl=0 hz=0.006329113924050633, 17:ds=155 fs=19 fl=1 hz=0.024242424242424242, 20:ds=133 fs=14 fl=2 hz=0.01853997682502897, 33:ds=79 fs=24 fl=1 hz=0.027472527472527472, 12:ds=78 fs=45 fl=0 hz=0.04928806133625411, 26:ds=73 fs=2 fl=1 hz=0.006075334143377886, 30:ds=63 fs=39 fl=1 hz=0.04405286343612335, 34:ds=60 fs=14 fl=2 hz=0.019698725376593278, 8:ds=56 fs=39 fl=2 hz=0.044956140350877194

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=97 flags=red+purple
- S23: ds=74 flags=blue+purple
- S21: ds=71 flags=purple
- S4: ds=65 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 127: score=4 tags=FLT,MIR,RS
  - 136: score=4 tags=FLT,MIR,RS
  - 019: score=3 tags=FLT,RS
  - 028: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 469: score=3 tags=MIR,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=2 last_repeat_gap=15 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=25), P2:7 (gap=21), P3:8 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 888: score=37.57125857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 184: score=36.058014285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 188: score=35.888778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.550442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=32.1356 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 181: score=31.893148571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=31.62802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.46078 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 484: score=31.128658571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 180: score=30.282907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=993 sev=B
- 333: ds=976 sev=B
- 255: ds=943 sev=B
- 355: ds=908 sev=B
- 466: ds=829 sev=B
- 446: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=59 sev=purple
  - 55: ds=37 sev=purple
  - 11: ds=27 sev=purple
  - 77: ds=20 sev=-
  - 88: ds=16 sev=-
  - 66: ds=11 sev=-
  - 44: ds=9 sev=-
  - 99: ds=3 sev=-
  - 33: ds=2 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 34: ds=68 sev=red
  - 07: ds=65 sev=red
  - 16: ds=51 sev=blue
  - 39: ds=39 sev=blue
  - 89: ds=39 sev=blue
  - 68: ds=35 sev=purple
  - 37: ds=34 sev=purple
  - 67: ds=34 sev=purple
  - 03: ds=32 sev=purple
  - 48: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:164, 34:159, 16:141, 27:96, 12:93, 14:78, 17:77, 20:66, 19:51, 24:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=164 fs=4 fl=3 hz=0.010432190760059612, 34:ds=159 fs=8 fl=4 hz=0.014423076923076924, 16:ds=141 fs=3 fl=0 hz=0.007462686567164179, 27:ds=96 fs=15 fl=2 hz=0.0189520624303233, 12:ds=93 fs=45 fl=0 hz=0.05079006772009029, 14:ds=78 fs=39 fl=0 hz=0.04276315789473684, 17:ds=77 fs=29 fl=2 hz=0.033879781420765025, 20:ds=66 fs=24 fl=3 hz=0.029315960912052113, 19:ds=51 fs=20 fl=2 hz=0.023732470334412083, 24:ds=41 fs=48 fl=0 hz=0.052805280528052806

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=75 flags=purple
- S25: ds=71 flags=purple
- S1: ds=60 flags=blue+purple
- S5: ds=58 flags=purple
- S8: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=52 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=15), P2:1 (gap=50), P3:9 (gap=37)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=50)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 888: score=37.57125857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 184: score=36.058014285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 188: score=35.888778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.550442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=32.1356 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 181: score=31.893148571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=31.62802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.46078 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 484: score=31.128658571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 180: score=30.282907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=900 sev=B
- 113: ds=851 sev=B
- 378: ds=844 sev=B
- 566: ds=833 sev=B
- 199: ds=825 sev=B
- 899: ds=803 sev=B
- 126: ds=799 sev=B
- 559: ds=794 sev=B
- 477: ds=783 sev=B
- 558: ds=749 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=229 sev=red
  - 22: ds=60 sev=purple
  - 00: ds=47 sev=purple
  - 44: ds=30 sev=purple
  - 11: ds=17 sev=-
  - 99: ds=15 sev=-
  - 88: ds=14 sev=-
  - 33: ds=12 sev=-
  - 77: ds=5 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 36: ds=72 sev=red
  - 24: ds=56 sev=red
  - 18: ds=50 sev=blue
  - 89: ds=50 sev=blue
  - 15: ds=49 sev=blue
  - 78: ds=48 sev=blue
  - 49: ds=42 sev=blue
  - 57: ds=39 sev=blue
  - 09: ds=29 sev=purple
  - 01: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:425, 1:340, 16:191, 26:123, 18:108, 17:101, 20:92, 3:71, 23:64, 33:62

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=425 fs=0 fl=2 hz=0.005366726296958855, 1:ds=340 fs=0 fl=0 hz=0.0, 16:ds=191 fs=3 fl=1 hz=0.007853403141361256, 26:ds=123 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=108 fs=16 fl=1 hz=0.019384264538198404, 17:ds=101 fs=13 fl=3 hz=0.018626309662398137, 20:ds=92 fs=15 fl=2 hz=0.01925254813137033, 3:ds=71 fs=15 fl=4 hz=0.02092511013215859, 23:ds=64 fs=25 fl=2 hz=0.03085714285714286, 33:ds=62 fs=27 fl=1 hz=0.030803080308030802

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=81 flags=purple
- S2: ds=71 flags=blue+purple
- S4: ds=69 flags=purple
- S25: ds=58 flags=purple
- S20: ds=51 flags=purple
- S9: ds=49 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:693(B); evening:799(B)
- 128 -> combined:917(B); evening:900(B)
- 333 -> combined:744(B); midday:976(B)
- 477 -> combined:701(B); evening:783(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:54(blue); evening:27(purple); midday:27(purple)
- 11 -> combined:34(purple); midday:27(purple)
- 12 -> combined:31(purple); evening:27(purple)
- 15 -> combined:51(blue); evening:49(blue); midday:25(purple)
- 18 -> combined:45(blue); evening:50(blue)
- 22 -> combined:119(red); evening:60(purple); midday:59(purple)
- 24 -> combined:29(purple); evening:56(red)
- 55 -> combined:75(blue); evening:229(red); midday:37(purple)
- 67 -> combined:26(purple); midday:34(purple)
- 68 -> combined:52(blue); evening:26(purple); midday:35(purple)
- 69 -> combined:30(purple); midday:26(purple)
- 89 -> combined:79(red); evening:50(blue); midday:39(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.8301714285714286)[R1,XVAR-Cons(CM)], 8(3.3226)[R2,XVAR-Cons(CE)], 5(2.8444285714285718)[R3,XVAR-Cons(CM)], 9(1.1150357142857141)[R1,Mirror-Echo], 4(0.3513642857142857)[R3,Mirror-Echo]
- P2: 8(6.581035714285714)[R1,Mirror-Echo], 6(2.970557142857143)[R3,XVAR-Cons(CE)], 1(1.8684999999999998)[R1,Mirror-Echo], 3(1.2791428571428571)[R2,Mirror-Echo], 7(0.706392857142857)[R1,Mirror-Echo]
- P3: 8(3.9775714285714283)[R2,XVAR-Cons(CM)], 4(3.146807142857143)[R1,XVAR-Cons(CE)], 9(1.724392857142857)[R1,Mirror-Echo], 1(1.0252999999999999)[R2,Double-Pressure], 0(0.8716999999999999)[R2,Double-Pressure]
