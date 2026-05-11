import unittest
from solution import Solution

INT_MAX = 2**31 - 1
INT_MIN = -2**31

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.myAtoi("42"), 42)

    def test_example_2(self):
        self.assertEqual(self.solution.myAtoi("   -42"), -42)

    def test_example_3(self):
        self.assertEqual(self.solution.myAtoi("1337c0d3"), 1337)

    def test_example_4(self):
        self.assertEqual(self.solution.myAtoi("0-1"), 0)

    def test_example_5(self):
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)

    def test_example_6(self):
        self.assertEqual(self.solution.myAtoi("-91283472332"), INT_MIN)

    def test_example_7(self):
        self.assertEqual(self.solution.myAtoi("91283472332"), INT_MAX)
        

if __name__ == "__main__":
    unittest.main(verbosity=0)