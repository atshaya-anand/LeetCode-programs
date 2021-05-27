# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root,list_):
            if root == None:
                return
            postorder(root.left,list_)
            postorder(root.right,list_)
            list_.append(root.val)
        
        list_ = []
        if root is not None:
            postorder(root,list_)
        return list_