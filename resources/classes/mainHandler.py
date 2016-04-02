from handler import *
from databases import *
from .. import funct

class MainHandler(Handler):
    def get(self, page_name=""):
    	ver = self.request.get("v")

    	if not page_name:
    		page_name = '/'

        if ver:
            key = db.Key.from_path('Wiki', int(ver), parent=wiki_key())
            page = db.get(key)
        else:
            page = db.GqlQuery("SELECT * FROM Wiki WHERE url = :url ORDER BY created DESC LIMIT 1", url = page_name).get()  	
  	    	
    	if page_name:
    	 	if page:
    	 		self.render('page.html', content = funct.WikiF.html_scape(page.content), url=page_name, user=self.user, full_url=self.request.url)
    	 	else:
    	 		self.redirect("/_edit" + page_name, permanent=False)
    	else:
    		if page:
    	 		self.render('page.html', content = funt.WikiF.html_scape(page.content), url=page_name, user=self.user, full_url=self.request.url)