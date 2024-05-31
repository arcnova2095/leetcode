class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res=0
        visited=set()
        row,col= len(grid),len(grid[0])

        def dfs(r,c):
            
            if r not in range(row) or c not in range(col) or (r,c)  in visited or grid[r][c]=="0":
                return 0
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)
        return res

