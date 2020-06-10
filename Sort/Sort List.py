# https://leetcode.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        arr = []

        def sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                l = arr[:mid]
                r = arr[mid:]

                sort(l)
                sort(r)

                i = j = k = 0
                while i < len(l) and j < len(r):
                    if l[i] < r[j]:
                        arr[k] = l[i]
                        i += 1
                    else:
                        arr[k] = r[j]
                        j += 1
                    k += 1
                while i < len(l):
                    arr[k] = l[i]
                    i += 1
                    k += 1
                while j < len(r):
                    arr[k] = r[j]
                    j += 1
                    k += 1

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        sort(arr)
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head

        '''
        Bad hack - but not really

        unsorted_list = []
        curr = head
        while curr:
            unsorted_list.append(curr.val)
            curr = curr.next
        sorted_list = sorted(unsorted_list)
        curr = head
        i = 0
        while curr:
            curr.val = sorted_list[i]
            curr = curr.next
            i += 1
        return head


        '''