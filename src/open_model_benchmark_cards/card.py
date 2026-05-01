from __future__ import annotations


def render_card(result: dict) -> str:
    metrics = "\n".join(f"| {name} | {value} |" for name, value in result["metrics"].items())
    limits = "\n".join(f"- {item}" for item in result.get("limitations", []))
    return f"""# {result['model']} Benchmark Card

## Task

{result['task']}

## Metrics

| Metric | Value |
| --- | --- |
{metrics}

## Reproduction

```bash
{result['repro_command']}
```

## Limitations

{limits}
"""
