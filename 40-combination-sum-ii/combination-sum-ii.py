class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        candidates.sort()
        def dfs(i,target):
            if target==0:
                res.append(sub.copy())
                return 
            if target<=0:
                return 0
            prev=-1
            for i in range(i,len(candidates)):
                if candidates[i]==prev:
                    continue
                sub.append(candidates[i])
                
                dfs(i+1,target - candidates[i])
                
                sub.pop()
                
                prev = candidates[i]
        dfs(0,target)
        return res
