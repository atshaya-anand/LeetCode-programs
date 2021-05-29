# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def inorder(root, li):
            if root == None:
                return
            inorder(root.left, li)
            li.append(root.val)
            inorder(root.right, li)
        
        li = []
        if root is not None:
            inorder(root, li)
        
        sum_ = 0
        for i in li:
            if i >= low and i <= high:
                sum_ += i
        return sum_