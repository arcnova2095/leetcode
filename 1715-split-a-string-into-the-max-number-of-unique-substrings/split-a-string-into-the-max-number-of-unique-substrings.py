class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i,path):
            if i==len(s):
                return 0
            max_split=0

            for j in range(i+1, len(s)+1):
                sub= s[i:j]
                if sub not in path:
                    path.add(sub)
                    max_split= max(max_split,1+dfs(j,path))
                    path.remove(sub)
            return max_split
        return dfs(0,set())    

        