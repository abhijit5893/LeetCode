#https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return root
        result = []

        def foo(root):
            if root != None:
                foo(root.left)
                result.append(root.val)
                foo(root.right)
            return root

        foo(root)
        return result


# Definition for a binary tree node with stack.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return root
        result = []
        stack = []
        top = root
        while top or len(stack):
            while top:
                stack.append(top)
                top = top.left
            top = stack.pop()
            result.append(top.val)
            top = top.right
        return result

