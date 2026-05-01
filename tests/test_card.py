from open_model_benchmark_cards.card import render_card


def test_card_contains_metrics():
    card = render_card({"model": "m", "task": "t", "metrics": {"acc": 1}, "repro_command": "run", "limitations": []})
    assert "| acc | 1 |" in card
    assert "```bash" in card
