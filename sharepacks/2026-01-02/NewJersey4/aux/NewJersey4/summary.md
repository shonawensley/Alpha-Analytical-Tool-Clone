# Aux Summary — NewJersey4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=504, 770, 418, 366, 356
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=770, 366, 421, 065, 530
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2026-01-02/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=504, 418, 356, 633, 311

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=22 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=22), P2:8 (gap=38), P3:2 (gap=23)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=54.61530357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 289: score=48.47053571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 292: score=43.651489285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 989: score=43.526764285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 222: score=43.246632142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=42.85521428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 212: score=42.54498928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=41.949489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=41.10232857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 262: score=40.84333214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 388: ds=988 sev=B
- 005: ds=986 sev=B
- 024: ds=923 sev=B
- 227: ds=889 sev=B
- 266: ds=877 sev=B
- 335: ds=873 sev=B
- 155: ds=859 sev=B
- 277: ds=802 sev=B
- 359: ds=678 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=151 sev=red
  - 22: ds=61 sev=purple
  - 88: ds=47 sev=purple
  - 00: ds=18 sev=-
  - 44: ds=17 sev=-
  - 99: ds=15 sev=-
  - 11: ds=8 sev=-
  - 33: ds=6 sev=-
  - 66: ds=3 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 08: ds=47 sev=blue
  - 19: ds=43 sev=blue
  - 39: ds=40 sev=blue
  - 26: ds=36 sev=purple
  - 25: ds=35 sev=purple
  - 02: ds=34 sev=purple
  - 27: ds=34 sev=purple
  - 69: ds=33 sev=purple
  - 89: ds=29 sev=purple
  - 17: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:802, 35:621, 1:236, 32:152, 28:99, 14:92, 17:91, 12:80, 16:75, 19:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=802 fs=2 fl=0 hz=0.016666666666666666, 35:ds=621 fs=1 fl=0 hz=0.008368200836820083, 1:ds=236 fs=0 fl=2 hz=0.005333333333333333, 32:ds=152 fs=2 fl=2 hz=0.005980861244019139, 28:ds=99 fs=20 fl=1 hz=0.024277456647398846, 14:ds=92 fs=35 fl=1 hz=0.041474654377880185, 17:ds=91 fs=20 fl=2 hz=0.02564102564102564, 12:ds=80 fs=38 fl=1 hz=0.044167610419026046, 16:ds=75 fs=1 fl=4 hz=0.007926023778071334, 19:ds=59 fs=26 fl=1 hz=0.030439684329199548

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=60 flags=purple
- S22: ds=54 flags=purple
- S16: ds=46 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=18 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=33), P2:8 (gap=23), P3:3 (gap=15)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=54.61530357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 289: score=48.47053571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 292: score=43.651489285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 989: score=43.526764285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 222: score=43.246632142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=42.85521428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 212: score=42.54498928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=41.949489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=41.10232857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 262: score=40.84333214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=975 sev=B
- 778: ds=971 sev=B
- 069: ds=947 sev=B
- 899: ds=920 sev=B
- 455: ds=911 sev=B
- 009: ds=891 sev=B
- 005: ds=889 sev=B
- 099: ds=844 sev=B
- 359: ds=828 sev=B
- 477: ds=819 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=75 sev=blue
  - 11: ds=45 sev=purple
  - 33: ds=33 sev=purple
  - 00: ds=32 sev=purple
  - 22: ds=30 sev=purple
  - 88: ds=23 sev=-
  - 44: ds=8 sev=-
  - 99: ds=7 sev=-
  - 66: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 26: ds=77 sev=red
  - 17: ds=45 sev=blue
  - 39: ds=40 sev=blue
  - 02: ds=27 sev=purple
  - 27: ds=26 sev=purple
  - 01: ds=25 sev=purple
  - 45: ds=24 sev=-
  - 08: ds=23 sev=-
  - 19: ds=21 sev=-
  - 48: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:444, 1:366, 35:310, 32:231, 5:75, 14:58, 12:51, 28:49, 17:45, 24:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=444 fs=1 fl=0 hz=0.007246376811594203, 1:ds=366 fs=4 fl=0 hz=0.009554140127388535, 35:ds=310 fs=3 fl=0 hz=0.008032128514056224, 32:ds=231 fs=0 fl=0 hz=0.003552397868561279, 5:ds=75 fs=12 fl=4 hz=0.017429193899782137, 14:ds=58 fs=37 fl=0 hz=0.039784946236559135, 12:ds=51 fs=41 fl=1 hz=0.04530744336569579, 28:ds=49 fs=20 fl=2 hz=0.023231256599788808, 17:ds=45 fs=26 fl=1 hz=0.029411764705882353, 24:ds=44 fs=59 fl=0 hz=0.06184486373165618

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=98 flags=purple
- S25: ds=88 flags=blue+purple
- S3: ds=80 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=8 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=27), P2:2 (gap=34), P3:9 (gap=22)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=54.61530357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 289: score=48.47053571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 292: score=43.651489285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 989: score=43.526764285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 222: score=43.246632142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=42.85521428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 212: score=42.54498928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=41.949489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=41.10232857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 262: score=40.84333214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 035: ds=952 sev=B
- 499: ds=943 sev=B
- 339: ds=929 sev=B
- 556: ds=861 sev=B
- 000: ds=847 sev=B
- 335: ds=827 sev=B
- 569: ds=817 sev=B
- 558: ds=807 sev=B
- 088: ds=804 sev=B
- 022: ds=746 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=110 sev=red
  - 55: ds=103 sev=blue
  - 77: ds=85 sev=blue
  - 44: ds=42 sev=purple
  - 22: ds=34 sev=purple
  - 99: ds=22 sev=-
  - 66: ds=19 sev=-
  - 00: ds=9 sev=-
  - 11: ds=4 sev=-
  - 33: ds=3 sev=-
- non_repeating:
  - 59: ds=64 sev=red
  - 03: ds=53 sev=blue
  - 08: ds=48 sev=blue
  - 47: ds=40 sev=blue
  - 25: ds=34 sev=purple
  - 89: ds=30 sev=purple
  - 34: ds=29 sev=purple
  - 12: ds=25 sev=purple
  - 09: ds=24 sev=-
  - 19: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:423, 26:401, 13:125, 1:118, 27:106, 4:103, 16:100, 17:97, 19:86, 28:78

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=423 fs=2 fl=1 hz=0.007692307692307693, 26:ds=401 fs=1 fl=0 hz=0.0056179775280898875, 13:ds=125 fs=16 fl=2 hz=0.021686746987951807, 1:ds=118 fs=1 fl=2 hz=0.008213552361396304, 27:ds=106 fs=7 fl=2 hz=0.011325028312570783, 4:ds=103 fs=14 fl=1 hz=0.01839080459770115, 16:ds=100 fs=2 fl=2 hz=0.012658227848101266, 17:ds=97 fs=10 fl=2 hz=0.014051522248243558, 19:ds=86 fs=18 fl=2 hz=0.022172949002217293, 28:ds=78 fs=26 fl=0 hz=0.028291621327529923

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=58 flags=blue+purple
- S23: ds=50 flags=purple
- S17: ds=46 flags=purple
- S21: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 005 -> combined:986(B); midday:889(B)
- 335 -> combined:873(B); evening:827(B)
- 359 -> combined:678(B); midday:828(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:34(purple); midday:27(purple)
- 08 -> combined:47(blue); evening:48(blue)
- 17 -> combined:28(purple); midday:45(blue)
- 22 -> combined:61(purple); evening:34(purple); midday:30(purple)
- 25 -> combined:35(purple); evening:34(purple)
- 26 -> combined:36(purple); midday:77(red)
- 27 -> combined:34(purple); midday:26(purple)
- 39 -> combined:40(blue); midday:40(blue)
- 55 -> combined:151(red); evening:103(blue); midday:75(blue)
- 88 -> combined:47(purple); evening:110(red)
- 89 -> combined:29(purple); evening:30(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(7.333507142857143)[R1,XVAR-Cons(CEM)], 1(3.4653)[R2,XVAR-Cons(CM)], 9(3.0182857142857142)[R3,XVAR-Cons(CE)], 7(1.1269785714285714)[R2,Mirror-Echo], 8(0.2881)[R3,Swap]
- P2: 8(8.083814285714286)[R1,XVAR-Cons(CEM)], 2(1.715142857142857)[R1,Double-Pressure], 9(1.1199999999999999)[R2,Mirror-Echo], 1(1.0135)[R2,Double-Pressure], 4(0.41800000000000004)[R3,Mirror-Echo]
- P3: 2(7.306099999999999)[R1,Mirror-Echo], 9(6.5532142857142865)[R2,XVAR-Cons(CEM)], 3(1.1178571428571429)[R1,Double-Pressure], 7(0.5682857142857143)[R3,Mirror-Echo], 5(0.31497142857142857)[R3,Swap]
