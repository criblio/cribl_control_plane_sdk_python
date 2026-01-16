# OutputWizHecURL


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `url`                                                                                        | *str*                                                                                        | :heavy_check_mark:                                                                           | URL to an endpoint to send events to, such as http://localhost:8088/services/collector/event |
| `weight`                                                                                     | *Optional[float]*                                                                            | :heavy_minus_sign:                                                                           | Assign a weight (>0) to each endpoint to indicate its traffic-handling capability            |