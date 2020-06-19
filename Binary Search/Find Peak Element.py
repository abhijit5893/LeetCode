#https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) -1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        return lo