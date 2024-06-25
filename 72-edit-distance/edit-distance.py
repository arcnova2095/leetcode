class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp={}
        def dfs(i,j):
            if i==len(w1):
                return len(w2)-j
        
            if j==len(w2):
                return len(w1)-i
            if (i,j) in dp:
                return dp[(i,j)]
            
            if w1[i]== w2[j]:
                dp[(i,j)]=dfs(i+1,j+1)
            else:
                dp[(i,j)]= 1+min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))
            return dp[(i,j)]
        return dfs(0,0)
            