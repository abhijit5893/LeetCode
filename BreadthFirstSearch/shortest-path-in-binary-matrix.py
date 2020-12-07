#https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        rows, cols, q = len(grid), len(grid[0]), [(0,0,1)]
        while q:
            row, col, dist = q.pop(0)
            if row == rows-1 and col == cols-1: return dist
            for r, c in [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]:
                if r >= 0 and r < rows and c>= 0 and c < cols and not grid[r][c]:
                    q.append((r,c,dist+1))
                    grid[r][c] = 1
        return -1

