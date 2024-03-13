class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
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
        def back(i,currstr):
            if (len(digits)== len(currstr)):
                res.append(currstr)
                return
            for c in digit[digits[i]]:
                back(i+1,currstr+c)
        if digits:
            back(0, "")

        return res
            
        
        