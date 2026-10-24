# Omni office furniture specifications (open dataset)

Model codes and dimensions for the 37 series in the **Omni Design Collection**, the product catalog of Jiangsu Omni Industrial Co., Ltd. (Yangzhou, China, est. 2004).

- Catalog: [omnidesign.site](https://omnidesign.site/)
- Official website: [omnidesking.com](https://www.omnidesking.com/)
- Version: 1.0.0 (2026-10-23)
- License: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

## Files

| File | Contents |
|---|---|
| `omni-office-furniture-specs.csv` | 151 rows: 150 model entries plus 1 series (SELLA PRO) with no published model code |
| `omni-office-furniture-specs.json` | The same rows, with metadata (version, license, citation, field list) |
| `examples/load.py` | Loads the CSV and prints the height-adjustable desk ranges (Python standard library only) |

Coverage: 37 series. Desks and Workstations 53 rows, Tables 9, Seating 22, Accessories 67. 149 unique model codes; `MDP-01` appears under both ARCH and FILE PEDESTAL, as in the printed catalog. 84 rows have width, depth and height; 4 have a diameter; 61 rows (mostly power modules and monitor arms) have a model code but no dimensions published.

## Fields

| Field | Type | Description |
|---|---|---|
| `series` | text | Series name as printed (e.g. `HA`, `X-RAIL`, `SELLA`) |
| `series_slug` | text | URL slug of the series |
| `category` | text | Desks and Workstations / Tables / Seating / Accessories |
| `subcategory` | text | e.g. Panel Systems, Benching, Height-Adjustable Desks, Power Access |
| `model_code` | text | Manufacturer model code |
| `width_mm`, `depth_mm`, `height_mm` | text | Millimetres. `560-1210` = adjustable range; `1200-1500` = available sizes; `711/1041` = alternative sizes. Empty = not published |
| `diameter_mm` | text | Round tables and bases. Same conventions |
| `materials_keywords` | text | Material words found in the series' published feature text and the model note (e.g. `steel; oak; mesh`). Keyword extraction, not a bill of materials |
| `model_note` | text | Note shown on the series page (e.g. base and arm options, "dimensions to be confirmed on quotation") |
| `series_specs` | text | Series-level specification rows shown on the page (height range, load capacity, VESA, electrical rating), `key: value; …` |
| `page_url` | URL | Series page on omnidesign.site |

## Caveats

- Dimensions are as printed in the Omni Design Collection catalog (lookbook). Rows whose note says "to be confirmed on quotation" should be treated as provisional.
- This is catalog data, not test data. Load ratings and certifications apply only to the model named in `series_specs`.
- No prices, MOQs, lead times or warranty terms are included.
- Finishes, colours and configurations vary. Confirm current specifications with Omni before ordering or specifying.

## How to cite

```text
Omni Design Collection (2026). Omni office furniture specifications (Version 1.0.0) [Data set].
Jiangsu Omni Industrial Co., Ltd. https://omnidesign.site/data/
```

`CITATION.cff` carries the same reference for GitHub's "Cite this repository" button.

Attribution line for reuse under CC BY 4.0: `Data: Omni Design Collection, omnidesign.site (CC BY 4.0)`.

## Contact

weiben.zhang@omnidesking.com · +86 139 0527 3603
