# https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)

        tmp = 0
        prd = 1
        for i in str(s[::-1]):
            tmp += (ord(i) - ord('A') + 1) * prd
            prd *= 26
        return tmp