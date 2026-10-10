# InputWindowsMetricsCustom

Custom host metric collection settings.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `system`                                                                               | [Optional[models.InputWindowsMetricsSystem]](../models/inputwindowsmetricssystem.md)   | :heavy_minus_sign:                                                                     | Select the level of details for system metrics                                         |
| `cpu`                                                                                  | [Optional[models.InputWindowsMetricsCPU]](../models/inputwindowsmetricscpu.md)         | :heavy_minus_sign:                                                                     | Select the level of details for CPU metrics                                            |
| `memory`                                                                               | [Optional[models.InputWindowsMetricsMemory]](../models/inputwindowsmetricsmemory.md)   | :heavy_minus_sign:                                                                     | Select the level of details for memory metrics                                         |
| `network`                                                                              | [Optional[models.InputWindowsMetricsNetwork]](../models/inputwindowsmetricsnetwork.md) | :heavy_minus_sign:                                                                     | Select the level of details for network metrics                                        |
| `disk`                                                                                 | [Optional[models.InputWindowsMetricsDisk]](../models/inputwindowsmetricsdisk.md)       | :heavy_minus_sign:                                                                     | Select the level of details for disk metrics                                           |