# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L, R = arr[:mid], arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if R[j] > L[i]:
                    arr[k] = R[j]
                    j += 1
                else:
                    arr[k] = L[i]
                    i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.mergeSort(nums)
        return nums[k - 1]
        '''
        Cheating

        return sorted(nums, reverse=True)[k-1]
        '''