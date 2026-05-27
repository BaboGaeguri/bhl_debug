# bhl_debug

Self-contained debugging workspace for **Berkeley Humanoid Lite (BHL)** — an open-source sub-$5,000 humanoid robot from HybridRobotics (UC Berkeley). Upstream code, firmware, vendor manuals, and a snapshot of the official docs are pinned under `docs/`.

## Where things live

All BHL reference material lives under `docs/`. Read **`docs/README.md`** for the full map and intent-based navigation. Quick orientation:

- `docs/Berkeley-Humanoid-Lite/` — main code (with nested `Assets` + `Lowlevel` submodules)
- `docs/Recoil-Motor-Controller-BESC/` — motor controller firmware (STM32G431CB)
- `docs/SteamVR-Bridge/` — VR teleoperation bridge
- `docs/hardware_manuals/` — CANable submodule + ST B-G431B-ESC1 PDFs
- `docs/berkeley_humanoid_lite_docs/` — gitbook docs mirror (snapshot 2026-05-27)
- `docs/paper/` — arXiv:2504.17249 PDF

## Live documentation (MCP)

The `berkeley-humanoid-lite-docs` MCP server provides live search/fetch of the upstream gitbook:

- `mcp__berkeley-humanoid-lite-docs__searchDocumentation` — keyword search
- `mcp__berkeley-humanoid-lite-docs__getPage` — fetch by URL

Use these when checking for content newer than the 2026-05-27 mirror snapshot.

## Conventions

- **Never modify anything under `docs/`.** Everything in `docs/` is upstream-pinned (submodules, vendor PDFs, gitbook mirror, paper) and is treated as read-only reference material. Do not `Edit`, `Write`, or `rm` files there, and do not run formatters, linters, or codemods that would touch them. If a fix is genuinely needed in upstream code, it becomes a PR against the upstream repo — not a local edit here.
- **Answering user questions: search `docs/` first.** When the user asks something and you are not certain of the answer, first explore the `docs/` tree (submodule code, gitbook mirror, paper, vendor manuals) for the answer. Answer from what you find there. If nothing in `docs/` covers it, **ask the user for permission before running `WebSearch`** — do not silently fall back to the web.
- **Default to local content first.** The local mirror + submodules cover all five officially-listed BHL repos. Reach for `WebSearch` only when the MCP and local files don't have what you need, and only after the user authorizes it per the rule above.
- **Nested submodule URLs are SSH upstream**, overridden to HTTPS in local `.git/config`. Do not edit upstream `.gitmodules` files to "fix" this — keep the override local so the submodule working trees stay clean.
- **Don't reach for CAD/3D-print files in-repo** — they are inherently external (Onshape, MakerWorld). Link out instead.
- **Build commands**: BHL Lowlevel uses `make build` / `make run` (CMake wrapper). Python projects use `uv`.
- This repo is a *reference workspace*, not the upstream itself. Code changes to upstream files should usually become PRs against the upstream repos, not commits here.

## External (not mirrored)

- Project site: <https://lite.berkeley-humanoid.org/>
- Onshape CAD (4 models), MakerWorld 3D-print files (3 models), demo video on YouTube
