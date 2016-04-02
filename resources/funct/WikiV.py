import re

## Regular Expressions
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

## Secret Password
SECRET = "Capt. Teemo"