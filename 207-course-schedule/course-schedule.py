class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        hm={i:[] for i in range(n)}

        for i, j in p:
            hm[i].append(j)
        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            if hm[crs]==[]:
                return True
            visit.add(crs)
            for i in hm[crs]:
            
                if not dfs(i):
                    return False
            visit.remove(crs)
            hm[crs]=[]
            return True
        for c in range(n):
            if not dfs(c):
                return False
        return True


