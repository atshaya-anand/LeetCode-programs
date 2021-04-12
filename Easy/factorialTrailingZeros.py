# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            fact = 1
            for i in range(1,n+1):
                fact *= i
            return fact
        if n == 0:
            return 0
        fac = factorial(n)
        count = 0
        while fac:
            rem = fac % 10
            if rem:
                break
            else:
                count += 1
            fac = fac // 10
        return count