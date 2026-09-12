# PipelineFunctionTeeConf

Configuration specific to the Pipeline Function.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `command`                                                                            | *str*                                                                                | :heavy_check_mark:                                                                   | Command to execute and feed events to, via stdin. One JSON-formatted event per line. |
| `args`                                                                               | List[*str*]                                                                          | :heavy_minus_sign:                                                                   | Command-line arguments to pass to the command.                                       |
| `restart_on_exit`                                                                    | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | Restart the process if it exits and/or we fail to write to it                        |
| `env`                                                                                | Dict[str, *str*]                                                                     | :heavy_minus_sign:                                                                   | Environment variables to overwrite or set                                            |