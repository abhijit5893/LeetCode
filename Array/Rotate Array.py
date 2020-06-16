#https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Two Pass array solution
        '''
        if k > 0:
            out = []
            out += nums[len(nums) - k:]
            out += nums[:len(nums) - k]
            for i in range(len(out)):
                nums[i] = out[i]    