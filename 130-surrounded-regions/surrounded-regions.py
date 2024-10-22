class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col= len(board), len(board[0])
        def dfs(i,j):
            if i not in range(row) or j not in range(col) or board[i][j]!="O":
                return 
            board[i][j]="T"
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            

        for r in range(row):
            for c in range(col):
                if board[r][c]=="O" and r in [0,row-1] or c in [0,col-1]:
                    dfs(r,c)
        for r in range(row):
            for c in range(col):       
                if board[r][c]=="O":
                    board[r][c]="X"
        for r in range(row):
            for c in range(col):
                if board[r][c]=="T":
                    board[r][c]="O"
                
        
