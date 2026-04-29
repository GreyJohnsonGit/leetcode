import unittest
from solution import Solution

class TestZigZagConversion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_valid_conversions(self):
        result = self.solution.convert("PAYPALISHIRING", 3)
        self.assertEqual(result, "PAHNAPLSIIGYIR")

    def test_single_conversion(self):
        result = self.solution.convert("PAYPALISHIRING", 4)
        self.assertEqual(result, "PINALSIGYAHRPI")

    def test_001(self):
        result = self.solution.convert("A", 1)
        self.assertEqual(result, "A")

    def test_002(self):
        result = self.solution.convert("AC", 1)
        self.assertEqual(result, "AC")

if __name__ == "__main__":
    unittest.main(verbosity=0)