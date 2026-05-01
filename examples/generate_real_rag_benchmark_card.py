import json
from pathlib import Path

rows = json.loads(Path("datasets/external/real_benchmark_card_inputs.json").read_text(encoding="utf-8"))
row = rows[0]
lines = [
    f"# {row['model_name']}",
    "",
    f"Task: {row['task']}",
    f"Source: {row['source_url']}",
    "",
    "## Metrics",
]
for key, value in row["metrics"].items():
    lines.append(f"- {key}: {value}")
lines.extend(["", "## Limitations", *[f"- {item}" for item in row["limitations"]]])
Path("reports/real_rag_benchmark_card.md").write_text("\n".join(lines), encoding="utf-8")
print("reports/real_rag_benchmark_card.md")
