import os
import pytest


@pytest.mark.smoke
def test_runtime_environment_variable():
    current_env = os.environ.get("TEST_ENV", "local")
    print(f"\nRunning inside container with TEST_ENV={current_env}")
    assert current_env in ["local", "dev", "staging", "prod"]


@pytest.mark.regression
def test_regression_env_config_format():
    current_env = os.environ.get("TEST_ENV", "local").strip().lower()
    assert len(current_env) > 0
