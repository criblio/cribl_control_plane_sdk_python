# NotificationConfigForSMTPTarget3

Simple Mail Transfer Protocol (SMTP) configuration for the Notification target.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `subject`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Email subject                                                    |
| `body`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Email body                                                       |
| `email_recipient`                                                | [Optional[models.EmailRecipient3]](../models/emailrecipient3.md) | :heavy_minus_sign:                                               | Email recipient settings for the Notification target.            |