from __future__ import annotations

import argparse
import json
from pathlib import Path

from .card import render_card
from .compare import comparison_table
from .validate import validate_result


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate model benchmark cards.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--metric", default=None)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if isinstance(data, list):
        metric = args.metric or next(iter(data[0]["metrics"]))
        print(comparison_table(data, metric))
        return
    errors = validate_result(data)
    if errors:
        raise SystemExit("; ".join(errors))
    print(render_card(data))


if __name__ == "__main__":
    main()
