#https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if token == '+':
                    stack.append(temp1 + temp2)
                elif token == '*':
                    stack.append(temp1 * temp2)
                elif token == '-':
                    stack.append(temp2 - temp1)
                elif token == '/':
                    stack.append(int(temp2 / temp1))

        return stack.pop()
