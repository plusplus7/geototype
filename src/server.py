# -*- coding: UTF-8 -*-

import stage
import time

class GameServer():

    PLAYER  = 0
    WATCHER = 1

    def __init__(self, ioloop, room_limit):
        self.ioloop = ioloop
        self.limit  = room_limit
        self.rooms  = {}

    def create_room(self, room_id):
        if room_id in self.rooms:
            return "Roomname already exists"
        if len(self.rooms) >= self.limit:
            return "The number of room is out of limit"

        self.rooms[room_id] = [] 
        self.rooms[room_id].append(stage.load_stage("demo1"))
        self.rooms[room_id].append({})
        self.ioloop.add_timeout(time.time() + 0.045, lambda:self.send_view(room_id))
        self.ioloop.add_timeout(time.time() + 0.015, lambda:self.run_loop(room_id))
        return "Success"

    def get_room_list(self):
        return self.rooms.keys()

    def player_input(self, sock, dir):
        sock.input_dir = dir

    def run_loop(self, room_id):
        for i in self.rooms[room_id][1].keys():
            sock = self.rooms[room_id][1][i]
            if sock.input_dir != None:
                self.rooms[room_id][0].player_operate(10000, i, sock.input_dir)
                sock.input_dir = None

        self.rooms[room_id][0].run()

        self.ioloop.add_timeout(time.time() + 0.015, lambda:self.run_loop(room_id))

    def send_view(self, room_id):
        self.announce(room_id, self.rooms[room_id][0].get_view())
        self.ioloop.add_timeout(time.time() + 0.045, lambda:self.send_view(room_id))

    def add_player(self, sock):
        self.rooms[sock.room_id][1][sock.sock_id] = sock
        if sock.user_type == GameServer.PLAYER:
            return self.rooms[sock.room_id][0].add_player(sock.sock_id, sock.nick_id)
        else:
            return "%s joined as watcher" % (sock.nick_id, )

    def del_player(self, sock):
        if hasattr(sock, "room_id") and sock.user_type == GameServer.PLAYER:
            self.rooms[sock.room_id][0].del_player(sock.sock_id)
        return self.rooms[sock.room_id][1].pop(sock.sock_id)

    def get_player_list(self, room_id):
        res = []
        for i in self.rooms[room_id][1].keys():
            res.append(self.rooms[room_id][1][i].nick_id)
        return res

    def announce(self, room_id, msg):
        for i in self.rooms[room_id][1].keys():
            sock = self.rooms[room_id][1][i]
            try:
                sock.write_message(msg)
            except Exception as e:
                print e
