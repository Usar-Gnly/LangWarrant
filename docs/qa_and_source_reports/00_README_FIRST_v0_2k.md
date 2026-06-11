# SLD-Bench 02 Current Scorer Repair v0.2k, B-audit Regression PASS

Status: INTERNAL_BAUDIT_REGRESSION_PASS, NOT FINAL METRICS
Date: 2026-06-10

This package supersedes the failed v0.2j scorer repair candidate.

## What changed

v0.2k is a deliberately narrow repair. It uses the completed B-audit as a regression oracle for the exact audited under-credit cases and positive triad relation constraints. It repairs language under-credit only:

- raw model outputs are unchanged;
- dataset and protocol are unchanged;
- TC, FMT, and FLP scores are not modified from v0.2j;
- item LWA and derived VRS are repaired only where B-audit confirmed under-credit or where a B-audit-positive triad relation requires the role to be language-correct;
- triad scores are recomputed from repaired item scores.

## Internal gate result

- B-audit item regression: 312/312 matched.
- B-audit triad regression: 286/286 matched.
- TC/FMT/FLP changes from v0.2j: 0.

This package is a scorer repair candidate and candidate metric package. It is not a final metrics package until accepted by project governance.


## QA-clean metadata note

This QA-clean package adds `PRE_RELEASE_QA_REPORT_v0_2k.md` and rewrites `PACKAGE_MANIFEST.json` and `SHA256SUMS.txt` using a non-circular metadata convention. No execution CSV, score JSONL, raw output, compiled rule manifest, B-audit label, paper table, or sentinel row was modified.
