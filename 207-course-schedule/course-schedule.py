class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm= {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hm[crs].append(pre)
        path= set()

        def dfs(i):
            if i in path:
                return False
            if hm[i]==[]:
                return True
            path.add(i) 
            for pre in hm[i]:
                if not dfs(pre):
                    return False
            path.remove(i)
            hm[i]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True