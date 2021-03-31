#https://leetcode.com/problems/target-sum/
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        def dfs(nums, target, idx, curr_sum):
            if (idx, curr_sum) in memo:
                return memo[(idx,curr_sum)]

            if idx < 0 and target == curr_sum:
                return 1
            elif idx < 0:
                return 0

            x = dfs(nums, target, idx-1, curr_sum + nums[idx])
            y = dfs(nums, target, idx-1, curr_sum - nums[idx])
            memo[(idx,curr_sum)] = x + y

            return memo[(idx,curr_sum)]
        memo = {}
        return dfs(nums, S, len(nums)-1, 0)


