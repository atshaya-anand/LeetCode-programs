# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(root, p, q):
            if root is None:
                return None
            if p.val <= root.val and q.val >= root.val or p.val >= root.val and q.val <= root.val:
                return root
            elif p.val < root.val and q.val < root.val:
                return recur(root.left, p , q)
            elif p.val > root.val and q.val > root.val:
                return recur(root.right, p, q)
            
        return recur(root, p, q)