#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        order = []


        def inorder(root):
            if not root:
                return
            inorder(root.left)
            order.append(root.val)
            inorder(root.right)
        inorder(root)

        return order[k-1]
