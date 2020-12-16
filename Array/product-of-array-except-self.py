#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out =[1] * n
        for i in range(1,n):
            out[i] = out[i-1] * nums[i-1]

        prod =1
        for i in range(n-1,-1,-1):
            out[i] *= prod
            prod *= nums[i]
        return out