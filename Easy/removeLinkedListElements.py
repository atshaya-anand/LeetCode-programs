# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ll = head
        prev = None
        while head:
            flag = 0
            if head.val == val:
                flag = 1
                if head.next is not None:
                    #prev = head
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    if prev == None:
                        ll = None
                        head = None
                    else:
                        prev.next = None
                        head = None
                    break
            if flag == 0:
                prev = head
                head = head.next
                
        return ll