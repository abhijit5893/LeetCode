#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def findPermutations(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                findPermutations(nums[:i]+nums[i+1:], path+[nums[i]])

        res = []
        findPermutations(nums,[])
        return res

