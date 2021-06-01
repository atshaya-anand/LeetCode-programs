# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
        
            leftRes =  max(dfs(root.left), 0)
            rightRes =  max(dfs(root.right), 0)
            self.res = max(self.res, root.val + leftRes + rightRes)
        
            return root.val+max(leftRes, rightRes)
        
        if not root:
            return 0
        
        self.res = float('-inf')
        dfs(root)
        
        return self.res