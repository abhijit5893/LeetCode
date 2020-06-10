# https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
        '''
        Accepted but not fast
        if not head: return head
        fast = head
        slow = head.next
        dummy1 = curr1 = ListNode(0)
        dummy2 =  curr2 = ListNode(0)

        while fast and fast.next and slow and slow.next:
            curr1.next = fast
            fast= fast.next.next
            curr1 = curr1.next

            curr2.next = slow
            slow= slow.next.next
            curr2 = curr2.next

        if fast:
            curr1.next = fast
            fast= fast.next
            curr1 = curr1.next

        if slow:
            curr2.next = slow
            slow= slow.next
            curr2 = curr2.next
        else:
            curr2.next = None

        curr1.next = dummy2.next

        print(dummy1.next, head)
        return dummy1.next
        '''
