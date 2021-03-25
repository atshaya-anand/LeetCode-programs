# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a = 0
            b = 1
            for i in range(1,n):
                c = a + b
                a = b
                b = c
            return c