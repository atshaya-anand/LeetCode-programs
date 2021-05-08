# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        count1, count2 = 1, 1
        ll = head
        temp = head
        kB = None
        kE = None
        
        a = head
        length = 0
        while a:
            length += 1
            a = a.next
        
        while head:
            if count1 == k:
                kB = head.val
                break
            count1 += 1
            head = head.next
        
        slow = fast = temp
        while fast and fast.next:
            if count2 >= k:
                slow = slow.next
            fast = fast.next
            count2 += 1
        kE = slow.val
        
        begVal = k - 1
        endVal = length - k
        count = 0
        res = ll
        
        while ll:
            if ll.val == kB and count == begVal:
                ll.val = kE
            elif ll.val == kE and count == endVal:
                ll.val = kB
            ll = ll.next
            count += 1
            
        return res