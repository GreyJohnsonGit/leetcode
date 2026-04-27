# Could be improve by traversing like a binary search (i.e. find the longest palindrome then stop)
class Solution(object):
    def is_palidrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
    
    def longestPalindrome(self, s: str) -> str:
        debug = False
        # Convert to all strings to odd length (e.g. "ab" [2] to "#a#a#" [5])
        s = '#' + '#'.join(s) + '#'
        if debug: print(f"Input: {s}")

        radius = 1
        center = radius
        current_best_palindrome = ""
        while center < len(s):
            left = center - radius
            right = center + radius
            if debug: print(f"center: {center}, radius: {radius}, left: {left}, right: {right}")

            palindrome_cannot_fit = left < 0
            if palindrome_cannot_fit:
                center += 1
                continue
        
            palidrome_cannot_be_big_enough = right >= len(s)
            if palidrome_cannot_be_big_enough:
                break

            is_not_palidrome_at_radius = s[left] != s[right]
            if palidrome_cannot_be_big_enough or is_not_palidrome_at_radius:
                center += 1
                continue

            radial_slice = s[left:right+1]
            is_palidrome = self.is_palidrome(radial_slice)
            if is_palidrome:
                current_best_palindrome = radial_slice
                radius += 1
            else:
                center += 1
        if debug: print(F"Iteration Ratio: {center / len(s)}, current_best_palindrome: {current_best_palindrome}")

        return current_best_palindrome.replace('#', '')