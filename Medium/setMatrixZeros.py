# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        dir_ = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dir_.append((i,j))
        
        for a,b in dir_:
            for i in range(n):
                matrix[a][i] = 0
            for j in range(m):
                matrix[j][b] = 0