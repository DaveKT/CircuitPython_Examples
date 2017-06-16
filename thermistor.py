import time
import neopixel
import board
import adafruit_thermistor

p = neopixel.NeoPixel(board.NEOPIXEL, 10)
t = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3380)

while True:
    if t.temperature < 21:
        p.fill((22,50,87))
        print("it's cool")
    elif t.temperature > 29:
        p.fill((64,14,12))
        print("it's warm")
    else:
        p.fill((18,70,20))
        print("it's comfortable")

    p.write()
    time.sleep(5)
