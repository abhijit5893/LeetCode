class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
        BFS approach
        11110
        11010
        11000
        00000
        '''

        if not grid: return 0

        nr = len(grid)  # 4 - Rows
        nc = len(grid[0])  # 5 - Columns

        lands = set()
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    lands.add((r, c))

        nbr_of_islands = 0

        while lands:
            nbr_of_islands += 1
            i, j = lands.pop()
            queue = []
            queue.append((i, j))
            while queue:
                i, j = queue.pop(0)
                if (i - 1, j) in lands:
                    queue.append((i - 1, j))
                    lands.remove((i - 1, j))
                if (i, j - 1) in lands:
                    queue.append((i, j - 1))
                    lands.remove((i, j - 1))
                if (i + 1, j) in lands:
                    queue.append((i + 1, j))
                    lands.remove((i + 1, j))
                if (i, j + 1) in lands:
                    queue.append((i, j + 1))
                    lands.remove((i, j + 1))

        return nbr_of_islands