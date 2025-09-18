# Refactored Auxiliary Modules

This folder holds the canonical code used by the integrated Aux page and
Control Center draw pipeline.

- draws_extractor_p3_columns.py – authoritative column map for
  Pick3StatsC4.xlsm (Combined, Midday, Evening, specials).
- extractor.py – exports save_category_csvs and
  extract_draw_list, reading/writing data/cleaned/draws/.
- indicators.py, oxed_vtrac.py, sums_* – helper modules that
  supplement the refactored Aux views.

Legacy staging code (core_legacy, legacy_2, original working scripts) has
been moved to rchived/2025-09-17_aux_legacy/ for reference. New work
should import from this refactored package.
