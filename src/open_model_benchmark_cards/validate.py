from __future__ import annotations


REQUIRED = {"model", "task", "metrics", "repro_command"}


def validate_result(result: dict) -> list[str]:
    errors = [f"missing:{key}" for key in sorted(REQUIRED - result.keys())]
    if "metrics" in result and not isinstance(result["metrics"], dict):
        errors.append("metrics:not_object")
    return errors
