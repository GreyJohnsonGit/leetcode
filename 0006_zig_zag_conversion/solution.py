class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        single_row = numRows == 1
        if single_row:
            return s
        
        max_location_index = 2 * numRows - 2
        rows = [[] for _ in range(numRows)]

        for index in range(len(s)):
            location = index % max_location_index
            is_on_diagonal = location >= numRows
            if is_on_diagonal:
                location = max_location_index - location
            rows[location].append(s[index])
        return ''.join([''.join(row) for row in rows])