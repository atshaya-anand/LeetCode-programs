# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for v in s:
            if stack and stack[-1][0]==v:
               val = stack.pop()
               val[1] +=1
               stack.append(val)
            else:
                stack.append([v,1])
            
            if stack[-1][1]==k:
                stack.pop()
        return "".join(v[0]*v[1] for v in stack)