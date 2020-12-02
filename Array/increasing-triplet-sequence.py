#https://leetcode.com/problems/increasing-triplet-subsequence/
import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        lis = [1] * n
        for i in range(n):
            for j in range(0,i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        #print(lis)
        for i in range(n):
            if lis[i] >= 3:
                return True
        return False