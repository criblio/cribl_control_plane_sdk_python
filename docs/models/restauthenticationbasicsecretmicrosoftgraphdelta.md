# RestAuthenticationBasicSecretMicrosoftGraphDelta

Internal opt-in for the Microsoft Graph deltaLink state-tracking hook. Set programmatically by the Microsoft Graph source when the configured URL targets a /delta endpoint; not user-configurable.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `delta_link_attribute`                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Response-body field name to extract as the delta link (typically '@odata.deltaLink') |