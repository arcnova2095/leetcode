class Solution:
    def numSteps(self, val: str) -> int:
        n=0
        s= int(val,2)
        while (s>1):
            if s%2==0:
                s//=2
            else:
                s+=1
            n+=1
        return n
        