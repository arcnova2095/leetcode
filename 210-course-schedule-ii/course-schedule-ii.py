class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hm[i].append(j)
        visit= set()
        cycle= set()
        out=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for p in hm[crs]:
                if  dfs(p)== False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            out.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return out
