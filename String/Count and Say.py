#https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        s, m = "1", 1
        for _ in range(1, n):
            tmp, l = '', len(s)
            for i, c in enumerate(s, 1):
                if i == l or s[i] != c:
                    tmp += str(m)+c
                    m = 1
                else:
                    m += 1
            s = tmp
        return s