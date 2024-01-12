# SPDX-FileCopyrightText: 2024 Steve Jeong for Hardkernel
# SPDX-License-Identifier: MIT

import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 12

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
  spi, NUM_PIXELS, pixel_order=neopixel.GRB, auto_write=False
)

while True:
  for i in range(NUM_PIXELS):
    pixels[i] = 0xFF0000
    pixels.show()
    time.sleep(0.1)
    pixels.fill(0)
