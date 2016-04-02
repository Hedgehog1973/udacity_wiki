from handler import *
from databases import *

class Login(Handler):
	def get(self):
		self.render('login.html')

	def post(self):
		username = self.request.get('username').lower()
		password = self.request.get('password')

		u = User.login(username, password)
		if u:
			self.login(u)
			self.redirect('/')
		else:
			self.render('login.html', error_user="Invalid login")