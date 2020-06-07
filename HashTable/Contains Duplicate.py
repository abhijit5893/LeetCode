#https://leetcode.com/problems/contains-duplicate/submissions/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            if a.get(i,None) is not None:
                return True
            else:
                a[i] = 1
        return False