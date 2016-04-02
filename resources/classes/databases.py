from google.appengine.ext import db
from .. import funct

## WIKI DATABASE
def wiki_key(name = 'default'):
	return db.Key.from_path('wiki', name)

class Wiki(db.Model):
	url = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	last_modified = db.DateTimeProperty(auto_now = True)



## USER DATABASE
def users_key(group = 'default'):
	return db.Key.from_path('users', group)

class User(db.Model):
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.StringProperty()

	@classmethod
	def by_id(cls, uid):
		return User.get_by_id(uid, parent = users_key())

	@classmethod
	def by_name(cls, name):
		u = User.all().filter('username =', name).get()
		return u

	@classmethod
	def register(cls, name, pw, email=None):
		pw_hash = funct.WikiF.make_pw_hash(name, pw)
		return User(parent = users_key(), username = name, password = pw_hash, email = email)

	@classmethod
	def login(cls, name, pw):
		u = cls.by_name(name)
		if u and funct.WikiF.valid_pw(name, pw, u.password):
			return u