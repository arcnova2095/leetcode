class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs(i, total):
            if total==target:
                res.append(sub.copy())
                return 
            if len(candidates)<= i or target<total:
                return 
            sub.append(candidates[i])
            dfs(i, total+candidates[i])
            sub.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res