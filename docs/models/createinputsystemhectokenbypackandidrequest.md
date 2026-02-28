# CreateInputSystemHecTokenByPackAndIDRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | The <code>id</code> of the Splunk HEC Source.                |
| `pack`                                                       | *str*                                                        | :heavy_check_mark:                                           | The <code>id</code> of the Pack to create.                   |
| `add_hec_token_request`                                      | [models.AddHecTokenRequest](../models/addhectokenrequest.md) | :heavy_check_mark:                                           | AddHecTokenRequest object                                    |