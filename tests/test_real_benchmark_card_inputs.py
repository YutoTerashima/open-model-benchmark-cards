import json
from pathlib import Path


def test_real_benchmark_card_inputs_include_source_and_metrics():
    rows = json.loads(Path("datasets/external/real_benchmark_card_inputs.json").read_text(encoding="utf-8"))
    assert rows
    row = rows[0]
    assert row["source_dataset"] == "aizip/Rag-Eval-Dataset-6k"
    assert row["metrics"]
    assert row["source_url"].startswith("https://huggingface.co/datasets/")
