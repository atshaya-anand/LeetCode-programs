# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        next_ = None
        ll = list1
        count = 0
        
        while list1:
            if count == a:
                prev.next = list2
            if count == b:
                if list1.next is not None:
                    next_ = list1.next
                    while list2:
                        if list2.next is None:
                            list2.next = next_
                            break
                        list2 = list2.next
            count += 1
            prev = list1
            list1 = list1.next
        
        return ll