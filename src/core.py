"""Core primitives for Zephyr Lite."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Config:
    name: str
    plugins: List[str] = field(default_factory=list)
    options: Dict[str, Any] = field(default_factory=dict)


def load_config(payload: Dict[str, Any]) -> Config:
    if not payload.get("name"):
        raise ValueError("configuration requires a name")
    return Config(
        name=payload["name"],
        plugins=list(payload.get("plugins", [])),
        options=dict(payload.get("options", {})),
    )


def build_pipeline(config: Config, steps: Optional[List[str]] = None):
        steps = steps or []
        resolved = [f"{config.name}.{step}" for step in steps]
        return {"config": config, "steps": resolved}
