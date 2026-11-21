# LabelFields1

Label configuration that reads key-value pairs from one object field.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `mode`                                                                                       | [models.PipelineFunctionMetricsExportMode1](../models/pipelinefunctionmetricsexportmode1.md) | :heavy_check_mark:                                                                           | Type of label configuration. Always <code>object</code>.                                     |
| `field`                                                                                      | [models.NameFieldType](../models/namefieldtype.md)                                           | :heavy_check_mark:                                                                           | Reference to a field by its original text and parsed path segments.                          |