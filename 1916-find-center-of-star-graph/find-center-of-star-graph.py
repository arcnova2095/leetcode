class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        res=set()
        
        res.add(edges[0][0])
        res.add(edges[0][1])
        for i in range(1,len(edges)):
            set1= set()
            set1.add(edges[i][0])
            set1.add(edges[i][1])
            res=res.intersection(set1)
        x= list(res)
        return x[0]