class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row= len(grid)
        col= len(grid[0])
        res=0
        path=set()
        def dfs(r,c):
            if ( r not in range(row) or c not in range(col) or grid[r][c]=="0" or (r,c) in path):
                return 
            path.add((r,c))
            directions=[[0,1],[1,0],[-1,0],[0,-1]]
            for rw,cl in directions:
                dfs(r+rw,c+cl)
        for r in range(row):
            for c in range(col):
                if ((r,c) not in path and grid[r][c]=='1'):
                    res+=1
                    dfs(r,c)
        return res
            
            
            
