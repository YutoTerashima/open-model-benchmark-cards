from __future__ import annotations


REQUIRED_FIELDS = {"model": str, "task": str, "metrics": dict, "repro_command": str}


def schema_report(result: dict) -> list[str]:
    errors = []
    for key, typ in REQUIRED_FIELDS.items():
        if key not in result:
            errors.append(f"missing:{key}")
        elif not isinstance(result[key], typ):
            errors.append(f"type:{key}:{typ.__name__}")
    return errors
