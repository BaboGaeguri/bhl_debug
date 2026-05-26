# 3D Printing Instructions

## Files

Please refer to the Releases page for the latest release of CAD model and 3D printing project files.

{% content-ref url="/pages/ReTulzQ4ECBUQPnquXTq" %}
[Releases](/docs/releases.md)
{% endcontent-ref %}

## Print settings

The following parameters are tuned for the Bambu Lab X1C 3D Printer. Additional modifications might be required to fit your own printer's characteristics.

## Printing the actuator

### Actuator Housing Profile

For the housing, output shaft, and the motor shell, the Actuator Housing Profile should be used.

<figure><img src="../_assets/2VFIkkK2XUlEeXTKzfrX.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Quality" %}

<figure><img src="../_assets/rfbufYaAydccHvUywk6B.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Strength" %}

<figure><img src="../_assets/6zx1jVucFkit12BQdr2d.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Speed" %}

<figure><img src="../_assets/rMsP7h3jGnVmfOdO8OGW.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Support" %}

<figure><img src="../_assets/xRzcr2uTocV0BPAbehR7.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Others" %}

<figure><img src="../_assets/E3wDeMNK22H3KEi8hoEU.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Actuator Shaft Profile

For the cycloidal disk, input shaft, motor shaft, and the spacers, the Actuator Shaft Profile should be used.

<figure><img src="../_assets/7oExDT57NpSkpAysuVwV.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Quality" %}

<figure><img src="../_assets/HfS6iGyyUQAdkn41NWQp.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Strength" %}

<figure><img src="../_assets/z1LBd6TXQEGnIhQTgSen.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Speed" %}

<figure><img src="../_assets/QGKi4leW3yhm0H0MA5TT.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Support" %}

<figure><img src="../_assets/f9UnDc5vVQOB2rrAi5eL.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Others" %}

<figure><img src="../_assets/k7oJQpBXldMqrAgqZgA4.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Printing the rest of the robot

Similar principle applies to the rest of the robot.&#x20;

<figure><img src="../_assets/ExpHvs9Sud9hsxo3K1kP.png" alt=""><figcaption></figcaption></figure>

Parts on the Upper Body and Lower Body plates need to be printed twice in mirrored setting to assemble the two arms and two legs. This can be achieved by right-clicking the part and selet "mirror along X axis".

The structural parts does not require the high precision as the actuator modules, so they can be printed at a faster speed setting.


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://berkeley-humanoid-lite.gitbook.io/docs/getting-started-with-hardware/3d-printing-instructions.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
