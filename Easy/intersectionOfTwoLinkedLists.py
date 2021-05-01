# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        slow = headA
        fast = headB
        visited = []
        
        while slow or fast:
            if slow:
                if slow not in visited:
                    visited.append(slow)
                    slow = slow.next
                else:
                    return slow
            if fast:
                if fast not in visited:
                    visited.append(fast)
                    fast = fast.next
                else:
                    return fast
            #print("val",slow.val,fast.val)
        return None
        '''
        
        count1 = 0
        count2 = 0
        ll1,ll2 = headA,headB
        
        while headA:
            count1 += 1
            headA = headA.next
        while headB:
            count2 += 1
            headB = headB.next
            
        diff = abs(count1-count2)
        if count1 > count2:
            j = 0
            while j < diff:
                ll1 = ll1.next
                j += 1
        else:
            j = 0
            while j < diff:
                ll2 = ll2.next
                j += 1
        
        slow = ll1
        fast = ll2
        
        while slow and fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next     
        
        return None   