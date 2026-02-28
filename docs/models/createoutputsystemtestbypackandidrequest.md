# CreateOutputSystemTestByPackAndIDRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Destination to send sample event data to. |
| `pack`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Pack to create.                           |
| `output_test_request`                                                | [models.OutputTestRequest](../models/outputtestrequest.md)           | :heavy_check_mark:                                                   | OutputTestRequest object                                             |