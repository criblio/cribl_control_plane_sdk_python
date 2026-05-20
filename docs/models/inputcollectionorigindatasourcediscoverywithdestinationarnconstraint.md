# InputCollectionOriginDataSourceDiscoveryWithDestinationArnConstraint

Read-only metadata that records how the Source was created. Preserved on update when omitted from the request body. Cannot be set on create.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `origin`                                                                   | [Optional[models.Origin]](../models/origin.md)                             | :heavy_minus_sign:                                                         | Feature that created the Source.                                           |
| `destination_arn`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | ARN of the S3 bucket or Firehose delivery stream configured as the Source. |
| `source_arn`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | ARN of the AWS resource that produces the logs.                            |