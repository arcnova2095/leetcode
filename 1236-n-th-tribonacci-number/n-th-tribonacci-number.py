class Solution:
    def tribonacci(self, n: int) -> int:
        def solve(n,t0,t1,t2):
            if n==0:
                return t0
            else:
                n-=1
                return solve(n,t1,t2,t0+t1+t2)
        return solve(n,0,1,1)

    
        
        
        