#https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        for col in range(cols):
            for row in range(rows):
                x,y = float('inf'),float('inf')
                if row - 1 >= 0:
                    x = grid[row-1][col]
                if col - 1 >= 0:
                    y = grid[row][col-1]
                if x != float('inf') or y != float('inf'):
                    grid[row][col] = grid[row][col] + min(x,y)
        return grid[rows-1][cols-1]



