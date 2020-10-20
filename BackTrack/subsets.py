#https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            res.append(path)
            if not len(nums):
                return
            for i in range(len(nums)):
                backtrack(nums[i+1:],path+[nums[i]])

        res = []
        backtrack(nums,[])
        return res