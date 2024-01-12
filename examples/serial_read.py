# SPDX-FileCopyrightText: 2024 Steve Jeong for Hardkernel
# SPDX-License-Identifier: MIT

import serial
import time

'''
You can use another valid serial device
instead of '/dev/serial0'.
'''
ser = serial.Serial('/dev/serial0')
cnt = 0

while True:
  try:
    cnt += 1
    print('read data: {0} {1}'.format(ser.read(5), cnt))
  except KeyboardInterrupt:
    break

ser.close()
