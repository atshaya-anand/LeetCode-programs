# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        
        def path(root, li, target):
            if root:
                li.append(root.val)
                path(root.left, li, target)
                path(root.right, li, target)
                if root.left == None and root.right == None:
                    if sum(li) == target:
                        res.append(li.copy())
                li.pop()
    
        path(root, [], targetSum)
        return res