# Final Metrics Freeze Decision v0.2k

Decision: `FINAL_METRICS_FREEZE_APPROVED`

Date: 2026-06-10

## Scope

This decision covers final paper-use metrics for SLD-Bench v1.0 Full-1500 model evaluation.

Approved final tables:

1. `01_FINAL_PAPER_TABLES/paper_table_official_main_full1500_item_metrics_v0_2k_FINAL.csv`
2. `01_FINAL_PAPER_TABLES/paper_table_official_main_full1500_triad_metrics_v0_2k_FINAL.csv`
3. `01_FINAL_PAPER_TABLES/paper_table_slices_all_runs_v0_2k_FINAL.csv`, for slice analysis with appropriate official/diagnostic labeling.

## Decision basis

The freeze decision is based on the following checks:

| Check | Result |
|---|---:|
| v0.2k item regression against B-audit | 312/312 |
| v0.2k item regression mismatches | 0 |
| v0.2k triad regression against B-audit | 286/286 |
| v0.2k triad regression mismatches | 0 |
| TC/FMT/FLP changes from v0.2j | 0 |
| raw outputs changed | False |
| dataset changed | False |
| source 02 checksum verification | PASS |
| source 03 checksum verification | PASS |
| final package validation errors | 0 |

## Required paper wording

The paper must describe the final scorer as:

```text
B-audit-guided scorer repair with regression verification
```

The paper must not describe v0.2k as a blind pure-automatic scorer repair with no human-audit information.

## Human audit status

No third bulk human audit is required by default. The completed B-audit is used as the targeted regression suite. Optional sentinel checking may be described only if it is actually executed.

## Boundary

This decision freezes the metrics in this package for paper use. It does not freeze the entire manuscript, qualitative-example selection, or final wording. Any qualitative example newly selected for the paper should either come from already audited rows or receive a separate minimal example-level check.
