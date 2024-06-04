class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        time=0
        row,col=len(grid),len(grid[0])
        q=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        d= [[0,1],[1,0],[-1,0],[0,-1]]

        while fresh>0 and q:
            for i in range(len(q)):
                r,c= q.popleft()
                for dr,dc in ((d)):
                    rd,cd= r+dr,dc+c 
                    if rd in range(row) and cd in range(col) and grid[rd][cd]==1:
                        grid[rd][cd]=2
                        q.append([rd,cd])
                        fresh-=1
            time+=1

        return time if fresh==0 else -1