# SystemSettingsConfUpdateSystem

System-level operational settings for the Cribl instance.


## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `intercom`                                                                                                         | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | If <code>true</code>, enable Intercom integration for in-product messaging. Otherwise, <code>false</code>.         |
| `upgrade`                                                                                                          | [Optional[models.UpgradeOptionsSystemSettingsConfSystem]](../models/upgradeoptionssystemsettingsconfsystem.md)     | :heavy_minus_sign:                                                                                                 | Upgrade permission policy: <code>api</code> to allow upgrades from the UI or API or <code>false</code> to disable. |