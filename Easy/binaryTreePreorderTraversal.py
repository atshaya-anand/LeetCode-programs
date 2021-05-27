# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root,list_):
            if root == None:
                return 
            list_.append(root.val)
            preorder(root.left,list_)
            preorder(root.right,list_)
        
        list_ = []
        if root is not None:
            preorder(root,list_)
        return list_