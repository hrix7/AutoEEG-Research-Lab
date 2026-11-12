# Starter validation record

Validated locally on November 11, 2026 (America/Phoenix), using Python 3.11.0 on macOS.

- `python3 -m unittest discover -s tests -v`: 6 tests passed.
- `python3 pipeline.py`: generated all synthetic artifacts successfully.
- `python3 pipeline.py --verify`: independent recomputation and artifact checksums matched.
- `actionlint 1.7.12 -no-color .github/workflows/daily.yml`: passed with no findings. Shellcheck was not installed; actionlint's optional shellcheck integration was therefore unavailable.
- Pinned checkout v4.2.2, setup-python v5.6.0 and upload-artifact v4.6.2 SHAs matched their official GitHub tag references.

Tests cover deterministic recomputation, finite metrics, deliberate artifact tampering, project-specific mathematical behavior, and workflow permission/publishing policy. No remote GitHub Actions execution has been observed yet. Local success does not establish clinical validity or guarantee platform-identical floating-point bytes. CI generates and verifies results in the same runtime before publication.

The daily workflow schedules execution and report verification; it does not schedule autonomous source-code development. Repository creation and the first remote push are required to activate it.

## GitHub publication verification — November 12, 2026

The repository has been published under `hrix7`. The initial hosted validation passed on ubuntu-24.04. Workflow action pins were then upgraded to official checkout v7.0.1, setup-python v7.1.0 and upload-artifact v7.0.2 commit references to remove the Node 20 deprecation warning. These versions use Node 24 and retain the inputs used by this workflow. Final hosted validation and publishing run evidence is recorded on the repository Actions page.
