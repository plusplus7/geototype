# -*- coding: UTF-8 -*-
import math

import math

QUADRANGLE      = "quadrangle"
QUADRANGLE_2    = "quadrangle2"

class FlyingObject():
    def __init__(self, x, y, speed, obj_type, health):
        self.x = x
        self.y = y
        self.speed  = speed
        self.health = health
        self.__points = self.__generate_points(obj_type)

    def move(self, degree):
        dx = self.speed * math.sin(math.radians(degree))
        dy = self.speed * math.cos(math.radians(degree))
        self.x = self.x + dx
        self.y = self.y + dy
        for pt in self.__points:
            pt[0] = pt[0] + dx
            pt[1] = pt[1] + dy


    def points(self):
        return self.__points

    def __generate_points(self, obj_type):
        if cmp(QUADRANGLE, obj_type) == 0:
            self.length = 4
            return [
                [self.x-2, self.y-2],
                [self.x+2, self.y-2],
                [self.x+2, self.y+2],
                [self.x-2, self.y+2],
            ]
        elif cmp(QUADRANGLE_2, obj_type) == 0:
            return [
                [self.x-4, self.y-4],
                [self.x+4, self.y-4],
                [self.x+4, self.y+4],
                [self.x-4, self.y+4],
            ]
        else:
            raise Exception('Unsupported object type')
