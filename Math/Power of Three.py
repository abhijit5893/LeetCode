# https://leetcode.com/problems/power-of-three/
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 2:
            if n % 3 > 0: return False
            n = n / 3
        return n == 1
        '''
        One liner - Yaaay
        return round(math.log(n,3),10) % 1 ==0 if n > 0 else False
        '''

