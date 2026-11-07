"""Execution runtime for Zephyr Lite."""

import time
from typing import Iterable


class Runtime:
    def __init__(self, workspace: str, dry_run: bool = False):
        self.workspace = workspace
        self.dry_run = dry_run
        self.started_at = None

    def run(self, pipeline: dict) -> dict:
        self.started_at = time.time()
        results = []
        for step in pipeline.get("steps", []):
            if self.dry_run:
                results.append({"step": step, "status": "skipped"})
            else:
                results.append({"step": step, "status": "ok"})
        return {"workspace": self.workspace, "results": results}

    def elapsed(self) -> float:
        if self.started_at is None:
            return 0.0
        return time.time() - self.started_at
