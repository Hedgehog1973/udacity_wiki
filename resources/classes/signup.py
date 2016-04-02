from handler import *
from databases import *
from .. import funct

class Signup(Handler):
	def get(self):
		self.render('signup.html')

	def post(self):
		fry, error1, error2, error3, error4 = "", "", "", "", ""

		username = self.request.get('username').lower()
		password = self.request.get('password')
		pass_ver = self.request.get('verify')
		email = self.request.get('email')

		valid_username = funct.WikiF.valid_username(username)
		valid_password = funct.WikiF.valid_password(password)
		validation = funct.WikiF.verification(password, pass_ver)
		valid_email = funct.WikiF.valid_mail(email)

		if not valid_username:
			error1 = "That's not a valid Username."
		if not valid_password:
			error2 = "That wasn't a valid password."
		if password != pass_ver:
			error3 = "Password doesn't match."
		
		if email != "":
			if not valid_email:
				error4 = "That's not a valid email address."
		else:
			valid_email = True
		
		if not (valid_username and valid_password and validation and valid_email):
			self.render('signup.html', error_user=error1, error_pass=error2, error_val=error3,
				                       error_mail=error4, username=username, email=email)
		else:
			u = User.by_name(username)
			if u:
				self.render('signup.html', error_user="That user already exists.")
			else:
				u = User.register(username, password, email)
				u.put()

				self.login(u)
				self.redirect('/')