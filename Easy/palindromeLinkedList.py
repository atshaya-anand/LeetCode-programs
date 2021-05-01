# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ll = head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        while ll:
            if ll.val != stack.pop():
                return False
            ll = ll.next
        return True