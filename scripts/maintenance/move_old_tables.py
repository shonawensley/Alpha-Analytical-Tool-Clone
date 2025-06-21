"""
Move legacy YYYY-MM-DD folders from data/outputs/tables/
into   data/outputs/tables/archive/<same-folder>
Keeps history but removes clutter from the active path.
Run once from repo root:  python -m scripts.maintenance.move_old_tables
"""
import re
import shutil
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
TABLE_DIR = ROOT / "data" / "outputs" / "tables"
ARCHIVE_DIR = TABLE_DIR / "archive"
ARCHIVE_DIR.mkdir(exist_ok=True)

DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

for item in TABLE_DIR.iterdir():
    if item.is_dir() and DATE_RE.fullmatch(item.name):
        shutil.move(str(item), ARCHIVE_DIR / item.name)
        print(f"moved {item.name}  → archive/")

print("✓  legacy folders archived") 