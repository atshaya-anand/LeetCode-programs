# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        if arr:
            node = ListNode(arr[0])
            head = node
            ll = head
            for i in range(1,len(arr)):
                node = ListNode(arr[i])
                head.next = node
                head = node
            return ll