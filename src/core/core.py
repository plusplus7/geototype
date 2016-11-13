# -*- coding: UTF-8 -*-

import math

class Core():
    def __init__(self):
        pass

    def add_flying_object(self, name, entity):
        self.fobj_name = name
        self.flying_object = entity

    def add_bullet(self, name, entity):
        self.bobj_name = name
        self.bullet = entity


    def check_collision(self, fobj, bobj):
        self.flying_object.health = fobj.health
        self.bullet.dmg = bobj.dmg
        flag = 0

        def distance(x1, x2, y1, y2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2
        if distance(bobj.x,fobj.x,bobj.y,fobj.y) <= 2*math.sqrt(2):
                flag = 1
                self.flying_object.health -= 1
                self.bullet = None
        if(flag):
            return 1
        else:
            return -1




    def get_entities(self):
        return [
            {"p1": self.flying_object},
            {"b1": self.bullet}
        ]


