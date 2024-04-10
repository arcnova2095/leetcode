class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C= len(heights),len(heights[0])
        atl,pac= set(),set()

        def dfs(r,c,visit,prevheight):
            if r not in range(R) or c not in range(C) or heights[r][c]<prevheight or (r,c) in visit:
                return 
            visit.add((r,c))
            dfs(r + 1, c,visit,heights[r][c]) 
            dfs(r - 1, c,visit,heights[r][c]) 
            dfs(r, c + 1,visit,heights[r][c])
            dfs(r, c - 1,visit,heights[r][c])
        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R - 1, c, atl, heights[R - 1][c])

        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C- 1, atl, heights[r][C - 1])

        res = []
        for r in range(R):
            for c in range(C):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
