# InputKafkaAuthentication

Authentication parameters to use when connecting to brokers. Using TLS is highly recommended.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `disabled`                                                                       | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | N/A                                                                              |
| `mechanism`                                                                      | [Optional[models.InputKafkaSASLMechanism]](../models/inputkafkasaslmechanism.md) | :heavy_minus_sign:                                                               | N/A                                                                              |
| `oauth_enabled`                                                                  | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Enable OAuth authentication                                                      |