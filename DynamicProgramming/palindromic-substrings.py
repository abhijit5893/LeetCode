#https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        count = 0
        dp = [[0 for x in range(n)] for y in range(n)]

        for i in range(n):
            dp[i][i] = 1
            count += 1

        for col in range(1,n):
            for row in range(i):
                if row == col-1 and s[row] == s[col]:
                    dp[row][col] = 1
                    count += 1
                elif  dp[row+1][col-1] and s[row] == s[col]:
                    dp[row][col] = 1
                    count+= 1
        return count
