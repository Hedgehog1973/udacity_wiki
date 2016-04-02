from handler import *
from databases import *
from .. import funct

class History(Handler):
    def get(self, page_name):
        pages = Wiki.all().filter("url =", page_name).order("-created")

        if self.user:
        	if pages.get() == None:
        		self.redirect('/_edit' + page_name)
        	else:
        		self.render('history.html', pages=pages, user=self.user, full_url=self.request.url)
        else:
            self.redirect('/login')