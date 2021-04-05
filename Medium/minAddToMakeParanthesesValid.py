# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        
        for i in S:
            if i == "(":
                stack.append(')')
            elif len(stack) == 0 or stack.pop() != i:
                count += 1
        
        size = len(stack)
        if size or count:
            return size + count
        else:
             return count       