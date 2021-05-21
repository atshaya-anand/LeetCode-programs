# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1 or n == 0:
            return 0
        primes = [True for i in range(n)]
        p = 2
        while(p * p <= n):
            if primes[p] == True:
                for i in range(p*p, n, p):
                    primes[i] = False
            p += 1
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        return count