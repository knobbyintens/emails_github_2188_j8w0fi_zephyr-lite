from src.core import load_config, build_pipeline
from src.runtime import Runtime


def test_runtime_dry_run_marks_steps_as_skipped():
    config = load_config({"name": "demo"})
    pipeline = build_pipeline(config, ["one"])
    result = Runtime("/tmp", dry_run=True).run(pipeline)
    assert result["results"][0]["status"] == "skipped"
