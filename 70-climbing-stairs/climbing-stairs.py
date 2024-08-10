class Solution:
    def climbStairs(self, n: int) -> int:
        o,t=1,1
        for i in range(n-1):
            temp= o+t
            o=t
            t=temp
        return t