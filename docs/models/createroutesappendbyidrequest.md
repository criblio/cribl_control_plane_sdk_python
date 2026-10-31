# CreateRoutesAppendByIDRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `id`                                                                              | *Literal["default"]*                                                              | :heavy_check_mark:                                                                | The <code>id</code> of the Routing table. The only value is <code>default</code>. |
| `request_body`                                                                    | List[[models.RouteConfInput](../models/routeconfinput.md)]                        | :heavy_check_mark:                                                                | RouteDefinitions object.                                                          |