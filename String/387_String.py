#387. First Unique Character in a String

'''
String solution
Space - O(26)
Time - O(n)
'''
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets  = [0] * 26
        for c in s:
            alphabets[ord(c)-97] += 1
        
        for i, c in enumerate(s):
            if alphabets[ord(c)-97] == 1:
                return i
        return -1
