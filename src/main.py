# -*- coding: UTF-8 -*-

import os
import sys
import tornado.web
import tornado.websocket
import tornado.ioloop
import json
import random
import server
from message import *

server_name = ["Wahaha", "Gahaha", "Papapa", "Wuwuwu", "Yinyinyin"]
ws_host = 'localhost:7777'


ioloop = tornado.ioloop.IOLoop.instance()
server = server.GameServer(ioloop, 5)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",
            rooms = server.get_room_list()
        )

class GameHandler(tornado.web.RequestHandler):
    def post(self, room_id):
        username = self.get_argument("username")
        self.render("panel.html",
            room_id = room_id,
            username = username,
            host = ws_host
        )

class MessageHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        self.write_message(
            Message.socket_open_response()
        )
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
            self.write_message(
                Message.player_init_response(
                    self.nick_id + "#" + str(self.sock_id),
                    server.get_player_list(self.room_id)
                )
            )
            server.announce(self.room_id,
                Message.player_join_response(
                    self.nick_id + "#" + str(self.sock_id),
                    self.user_type
                )
            )
        elif message["act"] == WSMOVE:
            self.room_id    = message["room_id"]
            server.player_input(self, message["input"])

    def on_close(self):
        server.announce(self.room_id,
            Message.player_leave_response(
                    self.nick_id + "#" + str(self.sock_id)
            )
        )
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
    global ws_host
    ws_host = host + ':' + str(port)
    app.listen(port, host)
    ioloop.start()

if __name__ == "__main__":
    if len(sys.argv) != 1:
        main(sys.argv[1], sys.argv[2])
