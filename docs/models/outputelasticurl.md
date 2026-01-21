# OutputElasticURL


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `url`                                                                             | *str*                                                                             | :heavy_check_mark:                                                                | The URL to an Elastic node to send events to. Example: http://elastic:9200/_bulk  |
| `weight`                                                                          | *Optional[float]*                                                                 | :heavy_minus_sign:                                                                | Assign a weight (>0) to each endpoint to indicate its traffic-handling capability |