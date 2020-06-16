# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)):
            if i < len(s) - i:
                temp = s[i]
                s[i] = s[len(s) - i - 1]
                s[len(s) - i - 1] = temp

        '''
        Very Bad Solution - Interviewer will not be happy
        s[:] = s[::-1]
        '''
