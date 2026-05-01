from open_model_benchmark_cards.compare import comparison_table, rank_models


def test_rank_models():
    results = [{"model": "a", "metrics": {"acc": 0.7}}, {"model": "b", "metrics": {"acc": 0.9}}]
    assert rank_models(results, "acc")[0]["model"] == "b"
    assert "| b | 0.9 |" in comparison_table(results, "acc")
