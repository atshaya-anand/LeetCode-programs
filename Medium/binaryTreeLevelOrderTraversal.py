# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queueUtil = []
        res = []
        if root is not None:
            queue.append(root)
            res.append([i.val for i in queue])
            while queue:
                temp = queue[0]
                if temp.left is not None:
                    queueUtil.append(temp.left)
                if temp.right is not None:
                    queueUtil.append(temp.right)
                queue.pop(0)
                if len(queue) == 0:
                    if queueUtil:
                        res.append([i.val for i in queueUtil])
                        queue = queueUtil[:]
                        queueUtil = []
        return res