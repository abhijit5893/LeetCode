# https://leetcode.com/problems/valid-anagram/submissions/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t1 = {}
        t2 = {}
        for i in s:
            if t1.get(i, None) is None:
                t1[i] = 1
            else:
                t1[i] += 1

        for i in t:
            if t2.get(i, None) is None:
                t2[i] = 1
            else:
                t2[i] += 1

        if len(t1.keys()) != len(t2.keys()):
            return False

        for i in t1.keys():
            if i not in t2.keys() or t1[i] != t2[i]:
                return False
        return True