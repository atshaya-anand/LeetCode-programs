# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(inorder, preorder, start, end):
            if start > end:
                return None
            
            tNode = TreeNode(preorder[build.preIndex])
            build.preIndex += 1
            
            if start == end:
                return tNode
            
            index = search(inorder, start, end, tNode.val)
            
            tNode.left = build(inorder, preorder, start, index-1)
            tNode.right = build(inorder, preorder, index+1, end)
            
            return tNode
            
        def search(inorder, start, end, value):
            for i in range(start, end+1):
                if inorder[i] == value:
                    return i
        
        build.preIndex = 0
        root = build(inorder, preorder, 0, len(inorder)-1)
        return root