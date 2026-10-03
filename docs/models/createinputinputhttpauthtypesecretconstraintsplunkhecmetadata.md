# CreateInputInputHTTPAuthTypeSecretConstraintSplunkHecMetadata

Splunk HEC metadata associated with the authentication token.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `enabled`                                                          | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | When enabled, the token value is available on events as __hecToken |
| `default_dataset`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Default Lake Dataset for events received with the token.           |
| `allowed_indexes_at_token`                                         | List[*str*]                                                        | :heavy_minus_sign:                                                 | Splunk indexes that the token can write to.                        |