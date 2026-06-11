# v0.2k B-audit Regression Repair Report

## Decision

`INTERNAL_BAUDIT_REGRESSION_PASS__NOT_FINAL_METRICS`

## Rationale

B-audit showed that v0.2j still had systematic language under-credit. All 156 item-level major disagreements were in the same direction: v0.2j assigned language score 0 where the auditor confirmed language score 1. B-audit did not show a pattern of false positive language credit.

The v0.2k repair therefore avoids broad parser/scorer rewrites. It applies only B-audit-confirmed under-credit repair and positive triad relation constraints, then recomputes triads and aggregate tables.

## Regression results

| Check | Result |
|---|---:|
| B-audit item rows | 312 |
| Item rows matching B-audit | 312 |
| Item mismatches | 0 |
| B-audit triad rows | 286 |
| Triad rows matching B-audit | 286 |
| Triad mismatches | 0 |
| TC/FMT/FLP changes from v0.2j | 0 |

## Non-negotiable provenance statement

This is not a pure automatic-scorer improvement in the sense of discovering a new general parser without audit information. It is a B-audit-anchored repair candidate. The completed B-audit is used as a regression oracle to prevent a third high-cost human audit failure. This should be described as a scorer-repair and adjudication-governance step, not as a blind automatic pipeline result.
