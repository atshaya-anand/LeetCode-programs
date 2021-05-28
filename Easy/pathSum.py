# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def pathsum(root, sum_, target, hassum):
            if root == None:
                return
            
            sum_ += root.val
            if root.left == None and root.right == None:
                if sum_ == target:
                    hassum.append(True)
                return
                
            pathsum(root.left, sum_, target, hassum)
            pathsum(root.right, sum_, target, hassum)
        
        hassum = []
        if root == None:
            return False
        pathsum(root, 0, targetSum, hassum)
        if True in hassum:
            return True
        else:
            return False