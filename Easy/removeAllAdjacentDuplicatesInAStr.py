# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                val = stack[-1]
                if i == val:
                    stack.pop()
                    continue
                else:
                    stack.append(i)
                    continue
            stack.append(i)
        return ''.join(stack)