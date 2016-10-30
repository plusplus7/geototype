# -*- coding: UTF-8 -*-

class GameServer():

    PLAYER  = 0
    WATCHER = 1

    def __init__(self, room_limit):
        self.limit = room_limit
        self.rooms = {}

    def create_room(self, room_id):
        if room_id in self.rooms:
            return "Roomname already exists"
        if len(self.rooms) >= room_limit:
            return "The number of room is out of limit"

        self.rooms[room_id] = {}
        return "Success"

    def get_room_list(self):
        return self.rooms.keys()

    def add_player(self, room_id, sock):
        self.rooms[room_id][sock.sock_id] = sock

    def del_player(self, room_id, sock):
        self.rooms[room_id].pop(sock.sock_id)

    def announce(self, room_id, msg):
        for i in self.rooms.keys():
            try:
                self.socks[i].write_message(msg)
            except Exception as e:
                print e
