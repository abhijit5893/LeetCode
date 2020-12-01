#https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        out = []
        ref = Counter(p)

        for i in range(len(s)-n+1):
            if Counter(s[i:i+n]) == ref:
                out.append(i)
        return out
        '''
        n = len(p)
        out = []
        ref = [0] * 26
        for i in list(p):
            ref[ord(i)-ord('a')] += 1

        for i in range(len(s)-n+1):
            ctrl = [0] * 26
            for j in list(s)[i:i+n]:
                ctrl[ord(j)-ord('a')] += 1
            if ctrl == ref:
                out.append(i)
        return out
        '''
        '''
        n = len(p)
        p = ''.join(sorted(list(p)))

        out =[]
        for i in range(len(s)-n+1):
            temp = sorted(list(s)[i:i+n])
            if ''.join(temp) == p:
                out.append(i)

        return out
        '''