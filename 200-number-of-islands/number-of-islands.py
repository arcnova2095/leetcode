class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island=0
        visited= set()
        rows = len(grid)
        col= len(grid[0])
        def bfs(r,c):
            q= deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,cols=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c= row+dr,cols+dc
                    if r in range(rows) and c in range(col) and grid[r][c]=='1' and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
        for r in range(rows):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island
        