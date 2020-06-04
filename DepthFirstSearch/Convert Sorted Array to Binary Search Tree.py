#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Height-balanced  BST - Depth of two subtrees of every node nver differ by more than 1
# All keys in n's left subtree are less than the key in n, and
# All keys in n's right subtree are greater than the key in n.
class Solution:

    # Divide and Conquer with DFS
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid], None, None)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root