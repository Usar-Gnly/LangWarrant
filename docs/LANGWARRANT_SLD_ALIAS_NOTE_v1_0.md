# LangWarrant and Legacy SLD Alias Note v1.0

`LangWarrant` is the paper-facing benchmark name used in the manuscript.

The frozen dataset, item identifiers, group identifiers, and some package filenames retain the legacy internal prefix `SLD_v1_0` or `SLD_Bench`. This is intentional. These identifiers were frozen before the paper-facing rename and are preserved to keep checksums, manifests, audit records, raw-output inventories, and scorer provenance stable.

Recommended wording for the paper and repository:

> LangWarrant is the paper-facing benchmark name. Frozen item identifiers and selected artifact filenames retain the legacy internal prefix `SLD_v1_0` to preserve release hashes and provenance links. The alias is documented in the release manifest rather than rewriting scored identifiers after metric freeze.

Do not rename frozen item IDs unless all hashes, manifests, scorer outputs, audit records, and run inventories are regenerated and revalidated.
