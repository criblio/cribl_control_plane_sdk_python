# RestAPIJSONError

JSON body returned for many REST failures that use RESTEndpoint.sendError (and similar handlers).


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `details`                                                               | Dict[str, *Any*]                                                        | :heavy_minus_sign:                                                      | Optional structured details about the error (e.g. validation failures). |
| `message`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | Human-readable message or serialized validation details for the error.  |
| `status`                                                                | *Literal["error"]*                                                      | :heavy_check_mark:                                                      | Always <code>error</code> for API error responses.                      |