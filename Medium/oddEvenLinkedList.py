# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = []
        count = 1
        ll = head
        prev = None
        
        while head:
            if count % 2 == 0:
                even.append(head.val)
                if head.next is not None:
                    head.val = head.next.val
                    head.next = head.next.next
                    count += 1
                    continue
                else:
                    count += 1
                    prev.next = None
                    break
            count += 1
            prev = head
            head = head.next
        
        for i in range(len(even)):
            a = ListNode(even[i])
            prev.next = a
            prev = a
        return ll