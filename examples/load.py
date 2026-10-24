"""Print the height ranges of the height-adjustable desks in the dataset (stdlib only)."""
import csv
from pathlib import Path

rows = csv.DictReader(open(Path(__file__).resolve().parent.parent / "omni-office-furniture-specs.csv", encoding="utf-8"))
for r in rows:
    if r["subcategory"] == "Height-Adjustable Desks" and "-" in r["height_mm"]:
        print(f'{r["series"]:<12} {r["model_code"]:<14} height {r["height_mm"]} mm')
