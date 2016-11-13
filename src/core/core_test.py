# -*- coding: UTF-8 -*-

import math
import sys
import unittest
import core

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
        p1 = flying_object.FlyingObject(0, 0, 1, flying_object.QUADRANGLE, 10)
        b1 = bullet.Bullet(5, 5, 225, math.sqrt(2), 1, 1)

        self.c.add_flying_object("p1", p1)
        self.c.add_bullet("b1", b1)

        ans_init = self.c.check_collision()
        #判断最开始子弹是否直接碰撞
        r = self.c.get_entities()


        # 子弹未击中飞机，飞机hp不变
        self.assertEqual(r[0]["p1"].health, 10)
        # 子弹未击中飞机，子弹不消失
        self.assertEqual(len(r[1].keys()), 1)
        #
        b1.move()
        b1.move()
        b1.move()
        b1.move()
        b1.move()

        #print str(p1.x) +" "+ str(p1.y)
        cur = self.c.check_collision()

        r = self.c.get_entities()
        print r

        # 子弹击中飞机，飞机hp-1
        self.assertEqual(r[0]["p1"].health, 9)
        #print p1.health
        # 子弹击中飞机，子弹消失
        self.assertEqual("b1" in r[1], False)


if __name__ == "__main__":
    unittest.main()
