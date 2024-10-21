class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sub=[]
        res=[]
        candidates.sort()
        def dfs(i,total):
            if total==target:
                res.append(sub[:])
                return 
            if i>= len(candidates) or target<total:
                return 
            if target<=0:
                return 
            sub.append(candidates[i])
            dfs(i+1,candidates[i]+total)
            sub.pop()
            while i+1<len(candidates) and candidates[i]== candidates[i+1]:
                i+=1
            dfs(i+1,total)
        dfs(0,0)
        return res


            
            
