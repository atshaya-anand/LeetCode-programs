# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for i in matrix:
            for j in i:
                array.append(j)
        array.sort()
        #print(array)
        start = 1
        end = len(array)
        while start <= end:
            mid = (start + end)//2
            if mid == k:
                return array[mid-1]
            elif mid < k:
                start = mid + 1
            else:
                end = mid - 1