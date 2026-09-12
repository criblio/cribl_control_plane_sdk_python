# DeployRequest


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `lookups`                                                                       | List[[models.DeployRequestLookups](../models/deployrequestlookups.md)]          | :heavy_minus_sign:                                                              | Optional list of lookup file deployments to include with the commit deployment. |
| `version`                                                                       | *str*                                                                           | :heavy_check_mark:                                                              | Commit hash to deploy to the Worker Group, Outpost Group, or Edge Fleet.        |