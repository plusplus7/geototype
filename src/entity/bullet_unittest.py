# -*- coding: UTF-8 -*-

import math
import unittest

import bullet


class BulletUnitTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFlyingBullet45(self):
        b = bullet.Bullet(0, 0, 45, math.sqrt(18), math.sqrt(2), 100)
        print b.points()
        self.assertAlmostEqual(0, b.points()[0][0])
        self.assertAlmostEqual(0, b.points()[0][1])
        self.assertAlmostEqual(3, b.points()[1][0])
        self.assertAlmostEqual(3, b.points()[1][1])

        b.move()
        print b.points()
        self.assertAlmostEqual(1, b.points()[0][0])
        self.assertAlmostEqual(1, b.points()[0][1])
        self.assertAlmostEqual(4, b.points()[1][0])
        self.assertAlmostEqual(4, b.points()[1][1])

        b.move()
        print b.points()
        self.assertAlmostEqual(2, b.points()[0][0])
        self.assertAlmostEqual(2, b.points()[0][1])
        self.assertAlmostEqual(5, b.points()[1][0])
        self.assertAlmostEqual(5, b.points()[1][1])

    def testFlyingBullet30(self):
        b = bullet.Bullet(0, 0, 30, 4, 2, 100)
        print b.points()
        self.assertAlmostEqual(0, b.points()[0][0])
        self.assertAlmostEqual(0, b.points()[0][1])
        self.assertAlmostEqual(2, b.points()[1][0])
        self.assertAlmostEqual(2 * math.sqrt(3), b.points()[1][1])

        b.move()
        print b.points()
        self.assertAlmostEqual(1, b.points()[0][0])
        self.assertAlmostEqual(math.sqrt(3), b.points()[0][1])
        self.assertAlmostEqual(3, b.points()[1][0])
        self.assertAlmostEqual(3 * math.sqrt(3), b.points()[1][1])

        b.move()
        b.move()
        print b.points()
        self.assertAlmostEqual(3, b.points()[0][0])
        self.assertAlmostEqual(3 * math.sqrt(3), b.points()[0][1])
        self.assertAlmostEqual(5, b.points()[1][0])
        self.assertAlmostEqual(5 * math.sqrt(3), b.points()[1][1])

if __name__ == '__main__':
    unittest.main()
