#https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target,res,[])
        return res
    def dfs(self,nums,target,res,path):
        if target < 0: return
        if target == 0 and sorted(path) not in res:
            res.append(sorted(path))
            return
        for i in range(len(nums)):
            self.dfs(nums, target - nums[i], res, path + [nums[i]])