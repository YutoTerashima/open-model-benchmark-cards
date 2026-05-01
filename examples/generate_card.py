from pathlib import Path

from open_model_benchmark_cards.card import render_card


result = {
    "model": "gpt-oss-20b",
    "task": "Mock safety and reasoning eval",
    "metrics": {"accuracy": "0.82", "refusal_precision": "0.91"},
    "repro_command": "python run_eval.py --model gpt-oss-20b --mock",
    "limitations": ["Mock data only", "No private benchmark prompts"],
}

if __name__ == "__main__":
    out = Path("reports/gpt-oss-20b-card.md")
    out.parent.mkdir(exist_ok=True)
    out.write_text(render_card(result), encoding="utf-8")
    print(out)
