import unittest

from coins import get_max_quarters


class CoinsTest(unittest.TestCase):

    def test_example(self):
        expected = 14
        actual = get_max_quarters(360)
        self.assertEqual(expected, actual)

    # Insert your test methods below
    def test_1(self):
        expected = 8
        actual = get_max_quarters(200)
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = 7
        actual = get_max_quarters(197)
        self.assertEqual(expected, actual)
    # Insert your test methods above


if __name__ == '__main__':
    unittest.main()
