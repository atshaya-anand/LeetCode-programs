# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        visited = []
        ll = head
        prev = None
        while head:
            flag = 0
            if head.val not in visited:
                visited.append(head.val)
            else:
                flag = 1
                if head.next is not None:
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    prev.next = None
                    flag = 0
            if flag == 0:
                prev = head
                head = head.next
        return ll