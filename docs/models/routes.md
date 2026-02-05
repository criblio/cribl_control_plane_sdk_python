# Routes


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `comments`                                                  | List[[models.RouteComment](../models/routecomment.md)]      | :heavy_minus_sign:                                          | Comments.                                                   |
| `groups`                                                    | Dict[str, [models.RoutesGroups](../models/routesgroups.md)] | :heavy_minus_sign:                                          | Map of route groups.                                        |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | Routes ID.                                                  |
| `routes`                                                    | List[[models.RouteConf](../models/routeconf.md)]            | :heavy_check_mark:                                          | Pipeline routing rules.                                     |