# Real Benchmark Card Input Analysis

Source: [aizip/Rag-Eval-Dataset-6k](https://huggingface.co/datasets/aizip/Rag-Eval-Dataset-6k)

This project now includes real benchmark-card inputs derived from a public RAG evaluation dataset.
The card records task definition, source dataset, source URL, metric names, and limitations.

- Baseline: bm25-lexical-retriever-baseline
- Average question/context overlap: 0.625
- Average contexts per case: 3.758

The Open LLM Leaderboard adapter remains implemented as a reproducible extension path, but this
checked-in artifact avoids inventing model scores while the external API is rate-limited.
