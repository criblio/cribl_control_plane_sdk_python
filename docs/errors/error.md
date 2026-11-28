# Error


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `status`                                                                | *Literal["error"]*                                                      | :heavy_check_mark:                                                      | Always "error" for API error responses.                                 |
| `message`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | Human-readable message describing the error.                            |
| `details`                                                               | *Optional[Any]*                                                         | :heavy_minus_sign:                                                      | Optional structured details about the error (e.g. validation failures). |