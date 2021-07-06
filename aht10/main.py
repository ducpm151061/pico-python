from machine import Pin, I2C
import time
from aht10 import AHT10
i2c = I2C(id=0, scl=Pin(9), sda=Pin(8), freq=400000)
aht10 = AHT10(i2c=i2c)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    aht10.print()
    led.value(0)
    time.sleep(0.5)
