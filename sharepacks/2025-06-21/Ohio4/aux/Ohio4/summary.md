# Aux Summary — Ohio4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2025-06-21/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=899, 270, 412, 112, 754
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2025-06-21/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=270, 112, 456, 552, 382
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2025-06-21/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=899, 412, 754, 433, 031

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=2 last_repeat_gap=40 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=15), P2:0 (gap=17), P3:5 (gap=23)
- consensus_notes: P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 945: score=35.84150714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 965: score=34.95895 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 545: score=33.003745 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 565: score=32.12118785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 905: score=31.112364285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 845: score=30.919364285714288 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 935: score=30.906507142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 995: score=30.787078571428573 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=30.036807142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 975: score=29.16617857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=934 sev=B
- 166: ds=889 sev=B
- 559: ds=883 sev=B
- 668: ds=877 sev=B
- 449: ds=867 sev=B
- 377: ds=857 sev=B
- 146: ds=775 sev=B
- 339: ds=771 sev=B
- 019: ds=754 sev=B
- 888: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=120 sev=red
  - 66: ds=82 sev=blue
  - 77: ds=31 sev=purple
  - 44: ds=29 sev=purple
  - 22: ds=20 sev=-
  - 88: ds=18 sev=-
  - 55: ds=7 sev=-
  - 33: ds=6 sev=-
  - 11: ds=3 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 04: ds=48 sev=blue
  - 58: ds=43 sev=blue
  - 29: ds=42 sev=blue
  - 06: ds=40 sev=blue
  - 16: ds=34 sev=purple
  - 18: ds=34 sev=purple
  - 79: ds=32 sev=purple
  - 08: ds=28 sev=purple
  - 78: ds=28 sev=purple
  - 15: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 27:173, 32:136, 35:129, 1:120, 4:104, 23:88, 28:86, 15:73, 2:66, 16:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 27:ds=173 fs=22 fl=2 hz=0.030690537084398974, 32:ds=136 fs=2 fl=0 hz=0.006051437216338881, 35:ds=129 fs=0 fl=1 hz=0.0027100271002710027, 1:ds=120 fs=3 fl=1 hz=0.006702412868632708, 4:ds=104 fs=21 fl=2 hz=0.026047565118912798, 23:ds=88 fs=29 fl=1 hz=0.03428571428571429, 28:ds=86 fs=26 fl=1 hz=0.03085714285714286, 15:ds=73 fs=26 fl=2 hz=0.03181818181818182, 2:ds=66 fs=22 fl=2 hz=0.027809965237543453, 16:ds=65 fs=1 fl=1 hz=0.003640776699029126

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=93 flags=purple
- S2: ds=90 flags=blue+purple
- S5: ds=87 flags=purple
- S20: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=7 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=21), P2:3 (gap=11), P3:3 (gap=17)
- consensus_notes: P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 945: score=35.84150714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 965: score=34.95895 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 545: score=33.003745 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 565: score=32.12118785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 905: score=31.112364285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 845: score=30.919364285714288 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 935: score=30.906507142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 995: score=30.787078571428573 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=30.036807142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 975: score=29.16617857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=921 sev=B
- 466: ds=895 sev=B
- 117: ds=894 sev=B
- 029: ds=887 sev=B
- 066: ds=865 sev=B
- 388: ds=845 sev=B
- 556: ds=800 sev=B
- 688: ds=777 sev=B
- 788: ds=759 sev=B
- 222: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=81 sev=blue
  - 66: ds=53 sev=purple
  - 33: ds=50 sev=purple
  - 88: ds=46 sev=purple
  - 22: ds=43 sev=purple
  - 99: ds=24 sev=-
  - 77: ds=15 sev=-
  - 44: ds=14 sev=-
  - 55: ds=3 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 78: ds=48 sev=blue
  - 08: ds=42 sev=blue
  - 79: ds=39 sev=blue
  - 26: ds=37 sev=blue
  - 04: ds=33 sev=purple
  - 36: ds=28 sev=purple
  - 29: ds=24 sev=-
  - 06: ds=23 sev=-
  - 16: ds=23 sev=-
  - 58: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:284, 19:232, 32:217, 2:100, 28:92, 27:86, 34:85, 23:67, 35:64, 18:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=284 fs=2 fl=0 hz=0.006382978723404256, 19:ds=232 fs=16 fl=0 hz=0.02309782608695652, 32:ds=217 fs=4 fl=2 hz=0.009510869565217392, 2:ds=100 fs=19 fl=1 hz=0.02242152466367713, 28:ds=92 fs=24 fl=2 hz=0.029478458049886625, 27:ds=86 fs=24 fl=2 hz=0.030842230130486363, 34:ds=85 fs=26 fl=2 hz=0.030701754385964914, 23:ds=67 fs=25 fl=0 hz=0.032552083333333336, 35:ds=64 fs=0 fl=3 hz=0.005333333333333333, 18:ds=53 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=76 flags=purple
- S22: ds=64 flags=purple
- S24: ds=60 flags=purple
- S25: ds=46 flags=purple
- S2: ds=45 flags=blue+purple
- S5: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 049: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 249: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR
  - 349: score=2 tags=FLT,MIR
  - 389: score=2 tags=FLT,MIR
  - 459: score=2 tags=FLT,MIR
  - 469: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=3 last_repeat_gap=11 last_repeat_index=10

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=16), P2:4 (gap=18), P3:5 (gap=33)
- consensus_notes: P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 945: score=35.84150714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 965: score=34.95895 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 545: score=33.003745 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 565: score=32.12118785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 905: score=31.112364285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 845: score=30.919364285714288 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 935: score=30.906507142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 995: score=30.787078571428573 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 865: score=30.036807142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 975: score=29.16617857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 446: ds=955 sev=B
- 199: ds=831 sev=B
- 678: ds=825 sev=B
- 003: ds=824 sev=B
- 357: ds=804 sev=B
- 559: ds=799 sev=B
- 777: ds=776 sev=B
- 166: ds=748 sev=B
- 224: ds=744 sev=B
- 038: ds=725 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=88 sev=blue
  - 00: ds=60 sev=purple
  - 77: ds=46 sev=purple
  - 66: ds=41 sev=purple
  - 44: ds=18 sev=-
  - 22: ds=10 sev=-
  - 88: ds=9 sev=-
  - 11: ds=8 sev=-
  - 33: ds=3 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 37: ds=75 sev=red
  - 35: ds=52 sev=blue
  - 39: ds=49 sev=blue
  - 58: ds=48 sev=blue
  - 38: ds=44 sev=blue
  - 56: ds=41 sev=blue
  - 48: ds=39 sev=blue
  - 05: ds=33 sev=purple
  - 69: ds=28 sev=purple
  - 09: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:252, 15:138, 35:132, 3:117, 27:109, 16:93, 5:84, 30:75, 32:68, 1:60

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=252 fs=4 fl=1 hz=0.009646302250803858, 15:ds=138 fs=27 fl=0 hz=0.03214285714285715, 35:ds=132 fs=1 fl=1 hz=0.00423728813559322, 3:ds=117 fs=24 fl=1 hz=0.02937720329024677, 27:ds=109 fs=21 fl=3 hz=0.027777777777777776, 16:ds=93 fs=1 fl=1 hz=0.003886010362694301, 5:ds=84 fs=14 fl=3 hz=0.020383693045563547, 30:ds=75 fs=37 fl=0 hz=0.04138702460850112, 32:ds=68 fs=0 fl=0 hz=0.0011534025374855825, 1:ds=60 fs=3 fl=0 hz=0.006024096385542169

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=79 flags=purple
- S3: ds=72 flags=purple
- S5: ds=55 flags=blue+purple
- S21: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 126: score=1 tags=FLT
  - 136: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 029 -> combined:712(B); midday:887(B)
- 066 -> combined:934(B); midday:865(B)
- 166 -> combined:889(B); evening:748(B)
- 224 -> evening:744(B); midday:696(B)
- 449 -> combined:867(B); evening:677(B)
- 559 -> combined:883(B); evening:799(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:120(red); evening:60(purple); midday:81(blue)
- 04 -> combined:48(blue); midday:33(purple)
- 05 -> combined:25(purple); evening:33(purple)
- 08 -> combined:28(purple); midday:42(blue)
- 09 -> combined:25(purple); evening:26(purple)
- 58 -> combined:43(blue); evening:48(blue)
- 66 -> combined:82(blue); evening:41(purple); midday:53(purple)
- 77 -> combined:31(purple); evening:46(purple)
- 78 -> combined:28(purple); midday:48(blue)
- 79 -> combined:32(purple); midday:39(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.649142857142857)[R1,XVAR-Cons(CE)], 8(1.2269999999999999)[R1,Double-Pressure], 0(1.0761999999999998)[R2,Double-Pressure], 6(0.9199999999999999)[R2,Double-Pressure], 5(0.879)[R2,Double-Pressure]
- P2: 4(3.4634285714285715)[R2,XVAR-Cons(CE)], 6(2.5808714285714287)[R3,XVAR-Cons(CE)], 0(1.2342857142857142)[R1,Double-Pressure], 3(1.0284285714285715)[R1,Double-Pressure], 9(0.9089999999999999)[R2,Double-Pressure]
- P3: 5(7.228935714285714)[R1,XVAR-Cons(CEM)], 8(2.4469214285714287)[R2,XVAR-Cons(CE)], 0(1.4404571428571429)[R2,Mirror-Echo], 3(1.1075714285714284)[R1,Double-Pressure], 9(0.9208)[R2,Double-Pressure]
