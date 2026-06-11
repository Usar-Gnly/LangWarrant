# SLD-Bench v1.0 Full-1500 Frozen Release

Date: 2026-06-09

Active release status: `FULL1500_FREEZE_APPROVED`.

This package is the canonical frozen Full-1500 resource for SLD-Bench v1.0. It consolidates the ten freeze-approved 50-group batches into one release namespace for model evaluation, paper experiments, and reproducibility.

Use the combined dataset file for model evaluation unless a per-batch run is needed:

- `SLD_Bench_v1_0_Full1500_all_1500rows.jsonl`
- `SLD_Bench_v1_0_Full1500_blueprints_500groups.jsonl`
- `SLD_Bench_v1_0_Full1500_manifest.json`

Per-batch canonical packages are provided under `individual_packs/` for provenance and local debugging. The active namespace is v1.0. Construction-line v0.5 names may appear only as source-lineage/provenance references.

## Integrity status

- Rows: 1500
- Groups: 500
- Controlled warrant triads: 500
- Role distribution: {'base': 500, 'distractor_change': 500, 'warrant_change': 500}
- Validation status: `PASS_RELEASE_INTEGRITY_CHECKS`

## Preservation policy

Model-visible task content, target languages, warrant fields, evidence spans, gold sketches, and business facts were preserved. Active identifiers and release metadata were normalized to the formal v1.0 frozen release namespace.
