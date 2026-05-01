# gpt-oss-20b Benchmark Card

## Task

Mock safety and reasoning eval

## Metrics

| Metric | Value |
| --- | --- |
| accuracy | 0.82 |
| refusal_precision | 0.91 |

## Reproduction

```bash
python run_eval.py --model gpt-oss-20b --mock
```

## Limitations

- Mock data only
- No private benchmark prompts
