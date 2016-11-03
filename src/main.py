# -*- coding: UTF-8 -*-

import os
import tornado.web
import tornado.websocket
import tornado.ioloop
import json
import random
import server
from message import *

server_name = ["Wahaha", "Gahaha", "Papapa", "Wuwuwu", "Yinyinyin"]


ioloop = tornado.ioloop.IOLoop.instance()
server = server.GameServer(ioloop, 5)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", rooms = server.get_room_list())

class GameHandler(tornado.web.RequestHandler):
    def get(self, room_id):
        self.render("panel.html", room_id = room_id)

class MessageHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        self.write_message({
            "act"   : WSOPEN,
        })
        self.sock_id    = random.randint(1000000, 2000000)
        self.user_type  = server.PLAYER

    def on_message(self, msg):
        message = json.loads(msg)
        print message
        print message["act"]
        if message["act"] == WSJOIN:
            self.room_id    = message["room_id"]
            self.nick_id    = message["nick_id"]
            self.user_type  = message["user_type"]
            self.input_dir  = None
            server.add_player(self)
            self.write_message({
                "act"   : WSINIT,
                "data"  : server.get_player_list(self.room_id),
            })
            server.announce(self.room_id, {
                "act"       : WSJOIN,
                "nick_id"   : self.nick_id,
            })
        elif message["act"] == WSMOVE:
            self.room_id    = message["room_id"]
            server.player_input(self, message["input"])

    def on_close(self):
        print "%d left" % self.sock_id
        server.del_player(self)

urls = [
    (r'/', IndexHandler),
    (r'/game/(?P<room_id>[a-zA-Z0-9-_]+)', GameHandler),
    (r'/msg', MessageHandler),
]

settings = {
    "static_path"   : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "debug"         : True,
    "gzip"          : True,
}

def main(host="0.0.0.0", port=7777):
    for i in range(server.limit):
        print server.create_room(server_name[i])
    app = tornado.web.Application(urls, **settings)
    app.listen(port, host)
    ioloop.start()

if __name__ == "__main__":
    main()
