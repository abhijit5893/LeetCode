# https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n, h = len(needle), len(haystack)
        hash_n = hash(needle)
        print(h - n + 1)
        for i in range(h - n + 1):
            if hash(haystack[i:i + n]) == hash_n:
                return i
        return -1

        '''
        Cheating - Fast Solution

        if needle in haystack:
            return haystack.index(needle)
        return -1
        '''