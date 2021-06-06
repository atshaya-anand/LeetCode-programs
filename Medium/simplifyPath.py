# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)
        
        while i < n:
            val = ''
            if path[i] != "/":
                while i < n and path[i] != "/":
                    val += path[i]
                    i += 1
                if val != "." and val != "":
                    if stack and val == "..":
                        stack.pop()
                    elif val != "..":
                        stack.append(val)
                
            i += 1
        
        res = "/"
        for i in range(0,len(stack)):
            if i == len(stack) - 1:
                res += stack[i]
            else:
                res = res + stack[i] + "/"
        
        return res