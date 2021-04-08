# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for i in S:
            if i != '#':
                stack1.append(i)
            elif stack1:
                stack1.pop()
        for i in T:
            if i != '#':
                stack2.append(i)
            elif stack2:
                stack2.pop()
                
        if stack1 == stack2:
            return True