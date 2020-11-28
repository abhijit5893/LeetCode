#https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        if head.next == None and head.val == val:
            return None
        elif head.next == None and head.val != val:
            return head
        else:
            new_head = head
            prev = None
            while head != None:
                if head.val ==  val:
                    temp = head.next
                    head.next = None
                    if head == new_head:
                        new_head = temp
                        head = temp
                    else:
                        prev.next = temp
                        head = temp
                else:
                    if prev == None:
                        prev = head
                    else:
                        prev = prev.next
                    head = head.next
        return new_head


'''
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        if head.val == val:
            return self.removeElements(head.next,val)
        else:
            curr = head
            prev = ListNode()
            while curr != None:
                if curr.val ==  val:
                    prev.next = curr.next
                    curr = prev.next
                else:
                    prev = curr
                    curr = curr.next
            return head

'''
