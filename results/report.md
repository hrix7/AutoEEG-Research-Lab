# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "conditions": [
    {
      "accepted": 12,
      "artifact_false_negatives": 0,
      "artifact_false_positives": 0,
      "artifact_injected": 4,
      "artifact_true_negatives": 12,
      "artifact_true_positives": 4,
      "hann_mean_alpha_fraction": 0.9197819990083852,
      "hann_mean_peak_hz": 10,
      "mean_alpha_fraction": 0.9244013070379887,
      "mean_peak_hz": 10,
      "noise_sd_uV": 2,
      "rejected": 4,
      "rejection_tradeoffs": [
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 75,
          "true_negatives": 12,
          "true_positives": 4
        },
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 150,
          "true_negatives": 12,
          "true_positives": 4
        },
        {
          "false_negatives": 4,
          "false_positives": 0,
          "precision": null,
          "recall": 0.0,
          "threshold_uV": 300,
          "true_negatives": 12,
          "true_positives": 0
        }
      ],
      "spectral_epochs": 12
    },
    {
      "accepted": 12,
      "artifact_false_negatives": 0,
      "artifact_false_positives": 0,
      "artifact_injected": 4,
      "artifact_true_negatives": 12,
      "artifact_true_positives": 4,
      "hann_mean_alpha_fraction": 0.7620219876051486,
      "hann_mean_peak_hz": 10,
      "mean_alpha_fraction": 0.8163211137423881,
      "mean_peak_hz": 10,
      "noise_sd_uV": 8,
      "rejected": 4,
      "rejection_tradeoffs": [
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 75,
          "true_negatives": 12,
          "true_positives": 4
        },
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 150,
          "true_negatives": 12,
          "true_positives": 4
        },
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 300,
          "true_negatives": 12,
          "true_positives": 4
        }
      ],
      "spectral_epochs": 12
    },
    {
      "accepted": 12,
      "artifact_false_negatives": 0,
      "artifact_false_positives": 0,
      "artifact_injected": 4,
      "artifact_true_negatives": 12,
      "artifact_true_positives": 4,
      "hann_mean_alpha_fraction": 0.5445426197932011,
      "hann_mean_peak_hz": 10,
      "mean_alpha_fraction": 0.6285293325330542,
      "mean_peak_hz": 10,
      "noise_sd_uV": 16,
      "rejected": 4,
      "rejection_tradeoffs": [
        {
          "false_negatives": 0,
          "false_positives": 12,
          "precision": 0.25,
          "recall": 1.0,
          "threshold_uV": 75,
          "true_negatives": 0,
          "true_positives": 4
        },
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 150,
          "true_negatives": 12,
          "true_positives": 4
        },
        {
          "false_negatives": 0,
          "false_positives": 0,
          "precision": 1.0,
          "recall": 1.0,
          "threshold_uV": 300,
          "true_negatives": 12,
          "true_positives": 4
        }
      ],
      "spectral_epochs": 12
    }
  ],
  "interpretation": "Spectral recovery on generated sinusoids only; no disease labels or patient data.",
  "off_bin_probe": {
    "amplitude": 1,
    "estimates": [
      {
        "absolute_peak_error_hz": 0.3000000000000007,
        "far_grid_fraction": 0.06283966699555597,
        "peak_hz": 10,
        "window": "rectangular"
      },
      {
        "absolute_peak_error_hz": 0.3000000000000007,
        "far_grid_fraction": 2.601673546983745e-05,
        "peak_hz": 10,
        "window": "hann"
      }
    ],
    "generator_frequency_hz": 10.3,
    "grid_hz": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12,
      13,
      14,
      15,
      16,
      17,
      18,
      19,
      20,
      21,
      22,
      23,
      24,
      25,
      26,
      27,
      28,
      29,
      30,
      31,
      32,
      33,
      34,
      35,
      36,
      37,
      38,
      39,
      40
    ],
    "interpretation": "Noiseless off-bin probe on the fixed integer-Hz evaluation grid; a fractional frequency is not recovered exactly and Hann suppression is not disease classification.",
    "noise_sd": 0
  }
}
```

Result SHA-256: `143b09bfbef4eae6a5160ee1b790c19d0264a238130febeb6bc9b1030f099e0a`
