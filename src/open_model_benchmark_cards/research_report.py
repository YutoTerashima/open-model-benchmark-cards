from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'Open Model Benchmark Cards'
RESEARCH_PROBLEM = 'How can benchmark claims become auditable cards with reproducibility metadata and limitations?'
DATASET_SUMMARY = 'Experiment indexes from the other 8 V2 repositories converted into benchmark-card records.'
TAKEAWAYS = ['Every upstream repo now has a generated benchmark card and completeness score.', 'Cards link claims to artifacts rather than relying on prose.', 'The repo provides a cross-project reproducibility index for the portfolio.']
NEXT_EXPERIMENTS = ['Add stricter limitation-quality checks.', 'Add markdown rendering tests for every generated card.', 'Optionally ingest external Open LLM leaderboard data when stable.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
