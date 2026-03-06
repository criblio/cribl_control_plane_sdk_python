# ErrorTypeStatusPq

Error information for the persistent queue, if applicable.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `details`                                                         | Dict[str, *Any*]                                                  | :heavy_minus_sign:                                                | Additional details for the persistent queue error.                |
| `message`                                                         | *str*                                                             | :heavy_check_mark:                                                | Human-readable message that describes the persistent queue error. |