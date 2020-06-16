#https://leetcode.com/problems/4sum-ii/
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count, table = 0, {}
        for n1 in A:
            for n2 in B:
                tmp = n1 + n2
                if table.get(tmp, None):
                    table[tmp] += 1
                else:
                    table[tmp] = 1
        for n3 in C:
            for n4 in D:
                tmp = 0 - (n3 + n4)
                if table.get(tmp,None):
                    count += table[tmp]
        return count