# CollectorS3

S3 collector configuration


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `type`                                                 | [models.CollectorS3Type](../models/collectors3type.md) | :heavy_check_mark:                                     | Collector type                                         |
| `conf`                                                 | [models.S3CollectorConf](../models/s3collectorconf.md) | :heavy_check_mark:                                     | N/A                                                    |
| `destructive`                                          | *Optional[bool]*                                       | :heavy_minus_sign:                                     | Delete any files collected (where applicable)          |
| `encoding`                                             | *Optional[str]*                                        | :heavy_minus_sign:                                     | Character encoding to use when parsing ingested data.  |