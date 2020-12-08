#https://leetcode.com/problems/container-with-most-water/
import sys
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = 0
        i = 0
        j = len(height) -1
        while  j > i:
            max_capacity = max(max_capacity ,min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_capacity


        # maxi = 0
        #     i = 0
        #     j = len(height)-1
        #     while i<j:
        #         mini = min(height[i],height[j])
        #         maxi = max(maxi,mini*(j-i))
        #         if height[i]<height[j]:
        #             i = i+1
        #         else:
        #             j = j-1
        #     return maxi

