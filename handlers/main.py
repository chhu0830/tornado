from handlers.application import RequestHandler

class index(RequestHandler):
  def get(self):
    self.render('main/index.html')
