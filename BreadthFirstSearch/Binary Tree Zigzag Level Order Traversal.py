#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def BFS(self, q, root):
        out = []
        level = 0
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                # pint(n, level, level % 2, out, temp)
                s = q.pop(0)
                temp.append(s.val)
                if s.left != None:
                    q.append(s.left)
                if s.right != None:
                    q.append(s.right)

            print(len(out), temp)
            if len(out) == 0:
                out.append(temp)
            elif len(out) % 2 == 0:
                out.append(temp)
            else:
                out.append(temp[::-1])
        return out

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return root
        q = []
        q.append(root)
        print(root)
        return self.BFS(q, root)