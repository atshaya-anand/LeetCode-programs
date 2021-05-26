# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is not None:
            count = 0
            ll = head
            while ll:
                count += 1
                ll = ll.next
            if count == 1:
                return head
            i = 1
            #return head
            k = k % count
            #print(k)
            while i <= k:
                temp = head
                prev = None
                head2 = temp
                while head2 and head2.next:
                    prev = head2
                    head2 = head2.next
                last = prev.next
                prev.next = None
                last.next = head
                head = last
                i += 1
            return head
        else:
            return None