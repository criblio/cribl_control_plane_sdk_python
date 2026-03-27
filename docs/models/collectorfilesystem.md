# CollectorFilesystem

Filesystem collector configuration


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [models.CollectorFilesystemType](../models/collectorfilesystemtype.md) | :heavy_check_mark:                                                     | Collector type                                                         |
| `conf`                                                                 | [models.FilesystemCollectorConf](../models/filesystemcollectorconf.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `destructive`                                                          | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Delete any files collected (where applicable)                          |
| `encoding`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Character encoding to use when parsing ingested data.                  |