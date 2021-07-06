from machine import Pin,I2C
from tcs34725 import TCS34725
import time
i2c = I2C(id=0,scl=Pin(9),sda=Pin(8),freq=400000)
tcs=TCS34725(i2c=i2c)
tcs.active(True)
led = Pin(25, Pin.OUT)

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    print(tcs.read())
    led.value(0)
    time.sleep(0.5)