from tornado import web

class index(web.RequestHandler):
    def get(self):
        self.render('main/index.html')
