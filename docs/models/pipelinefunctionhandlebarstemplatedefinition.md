# PipelineFunctionHandlebarsTemplateDefinition


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique identifier for this template                                  |
| `content`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Handlebars template string                                           |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional description of what this template is used for               |
| `type`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Type categorization for the template (e.g., Universal, Email, Slack) |