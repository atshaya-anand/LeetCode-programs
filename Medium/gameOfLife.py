# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        
        mapping = {0:0,1:1,-2:0,-1:1}
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for i in range(0,m):
            for j in range(0,n):
                count = 0
                for a,b in dirs:
                    if -1 < i + a < m and -1 < j + b < n:
                        if board[i+a][j+b] == 1 or board[i+a][j+b] == -2:
                            count += 1
                
                if board[i][j]:
                    if count < 2:
                        board[i][j] = -2
                    elif count > 3:
                        board[i][j] = -2
                else:
                    if count == 3:
                        board[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = mapping[board[i][j]]