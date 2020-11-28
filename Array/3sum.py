#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets =[]
        nums.sort()

        for i in range(len(nums)-2):
            curr, seen, used =  nums[i], {}, set()
            if curr > 0: break
            if i > 0 and curr == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if nums[j] in seen and nums[j] not in used:
                    triplets.append([curr, seen[nums[j]], nums[j]])
                    used.add(nums[j])
                else:
                    seen[-(nums[j]+curr)] = nums[j]
        return triplets