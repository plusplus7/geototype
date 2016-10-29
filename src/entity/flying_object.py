# -*- coding: UTF-8 -*-

class FlyingObject():
    QUADRANGLE = "quadrangle"
    def __init__(self, x, y, speed, obj_type):
        self.x = x
        self.y = y
        self.speed = speed
        self.points = self.__generate_points(obj_type)

    def move(self, degree):
        dx = self.speed * math.sin(math.radians(degree))
        dy = self.speed * math.cos(math.radians(degree))
        for pt in points:
            pt[0] = pt[0] + dx
            pt[1] = pt[1] + dy

    def points(self):
        return self.points

    def __generate_points(self, obj_type):
        if cmp(QUADRANGLE, obj_type):
            return [
                [x-2, y-2],
                [x+2, y-2],
                [x+2, y+2],
                [x-2, y+2],
            ]
        else:
            raise Exception('Unsupported object type')
