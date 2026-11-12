# AutoEEG-Research-Lab

Synthetic EEG spectral recovery and artifact rejection. Reproducible educational biomedical engineering project, with daily verified experiment reports.

**Synthetic data only. No clinical validity, diagnostic performance or medical-device suitability is claimed.** Every metric in [the report](results/report.md) is computed by the pipeline. There are no hand-entered performance claims.

## Run locally

Requires Python 3.11 and Git. No packages, credentials, network access, special hardware or downloaded datasets are required.

```sh
python3 -m unittest discover -s tests -v
python3 pipeline.py
python3 pipeline.py --verify
```

Run commands from this repository's root. `--output /tmp/experiment` supports isolated results. `--verify` recomputes data and metrics and compares every artifact byte and manifest; it exits nonzero on missing or modified results. To change an experiment, edit `config.json`, run tests, regenerate, verify and review the diff before committing.

## Method and provenance

The generator creates 2-second, 128 Hz epochs with a 15 uV 10 Hz sinusoid, a 4 uV 20 Hz sinusoid and Gaussian noise (SD 2, 8 or 16 uV). Every fourth epoch receives an eight-sample 250 uV pulse. A fixed 150 uV peak-to-peak rule excludes contaminated epochs before analysis. The one-sided rectangular-window periodogram covers integer frequencies 1–40 Hz. Outputs include peak frequency, 8–12 Hz power fraction and artifact counts by noise level. Epoch length aligns both sinusoids to DFT bins; this makes recovery easier than real EEG. No filtering, source localization or seizure detection is claimed.

See [data provenance](DATA_PROVENANCE.md) for units, assumptions, origin and limitations. The configuration lists all experiment settings and seeds. There is no automatic patient-data ingestion.

## Repository layout

- `pipeline.py`: generator, method, metrics, report and verification CLI.
- `config.json`: versioned experiment protocol.
- `tests/`: mathematical, reproducibility and tamper-detection checks.
- `results/`: generated CSV, measured JSON, Markdown report and checksum manifest.
- `.github/workflows/daily.yml`: test, reproduce, verify, then publish changed results.

## Daily automation and setup

The workflow runs on pushes, pull requests, manual dispatch and daily at `23 9 * * *` UTC. Schedules use the default branch; GitHub can delay scheduled runs and can disable schedules on inactive public repositories. Enable Actions in repository settings and inspect the Actions page after the first push. No personal access token or external secrets are needed.

Validation has read-only repository permissions and never retains checkout credentials. Only the separate publish job receives `contents: write`; it runs after successful validation on default-branch schedule/manual events. It reruns tests and verification before committing only `results/`, using the built-in token. Pull requests cannot publish. All external actions are pinned to commit SHAs. Concurrency prevents overlapping publishers; pushes use normal fast-forward semantics and fail safely on competing changes. Branch protection may intentionally block direct bot pushes; in that case reports remain in run artifacts and maintainers can adopt a PR publishing policy.

Each successful run uploads its verified report/data artifact for 30 days and displays the report in the run summary. Identical results produce no empty commits. A daily rerun verifies reproducibility; it does not invent research progress or autonomously modify algorithms. Notifications and branch protections are controlled in GitHub settings. Public repositories may need schedule reactivation after inactivity.

## Numerical and evaluation safeguards

Artifact labels are counted from the generated epochs, including nonmultiples of four. The report includes false positives, false negatives and true negatives. If no epochs survive rejection, spectral means are JSON null (undefined), not zero.

## Development history

See [completed improvements and validation](DEVELOPMENT_LOG.md) and the [ordered development backlog](DEVELOPMENT_BACKLOG.md).

## Roadmap

Add independently sourced, license-reviewed public data, stronger baselines and uncertainty estimates before any real-data claims. Keep synthetic and public-data results visibly separate. Clinical deployment is outside this project's scope.

## License

MIT; see [LICENSE](LICENSE).
