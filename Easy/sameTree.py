# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None and root2 is not None or root1 is not None and root2 is None:
                return False
            
            if root1.val != root2.val:
                return False
            if dfs(root1.left, root2.left) == True and dfs(root1.right, root2.right) == True:
                return True
            else:
                return False
        
        return dfs(p, q)