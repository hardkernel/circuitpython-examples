# SPDX-FileCopyrightText: 2024 Steve Jeong for Hardkernel
# SPDX-License-Identifier: MIT

import time
import board
from analogio import AnalogIn


def get_voltage(pin):
    return (pin.value * 1.8) / 1095 # Based on ODROIDs

adc0 = AnalogIn(board.A0)

while True:
    print((get_voltage(adc0),))
    time.sleep(0.1)
