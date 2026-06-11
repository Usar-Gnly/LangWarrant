# LangWarrant

LangWarrant is a controlled benchmark for evaluating response-language authorization in multilingual workflow prompts. The benchmark contains 1,500 instances organized into 500 warrant triads. Each triad tests whether a model follows the workflow evidence item that authorizes the response language rather than a salient but non-authoritative language cue.

This repository is the public-safe artifact package for the ICDE EAB-style benchmark paper:

> LangWarrant: Evaluating Response-Language Authorization in Multilingual Workflow Prompts

## Repository layout

```text
data/
  frozen_release/        Frozen 1,500-instance benchmark release
  inventory/             Dataset and run inventory tables
results/
  final_paper_tables/    Frozen paper metric tables
  scored_runs/           Raw outputs, item scores, triad scores, and scorer manifests
  lw3_analysis/          Additional analysis tables used in the LW3/LW4 paper revisions
scripts/
  compute_lw3_analysis_tables.py
  verify_checksums.py
paper/
  LW4 paper source/PDF snapshot and figures
docs/
  dataset card, reproducibility guide, model metadata, AI/human-audit note, and freeze reports
```

## Quick checks

Verify checksums:

```bash
python scripts/verify_checksums.py --repo-root .
```

Recompute LW3 analysis tables:

```bash
python -m pip install pandas
python scripts/compute_lw3_analysis_tables.py --repo-root .
```

## Naming note

`LangWarrant` is the paper-facing benchmark name. Frozen item identifiers preserve the legacy `SLD_v1_0` prefix to maintain checksum and provenance compatibility.

## AI assistance and human audit

Generative AI tools assisted figure prototyping, language editing, grammar refinement, dataset-instance drafting, and code drafting. The released instances, code, figures, analyses, and paper text were reviewed, revised, and audited by the authors. See `docs/AI_ASSISTANCE_AND_HUMAN_AUDIT_NOTE.md`.

## Privacy and safety

This public package was curated rather than copied wholesale from internal working bundles. It excludes local logs, temporary build directories, private-path source bundles, and internal files marked as not for sharing with new auditors. Local model-cache paths in public run metadata have been sanitized to model repository identifiers. See `SECURITY_AND_PRIVACY_SCAN.md`.

## License

Code is released under Apache-2.0. Dataset files, benchmark metadata, and analysis tables are released under CC BY 4.0 unless a file states otherwise.
