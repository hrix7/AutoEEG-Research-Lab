# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "artifact_family_probe": {
    "cases": [
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7228816040868178,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.6059316119806523,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "pulse",
        "injected_amplitude_uV": 30,
        "peak_to_peak_uV": 63.37324022483098,
        "rejected": false,
        "signal_sha256": "7e8ba6c44f6d4bb14011d1eefadc0f7b7cd47db00f74b9a5439395be745cb95f",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.2686834878791994,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.18192095097853003,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "pulse",
        "injected_amplitude_uV": 100,
        "peak_to_peak_uV": 133.37324022483097,
        "rejected": false,
        "signal_sha256": "0cfee9827c01cfbadaacebe144dc05e005f4abfaab83691631dda2f6b45bb5cd",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09392531074906697,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.0684468531479579,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "pulse",
        "injected_amplitude_uV": 250,
        "peak_to_peak_uV": 283.37324022483097,
        "rejected": true,
        "signal_sha256": "7ca540fdfaf943e2b97489c4a335caee02dcdf20320b1500d6472767e863f8f9",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.8129775085855774,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7232189817190063,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "blink",
        "injected_amplitude_uV": 30,
        "peak_to_peak_uV": 62.95309673289945,
        "rejected": false,
        "signal_sha256": "bfb4649fb17ba019e7660e01adff6100fc79b152984e7c8ea1e0a3839e2caf72",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.34715980810743485,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.21471317461374623,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "blink",
        "injected_amplitude_uV": 100,
        "peak_to_peak_uV": 132.2805815470125,
        "rejected": false,
        "signal_sha256": "45dae42f09717582d464d4841e724c7fa8d3d8166567d1dc85439072637f4e8c",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07654554769487526,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03949936880181493,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "blink",
        "injected_amplitude_uV": 250,
        "peak_to_peak_uV": 281.6866201124155,
        "rejected": true,
        "signal_sha256": "cf116e144ab4fe4a29a6651406ab713ecfdff4a8ddc327b257ca8587919674b7",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.8584758200772707,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7973260313595157,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "muscle",
        "injected_amplitude_uV": 30,
        "peak_to_peak_uV": 72.55885636114562,
        "rejected": false,
        "signal_sha256": "6a6cb299e5f13a28c222540bacde0c575530492094c548ad141615945019ce2d",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.47332642066253416,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3222269561751266,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "muscle",
        "injected_amplitude_uV": 100,
        "peak_to_peak_uV": 193.8014373208415,
        "rejected": true,
        "signal_sha256": "4aa22459f510993479d382b877b6585fccd1913aa7abbe3ebfa3aa4e81c796a3",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.13191030996663078,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07262780293677662,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "muscle",
        "injected_amplitude_uV": 250,
        "peak_to_peak_uV": 482.893162469854,
        "rejected": true,
        "signal_sha256": "3f21ecba9f2b6f77f06b0c4dbf8b37f4b7f27e05be354404262aa6c0d92fa286",
        "start_sample": 64
      }
    ],
    "clean_diagnostic_spectra": [
      {
        "alpha_fraction": 0.9336099585062241,
        "peak_hz": 10,
        "window": "rectangular"
      },
      {
        "alpha_fraction": 0.9336058859664749,
        "peak_hz": 10,
        "window": "hann"
      }
    ],
    "interpretation": "Separate noiseless nine-case probe: fixed floor(fs/4)-sample rectangular pulse, sin-squared blink-like deflection, or 30 Hz sinusoid under the same envelope. Names describe teaching shapes, not validated physiological artifacts. Known injection window; primary epoch generator/noise stream/threshold unchanged. No tuning or clinical inference.",
    "spectral_scope": "Spectra are diagnostic on every probe signal, including rejected cases; they do not bypass primary rejection. Compare fixed-grid peaks/alpha fractions with the clean two-sinusoid reference. No fitted threshold or clinical interpretation."
  },
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
      "hann_mean_alpha_fraction": 0.5445426197932012,
      "hann_mean_peak_hz": 10,
      "mean_alpha_fraction": 0.6285293325330541,
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
        "far_grid_fraction": 0.06283966699555599,
        "peak_hz": 10,
        "window": "rectangular"
      },
      {
        "absolute_peak_error_hz": 0.3000000000000007,
        "far_grid_fraction": 2.6016735469837423e-05,
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

Result SHA-256: `a3e18e6a784efc0074c151e5fb4db67b31cbc2a58063919229de27f3ca3962c3`
