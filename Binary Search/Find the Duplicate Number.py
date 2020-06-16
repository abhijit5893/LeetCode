#https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        The idea is that if you have a number (e.g. 5) and there are 5 numbers in the array         that are less than or equal to 5 then the duplicate has to be a number greater than         5. Otherwise, by the pigeonhole principle the duplicate has to be one of the numbers         between 1 and 5 inclusive.
        '''
        l, h, m = 0, len(nums) - 1, len(nums) // 2
        while h - l > 1:
            print(m,[1 for i in nums if i <= m])
            if sum(1 for i in nums if i <= m) > m:
                h = m
            else:
                l = m
            m = (h + l + 1) // 2
        return m

        '''
        Sorting solution - Did not modify the original array
        import copy
        if not len(nums): return 0
        nums_new = copy.deepcopy(nums)
        nums_new.sort()

        for i in range(1,len(nums_new),1):
            if nums_new[i-1] == nums_new[i]:
                return nums_new[i]
        return 0
        '''

