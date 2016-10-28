# -*- coding: UTF-8 -*-

import os
import tornado.web
import tornado.websocket
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

urls = [
    (r'/', IndexHandler),
]

settings = {
    "static_path"   : os.path.join(os.path.dirname(__file__), "static"),
    "debug"         : True,
    "gzip"          : True,
}

def main(host="0.0.0.0", port=7777):
    app = tornado.web.Application(urls, **settings)
    app.listen(port, host)
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()

if __name__ == "__main__":
    main()
