# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def preorder(root, li):
            if root == None:
                return
            if root.left is not None:
                temp = root.left
                if temp.left == None and temp.right == None:
                    li.append(temp.val)
                preorder(temp, li)
            preorder(root.right, li)
        
        li = []
        if root is not None:
            preorder(root, li)
        
        if li:
            return sum(li)
        else:
            return 0