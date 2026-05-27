#!/usr/bin/env python3
"""Block Edit/Write/MultiEdit/NotebookEdit on anything under docs/.

See CLAUDE.md "Never modify anything under docs/" convention.
Exit 2 with stderr message tells Claude Code to block the tool call.
"""
import json
import os
import sys


def main() -> int:
    project_root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    ti = payload.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("notebook_path")
    if not path:
        return 0

    abs_path = os.path.abspath(
        path if os.path.isabs(path) else os.path.join(project_root, path)
    )
    docs = os.path.abspath(os.path.join(project_root, "docs"))

    if abs_path == docs or abs_path.startswith(docs + os.sep):
        sys.stderr.write(
            f"Blocked: '{path}' is under docs/ — upstream-pinned, read-only "
            "per CLAUDE.md.\nIf a real fix is needed, send a PR upstream "
            "instead of editing here.\n"
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
