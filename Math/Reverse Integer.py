# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            result = result * 10 + x % 10
            x //= 10

        return 0 if result > pow(2, 31) else result * symbol
        '''
        Bad since i used strings to do it
        res = 0
        if x > 0:
            res = int(str(x)[::-1])
        else:
            res = -1 * int(str(-1*x)[::-1])

        return  res if res < (1 << 31) - 1 and res > (-1 << 31) else 0
        '''