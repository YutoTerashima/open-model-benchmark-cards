from open_model_benchmark_cards.schema import schema_report


def test_schema_report():
    assert not schema_report({"model": "m", "task": "t", "metrics": {}, "repro_command": "run"})
    assert "missing:model" in schema_report({"task": "t", "metrics": {}, "repro_command": "run"})
