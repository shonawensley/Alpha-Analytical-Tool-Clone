# Aux Summary — PuertoRico4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-04/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=359, 529, 917, 144, 913
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-04/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=529, 144, 451, 098, 875
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-04/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=359, 917, 913, 643, 785

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=9 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=62), P2:3 (gap=22), P3:6 (gap=25)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=62)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 236: score=50.75138571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 206: score=42.561099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=42.107749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 276: score=41.75272142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=40.80746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 216: score=40.776607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 836: score=40.70773571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 266: score=40.25646428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 230: score=40.254821428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 636: score=37.47891357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=995 sev=B
- 447: ds=986 sev=B
- 000: ds=734 sev=B
- 039: ds=722 sev=B
- 466: ds=718 sev=B
- 677: ds=696 sev=B
- 577: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=66 sev=purple
  - 77: ds=65 sev=purple
  - 99: ds=56 sev=purple
  - 11: ds=50 sev=purple
  - 55: ds=31 sev=purple
  - 33: ds=26 sev=purple
  - 66: ds=25 sev=purple
  - 88: ds=18 sev=-
  - 00: ds=16 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 47: ds=174 sev=red
  - 24: ds=88 sev=red
  - 48: ds=52 sev=blue
  - 23: ds=49 sev=blue
  - 56: ds=45 sev=blue
  - 05: ds=43 sev=blue
  - 28: ds=38 sev=blue
  - 06: ds=25 sev=purple
  - 01: ds=22 sev=-
  - 03: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:193, 27:134, 5:97, 32:91, 26:86, 31:83, 28:65, 18:57, 34:56, 33:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=193 fs=18 fl=1 hz=0.025477707006369428, 27:ds=134 fs=24 fl=1 hz=0.029868578255675033, 5:ds=97 fs=27 fl=1 hz=0.0343980343980344, 32:ds=91 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=86 fs=4 fl=2 hz=0.01020408163265306, 31:ds=83 fs=14 fl=3 hz=0.018619934282584887, 28:ds=65 fs=26 fl=0 hz=0.0278372591006424, 18:ds=57 fs=20 fl=0 hz=0.022727272727272728, 34:ds=56 fs=26 fl=0 hz=0.02857142857142857, 33:ds=53 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=83 flags=purple
- S23: ds=65 flags=blue+purple
- S26: ds=56 flags=blue+purple
- S8: ds=50 flags=purple
- S6: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6', '8'], 'pairs': {'remaining_count': 1}}
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
- current_index=12 streak=1 max=3 last_repeat_gap=61 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=31), P2:1 (gap=27), P3:6 (gap=12)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 236: score=50.75138571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 206: score=42.561099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=42.107749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 276: score=41.75272142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=40.80746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 216: score=40.776607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 836: score=40.70773571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 266: score=40.25646428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 230: score=40.254821428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 636: score=37.47891357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=961 sev=B
- 299: ds=952 sev=B
- 003: ds=943 sev=B
- 077: ds=929 sev=B
- 333: ds=878 sev=B
- 555: ds=852 sev=B
- 088: ds=823 sev=B
- 888: ds=817 sev=B
- 666: ds=802 sev=B
- 447: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=108 sev=red
  - 22: ds=81 sev=blue
  - 11: ds=57 sev=purple
  - 99: ds=41 sev=purple
  - 77: ds=32 sev=purple
  - 33: ds=26 sev=purple
  - 88: ds=23 sev=-
  - 55: ds=15 sev=-
  - 66: ds=12 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 47: ds=114 sev=red
  - 24: ds=60 sev=red
  - 38: ds=45 sev=blue
  - 03: ds=44 sev=blue
  - 04: ds=44 sev=blue
  - 35: ds=42 sev=blue
  - 48: ds=34 sev=purple
  - 19: ds=33 sev=purple
  - 18: ds=30 sev=purple
  - 13: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:98, 10:96, 27:95, 26:92, 3:85, 16:57, 23:52, 15:50, 5:48, 32:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=98 fs=16 fl=2 hz=0.020809248554913295, 10:ds=96 fs=20 fl=3 hz=0.026376146788990827, 27:ds=95 fs=19 fl=1 hz=0.024721878862793572, 26:ds=92 fs=7 fl=2 hz=0.011682242990654207, 3:ds=85 fs=31 fl=0 hz=0.03506787330316742, 16:ds=57 fs=4 fl=2 hz=0.009695290858725763, 23:ds=52 fs=31 fl=1 hz=0.034782608695652174, 15:ds=50 fs=25 fl=0 hz=0.026939655172413795, 5:ds=48 fs=28 fl=0 hz=0.03181818181818182, 32:ds=45 fs=2 fl=1 hz=0.006112469437652812

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=44 flags=purple
- S25: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=3 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=31), P2:2 (gap=33), P3:6 (gap=23)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 236: score=50.75138571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 206: score=42.561099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 226: score=42.107749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 276: score=41.75272142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=40.80746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 216: score=40.776607142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Swap src=cartesian
- 836: score=40.70773571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 266: score=40.25646428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 230: score=40.254821428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 636: score=37.47891357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=993 sev=B
- 579: ds=974 sev=B
- 114: ds=918 sev=B
- 555: ds=857 sev=B
- 888: ds=765 sev=B
- 067: ds=754 sev=B
- 446: ds=741 sev=B
- 259: ds=739 sev=B
- 224: ds=725 sev=B
- 449: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=145 sev=red
  - 44: ds=141 sev=red
  - 77: ds=43 sev=purple
  - 66: ds=34 sev=purple
  - 22: ds=33 sev=purple
  - 99: ds=28 sev=purple
  - 11: ds=25 sev=purple
  - 33: ds=13 sev=-
  - 88: ds=9 sev=-
  - 00: ds=8 sev=-
- non_repeating:
  - 25: ds=101 sev=red
  - 47: ds=87 sev=red
  - 45: ds=71 sev=red
  - 26: ds=64 sev=red
  - 24: ds=44 sev=blue
  - 05: ds=40 sev=blue
  - 56: ds=40 sev=blue
  - 23: ds=31 sev=purple
  - 89: ds=28 sev=purple
  - 48: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:450, 32:165, 4:119, 10:106, 31:94, 5:84, 33:70, 27:67, 1:59, 30:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=450 fs=5 fl=1 hz=0.01662049861495845, 32:ds=165 fs=6 fl=1 hz=0.009987515605493134, 4:ds=119 fs=23 fl=2 hz=0.03071253071253071, 10:ds=106 fs=16 fl=2 hz=0.0234375, 31:ds=94 fs=18 fl=3 hz=0.02394526795895097, 5:ds=84 fs=18 fl=2 hz=0.022446689113355782, 33:ds=70 fs=12 fl=1 hz=0.017361111111111112, 27:ds=67 fs=18 fl=1 hz=0.02358490566037736, 1:ds=59 fs=4 fl=4 hz=0.00909090909090909, 30:ds=44 fs=42 fl=0 hz=0.044823906083244394

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=77 flags=purple
- S24: ds=68 flags=purple
- S18: ds=53 flags=red+purple
- S23: ds=48 flags=blue+purple
- S16: ds=43 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 447 -> combined:986(B); midday:741(B)
- 555 -> evening:857(B); midday:852(B)
- 888 -> evening:765(B); midday:817(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:43(blue); evening:40(blue)
- 11 -> combined:50(purple); evening:25(purple); midday:57(purple)
- 22 -> combined:66(purple); evening:33(purple); midday:81(blue)
- 23 -> combined:49(blue); evening:31(purple)
- 24 -> combined:88(red); evening:44(blue); midday:60(red)
- 33 -> combined:26(purple); midday:26(purple)
- 47 -> combined:174(red); evening:87(red); midday:114(red)
- 48 -> combined:52(blue); evening:26(purple); midday:34(purple)
- 55 -> combined:31(purple); evening:145(red)
- 56 -> combined:45(blue); evening:40(blue)
- 66 -> combined:25(purple); evening:34(purple)
- 77 -> combined:65(purple); evening:43(purple); midday:32(purple)
- 99 -> combined:56(purple); evening:28(purple); midday:41(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.902571428571429)[R1,Mirror-Echo], 8(2.3589214285714286)[R2,XVAR-Cons(CE)], 3(1.2016)[R2,Double-Pressure], 1(1.0344)[R2,Double-Pressure], 7(0.7131428571428572)[R3,Mirror-Echo]
- P2: 3(6.4809214285714285)[R1,XVAR-Cons(CEM)], 2(1.8372857142857142)[R1,Mirror-Echo], 0(1.7906357142857143)[R3,XVAR-Cons(CM)], 1(1.5061428571428572)[R1,Double-Pressure], 7(1.4822571428571427)[R2,Mirror-Echo]
- P3: 6(7.8678928571428575)[R1,XVAR-Cons(CEM)], 0(1.8713285714285715)[R3,XVAR-Cons(CM)], 2(0.964)[R2,Double-Pressure], 1(0.5599357142857142)[R3,Mirror-Echo], 4(0.3761999999999999)[R2]
