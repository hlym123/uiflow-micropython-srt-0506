# SPDX-FileCopyrightText: 2026 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import startup
from . import framework
from . import apps
import M5
import time


class CoreS3_Startup:
    def __init__(self) -> None:
        self._wlan = startup.Startup()
        # self._status_bar = StatusBarApp(None, self._wifi)

    def startup(
        self,
        ssid: str,
        pswd: str,
        protocol: str = "",
        ip: str = "",
        netmask: str = "",
        gateway: str = "",
        dns: str = "",
        timeout: int = 60,
    ) -> None:
        self._wlan.connect_network(
            ssid, pswd, protocol=protocol, ip=ip, netmask=netmask, gateway=gateway, dns=dns
        )
        # M5.Lcd.drawImage("/system/energybean_cores3/boot.png", 0, 0)
        # time.sleep(0.2)

        M5.Lcd.clear(0x000000)
        sprite = M5.Lcd.newCanvas(320, 160, 16, True)

        fw = framework.Framework()
        run_app = apps.RunApp(None)
        list_app = apps.ListApp(sprite)
        fw.install_bar(apps.StatusBarApp(None, self._wlan))
        fw.install_launcher(run_app)
        fw.install(run_app)
        fw.install(list_app)
        fw.start()
