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
