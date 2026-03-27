# CollectorAzureBlob

AzureBlob collector configuration


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | [models.CollectorAzureBlobType](../models/collectorazureblobtype.md) | :heavy_check_mark:                                                   | Collector type                                                       |
| `conf`                                                               | [models.AzureBlobCollectorConf](../models/azureblobcollectorconf.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `destructive`                                                        | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Delete any files collected (where applicable)                        |
| `encoding`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Character encoding to use when parsing ingested data.                |