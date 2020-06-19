# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            arr[i] = max(nums[i], arr[i - 1], nums[i] + arr[i - 2])

        print(arr)
        return arr[len(nums) - 1]