import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        s = "aa"
        p = "a"
        expected = False
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test_case_2(self):
        s = "aa"
        p = "a*"
        expected = True
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test_case_3(self):
        s = "ab"
        p = ".*"
        expected = True
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test_case_4(self):
        s = "aaa"
        p = "a*a"
        expected = True
        self.assertEqual(self.solution.isMatch(s, p), expected)

if __name__ == "__main__":
    unittest.main(verbosity=0)