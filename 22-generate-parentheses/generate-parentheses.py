class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]

        def back(close,openn):
            if openn==close==n:
                res.append("".join(stack))
                return 
            if openn<n:
                stack.append("(")
                back(close,openn+1)
                stack.pop()
            if close<openn:
                stack.append(")")
                back(close+1,openn)
                stack.pop()
        back(0,0)
        return res