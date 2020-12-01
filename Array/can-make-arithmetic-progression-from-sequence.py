#https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2: return True
        arr.sort()
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True
