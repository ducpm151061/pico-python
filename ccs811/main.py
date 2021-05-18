from machine import Pin, I2C
import time
from ccs811 import CCS811

led = Pin(25, Pin.OUT)

i2c = I2C(id=1,scl=Pin(27), sda=Pin(26),freq=100000)
    # Adafruit sensor breakout has i2c addr: 90; Sparkfun: 91
s = CCS811(i2c=i2c, addr=91)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    if s.data_ready():
        # print(s.eCO2)
        # print(s.tVOC)
        print('eCO2: %d ppm, TVOC: %d ppb' % (s.eCO2, s.tVOC))
    time.sleep(1)