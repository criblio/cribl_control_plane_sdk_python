# CreateRoutesAppendByPackAndIDRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `id`                                                                              | *Literal["default"]*                                                              | :heavy_check_mark:                                                                | The <code>id</code> of the Routing table. The only value is <code>default</code>. |
| `pack`                                                                            | *str*                                                                             | :heavy_check_mark:                                                                | The <code>id</code> of the Pack.                                                  |
| `request_body`                                                                    | List[[models.RouteConfInput](../models/routeconfinput.md)]                        | :heavy_check_mark:                                                                | RouteDefinitions object.                                                          |