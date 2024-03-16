"""function_tests.py

Write each unit test to your function definitions as its own test method in the class below.

You will need to import your functions.
"""
import unittest

from point import Point
from function_definitions import first_element, x_coordinates, are_in_positive_quadrant, distance, manhattan_distance, origin_distances


class Lab5Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual([1.2, 7.8, 11.12, 13.14], first_element([[1.2, 3.4, 5.6], [], [7.8, 9.0], [11.12], [], [13.14, 15.16]]))
    def test2(self):
        self.assertEqual([1, 2], first_element([[1], [2], []]))

    def test3(self):
        self.assertEqual([3, 4], x_coordinates([Point(3, 5), Point(4, 6)]))
    def test4(self):
        self.assertEqual([3], x_coordinates([Point(3, 6)]))

    def test5(self):
        self.assertEqual([Point(3, 4)], are_in_positive_quadrant([Point(3,4), Point(-4,3)]))
    def test6(self):
        self.assertEqual([], are_in_positive_quadrant([Point(-1, -2)]))

    def test7(self):
        self.assertEqual(5.0, distance(Point(0, 0), Point(3, 4)))
    def test8(self):
        self.assertEqual(0, distance(Point(0, 0), Point(0,0)))

    def test9(self):
        self.assertEqual(2, (manhattan_distance(Point(3, 5), Point(4, 6))))

    def test10(self):
        self.assertEqual(0, manhattan_distance(Point(0,0), Point(0,0)))

    def test11(self):
        self.assertEqual([5.0, 7.211102550927978], origin_distances(Point(3, 4), Point(4, 6)))
    def test12(self):
        self.assertEqual([0,0], origin_distances(Point(0,0), Point(0,0)))
if __name__ == '__main__':
    unittest.main()
