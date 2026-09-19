# LabelFields2

Label configuration that reads values from a list of fields.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `mode`                                                                                       | [models.PipelineFunctionMetricsExportMode2](../models/pipelinefunctionmetricsexportmode2.md) | :heavy_check_mark:                                                                           | Type of label configuration. Always <code>list</code>.                                       |
| `fields`                                                                                     | List[[models.NameFieldType](../models/namefieldtype.md)]                                     | :heavy_check_mark:                                                                           | Field references to attach as labels to each exported metric.                                |