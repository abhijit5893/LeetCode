#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
        '''
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        out = []
        out.append([1])
        out.append([1,1])
        for i in range(2,numRows):
            temp = []
            temp.append(1)
            for j in range(1, len(out[i-1])):
                temp.append(out[i-1][j-1]+out[i-1][j])
            temp.append(1)
            out.append(temp)
        return out
        '''