import pytest

from src.core import load_config, build_pipeline


def test_load_config_requires_name():
    with pytest.raises(ValueError):
        load_config({})


def test_build_pipeline_prefixes_steps():
    config = load_config({"name": "demo", "plugins": ["io"]})
    pipeline = build_pipeline(config, ["prepare", "write"])
    assert pipeline["steps"] == ["demo.prepare", "demo.write"]
