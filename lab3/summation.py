"""summation.py"""
import unittest

class testers(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_of_integers(5), 15)
    def test2(self):
        self.assertEqual(sum_of_integers(4), 10)


def sum_of_integers(n: int) -> int:
    """Return the sum of values from 0 to n."""
    i = 1
    val = 0
    while i<=n:
        val+=i
        i+=1
    return val

if __name__ == '__main__':
    unittest.main()
