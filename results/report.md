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
        "signal_sha256": "146efbc091cd71bbaf1fa56acd76a89f8f9e4926f641e7cccc136d554adeee2e",
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
        "signal_sha256": "cf343c424949a8920619db2e3de4eedbf55a8d65541c55738926154b1e8b0907",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09392531074906696,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06844685314795793,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "pulse",
        "injected_amplitude_uV": 250,
        "peak_to_peak_uV": 283.37324022483097,
        "rejected": true,
        "signal_sha256": "f89ec2200d2494d2fcdd63ec7f871998d8bb7af01901a52abca3ceaeed02c562",
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
        "signal_sha256": "e4fcfd0dde9a5596af689f323b9eca8d888b7c06ae5a2772f248cf5ef4f96efc",
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
            "alpha_fraction": 0.2147131746137462,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "blink",
        "injected_amplitude_uV": 100,
        "peak_to_peak_uV": 132.2805815470125,
        "rejected": false,
        "signal_sha256": "32bb90d134dafb0716e04e15d2bc297616112de40f4322e7175c7a38f1bf3a43",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07654554769487525,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03949936880181495,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "blink",
        "injected_amplitude_uV": 250,
        "peak_to_peak_uV": 281.6866201124155,
        "rejected": true,
        "signal_sha256": "a11b519b0a58df317b32d737bc9ec88fa2fca310b515d8cb525ee43516e2edfc",
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
        "signal_sha256": "add873c6742ed89f9f83064f4220e1e4bd20e237cec15a8e9d675f65fb911b0d",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.47332642066253433,
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
        "signal_sha256": "583fe36f3f8fb83aa07b7394953285952b70383ca3af80e5fedbc8e57ef06d8d",
        "start_sample": 64
      },
      {
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.1319103099666308,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.0726278029367766,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "end_sample_exclusive": 96,
        "family": "muscle",
        "injected_amplitude_uV": 250,
        "peak_to_peak_uV": 482.893162469854,
        "rejected": true,
        "signal_sha256": "b5b200d9053e401a4287e1118b59593544c97d391ae19a4b627136aec9d87a18",
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

Result SHA-256: `a309c5baeffb1b77b57f9edf31f222c27d83a68c987f55ac73958d063945dbf3`
