# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):

            if root == None:
                return

            root.left = dfs(root.left)
            temp = root
            
            if root.left is not None:
                right = root.right
                root.right = root.left
                root.left = None
                
                while (root.right):
                    root = root.right
                    
                root.right = right
            
            root.right = dfs(root.right)
            return temp
        
        if root is not None:
            root = dfs(root)