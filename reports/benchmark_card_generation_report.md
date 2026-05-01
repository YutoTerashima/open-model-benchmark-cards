# Benchmark Card Generation Report

Benchmark cards generated from local GPU experiment metadata.

## Dataset

- Source: `local-portfolio-results`
- Config: `default`
- Split: `reports`

## Reproducibility

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

## Generated Artifacts

- Result JSON: `results/portfolio_benchmark_cards.json`
- Figure: `figures/benchmark_cards_by_repo.png`

## Result Snapshot

```json
[
  {
    "repo": "agent-safety-eval-lab",
    "metric_file": "reports\\results\\gpu_classification_metrics.json",
    "dataset": "PKU-Alignment/BeaverTails",
    "device": {
      "requested_device": "cuda",
      "actual_device": "cuda",
      "cuda_available": true,
      "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
      "torch_version": "2.10.0+cu128",
      "cuda_runtime": "12.8"
    },
    "keys": [
      "dataset",
      "device",
      "failure_examples",
      "gpu_mlp_accuracy",
      "gpu_mlp_macro_f1",
      "gpu_pred_labels",
      "gpu_training_seconds",
      "history",
      "kind",
      "labels",
      "lr_pred_labels",
      "test_rows"
    ]
  },
  {
    "repo": "agent-trace-viewer",
    "metric_file": "reports\\results\\trace_summary.json",
    "dataset": null,
    "device": {
      "requested_device": "cuda",
      "actual_device": "cuda",
      "cuda_available": true,
      "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
      "torch_version": "2.10.0+cu128",
      "cuda_runtime": "12.8"
    },
    "keys": [
      "device",
      "policy_counts",
      "traces"
    ]
  },
  {
    "repo": "llm-eval-cookbook",
    "metric_file": "reports\\results\\eval_method_summary.json",
    "dataset": "aizip/Rag-Eval-Dataset-6k",
    "device": {
      "requested_device": "cuda",
      "actual_device": "cuda",
      "cuda_available": true,
      "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
      "torch_version": "2.10.0+cu128",
      "cuda_runtime": "12.8"
    },
    "keys": [
      "correlation",
      "dataset",
      "device",
      "mean_exact",
      "mean_lexical_overlap",
      "rows"
    ]
  },
  {
    "repo": "mcp-tool-security-playground",
    "metric_file": "reports\\results\\gpu_classification_metrics.json",
    "dataset": "S-Labs/prompt-injection-dataset",
    "device": {
      "requested_device": "cuda",
      "actual_device": "cuda",
      "cuda_available": true,
      "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
      "torch_version": "2.10.0+cu128",
      "cuda_runtime": "12.8"
    },
    "keys": [
      "dataset",
      "device",
      "failure_examples",
      "gpu_mlp_accuracy",
      "gpu_mlp_macro_f1",
      "gpu_pred_labels",
      "gpu_training_seconds",
      "history",
      "kind",
      "labels",
      "lr_pred_labels",
      "test_rows"
    ]
  },
  {
    "repo": "multilingual-llm-safety-bench",
    "metric_file": "reports\\results\\gpu_classification_metrics.json",
    "dataset": "lumees/multilingual-safety-classification-dataset",
    "device": {
      "requested_device": "cuda",
      "actual_device": "cuda",
      "cuda_available": true,
      "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
      "torch_version": "2.10.0+cu128",
      "cuda_runtime": "12.8"
    },
    "keys": [
      "dataset",
      "device",
      "failure_examples",
      "gpu_mlp_accuracy",
      "gpu_mlp_macro_f1",
      "gpu_pred_labels",
      "gpu_training_seconds",
      "history",
      "kind",
      "labels",

```

## Failure Analysis

The experiment stores model disagreements, retrieval misses, or policy-risk examples in the result JSON/CSV files when available. These examples are intentionally kept as previews or structured metadata where the source data can contain unsafe or sensitive text.

## Limitations

- Smoke mode prioritizes reproducibility and runtime over leaderboard-scale performance.
- Raw datasets are downloaded to `data/raw/` and are not committed.
- Metrics should be interpreted as portfolio research baselines, not production claims.
