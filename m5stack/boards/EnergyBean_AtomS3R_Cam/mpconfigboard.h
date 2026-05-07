/*
 * SPDX-FileCopyrightText: 2026 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */

#define MICROPY_HW_BOARD_NAME "EnergyBean AtomS3R-CAM"
#define MICROPY_HW_MCU_NAME   "ESP32-S3-PICO-1"

#define MICROPY_PY_MACHINE_DAC (0)

#define MICROPY_HW_ENABLE_UART_REPL (0)

#define MICROPY_HW_I2C0_SCL         (1)
#define MICROPY_HW_I2C0_SDA         (2)

#define MICROPY_HW_USB_VID 0x303A
#define MICROPY_HW_USB_PID 0x8350
#define MICROPY_HW_USB_MANUFACTURER_STRING "EnergyBean"
#define MICROPY_HW_USB_PRODUCT_FS_STRING "AtomS3R-CAM"

#include "./../mpconfiglvgl.h"
