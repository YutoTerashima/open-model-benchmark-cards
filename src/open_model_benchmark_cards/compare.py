from __future__ import annotations


def rank_models(results: list[dict], metric: str) -> list[dict]:
    return sorted(results, key=lambda item: float(item["metrics"].get(metric, 0)), reverse=True)


def comparison_table(results: list[dict], metric: str) -> str:
    rows = [f"| {item['model']} | {item['metrics'].get(metric, 'n/a')} |" for item in rank_models(results, metric)]
    return "\n".join(["| Model | " + metric + " |", "| --- | ---: |", *rows])
