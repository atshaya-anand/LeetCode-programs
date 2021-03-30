# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        res = list(range(n))
        i = 0
        j = n - 1
        
        for k in range(n):
            res[i] = s[j]
            i += 1
            j -= 1
        
        for ss in range(n):
            s[ss] = res[ss]