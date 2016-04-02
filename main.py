#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from resources.funct import WikiV
from resources.funct import WikiF

from resources.classes import mainHandler
from resources.classes import logout
from resources.classes import edit
from resources.classes import login
from resources.classes import signup
from resources.classes import history

import webapp2

app = webapp2.WSGIApplication([('/', mainHandler.MainHandler),
						       ('/login', login.Login),
						       ('/signup', signup.Signup),
						       ('/logout', logout.Logout),
						       ('/_history' + WikiV.PAGE_RE, history.History),
						       ('/_edit' + WikiV.PAGE_RE, edit.EditPage),
						       (WikiV.PAGE_RE, mainHandler.MainHandler)],
							   debug=True)