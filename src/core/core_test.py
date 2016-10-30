# -*- coding: UTF-8 -*-

import unittest
import math
import core
import sys
sys.path.append("..")
from entity import bullet
from entity import flying_object

class CoreTest(unittest.TestCase):

    def setUp(self):
        self.c = core.Core()
        pass

    def tearDown(self):
        pass

    def testGeneralCase1(self):
        p1 = flying_object.FlyingObject(0, 0, 1, flying_object.QUADRANGLE, 1)
        b1 = bullet.Bullet(5, 5, 45, math.sqrt(2), 1, 10)

        self.c.add_flying_object("p1", p1)
        self.c.add_bullet("b1", b1)

        self.c.check_collision()
        r = self.c.get_entities()
        # 子弹未击中飞机，飞机hp不变
        self.assertEqual(r[0]["p1"].health, 10)
        # 子弹未击中飞机，子弹不消失
        self.assertEqual(len(r[1].keys()), 1)

        b1.move()
        b1.move()
        b1.move()
        b1.move()

        self.check_collision()
        r = self.get_entities()

        # 子弹击中飞机，飞机hp-1
        self.assertEqual(r[0]["p1"].health, 9)
        # 子弹击中飞机，子弹消失
        self.assertEqual(len(r[1].keys()), 0)

if __name__ == "__main__":
    unittest.main()
