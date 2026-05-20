"""Cross-session usage-limit guard for OpenAI Codex OAuth.

OpenAI Codex OAuth usage caps are account/plan scoped. When the provider
returns a usage-limit 429 with a reset window, retrying from other gateway
sessions only amplifies the failure. This guard records the reset window in a
shared file so all Hermes sessions can skip Codex until the cap resets and use
configured fallbacks instead.
"""

from __future__ import annotations

import json
import logging
import os
import tempfile
import time
from typing import Any, Mapping, Optional
from utils import atomic_replace

logger = logging.getLogger(__name__)

_STATE_SUBDIR = "rate_limits"
_STATE_FILENAME = "openai-codex.json"


def _state_path() -> str:
    try:
        from hermes_constants import get_hermes_home
        base = get_hermes_home()
    except ImportError:
        base = os.path.join(os.path.expanduser("~"), ".hermes")
    return os.path.join(base, _STATE_SUBDIR, _STATE_FILENAME)


def _parse_reset_seconds(headers: Optional[Mapping[str, str]]) -> Optional[float]:
    if not headers:
        return None
    lowered = {str(k).lower(): v for k, v in headers.items()}
    for key in (
        "retry-after",
        "x-ratelimit-reset",
        "x-ratelimit-reset-requests",
        "x-ratelimit-reset-tokens",
    ):
        raw = lowered.get(key)
        if raw is None:
            continue
        try:
            val = float(raw)
            if val > 0:
                return val
        except (TypeError, ValueError):
            pass
    return None


def is_codex_usage_limit(error_context: Optional[dict[str, Any]] = None) -> bool:
    if not isinstance(error_context, dict):
        return False
    reason = str(error_context.get("reason") or "").lower()
    message = str(error_context.get("message") or "").lower()
    return (
        "usage_limit_reached" in reason
        or "usage limit has been reached" in message
        or ("usage limit" in message and "reset" in message)
    )


def record_openai_codex_rate_limit(
    *,
    headers: Optional[Mapping[str, str]] = None,
    error_context: Optional[dict[str, Any]] = None,
    default_cooldown: float = 300.0,
) -> None:
    now = time.time()
    reset_at = None

    header_seconds = _parse_reset_seconds(headers)
    if header_seconds is not None:
        reset_at = now + header_seconds

    if reset_at is None and isinstance(error_context, dict):
        resets_in = error_context.get("resets_in_seconds")
        if isinstance(resets_in, (int, float)) and resets_in > 0:
            reset_at = now + float(resets_in)

    if reset_at is None and isinstance(error_context, dict):
        ctx_reset = error_context.get("reset_at")
        if isinstance(ctx_reset, (int, float)) and ctx_reset > now:
            reset_at = float(ctx_reset)
        elif isinstance(ctx_reset, str):
            try:
                numeric = float(ctx_reset)
                reset_at = numeric if numeric > now else now + numeric
            except (TypeError, ValueError):
                pass

    if reset_at is None:
        reset_at = now + default_cooldown

    path = _state_path()
    try:
        state_dir = os.path.dirname(path)
        os.makedirs(state_dir, exist_ok=True)
        state = {
            "provider": "openai-codex",
            "reason": "usage_limit_reached" if is_codex_usage_limit(error_context) else "rate_limit",
            "plan_type": (error_context or {}).get("plan_type") if isinstance(error_context, dict) else None,
            "reset_at": reset_at,
            "recorded_at": now,
            "reset_seconds": reset_at - now,
        }
        fd, tmp_path = tempfile.mkstemp(dir=state_dir, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(state, f)
            atomic_replace(tmp_path, path)
        except Exception:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise
        logger.info(
            "OpenAI Codex rate limit recorded: reason=%s resets in %.0fs",
            state["reason"],
            reset_at - now,
        )
    except Exception as exc:
        logger.debug("Failed to write OpenAI Codex rate limit state: %s", exc)


def openai_codex_rate_limit_remaining() -> Optional[float]:
    path = _state_path()
    try:
        with open(path, encoding="utf-8") as f:
            state = json.load(f)
        reset_at = state.get("reset_at", 0)
        remaining = float(reset_at) - time.time()
        if remaining > 0:
            return remaining
        try:
            os.unlink(path)
        except OSError:
            pass
        return None
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return None


def clear_openai_codex_rate_limit() -> None:
    try:
        os.unlink(_state_path())
    except FileNotFoundError:
        pass
    except OSError as exc:
        logger.debug("Failed to clear OpenAI Codex rate limit state: %s", exc)


def format_remaining(seconds: float) -> str:
    s = max(0, int(seconds))
    if s < 60:
        return f"{s}s"
    if s < 3600:
        m, sec = divmod(s, 60)
        return f"{m}m {sec}s" if sec else f"{m}m"
    h, remainder = divmod(s, 3600)
    m = remainder // 60
    return f"{h}h {m}m" if m else f"{h}h"
