#https://leetcode.com/problems/game-of-life/
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        copy_board = copy.deepcopy(board)
        for i in range(m):
            for j in range(n):
                total = 0
                for a,b in [[i+1,j], [i+1,j+1], [i+1,j-1],\
                               [i-1,j], [i-1,j-1], [i-1,j+1], \
                                     [i, j+1], [i,j-1]]:
                    if m > a >= 0 and n > b >=0:
                        total += copy_board[a][b]
                if copy_board[i][j] == 1:
                    if total < 2 or total > 3:  #Rule 1 and 3
                        board[i][j] =0
                    elif total == 2 or total == 3: #rule 2
                        board[i][j] = 1
                elif copy_board[i][j] == 0:
                    if total == 3:
                        board[i][j] = 1
