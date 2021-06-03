# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue, queueUtils, res = [], [], []
        if root is not None:
            queue.append(root)
            res.append([i.val for i in queue])
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                if len(queue) == 0:
                    if queueUtils:
                        res.append([i.val for i in queueUtils])
                        queue = queueUtils[:]
                        queueUtils = []
        
        return res[::-1]