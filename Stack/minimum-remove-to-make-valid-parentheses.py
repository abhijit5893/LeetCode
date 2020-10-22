#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk1 = []
        pos1 = []
        res = []
        for i in range(len(s)):
            if  s[i] == '(':
                stk1.append('(')
                pos1.append(i)
                res.append('')
            elif  s[i] == ')':
                stk1.append(')')
                pos1.append(i)
                res.append('')
            else:
                res.append(s[i])

        stk2 = []
        pos2 = []
        for i in range(len(stk1)):
            if stk1[i] == '(':
                stk2.append('(')
                pos2.append(pos1[i])
            elif stk1[i] == ')':
                if len(stk2) and stk2[len(stk2)-1] == '(':
                    stk2.pop()
                    idx = pos2.pop()
                    res[idx] = '('
                    res[pos1[i]] = ')'
        print(res)
        out = ''
        for i in res:
            if i != '':
                out += str(i)
        return out

        '''
        sList = list(s)
        stack = []
        for i,ch in enumerate(sList):
            if ch == "(":
                stack.append((ch,i))
            elif ch == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((ch,i))

        # for each index in stack, set sList[index] to empty string
        for _,item in enumerate(stack):
            sList[item[1]] = ""

        return "".join(sList)
        '''