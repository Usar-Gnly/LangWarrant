# LangWarrant LW3 Data Analysis Implementation Report

Date: 2026-06-11
Base package: `LangWarrant_LW2_BlockerFix_2026-06-11.zip`
Output package: `LangWarrant_LW3_DataAnalysis_2026-06-11.zip`

## Scope

LW3 adds paper-level data analysis using only the frozen v0.2k scoring outputs and frozen 1,500-row dataset metadata. No model outputs were regenerated and no scoring rules were changed.

## Added analyses

1. Headline uncertainty intervals
   - Added Wilson 95% intervals for item-level LWA over 1,500 items per official-main run.
   - Added Wilson 95% intervals for TWCS over 500 triads per official-main run.

2. Role-level and relation diagnostics
   - Added Base / Warrant-change / Distractor-change LWA by model.
   - Added WSS and DIS relation checks by model.
   - This makes the counterfactual triad structure visible in the main paper rather than only in artifacts.

3. Warrant-source slice analysis
   - Aggregated target-language-source fields into main paper-safe source families.
   - Added LWA, VRS, and TC by source family across the six official-main runs.
   - Kept fine-grained field paths in artifacts to avoid overclaiming small cells.

4. Static shortcut-cue baselines
   - Added metadata-only shortcut baselines: follow operator language, follow source/material language, follow audience language, and always use the majority target language.
   - These baselines use the frozen gold target labels and do not depend on model predictions.

5. Results text update
   - Updated the RQ organization paragraph.
   - Expanded RQ1, RQ2, and RQ3 with the new analyses.
   - Updated the Summary of Findings to include shortcut-baseline evidence.

## Generated analysis files

- `analysis/headline_wilson_ci.csv`
- `analysis/role_counterfactual_diagnostics.csv`
- `analysis/warrant_source_metrics.csv`
- `analysis/shortcut_cue_baselines.csv`
- `analysis/shortcut_tag_metrics.csv`
- `analysis/lw3_compute_analysis_tables.py`

## Compilation and QA

- Compiler chain used in this environment: `pdflatex`, `bibtex8`, `pdflatex`, `pdflatex`.
- Final PDF builds successfully.
- Rendered PDF pages were visually inspected at 120 DPI.
- Known non-blocking warnings: standard IEEEtran camera-ready reminder, balance warning, and font fallback for small caps italic.
- Page count increased from LW2 to 14 pages with references. Final page-budget compression is deferred to LW4.

## Not changed in LW3

- No model reruns.
- No scorer changes.
- No new claims based on unscored Gemini Pro diagnostic outputs.
- No final repository URL, DOI, license, or author-specific AI acknowledgement was filled in.
