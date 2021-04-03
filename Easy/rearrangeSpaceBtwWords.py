# https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        res = text.split()
        words = len(res)
        if words == 1:
            gap = 0
        else:
            gap = spaces // (words - 1)
        
        trailing_spaces = spaces - gap * (words - 1)
        return (' ' * gap).join(res) + ' ' * trailing_spaces 