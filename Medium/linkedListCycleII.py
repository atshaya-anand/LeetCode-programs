# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        visited = []
        slow = head
        while slow and slow.next:
            if slow not in visited:
                visited.append(slow)
            else:
                return slow
            slow = slow.next
                