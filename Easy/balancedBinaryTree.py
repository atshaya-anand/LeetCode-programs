# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if root == None:
                return True
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1:
                return False
            if dfs(root.left) == False:
                return False
            if dfs(root.right) == False:
                return False
            return True
        
        def height(root):
            if root == None:
                return 0
            l = height(root.left) + 1
            r = height(root.right) + 1
            return max(l, r)
        
        return dfs(root)