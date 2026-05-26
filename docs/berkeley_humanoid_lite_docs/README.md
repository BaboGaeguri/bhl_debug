# Berkeley Humanoid Lite Docs — Local Mirror

This directory is a local mirror of the documentation site at
<https://berkeley-humanoid-lite.gitbook.io/docs> (snapshot taken 2026-05-27).

- **Project**: Berkeley Humanoid Lite — open-source sub-$5,000 humanoid robot
- **Project site**: <https://lite.berkeley-humanoid.org/>
- **Source code**: <https://github.com/HybridRobotics/Berkeley-Humanoid-Lite>
- **Paper (arXiv)**: <https://arxiv.org/abs/2504.17249>

## How this mirror was made

GitBook exposes each page as a portable Markdown export via the
`<page>.md` URL pattern, and the rendered HTML embeds each image
through a signed `~gitbook/image` proxy. This mirror was assembled by:

1. Enumerating pages from the site's `sitemap-pages.xml`.
2. Downloading each page's `.md` export.
3. Parsing each rendered HTML page to resolve every `/files/<id>`
   reference to its underlying asset URL, then saving those assets
   under `_assets/`.
4. Rewriting `<img src="/files/<id>">` references in the Markdown to
   point at the local `_assets/<id>.<ext>` files.

## Caveats

- No explicit license is published on the GitBook. Treat this mirror
  as a personal/study snapshot — consult the upstream project before
  redistributing.
- The mirror is a point-in-time copy. For the latest version, always
  refer back to the original site.

## Page index

### Top level
- [Home](home.md)
- [Releases](releases.md)
- [lerobot Integration](lerobot-integration.md)
- [Contribute](contribute.md)

### Getting Started with Hardware
- [Overview](getting-started-with-hardware.md)
- [Materials and Parts (BOM)](getting-started-with-hardware/materials-and-parts-bom.md)
- [Preparing the Tools](getting-started-with-hardware/preparing-the-tools.md)
- [3D Printing Instructions](getting-started-with-hardware/3d-printing-instructions.md)
- [Building the Actuator](getting-started-with-hardware/building-the-actuator.md)
- [Flashing the Motor Controllers](getting-started-with-hardware/flashing-the-motor-controllers.md)
- [Building the Robot](getting-started-with-hardware/building-the-robot.md)

### Getting Started with Software
- [Overview](getting-started-with-software.md)
- [Software Development Environment Overview](getting-started-with-software/software-development-environment-overview.md)
- [Training Environment](getting-started-with-software/training-environment.md)
- [Sim2sim Validation](getting-started-with-software/sim2sim-validation.md)
- [The On-board Computer](getting-started-with-software/the-on-board-computer.md)
- [Motion Capture System](getting-started-with-software/motion-capture-system.md)

### In-depth Contents
- [Overview](in-depth-contents.md)
- [Field Oriented Control (FOC) Operation](in-depth-contents/field-oriented-control-foc-operation.md)
- [Motor Controller Firmware Execution Timing Information](in-depth-contents/motor-controller-firmware-execution-timing-information.md)
- [Motor Characterization](in-depth-contents/motor-characterization.md)
- [IMU Comparision](in-depth-contents/imu-comparision.md)
- [CAN Communication](in-depth-contents/can-communication.md)
- [Joint ID Mapping](in-depth-contents/joint-id-mapping.md)
- [Exporting Robot Description Files from Onshape](in-depth-contents/exporting-robot-description-files-from-onshape.md)
- [Training Environment Coding Convention](in-depth-contents/training-environment-coding-convention.md)
- [Syncing Files From Training Server](in-depth-contents/syncing-files-from-training-server.md)
