# -*- coding: UTF-8 -*-

import unittest

import flying_object


class FlyingObjectTest(unittest.TestCase):

    def testFlyingObject(self):
        p = flying_object.FlyingObject(0, 0, 10, flying_object.QUADRANGLE, 100)
        pt = p.points()
        print pt
        self.assertAlmostEqual(-2, pt[0][0])
        self.assertAlmostEqual(-2, pt[0][1])
        self.assertAlmostEqual(2, pt[1][0])
        self.assertAlmostEqual(-2, pt[1][1])
        self.assertAlmostEqual(2, pt[2][0])
        self.assertAlmostEqual(2, pt[2][1])
        self.assertAlmostEqual(-2, pt[3][0])
        self.assertAlmostEqual(2, pt[3][1])

if __name__ == "__main__":
    unittest.main()
