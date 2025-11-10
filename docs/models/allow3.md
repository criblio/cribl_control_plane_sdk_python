# Allow3


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `procname`                                                                         | *str*                                                                              | :heavy_check_mark:                                                                 | Specify the name of a process or family of processes.                              |
| `arg`                                                                              | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Specify a string to substring-match against process command-line.                  |
| `config`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | Choose a config to apply to processes that match the process name and/or argument. |