#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        targets = [total//k] * k
        taken = [False] * len(nums)

        def backtrack(i,k_th):
            if targets[k_th] < 0: return False
            if targets[k_th] == 0:
                if k_th == k-1: return True
                return backtrack(0,k_th+1 )
            for j in range(i,len(nums)):
                if taken[j] == True: continue
                taken[j] = True
                targets[k_th] -= nums[j]
                if backtrack(j+1,k_th): return True
                taken[j] = False
                targets[k_th] += nums[j]
            return False

        return backtrack(0,0)