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
