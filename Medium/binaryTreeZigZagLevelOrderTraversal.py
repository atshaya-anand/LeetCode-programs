# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, queueUtils, res = [], [], []
        count = 1
        if root is not None:
            queue.append(root)
            count += 1
            res.append([i.val for i in queue])
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                    
                if len(queue) == 0:
                    if queueUtils:
                        if count % 2 == 0:
                            res.append(i.val for i in queueUtils[::-1])
                        else:
                            res.append(i.val for i in queueUtils)
                        count += 1
                        queue = queueUtils[:]
                        queueUtils = []
        
        return res