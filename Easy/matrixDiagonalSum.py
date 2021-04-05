# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumOfDiagonals = 0
        count = len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j:
                    sumOfDiagonals += mat[i][j]
                elif i + j == len(mat) - 1:
                    sumOfDiagonals += mat[i][j]
        return sumOfDiagonals