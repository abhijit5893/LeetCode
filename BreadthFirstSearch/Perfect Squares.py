#https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n)) * int(sqrt(n)) == n: return 1

        pool = []
        for i in range(1, int(sqrt(n)) + 1):
            pool.append(i * i)

        step = 0
        rest = {n}
        while True:
            step += 1
            temp = set()
            for r in rest:
                for p in pool:
                    if r - p < 0:
                        break
                    else:
                        if r - p in pool:
                            return step + 1

                    temp.add(r - p)
                    rest = temp



