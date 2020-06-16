#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)
        '''
        O(n) but uses extra space
        out = []
        for i in nums:
            if i in out:
                continue
            else:
                out.append(i)
        for i in range(len(out)):
            nums[i] = out[i]
        return len(out)
        '''