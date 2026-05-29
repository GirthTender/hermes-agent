"""Kanban worker lifecycle tool-surface hardening tests."""


def _tool_names(enabled_toolsets):
    from model_tools import _clear_tool_defs_cache, get_tool_definitions
    from tools.registry import invalidate_check_fn_cache

    invalidate_check_fn_cache()
    _clear_tool_defs_cache()
    return {
        tool["function"]["name"]
        for tool in get_tool_definitions(enabled_toolsets=enabled_toolsets, quiet_mode=True)
    }


def test_terminal_toolset_without_kanban_task_excludes_lifecycle_tools(monkeypatch):
    from model_tools import _clear_tool_defs_cache

    monkeypatch.delenv("HERMES_KANBAN_TASK", raising=False)
    monkeypatch.delenv("HERMES_KANBAN_RUN_ID", raising=False)
    _clear_tool_defs_cache()

    names = _tool_names(["terminal"])

    assert "terminal" in names
    assert "kanban_complete" not in names
    assert "kanban_block" not in names
    assert "kanban_heartbeat" not in names


def test_terminal_toolset_with_kanban_task_includes_lifecycle_tools(monkeypatch):
    from model_tools import _clear_tool_defs_cache

    monkeypatch.setenv("HERMES_KANBAN_TASK", "task-worker-1")
    _clear_tool_defs_cache()

    names = _tool_names(["terminal"])

    assert "terminal" in names
    assert {"kanban_complete", "kanban_block", "kanban_heartbeat"}.issubset(names)
