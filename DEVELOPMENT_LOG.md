# Development log

## 2026-11-12 — correctness and reproducibility

Fixed an undercount when epoch counts are not divisible by four (for example, five epochs inject artifacts at indices 0 and 4). Added complete artifact confusion counts. All-rejected conditions now return null spectral means instead of crashing or inventing a zero value.

Regression cases cover epoch counts 1, 3, 5 and 7, all-rejected conditions, and a detector threshold that misses every injected artifact.

Validation before publication (Python 3.11.0, macOS):

- Full suite: 9 tests passed with `python3 -m unittest discover -s tests -v`.
- `python3 pipeline.py` regenerated the checked-in data, measured results, report and manifest.
- `python3 pipeline.py --verify` passed independent byte-for-byte recomputation.
- `git diff --check` and actionlint 1.7.12 passed; workflow configuration is unchanged. Optional shellcheck integration is unavailable locally.

Metrics were regenerated, not edited by hand. Source hashes and artifact checksums were refreshed. Linux may differ from macOS in final floating-point bits; CI generates and verifies results within its own runtime. Synthetic data only; no clinical validation is claimed.

Hosted results are available on this repository's [Actions page](https://github.com/hrix7/AutoEEG-Research-Lab/actions). This entry records local checks, not a claim that an as-yet-unobserved hosted run succeeded.

## 2026-11-13

Hann spectral estimates with explicit window-energy normalization and off-bin leakage/flat-spectrum tests.

Adds symmetric Hann power estimates alongside existing rectangular estimates on the same accepted epochs. Power is normalized by fs × sum(window²). Alpha fractions use the 1–40 Hz integer evaluation grid, not a continuous-band integral. Zero-power accepted epochs are counted separately and have undefined spectral estimates; no arbitrary peak is assigned. The window comparison does not establish patient or disease performance.

Validation: full unittest suite, pipeline regeneration and byte-for-byte verifier, diff review; GitHub validation outcome is tracked after push. No workflow/permission changes.

## 2026-11-14

Noiseless off-bin recovery/leakage probe on the fixed evaluation grid.

Adds a deterministic amplitude-1 10.3 Hz sinusoid probe separate from noisy epoch data. Reports each window’s integer-grid peak error and fraction of sampled 1–40 Hz power more than 2 Hz from truth. This exposes frequency-resolution limits, not an interpolated exact-frequency claim. Existing noisy datasets and acceptance thresholds stay unchanged.

Validation before publication: full unittest suite, regenerated pipeline artifacts, byte-for-byte verification and diff review. Workflow configuration/permissions unchanged; existing policy tests pass. Hosted CI is followed after the tested source is published.

## 2026-11-15

Validate configuration before generating signal epochs.

Rejects unsupported sampling/duration/epoch types, nonfinite or negative amplitudes/noise/thresholds, and empty/duplicate noise grids before generation. Zero noise and a zero rejection threshold remain supported. Current default data and scientific thresholds are unchanged.

Validation before publication: full unittest suite, pipeline regeneration/byte verifier, diff review and existing workflow-policy tests. Workflows and permissions unchanged. Hosted validation is followed after publication.

## 2026-11-17 — Preset rejection-threshold tradeoffs

Completed the retained, unpublished implementation from November 16. Added fixed 75/150/300 uV peak-to-peak rejection tables with hand-counted confusion tests and strict boundary coverage. Thresholds are predeclared, not tuned or selected on these results. The configured detector and random stream remain unchanged. Full unit tests, pipeline regeneration and artifact verification run before publication; no workflow or permission changes.

## 2026-11-18 — Reject invalid threshold-study inputs

Threshold tradeoffs now reject NaN/infinite/negative amplitudes, ambiguous injection labels, duplicate/invalid thresholds and one-shot iterators. This prevents silent clean/artifact miscounts. Tests cover malformed inputs, zero boundaries, empty records and nonmutation. Existing valid benchmark settings are unchanged. Full suite: 22 tests passed; pipeline generation, independent --verify and diff checks passed before publication. No workflow/permission changes; workflow policy tests passed.

## 2026-11-19 — Known-support artifact-family probes

Added a separate nine-case noiseless study of rectangular pulse, blink-like deflection and enveloped 30 Hz muscle-like teaching shapes at predeclared amplitudes. Injection support is explicit in sample indices and full signals have reproducible hashes. The original noisy epochs, random stream and rejection threshold are unchanged. These shapes are not validated physiological artifact models. Tests independently evaluate injection formulas/support and recompute hashes/rejections. Full suite: 25 tests passed; pipeline generation, independent --verify and diff checks passed before publication. No workflow or permission changes; workflow policy tests passed.

## 2026-11-20 — Spectral effects of injected artifacts

Added rectangular/Hann fixed-grid peak and alpha-fraction diagnostics for every artifact-family probe plus its clean two-sinusoid reference. Rejected cases remain explicitly diagnostic and do not bypass the primary rejection pipeline. Independent complex-DFT, known-frequency and flat/undefined tests validate summaries. No random streams or thresholds were tuned. Full suite: 27 tests passed; pipeline generation, independent --verify and diff checks passed before publication. Workflow policy tests passed without workflow/permission changes.

## 2026-11-21 — Reject unrepresentable spectral power

A finite input can overflow the DFT power calculation. Reject nonfinite power before it becomes a JSON infinity or an undefined alpha ratio. Extreme-amplitude rectangular/Hann and diagnostic failure cases added. Ordinary synthetic values and seeds unchanged.

Validation: full existing suite plus new tests (28 passed), pipeline generation and independent --verify, scoped diff review and git diff --check before publication. Hosted CI is followed after pushing. Existing read-only validation/publisher workflows unchanged; workflow-policy tests included.

## 2026-11-24 — Paired artifact-family noise sensitivity

Three predeclared local noise seeds and each configured noise level now evaluate nine teaching injection cases against matched clean signals. Fixed threshold, signal hashes, separate RNG and no retuning or population/clinical sensitivity claim. Tests independently reconstruct every signal/hash/rejection and check zero-noise invariance/global-RNG isolation.

Validation before publication: 30 full-suite tests passed, pipeline regeneration and independent --verify passed, scoped diff/checksum review and git diff --check passed. Workflow policy tests included; workflows and permissions unchanged. Hosted validation followed after pushing.

## 2026-11-25 — Paired noisy-artifact spectra

Each predeclared noise/artifact case now retains both its matched clean and injected rectangular/Hann spectral summaries, including rejected cases as diagnostic-only values. Fixed grid/rule and separate RNG remain unchanged. An independent complex DFT checks the matched clean fraction; rejected-case finiteness is checked. No rejection bypass or clinical spectrum claim.

Pre-publication validation: 32 full-suite tests passed; pipeline generation and independent --verify, scoped diff and checksum review, git diff --check passed. Existing workflow policy tests included; no permission/workflow changes. Hosted CI followed after publication.
