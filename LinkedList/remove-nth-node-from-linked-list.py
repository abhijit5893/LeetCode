#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next

        count = 0
        if len(arr) == n:
            return head.next
        curr = head
        prev = None
        while curr != None:
            if count == len(arr) - n:
                temp = curr.next
                prev.next = temp
                curr.next = None
            prev = curr
            curr = curr.next
            count += 1
        return head

    '''
    def remove(head, n):
            if head == None: return head, 0

            node, count = remove(head.next, n)
            count += 1
            head.next = node

            if count == n: head = head.next

            return head, count

        return remove(head, n)[0]

    class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
    '''