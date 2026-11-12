# Security and data policy

Do not commit patient records, credentials, health identifiers or private measurements. Use synthetic inputs by default. No network access occurs in experiments. Pull request validation has read-only permissions and cannot publish. Do not switch to pull_request_target to execute contributor code. The trusted default-branch publishing job has narrowly scoped contents write permission and stages only results/. Keep workflow actions pinned and review source changes before merging.

Report suspected security problems privately to the repository owner through GitHub's available private reporting channel. Do not attach sensitive biomedical data to issues.
