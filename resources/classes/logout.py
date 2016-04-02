from .. import funct
from handler import *

class Logout(Handler):
	def get(self):
		url = self.request.headers.get('referer').split('/')[3:]
		if url:
			url_redirect = funct.WikiF.url_creator(url)
		else:
			url_redirect = '/'

		self.logout()
		self.redirect(url_redirect)