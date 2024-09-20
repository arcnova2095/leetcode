class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}

        def dfs(r,c,prev):
            if r not in range(len(matrix)) or c not in range(len(matrix[0])) or matrix[r][c]<= prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            res=max(res,1+dfs(r+1,c,matrix[r][c]), 1+dfs(r-1,c,matrix[r][c]),1+dfs(r,c+1,matrix[r][c]),1+dfs(r,c-1, matrix[r][c])) 
            dp[(r,c)]= res
            return res
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j,-1)
        return max(dp.values())

        