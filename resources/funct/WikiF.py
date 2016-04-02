import cgi
import WikiV
import hashlib
import hmac
import string
import random
import urllib2
from xml.dom import minidom
import json

## Scape HTML
def escape_html(s):
	return cgi.escape(s, quote = True)

## User, Mail and Password Validations
def valid_username(username):
	return WikiV.USER_RE.match(username)

def valid_password(password):
	return WikiV.PASS_RE.match(password)

def valid_mail(mail):
	return WikiV.MAIL_RE.match(mail)

def verification(pass1, pass2):
	if pass1 != pass2:
		return False
	return True


## Hashing, Salt and comprobation
def hash_md5(x):
	return hashlib.md5(x).hexdigest()

def hash_sha256(x):
	return hashlib.sha256(x).hexdigest()

def make_secure_val(s):
	return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    s = h.split('|')[0]
    if h == make_secure_val(s):
        return s

def hash_str(s):
	return hmac.new(WikiV.SECRET, s).hexdigest()

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=None):
    if not salt:
    	salt = make_salt()
    return '%s|%s' % (hash_str(name+pw+salt), salt)

def valid_pw(name, pw, h):
	salt = h.split('|')[1]
	return h == make_pw_hash(name, pw, salt)

## Json Converter
def render_json(self, d):
    json_txt = json.dumps(d)
    return json_txt

## URL Creator
def url_creator(v):
	url = ''
	for data in v:
		url += "/" + data
	return url

## HTML Scaping
def html_scape(text):
	return text.replace('\n', '<br>')

def html_unscape(text):
	return text.replace('<br>', '\n')