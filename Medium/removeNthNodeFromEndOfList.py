# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        prev = None
        count = 1
        while fast and fast.next:
            if count >= n:
                prev = slow
                slow = slow.next
            fast = fast.next
            count += 1
        
        if slow.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            if prev == None:
                head = None
            else:
                prev.next = None
        return head