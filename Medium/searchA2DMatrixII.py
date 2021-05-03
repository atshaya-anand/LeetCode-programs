# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(arr,start,end):
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    return True
                elif target < arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
        
        i = 0
        while i < len(matrix):
            if binarySearch(matrix[i],0,len(matrix[i])-1):
                return True
            else:
                i += 1