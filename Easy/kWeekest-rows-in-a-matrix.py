# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = {}
        for i,v in enumerate(mat):
            count[i]= v.count(1)
        arr = sorted(count, key=count.get, reverse=False)
        return arr[:k]