# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_ = []
        while l1:
            list_.append(l1.val)
            l1 = l1.next
        while l2:
            list_.append(l2.val)
            l2 = l2.next
        list_.sort()
        if list_:
            node = ListNode(list_[0])
            head = node
            linkedlist = head
            for el in range(1,len(list_)):
                node = ListNode(list_[el])
                head.next = node
                head = node
            return linkedlist
        else:
            return None