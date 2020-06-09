# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: return None

        tempA = headA
        tempB = headB

        while tempA is not tempB:
            tempA = headB if tempA is None else tempA.next
            tempB = headA if tempB is None else tempB.next

        return tempA
