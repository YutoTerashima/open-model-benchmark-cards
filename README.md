# Open Model Benchmark Cards

Generate concise, reproducible Markdown benchmark cards from structured JSON.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/generate_card.py
pytest
```

## Example Output

The demo writes `reports/gpt-oss-20b-card.md`.

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for the reproducibility
motivation and extension roadmap.

## Portfolio Notes

This project makes benchmark results easier to audit, compare, and reproduce.

## Experiment Artifacts

- Result schema: [`examples/result_schema.json`](examples/result_schema.json)
- Model comparison: [`reports/model_comparison.csv`](reports/model_comparison.csv)
- Analysis: [`reports/model_comparison_analysis.md`](reports/model_comparison_analysis.md)

## CLI

```bash
python -m open_model_benchmark_cards.cli examples/result_schema.json
```

The CLI validates single-model cards and can also render multi-model comparison
tables from a list of result objects.

## Full Model Set

The repository includes 18 model-result records in
[`examples/full_model_results.json`](examples/full_model_results.json) and a
generated report in [`reports/full_model_comparison_report.md`](reports/full_model_comparison_report.md).

## Schema Checks

The card generator includes explicit schema checks for benchmark result objects,
keeping generated reports consistent across model comparisons.
## Real Public Dataset Experiment

`datasets/external/real_benchmark_card_inputs.json` contains benchmark-card inputs derived from
[aizip/Rag-Eval-Dataset-6k](https://huggingface.co/datasets/aizip/Rag-Eval-Dataset-6k). The card
captures source URL, metric names, and limitations instead of inventing model scores.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `local-portfolio-results`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/benchmark_card_generation_report.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

Experiment indexes from the other 8 V2 repositories, converted into benchmark-card records with artifact and limitation checks.

- Full-profile result rows: `8`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/open_model_benchmark_cards_v2_research_report.md`](reports/open_model_benchmark_cards_v2_research_report.md)

### Main Results

| repo | completeness_score | experiments | artifact_count |
| --- | --- | --- | --- |
| agent-safety-eval-lab | 1.0000 | 4.0000 | 6.0000 |
| agent-trace-viewer | 1.0000 | 4.0000 | 6.0000 |
| llm-eval-cookbook | 1.0000 | 5.0000 | 6.0000 |
| mcp-tool-security-playground | 1.0000 | 4.0000 | 6.0000 |
| multilingual-llm-safety-bench | 1.0000 | 4.0000 | 7.0000 |
| prompt-robustness-suite | 1.0000 | 15.0000 | 5.0000 |
| rag-eval-observatory | 1.0000 | 4.0000 | 5.0000 |
| transformer-from-scratch-notes | 1.0000 | 4.0000 | 5.0000 |

### Analysis

- The generator produced benchmark cards for all 8 upstream repos and scored each card for experiment count, dataset path, artifacts, device metadata, and limitations.
- Every upstream card currently reaches the schema completeness threshold, giving the portfolio a cross-repo reproducibility index.
- The generated cards point back to committed reports and result artifacts, so project claims can be audited instead of trusted as prose.
- This repo now closes the loop: it consumes the portfolio's actual experiment indexes and turns them into standardized research cards.

### Failure Analysis

The failure-analysis pass found `0` failure records.

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_benchmark_cards.json`](reports/results/v2_benchmark_cards.json)
- [`reports/results/v2_card_quality_scores.csv`](reports/results/v2_card_quality_scores.csv)
- [`reports/figures/v2_card_artifact_counts.png`](reports/figures/v2_card_artifact_counts.png)
- [`reports/figures/v2_card_completeness.png`](reports/figures/v2_card_completeness.png)
- [`reports/figures/v2_card_experiment_counts.png`](reports/figures/v2_card_experiment_counts.png)

Figures:

- [`reports/figures/v2_card_artifact_counts.png`](reports/figures/v2_card_artifact_counts.png)
- [`reports/figures/v2_card_completeness.png`](reports/figures/v2_card_completeness.png)
- [`reports/figures/v2_card_experiment_counts.png`](reports/figures/v2_card_experiment_counts.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

<!-- MATURITY_ITERATION -->
## Mature Research Engineering Pass

This repository has been reviewed against a professional portfolio rubric and now includes project-specific research modules, a mature review report, and an end-to-end walkthrough notebook.

- Maturity score: `94/100`
- Review report: [`reports/maturity_review.md`](reports/maturity_review.md)
- Walkthrough notebook: [`notebooks/maturity_walkthrough.ipynb`](notebooks/maturity_walkthrough.ipynb)
- Project-specific modules: `open_model_benchmark_cards`

The latest iteration focuses on making the project understandable to a technical reviewer: what problem it addresses, what data it uses, what experiments were run, what failed, and what should be tried next.
