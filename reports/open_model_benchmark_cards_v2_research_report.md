# Open Model Benchmark Cards V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `reports/results/portfolio_benchmark_cards.json`
- Profile: `full`
- Runtime: `0.307` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `schema_validation`: `schema`
- `reproducibility_score`: `reproducibility`
- `limitation_quality`: `limitations`
- `portfolio_index`: `portfolio`

## Experiments

The matrix produced `8` result rows. Best observed `completeness_score`: `1.0000` from `agent-safety-eval-lab`.

## Results

Key artifacts:

- `reports\results\v2_benchmark_cards.json`
- `reports\results\v2_card_quality_scores.csv`
- `reports\figures\v2_card_artifact_counts.png`
- `reports\figures\v2_card_completeness.png`
- `reports\figures\v2_card_experiment_counts.png`

## Ablations

Configured ablations: required_fields, artifact_links, risk_sections, metric_coverage. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `0`.

Top clusters:



## Discussion

Benchmark cards are useful when they are auditable. V2 consumes the other repositories' experiment indexes and scores every card for reproducibility and limitation coverage.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
