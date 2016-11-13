# -*- coding: UTF-8 -*-

import math

class Bullet():

    def __init__(self, x, y, degree, length, speed, damage):
        self.x  = x
        self.y  = y
        self.dg = degree
        self.l  = length
        self.sp = speed

        self.dx = self.sp * math.sin(math.radians(self.dg))
        self.dy = self.sp * math.cos(math.radians(self.dg))

        self.dmg = damage

        self.__points = self.__generate_points()

    def move(self):
        for pt in self.__points:
            pt[0] = pt[0] + self.dx
            pt[1] = pt[1] + self.dy
        self.x = pt[0]
        self.y = pt[1]

    def points(self):
        return self.__points

    def __generate_points(self):
        return [
            [self.x, self.y],
            [self.x + self.l * math.sin(math.radians(self.dg)),
             self.y + self.l * math.cos(math.radians(self.dg))],
        ]
