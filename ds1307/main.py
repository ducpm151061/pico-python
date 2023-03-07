from machine import I2C, Pin
import ds1307
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
ds = ds1307.DS1307(i2c)
led = Pin(25, Pin.OUT)

# now = (20231, 3, 7, 6, 22, 9, 0, 0)
# ds.datetime(now)
while True:
    led.value(1)
    time.sleep(1)
    print(ds.datetime())
    led.value(0)
    time.sleep(1)
