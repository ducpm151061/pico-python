from machine import Pin
import time
from lora import LoRa
from machine import SPI


led = Pin(25, Pin.OUT)
spi = SPI(0)
lora = LoRa(
    spi,
    cs=Pin(17, Pin.OUT),
    rx=Pin(16, Pin.IN),
)
while True:
    led.value(1)
    time.sleep(0.5)
    lora.send('Hello world!')
    led.value(0)
    time.sleep(0.5)
