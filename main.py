import network
from machine import Pin
import usocket as socket
import json
from multpin import MultPin

auth_dict = dict()

with open("auth.json") as f:
    auth_dict = json.loads(f.read())    

ssid = auth_dict['ssid']
password = auth_dict['password']

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

right_pin = Pin(5, Pin.OUT) # D1
left_pin = Pin(4, Pin.OUT) # D2

forward_pin = Pin(14, Pin.OUT) # D5
backward_pin = Pin(12, Pin.OUT) # D6

led = Pin(2, Pin.OUT) # LED

break_pin = MultPin(forward_pin, backward_pin)

keys_dict = {'a': left_pin, 'd': right_pin, 's': backward_pin, 'w': forward_pin}
value_dict = {'-': 0, '+': 1}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.2)
s.bind(('', 2048))

led = Pin(2, Pin.OUT)
led.value(0)

while True:
    try:
        data, addr = s.recvfrom(1024)
        send_data = data
        data = data.decode('utf-8')
        print(data)
        keys_dict[data[:-1]].value(value_dict[data[-1]])
        print('key: {0}\nvalue: {1}'.format(keys_dict[data[:-1]], value_dict[data[-1]]))
        s.sendto(send_data, addr)
    except OSError:
        break_pin.value(0)
