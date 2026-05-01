import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_10(self):
        self.assertEqual(self.solution.reverse(10), 1)

    def test_123(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_n156(self):
        self.assertEqual(self.solution.reverse(-156), -651)
    
    def test_neg_int_max(self):
        self.assertEqual(self.solution.reverse(-2**31), 0)

    def test_pos_int_max(self):
        self.assertEqual(self.solution.reverse(2**31 - 1), 0)

if __name__ == "__main__":
    unittest.main(verbosity=0)