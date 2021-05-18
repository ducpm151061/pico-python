from machine import Pin
# from bmp180 import BMP180
from bmp085 import BMP180

import utime as time
from machine import I2C
i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)

bmp = BMP180(i2c)
bmp.oversample = 2
bmp.sealevel = 101325

while True:
    temp = bmp.temperature
    p = bmp.pressure
    altitude = bmp.altitude
    print("Temp: "+str(temp))
    print("pressure: "+str(p))
    print("altitude "+ str(altitude))
    time.sleep(1)
