class Solution:
    # Time complexity: O(log(x))
    # Space complexity: O(1)
    # Possible Improvements: 
    # None
    def reverse(self, x: int) -> int:
        max_pos_int = 2**31 - 1
        max_neg_int = 2**31
        is_neg = x < 0
        sign = -1 if is_neg else 1
        max_int = max_neg_int if is_neg else max_pos_int

        original = abs(x)
        reverse_sum = 0
        while original > 0:
            next_digit = original % 10

            would_create_overflow = ((max_int - next_digit) // 10) < reverse_sum
            if would_create_overflow:
                return 0

            reverse_sum = reverse_sum * 10 + next_digit
            original //= 10

        return sign * reverse_sum