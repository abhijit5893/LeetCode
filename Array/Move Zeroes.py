# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        '''
        #Two-pass O(n) solution

        out_num = []
        out_zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                out_zero.append(0)
            else:
                out_num.append(nums[i])

        for i in range(len(out_num)):
            nums[i] = out_num[i]

        for i in range(len(out_num), len(out_num)+len(out_zero)):
            nums[i] = out_zero[i- len(out_num)]
        '''