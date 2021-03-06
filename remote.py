import signal
import keyboard
import time
import socket
import sys
from time import sleep

class Remote():
	__possible_keys = ['a', 'w', 's', 'd', 'n', 'p']
	__signals = {'up': '-', 'down': '+'}
	def __init__(self, udp_ip, udp_port):
		self.udp_ip = udp_ip
		self.udp_port = udp_port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def start(self):
		self.done = False
		signal.signal(signal.SIGINT, self.cleanup)
		keyboard.hook(self.my_on_key_event)
		while not self.done:
		  time.sleep(1)

	def cleanup(self, signum, frame):
		self.done = True

	def my_on_key_event(self, e):
		if e.name in Remote.__possible_keys:
			self.sock.sendto('{0}{1}'.format(e.name, Remote.__signals[e.event_type]).encode(), (self.udp_ip, self.udp_port))
			print('sending {0}{1}'.format(e.name, Remote.__signals[e.event_type]).encode(), (self.udp_ip, self.udp_port))
			
remote = Remote(sys.argv[1], int(sys.argv[2]))
remote.start()
