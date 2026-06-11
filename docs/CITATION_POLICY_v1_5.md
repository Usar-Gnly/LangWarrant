# LangWarrant citation policy preview

This package uses BibTeX with IEEEtran ordering. The paper-facing source is `main.tex`, and all external references are managed in `references.bib`.

## Policy

1. Prefer official venue BibTeX for recent ACL, NAACL, EMNLP, NeurIPS, ICML, AAAI, VLDB, SIGMOD, and ICDE references.
2. Use arXiv metadata only when no official proceedings entry exists.
3. Keep benchmark-positioning citations in the surrounding prose rather than overloading compact tables.
4. Do not introduce uncited bibliography entries into the final submission source unless they support an explicit paper claim.
5. When official metadata appears malformed, normalize author names only when the paper PDF or another official source clearly supports the correction.

## LW1 notes

- M-IFEval, MaXIFE, and Marco-Bench-MIF were checked against ACL Anthology metadata.
- RAGDrift was checked against AAAI 2026 metadata.
- MaXIFE's malformed legacy author string was normalized to `Chang, Jing`.
