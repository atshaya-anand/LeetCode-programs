# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_ = []
        for el in lists:
            i = el
            while i:
                list_.append(i.val)
                i = i.next
        list_.sort()
        if list_:
            node = ListNode(list_[0])
            head = node
            linkedlist = head
            for i in range(1,len(list_)):
                node = ListNode(list_[i])
                head.next = node
                head = node
            return linkedlist
        else:
            return None