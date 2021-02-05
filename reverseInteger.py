# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            x *= -1
            while(x):
                rem = x % 10
                rev = rev * 10 + rem
                x = x//10
            if rev <= 2**31 - 1:
                return rev*-1
            else:
                return 0
        elif x > 0:
            while(x):
                rem = x % 10
                rev = rev * 10 + rem
                x = x//10
            if rev <= 2**31 - 1:
                return rev
            else:
                return 0
        else:
            return 0