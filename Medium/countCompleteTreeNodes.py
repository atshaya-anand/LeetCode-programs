# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(root, ls):
            if root is None:
                return
            
            ls.append(root.val)
            dfs(root.left, ls)
            dfs(root.right, ls)
        
        ls = []
        dfs(root, ls)
        return len(ls)