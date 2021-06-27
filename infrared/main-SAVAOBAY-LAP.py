from machine import Pin
import utime as time
from pico_i2c_lcd import I2cLcd
from machine import I2C
import mlx90614
import random

i2c = I2C(id=1, scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)


i2c_Mlx = I2C(id=0, scl=Pin(17), sda=Pin(16), freq=100000)
sensor = mlx90614.MLX90614(i2c_Mlx)


while True:
    if sensor.read_ambient_temp() < 100 and sensor.read_object_temp() < 100:
        ambient = str(sensor.read_ambient_temp())

    object = str(sensor.read_ambient_temp())
    # print(sensor.read_ambient_temp())
    # print(sensor.read_object_temp())
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr('Ambient:'+ambient)
    lcd.move_to(0, 1)
    lcd.putstr('Object:'+object)
    time.sleep(1)
