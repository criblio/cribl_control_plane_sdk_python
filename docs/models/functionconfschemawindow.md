# FunctionConfSchemaWindow


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `event_window_id`                                               | *Optional[float]*                                               | :heavy_minus_sign:                                              | Identifies the unique ID, used for a event window               |
| `registered_functions`                                          | List[*str*]                                                     | :heavy_minus_sign:                                              | All window functions, tracked by this event window              |
| `tail_event_count`                                              | *Optional[float]*                                               | :heavy_minus_sign:                                              | Number of events to keep before the current event in the window |
| `head_event_count`                                              | *Optional[float]*                                               | :heavy_minus_sign:                                              | Number of events to keep after the current event in the window  |