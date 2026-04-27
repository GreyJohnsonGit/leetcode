import unittest
from solution import Solution


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_valid_palindromes(self):
        result = self.solution.longestPalindrome("babad")
        self.assertIn(result, ["aba", "bab"])

    def test_single_palindrome(self):
        result = self.solution.longestPalindrome("cbbd")
        self.assertEqual(result, "bb")

    def test_001(self):
        result = self.solution.longestPalindrome("a")
        self.assertEqual(result, "a")

    def test_002(self):
        result = self.solution.longestPalindrome("ac")
        self.assertIn(result, ["a", "c"])

    def test_003(self):
        result = self.solution.longestPalindrome("abccbd")
        self.assertEqual(result, "bccb")

    def test_004(self):
        result = self.solution.longestPalindrome("abcdefghijklmnoqrstuvwxyz")
        self.assertIn(result, list("abcdefghijklmnoqrstuvwxyz"))


if __name__ == "__main__":
    unittest.main(verbosity=0)