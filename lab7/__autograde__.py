import unittest
import os
from lab07 import main


class TestLab07(unittest.TestCase):
    def setUp(self):
        if os.path.exists("output.txt"):
            os.remove("output.txt")

        self.expected_output = [
            "1 + 2 = 3\n",
            "3 + 4 = 7\n",
            "5 + 6 = 11\n",
            "9 + 10 = 19\n",
            "17 + 18 = 35\n"
        ]

    def test_main(self):
        main()

        self.assertTrue(os.path.exists("output.txt"))

        with open("output.txt", 'r') as f:
            output_lines = f.readlines()

        self.assertEqual(output_lines, self.expected_output)

    def tearDown(self):
        if os.path.exists("output.txt"):
            os.remove("output.txt")


if __name__ == '__main__':
    unittest.main()
