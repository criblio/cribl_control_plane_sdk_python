# RouteComment


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `comment`                                                                | *str*                                                                    | :heavy_check_mark:                                                       | Brief description of the Route.                                          |
| `group_id`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Unique identifier for the Route Group that the Route is associated with. |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique identifier for the comment.                                       |
| `index`                                                                  | *float*                                                                  | :heavy_check_mark:                                                       | Relative position of the comment among all comments for the Route.       |