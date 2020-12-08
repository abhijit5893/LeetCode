#https://leetcode.com/problems/01-matrix/
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        def bfs(i,j):
            q = deque()
            q.append([i,j,0])
            while q:
                m, n, dist = q.popleft()
                if matrix[m][n] == 0:
                    matrix[i][j] = dist
                    return 0

                for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0<= m +x <rows and 0<= n + y <cols: q.append([m+x,n+y,dist+1])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    bfs(i,j)
        return matrix



