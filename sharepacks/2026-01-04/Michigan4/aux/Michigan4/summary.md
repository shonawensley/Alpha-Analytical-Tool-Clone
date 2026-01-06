# Aux Summary — Michigan4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2026-01-04/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=479, 826, 523, 975, 204
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2026-01-04/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=826, 975, 032, 583, 250
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2026-01-04/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=479, 523, 204, 477, 214

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=3 last_repeat_gap=4 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=33), P2:6 (gap=28), P3:8 (gap=35)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 368: score=53.06106535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 168: score=50.000871428571436 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=45.17066571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 361: score=44.42355642857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 348: score=41.106908571428576 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 164: score=39.03045714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 364: score=38.62616428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 165: score=38.56964285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 108: score=38.45520714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 360: score=38.228966785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=973 sev=B
- 111: ds=927 sev=B
- 077: ds=926 sev=B
- 556: ds=921 sev=B
- 144: ds=909 sev=B
- 599: ds=870 sev=B
- 099: ds=830 sev=B
- 247: ds=753 sev=B
- 135: ds=737 sev=B
- 399: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=76 sev=blue
  - 55: ds=62 sev=purple
  - 88: ds=58 sev=purple
  - 33: ds=33 sev=purple
  - 11: ds=29 sev=purple
  - 66: ds=28 sev=purple
  - 99: ds=17 sev=-
  - 00: ds=16 sev=-
  - 44: ds=15 sev=-
  - 77: ds=6 sev=-
- non_repeating:
  - 01: ds=82 sev=red
  - 45: ds=69 sev=red
  - 19: ds=64 sev=red
  - 39: ds=43 sev=blue
  - 67: ds=38 sev=blue
  - 15: ds=35 sev=purple
  - 18: ds=35 sev=purple
  - 34: ds=31 sev=purple
  - 06: ds=30 sev=purple
  - 36: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:466, 32:325, 1:112, 6:110, 23:96, 10:88, 5:84, 30:80, 15:78, 20:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=466 fs=2 fl=3 hz=0.010660980810234541, 32:ds=325 fs=1 fl=0 hz=0.003125, 1:ds=112 fs=5 fl=1 hz=0.009060022650056626, 6:ds=110 fs=13 fl=2 hz=0.018018018018018018, 23:ds=96 fs=12 fl=3 hz=0.018203883495145633, 10:ds=88 fs=15 fl=3 hz=0.02011173184357542, 5:ds=84 fs=22 fl=1 hz=0.026345933562428404, 30:ds=80 fs=58 fl=0 hz=0.06775700934579439, 15:ds=78 fs=21 fl=2 hz=0.02547065337763012, 20:ds=72 fs=22 fl=1 hz=0.025081788440567066

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=66 flags=red+purple
- S2: ds=61 flags=purple
- S25: ds=58 flags=blue+purple
- S26: ds=55 flags=blue+purple
- S12: ds=40 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=3 tags=FLT,RS
  - 049: score=3 tags=MIR,RS
  - 058: score=3 tags=MIR,RS
  - 139: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 238: score=3 tags=MIR,RS
  - 247: score=3 tags=MIR,RS
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=8 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=17), P2:0 (gap=30), P3:8 (gap=17)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 368: score=53.06106535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 168: score=50.000871428571436 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=45.17066571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 361: score=44.42355642857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 348: score=41.106908571428576 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 164: score=39.03045714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 364: score=38.62616428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 165: score=38.56964285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 108: score=38.45520714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 360: score=38.228966785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 339: ds=999 sev=B
- 266: ds=971 sev=B
- 667: ds=868 sev=B
- 188: ds=828 sev=B
- 345: ds=821 sev=B
- 499: ds=816 sev=B
- 114: ds=807 sev=B
- 777: ds=787 sev=B
- 099: ds=776 sev=B
- 566: ds=754 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=128 sev=red
  - 88: ds=78 sev=blue
  - 55: ds=37 sev=purple
  - 66: ds=29 sev=purple
  - 33: ds=16 sev=-
  - 11: ds=14 sev=-
  - 00: ds=12 sev=-
  - 77: ds=9 sev=-
  - 99: ds=8 sev=-
  - 44: ds=7 sev=-
- non_repeating:
  - 69: ds=65 sev=red
  - 67: ds=61 sev=red
  - 07: ds=53 sev=blue
  - 19: ds=52 sev=blue
  - 04: ds=51 sev=blue
  - 01: ds=49 sev=blue
  - 12: ds=49 sev=blue
  - 45: ds=34 sev=purple
  - 24: ds=33 sev=purple
  - 06: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:467, 26:323, 16:182, 27:180, 32:162, 23:146, 6:123, 5:122, 24:89, 1:87

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=467 fs=2 fl=2 hz=0.01078167115902965, 26:ds=323 fs=0 fl=1 hz=0.005249343832020997, 16:ds=182 fs=1 fl=0 hz=0.008032128514056224, 27:ds=180 fs=23 fl=0 hz=0.03054448871181939, 32:ds=162 fs=4 fl=2 hz=0.008739076154806492, 23:ds=146 fs=12 fl=2 hz=0.017412935323383085, 6:ds=123 fs=19 fl=1 hz=0.02551020408163265, 5:ds=122 fs=10 fl=2 hz=0.01892744479495268, 24:ds=89 fs=60 fl=0 hz=0.06734006734006734, 1:ds=87 fs=2 fl=1 hz=0.0067226890756302525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S1: ds=94 flags=blue+purple
- S19: ds=79 flags=red+purple
- S25: ds=78 flags=purple
- S27: ds=74 flags=blue+purple
- S24: ds=73 flags=blue+purple
- S6: ds=55 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 0}}
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
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=3 last_repeat_gap=21 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=26), P2:5 (gap=31), P3:5 (gap=27)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 368: score=53.06106535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 168: score=50.000871428571436 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=45.17066571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 361: score=44.42355642857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 348: score=41.106908571428576 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 164: score=39.03045714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 364: score=38.62616428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 165: score=38.56964285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 108: score=38.45520714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 360: score=38.228966785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 017: ds=978 sev=B
- 146: ds=904 sev=B
- 135: ds=825 sev=B
- 557: ds=804 sev=B
- 258: ds=792 sev=B
- 144: ds=768 sev=B
- 228: ds=759 sev=B
- 009: ds=751 sev=B
- 399: ds=730 sev=B
- 288: ds=713 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=114 sev=red
  - 22: ds=38 sev=purple
  - 33: ds=33 sev=purple
  - 55: ds=31 sev=purple
  - 99: ds=30 sev=purple
  - 88: ds=29 sev=purple
  - 11: ds=17 sev=-
  - 66: ds=14 sev=-
  - 00: ds=8 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 34: ds=71 sev=red
  - 56: ds=69 sev=red
  - 48: ds=68 sev=red
  - 03: ds=53 sev=blue
  - 38: ds=52 sev=blue
  - 01: ds=41 sev=blue
  - 05: ds=41 sev=blue
  - 15: ds=41 sev=blue
  - 39: ds=40 sev=blue
  - 45: ds=39 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:233, 32:169, 17:103, 7:82, 9:65, 34:63, 1:56, 6:55, 23:48, 10:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=233 fs=4 fl=0 hz=0.0091324200913242, 32:ds=169 fs=2 fl=0 hz=0.005859375, 17:ds=103 fs=16 fl=3 hz=0.021252796420581654, 7:ds=82 fs=36 fl=0 hz=0.040178571428571425, 9:ds=65 fs=35 fl=1 hz=0.03854389721627409, 34:ds=63 fs=9 fl=2 hz=0.01649175412293853, 1:ds=56 fs=2 fl=5 hz=0.008130081300813009, 6:ds=55 fs=18 fl=3 hz=0.022850924918389557, 23:ds=48 fs=22 fl=3 hz=0.026399155227032733, 10:ds=44 fs=18 fl=3 hz=0.022900763358778626

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=63 flags=blue+purple
- S2: ds=55 flags=purple
- S9: ds=54 flags=red+purple
- S3: ds=53 flags=purple
- S14: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 099 -> combined:830(B); midday:776(B)
- 135 -> combined:737(B); evening:825(B)
- 144 -> combined:909(B); evening:768(B)
- 399 -> combined:683(B); evening:730(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:82(red); evening:41(blue); midday:49(blue)
- 06 -> combined:30(purple); midday:32(purple)
- 15 -> combined:35(purple); evening:41(blue)
- 19 -> combined:64(red); evening:32(purple); midday:52(blue)
- 22 -> combined:76(blue); evening:38(purple); midday:128(red)
- 33 -> combined:33(purple); evening:33(purple)
- 34 -> combined:31(purple); evening:71(red)
- 39 -> combined:43(blue); evening:40(blue)
- 45 -> combined:69(red); evening:39(blue); midday:34(purple)
- 55 -> combined:62(purple); evening:31(purple); midday:37(purple)
- 56 -> combined:27(purple); evening:69(red)
- 66 -> combined:28(purple); midday:29(purple)
- 67 -> combined:38(blue); midday:61(red)
- 88 -> combined:58(purple); evening:29(purple); midday:78(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(8.047828571428571)[R1,XVAR-Cons(CEM)], 1(7.452121428571429)[R2,Mirror-Echo], 6(2.401364285714286)[R3,Mirror-Echo], 9(0.24779285714285712)[R3,Swap]
- P2: 6(7.141378571428571)[R1,XVAR-Cons(CEM)], 0(1.5957142857142856)[R1,Double-Pressure], 5(1.5955714285714284)[R1,Double-Pressure], 4(1.0942857142857143)[R2,Mirror-Echo], 3(1.0344)[R2,Double-Pressure]
- P3: 8(7.9073714285714285)[R1,XVAR-Cons(CEM)], 1(2.570407142857143)[R2,XVAR-Cons(CE)], 5(1.4761428571428572)[R1,Double-Pressure], 4(0.9369571428571428)[R2,Mirror-Echo], 9(0.2929857142857143)[R3,Mirror-Echo]
