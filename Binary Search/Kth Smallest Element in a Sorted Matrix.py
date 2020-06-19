#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        while l< r:
            mid = l + (r-l)//2
            count = 0
            for i in range(len(matrix)):
                for j in matrix[i]:
                    if j <= mid:
                        count+= 1
            if count < k:
                l = mid +1
            else:
                r = mid
        return l
        '''
        O(n2) with O(n2) extra space
        if not matrix: return 0
        out = []
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                out.append(matrix[i][j])
        out.sort()
        return out[k-1]
        '''
