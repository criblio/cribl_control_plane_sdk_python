# UpdatePacksByIDRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | The <code>id</code> of the Pack to upgrade.                 |
| `source`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | body string required Pack source                            |
| `minor`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | body boolean optional Only upgrade to minor/patch versions  |
| `spec`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | body string optional Specify a branch, tag or a semver spec |