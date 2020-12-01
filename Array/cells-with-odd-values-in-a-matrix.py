#https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        out = [[0 for i in range(m)] for i in range(n)]
        for item in indices:
            for i in range(m):
                out[item[0]][i] += 1
            for i in range(n):
                out[i][item[1]] += 1

        count = 0
        for i in range(n):
            for j in range(m):
                if out[i][j] % 2==1:
                    count += 1
        return count