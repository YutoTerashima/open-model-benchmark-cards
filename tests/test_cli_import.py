from open_model_benchmark_cards.cli import main


def test_cli_importable():
    assert callable(main)
