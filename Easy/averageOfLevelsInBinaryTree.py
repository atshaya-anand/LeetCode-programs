# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue, queueUtils = [], []
        res = []
        
        if root is not None:
            queue.append(root)
            res.append(sum([i.val for i in queue])/len(queue))
            
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                
                if len(queue) == 0:
                    if queueUtils:
                        res.append(sum([i.val for i in queueUtils])/len(queueUtils))
                        queue = queueUtils[:]
                        queueUtils = []
                        
        return res