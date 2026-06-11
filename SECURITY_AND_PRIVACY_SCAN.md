# Security and Privacy Scan

Status: REVIEW_NEEDED

Scope: curated public package files. The scan checks high-confidence credential patterns, obvious local absolute paths, and directories marked not for sharing.

Curated exclusions: internal working zips, local build logs, temporary directories, private-path source bundles, and files under `reference_after_completion_do_not_share_with_new_auditors`.

Sanitization applied: local model-cache paths in run metadata were replaced with model repository identifiers.

## Findings

| file | pattern | preview |
|---|---|---|
| `PACKAGE_MANIFEST.json` | do_not_share_path | `do_not_share_with_new_auditors` |
