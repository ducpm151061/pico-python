from machine import Pin
import utime as time
from pico_i2c_lcd import I2cLcd
from machine import I2C

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

while True:
    time.sleep(1)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('Temp :')
    lcd.move_to(7,0)
    lcd.move_to(0,1)
    lcd.putstr('Humi :')
    lcd.move_to(7,1)
    time.sleep(1)