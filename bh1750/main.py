from machine import Pin,I2C
from bh1750 import BH1750
import time


# init i2c
i2c = I2C(id=0,scl=Pin(5),sda=Pin(4))


# init module bh1750
object = BH1750(i2c)

while True:
    print(object.luminance(BH1750.ONCE_HIRES_1))
    time.sleep(1)
