#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {num: i for i,num in enumerate(nums)}
        for i, num in enumerate(nums):
            if hasht.get(target-num, None) and hasht[target-num] != i:
                return [i, hasht[target-num]]

        hasht = {}
        for i in range(len(nums)):
            if nums[i] in hasht.keys():
                return [i, hasht[nums[i]]]
            else:
                hasht[target-nums[i]] = i

#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.res = []
        self.inorder(root)
        hasht = {num: i for i,num in enumerate(self.res)}
        for i, num in enumerate(self.res):
            if hasht.get(k-num, None) and hasht[k-num] != i:
                return [i, hasht[k-num]]

#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hasht = {num: i for i,num in enumerate(numbers)}
        for i, num in enumerate(numbers):
            if hasht.get(target-num, None) and hasht[target-num] != i:
                return [i+1, 1+hasht[target-num]]
