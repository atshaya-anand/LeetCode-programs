# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(root,ls,string):
            if root == None:
                return
            val = root.val
            string += str(val)
            if root.left is not None or root.right is not None:
                string += "->"
            if root.left == None and root.right == None:
                ls.append(string)
                return
            dfs(root.left,ls,string)
            dfs(root.right,ls,string)
        
        if root is not None:
            ls = []
            str_ = ''
            dfs(root, ls, str_)
            return ls