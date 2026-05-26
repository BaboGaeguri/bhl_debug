# Software Development Environment Overview

## Directory walkthrough

The [HybridRobotics/Berkeley-Humanoid-Lite](https://github.com/hybridrobotics/berkeley-humanoid-lite) repository will be our working directory for everything.&#x20;

Inside the directory, there are three packages:

`source/berkeley_humanoid_lite/` contains the IsaacLab environment and task definitions.

`source/berkeley_humanoid_lite_assets/` contains robot descriptions (URDF, MJCF, and USD) and the script to export these description files from Onshape project.

`source/berkeley_humanoid_lite_lowlevel/` contains the lowlevel code running on the real robot. Only contents inside this folder is required to copy to the robot. We will cover that part in a later section.

## Code Editor

We recommend using [Cursor](https://www.cursor.com/en) / [VisualStudio Code](https://code.visualstudio.com/) as the editor.


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://berkeley-humanoid-lite.gitbook.io/docs/getting-started-with-software/software-development-environment-overview.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
