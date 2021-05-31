# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(root, ls):
            if root == None:
                return 
            dfs(root.left, ls)
            ls.append(root.val)
            dfs(root.right, ls)
            
        ls = []
        dfs(root, ls)
        i = 1
        n = len(ls)
        while i < n + 1:
            if i == k:
                return ls[i-1]
            i += 1