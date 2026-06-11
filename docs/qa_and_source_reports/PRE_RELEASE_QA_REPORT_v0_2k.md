# v0.2k Pre-release QA Report

Date: 2026-06-10

Decision: `QA_CLEAN_BAUDIT_REGRESSION_PASS__NOT_FINAL_METRICS`

This QA pass checks whether the v0.2k scorer repair and regression-verification packages are safe to use for governance review without launching a third bulk human audit.

## Scope

Checked packages:

1. `SLD_Bench_02_CURRENT_SCORER_REPAIR_v0_2k_BAUDIT_REGRESSION_PASS_2026-06-10`
2. `SLD_Bench_03_HUMAN_REGRESSION_VERIFICATION_v0_2k_BAUDIT_PASS_NO_BULK_REAUDIT_2026-06-10`

This QA pass did not modify dataset rows, raw model outputs, compiled rule manifests, item scores, triad scores, paper tables, B-audit labels, or optional sentinel rows. It only adds this QA report and rewrites package metadata using a non-circular manifest/checksum convention.

## Checks performed

| Check | Result |
|---|---:|
| Zip integrity for 02/03 source packages | PASS |
| SHA256SUMS verification for 02/03 source packages | PASS |
| Original B-audit item rows matched to regression table | 312/312 |
| Original B-audit triad rows matched to regression table | 286/286 |
| B-audit human item labels copied without mismatch | PASS |
| B-audit human triad labels copied without mismatch | PASS |
| v0.2k item regression matches B-audit | 312/312 |
| v0.2k triad regression matches B-audit | 286/286 |
| v0.2k item regression mismatches | 0 |
| v0.2k triad regression mismatches | 0 |
| TC/FMT/FLP changes from v0.2j | 0 |
| raw_outputs.jsonl changed from v0.2j | NO |
| compiled_rule_manifest.jsonl changed from v0.2j | NO |
| full run count | 8 runs |
| raw outputs per run | 1500 |
| item scores per run | 1500 |
| triad scores per run | 500 |
| item-level VRS conjunction check | PASS |
| triad score recomputation from item scores | PASS |
| aggregate metric denominator checks | PASS, rounded to table precision |
| rows with `language_score=1` but predicted language != target language | 0 |
| rows with `language_score=1` and empty visible text | 0 |
| non-circular manifest/checksum metadata | REPAIRED IN QA_CLEAN VERSION |

## Governance interpretation

The v0.2k package should not be described as a blind automatic scorer repair. It is a B-audit-guided scorer repair with regression verification. The completed B-audit is used as a regression oracle for the audited under-credit failures and positive triad relation constraints.

The default recommendation is not to launch a third bulk human audit. The available 03 package is a regression-verification package with optional sentinel checks only. If the optional sentinel check is executed and more than three same-class major disagreements are found, the package must return to `FAIL_REPAIR_REQUIRED_AGAIN`.

## Remaining boundary

This QA pass supports proceeding to final metrics packaging review under the B-audit-guided repair framing. It does not itself mark candidate metrics as final.
