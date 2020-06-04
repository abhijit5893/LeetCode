# https://leetcode.com/problems/surrounded-regions/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        nr = len(board)
        if nr > 0:
            nc = len(board[0])

            def dfs(i, j, marker):
                print(i, j, marker)
                if i < nr and j < nc:
                    board[i][j] = marker
                    if i + 1 < nr and board[i + 1][j] == 'O': dfs(i + 1, j, marker)
                    if j + 1 < nc and board[i][j + 1] == 'O': dfs(i, j + 1, marker)
                    if i - 1 > 0 and board[i - 1][j] == 'O': dfs(i - 1, j, marker)
                    if j - 1 > 0 and board[i][j - 1] == 'O': dfs(i, j - 1, marker)

            # Check for zeros in the border
            for i in range(nr):
                for j in range(nc):
                    if i == 0 or j == 0 or i == nr - 1 or j == nc - 1:
                        if board[i][j] == 'O':
                            dfs(i, j, '-1')

            for i in range(nr):
                for j in range(nc):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'

            # Conver all -1 to O
            # Check for the rest
            for i in range(nr):
                for j in range(nc):
                    if board[i][j] == '-1':
                        board[i][j] = 'O'




