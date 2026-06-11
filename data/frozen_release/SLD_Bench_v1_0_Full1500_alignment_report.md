# SLD-Bench v1.0 Full-1500 Release Alignment Report

Date: 2026-06-09

## Decision

The formal frozen release is now named `SLD_Bench_v1_0_Full1500_FrozenRelease`. The earlier `v0_5` namespace is treated as a construction-line provenance namespace, not the active release namespace.

## Files regenerated

- `SLD_Bench_v1_0_Full1500_FrozenRelease_2026-06-09.zip`
- `SLD_Bench_v1_0_Full1500_BatchArchive_2026-06-09.zip`
- `SLD_Bench_v1_0_Full1500_manifest_2026-06-09.json`
- `SLD_Bench_v1_0_Full1500_alignment_report_2026-06-09.md`

## Active changes

1. Renamed the root release package from the v0.5 namespace to the v1.0 namespace.
2. Renamed active combined files, batch files, manifests, validation reports, and individual batch packs to `SLD_Bench_v1_0_Full1500_*`.
3. Normalized active `item_id` and `group_id` prefixes from `SLD_v0_5_*` to `SLD_v1_0_*`.
4. Regenerated active README files, generation manifests, release manifest, validation reports, and checksum files.
5. Preserved construction-line source names under source-lineage metadata and `provenance_superseded_source_notes/`.

## Content preservation boundary

The following fields were not semantically rewritten: model-visible task input, target response language, selected warrant field, warrant evidence spans, anti-warrant spans, distractor cues, gold response sketch, business facts, workflow family, level, structured-output policy, and format rule.

## Integrity checks

- Rows: 1500 / expected 1,500
- Groups: 500 / expected 500
- Blueprints: 500 / expected 500
- Role distribution: {'base': 500, 'distractor_change': 500, 'warrant_change': 500}
- Duplicate item IDs: 0
- Bad triad groups: 0
- Validation status: `PASS_RELEASE_INTEGRITY_CHECKS`

## Release policy

Use `SLD_Bench_v1_0_Full1500_FrozenRelease_2026-06-09.zip` as the only primary resource for model evaluation and paper experiments. Use `SLD_Bench_v1_0_Full1500_BatchArchive_2026-06-09.zip` only for per-batch provenance and localized debugging.
