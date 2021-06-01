# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root,ls,string):
            if root == None:
                return
            val = root.val
            string += str(val)
            if root.left == None and root.right == None:
                ls.append(string)
                return
            dfs(root.left,ls,string)
            dfs(root.right,ls,string)
        
        if root is not None:
            ls = []
            str_ = ''
            dfs(root, ls, str_)
            ls = [int(i) for i in ls]
            return sum(ls)