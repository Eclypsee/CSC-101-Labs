import unittest

from summation import summation


class Lab4TestCases(unittest.TestCase):
    def test_summation_1(self):
        result = summation([0, 1, 2, 3])
        expected = 6
        self.assertEqual(expected, result)

    def test_summation_2(self):
        result = summation([4, 10, 3, 3])
        expected = 20
        self.assertEqual(expected, result)

    def test_summation_3(self):
        result = summation([3, 2, 1, 0])
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
