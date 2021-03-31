# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev_x = ''
        
        l = len(x) - 1
        while l >= 0:
            rev_x += x[l]
            l -= 1
        
        if x == rev_x:
            return True