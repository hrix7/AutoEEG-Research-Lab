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
  "artifact_noise_probe": {
    "cases": [
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7097367289247111,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5865311242471727,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "382a8d886d513e55f0cd509f63a32717f4b2316f8af15ce8a84b56a04a6c4a8e"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.2661282447265434,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.17845395580545947,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "f14cc6f218a446d25b21bedb670259e142db9b40fa552c987c81fe677a9ff8ca"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09383582634185214,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06791351845494728,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "f196f68480683ba44337e0daa10ff42bd08bf70093e75ea47e258094bd7f113b"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7967365676071392,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.6965206486387833,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "0d0d58195fcf037c493b0e1ad2de1712dfbe57b6bcb9256cc5eac347b879ed77"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.3406565181876568,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.20734490653168958,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "d2523809fbc916407677c35003f60bfa921aab6d7ac585b6a87d13f711ad67d7"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07575107049446284,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.0384906941284076,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "01ca870b3b0203e39addebedf6ca69fb6fb4df4e0137c5a17951d3ce6e9cfea5"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.8523061798259153,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7902553052017794,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "2f68580f21844e5fc0d202e164856017f4c9826ef20f7910fa58be076ecfe55a"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.47384895085991313,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3218208744074873,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "c761988bb2e6e40b7ab379037488aac9faa9bdd3a179e130e2838fd358f1f4a3"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9225367079360822,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9140717322970915,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.1323878528474417,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07219921596653567,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "bf0d5c763762810adaa7fea3c78f93324d1073f92c4bd7322b6bdc332088c69b"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.6350980157268191,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.49909881636435677,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "cc39e448fce912ae4c78b6f0bf6e9f6f77233a75169518be16475686e98ff159"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.2551371818690146,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.16709151589179386,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "d67a58ac03be939891bb5fbf86d0d8f079d282305c8a2f50a638a4525e73b974"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09344125193882244,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06639440374596481,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "964a880001740eded6a9ef91aadbdf626f250187b6dc37e00fdc568b64012098"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.6972637944119519,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.567048480274811,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "a69a0f98e1999db75bbdc49e645f1bb9cbbe6e95aa930681d32a56b8062df1c1"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.31296320040808817,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.18318854559594908,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "6d1f801ac19d235d3338fa0bbd3c30a479e87c538f0e296a16e2dc41d51bd577"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07333035681830519,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03591164469479572,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "15ff238c13c8c9d59c87b55386c6eb200ca7cd11893eb9a7753b129d145e74ac"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7680180420447422,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.6840056645646126,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "89345bb6de5a5ffc2fbf81c27df1bc846e957ced844d41fee6ad874dbceb8e6f"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.4543587280551258,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3072870344855936,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "a0149a1189f39ec82e25525ed2e96526999e892ef727668ecbb1ba2afbf05b83"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8153418760001054,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7521159291796213,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.1327418697397549,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07099638950243731,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "0cb0c71d15db6d6b680e01a4f2a9f6754b0bdd010e2812a278132c47d38ec166"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5030166262048561,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3696664027637027,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "1819f54cb4e50f9bd9e04ab9317adb3f694d1c78bb147b4c2ee982eefbb15b04"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.23516143253957428,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.151112904129182,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "eef07b9a921e41ec24cdf2bdd81db4788e8adb479d5983d070c238285d858f39"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09264859482290465,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06457607830694677,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "d2a60777e772daf1125728af9ef10684bcbf87cf21991a78d1d5990e41e34b6d"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5264224534494013,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3870492887990503,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "272a25dfb64e734b1f2e2ee9d554bf56bdbccc4855d0c6ae7248760774fef40a"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.26703708529395853,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.15178959971398148,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "d87272502986ce3b2e98e52cd19f88cfcd81d3609c3f54f64239cf6314ebd46d"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07015311007702374,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03352244295665324,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "81b00228c443a599d18986a1ec4c9d87d686f219a9347f98ab3d0aba51186a57"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.587715486365619,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4751528171740194,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6729,
        "signal_sha256": "b02643209a60e302f919eacbb95b46fa3285e9efa32ded1c9ba59874fa2e6379"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.3940844472852369,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.2654251915778248,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "9bf0be1c2629baa718af963657edebc5ce6713b2775aee23b16844bd2df4d6d1"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6079911977386002,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4924898279295362,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.13077442927070126,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06968125572588472,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6729,
        "signal_sha256": "ff1dba1f516d714ec3c88fa22197a90fcad0f9519eefdafc2d7541c691d904a5"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7103597473347437,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5962647417320202,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "0feee8be287c9997f57da42f87a39484a610f83e04455a62428e7ee941c44f71"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.26422804408901185,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.18093339426066055,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "9e5d15b0007b18128fa09f58f6d034f37521562d09ed485301572c71df5ab9ac"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09284502922363819,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06834175660209546,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "ead006605add229e62ca3050ea60e5fdc642b56b7c8d7f34a9202e9133a5e530"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7947606266454871,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7031468102067536,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "599ab78702f80416d0f2811e4c2a932f531fd5ffc2b1d9e72042a50bdebf70d2"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.337261552689695,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.21095795812354912,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "d9ec89875833f62f27f18d56c89b06372beec12f0b0072c382d7be168618022b"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07500729900379988,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03929562145978891,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "652cbb6ac369b05480067d1c415deb1fb8e453fbde57765d874444f8d612e969"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.8490145205502381,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7861614017445966,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "ace87b549f93bdcdb4d2b1301e75bbd23ddd6f76bd190ae965b234ba8c0a6429"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.4672505286001235,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3209527248199893,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "12613df8d0827c2573837f410f5bc0e3c98830281c1cf5a2d28fb0af4ed62b5f"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9252840990861405,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9181472757458512,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.13036938246363883,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07275424485365435,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "1c503ef6dba81cfe267f5cc549589e16781b965ef5369c371e43c8e3c38f43be"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.6331474604789993,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5368277774815515,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "5f2041b737c65610d53a7d16ab0b6ce798185988124e2050ff6aab81672f3654"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.24751801858441716,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.17641113420569335,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "9e329eb89bcf6a4dd70ac9f8d45000f44539aab8b78b5755423d603a1e5d548e"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.08953110044382395,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06801645501126885,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "af40fcf7cbb94f5dae1664323553068792253f349edce770326d03ae6932877c"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.6865241561718534,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5991824668640967,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "57c44ea55f7b03c76dda338663eb2dfee05969bf7052d4cd98f99b7de4f55e7c"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.3004846407510828,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.19654504478459797,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "8079623083991e5da646166f13dfab669491790882b9f43c0a26bc43461b679b"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07049618867014192,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03885833697852588,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "47292ee4b0e04c7273ff414fd368d749eb2b369f1dc7a4c36a0210b3e040cd3f"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7527548669402861,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.6875157576373628,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "f277340f10c4ff40435c04a247892efc2741a378a9ac14ea726dfaca15fc01a0"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.4294044813542155,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.30621693777184866,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "0b05e0894c306ff5cffb98ca160248c838ef980ea5e91f1aab0b497de4ee3a66"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8185165186758689,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7849556045330249,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.12480947467786416,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.0730258319953948,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "b778866fbf3e353adc67a7ee258522d93bb79b35f64e91320dc26eec8b8a4c97"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.48960376616352347,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.42844957076798174,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "23c231031e0d6af55f0d4db8deb6fe0fea041194910e26b577f3f87d295d4336"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.22034204469539348,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.16754041261804722,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "58d65ea276c8091b6e804be3769401c71985335277c6eaec4ae2a6ac277d6013"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.08503121182911706,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06756554798549681,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "20cf6d008b8c4415934a60a2c77074d4d5608d2b3e096a2bef91d5b418864071"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5027779905762105,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.441651385619714,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "32f2e65d93a25812f563a88c3abf1c9069c7cf21862f0820af3bbcd2390e9369"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.24628901603398184,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.17401056417740635,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "7006abe9e0d0bb741a7cdce4ae8b76b3e7b2a7be5f130e9223b42cdbd4658864"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.06493346288153493,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.038658911651776866,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "449d3191e79da5219891335811aa064467d124605f82c73f9b4de309ba53e8e8"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5572853731592324,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5077132568062258,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6730,
        "signal_sha256": "b1c88fa7858a7853519c4c695b8d7e36a632c6aa537c87c90ea2b24631289d70"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.35330919934447336,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.26998795467476383,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "b1fade6b469632d24a9b1ccf1da3a8679d7433af294e170d98299cf4c7437e10"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.5965800032731549,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5569173582933972,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.11587593146215422,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07313492598425168,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6730,
        "signal_sha256": "57d92f5cc1b4271de6f256f56498b06e3dd8c41212e7400a98e516dee5f92674"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7163982620457389,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5908753528773697,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "02ac88cf7498ea095260d0b69e3213ea63ca0629c1906864a5df3ea3afaf73f2"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.2648256788317553,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.17631490367041625,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "ce768326a095ab4fbb4188c9386ff77d4f8626cd9fee622b4bbe841769b883a6"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.09217154587033868,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.0665102034268053,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "6368045dbb3de646b5d0789434fc61a9241e20f88b3e0512e4e6d979c346b165"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.8081287023165786,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7146475306083896,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "b038a0bcf0eba7c4622d0607ec885c49db948bb7131ea4f2ad6c5e18213de300"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.3458290497648247,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.2118404826398571,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "b832696413ef2dd57b507cec96d846bf2240a2a619e4fa5fa102eac536399552"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07644778167559778,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.03911437128120127,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "92da341390fc0186fbd2a3493a2de05eaa773eab592ddfac4013e359042ae39e"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.8463175481268143,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.783490328511785,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "1f8f06f55d6d816a8dd113d74533b9ff424d3fdf6147cf4620143bef9f559a9f"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.4641266814477348,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.3149067245952545,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "227c818adf88adcaa22ee98c0416bd437b41f97a7a94fa44b0a45ab93aa04373"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.9267333410560842,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.9249970516378787,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.12986738358713318,
            "peak_hz": 30,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07115370995541274,
            "peak_hz": 30,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 2,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "5d1af8d9df7b6bae4729515ac4e056329cd3189d0410d7f1d5ac022d2dc08e2f"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.6531749815407581,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5068015237870475,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "f073dcd20c78ceaece7540cb64c6bc42e6e874eff8a9992f91ee4d645d84d9e9"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.25324054477754354,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.16128309362582718,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "96472a5b7c07108eebbd7774c0675850884a7d06318503ea122f4cdc33caccb2"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.08792227049742037,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06153676863650534,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "1d84edb6a6b872de1c19414e2ce78073fab2b462535c2e131c3bde2410898163"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7271895793930524,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.6092413472694029,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "79cbf85f9835c3556a627cdabf46e6d9aa744ec869baffc9b73503747fbb804a"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.3367760828739153,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.20393754309670983,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "c8ecb71e2ad99421441efc4bca2f3464d91b5f00962b4367967cc113b933a43a"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.07872063376060974,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.04010464613446945,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "ee758dc0bd9e2ddbf941c181dfcc40847c3a73c96fbe187edba658bff8d6d251"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.7417288213861664,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.6493421270668984,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "56cb4c03f6e91fdb8b0675bbaf0775be6e3e6a2217e6a6853e17874089fb056e"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.42489389811985867,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.28748950655061795,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "ac0b5d4e051d56727aa3a3f32ec359eb7b80ae4d9ffea8bd007cbb1e8b56cfb1"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.8168739219370345,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.7578251857592025,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.12675923111822504,
            "peak_hz": 29,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.06963415366105515,
            "peak_hz": 29,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 8,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "d31bb9e3f2e4b54b47b625a896f65b81e3d1318140d7bdc085d942946a09a94b"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5294589918394196,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.38388117770716595,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "516f35affdce22f45da8486505123d7e5361f28ab090f0db717ad171c35a5b91"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.23971733749660845,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.14706451078369676,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "fc9ea45edb6cfd3e9d92e9ba6fcf58e1696275d257520159cf88bb5122d281a7"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.0847277336495237,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.0569319060958418,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "pulse",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "05f108ac1f0b8d166248ba273e32d10705b87809ec19abf80e4230ed7b366cfe"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5687383769170936,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.4400396514404042,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "01b9b1a1fa139e48ef7f4a79ce3864e3fde3e239f16e996e45caba323d2afeeb"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.3182238019356875,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.1970317132251691,
            "peak_hz": 2,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "4a128cc5d3c998f25b0d132551b33623ccf4cc68026bc8e19db4d353b447bdec"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.0871903869688683,
            "peak_hz": 1,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.04605974767219528,
            "peak_hz": 1,
            "window": "hann"
          }
        ],
        "family": "blink",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "5b01409abfde8ea9093acf8239f995da188a64fdb0f1c19a93c0e7adfdaa66a7"
      },
      {
        "amplitude_uV": 30,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.5661812245554168,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.45311925080648435,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": false,
        "seed": 6731,
        "signal_sha256": "8f7731e58b842dd872cb49fb8e51b4a1c857ce447ebc947e878022701c5e4b44"
      },
      {
        "amplitude_uV": 100,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.36763696821699016,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.25243187924922345,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "12eab0b07298ebed98b404df190a9dde1a7db2e6a7797ce02e15f2c9a6bdda7c"
      },
      {
        "amplitude_uV": 250,
        "clean_diagnostic_spectra": [
          {
            "alpha_fraction": 0.6141160220732265,
            "peak_hz": 10,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.5041529334506255,
            "peak_hz": 10,
            "window": "hann"
          }
        ],
        "clean_rejected": false,
        "diagnostic_spectra": [
          {
            "alpha_fraction": 0.12896846918317043,
            "peak_hz": 29,
            "window": "rectangular"
          },
          {
            "alpha_fraction": 0.07374859138261486,
            "peak_hz": 29,
            "window": "hann"
          }
        ],
        "family": "muscle",
        "noise_sd_uV": 16,
        "rejected": true,
        "seed": 6731,
        "signal_sha256": "fafd9842062d6718b4ec1d2ff6035cf8f2d954024bc50f4918dc0ca00fdfa56f"
      }
    ],
    "method": "Three predeclared noise seeds seed+5000..5002; paired base noise across nine teaching artifacts and matched clean comparator. Fixed rejection threshold, no tuning. Separate RNG from primary epochs. Descriptive finite scenario grid, not population sensitivity or clinical validation."
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

Result SHA-256: `587aa00fe18763accfcd1df447ada7130534f2c22152808d41b2540d24732814`
