from handler import *
from databases import *
from .. import funct

class EditPage(Handler):
    def get(self, page_name):
    	if ('/_edit' in page_name) or ('/_history' in page_name):
    		self.redirect('/')

    	ver = self.request.get("v")

    	if ver:
            key = db.Key.from_path('Wiki', int(ver), parent=wiki_key())
            page = db.get(key)
        else:
            page = db.GqlQuery("SELECT * FROM Wiki WHERE url = :url ORDER BY created DESC LIMIT 1", url = page_name).get()

    	if self.user:
    		if page:
    			self.render("edit.html", url=page_name, content=page.content, user=self.user, page=page, full_url=self.request.url)
    		else:
    			self.render("edit.html", url=page_name, user=self.user, full_url=self.request.url)
    	else:
    		self.redirect("/login")

    def post(self, page_name):
        if not self.user:
            self.redirect('/login')
        
        content = funct.WikiF.html_unscape(self.request.get('content'))

        if content:
        	p = Wiki(parent = wiki_key(), url = page_name, content = content)
        	p.put()
        	self.redirect('%s' % str(page_name))
        else:
            error = "Insert Valid Content Please"
            self.render("edit.html", content=content, error=error, full_url=self.request.url)