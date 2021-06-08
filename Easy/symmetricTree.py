# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def dfs(a, b):
            if a is None and b is None:
                return True
            elif a is not None and b is None or a is None and b is not None:
                return False
            
            if a.val != b.val:
                return False
            
            if dfs(a.left, b.right) == True and dfs(a.right, b.left) == True:
                return True
            else:
                return False
        
        return dfs(root.left, root.right)