#https://leetcode.com/problems/divide-two-integers/submissions/
import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    	#Cheating Method
        if dividend / divisor < (-1 << 31) or  dividend / divisor > ((1 << 31) - 1):
            return ((1 << 31) - 1)
        else:
            symbol = -1 if dividend * divisor < 0 else 1
            return math.ceil(dividend/divisor) if dividend * divisor < 0 else math.floor(dividend/divisor)