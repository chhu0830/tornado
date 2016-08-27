from tornado import web

class RequestHandler(web.RequestHandler):
    def prepare(self):
        super().prepare()
        try:
            print(self.get_argument('_method'))
            self.request.method = self.get_argument('_method').upper()
        except:
            pass
        print(self.request.method)

