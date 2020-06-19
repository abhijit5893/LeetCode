#https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]): return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                print(row)
                l, r = 0, len(row) -1
                while l <= r:
                    if l == r and row[l] != target:
                        break
                    mid = l+ ((r-l)) //2
                    if row[mid] == target:
                        return True
                    if row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid
        return False

        '''
        #O(mn) solution with O(mn) space

        out = []
        for row in matrix:
            out += row
        return target in out
        '''