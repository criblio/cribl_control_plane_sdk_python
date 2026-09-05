# BackupsSettings


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `backup_persistence`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | How long to retain backups. Value is a duration string such as <code>24h</code>. |
| `backups_directory`                                                              | *str*                                                                            | :heavy_check_mark:                                                               | Filesystem path where configuration backups are stored.                          |