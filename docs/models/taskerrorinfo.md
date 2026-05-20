# TaskErrorInfo

Serialized error object that describes why a job entered its current <code>state</code>. Includes <code>message</code> and may include a nested <code>reason</code> for wrapped errors.


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `message`                           | *str*                               | :heavy_check_mark:                  | Human-readable error message.       |
| `name`                              | *Optional[str]*                     | :heavy_minus_sign:                  | Error name, if available.           |
| `stack`                             | *Optional[str]*                     | :heavy_minus_sign:                  | Truncated stack trace of the error. |
| `__pydantic_extra__`                | Dict[str, *Any*]                    | :heavy_minus_sign:                  | N/A                                 |