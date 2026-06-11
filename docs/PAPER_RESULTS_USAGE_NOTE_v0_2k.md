# Paper Results Usage Note v0.2k

Use these as main paper result tables:

```text
01_FINAL_PAPER_TABLES/paper_table_official_main_full1500_item_metrics_v0_2k_FINAL.csv
01_FINAL_PAPER_TABLES/paper_table_official_main_full1500_triad_metrics_v0_2k_FINAL.csv
```

Diagnostic or sensitivity tables must not be mixed into the main official model comparison unless explicitly labeled.

Recommended wording for methods/results provenance:

```text
After the initial automatic scoring pass, a targeted human audit identified systematic under-crediting caused by visible-region extraction and language-detection failures. We rejected the affected candidate metrics, repaired the scorer under a narrow B-audit-guided scope, and verified the repaired scorer against the completed audit as a regression suite. The final reported metrics are computed from immutable raw model outputs using the v0.2k scorer, with the audit-guided repair and regression evidence released as provenance artifacts.
```

Do not write that the final metrics come from a blind pure-automatic scorer with no human-audit input.
