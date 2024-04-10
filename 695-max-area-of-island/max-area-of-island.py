class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row= len(grid)
        col= len(grid[0])
        res=0
        path=set()
        def dfs(r,c):
            if ( r not in range(row) or c not in range(col) or grid[r][c]==0 or (r,c) in path):
                return 0
            path.add((r,c))
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                    
                res= max(res,dfs(r,c))
        return res
                    