"""function_tests.py

Write each unit test to your function definitions as its own test method in the class below.

You will need to import your functions.
"""
import unittest
from book import Book
from geometry import Point, Rectangle, Circle
from employee import Employee
from price import Price
from function_definitions import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_perimeter, books_by_author, circle_bound, below_pay_average

class Homework4Tests(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(9, vowel_count("adei ousu eqa .*&%$#isf")) # expected, actual
    def test_1b(self):
        self.assertEqual(0, vowel_count("bcdfghj")) # expected, actual

    def test_2a(self):
        self.assertEqual([[1, 2]], short_lists([[1, 2], [4, 5, 6], [7, 8, 9]]))
    def test_2b(self):
        self.assertEqual([], short_lists([[1, 2, 2], [4, 5, 6], [7, 8, 9]]))

    def test3a(self):
        self.assertEqual([[1, 2], [12, 1, 16], [9, 11]], ascending_pairs([[1, 2], [12, 1, 16], [11, 9]]))
    def test3b(self):
        self.assertEqual([], ascending_pairs([]))

    def test4a(self):
        self.assertEqual(Price(13, 40), add_prices(Price(3, 41), Price(9, 99)))
    def test4b(self):
        self.assertEqual(Price(7, 9), add_prices(Price(3, 4), Price(4, 5)))
    def test5a(self):
        self.assertEqual(17.6, rectangle_perimeter(Rectangle(Point(3.2, 4), Point(7,9))))
    def test5b(self):
        self.assertEqual(134, rectangle_perimeter(Rectangle(Point(3, 5), Point(66, 9))))

    def test6a(self):
        self.assertEqual([Book("book2", "a2"), Book("book3", "a2")], books_by_author("a2", [Book("book1", "a1"), Book("book2", "a2"), Book("book3", "a2"), Book("book4", "a9"), Book("book11", "a1")]))
    def test6b(self):
        self.assertEqual([], books_by_author("adsf", []))

    def test7a(self):
        self.assertEqual(Circle(Point(8, 10), 4.00), circle_bound(Rectangle(Point(4, 12), Point(12, 8))))
    def test7b(self):
        self.assertEqual(Circle(Point(7.5, 7.5), 2.500), circle_bound(Rectangle(Point(5, 5), Point(10, 10))))

    def test8a(self):
        self.assertEqual(['Joe'], below_pay_average([Employee("john", 33.0), Employee("Joe", 11.0)]))
    def test8b(self):
        self.assertEqual([], below_pay_average([]))
if __name__ == '__main__':
    unittest.main()
