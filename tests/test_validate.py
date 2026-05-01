from open_model_benchmark_cards.validate import validate_result


def test_validate_result():
    assert validate_result({"model": "m", "task": "t", "metrics": {}, "repro_command": "run"}) == []
    assert "missing:model" in validate_result({"task": "t", "metrics": {}, "repro_command": "run"})
