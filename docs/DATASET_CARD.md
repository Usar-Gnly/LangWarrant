# LangWarrant Dataset Card

## Dataset

LangWarrant is a controlled benchmark for response-language authorization in multilingual workflow prompts. The public release contains 1,500 instances organized into 500 warrant triads.

## Task

Each instance presents a model-visible workflow input. The target response language is determined by a selected language warrant, a model-visible evidence field that authorizes the output language for the current workflow task.

## Triad design

Each group contains a base item, a warrant-shift item, and a distractor-shift item. The warrant shift changes the authorized response language. The distractor shift changes non-authoritative language cues while preserving the authorized response language.

## Privacy and provenance

The records are constructed benchmark instances, not real customer records. Frozen item identifiers preserve the legacy `SLD_v1_0` prefix for checksum and provenance compatibility.

## License

Dataset files and analysis tables are released under CC BY 4.0 unless a file states otherwise. Code is released under Apache-2.0.
