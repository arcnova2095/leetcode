class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time=0,0
        q= deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        d=[[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh:
            for i in range(len(q)):
                r,c= q.popleft()
                for dr,dc in d:
                    row,col= r+dr,c+dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1:
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1  

                

    