Archived V‑TRAC Reference Copies

Purpose
- Keep unused historical V‑TRAC references out of import resolution, while preserving them for future study.

Candidates to archive (move-only; no deletes)
- modules/module_d_auxiliary_tools/legacy_2/modules/vtrac_reference.py → archived/vtrac_refs/legacy_2_modules_vtrac_reference.py
- modules/module_d_auxiliary_tools/core_legacy/legacy_modules_backup/vtrac_reference.py → archived/vtrac_refs/core_legacy_backup_vtrac_reference.py

Live locations (do not archive)
- scripts/auxiliary/working/modules/vtrac_reference.py   (staged, Aux page only)
- modules/vtrac_reference.py                              (canonical API for non‑Aux pages)

Process (safe)
1) Verify integrated app and Aux page behavior.
2) Move the candidate files listed above to this folder.
3) App boot + Winners Full + Aux smoke again.
4) If needed, retain a re‑export shim in the original location for legacy scripts (not used by the integrated app).

