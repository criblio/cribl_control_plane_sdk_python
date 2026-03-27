# CollectorScript

Script collector configuration


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `type`                                                         | [models.CollectorScriptType](../models/collectorscripttype.md) | :heavy_check_mark:                                             | Collector type                                                 |
| `conf`                                                         | [models.ScriptCollectorConf](../models/scriptcollectorconf.md) | :heavy_check_mark:                                             | N/A                                                            |
| `destructive`                                                  | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Delete any files collected (where applicable)                  |
| `encoding`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | Character encoding to use when parsing ingested data.          |