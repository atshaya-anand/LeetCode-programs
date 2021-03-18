# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sumeven = sum(i for i in A if i%2==0)
        for i in queries:
            A[i[1]] += i[0]
            if i[0]%2 == 0 and A[i[1]]%2 == 0:
                sumeven += i[0]
            elif i[0]%2 == 1 and A[i[1]]%2 == 0:
                sumeven += A[i[1]]
            elif i[0]%2 == 1 and A[i[1]]%2 == 1:
                sumeven -= (A[i[1]]-i[0])
            res.append(sumeven)
        return res