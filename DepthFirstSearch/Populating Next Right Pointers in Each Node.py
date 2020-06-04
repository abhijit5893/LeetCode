#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root: return None

        stack = []
        root.next = None
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left != None:
                node.left.next = node.right
                stack.append(node.left)
            if node.right != None:
                if node.next != None:
                    node.right.next = node.next.left
                else:
                    node.right.next = node.next
                stack.append(node.right)

        return root


