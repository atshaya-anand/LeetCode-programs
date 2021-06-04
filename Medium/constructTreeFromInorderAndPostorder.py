# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def build(inorder, postorder, start, end):
            if start > end:
                return None
            
            tNode = TreeNode(postorder[build.postIndex])
            build.postIndex += 1
            
            if start == end:
                return tNode
            
            index = search(inorder, start, end, tNode.val)
            tNode.right = build(inorder, postorder, index+1, end)
            tNode.left = build(inorder, postorder, start, index-1)
            
            return tNode
        
        def search(inorder, start, end, value):
            for i in range(start, end+1):
                if inorder[i] == value:
                    return i
                
        
        postorder = postorder[::-1]
        build.postIndex = 0
        root = build(inorder, postorder, 0, len(inorder)-1)
        return root