class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        visit= set()
        row,col= len(grid), len(grid[0])

        def dfs(r,c):
            if r not in range(row) or c not in range(col) or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            return 1+ dfs(r+1,c)+ dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        
        for r in range(row):
            for c in range(col):
                res= max(dfs(r,c),res)
        return res
            

    
