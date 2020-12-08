#https://leetcode.com/problems/4sum/
class Solution:
    def twoSum(self,nums,target):
        match = set()
        res = []
        for num in nums:
            if target - num in match:
                res.append((target-num,num))
            match.add(num)
        return res

    def helper(self,nums, target,k):
        if k == 2:
            return self.twoSum(nums, target)
        res = set()
        for i in range(len(nums) - k + 1):
            candidates = self.helper(nums[i+1:], target - nums[i], k - 1)
            for c in candidates:
                res.add((nums[i],) + c)
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return nums
        nums.sort()
        return self.helper(nums,target,4)


