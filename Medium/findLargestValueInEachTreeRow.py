# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        queue = []
        queueUtils = []
        
        if root is not None:
            queue.append(root)
            ans.append(root.val)
            
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                
                if len(queue) == 0:
                    if queueUtils:
                        ans.append(max([i.val for i in queueUtils]))
                        queue = queueUtils[:]
                        queueUtils = []
                    
        return ans