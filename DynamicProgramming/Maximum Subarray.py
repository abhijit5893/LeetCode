# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        max_so_far = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            #print(nums[i], curr_max, max_so_far)
            curr_max = max(nums[i], nums[i] + curr_max)
            max_so_far = max(curr_max, max_so_far)

        return max_so_far