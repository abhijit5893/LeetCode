# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        # Recursive

        if not head: return prev
        temp = head.next
        head.next = prev
        return self.reverseList(temp, head)

        '''

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        '''

        '''
        Using Stack - O(n)

        temp1 = temp2 = head
        stack = []
        while head!= None:
            stack.append(head.val)
            head = head.next

        while stack:
            item = stack.pop()
            temp1.val = item
            temp1 = temp1.next

        return temp2

        '''