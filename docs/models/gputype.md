# GpuType


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `mode`                                                         | [Optional[models.ModeOptionsGpu]](../models/modeoptionsgpu.md) | :heavy_minus_sign:                                             | Select the level of detail for GPU metrics                     |
| `per_gpu`                                                      | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Generate metrics for each GPU                                  |
| `detail`                                                       | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Generate full GPU metrics                                      |