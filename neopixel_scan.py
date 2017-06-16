# Author:   David Kolet-Tassara
# Date:     June 16, 2017
# Purpose:  Demonstrates the use of the neopixels on Adafruit's
#           Circuit Python. Simulates cylon scanning.
# Required Packages:
# neopixel
# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/releases
# adafruit_thermistor

import board
import neopixel
import time

DELAY = .07
COLOR = (0,0,50)

p = neopixel.NeoPixel(board.NEOPIXEL, 10)

def scan(t, c):
    for i in range(10):
        p[i] = c
        p[i-1] = (0,0,0)
        p.write()
        time.sleep(t)

    for i in range(8,0,-1):
        p[i] = (0,0,50)
        p[i+1] = (0,0,0)
        p.write()
        time.sleep(t)

while True:
    scan(DELAY, COLOR)
