# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        temphead = head
        prev = None
        curr = head
        previousNode = None
        count = 1
        while curr:
            if count == left:
                break
            prev = curr
            curr = curr.next
            count += 1
        
        count = 1
        while temphead:
            if count == right:
                break
            temphead = temphead.next
            count += 1
        remList = temphead.next
        
        current = curr
        while curr:
            if curr.val == remList.val:
                previousNode.next = None
            previousNode = curr
            curr = curr.next
        
        prev_ = None
        next_ = None
        while current:
            next_ = current.next
            current.next = prev_
            prev_ = current
            current = next_
        
        #print(prev_)
        #print(remList)
        
        count = 1
        previous = None
        while prev:
            if count == left:
                previous.next = prev_
                break
            previous = prev
            prev = prev.next
            count += 1
        
        #print(previous)
        
        head = previous
        node = None
        while previous:
            node = previous
            previous = previous.next
        node.next = remList
        
        return head
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        prev = arr[:left-1]
        rem = arr[right:]
        
        #print(prev,rem)
        
        arr = arr[left-1:right]
        arr = arr[::-1]
        
        #print(arr)
        
        if prev:
            node = ListNode(prev[0])
            head = node
            list_ = head
            
            for i in range(1,len(prev)):
                node = ListNode(prev[i])
                head.next = node
                head = node
        else:
            head = None
        
        if arr:
            node = ListNode(arr[0])
            if head is not None:
                head.next = node
                head = node
            else:
                head = node
                list_ = head
            
            for i in range(1,len(arr)):
                node = ListNode(arr[i])
                head.next = node
                head = node
        
        if rem:
            node = ListNode(rem[0])
            if head is not None:
                head.next = node
                head = node
            else:
                head = node
                list_ = head
            
            for i in range(1,len(rem)):
                node = ListNode(rem[i])
                head.next = node
                head = node
                
        return list_