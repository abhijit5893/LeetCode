#https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        for i in range(n):
            out.append(nums[i])
            out.append(nums[n+i])
        return out