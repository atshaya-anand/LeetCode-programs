# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root,list_):
            if root == None:
                return 
            inorder(root.left,list_)
            list_.append(root.val)
            inorder(root.right,list_)
        
        list_ = []
        if root is not None:
            inorder(root,list_)
        return list_