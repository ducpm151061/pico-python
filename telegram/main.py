import network
import socket
import time
import sys
import rp2
from machine import Pin
import urequests

rp2.country('VN')
led = Pin('LED', Pin.OUT)

ssid = 'savaobay'
password = 'Anhladuc97@'

bot_token = '6216512264:AAFtEKD3lPZA0dfjJEJCC2VzfhqsAOd97wY'
chat_id = '1187155703'


def send_message(chat_id, message):
    url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message
    results = urequests.get(url_req)
    print(results.json())
    results.close()


def get_updates():
    url_req = "https://api.telegram.org/bot" + bot_token + "/getUpdates"
    results = urequests.get(url_req)
    print(results.json())
    results.close()


hardware = str(sys.implementation)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def is_wifi_connected():
    wlan_status = wlan.status()
    if wlan_status != 3:
        return False
    else:
        return True


def connect_wifi():
    while True:
        if (is_wifi_connected()):
            led.on()
            status = wlan.ifconfig()
            print('ip = ' + status[0])
            send_message(chat_id, hardware)
            break
        else:
            print('WiFi is disconnected. Trying to connect.')
            led.off()
            wlan.connect(ssid, password)
            time.sleep(3)


# Connect to WiFi
connect_wifi()

while True:
    try:
        if (not is_wifi_connected()):
            connect_wifi()
        send_message(chat_id, 'test telegram')
        time.sleep(10)

    except OSError as e:
        led.off()
        wlan.disconnect()
        # Grace period.
        time.sleep(10)
        led.on()
        pass