# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

package(
    "startup",
    (
        "__init__.py",
        "energybean_fire/__init__.py",
        "energybean_fire/app_base.py",
        "energybean_fire/framework.py",
        "energybean_fire/res.py",
        "energybean_fire/apps/app_list.py",
        "energybean_fire/apps/app_run.py",
        "energybean_fire/apps/dev.py",
        "energybean_fire/apps/ezdata.py",
        "energybean_fire/apps/settings.py",
    ),
    base_path="..",
    opt=3,
)
