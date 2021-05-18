from machine import Pin
import utime as time
from pico_i2c_lcd import I2cLcd
from machine import I2C
import mlx90614
import random

# Touch Sensor GPIO Pin 18
touch_pin = Pin(18, Pin.IN, Pin.PULL_DOWN)

# LCD SCL: 27 SDA 26
i2c = I2C(id=1, scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# MLX SCL: 17 SDA 16
i2c_Mlx = I2C(id=0, scl=Pin(17), sda=Pin(16), freq=100000)
sensor = mlx90614.MLX90614(i2c_Mlx)


while True:
    if touch_pin.value():
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Xin chao ban!")
        time.sleep(0.5)
    time.sleep(0.2)
    ambient = sensor.read_ambient_temp()
    object = sensor.read_object_temp()
    if (ambient < 100 and object < 100):
        ambient = str(ambient)
        object = str(object)
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr('Ambient:'+ambient)
        lcd.move_to(0, 1)
        lcd.putstr('Object:'+object)
        time.sleep(1)
    else:
        continue
