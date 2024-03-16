"""function_tests.py"""

import unittest
from selection_sort import selection_sort
from book import Book
from function_definitions import selection_sort_books, swap_case, str_translate

class Lab6Tests(unittest.TestCase):

    def test_selection_sort1(self):
        values = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]

        selection_sort(values)

        self.assertEqual(expected, values)

    def test_selection_sort2(self):
        values = [-100, 100, 0, -100, 100]
        expected = [-100, -100, 0, 100, 100]

        selection_sort(values)

        self.assertEqual(expected, values)

    def test_selection_sort3(self):
        values = []
        expected = []

        selection_sort(values)

        self.assertEqual(expected, values)

    def test1(self):
        self.assertEqual([],selection_sort_books([]))
    def test2(self):
        self.assertEqual([Book("asdf", "fda"), Book("ffff", "ffff")], [Book("asdf", "fda"), Book("ffff", "ffff")])
    def test3(self):
        self.assertEqual("asdfAUIDFDJKnnJ", swap_case("ASDFauidfdjkNNj"))
    def test4(self):
        self.assertEqual("", swap_case(''))
    def test5(self):
        self.assertEqual("0sdf12t40f", str_translate("asdf12t4af", "a", "0"))
    def test6(self):
        self.assertEqual("", str_translate("","",""))
if __name__ == '__main__':
    unittest.main()
