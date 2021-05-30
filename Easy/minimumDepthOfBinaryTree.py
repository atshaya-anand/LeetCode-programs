# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0 and right != 0:
                return right + 1
            if left != 0 and right == 0:
                return left + 1
            
            return min(left+1,right+1)
        
        if root is not None:
            return dfs(root)
        else:
            return 0