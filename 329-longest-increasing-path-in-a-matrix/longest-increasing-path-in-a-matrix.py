class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        def dfs(i,j,preval):
            if i not in range(len(matrix)) or j not in range(len(matrix[0])) or matrix[i][j]<=preval:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res=1
            res= max(res,1+ dfs(i+1,j,matrix[i][j]),1+ dfs(i-1,j,matrix[i][j]),1+ dfs(i,j-1,matrix[i][j]),1+ dfs(i,j+1,matrix[i][j]))
            dp[(i,j)]=res
            return res
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j,-1)
        return max(dp.values())