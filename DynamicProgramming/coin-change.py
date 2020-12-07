#https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
