#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {'(':')',
             '{':'}',
             '[':']'}
        stack = []
        for i in s:
            if i in m.keys():
                stack.append(i)
            elif stack and i == m[stack[-1]]:
                stack.pop()
            else:
                return False

        return not stack
