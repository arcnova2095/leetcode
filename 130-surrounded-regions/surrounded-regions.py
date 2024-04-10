from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        row, col = len(board), len(board[0])
        
        
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and board[r][c] == 'O':
                board[r][c] = 'T'  
                
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
       
        for r in range(row):
            for c in [0, col - 1]: 
                if board[r][c] == 'O':
                    dfs(r, c)
        for c in range(col):
            for r in [0, row - 1]:  
                if board[r][c] == 'O':
                    dfs(r, c)
        
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  
                elif board[r][c] == 'T':
                    board[r][c] = 'O' 
