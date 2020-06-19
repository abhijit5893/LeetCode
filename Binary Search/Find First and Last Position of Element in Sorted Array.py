#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        start, end = -1, -1
        while l <= r:
            if l== r and nums[l] != target:
                break
            mid = (r+l)//2
            if nums[mid] == target:
                start = mid
                for i in range(mid-1,-1,-1):
                    if nums[i] == target:
                        start = i
                end = mid
                for i in range(mid+1,len(nums),1):
                    if nums[i] == target:
                        end = i
                return [start, end]

            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return [start, end]


