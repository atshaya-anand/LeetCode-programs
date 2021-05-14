# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] != ' ' and i == len(s) - 1:
                stack.append(s[i])
                while stack:
                    res += stack.pop()
            elif s[i] == ' ':
                while stack:
                    res += stack.pop()
                res += ' '
            else:
                stack.append(s[i])
        return res