# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

_attrs = {
    "BATTERY_BLACK_CHARGE_IMG": "/system/energybean_fire/Battery/battery_Black_Charge.png",
    "BATTERY_BLACK_IMG": "/system/energybean_fire/Battery/battery_Black.png",
    "BATTERY_GRAY_IMG": "/system/energybean_fire/Battery/battery_Gray.png",
    "BATTERY_GREEN_CHARGE_IMG": "/system/energybean_fire/Battery/battery_Green_Charge.png",
    "BATTERY_GREEN_IMG": "/system/energybean_fire/Battery/battery_Green.png",
    "BATTERY_RED_CHARGE_IMG": "/system/energybean_fire/Battery/battery_Red_Charge.png",
    "BATTERY_RED_IMG": "/system/energybean_fire/Battery/battery_Red.png",
    "BATTERY_YELLOW_IMG": "/system/energybean_fire/Battery/battery_Yellow.png",
    "SERVER_BLUE_IMG": "/system/energybean_fire/Server/server_blue.png",
    "SERVER_EMPTY_IMG": "/system/energybean_fire/Server/server_empty.png",
    "SERVER_ERROR_IMG": "/system/energybean_fire/Server/server_error.png",
    "SERVER_GREEN_IMG": "/system/energybean_fire/Server/Server_Green.png",
    "SERVER_RED_IMG": "/system/energybean_fire/Server/server_red.png",
    "WIFI_DISCONNECTED_IMG": "/system/energybean_fire/WiFi/wifi_disconnected.png",
    "WIFI_EMPTY_IMG": "/system/energybean_fire/WiFi/wifi_empty.png",
    "WIFI_GOOD_IMG": "/system/energybean_fire/WiFi/wifi_good.png",
    "WIFI_MID_IMG": "/system/energybean_fire/WiFi/wifi_mid.png",
    "WIFI_WORSE_IMG": "/system/energybean_fire/WiFi/wifi_worse.png",
    "APPLIST_SELECTED_IMG": "/system/energybean_fire/appList_selected.png",
    "APPLIST_UNSELECTED_IMG": "/system/energybean_fire/appList_unselected.png",
    "APPLIST_IMG": "/system/energybean_fire/applist.png",
    "APPLIST_LEFT_IMG": "/system/energybean_fire/applistLeft.png",
    "APPLIST_RIGHT_IMG": "/system/energybean_fire/applistRight.png",
    "APPRUN_SELECTED_IMG": "/system/energybean_fire/appRun_selected.png",
    "APPRUN_UNSELECTED_IMG": "/system/energybean_fire/appRun_unselected.png",
    "BAR1_IMG": "/system/energybean_fire/bar1.png",
    "BAR2_IMG": "/system/energybean_fire/bar2.png",
    "BAR3_IMG": "/system/energybean_fire/bar3.png",
    "BAR4_IMG": "/system/energybean_fire/bar4.png",
    "BAR5_IMG": "/system/energybean_fire/bar5.png",
    "BOOT_NO_IMG": "/system/energybean_fire/boot_No.png",
    "BOOT_YES_IMG": "/system/energybean_fire/boot_Yes.png",
    "DEVELOP_SELECTED_IMG": "/system/energybean_fire/develop_selected.png",
    "DEVELOP_UNSELECTED_IMG": "/system/energybean_fire/develop_unselected.png",
    "DEVELOP_PRIVATE_IMG": "/system/energybean_fire/developPrivate.png",
    "DEVELOP_PUBLIC_IMG": "/system/energybean_fire/developPublic.png",
    "EZDATA_SELECTED_IMG": "/system/energybean_fire/ezdata_selected.png",
    "EZDATA_UNSELECTED_IMG": "/system/energybean_fire/ezdata_unselected.png",
    "LOGO_IMG": "/system/energybean_fire/logo.png",
    "RUN_IMG": "/system/energybean_fire/run.png",
    "SCREEN25_IMG": "/system/energybean_fire/screen25.png",
    "SCREEN50_IMG": "/system/energybean_fire/screen50.png",
    "SCREEN75_IMG": "/system/energybean_fire/screen75.png",
    "SCREEN100_IMG": "/system/energybean_fire/screen100.png",
    "SETTING_SELECTED_IMG": "/system/energybean_fire/setting_selected.png",
    "SETTING_UNSELECTED_IMG": "/system/energybean_fire/setting_unselected.png",
    "SETTING_SELECT_IMG": "/system/energybean_fire/settingSelect.png",
    "SETTING_UNSELECT_IMG": "/system/energybean_fire/settingUnselect.png",
    "SETTING_WIFI_IMG": "/system/energybean_fire/SettingWifi.png",
}


def __getattr__(attr):
    value = _attrs.get(attr, None)
    if value is None:
        raise AttributeError(attr)
    globals()[attr] = value
    return value
