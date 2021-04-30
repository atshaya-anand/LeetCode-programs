# https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        l = len(n)
        if l <= 3:
            return n
        nstr = n[::-1]
        num = ''
        i = 0
        while i < l:
            if i % 3 == 0 and i != 0:
                num += '.'
            num += nstr[i]
            i += 1
        return num[::-1]