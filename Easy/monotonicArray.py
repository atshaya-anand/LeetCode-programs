# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A)==1:
            return True
        else:
            return A==sorted(A) or A==sorted(A, reverse=True)