# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if not len(nums): return 0

        x1, x2 = 0, nums[0]
        for i in range(1, len(nums) + 1):
            x1 ^= i
        for i in range(1, len(nums)):
            x2 ^= nums[i]
        return x1 ^ x2
        '''
        Dumb Accepted Solution
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        return 0
        '''