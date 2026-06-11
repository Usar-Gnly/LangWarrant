# SLD-Bench Final Metrics Freeze Package v0.2k

Date: 2026-06-10
Status: `FINAL_METRICS_FREEZE_APPROVED`
Generated at: `2026-06-10T11:47:20.493879+00:00`

## What this package is

This is the final metrics freeze package for SLD-Bench v1.0 Full-1500 model evaluation under the v0.2k B-audit-guided scorer repair.

It is the paper-facing metrics package. Use the files under:

```text
01_FINAL_PAPER_TABLES/
```

for paper result tables.

## What this package is not

This package is not a new human-audit execution package, not a new model-run package, and not a new scorer-development package. It does not modify raw model outputs, dataset rows, compiled rule manifests, or TC/FMT/FLP scores.

## Current decision

`FINAL_METRICS_FREEZE_APPROVED`

The approval is conditional on the provenance statement that v0.2k is a B-audit-guided scorer repair with regression verification, not a blind pure-automatic repair.

## Directory map

| Directory | Use |
|---|---|
| `01_FINAL_PAPER_TABLES/` | Final paper-facing CSV tables |
| `02_FINAL_RUN_METRICS/` | Full v0.2k run-level score files used to derive tables |
| `03_AUDIT_REGRESSION_AND_REPAIR_EVIDENCE/` | B-audit evidence and regression proof |
| `04_DIFFS_AND_PROVENANCE/` | Before/after diffs and high-risk provenance reconciliation |
| `05_QA_AND_SOURCE_REPORTS/` | QA and scorer repair reports copied from source packages |
| `06_SOURCE_PACKAGE_REFERENCES/` | Source package zips and SHA references |

## Paper-use rule

Use official-main tables for main paper results:

```text
01_FINAL_PAPER_TABLES/paper_table_official_main_full1500_item_metrics_v0_2k_FINAL.csv
01_FINAL_PAPER_TABLES/paper_table_official_main_full1500_triad_metrics_v0_2k_FINAL.csv
```

Use diagnostic/sensitivity tables only if explicitly labeled as diagnostic or appendix material.
