# Aux Summary — Florida4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2025-06-21/Florida4/aux/draws/Florida_draws.csv` n=1000 head=241, 433, 262, 255, 529
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2025-06-21/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=433, 255, 501, 572, 897
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2025-06-21/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=241, 262, 529, 666, 143

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=32 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=59), P2:1 (gap=20), P3:0 (gap=35)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=59)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 010: score=50.19091 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 310: score=50.06257428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 080: score=47.16706714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 380: score=46.735155 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 090: score=45.61262428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 060: score=44.852938571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=43.349552857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 390: score=42.21525714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 360: score=41.45557142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 070: score=41.43306714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 499: ds=966 sev=B
- 009: ds=915 sev=B
- 889: ds=893 sev=B
- 337: ds=867 sev=B
- 277: ds=840 sev=B
- 224: ds=799 sev=B
- 288: ds=780 sev=B
- 189: ds=763 sev=B
- 455: ds=754 sev=B
- 137: ds=752 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=62 sev=purple
  - 77: ds=61 sev=purple
  - 99: ds=46 sev=purple
  - 11: ds=17 sev=-
  - 88: ds=12 sev=-
  - 44: ds=11 sev=-
  - 66: ds=6 sev=-
  - 55: ds=3 sev=-
  - 22: ds=2 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 07: ds=92 sev=red
  - 47: ds=67 sev=red
  - 37: ds=51 sev=blue
  - 19: ds=49 sev=blue
  - 69: ds=46 sev=blue
  - 48: ds=45 sev=blue
  - 04: ds=40 sev=blue
  - 02: ds=37 sev=blue
  - 06: ds=37 sev=blue
  - 17: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:275, 31:91, 19:90, 16:87, 32:77, 1:64, 11:56, 34:53, 28:50, 9:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=275 fs=2 fl=0 hz=0.004552352048558422, 31:ds=91 fs=24 fl=1 hz=0.029481132075471695, 19:ds=90 fs=23 fl=1 hz=0.02724177071509648, 16:ds=87 fs=0 fl=2 hz=0.004761904761904762, 32:ds=77 fs=1 fl=1 hz=0.005797101449275362, 1:ds=64 fs=5 fl=2 hz=0.012302284710017574, 11:ds=56 fs=54 fl=0 hz=0.05787781350482315, 34:ds=53 fs=15 fl=2 hz=0.021683673469387755, 28:ds=50 fs=23 fl=1 hz=0.02823529411764706, 9:ds=49 fs=39 fl=1 hz=0.044543429844097995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S20: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=96 flags=blue+purple
- S26: ds=68 flags=blue+purple
- S5: ds=56 flags=purple
- S11: ds=54 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 029: score=3 tags=FLT,RS
  - 038: score=3 tags=FLT,RS
  - 047: score=3 tags=FLT,RS
  - 056: score=3 tags=FLT,RS
  - 128: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 389: score=3 tags=FLT,RS
  - 479: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 146: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=15 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=29), P2:1 (gap=51), P3:0 (gap=17)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=51)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 010: score=50.19091 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 310: score=50.06257428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 080: score=47.16706714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 380: score=46.735155 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 090: score=45.61262428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 060: score=44.852938571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=43.349552857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 390: score=42.21525714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 360: score=41.45557142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 070: score=41.43306714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=956 sev=B
- 555: ds=954 sev=B
- 066: ds=913 sev=B
- 011: ds=901 sev=B
- 003: ds=899 sev=B
- 266: ds=852 sev=B
- 008: ds=833 sev=B
- 557: ds=789 sev=B
- 122: ds=766 sev=B
- 126: ds=754 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=114 sev=red
  - 22: ds=104 sev=blue
  - 66: ds=79 sev=blue
  - 99: ds=36 sev=purple
  - 00: ds=32 sev=purple
  - 77: ds=30 sev=purple
  - 11: ds=8 sev=-
  - 44: ds=5 sev=-
  - 55: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 18: ds=92 sev=red
  - 69: ds=86 sev=red
  - 17: ds=61 sev=red
  - 07: ds=54 sev=blue
  - 12: ds=53 sev=blue
  - 16: ds=43 sev=blue
  - 14: ds=40 sev=blue
  - 24: ds=33 sev=purple
  - 47: ds=33 sev=purple
  - 04: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 19:229, 1:178, 26:137, 17:107, 20:77, 22:56, 18:51, 24:47, 31:45, 13:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 19:ds=229 fs=11 fl=1 hz=0.018691588785046728, 1:ds=178 fs=4 fl=1 hz=0.009022556390977444, 26:ds=137 fs=4 fl=0 hz=0.008207934336525308, 17:ds=107 fs=19 fl=0 hz=0.02288329519450801, 20:ds=77 fs=21 fl=1 hz=0.024858757062146894, 22:ds=56 fs=38 fl=1 hz=0.043237250554323724, 18:ds=51 fs=19 fl=1 hz=0.0213903743315508, 24:ds=47 fs=39 fl=0 hz=0.04118268215417107, 31:ds=45 fs=27 fl=1 hz=0.029473684210526315, 13:ds=44 fs=30 fl=0 hz=0.0320855614973262

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=90 flags=purple
- S19: ds=76 flags=red+purple
- S20: ds=64 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 056: score=3 tags=FLT,RS
  - 146: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 569: score=3 tags=FLT,RS
  - 029: score=2 tags=RS
  - 038: score=2 tags=RS
  - 047: score=2 tags=RS
  - 128: score=2 tags=RS
  - 137: score=2 tags=RS
  - 245: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=8 last_repeat_index=15

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=51), P2:0 (gap=16), P3:5 (gap=30)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=51)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 010: score=50.19091 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 310: score=50.06257428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 080: score=47.16706714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 380: score=46.735155 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 090: score=45.61262428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 060: score=44.852938571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=43.349552857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 390: score=42.21525714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 360: score=41.45557142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 070: score=41.43306714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 389: ds=957 sev=B
- 688: ds=939 sev=B
- 088: ds=877 sev=B
- 888: ds=843 sev=B
- 222: ds=836 sev=B
- 333: ds=805 sev=B
- 133: ds=767 sev=B
- 999: ds=765 sev=B
- 224: ds=759 sev=B
- 889: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=77 sev=blue
  - 55: ds=43 sev=purple
  - 77: ds=40 sev=purple
  - 00: ds=31 sev=purple
  - 99: ds=23 sev=-
  - 11: ds=13 sev=-
  - 44: ds=7 sev=-
  - 88: ds=6 sev=-
  - 66: ds=3 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 06: ds=61 sev=red
  - 48: ds=47 sev=blue
  - 07: ds=46 sev=blue
  - 46: ds=44 sev=blue
  - 37: ds=41 sev=blue
  - 47: ds=40 sev=blue
  - 27: ds=38 sev=blue
  - 19: ds=35 sev=purple
  - 05: ds=32 sev=purple
  - 23: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:483, 16:204, 26:187, 32:172, 3:109, 33:94, 31:81, 10:56, 27:51, 2:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=483 fs=1 fl=1 hz=0.006012024048096192, 16:ds=204 fs=1 fl=2 hz=0.008174386920980927, 26:ds=187 fs=2 fl=2 hz=0.0074962518740629685, 32:ds=172 fs=4 fl=1 hz=0.010273972602739727, 3:ds=109 fs=14 fl=4 hz=0.020270270270270268, 33:ds=94 fs=23 fl=0 hz=0.026136363636363638, 31:ds=81 fs=25 fl=1 hz=0.028602860286028604, 10:ds=56 fs=13 fl=2 hz=0.01733477789815818, 27:ds=51 fs=19 fl=1 hz=0.02305159165751921, 2:ds=48 fs=28 fl=1 hz=0.03049421661409043

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S25: ds=81 flags=purple
- S20: ds=59 flags=purple
- S6: ds=57 flags=purple
- S1: ds=48 flags=blue+purple
- S26: ds=34 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 029: score=3 tags=FLT,RS
  - 038: score=3 tags=FLT,RS
  - 047: score=3 tags=FLT,RS
  - 056: score=3 tags=FLT,RS
  - 128: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 389: score=3 tags=FLT,RS
  - 479: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 146: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 189 -> combined:763(B); evening:667(B)
- 222 -> combined:687(B); evening:836(B)
- 224 -> combined:799(B); evening:759(B)
- 889 -> combined:893(B); evening:726(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:62(purple); evening:31(purple); midday:32(purple)
- 04 -> combined:40(blue); midday:27(purple)
- 06 -> combined:37(blue); evening:61(red)
- 07 -> combined:92(red); evening:46(blue); midday:54(blue)
- 17 -> combined:36(purple); midday:61(red)
- 19 -> combined:49(blue); evening:35(purple)
- 23 -> combined:25(purple); evening:28(purple)
- 37 -> combined:51(blue); evening:41(blue); midday:25(purple)
- 47 -> combined:67(red); evening:40(blue); midday:33(purple)
- 48 -> combined:45(blue); evening:47(blue)
- 69 -> combined:46(blue); midday:86(red)
- 77 -> combined:61(purple); evening:40(purple); midday:30(purple)
- 99 -> combined:46(purple); midday:36(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(8.920857142857143)[R1,XVAR-Cons(CEM)], 0(7.5478000000000005)[R2,XVAR-Cons(CEM)], 7(1.8257)[R3,XVAR-Cons(CE)], 9(0.30153571428571424)[R3,Swap]
- P2: 1(4.519071428571428)[R1,XVAR-Cons(CM)], 8(2.4952285714285716)[R2,XVAR-Cons(CM)], 9(1.9407857142857141)[R3,XVAR-Cons(CE)], 6(1.6810999999999998)[R2,Mirror-Echo], 0(1.1777142857142857)[R1,Double-Pressure]
- P3: 0(8.353614285714286)[R1,XVAR-Cons(CEM)], 5(1.6952142857142856)[R1,Mirror-Echo], 4(1.6896214285714286)[R3,XVAR-Cons(CE)], 8(0.964)[R2,Double-Pressure], 6(0.879)[R2,Double-Pressure]
