# -*- coding: UTF-8 -*-

import math
#from .. import entity
#from ..entity import bullet
#from ..entity import flying_object
#from ..entity.bullet import Bullet
#from ..entity.flying_object import FlyingObject

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
        '''self.flying_object.x = fobj.x
        self.flying_object.y = fobj.y
        self.flying_object.speed = fobj.speed
        self.flying_object.obj_type = fobj.obj_type
        '''
        self.flying_object.health = fobj.health
        '''self.bullet.x = bobj.x
        self.bullet.y =bobj.y
        self.bullet.dg = bobj.dg
        self.bullet.l = bobj.l
        self.bullet.sp = bobj.sp
        '''
        self.bullet.dmg = bobj.dmg
        '''
        self.bullet.dx = bobj.dx
        self.bullet.dy = bobj.dy'''
        flag = 0

        def distance(x1, x2, y1, y2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2
        # print distance(bobj.x,fobj.x,bobj.y,fobj.y)
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


