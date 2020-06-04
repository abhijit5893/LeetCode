# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True

        out = []

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            out.append(node.val)
            inorder(node.right)

        inorder(root)
        print(out)
        for i in range(1, len(out)):
            if out[i - 1] >= out[i]:
                return False

        return True