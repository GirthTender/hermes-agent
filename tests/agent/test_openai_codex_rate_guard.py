"""Tests for OpenAI Codex OAuth usage-limit guard."""

import json
import os
import time

import pytest


@pytest.fixture
def codex_rate_guard_env(tmp_path, monkeypatch):
    hermes_home = str(tmp_path / ".hermes")
    os.makedirs(hermes_home, exist_ok=True)
    monkeypatch.setenv("HERMES_HOME", hermes_home)
    return hermes_home


class TestOpenAICodexRateGuard:
    def test_detects_usage_limit_context(self):
        from agent.openai_codex_rate_guard import is_codex_usage_limit

        assert is_codex_usage_limit({
            "reason": "usage_limit_reached",
            "message": "The usage limit has been reached",
        })
        assert not is_codex_usage_limit({"message": "Too many requests"})

    def test_records_with_resets_in_seconds(self, codex_rate_guard_env):
        from agent.openai_codex_rate_guard import (
            _state_path,
            record_openai_codex_rate_limit,
        )

        record_openai_codex_rate_limit(
            error_context={
                "reason": "usage_limit_reached",
                "plan_type": "plus",
                "resets_in_seconds": 900,
            }
        )

        with open(_state_path(), encoding="utf-8") as f:
            state = json.load(f)
        assert state["provider"] == "openai-codex"
        assert state["reason"] == "usage_limit_reached"
        assert state["plan_type"] == "plus"
        assert state["reset_seconds"] == pytest.approx(900, abs=2)

    def test_remaining_expires_and_cleans_state(self, codex_rate_guard_env):
        from agent.openai_codex_rate_guard import (
            _state_path,
            openai_codex_rate_limit_remaining,
        )

        path = _state_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"reset_at": time.time() - 1}, f)

        assert openai_codex_rate_limit_remaining() is None
        assert not os.path.exists(path)


class TestCodexErrorContextExtraction:
    def test_extracts_response_json_usage_limit_fields(self):
        from agent.agent_runtime_helpers import extract_api_error_context

        class Response:
            headers = {"retry-after": "120"}

            @staticmethod
            def json():
                return {
                    "error": {
                        "type": "usage_limit_reached",
                        "message": "The usage limit has been reached",
                        "plan_type": "plus",
                        "resets_in_seconds": 600,
                    }
                }

        class APIError(Exception):
            response = Response()

        context = extract_api_error_context(APIError("HTTP 429"))

        assert context["reason"] == "usage_limit_reached"
        assert context["message"] == "The usage limit has been reached"
        assert context["plan_type"] == "plus"
        assert context["resets_in_seconds"] == 600
        assert context["reset_at"] > time.time()
