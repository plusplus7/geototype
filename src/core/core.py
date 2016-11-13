# -*- coding: UTF-8 -*-

import math

class Core():
    def __init__(self):
        self.flying_objects = {}
        self.bullets        = {}
        pass

    def add_flying_object(self, name, entity):
        self.flying_objects[name] = entity

    def add_bullet(self, name, entity):
        self.bullets[name] = entity

    def check_collision(self):
        def distance(x1, x2, y1, y2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2
        def collide(f_obj, b_obj):
            b_pts = b_obj.points()
            return distance(b_pts[0][0], f_obj.x, b_pts[1][1], f_obj.y) <= 2*math.sqrt(f_obj.length)\
            and distance(b_pts[1][0], f_obj.x, b_pts[1][1], f_obj.y) <= 2*math.sqrt(f_obj.length)

        for f_name in self.flying_objects.keys():
            f_obj = self.flying_objects[f_name]
            for b_name in  self.bullets.keys():
                b_obj = self.bullets[b_name]
                if collide(f_obj, b_obj) == True:
                    f_obj.health -= b_obj.dmg
                    self.bullets.pop(b_name)
                    if f_obj.health <= 0:
                        self.flying_objects.pop(f_name)

    def get_entities(self):
        return [
            self.flying_objects,
            self.bullets,
        ]


