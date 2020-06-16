#https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        out = 0
        while n > 1:
            out += n//5
            n = n//5
        return out