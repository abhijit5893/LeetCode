#https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [[]]
        for i in s:
            if i == '(':
                stk.append([])
            elif i == ')':
                rs = stk.pop()
                stk[-1].extend(rs[::-1])
            else:
                stk[-1].append(i)

        return ''.join([y for x in stk for y in x])