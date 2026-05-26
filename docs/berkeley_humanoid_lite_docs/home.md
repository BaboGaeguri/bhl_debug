# Home

[**Website**](https://lite.berkeley-humanoid.org/) | [**arXiv**](https://arxiv.org/abs/2504.17249) | [**Paper**](https://lite.berkeley-humanoid.org/static/paper/demonstrating-berkeley-humanoid-lite.pdf) | [**Video**](https://youtu.be/5qgEJpEf3pQ) | [**Documentation**](/docs/home.md) | [**Code**](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)

**Berkeley Humanoid Lite** is an open-source, sub-$5,000 humanoid robot featuring modular 3D-printed gearboxes and widely available components, designed to democratize and advance humanoid robotics research.

This website contains documentation on helping you build your own version of the robot and setting up the corresponding software environment to perform locomotion and teleoperated manipulation on the robot.

During the development of the robot, we encountered numerous bugs and challenges. In the *In-depth Contents* section, we document our effort of understanding the system and the steps we took to resolve these problems. We hope this serves as a valuable resource for the community.

If you have any questions or comments, please reach out to us by either [creating a Github Issue](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite/issues/new) or joining our community!

{% hint style="info" %}

## ⚠ <mark style="color:red;">**WARNING**</mark>

This is not just a software project. It includes designs for high power electronics. It has not yet burned down any UC Berkeley labs or anyone's houses, but there are no guarantees : )\
Please follow all steps with extra caution.
{% endhint %}


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://berkeley-humanoid-lite.gitbook.io/docs/home.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
