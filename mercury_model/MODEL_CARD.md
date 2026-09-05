# MERCURY model card

## Intended use

Research-oriented classification of English social-media text into inherited
dataset labels: `depression`, `anxiety`, or `stress`.

## Not intended for

Clinical diagnosis, treatment, crisis assessment, individual surveillance,
employment, insurance, policing, or other high-impact decisions.

## Architecture

RoBERTa-Large + seq_bn/Pfeiffer-style adapter + one-layer bidirectional LSTM
(256 hidden units per direction) + 512-unit token attention + dropout 0.5 +
three-class linear head. Maximum input length is 128 subword tokens.

## Training strategy

The deployed architecture follows the RAMHA-compatible inference path. MERCURY
adds training-only probability-teacher distillation, uncertainty weighting,
condition-term masking, and robustness-aware validation selection.

## Verified five-seed DAS results

| Split | RAMHA macro-F1 mean ± SD | MERCURY macro-F1 mean ± SD |
|---|---:|---:|
| Natural test | 0.927380 ± 0.010315 | 0.929981 ± 0.009760 |
| Balanced test | 0.925094 ± 0.008556 | 0.925064 ± 0.009706 |
| Condition-masked test | 0.878510 ± 0.016461 | 0.885669 ± 0.011001 |

Exact paired sign-flip p-values were 0.0625, 0.8750, and 0.0625. These results
do not establish statistical superiority at alpha 0.05.

## Known limitations

The labels are not clinician-verified diagnoses. The source corpus contains
strong topical and diagnostic-term cues, has uncertain provenance, and lacks
author/source identifiers. Performance may not transfer to private messages,
other platforms, dialects, languages, demographics, or clinical settings.
