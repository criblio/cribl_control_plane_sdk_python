# UserAccessControlList


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `perms`                                                                       | List[[models.ResourcePolicy](../models/resourcepolicy.md)]                    | :heavy_check_mark:                                                            | List of resource policies that define the access permissions for this member. |
| `user`                                                                        | *str*                                                                         | :heavy_check_mark:                                                            | Username of the member whose access control entries are listed.               |