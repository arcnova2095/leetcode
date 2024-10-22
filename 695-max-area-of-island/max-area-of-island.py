class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        row,col=len(grid), len(grid[0])

        path=set()
        def dfs(i,j):
            if i not in range(row) or j not in range(col) or (i,j) in path or grid[i][j]==0:
                return 0 
            path.add((i,j))
            res=1+dfs(i,j+1) +dfs(i+1,j)+ dfs(i,j-1)+dfs(i-1,j)
            return res
        for r in range(row):
            for c in range(col):
                if ((r,c)) not in path and grid[r][c]==1:
                    area= max(area, dfs(r,c))
        return area