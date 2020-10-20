#https://leetcode.com/problems/maximum-binary-tree-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        #if root is None
        if root == None:
            return TreeNode(val)
        #if root value is lesser
        if root.val < val:
            newNode = TreeNode(val)
            newNode.left = root
            root = newNode
            return root
        root.right = self.insertIntoMaxTree(root.right,val)
        return root


