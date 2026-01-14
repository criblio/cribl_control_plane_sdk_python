# FunctionConfSchemaJoin


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `kind`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | Join kind, e.g. inner                                      |
| `hints`                                                    | Dict[str, *str*]                                           | :heavy_minus_sign:                                         | Hints passed to the join function                          |
| `field_conditions`                                         | List[[models.FieldCondition](../models/fieldcondition.md)] | :heavy_minus_sign:                                         | Fields to use when joining                                 |
| `search_job_id`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | The id for this search job.                                |
| `stage_id`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | The stage we are joining with.                             |