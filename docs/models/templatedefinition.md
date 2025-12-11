# TemplateDefinition


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `content`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Handlebars template string                                           |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional description of what this template is used for               |
| `type`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Type categorization for the template (e.g., Universal, Email, Slack) |