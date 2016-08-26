import os
from tornado.options import define, options
from config.routes import urls
from tornado import web, ioloop

settings = dict(
    autoreload=True,
    compiled_template_cache=False,
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates")
)

# define("port", default="3000", type=int)

if __name__ == "__main__":
    app = web.Application(urls, **settings)
    app.listen(3000)
    print("server at port 3000")
    options.parse_command_line()
    ioloop.IOLoop.current().start()
