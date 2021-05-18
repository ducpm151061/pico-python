from machine import Pin
import time
from pico_i2c_lcd import I2cLcd
from machine import I2C

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def find():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(5)
    trig.low()
    
    while echo.value() == 0:
        signaloff = time.ticks_us()
    
    while echo.value() == 1:
        signalon = time.ticks_us()
        
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    
    print("Distance is: ", distance, "cm")
    
    # oled.text("Distance is : ", 0, 0)
    # oled.text(str(distance) + " cm", 0, 10)
    # oled.show()
    # oled.fill(0)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(str(distance))
while True:
    find()
    time.sleep(0.1)