# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))
        n = n.split('b')
        l = len(n[1])
        d = 32 - l
        n = n[1][::-1]
        for i in range(d):
            n += '0'
        return int(n,2)