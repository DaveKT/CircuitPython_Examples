import board
import neopixel
import time
import busio
import adafruit_lis3dh

ACCEL_RANGE   = adafruit_lis3dh.RANGE_16_G

p = neopixel.NeoPixel(board.NEOPIXEL, 10)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=25)

lis3dh.range = ACCEL_RANGE

while True:

    if(lis3dh.acceleration[0] > 5):
        p.fill((0,0,50))
    elif(lis3dh.acceleration[0] < -5):
        p.fill((0,0,50))
    else:
        p.fill((0,0,0))

    p.write()
    time.sleep(.1)
