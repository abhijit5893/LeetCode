#https://leetcode.com/problems/maximum-subarray/
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -sys.maxsize -1
        max_ending = 0
        for num in nums:
            max_ending = max_ending + num
            if max_so_far < max_ending:
                max_so_far = max_ending
            if max_ending < 0:
                max_ending = 0
        return max_so_far



