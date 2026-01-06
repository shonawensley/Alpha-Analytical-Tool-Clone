# Aux Summary — NewJersey4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=963, 293, 331, 633, 504
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=293, 633, 770, 366, 421
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2026-01-04/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=963, 331, 504, 418, 356

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=3 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=24), P2:8 (gap=42), P3:2 (gap=27)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 182: score=49.325700000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=49.11657142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 882: score=43.429300000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=43.22017142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 282: score=42.55681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 122: score=41.81265714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 129: score=41.60352857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 989: score=38.88550214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 142: score=37.13637142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 112: score=37.09567142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 388: ds=992 sev=B
- 005: ds=990 sev=B
- 024: ds=927 sev=B
- 227: ds=893 sev=B
- 266: ds=881 sev=B
- 335: ds=877 sev=B
- 155: ds=863 sev=B
- 277: ds=806 sev=B
- 359: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=155 sev=red
  - 22: ds=65 sev=purple
  - 88: ds=51 sev=purple
  - 00: ds=22 sev=-
  - 44: ds=21 sev=-
  - 99: ds=19 sev=-
  - 11: ds=12 sev=-
  - 66: ds=7 sev=-
  - 77: ds=5 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 08: ds=51 sev=blue
  - 19: ds=47 sev=blue
  - 26: ds=40 sev=blue
  - 25: ds=39 sev=blue
  - 02: ds=38 sev=blue
  - 27: ds=38 sev=blue
  - 89: ds=33 sev=purple
  - 17: ds=32 sev=purple
  - 16: ds=31 sev=purple
  - 28: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:806, 35:625, 1:240, 32:156, 28:103, 14:96, 17:95, 12:84, 16:79, 19:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=806 fs=2 fl=0 hz=0.016666666666666666, 35:ds=625 fs=1 fl=0 hz=0.008368200836820083, 1:ds=240 fs=0 fl=2 hz=0.005333333333333333, 32:ds=156 fs=2 fl=2 hz=0.005980861244019139, 28:ds=103 fs=20 fl=1 hz=0.024277456647398846, 14:ds=96 fs=35 fl=1 hz=0.041474654377880185, 17:ds=95 fs=20 fl=2 hz=0.02564102564102564, 12:ds=84 fs=38 fl=1 hz=0.044167610419026046, 16:ds=79 fs=1 fl=4 hz=0.007926023778071334, 19:ds=63 fs=26 fl=1 hz=0.030439684329199548

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=64 flags=purple
- S22: ds=58 flags=purple
- S16: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=20 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=19), P2:8 (gap=25), P3:2 (gap=13)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 182: score=49.325700000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=49.11657142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 882: score=43.429300000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=43.22017142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 282: score=42.55681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 122: score=41.81265714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 129: score=41.60352857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 989: score=38.88550214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 142: score=37.13637142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 112: score=37.09567142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=977 sev=B
- 778: ds=973 sev=B
- 069: ds=949 sev=B
- 899: ds=922 sev=B
- 455: ds=913 sev=B
- 009: ds=893 sev=B
- 005: ds=891 sev=B
- 099: ds=846 sev=B
- 359: ds=830 sev=B
- 477: ds=821 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=77 sev=blue
  - 11: ds=47 sev=purple
  - 00: ds=34 sev=purple
  - 22: ds=32 sev=purple
  - 88: ds=25 sev=purple
  - 44: ds=10 sev=-
  - 99: ds=9 sev=-
  - 66: ds=3 sev=-
  - 77: ds=2 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 26: ds=79 sev=red
  - 17: ds=47 sev=blue
  - 02: ds=29 sev=purple
  - 27: ds=28 sev=purple
  - 01: ds=27 sev=purple
  - 45: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 19: ds=23 sev=-
  - 48: ds=22 sev=-
  - 58: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:446, 1:368, 35:312, 32:233, 5:77, 14:60, 12:53, 28:51, 17:47, 24:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=446 fs=1 fl=0 hz=0.007246376811594203, 1:ds=368 fs=4 fl=0 hz=0.009554140127388535, 35:ds=312 fs=3 fl=0 hz=0.008032128514056224, 32:ds=233 fs=0 fl=0 hz=0.003552397868561279, 5:ds=77 fs=12 fl=4 hz=0.017429193899782137, 14:ds=60 fs=37 fl=0 hz=0.039784946236559135, 12:ds=53 fs=41 fl=1 hz=0.04530744336569579, 28:ds=51 fs=20 fl=2 hz=0.023231256599788808, 17:ds=47 fs=26 fl=1 hz=0.029411764705882353, 24:ds=46 fs=58 fl=0 hz=0.06568516421291054

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=90 flags=blue+purple
- S3: ds=82 flags=blue+purple

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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=10 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=24), P2:2 (gap=36), P3:9 (gap=24)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 182: score=49.325700000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=49.11657142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 882: score=43.429300000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 889: score=43.22017142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 282: score=42.55681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 122: score=41.81265714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 129: score=41.60352857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 989: score=38.88550214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 142: score=37.13637142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 112: score=37.09567142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 035: ds=954 sev=B
- 499: ds=945 sev=B
- 339: ds=931 sev=B
- 556: ds=863 sev=B
- 000: ds=849 sev=B
- 335: ds=829 sev=B
- 569: ds=819 sev=B
- 558: ds=809 sev=B
- 088: ds=806 sev=B
- 022: ds=748 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=112 sev=red
  - 55: ds=105 sev=blue
  - 77: ds=87 sev=blue
  - 44: ds=44 sev=purple
  - 22: ds=36 sev=purple
  - 99: ds=24 sev=-
  - 66: ds=21 sev=-
  - 00: ds=11 sev=-
  - 11: ds=6 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 59: ds=66 sev=red
  - 03: ds=55 sev=blue
  - 08: ds=50 sev=blue
  - 47: ds=42 sev=blue
  - 25: ds=36 sev=purple
  - 89: ds=32 sev=purple
  - 34: ds=31 sev=purple
  - 12: ds=27 sev=purple
  - 09: ds=26 sev=purple
  - 19: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:425, 26:403, 13:127, 1:120, 27:108, 4:105, 16:102, 17:99, 19:88, 28:80

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=425 fs=2 fl=1 hz=0.007692307692307693, 26:ds=403 fs=1 fl=0 hz=0.0056179775280898875, 13:ds=127 fs=16 fl=2 hz=0.021686746987951807, 1:ds=120 fs=1 fl=2 hz=0.008213552361396304, 27:ds=108 fs=7 fl=2 hz=0.011325028312570783, 4:ds=105 fs=14 fl=1 hz=0.01839080459770115, 16:ds=102 fs=2 fl=2 hz=0.012658227848101266, 17:ds=99 fs=10 fl=2 hz=0.014051522248243558, 19:ds=88 fs=18 fl=2 hz=0.022172949002217293, 28:ds=80 fs=26 fl=0 hz=0.028291621327529923

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=60 flags=blue+purple
- S23: ds=52 flags=purple
- S17: ds=48 flags=purple
- S21: ds=34 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 005 -> combined:990(B); midday:891(B)
- 335 -> combined:877(B); evening:829(B)
- 359 -> combined:682(B); midday:830(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:38(blue); midday:29(purple)
- 08 -> combined:51(blue); evening:50(blue); midday:25(purple)
- 17 -> combined:32(purple); midday:47(blue)
- 19 -> combined:47(blue); evening:26(purple)
- 22 -> combined:65(purple); evening:36(purple); midday:32(purple)
- 25 -> combined:39(blue); evening:36(purple)
- 26 -> combined:40(blue); midday:79(red)
- 27 -> combined:38(blue); midday:28(purple)
- 47 -> combined:25(purple); evening:42(blue)
- 55 -> combined:155(red); evening:105(blue); midday:77(blue)
- 88 -> combined:51(purple); evening:112(red); midday:25(purple)
- 89 -> combined:33(purple); evening:32(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(6.7828)[R1,XVAR-Cons(CEM)], 8(3.3864)[R2,XVAR-Cons(CM)], 7(1.5100714285714285)[R1,Mirror-Echo], 2(1.2974142857142856)[R2,Mirror-Echo], 0(0.2255714285714286)[R3,Swap]
- P2: 8(8.285328571428572)[R1,XVAR-Cons(CEM)], 2(3.2722857142857142)[R3,XVAR-Cons(CE)], 4(1.0959999999999999)[R2,Double-Pressure], 1(1.0553)[R2,Double-Pressure], 5(0.30153571428571424)[R3,Swap]
- P3: 2(7.757571428571429)[R1,Mirror-Echo], 9(7.548442857142856)[R2,XVAR-Cons(CEM)], 7(0.682)[R3,Mirror-Echo], 4(0.34835714285714287)[R3,Mirror-Echo], 5(0.3418428571428571)[R3,Swap]
