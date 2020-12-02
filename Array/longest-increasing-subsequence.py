#https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        m = 0
        for i in range(n):
            m = max(m, lis[i])
        return m
