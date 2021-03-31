# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum())
        s = s.lower()
        
        j = len(s) - 1
        rev_s = ''
        
        while j >= 0:
            rev_s += s[j]
            j -= 1
        
        if s == rev_s:
            return True