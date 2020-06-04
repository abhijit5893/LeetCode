#https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def DFSUtil(self, node):
        l = r = 1
        if node == None:
            return 0
        if node.left != None:
            l = 1 + self.DFSUtil(node.left)
        if node.right != None:
            r = 1 + self.DFSUtil(node.right)
        return max(l, r)

    def maxDepth(self, root: TreeNode) -> int:
        return self.DFSUtil(root)