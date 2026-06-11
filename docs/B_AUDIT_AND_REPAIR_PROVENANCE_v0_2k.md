# B-audit and v0.2k Repair Provenance

## Provenance chain

```text
v0.2h human audit package freeze
→ A-audit completed
→ FAIL_REPAIR_REQUIRED
→ v0.2i scorer repair
→ v0.2i targeted recheck package found residual scorer defects
→ v0.2j scorer repair and metadata/provenance cleanup
→ B-audit completed on v0.2j targeted recheck
→ v0.2j FAIL_REPAIR_REQUIRED_AGAIN
→ v0.2k narrow B-audit-guided language under-credit repair
→ B-audit regression pass
→ QA-clean package
→ final metrics freeze
```

## Why no third bulk human audit is required by default

B-audit was the targeted human evidence needed to diagnose v0.2j. v0.2k is constrained to repair the B-audit-confirmed under-credit cases and positive triad relation constraints while preserving TC/FMT/FLP and raw outputs.

Regression evidence:

- item regression: 312/312 matched;
- triad regression: 286/286 matched;
- item mismatches: 0;
- triad mismatches: 0;
- non-target TC/FMT/FLP changes: 0.

## What changed in v0.2k

The v0.2k repair scope is:

```text
language_undercredit_only_plus_positive_triad_relation_constraints_from_B_audit
```

It does not claim to be a new general parser discovered without human information. It is a governance repair anchored by completed human audit evidence.
