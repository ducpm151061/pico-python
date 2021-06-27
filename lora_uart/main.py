from machine import Pin, UART
import time
# LED Blink
led = Pin(25, Pin.OUT)
# UART Init
# init with given baudrate TX: Pin 4, RX: Pin 5
uart = UART(1, 9600, tx=Pin(4), rx=Pin(5))
# uart.init(9600, bits=8, parity=None, stop=1)  # init with given parameters

while True:
    rxData = bytes()
    # while uart.any() > 0:
    if uart.any() > 0:
        rxData = uart.read()
        if rxData.decode('utf-8') == 'Gui':
            uart.write("Phung Minh Duc")
            led.value(1)
            time.sleep(1)
            led.value(0)
            time.sleep(1)
