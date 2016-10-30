# -*- coding: UTF-8 -*-

import sys
sys.path.append("../../entity")
import flying_object
import time

class DemoStage():

    __PLAYER_LIMIT = 2
    __PLAYER_MOVE  = 10000

    def __init__(self):
        self.l  = 2
        self.ps = {}
        self.es = {}
        self.d  = {}
        for i in range(3):
            t = flying_object.FlyingObject(10 + i * 10, 40, 1, flying_object.QUADRANGLE_2, 100)
            self.es[i]  = t
            self.d[i]   = (((i&1) << 1 ) - 1) * 90
        pass

    def get_view(self):
        view = {
            "P" : {},
            "E" : {},
        }
        for i in self.ps.keys():
            view["P"][i] = self.ps[i].points()

        for i in self.es.keys():
            view["E"][i] = self.es[i].points()

        return view

    def run(self):
        for e in self.es.keys():
            print self.es[e].x
            if self.es[e].x <= 5:
                self.d[e] = 90
            if self.es[e].x >= 45:
                self.d[e] = -90

            self.es[e].move(self.d[e])
        pass

    def add_player(self, name):
        cnt = len(self.ps.keys())
        if cnt >= DemoStage.__PLAYER_LIMIT:
            return "Out of player limit"

        t = flying_object.FlyingObject(15 + cnt * 20, 5, 1, flying_object.QUADRANGLE, 100)
        self.ps[name] = t
        return "Player %s joined!" % (name,)

    def player_operate(self, op_type, name, data):
        if op_type == DemoStage.__PLAYER_MOVE:
            if name not in self.ps.keys():
                return "No such player"

            self.ps[name].move(data)
            return ""

if __name__ == "__main__":
    a = DemoStage()

    a.add_player(100)
    for i in range(100):
        a.run()
        print a.get_view()
        a.player_operate(10000, 100, 45)
        time.sleep(1)
