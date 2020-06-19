# https://leetcode.com/problems/wiggle-sort-ii/
import copy
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        '''
        I actually did it

        out = copy.deepcopy(nums)
        out.sort()
        start = 0
        mid = (len(out) // 2) + len(out) % 2
        out[:mid], out[mid:] = out[:mid][::-1], out[mid:][::-1]
        for i in range(len(nums)):
            if i % 2  ==0:
                nums[i] = out[start]
                start += 1
            else:
                nums[i] = out[mid]
                mid += 1
        '''