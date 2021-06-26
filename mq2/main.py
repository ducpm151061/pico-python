from machine import Pin
from KalmanFilter import KalmanFilter
import time

kf = KalmanFilter(1, 1, 0.01)
led = Pin(25, Pin.OUT)
mq = machine.ADC(28)
conversion_factor = 5.0/65535


def average_adc(times):
    temp = 0.0
    for i in range(times):
        print(mq.read_u16())
        temp = temp+mq.read_u16()
    return temp/times


while True:
    led.value(1)
    time.sleep(0.5)
    raw = kf.updateEstimate(average_adc(100))
    voltage = raw*conversion_factor
    print("ADC: ", raw)
    print("Voltage: ", voltage)
    led.value(0)
    time.sleep(0.5)
