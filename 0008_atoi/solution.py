INT_MAX = 2**31 - 1
INT_MIN = -2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        accumulator = 0
        index = 0
        sign = 1

        while index < len(s) and s[index] == ' ':
            index += 1

        if index == len(s):
            return accumulator
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            accumulator = accumulator * 10 + int(s[index])
            index += 1

        accumulator *= sign

        if sign == 1 and accumulator > INT_MAX:
            return INT_MAX
        
        if sign == -1 and accumulator < INT_MIN:
            return INT_MIN

        return accumulator