# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = ""
        while n > 0:
            if n % 2 == 0:
                bit = '0' + bit
            else:
                bit = '1' + bit
            n = n >> 1
        
        return bit.count('1')