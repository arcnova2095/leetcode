class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols= len(grid), len(grid[0])
        visited= set()
        area=0
        def dfs(r,c):
            if (r>=Rows or r<0 or
            c>=Cols or c<0 or
            (r,c) in visited or
            grid[r][c]==0):
                return 0
            visited.add((r,c))
            return 1+ dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            


        for r in range(Rows):
            for c in range(Cols):
                area= max(dfs(r,c), area)
                    
        return area
                    