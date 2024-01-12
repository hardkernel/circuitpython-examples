# SPDX-FileCopyrightText: 2024 Steve Jeong for Hardkernel
# SPDX-License-Identifier: MIT

import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)
RESET_PIN = digitalio.DigitalInOut(board.D18)

# input oled size, address, and reset pin
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=RESET_PIN)

# clear
oled.fill(0)
oled.show()

# create blank for drawing
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
line = 16

while True:
  draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
  draw.text((0, 0), time.strftime("%e %b %Y"), fill=255)
  draw.text((0, line), time.strftime("%A"), fill=255)
  draw.text((0, line*2), time.strftime("%X"), fill=255)
  oled.image(image)
  oled.show()
