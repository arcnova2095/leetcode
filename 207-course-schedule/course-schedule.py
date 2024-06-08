class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        hm= {i: [] for i in range(n)}

        for crs, pre in p:
            hm[crs].append(pre)
        visit= set()

        def dfs(crs):
            if crs in visit:
                return False
            if hm[crs]==[]:
                return True
            visit.add(crs)

            for pre in hm[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            hm[crs]=[]
            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True


