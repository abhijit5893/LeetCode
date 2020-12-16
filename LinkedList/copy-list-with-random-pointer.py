#https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = dict()
        def deep_copy(node):
            if not node: return None
            if node in d: return d[node]
            n = Node(node.val)
            d[node] = n
            n.next = deep_copy(node.next)
            n.random = deep_copy(node.random)
            return n
        return deep_copy(head)
