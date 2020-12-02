#https://leetcode.com/problems/3sum-closest/
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums: return nums
        min_score = sys.maxsize
        min_sum = 0
        nums.sort()

        for i in range(len(nums)-2):
                l = i+1
                r = len(nums) -1
                while l < r:
                    if abs(nums[i] + nums[l] + nums[r] - target) < min_score:
                        min_score = abs(nums[i] + nums[l] + nums[r] - target)
                        min_sum = nums[i] + nums[l] + nums[r]
                    if  nums[i] + nums[l] + nums[r] < target:
                        l = l + 1
                    else:
                        r = r - 1
        return min_sum