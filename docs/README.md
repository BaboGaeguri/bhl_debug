# docs/ — Berkeley Humanoid Lite Reference Tree

Self-contained reference for debugging the Berkeley Humanoid Lite (BHL) hardware/software stack. Everything here can be read offline; the only optional online dependency is the MCP server for live docs queries.

## Map

```
docs/
├── Berkeley-Humanoid-Lite/              [submodule, upstream HybridRobotics/Berkeley-Humanoid-Lite]
│   ├── source/berkeley_humanoid_lite/           IsaacLab environment + task definitions
│   ├── source/berkeley_humanoid_lite_assets/    [nested submodule] URDF/MJCF/USD + Onshape export
│   ├── source/berkeley_humanoid_lite_lowlevel/  [nested submodule] on-robot low-level control
│   ├── scripts/                                 entry points for all flows
│   ├── docker/                                  containerization
│   └── motor_configuration.json                 joint actuator map
│
├── Recoil-Motor-Controller-BESC/        [submodule, T-K-233/Recoil-Motor-Controller-BESC]
│   └── motor controller firmware (B-G431B-ESC1, STM32G431CB)
│
├── SteamVR-Bridge/                      [submodule, ucb-bar/SteamVR-Bridge]
│   └── Windows SteamVR → UDP teleoperation bridge
│
├── hardware_manuals/
│   ├── canable/                         [submodule @ b5c7a39, makerbase-mks/CANable-MKS]
│   │   └── Makerbase USB-CAN adapter HW + firmware + manuals
│   └── BESC/                            ST B-G431B-ESC1 datasheets and UM2516 user manual
│
├── berkeley_humanoid_lite_docs/         local mirror of the gitbook site (snapshot 2026-05-27)
│   ├── getting-started-with-hardware/   BOM, tools, 3D printing, actuator/robot assembly
│   ├── getting-started-with-software/   dev env, training, sim2sim, on-board computer, mocap
│   ├── in-depth-contents/               FOC, firmware timing, IMU, CAN, joint IDs, Onshape export
│   └── _assets/                         62 inline images (PNG/JPG)
│
└── paper/
    └── demonstrating-berkeley-humanoid-lite.pdf    arXiv:2504.17249, downloaded for offline use
```

## Navigate by intent

| If you're working on... | Start here |
|---|---|
| RL training / policy | `Berkeley-Humanoid-Lite/source/berkeley_humanoid_lite/`, `scripts/`, docs `getting-started-with-software/training-environment.md` |
| Sim2sim validation | docs `getting-started-with-software/sim2sim-validation.md`, `scripts/` |
| URDF/MJCF/USD generation | `Berkeley-Humanoid-Lite/source/berkeley_humanoid_lite_assets/`, docs `in-depth-contents/exporting-robot-description-files-from-onshape.md` |
| On-robot deploy / CAN / IMU | `Berkeley-Humanoid-Lite/source/berkeley_humanoid_lite_lowlevel/`, docs `in-depth-contents/can-communication.md`, `imu-comparision.md` |
| Motor controller firmware | `Recoil-Motor-Controller-BESC/`, docs `in-depth-contents/field-oriented-control-foc-operation.md`, `motor-controller-firmware-execution-timing-information.md` |
| Joint ID / wiring / BOM | docs `in-depth-contents/joint-id-mapping.md`, `getting-started-with-hardware/materials-and-parts-bom.md` |
| Teleoperation (VR) | `SteamVR-Bridge/`, docs `getting-started-with-hardware/building-the-robot.md` |
| Vendor hardware spec | `hardware_manuals/` (CANable, B-G431B-ESC1) |
| Paper / methodology | `paper/demonstrating-berkeley-humanoid-lite.pdf` |

## Submodule pins

| Path | Pinned revision |
|---|---|
| `Berkeley-Humanoid-Lite` | `984741a` (v1.1.0-4) |
| `Berkeley-Humanoid-Lite/source/.../assets` | `fc90fed` (v2025.09.03-1) |
| `Berkeley-Humanoid-Lite/source/.../lowlevel` | `652777c` |
| `Recoil-Motor-Controller-BESC` | `3571ab6` |
| `SteamVR-Bridge` | `3c254a6` |
| `hardware_manuals/canable` | `b5c7a39` |

## Live documentation (MCP)

The `berkeley-humanoid-lite-docs` MCP server provides live access to the upstream gitbook documentation:

- `mcp__berkeley-humanoid-lite-docs__searchDocumentation` — keyword search
- `mcp__berkeley-humanoid-lite-docs__getPage` — fetch a page by URL

Use these when the local mirror (`berkeley_humanoid_lite_docs/`, snapshot 2026-05-27) may be stale.

## External resources (not mirrored here)

Linked from official docs but hosted on third-party platforms:

- **Onshape CAD**: main robot, 6512 actuator, 5010 actuator, USB-CAN adapter case
- **MakerWorld 3D-print files**: main robot, 6512 actuator, 5010 actuator
- **Project site**: <https://lite.berkeley-humanoid.org/>
- **Video**: <https://youtu.be/dIdJGkMDFl4>

## Conventions

- Nested submodules under `Berkeley-Humanoid-Lite` use SSH URLs upstream; locally they are overridden to HTTPS via `.git/config` so the working tree stays clean. Mirror that override when recloning.
- Each gitbook page supports `?ask=<question>` for dynamic Q&A; the MCP tools wrap this.
- CAD and 3D-print files are NOT in this repo — link out to Onshape/MakerWorld.
