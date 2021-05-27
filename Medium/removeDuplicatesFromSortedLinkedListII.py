# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        visited = []
        revisit = []
        ll = head
        prev = None
        while head:
            flag = 0
            if head.val not in visited:
                visited.append(head.val)
            else:
                if head.val not in revisit:
                    revisit.append(head.val)
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
        
        #print(revisit,'ll',ll)
        temp = ll
        prev = None
        while ll:
            #print('inside loop',ll)
            flag = 0
            if ll.val in revisit:
                flag = 1
                if ll.next is not None:
                    ll.val = ll.next.val
                    ll.next = ll.next.next
                else:
                    if prev is None:
                        return None
                    prev.next = None
                    flag = 0
            if flag == 0:
                prev = ll
                ll = ll.next
        
        return temp