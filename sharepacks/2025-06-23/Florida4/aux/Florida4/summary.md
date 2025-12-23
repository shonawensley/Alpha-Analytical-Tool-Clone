# Aux Summary — Florida4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2025-06-23/Florida4/aux/draws/Florida_draws.csv` n=1000 head=924, 330, 120, 927, 241
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2025-06-23/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=330, 927, 433, 255, 501
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2025-06-23/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=924, 120, 241, 262, 529

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=2 last_repeat_gap=36 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=41), P2:1 (gap=24), P3:8 (gap=16)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 018: score=45.94415214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 088: score=42.501913571428574 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 016: score=40.07550642857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 098: score=39.95724285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 019: score=39.10140714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 718: score=38.79152857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 068: score=37.64098571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 008: score=36.05551428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 788: score=35.66784285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 798: score=35.6669 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 499: ds=970 sev=B
- 009: ds=919 sev=B
- 889: ds=897 sev=B
- 337: ds=871 sev=B
- 277: ds=844 sev=B
- 224: ds=803 sev=B
- 288: ds=784 sev=B
- 189: ds=767 sev=B
- 455: ds=758 sev=B
- 137: ds=756 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=66 sev=purple
  - 77: ds=65 sev=purple
  - 99: ds=50 sev=purple
  - 11: ds=21 sev=-
  - 88: ds=16 sev=-
  - 44: ds=15 sev=-
  - 66: ds=10 sev=-
  - 55: ds=7 sev=-
  - 22: ds=6 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 07: ds=96 sev=red
  - 47: ds=71 sev=red
  - 37: ds=55 sev=blue
  - 19: ds=53 sev=blue
  - 69: ds=50 sev=blue
  - 48: ds=49 sev=blue
  - 04: ds=44 sev=blue
  - 06: ds=41 sev=blue
  - 17: ds=40 sev=blue
  - 09: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:279, 19:94, 16:91, 32:81, 1:68, 11:60, 34:57, 9:53, 17:40, 5:39

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=279 fs=2 fl=0 hz=0.004552352048558422, 19:ds=94 fs=23 fl=1 hz=0.02724177071509648, 16:ds=91 fs=0 fl=2 hz=0.004761904761904762, 32:ds=81 fs=1 fl=1 hz=0.005797101449275362, 1:ds=68 fs=5 fl=2 hz=0.012302284710017574, 11:ds=60 fs=54 fl=0 hz=0.05787781350482315, 34:ds=57 fs=15 fl=2 hz=0.021683673469387755, 9:ds=53 fs=39 fl=1 hz=0.044543429844097995, 17:ds=40 fs=17 fl=2 hz=0.021231422505307854, 5:ds=39 fs=24 fl=2 hz=0.027689030883919063

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S20: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=72 flags=blue+purple
- S5: ds=60 flags=purple
- S11: ds=58 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=4 tags=FLT,MIR,RS
  - 056: score=4 tags=FLT,MIR,RS
  - 146: score=4 tags=FLT,MIR,RS
  - 389: score=4 tags=FLT,MIR,RS
  - 128: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 245: score=3 tags=FLT,RS
  - 479: score=3 tags=MIR,RS
  - 569: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=17 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=20), P2:1 (gap=53), P3:6 (gap=12)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=53)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 018: score=45.94415214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 088: score=42.501913571428574 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 016: score=40.07550642857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 098: score=39.95724285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 019: score=39.10140714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 718: score=38.79152857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 068: score=37.64098571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 008: score=36.05551428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 788: score=35.66784285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 798: score=35.6669 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=958 sev=B
- 555: ds=956 sev=B
- 066: ds=915 sev=B
- 011: ds=903 sev=B
- 003: ds=901 sev=B
- 266: ds=854 sev=B
- 008: ds=835 sev=B
- 557: ds=791 sev=B
- 122: ds=768 sev=B
- 126: ds=756 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=116 sev=red
  - 22: ds=106 sev=blue
  - 66: ds=81 sev=blue
  - 99: ds=38 sev=purple
  - 00: ds=34 sev=purple
  - 77: ds=32 sev=purple
  - 11: ds=10 sev=-
  - 44: ds=7 sev=-
  - 55: ds=3 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 18: ds=94 sev=red
  - 69: ds=88 sev=red
  - 17: ds=63 sev=red
  - 07: ds=56 sev=red
  - 12: ds=55 sev=blue
  - 16: ds=45 sev=blue
  - 14: ds=42 sev=blue
  - 24: ds=35 sev=purple
  - 47: ds=35 sev=purple
  - 04: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 19:231, 1:180, 26:139, 17:109, 20:79, 22:58, 18:53, 24:49, 31:47, 16:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 19:ds=231 fs=11 fl=1 hz=0.018691588785046728, 1:ds=180 fs=4 fl=1 hz=0.009022556390977444, 26:ds=139 fs=4 fl=0 hz=0.008207934336525308, 17:ds=109 fs=19 fl=0 hz=0.02288329519450801, 20:ds=79 fs=21 fl=1 hz=0.024858757062146894, 22:ds=58 fs=38 fl=1 hz=0.043237250554323724, 18:ds=53 fs=19 fl=1 hz=0.0213903743315508, 24:ds=49 fs=39 fl=0 hz=0.04118268215417107, 31:ds=47 fs=27 fl=1 hz=0.029473684210526315, 16:ds=45 fs=0 fl=1 hz=0.00410958904109589

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=92 flags=purple
- S19: ds=78 flags=red+purple
- S20: ds=66 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=3 tags=FLT,RS
  - 056: score=3 tags=FLT,RS
  - 128: score=3 tags=FLT,RS
  - 146: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 389: score=3 tags=FLT,RS
  - 569: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 029: score=2 tags=RS
  - 047: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=2 last_repeat_gap=10 last_repeat_index=15

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=53), P2:0 (gap=18), P3:5 (gap=32)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=53)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 018: score=45.94415214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 088: score=42.501913571428574 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 016: score=40.07550642857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 098: score=39.95724285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 019: score=39.10140714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 718: score=38.79152857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 068: score=37.64098571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 008: score=36.05551428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 788: score=35.66784285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 798: score=35.6669 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 389: ds=959 sev=B
- 688: ds=941 sev=B
- 088: ds=879 sev=B
- 888: ds=845 sev=B
- 222: ds=838 sev=B
- 333: ds=807 sev=B
- 133: ds=769 sev=B
- 999: ds=767 sev=B
- 224: ds=761 sev=B
- 889: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=79 sev=blue
  - 55: ds=45 sev=purple
  - 77: ds=42 sev=purple
  - 00: ds=33 sev=purple
  - 99: ds=25 sev=purple
  - 11: ds=15 sev=-
  - 44: ds=9 sev=-
  - 88: ds=8 sev=-
  - 66: ds=5 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 06: ds=63 sev=red
  - 48: ds=49 sev=blue
  - 07: ds=48 sev=blue
  - 46: ds=46 sev=blue
  - 37: ds=43 sev=blue
  - 47: ds=42 sev=blue
  - 27: ds=40 sev=blue
  - 19: ds=37 sev=blue
  - 05: ds=34 sev=purple
  - 23: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:485, 16:206, 26:189, 32:174, 3:111, 33:96, 10:58, 27:53, 2:50, 19:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=485 fs=1 fl=1 hz=0.006012024048096192, 16:ds=206 fs=1 fl=2 hz=0.008174386920980927, 26:ds=189 fs=2 fl=2 hz=0.0074962518740629685, 32:ds=174 fs=4 fl=1 hz=0.010273972602739727, 3:ds=111 fs=14 fl=4 hz=0.020270270270270268, 33:ds=96 fs=23 fl=0 hz=0.026136363636363638, 10:ds=58 fs=13 fl=2 hz=0.01733477789815818, 27:ds=53 fs=19 fl=1 hz=0.02305159165751921, 2:ds=50 fs=27 fl=1 hz=0.029787234042553193, 19:ds=47 fs=25 fl=2 hz=0.029315960912052113

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S22: ds=87 flags=purple
- S25: ds=83 flags=purple
- S20: ds=61 flags=purple
- S6: ds=59 flags=purple
- S1: ds=50 flags=blue+purple
- S26: ds=36 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=4 tags=FLT,MIR,RS
  - 389: score=4 tags=FLT,MIR,RS
  - 479: score=4 tags=FLT,MIR,RS
  - 047: score=3 tags=FLT,RS
  - 056: score=3 tags=MIR,RS
  - 128: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 146: score=3 tags=MIR,RS
  - 236: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 189 -> combined:767(B); evening:669(B)
- 222 -> combined:691(B); evening:838(B)
- 224 -> combined:803(B); evening:761(B)
- 889 -> combined:897(B); evening:728(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:66(purple); evening:33(purple); midday:34(purple)
- 04 -> combined:44(blue); midday:29(purple)
- 06 -> combined:41(blue); evening:63(red)
- 07 -> combined:96(red); evening:48(blue); midday:56(red)
- 17 -> combined:40(blue); midday:63(red)
- 19 -> combined:53(blue); evening:37(blue); midday:26(purple)
- 23 -> combined:29(purple); evening:30(purple)
- 37 -> combined:55(blue); evening:43(blue); midday:27(purple)
- 47 -> combined:71(red); evening:42(blue); midday:35(purple)
- 48 -> combined:49(blue); evening:49(blue)
- 67 -> combined:28(purple); midday:27(purple)
- 69 -> combined:50(blue); evening:25(purple); midday:88(red)
- 77 -> combined:65(purple); evening:42(purple); midday:32(purple)
- 99 -> combined:50(purple); evening:25(purple); midday:38(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.140542857142858)[R1,XVAR-Cons(CEM)], 7(4.8502)[R2,XVAR-Cons(CEM)], 3(1.7149999999999999)[R1,Double-Pressure], 1(0.9089999999999999)[R2,Double-Pressure], 8(0.28385714285714286)[R3,Swap]
- P2: 1(4.763785714285714)[R1,XVAR-Cons(CM)], 8(2.6401)[R2,XVAR-Cons(CM)], 9(2.639157142857143)[R3,XVAR-Cons(CE)], 6(1.8228999999999997)[R2,Mirror-Echo], 0(1.2374285714285713)[R1,Double-Pressure]
- P3: 8(6.177542857142857)[R1,XVAR-Cons(CEM)], 6(3.248285714285714)[R2,XVAR-Cons(CM)], 9(2.401242857142857)[R3,XVAR-Cons(CM)], 5(1.5554285714285714)[R1,Double-Pressure], 7(0.09405000000000001)[R3]
