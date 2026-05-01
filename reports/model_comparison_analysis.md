# Model Comparison Analysis

The benchmark-card generator supports model comparison tables in addition to
single-model cards.

| model | accuracy | refusal_precision | cost_class |
| --- | --- | --- | --- |
| open-model-a | 0.82 | 0.91 | local |
| open-model-b | 0.78 | 0.87 | local |
| open-model-c | 0.84 | 0.83 | api |

## Interpretation

The best model depends on the target metric. `open-model-c` has the strongest
accuracy in this sample, while `open-model-a` has better refusal precision and a
local cost profile.
