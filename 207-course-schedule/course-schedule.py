class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm= {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hm[crs].append(pre)
        path= set()
        def dfs(crs):
            if crs in path:
                return False
            if hm[crs]==[]:
                return True
            path.add(crs)
            for i in hm[crs]:
                if not dfs(i):
                    return False
            path.remove(crs)
            hm[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


