class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hmap= {i: [] for i in range(n)}
        for i,j in edges:
            hmap[i].append(j)
            hmap[j].append(i)
        visit=set()
        def dfs(node):
            if node== destination:
                return True
            visit.add(node)
            for i in hmap[node]:
                if i not in visit:
                    if dfs(i):
                        return True
            return False
        return dfs(source)