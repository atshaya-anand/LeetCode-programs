# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numbers = []
        i = 0
        while i < len(s):
            if s[i] == "[":
                stack.append(s[i])
                i += 1
                while i < len(s) and s[i] != "]":
                    if s[i].isnumeric():
                        val = 0
                        while i < len(s) and s[i].isdigit():
                            val = (val * 10) + int(s[i])
                            i += 1
                        numbers.append(val)
                        i -= 1
                    else:
                        stack.append(s[i])
                    i += 1
                continue
            
            elif s[i] == "]":
                val = ''
                while stack[-1] != "[":
                    a = stack.pop()
                    val += a[::-1]
                stack.pop()
                no = numbers.pop()
                stack.append(no * val[::-1])
            
            elif s[i].isnumeric():
                val = 0
                while i < len(s) and s[i].isdigit():
                    val = (val * 10) + int(s[i])
                    i += 1
                numbers.append(val)
                i -= 1
            
            else:
                stack.append(s[i])
            
            i += 1
        
        return ''.join(stack)