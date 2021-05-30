# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def preorder(root):
            if root == None:
                return 0
            #left = preorder(root.left) + 1
            #right = preorder(root.right) + 1
            return max(preorder(root.left)+1, preorder(root.right)+1) 
        
        if root is not None:
            return preorder(root)
        else:
            return 0