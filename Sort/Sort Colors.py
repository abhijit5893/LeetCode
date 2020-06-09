# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 0:

            '''
            Bubble Sort
            '''
            for j in range(len(nums)):
                for i in range(0, len(nums) - j - 1):
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]

            '''
            O(n^2) solution

            for j in range(len(nums)):
                for i in range(1,len(nums)):
                    if nums[i-1] > nums[i]:
                        temp = nums[i-1]
                        nums[i-1] = nums[i]
                        nums[i] = temp
            '''
            '''
            Two-pass solution O(n)

            table = {}
            for i in range(len(nums)):
                if table.get(nums[i], None) is not None:
                    table[nums[i]] += 1
                else:
                    table[nums[i]] = 1

            for i in range(len(nums)):
                if table.get(0,0) > 0:
                    nums[i] = 0
                    table[0] -= 1
                elif table.get(1,0) > 0:
                    nums[i] = 1
                    table[1] -= 1
                elif table.get(2,0) > 0:
                    nums[i] = 2
                    table[2] -= 1
            '''