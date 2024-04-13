class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time=0,0
        ROW,COL= len(grid), len(grid[0])
        q= deque()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]== 2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        
        while q and fresh>0:
            direct=[[0,1],[0,-1],[1,0],[-1,0]]
            for i in range(len(q)):
                r,c= q.popleft()
                for rc,cc in direct:
                    row,col= r+rc, c+cc
                    if row not in range(ROW) or col not in range(COL) or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    
                    q.append([row,col])
                    fresh-=1
            time+=1
        
        return time if fresh==0 else -1
                