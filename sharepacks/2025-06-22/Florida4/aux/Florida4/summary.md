# Aux Summary — Florida4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2025-06-22/Florida4/aux/draws/Florida_draws.csv` n=1000 head=120, 927, 241, 433, 262
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2025-06-22/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=927, 433, 255, 501, 572
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2025-06-22/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=120, 241, 262, 529, 666

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=34 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=61), P2:1 (gap=22), P3:8 (gap=14)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=61)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 314: score=40.745644285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 318: score=40.21762178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 316: score=39.96346357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 014: score=39.18036285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 394: score=37.32896857142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 384: score=37.320565357142854 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 398: score=36.80094607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 388: score=36.792542857142855 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 396: score=36.54678785714285 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 386: score=36.53838464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 499: ds=968 sev=B
- 009: ds=917 sev=B
- 889: ds=895 sev=B
- 337: ds=869 sev=B
- 277: ds=842 sev=B
- 224: ds=801 sev=B
- 288: ds=782 sev=B
- 189: ds=765 sev=B
- 455: ds=756 sev=B
- 137: ds=754 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=64 sev=purple
  - 77: ds=63 sev=purple
  - 99: ds=48 sev=purple
  - 11: ds=19 sev=-
  - 88: ds=14 sev=-
  - 44: ds=13 sev=-
  - 66: ds=8 sev=-
  - 55: ds=5 sev=-
  - 22: ds=4 sev=-
  - 33: ds=3 sev=-
- non_repeating:
  - 07: ds=94 sev=red
  - 47: ds=69 sev=red
  - 37: ds=53 sev=blue
  - 19: ds=51 sev=blue
  - 69: ds=48 sev=blue
  - 48: ds=47 sev=blue
  - 04: ds=42 sev=blue
  - 06: ds=39 sev=blue
  - 17: ds=38 sev=blue
  - 03: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:277, 31:93, 19:92, 16:89, 32:79, 1:66, 11:58, 34:55, 9:51, 17:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=277 fs=2 fl=0 hz=0.004552352048558422, 31:ds=93 fs=24 fl=1 hz=0.029481132075471695, 19:ds=92 fs=23 fl=1 hz=0.02724177071509648, 16:ds=89 fs=0 fl=2 hz=0.004761904761904762, 32:ds=79 fs=1 fl=1 hz=0.005797101449275362, 1:ds=66 fs=5 fl=2 hz=0.012302284710017574, 11:ds=58 fs=54 fl=0 hz=0.05787781350482315, 34:ds=55 fs=15 fl=2 hz=0.021683673469387755, 9:ds=51 fs=39 fl=1 hz=0.044543429844097995, 17:ds=38 fs=17 fl=2 hz=0.021231422505307854

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S20: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=98 flags=blue+purple
- S26: ds=70 flags=blue+purple
- S5: ds=58 flags=purple
- S11: ds=56 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=3 tags=FLT,RS
  - 056: score=3 tags=FLT,RS
  - 128: score=3 tags=FLT,RS
  - 245: score=3 tags=FLT,RS
  - 389: score=3 tags=FLT,RS
  - 569: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 029: score=2 tags=RS
  - 047: score=2 tags=RS
  - 137: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=16 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=30), P2:1 (gap=52), P3:0 (gap=18)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=52)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 314: score=40.745644285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 318: score=40.21762178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 316: score=39.96346357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 014: score=39.18036285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 394: score=37.32896857142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 384: score=37.320565357142854 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 398: score=36.80094607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 388: score=36.792542857142855 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 396: score=36.54678785714285 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 386: score=36.53838464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=957 sev=B
- 555: ds=955 sev=B
- 066: ds=914 sev=B
- 011: ds=902 sev=B
- 003: ds=900 sev=B
- 266: ds=853 sev=B
- 008: ds=834 sev=B
- 557: ds=790 sev=B
- 122: ds=767 sev=B
- 126: ds=755 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=115 sev=red
  - 22: ds=105 sev=blue
  - 66: ds=80 sev=blue
  - 99: ds=37 sev=purple
  - 00: ds=33 sev=purple
  - 77: ds=31 sev=purple
  - 11: ds=9 sev=-
  - 44: ds=6 sev=-
  - 55: ds=2 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 18: ds=93 sev=red
  - 69: ds=87 sev=red
  - 17: ds=62 sev=red
  - 07: ds=55 sev=blue
  - 12: ds=54 sev=blue
  - 16: ds=44 sev=blue
  - 14: ds=41 sev=blue
  - 24: ds=34 sev=purple
  - 47: ds=34 sev=purple
  - 04: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 19:230, 1:179, 26:138, 17:108, 20:78, 22:57, 18:52, 24:48, 31:46, 13:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 19:ds=230 fs=11 fl=1 hz=0.018691588785046728, 1:ds=179 fs=4 fl=1 hz=0.009022556390977444, 26:ds=138 fs=4 fl=0 hz=0.008207934336525308, 17:ds=108 fs=19 fl=0 hz=0.02288329519450801, 20:ds=78 fs=21 fl=1 hz=0.024858757062146894, 22:ds=57 fs=38 fl=1 hz=0.043237250554323724, 18:ds=52 fs=19 fl=1 hz=0.0213903743315508, 24:ds=48 fs=39 fl=0 hz=0.04118268215417107, 31:ds=46 fs=27 fl=1 hz=0.029473684210526315, 13:ds=45 fs=30 fl=0 hz=0.0320855614973262

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=91 flags=purple
- S19: ds=77 flags=red+purple
- S20: ds=65 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=4 tags=FLT,MIR,RS
  - 056: score=4 tags=FLT,MIR,RS
  - 146: score=4 tags=FLT,MIR,RS
  - 389: score=4 tags=FLT,MIR,RS
  - 128: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 479: score=3 tags=MIR,RS
  - 569: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 016: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=9 last_repeat_index=15

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=52), P2:0 (gap=17), P3:5 (gap=31)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=52)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 314: score=40.745644285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 318: score=40.21762178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 316: score=39.96346357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 014: score=39.18036285714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 394: score=37.32896857142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 384: score=37.320565357142854 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 398: score=36.80094607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 388: score=36.792542857142855 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 396: score=36.54678785714285 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 386: score=36.53838464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 389: ds=958 sev=B
- 688: ds=940 sev=B
- 088: ds=878 sev=B
- 888: ds=844 sev=B
- 222: ds=837 sev=B
- 333: ds=806 sev=B
- 133: ds=768 sev=B
- 999: ds=766 sev=B
- 224: ds=760 sev=B
- 889: ds=727 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=78 sev=blue
  - 55: ds=44 sev=purple
  - 77: ds=41 sev=purple
  - 00: ds=32 sev=purple
  - 99: ds=24 sev=-
  - 11: ds=14 sev=-
  - 44: ds=8 sev=-
  - 88: ds=7 sev=-
  - 66: ds=4 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 06: ds=62 sev=red
  - 48: ds=48 sev=blue
  - 07: ds=47 sev=blue
  - 46: ds=45 sev=blue
  - 37: ds=42 sev=blue
  - 47: ds=41 sev=blue
  - 27: ds=39 sev=blue
  - 19: ds=36 sev=purple
  - 05: ds=33 sev=purple
  - 23: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:484, 16:205, 26:188, 32:173, 3:110, 33:95, 31:82, 10:57, 27:52, 2:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=484 fs=1 fl=1 hz=0.006012024048096192, 16:ds=205 fs=1 fl=2 hz=0.008174386920980927, 26:ds=188 fs=2 fl=2 hz=0.0074962518740629685, 32:ds=173 fs=4 fl=1 hz=0.010273972602739727, 3:ds=110 fs=14 fl=4 hz=0.020270270270270268, 33:ds=95 fs=23 fl=0 hz=0.026136363636363638, 31:ds=82 fs=25 fl=1 hz=0.028602860286028604, 10:ds=57 fs=13 fl=2 hz=0.01733477789815818, 27:ds=52 fs=19 fl=1 hz=0.02305159165751921, 2:ds=49 fs=27 fl=1 hz=0.029787234042553193

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S22: ds=86 flags=purple
- S25: ds=82 flags=purple
- S20: ds=60 flags=purple
- S6: ds=58 flags=purple
- S1: ds=49 flags=blue+purple
- S26: ds=35 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=3 tags=FLT,RS
  - 047: score=3 tags=FLT,RS
  - 128: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 389: score=3 tags=FLT,RS
  - 479: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 029: score=2 tags=RS
  - 056: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 189 -> combined:765(B); evening:668(B)
- 222 -> combined:689(B); evening:837(B)
- 224 -> combined:801(B); evening:760(B)
- 889 -> combined:895(B); evening:727(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:64(purple); evening:32(purple); midday:33(purple)
- 04 -> combined:42(blue); midday:28(purple)
- 06 -> combined:39(blue); evening:62(red)
- 07 -> combined:94(red); evening:47(blue); midday:55(blue)
- 17 -> combined:38(blue); midday:62(red)
- 19 -> combined:51(blue); evening:36(purple); midday:25(purple)
- 23 -> combined:27(purple); evening:29(purple)
- 37 -> combined:53(blue); evening:42(blue); midday:26(purple)
- 47 -> combined:69(red); evening:41(blue); midday:34(purple)
- 48 -> combined:47(blue); evening:48(blue)
- 67 -> combined:26(purple); midday:26(purple)
- 69 -> combined:48(blue); midday:87(red)
- 77 -> combined:63(purple); evening:41(purple); midday:31(purple)
- 99 -> combined:48(purple); midday:37(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(8.950714285714286)[R1,XVAR-Cons(CEM)], 0(7.589599999999999)[R2,XVAR-Cons(CEM)], 7(1.8674214285714286)[R3,XVAR-Cons(CE)], 1(0.22092142857142857)[R3,Swap]
- P2: 1(4.691428571428571)[R1,XVAR-Cons(CM)], 9(2.5899714285714284)[R3,XVAR-Cons(CE)], 8(2.5826642857142854)[R2,XVAR-Cons(CM)], 6(1.8019999999999998)[R2,Mirror-Echo], 0(1.2075714285714285)[R1,Double-Pressure]
- P3: 4(3.0932000000000004)[R2,XVAR-Cons(CE)], 8(2.6340500000000002)[R1,XVAR-Cons(CE)], 6(2.413042857142857)[R3,XVAR-Cons(CM)], 5(1.5255714285714284)[R1,Double-Pressure], 0(1.2374285714285713)[R1,Double-Pressure]
