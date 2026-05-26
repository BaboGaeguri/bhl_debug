# IMU Comparision

In this page we list the performance characteristics of the BNO085 IMU, which we originally used, and the IM10A IMU, which is the upgraded one that already provides USB interface.

| Parameter                                         | Unit          | BNO085    | IM10A         |
| ------------------------------------------------- | ------------- | --------- | ------------- |
| <mark style="color:red;">**Accelerometer**</mark> |               |           |               |
| Range                                             | g             | ±16       | ± 16          |
| Resolution                                        | mg / LSB      | 1         | 0.5           |
| RMS Noise                                         | mg            | 0.16      | 0.75 \~ 1     |
| Static Zero Drift                                 | mg            | ± 150     | ± 20 \~ 40    |
| Bandwidth                                         | Hz            | 8 \~ 1000 | 5 \~ 256      |
| <mark style="color:green;">**Gyroscope**</mark>   |               |           |               |
| Range                                             | °/s           | ± 2000    | ± 2000        |
| Resolution                                        | (°/s) / (LSB) | 0.0625    | 0.061         |
| RMS Noise                                         | °/s           | 0.014     | 0.028 \~ 0.07 |
| Static Zero Drift                                 | °/s           | ± 1       | ± 0.5 \~ 1    |
| Bandwidth                                         | Hz            | 12 \~ 523 | 5 \~ 256      |
| <mark style="color:blue;">**Magnetometer**</mark> |               |           |               |
| Range                                             | Gauss         | ± 13      | ± 2           |
| Resolution                                        | Gauss / LSB   | 0.003     | 0.0667        |


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://berkeley-humanoid-lite.gitbook.io/docs/in-depth-contents/imu-comparision.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
