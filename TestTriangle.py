# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

Updated/added more test for Triangle verification
Date:09/18/2021
@author: Emay Pandarakutty
email: epandar@stevens.edu

"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3,5,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4, 5, 6) is a Scalene triangle')

    def testIsoscelesTrianglesAB(self):
        self.assertEqual(classifyTriangle(7, 7, 8), 'Isoceles', '(7, 7, 8) is a Isoceles triangle')

    def testIsoscelesTrianglesAC(self):
        self.assertEqual(classifyTriangle(7, 8, 7), 'Isoceles', '(7, 8, 7) is a Isoceles triangle')

    def testIsoscelesTrianglesBC(self):
        self.assertEqual(classifyTriangle(8, 7, 7), 'Isoceles', '(8, 7, 7) is a Isoceles triangle')

    def testFloatInputA(self):
        self.assertEqual(classifyTriangle(1.23, 5, 6), 'InvalidInput', '(1.23, 5, 6) is a InvalidInput')

    def testFloatInputB(self):
        self.assertEqual(classifyTriangle(1, 5.3, 6), 'InvalidInput', '(1, 5.3, 6) is a InvalidInput')

    def testFloatInputC(self):
        self.assertEqual(classifyTriangle(1, 5, 6.3), 'InvalidInput', '(1, 5, 6.3) is a InvalidInput')

    def testStringInputA(self):
        self.assertEqual(classifyTriangle("a", 5, 6), 'TypeError', '("a", 5, 6) "a" InvalidInput datatype')

    def testStringInputB(self):
        self.assertEqual(classifyTriangle(1, "b", 6), 'TypeError', '(1, "b", 6) "b" InvalidInput datatype')

    def testStringInputC(self):
        self.assertEqual(classifyTriangle(1, 5, "c"), 'TypeError', '(1, 5, "c")  "c" InvalidInput datatype')

    def testMaxPlus1A(self):
        self.assertEqual(classifyTriangle(201,4,5),'InvalidInput','201,4,5 "a = Max+1" is a InvalidInput')

    def testMaxPlus1B(self):
        self.assertEqual(classifyTriangle(3,201,5),'InvalidInput','3,201,5 "b = Max+1" is a InvalidInput')

    def testMaxPlus1C(self):
        self.assertEqual(classifyTriangle(3,4,201),'InvalidInput','3,4,201 "c = Max+1" is a InvalidInput')

    def testMaxA(self):
        self.assertEqual(classifyTriangle(200, 198, 199), 'Scalene', '200, 198, 199 "a = Max" is a Scalene')

    def testMaxB(self):
        self.assertEqual(classifyTriangle(199, 200, 198), 'Scalene', '198, 200, 198 "b = Max" is a Scalene')

    def testMaxC(self):
        self.assertEqual(classifyTriangle(198, 199, 200), 'Scalene', '198, 199, 200 "c = Max" is a Scalene')

    def testMinA(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput', '0,4,5 "a = Min" is a InvalidInput')

    def testMinB(self):
        self.assertEqual(classifyTriangle(3, 0, 5), 'InvalidInput', '3,0,5 "b = Min" is a InvalidInput')

    def testMinC(self):
        self.assertEqual(classifyTriangle(3, 4, 0), 'InvalidInput', '3,4,0 "c = Min" is a InvalidInput')

    def testMinMinus1A(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput', '-1,4,5 "a = Min-1" is a InvalidInput')

    def testMinMinus1B(self):
        self.assertEqual(classifyTriangle(3, -1, 5), 'InvalidInput', '3,-1,5 "b = Min-1" is a InvalidInput')

    def testMinMinus1C(self):
        self.assertEqual(classifyTriangle(3, 4, -1), 'InvalidInput', '3,4,-1 "c = Min-1" is a InvalidInput')

    def testNotaTriangleA(self):
        self.assertEqual(classifyTriangle(16, 8, 7), 'NotATriangle', '(16, 8, 7) is NotATriangle')

    def testNotaTriangleB(self):
        self.assertEqual(classifyTriangle(7, 16, 8), 'NotATriangle', '(7, 16, 8) is NotATriangle')

    def testNotaTriangleC(self):
        self.assertEqual(classifyTriangle(7, 8, 16), 'NotATriangle', '(7, 8, 16) is NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

