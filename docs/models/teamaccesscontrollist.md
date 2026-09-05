# TeamAccessControlList


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `perms`                                                                     | List[[models.ResourcePolicy](../models/resourcepolicy.md)]                  | :heavy_check_mark:                                                          | List of resource policies that define the access permissions for this team. |
| `team`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | Name of the team whose access control entries are listed.                   |