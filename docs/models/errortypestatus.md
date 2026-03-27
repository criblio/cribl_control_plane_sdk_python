# ErrorTypeStatus

Error information, if applicable.


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `details`                                                                                                 | Dict[str, *Any*]                                                                                          | :heavy_minus_sign:                                                                                        | Additional error details, which may include stack traces, request information, and other diagnostic data. |
| `message`                                                                                                 | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Human-readable message that describes the error.                                                          |