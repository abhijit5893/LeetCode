#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def foo(inorder, preorder):
            if len(inorder) and len(preorder):
                root_val = preorder.pop()
                root = TreeNode(root_val, None, None)

                root_index = -1
                for i, v in enumerate(inorder):
                    if v == root_val:
                        root_index = i
                        break
                root.left = foo(inorder[:root_index], preorder)
                root.right = foo(inorder[root_index + 1:], preorder)

                return root

        return foo(inorder, preorder[::-1])