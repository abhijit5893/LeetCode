# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        bit = [0] * 32
        for i in range(32):
            bit[31 - i] = n >> i & 1  # Check if is 1 and then right shift

        res = 0
        for i in range(32):
            if bit[i] == 1:
                res |= 1 << i  # Insert 1 in the ith position
        return res