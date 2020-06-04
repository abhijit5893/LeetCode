#https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
        DFS approach with recursion
        11110
        11010
        11000
        00000
        '''

        if not grid: return 0

        nr = len(grid)  # 4 - Rows
        nc = len(grid[0])  # 5 - Columns

        def foo(i, j):
            grid[i][j] = 0
            if i - 1 >= 0 and grid[i - 1][j] == '1': foo(i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1': foo(i, j - 1)
            if i + 1 < nr and grid[i + 1][j] == '1': foo(i + 1, j)
            if j + 1 < nc and grid[i][j + 1] == '1': foo(i, j + 1)

        nbr_of_islands = 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    foo(i, j)
                    nbr_of_islands += 1

        return nbr_of_islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
        DFS approach with stack
        11110
        11010
        11000
        00000
        '''

        if not grid: return 0

        nr = len(grid)  # 4 - Rows
        nc = len(grid[0])  # 5 - Columns

        stack = []
        nbr_of_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    stack.append((r, c))
                    nbr_of_islands += 1
                    while stack:
                        i, j = stack.pop()
                        grid[i][j] = 0
                        if i - 1 >= 0 and grid[i - 1][j] == '1':  stack.append((i - 1, j))
                        if j - 1 >= 0 and grid[i][j - 1] == '1':  stack.append((i, j - 1))
                        if i + 1 < nr and grid[i + 1][j] == '1':  stack.append((i + 1, j))
                        if j + 1 < nc and grid[i][j + 1] == '1':  stack.append((i, j + 1))

        return nbr_of_islands