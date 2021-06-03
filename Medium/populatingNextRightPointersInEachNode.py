# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue, queueUtils = [], []
        if root is not None:
            queue.append(root)
            for i in range(0,len(queue)):
                if i == len(queue) - 1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i+1]
            
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                    
                if len(queue) == 0:
                    if queueUtils:
                        for i in range(0,len(queueUtils)):
                            if i == len(queueUtils) - 1:
                                queueUtils[i].next = None
                            else:
                                queueUtils[i].next = queueUtils[i+1]
                        queue = queueUtils[:]
                        queueUtils = []
                
        return root