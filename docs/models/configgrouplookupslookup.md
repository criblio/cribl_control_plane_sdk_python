# ConfigGroupLookupsLookup


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `deployed_version`                                                   | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Version of the lookup file currently deployed on the Worker or Node. |
| `file`                                                               | *str*                                                                | :heavy_check_mark:                                                   | File name of the deployed lookup.                                    |
| `version`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Version of the lookup file currently staged for deployment.          |