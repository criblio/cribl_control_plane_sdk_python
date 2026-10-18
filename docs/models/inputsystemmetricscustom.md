# InputSystemMetricsCustom

Custom host metric collection settings.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `system`                                                                             | [Optional[models.InputSystemMetricsSystem]](../models/inputsystemmetricssystem.md)   | :heavy_minus_sign:                                                                   | Select the level of detail for system metrics                                        |
| `cpu`                                                                                | [Optional[models.InputSystemMetricsCPU]](../models/inputsystemmetricscpu.md)         | :heavy_minus_sign:                                                                   | Select the level of detail for CPU metrics                                           |
| `memory`                                                                             | [Optional[models.InputSystemMetricsMemory]](../models/inputsystemmetricsmemory.md)   | :heavy_minus_sign:                                                                   | Select the level of detail for memory metrics                                        |
| `network`                                                                            | [Optional[models.InputSystemMetricsNetwork]](../models/inputsystemmetricsnetwork.md) | :heavy_minus_sign:                                                                   | Select the level of detail for network metrics                                       |
| `disk`                                                                               | [Optional[models.InputSystemMetricsDisk]](../models/inputsystemmetricsdisk.md)       | :heavy_minus_sign:                                                                   | Select the level of detail for disk metrics                                          |