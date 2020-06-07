# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        table = dict()
        table['0'] = 0
        table['1'] = 1
        for i in range(2, 10):
            table[str(i)] = i * i

        counter = set()
        counter.add(n)
        while n != 1:
            happy = 0
            for i in str(n):
                happy += table[i]
            counter.add(n)
            if happy in counter:
                return False
            if happy == 1:
                return True
            n = happy

        return True
