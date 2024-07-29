class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        sub=""
        digit={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            "0":" "}
        def dfs(i,curr):
            if i>= len(digits):
                res.append(curr)
                return 
            for c in digit[digits[i]]:
                
                dfs(i+1,curr+c)
                
        dfs(0,"")
        return res if digits else []
        
        