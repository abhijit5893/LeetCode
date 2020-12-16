#https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        self.dfs(nums,res,[])
        return res
    def dfs(self, nums,res,path):
        if path not in res:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], res, path + [nums[i]])