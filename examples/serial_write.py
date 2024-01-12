# SPDX-FileCopyrightText: 2024 Steve Jeong for Hardkernel
# SPDX-License-Identifier: MIT

import random
import serial
import string
import time

'''
You can use another valid serial device
instead of '/dev/serial0'.
'''
ser = serial.Serial('/dev/serial0')

while True:
  try:
    msg = generate_random_string(5)
    ser.write(b'hello')
    time.sleep(0.5)
  except KeyboardInterrupt:
    break

ser.close()
