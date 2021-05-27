# https://leetcode.com/problems/add-two-numbers-ii/

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
            
        #print(str1,'---',str2)
        val = int(str1) + int(str2)
        #print(val)
        valstr = str(val)
        if valstr != '':
            node = ListNode(valstr[0])
            head = node
            list_ = head
            
            i = 1
            n = len(valstr)
            while i < n:
                node = ListNode(valstr[i])
                head.next = node
                head = node
                i += 1
            
            return list_
        return None