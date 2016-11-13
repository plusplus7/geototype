# -*- coding: UTF-8 -*-

WSOPEN = 1
WSJOIN = 2
WSINIT = 3
WSMOVE = 4
WSLEAVE = 5

class Message():

    @staticmethod
    def socket_open_response():
        return {
            "act" : WSOPEN,
        }

    @staticmethod
    def player_init_response(name, player_list):
        return {
            "act"           : WSINIT,
            "name"          : name,
            "player_list"   : player_list,
        }

    @staticmethod
    def player_join_response(name, user_type):
        return {
            "act"           : WSJOIN,
            "name"          : name,
            "user_type"     : user_type,
        }

    @staticmethod
    def player_leave_response(name):
        return {
            "act"           : WSLEAVE,
            "name"          : name,
        }