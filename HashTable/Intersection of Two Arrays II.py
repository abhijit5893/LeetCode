# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1 = dict()
        out = []

        for i in nums1:
            if N1.get(i, None) is not None:
                N1[i] += 1
            else:
                N1[i] = 1

        for i in nums2:
            if N1.get(i, None) is not None:
                if N1[i] != 0:
                    N1[i] -= 1
                    out.append(i)
        return out
