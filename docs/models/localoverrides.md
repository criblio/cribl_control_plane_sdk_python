# LocalOverrides

Instance-level tuning applied after all sources are merged. No git required.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `disabled`                                                                           | List[*str*]                                                                          | :heavy_minus_sign:                                                                   | Rule IDs to silence entirely.                                                        |
| `field_overrides`                                                                    | List[[models.FieldOverride](../models/fieldoverride.md)]                             | :heavy_minus_sign:                                                                   | Patch scalar fields of a rule without copying its full definition.                   |
| `inline_rules`                                                                       | List[[models.InlineRule](../models/inlinerule.md)]                                   | :heavy_minus_sign:                                                                   | Full rule definitions authored here. Quick one-offs that don't warrant a git commit. |