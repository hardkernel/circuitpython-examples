# SPDX-FileCopyrightText: 2024 Steve Jeong for Hardkernel
# SPDX-License-Identifier: MIT

import board
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(board.I2C0_SCL, board.I2C0_SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 50hz.
pca.frequency = 50

# Default Setting
default_duty, default_step = 0xFFF, 0x2FF
min_duty, max_duty = 0x3FF, 0x20FF
motor_chennels = 3
duty, duty_step = default_duty, default_step

for i in range(motor_chennels):
  pca.channels[i].duty_cycle += default_duty

while True:
  duty += duty_step

  if duty <= min_duty or duty >= max_duty:
    duty_step = -duty_step

  duty = max(min_duty, min(duty, max_duty))

  for i in range(motor_chennels):
    pca.channels[i].duty_cycle = duty

  time.sleep(0.4)
