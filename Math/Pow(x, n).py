#https://leetcode.com/problems/powx-n/
import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
        '''
        if x > 0:
            return math.exp(n*math.log(x))
        else:
            return -1*math.exp(n*math.log(-1*x)) if n%2 == 1 else math.exp(n*math.log(-1*x))
       '''