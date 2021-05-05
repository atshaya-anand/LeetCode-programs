# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1 = ''
        str2 = ''
        
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        
        str1 = str1[::-1]
        str2 = str2[::-1]
        val = int(str1) + int(str2)
        val = str(val)
        val = val[::-1]
        
        n = len(val)
        node = ListNode(int(val[0]))
        head = node
        ll = head
        for i in range(1,n):
            node = ListNode(int(val[i]))
            head.next = node
            head = node
        return ll