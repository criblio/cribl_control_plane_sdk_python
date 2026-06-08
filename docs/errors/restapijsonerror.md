# RestAPIJSONError

JSON body returned for many REST failures that use RESTEndpoint.sendError (and similar handlers).


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `message`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | Human-readable message or serialized validation details for the error. |
| `status`                                                               | *Literal["error"]*                                                     | :heavy_check_mark:                                                     | Always <code>error</code> for API error responses.                     |