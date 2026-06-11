# Reproducibility Guide

## Verify package checksums

```bash
python scripts/verify_checksums.py --repo-root .
```

## Recompute LW3 analysis tables

```bash
python -m pip install pandas
python scripts/compute_lw3_analysis_tables.py --repo-root .
```

The recomputed tables are written to `results/lw3_analysis_recomputed/` and can be compared against `results/lw3_analysis/`.

## Scored runs

Per-run raw outputs and scored artifacts are in `results/scored_runs/`. The official-main runs are:

- `openai_gpt55_main_v1`
- `google_gemini35flash_main_v1`
- `anthropic_sonnet46_main_v1`
- `qwen3_8b_main_v1`
- `aya_expanse_8b_main_v1`
- `llama31_8b_main_v1`

Diagnostic/sensitivity runs are also included where available.
