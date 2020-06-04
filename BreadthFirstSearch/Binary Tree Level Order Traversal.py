#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def BFS(self, q, root):
        out = []
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                s = q.pop(0)
                temp.append(s.val)
                if s.left != None:
                    q.append(s.left)
                if s.right != None:
                    q.append(s.right)
            out.append(temp)
        return out

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return root
        q = []
        q.append(root)
        print(root)
        return self.BFS(q, root)

