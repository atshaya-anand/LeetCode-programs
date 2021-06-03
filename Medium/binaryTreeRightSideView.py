# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue, queueUtils, res = [], [], []
        if root is not None:
            queue.append(root)
            res.append(queue[-1].val)
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                
                if len(queue) == 0:
                    if queueUtils:
                        res.append(queueUtils[-1].val)
                        queue = queueUtils[:]
                        queueUtils = []
                        
        return res