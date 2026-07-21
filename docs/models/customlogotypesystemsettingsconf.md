# CustomLogoTypeSystemSettingsConf

Custom logo configuration for the Cribl UI login page and navigation bar.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `enabled`                                                                               | *bool*                                                                                  | :heavy_check_mark:                                                                      | If <code>true</code>, display the custom logo in the UI. Otherwise, <code>false</code>. |
| `logo_description`                                                                      | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Description text displayed alongside the custom logo.                                   |
| `logo_image`                                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Custom logo image as a base64-encoded data URI (PNG or JPEG, maximum 2 MB).             |