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
